"""
Stock-related API endpoints.
14 routes: /api/stocks, /api/stock/<symbol>/*, search, categories, compatibility endpoints.
"""

from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta

from api.helpers import query_db

stocks_bp = Blueprint('stocks', __name__)


@stocks_bp.route('/api/stocks', methods=['GET'])
def get_stocks():
    """Get all stocks"""
    stocks = query_db("""
        SELECT id, symbol, name, exchange, sector, category, market_cap, is_active
        FROM stocks
        WHERE is_active = TRUE
        ORDER BY symbol;
    """)

    return jsonify({
        "success": True,
        "stocks": stocks,
        "total": len(stocks)
    })


@stocks_bp.route('/api/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    """Get single stock by symbol"""
    stock = query_db("""
        SELECT * FROM stocks WHERE symbol = %s;
    """, (symbol,), one=True)

    if stock:
        return jsonify({"success": True, **stock})
    else:
        return jsonify({"success": False, "error": "Stock not found"}), 404


@stocks_bp.route('/api/stock/<symbol>/current', methods=['GET'])
def get_stock_current_price(symbol):
    """Get current price for a stock"""
    data = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.date,
            sp.open,
            sp.high,
            sp.low,
            sp.close as price,
            sp.volume,
            (sp.close - sp.open) as change,
            sp.change_percent
        FROM stocks s
        JOIN stock_prices sp ON s.id = sp.stock_id
        WHERE s.symbol = %s
        ORDER BY sp.date DESC
        LIMIT 1;
    """, (symbol,), one=True)

    if data:
        return jsonify({"success": True, **data})
    else:
        return jsonify({"success": False, "error": "No price data found"}), 404


@stocks_bp.route('/api/stock/<symbol>/history', methods=['GET'])
def get_stock_history(symbol):
    """Get historical prices for a stock"""
    days = request.args.get('days', default=30, type=int)
    date_from = (datetime.now() - timedelta(days=days)).date()

    history = query_db("""
        SELECT
            sp.date,
            sp.open,
            sp.high,
            sp.low,
            sp.close,
            sp.volume,
            (sp.close - sp.open) as change,
            sp.change_percent
        FROM stocks s
        JOIN stock_prices sp ON s.id = sp.stock_id
        WHERE s.symbol = %s AND sp.date >= %s
        ORDER BY sp.date ASC;
    """, (symbol, date_from))

    return jsonify({
        "success": True,
        "symbol": symbol,
        "data": history,
        "count": len(history)
    })


@stocks_bp.route('/api/latest-prices', methods=['GET'])
def get_latest_prices():
    """Get latest prices for all stocks"""
    limit = request.args.get('limit', default=100, type=int)

    prices = query_db("""
        SELECT
            s.symbol,
            s.name,
            s.exchange,
            sp.date,
            sp.close as price,
            (sp.close - sp.open) as change,
            sp.change_percent,
            sp.volume
        FROM stocks s
        JOIN LATERAL (
            SELECT * FROM stock_prices
            WHERE stock_id = s.id
            ORDER BY date DESC
            LIMIT 1
        ) sp ON TRUE
        WHERE s.is_active = TRUE
        ORDER BY s.symbol
        LIMIT %s;
    """, (limit,))

    return jsonify({
        "success": True,
        "prices": prices,
        "total": len(prices),
        "timestamp": datetime.now().isoformat()
    })


@stocks_bp.route('/api/latest', methods=['GET'])
def get_latest():
    """Get latest data for all stocks (compatibility endpoint for dashboard_history.html)"""
    prices = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.date,
            sp.open,
            sp.high,
            sp.low,
            sp.close,
            sp.volume,
            sp.change_percent,
            (sp.close - sp.open) as change
        FROM stocks s
        JOIN LATERAL (
            SELECT * FROM stock_prices
            WHERE stock_id = s.id
            ORDER BY date DESC
            LIMIT 1
        ) sp ON TRUE
        WHERE s.is_active = TRUE
        ORDER BY s.symbol;
    """)

    # Format as {all_results: {SYMBOL: data}} for dashboard_history.html compatibility
    all_results = {}
    for row in prices:
        symbol = row['symbol']
        all_results[symbol] = {
            'symbol': symbol,
            'name': row['name'],
            'date': row['date'].isoformat() if row['date'] else '',
            'open': float(row['open']) if row['open'] else 0,
            'high': float(row['high']) if row['high'] else 0,
            'low': float(row['low']) if row['low'] else 0,
            'close': float(row['close']) if row['close'] else 0,
            'price': float(row['close']) if row['close'] else 0,
            'volume': int(row['volume']) if row['volume'] else 0,
            'change': float(row['change']) if row['change'] else 0,
            'change_percent': float(row['change_percent']) if row['change_percent'] else 0
        }

    return jsonify({
        'success': True,
        'all_results': all_results,
        'total': len(all_results),
        'timestamp': datetime.now().isoformat()
    })


@stocks_bp.route('/api/top-gainers', methods=['GET'])
def get_top_gainers():
    """Get top gaining stocks"""
    limit = request.args.get('limit', default=10, type=int)

    gainers = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.close as price,
            (sp.close - sp.open) as change,
            sp.change_percent,
            sp.volume
        FROM stocks s
        JOIN LATERAL (
            SELECT * FROM stock_prices
            WHERE stock_id = s.id
            ORDER BY date DESC
            LIMIT 1
        ) sp ON TRUE
        WHERE s.is_active = TRUE AND sp.change_percent IS NOT NULL
        ORDER BY sp.change_percent DESC
        LIMIT %s;
    """, (limit,))

    return jsonify({
        "success": True,
        "gainers": gainers
    })


@stocks_bp.route('/api/top-losers', methods=['GET'])
def get_top_losers():
    """Get top losing stocks"""
    limit = request.args.get('limit', default=10, type=int)

    losers = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.close as price,
            (sp.close - sp.open) as change,
            sp.change_percent,
            sp.volume
        FROM stocks s
        JOIN LATERAL (
            SELECT * FROM stock_prices
            WHERE stock_id = s.id
            ORDER BY date DESC
            LIMIT 1
        ) sp ON TRUE
        WHERE s.is_active = TRUE AND sp.change_percent IS NOT NULL
        ORDER BY sp.change_percent ASC
        LIMIT %s;
    """, (limit,))

    return jsonify({
        "success": True,
        "losers": losers
    })


@stocks_bp.route('/api/most-active', methods=['GET'])
def get_most_active():
    """Get most active stocks by volume"""
    limit = request.args.get('limit', default=10, type=int)

    most_active = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.close as price,
            sp.change_percent,
            sp.volume
        FROM stocks s
        JOIN LATERAL (
            SELECT * FROM stock_prices
            WHERE stock_id = s.id
            ORDER BY date DESC
            LIMIT 1
        ) sp ON TRUE
        WHERE s.is_active = TRUE
        ORDER BY sp.volume DESC
        LIMIT %s;
    """, (limit,))

    return jsonify({
        "success": True,
        "most_active": most_active
    })


@stocks_bp.route('/api/search', methods=['GET'])
def search_stocks():
    """Search stocks by symbol or name"""
    query = request.args.get('q', '').strip()

    if not query:
        return jsonify({"success": False, "error": "Query parameter 'q' is required"}), 400

    stocks = query_db("""
        SELECT symbol, name, exchange, sector
        FROM stocks
        WHERE (symbol ILIKE %s OR name ILIKE %s) AND is_active = TRUE
        ORDER BY
            CASE WHEN symbol ILIKE %s THEN 1 ELSE 2 END,
            symbol
        LIMIT 20;
    """, (f'%{query}%', f'%{query}%', f'{query}%'))

    return jsonify({
        "success": True,
        "query": query,
        "results": stocks,
        "total": len(stocks)
    })


# ============================================================
# COMPATIBILITY ENDPOINTS (for frontend expecting JSON files)
# ============================================================

@stocks_bp.route('/data/<symbol>_current.json', methods=['GET'])
def get_current_json(symbol):
    """Get current price in JSON file format (compatibility endpoint)"""
    data = query_db("""
        SELECT
            s.symbol,
            sp.close as price,
            (sp.close - sp.open) as change,
            sp.change_percent,
            sp.volume,
            sp.high,
            sp.low,
            sp.open,
            sp.date as timestamp
        FROM stocks s
        JOIN stock_prices sp ON s.id = sp.stock_id
        WHERE s.symbol = %s
        ORDER BY sp.date DESC
        LIMIT 1;
    """, (symbol.upper(),), one=True)

    if data:
        # Format to match old JSON structure
        result = {
            "symbol": data['symbol'],
            "price": float(data['price']) if data['price'] else 0,
            "change": float(data['change']) if data['change'] else 0,
            "change_percent": float(data['change_percent']) if data['change_percent'] else 0,
            "volume": int(data['volume']) if data['volume'] else 0,
            "high": float(data['high']) if data['high'] else 0,
            "low": float(data['low']) if data['low'] else 0,
            "open": float(data['open']) if data['open'] else 0,
            "timestamp": data['timestamp'].isoformat() if data['timestamp'] else datetime.now().isoformat(),
            "source": "PostgreSQL"
        }
        return jsonify(result)
    else:
        return jsonify({"error": f"No data for {symbol}"}), 404


@stocks_bp.route('/data/<symbol>_history.json', methods=['GET'])
def get_history_json(symbol):
    """Get historical prices in JSON file format (compatibility endpoint)"""
    history = query_db("""
        SELECT
            date,
            open,
            high,
            low,
            close,
            volume,
            change,
            change_percent
        FROM stocks s
        JOIN stock_prices sp ON s.id = sp.stock_id
        WHERE s.symbol = %s
        ORDER BY date ASC;
    """, (symbol.upper(),))

    if history:
        # Format to match old JSON structure
        result = []
        for row in history:
            result.append({
                "date": row['date'].isoformat() if row['date'] else '',
                "open": float(row['open']) if row['open'] else 0,
                "high": float(row['high']) if row['high'] else 0,
                "low": float(row['low']) if row['low'] else 0,
                "close": float(row['close']) if row['close'] else 0,
                "price": float(row['close']) if row['close'] else 0,  # alias
                "volume": int(row['volume']) if row['volume'] else 0,
                "change": float(row['change']) if row['change'] else 0,
                "change_percent": float(row['change_percent']) if row['change_percent'] else 0
            })
        return jsonify(result)
    else:
        return jsonify([])


@stocks_bp.route('/api/stock-names', methods=['GET'])
@stocks_bp.route('/stock_names.json', methods=['GET'])
def get_stock_names():
    """Get stock symbol to name mappings"""
    stocks = query_db("""
        SELECT symbol, name
        FROM stocks
        WHERE is_active = TRUE
        ORDER BY symbol;
    """)

    # Convert to {symbol: name} dict
    result = {stock['symbol']: stock['name'] for stock in stocks}
    return jsonify(result)


@stocks_bp.route('/api/stock-categories', methods=['GET'])
def get_stock_categories():
    """Get stock categories organized by sector"""
    stocks = query_db("""
        SELECT symbol, sector, category, exchange
        FROM stocks
        WHERE is_active = TRUE
        ORDER BY symbol;
    """)

    # Build categories dynamically from database
    categories = {
        'commodities': [],
        'blue_chips': [],
        'banks': [],
        'real_estate': [],
        'tech': [],
        'consumer': [],
        'oil_gas': [],
        'affordable': [],
        'industrial': [],
        'transportation': [],
        'utilities': [],
        'all': []
    }

    for stock in stocks:
        symbol = stock['symbol']
        sector = (stock['sector'] or '').lower()
        category = (stock['category'] or '').lower()

        # Categorize based on sector
        if 'bank' in sector or 'financial' in sector:
            categories['banks'].append(symbol)
        if 'real estate' in sector or 'property' in sector:
            categories['real_estate'].append(symbol)
        if 'tech' in sector or 'it' in sector:
            categories['tech'].append(symbol)
        if 'consumer' in sector or 'retail' in sector:
            categories['consumer'].append(symbol)
        if 'oil' in sector or 'gas' in sector or 'energy' in sector:
            categories['oil_gas'].append(symbol)
        if 'industrial' in sector or 'materials' in sector or 'manufacturing' in sector:
            categories['industrial'].append(symbol)
        if 'transport' in sector or 'aviation' in sector or 'logistics' in sector:
            categories['transportation'].append(symbol)
        if 'utilities' in sector or 'power' in sector or 'electricity' in sector:
            categories['utilities'].append(symbol)

        # Commodities
        if 'COPPER' in symbol or 'GOLD' in symbol or 'SILVER' in symbol:
            categories['commodities'].append(symbol)

        # Blue chips (major stocks with high market cap)
        if category == 'large_cap' or symbol in ['VNM', 'VIC', 'VCB', 'FPT', 'HPG', 'GAS', 'MSN', 'VHM', 'TCB', 'VRE', 'MWG', 'PLX', 'VPB', 'BID', 'CTG', 'POW', 'SAB', 'MBB', 'ACB', 'SSI']:
            categories['blue_chips'].append(symbol)

    # Remove duplicates and sort
    for key in categories:
        categories[key] = sorted(list(set(categories[key])))

    # Build 'all' category (all stocks)
    all_symbols = [stock['symbol'] for stock in stocks]
    categories['all'] = sorted(list(set(all_symbols)))

    return jsonify({
        'success': True,
        'categories': categories,
        'total': len(categories['all'])
    })
