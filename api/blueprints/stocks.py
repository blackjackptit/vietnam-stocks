"""
Stock-related API endpoints.
14 routes: /api/stocks, /api/stock/<symbol>/*, search, categories, compatibility endpoints.
"""

import logging
from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta

from api.helpers import query_db

logger = logging.getLogger(__name__)

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
    """Get historical prices for a stock

    Args:
        symbol: Stock symbol (from URL path)
        days: Number of days of history to fetch (query param, default=30, max=365)

    Returns:
        JSON with historical price data
    """
    days = request.args.get('days', default=30, type=int)

    # Validate days parameter
    if days < 1:
        logger.warning(f"Invalid days parameter: {days} (must be >= 1)")
        return jsonify({
            'success': False,
            'error': 'Days parameter must be at least 1'
        }), 400

    if days > 365:
        logger.warning(f"Days parameter {days} exceeds maximum (365), capping to 365")
        days = 365  # Cap to 1 year maximum

    date_from = (datetime.now() - timedelta(days=days)).date()

    try:
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

        logger.debug(f"Retrieved {len(history)} days of history for {symbol}")
        return jsonify({
            "success": True,
            "symbol": symbol,
            "data": history,
            "count": len(history)
        })
    except Exception as e:
        logger.error(f"Error fetching history for {symbol}: {e}", exc_info=True)
        return jsonify({
            'success': False,
            'error': f'Failed to fetch historical data for {symbol}'
        }), 500


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


def _compute_technical_analysis(symbol, historical_data):
    """Compute technical analysis and signals for a stock"""
    if not historical_data or len(historical_data) < 5:
        return {
            'score': 0,
            'recommendation': 'HOLD',
            'emoji': '⚪',
            'signals': [],
            'indicators': {}
        }

    prices = [float(h['close']) for h in historical_data]
    signals = []
    score = 0

    # 1. Detect support levels (local minima)
    support_found = False
    for i in range(2, len(prices) - 2):
        if prices[i] < prices[i-1] and prices[i] < prices[i+1] and \
           prices[i] < prices[i-2] and prices[i] < prices[i+2]:
            signals.append(f"🟢 Support Level at {prices[i]:.0f}")
            support_found = True
            score += 15
            break

    # 2. Detect resistance levels (local maxima)
    resistance_found = False
    for i in range(2, len(prices) - 2):
        if prices[i] > prices[i-1] and prices[i] > prices[i+1] and \
           prices[i] > prices[i-2] and prices[i] > prices[i+2]:
            signals.append(f"🔴 Resistance Level at {prices[i]:.0f}")
            resistance_found = True
            score -= 15
            break

    # 3. Detect trend direction (last 3+ price movements)
    recent_uptrend = 0
    recent_downtrend = 0
    for i in range(len(prices) - 1, max(len(prices) - 5, 0), -1):
        if i > 0:
            if float(prices[i]) > float(prices[i-1]):
                recent_uptrend += 1
                recent_downtrend = 0
            else:
                recent_downtrend += 1
                recent_uptrend = 0

    if recent_uptrend >= 3:
        signals.append("🟢 Recent Uptrend Detected")
        score += 20
    elif recent_downtrend >= 3:
        signals.append("🔴 Recent Downtrend Detected")
        score -= 20

    # 4. Detect volatility
    returns = []
    for i in range(1, len(prices)):
        # Convert to float to handle decimal.Decimal from database
        price_i = float(prices[i])
        price_i_1 = float(prices[i-1])
        if price_i_1 != 0:
            returns.append(abs((price_i - price_i_1) / price_i_1))

    if returns:
        avg_return = float(sum(returns) / len(returns))
        recent_return = float(returns[-1])
        if recent_return > avg_return * 1.5:
            if float(prices[-1]) > float(prices[-2]):
                signals.append("🟢 High Volatility with Upward Movement")
                score += 10
            else:
                signals.append("🔴 High Volatility with Downward Movement")
                score -= 10

    # 5. Volume trend (if we have the data)
    if len(historical_data) >= 2:
        recent_vol = historical_data[-1].get('volume', 0)
        prev_vol = historical_data[-2].get('volume', 0)
        if prev_vol > 0 and recent_vol > prev_vol * 1.2:
            signals.append("🟢 Volume Spike Detected")
            score += 5

    # Determine recommendation based on score
    if score > 20:
        recommendation = 'BUY'
        emoji = '🟢'
    elif score < -20:
        recommendation = 'SELL'
        emoji = '🔴'
    else:
        recommendation = 'HOLD'
        emoji = '⚪'

    return {
        'score': score,
        'recommendation': recommendation,
        'emoji': emoji,
        'signals': signals,
        'indicators': {
            'support_level': min(prices) if support_found else None,
            'resistance_level': max(prices) if resistance_found else None
        }
    }


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
            'change_percent': float(row['change_percent']) if row['change_percent'] else 0,
            'analysis': {}  # Empty analysis - use /api/stock-analysis endpoint
        }

    return jsonify({
        'success': True,
        'all_results': all_results,
        'total': len(all_results),
        'timestamp': datetime.now().isoformat()
    })


@stocks_bp.route('/api/stock-analysis/<symbol>', methods=['GET'])
def get_stock_analysis(symbol):
    """Get technical analysis for a specific stock"""
    try:
        # Get historical data for the stock (last 60 days)
        historical = query_db("""
            SELECT
                date,
                open,
                high,
                low,
                close,
                volume
            FROM stock_prices
            WHERE stock_id = (SELECT id FROM stocks WHERE symbol = %s)
            ORDER BY date DESC
            LIMIT 60
        """, (symbol.upper(),))

        if not historical:
            return jsonify({
                'success': False,
                'error': f'No data found for {symbol}'
            }), 404

        # Reverse to get chronological order
        historical = list(reversed(historical))

        # Compute technical analysis
        analysis = _compute_technical_analysis(symbol, historical)

        return jsonify({
            'success': True,
            'symbol': symbol,
            'analysis': analysis
        })
    except Exception as e:
        logger.error(f"Error computing analysis for {symbol}: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


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
        AND symbol !~ '^[0-9]'  -- Exclude bonds/certificates
        AND LENGTH(symbol) <= 5  -- Real stocks have 3-5 chars
        ORDER BY symbol;
    """)

    # Hardcoded category memberships (fallback when sector/category data missing)
    BLUE_CHIPS = {'VCB', 'VHM', 'VIC', 'VNM', 'HPG', 'GAS', 'MSN', 'TCB', 'VPB', 'MBB', 'BID', 'CTG', 'VRE', 'SAB', 'PLX', 'MWG', 'SSI', 'FPT', 'VJC', 'GVR', 'POW', 'VCI', 'NVL', 'HDB', 'TPB', 'HVN', 'PVD'}
    BANKS = {'VCB', 'TCB', 'MBB', 'VPB', 'CTG', 'BID', 'ACB', 'STB', 'HDB', 'TPB', 'VIB', 'MSB', 'SHB', 'EIB', 'LPB', 'OCB', 'VAB', 'VBB', 'BAB', 'BVB', 'NVB', 'PGB', 'SGB', 'ABB', 'NAB'}
    REAL_ESTATE = {'VHM', 'VIC', 'NVL', 'PDR', 'DXG', 'KDH', 'BCM', 'DIG', 'HDG', 'NLG', 'DXS', 'SCR', 'CEO', 'HDC', 'LDG', 'QCG', 'TCH', 'TDH', 'AGG', 'CII', 'HQC', 'IDC', 'IJC', 'KBC', 'LHG', 'NBB', 'NTL', 'OGC', 'PPI', 'SZL', 'TDC', 'TIX', 'VCG', 'VPI', 'VRE', 'ASM', 'C32', 'CCL', 'CTD', 'DPR', 'FCN', 'HUT', 'ITA', 'LCG', 'NHA', 'PIT', 'PTL', 'SJS', 'TDM', 'THG', 'UIC'}
    TECH = {'FPT', 'CMG', 'VGI', 'SAM', 'ITD', 'ELC', 'SGT', 'ICT', 'DGW', 'CTR', 'FOX', 'VNT', 'SHI', 'SVT', 'ONE', 'VTP', 'SGN', 'CMX', 'TTN', 'NET', 'ITC', 'SCS', 'MMC', 'TDG', 'STG', 'VIT', 'DAG', 'AST', 'ALT', 'PTI', 'TEG'}
    CONSUMER = {'VNM', 'MSN', 'MWG', 'PNJ', 'SAB', 'VHC', 'DGC', 'KDC', 'FRT', 'DBC', 'MCH', 'VCF', 'QNS', 'BBC', 'VGC', 'ASP', 'SAV', 'ANV', 'ACL', 'DRC', 'TRI', 'VTO', 'HNG', 'VNE', 'TLG', 'PAN', 'LAF', 'SBT', 'TAC', 'TCM', 'VFG', 'AGF', 'HAG', 'SJD', 'CHP', 'VHG', 'KLF', 'HT1', 'SRC'}
    OIL_GAS = {'GAS', 'PLX', 'PVD', 'PVS', 'PVT', 'PVB', 'PVG', 'PVC', 'PVX', 'BSR', 'OIL', 'PVE', 'PVA', 'PVO', 'PCT', 'CNG', 'GEG', 'PTB', 'PTC'}
    AFFORDABLE = {'VPB', 'STB', 'HDB', 'SHB', 'MBB', 'ACB', 'FPT', 'POW', 'DGC', 'GEX', 'MSB', 'VIB', 'TPB', 'OCB', 'LPB', 'EIB', 'VCI', 'SHS', 'AGR', 'AAM', 'DCM', 'DPM', 'DGW', 'PVT', 'BMI', 'BMP', 'CMG', 'PHR', 'DBD', 'NT2', 'REE', 'VSH', 'BWE', 'TNG', 'QCG', 'HVN', 'VJC', 'PAN', 'GMD', 'VCS'}
    INDUSTRIAL = {'HPG', 'HSG', 'NKG', 'VCS', 'TVN', 'DTL', 'TLH', 'VGS', 'HT1', 'TIS', 'VIS', 'DGW', 'TMP', 'POM', 'TRA', 'AAA', 'AAT', 'CSV', 'KSB', 'SBT', 'FIT', 'PHR', 'DCM', 'DPM', 'BMP', 'DGC', 'DDG', 'BMI', 'HMC', 'C32', 'LBM', 'VGC'}
    TRANSPORTATION = {'VJC', 'HVN', 'VTP', 'VSC', 'GMD', 'VOS', 'HAH', 'PHP', 'SCS', 'VST', 'TCL', 'VFC', 'SFI', 'TMS', 'DVP', 'PJT', 'ACV', 'STG', 'VTO', 'MWG'}
    UTILITIES = {'POW', 'GAS', 'NT2', 'REE', 'PC1', 'PPC', 'VSH', 'BWE', 'SBA', 'TNG', 'HND', 'TBC', 'HJS', 'SJD', 'SJE'}

    # Build categories
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

        # Commodities
        if 'COPPER' in symbol or 'GOLD' in symbol or 'SILVER' in symbol:
            categories['commodities'].append(symbol)

        # Use hardcoded categories
        if symbol in BLUE_CHIPS:
            categories['blue_chips'].append(symbol)
        if symbol in BANKS:
            categories['banks'].append(symbol)
        if symbol in REAL_ESTATE:
            categories['real_estate'].append(symbol)
        if symbol in TECH:
            categories['tech'].append(symbol)
        if symbol in CONSUMER:
            categories['consumer'].append(symbol)
        if symbol in OIL_GAS:
            categories['oil_gas'].append(symbol)
        if symbol in AFFORDABLE:
            categories['affordable'].append(symbol)
        if symbol in INDUSTRIAL:
            categories['industrial'].append(symbol)
        if symbol in TRANSPORTATION:
            categories['transportation'].append(symbol)
        if symbol in UTILITIES:
            categories['utilities'].append(symbol)

    # Remove duplicates and sort
    for key in categories:
        categories[key] = sorted(list(set(categories[key])))

    # Build 'all' category (excluding commodities, real stocks only)
    all_symbols = [stock['symbol'] for stock in stocks if 'COPPER' not in stock['symbol'] and 'GOLD' not in stock['symbol'] and 'SILVER' not in stock['symbol']]
    categories['all'] = sorted(list(set(all_symbols)))

    return jsonify({
        'success': True,
        'categories': categories,
        'total': len(categories['all']),
        'total_stocks': len(categories['all'])
    })
