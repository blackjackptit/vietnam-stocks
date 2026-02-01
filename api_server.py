#!/usr/bin/env python3
"""
Vietnamese Stock Analytics API Server
Serves stock data from PostgreSQL database
"""

from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
from pathlib import Path
from config import get_database_pool, API_SERVER, CORS_ORIGINS

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/*": {"origins": CORS_ORIGINS}})

# Create database connection pool at startup
db_pool = get_database_pool()


def query_db(query, args=(), one=False):
    """Execute query and return results"""
    conn = db_pool.getconn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, args)
            if one:
                return cursor.fetchone()
            return cursor.fetchall()
    finally:
        db_pool.putconn(conn)


# ============================================================
# STOCK ENDPOINTS
# ============================================================

@app.route('/api/stocks', methods=['GET'])
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


@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    """Get single stock by symbol"""
    stock = query_db("""
        SELECT * FROM stocks WHERE symbol = %s;
    """, (symbol,), one=True)

    if stock:
        return jsonify({"success": True, **stock})
    else:
        return jsonify({"success": False, "error": "Stock not found"}), 404


@app.route('/api/stock/<symbol>/current', methods=['GET'])
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
            sp.change,
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


@app.route('/api/stock/<symbol>/history', methods=['GET'])
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
            sp.change,
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


@app.route('/api/latest-prices', methods=['GET'])
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
            sp.change,
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


@app.route('/api/latest', methods=['GET'])
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
            sp.change,
            sp.change_percent
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


@app.route('/api/top-gainers', methods=['GET'])
def get_top_gainers():
    """Get top gaining stocks"""
    limit = request.args.get('limit', default=10, type=int)

    gainers = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.close as price,
            sp.change,
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


@app.route('/api/top-losers', methods=['GET'])
def get_top_losers():
    """Get top losing stocks"""
    limit = request.args.get('limit', default=10, type=int)

    losers = query_db("""
        SELECT
            s.symbol,
            s.name,
            sp.close as price,
            sp.change,
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


@app.route('/api/most-active', methods=['GET'])
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


@app.route('/api/search', methods=['GET'])
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

@app.route('/data/<symbol>_current.json', methods=['GET'])
def get_current_json(symbol):
    """Get current price in JSON file format (compatibility endpoint)"""
    data = query_db("""
        SELECT
            s.symbol,
            sp.close as price,
            sp.change,
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


@app.route('/data/<symbol>_history.json', methods=['GET'])
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


@app.route('/api/stock-names', methods=['GET'])
@app.route('/stock_names.json', methods=['GET'])
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


@app.route('/api/stock-categories', methods=['GET'])
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


# ============================================================
# MARKET INDICES ENDPOINTS
# ============================================================

@app.route('/api/indices', methods=['GET'])
def get_indices():
    """Get latest market indices"""
    indices = query_db("""
        SELECT
            index_code,
            index_name,
            value,
            change,
            change_percent,
            volume,
            date
        FROM market_indices
        WHERE date = (SELECT MAX(date) FROM market_indices)
        ORDER BY index_code;
    """)

    return jsonify({
        "success": True,
        "indices": indices
    })


# ============================================================
# WATCHLIST ENDPOINTS
# ============================================================

# Simple in-memory watchlist storage (for demo purposes)
# In production, this should be stored in database per user
watchlist_storage = []

@app.route('/api/watchlist', methods=['GET', 'POST', 'OPTIONS'])
def handle_watchlist():
    """Get or update user watchlist"""
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        return response

    if request.method == 'GET':
        # Return current watchlist as array (for frontend compatibility)
        # If empty, return a default watchlist with popular stocks
        if not watchlist_storage:
            default_watchlist = ['VNM', 'VCB', 'FPT', 'HPG', 'VIC', 'VHM', 'GAS', 'ACB', 'BID', 'MSN']
            return jsonify(default_watchlist)

        return jsonify(watchlist_storage)

    elif request.method == 'POST':
        # Update watchlist
        try:
            data = request.get_json()

            # Accept either array directly or object with watchlist key
            if isinstance(data, list):
                watchlist_storage.clear()
                watchlist_storage.extend(data)
            elif isinstance(data, dict) and 'watchlist' in data:
                watchlist_storage.clear()
                watchlist_storage.extend(data['watchlist'])
            else:
                return jsonify({
                    'success': False,
                    'error': 'Invalid data format. Expected array of stock symbols.'
                }), 400

            return jsonify({
                'success': True,
                'message': 'Watchlist updated successfully',
                'watchlist': watchlist_storage,
                'count': len(watchlist_storage)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500


# ============================================================
# UTILITY ENDPOINTS
# ============================================================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Test database connection
        result = query_db("SELECT COUNT(*) as count FROM stocks;", one=True)
        stock_count = result['count'] if result else 0

        return jsonify({
            "status": "healthy",
            "database": "connected",
            "stocks": stock_count,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500


@app.route('/api/system-status', methods=['GET'])
def system_status():
    """Comprehensive system status check"""
    import subprocess
    import os

    status = {
        "timestamp": datetime.now().isoformat(),
        "api": {
            "status": "online",
            "message": "API server is running"
        },
        "database": {
            "status": "unknown",
            "message": "",
            "stock_count": 0,
            "latest_data": None
        },
        "scheduler": {
            "status": "unknown",
            "message": "",
            "pid": None
        },
        "data_collection": {
            "last_stock_update": None,
            "last_index_update": None,
            "last_macro_update": None,
            "stock_count_today": 0
        }
    }

    # Check database
    try:
        stock_count = query_db("SELECT COUNT(*) as count FROM stocks WHERE is_active = TRUE;", one=True)
        status["database"]["stock_count"] = stock_count['count']
        status["database"]["status"] = "connected"
        status["database"]["message"] = f"{stock_count['count']} active stocks"

        # Get latest stock data
        latest_stock = query_db("""
            SELECT MAX(date) as latest_date, COUNT(*) as count
            FROM stock_prices
            WHERE date = (SELECT MAX(date) FROM stock_prices);
        """, one=True)

        if latest_stock and latest_stock['latest_date']:
            status["data_collection"]["last_stock_update"] = latest_stock['latest_date'].isoformat()
            status["data_collection"]["stock_count_today"] = latest_stock['count']

        # Get latest index data
        latest_index = query_db("""
            SELECT MAX(date) as latest_date
            FROM market_indices;
        """, one=True)

        if latest_index and latest_index['latest_date']:
            status["data_collection"]["last_index_update"] = latest_index['latest_date'].isoformat()

        # Get latest macro data
        latest_macro = query_db("""
            SELECT MAX(date) as latest_date
            FROM macro_indicators;
        """, one=True)

        if latest_macro and latest_macro['latest_date']:
            status["data_collection"]["last_macro_update"] = latest_macro['latest_date'].isoformat()

    except Exception as e:
        status["database"]["status"] = "error"
        status["database"]["message"] = str(e)

    # Check scheduler process
    try:
        result = subprocess.run(
            ['pgrep', '-f', 'jobs/scheduler.py'],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 and result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            status["scheduler"]["status"] = "running"
            status["scheduler"]["message"] = f"Scheduler is running (PID: {pids[0]})"
            status["scheduler"]["pid"] = int(pids[0])
        else:
            status["scheduler"]["status"] = "stopped"
            status["scheduler"]["message"] = "Scheduler is not running"
    except Exception as e:
        status["scheduler"]["status"] = "unknown"
        status["scheduler"]["message"] = f"Cannot check scheduler status: {str(e)}"

    # Overall status
    overall_status = "healthy"
    if status["database"]["status"] != "connected":
        overall_status = "degraded"
    if status["scheduler"]["status"] == "stopped":
        overall_status = "warning"

    status["overall"] = overall_status

    return jsonify(status)


@app.route('/api/controls', methods=['GET'])
def get_controls():
    """Get all system controls and settings"""
    try:
        controls = query_db("""
            SELECT control_key, control_value, control_type, description, updated_at
            FROM system_controls
            ORDER BY control_type, control_key;
        """)

        # Group by type
        result = {
            'settings': [],
            'signals': [],
            'states': []
        }

        for control in controls:
            item = dict(control)
            if control['control_type'] == 'setting':
                result['settings'].append(item)
            elif control['control_type'] == 'signal':
                result['signals'].append(item)
            elif control['control_type'] == 'state':
                result['states'].append(item)

        return jsonify({
            "success": True,
            **result,
            "total": len(controls)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/controls/<key>', methods=['GET', 'PUT'])
def manage_control(key):
    """Get or update a specific control"""
    try:
        if request.method == 'GET':
            control = query_db("""
                SELECT * FROM system_controls WHERE control_key = %s;
            """, (key,), one=True)

            if control:
                return jsonify({"success": True, **control})
            else:
                return jsonify({"success": False, "error": "Control not found"}), 404

        elif request.method == 'PUT':
            data = request.get_json()
            new_value = data.get('value')

            if new_value is None:
                return jsonify({"success": False, "error": "Value required"}), 400

            conn = db_pool.getconn()
            try:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        UPDATE system_controls
                        SET control_value = %s, updated_at = NOW()
                        WHERE control_key = %s
                        RETURNING *;
                    """, (str(new_value), key))

                    result = cursor.fetchone()
                    conn.commit()

                    if result:
                        # Log the change
                        cursor.execute("""
                            INSERT INTO activity_log (activity_type, activity, details, status)
                            VALUES ('system', 'Control updated', %s, 'info');
                        """, (f"Updated {key} to {new_value}",))
                        conn.commit()

                        return jsonify({"success": True, "message": "Control updated"})
                    else:
                        return jsonify({"success": False, "error": "Control not found"}), 404
            finally:
                db_pool.putconn(conn)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/jobs/trigger', methods=['POST'])
def trigger_job():
    """Trigger a data collection job"""
    try:
        data = request.get_json()
        job_type = data.get('job_type')  # 'stock' or 'macro'

        if job_type not in ['stock', 'macro']:
            return jsonify({"success": False, "error": "Invalid job type"}), 400

        control_key = f'job.collect_{job_type}.trigger'

        conn = db_pool.getconn()
        try:
            with conn.cursor() as cursor:
                # Set trigger signal
                cursor.execute("""
                    UPDATE system_controls
                    SET control_value = 'true', updated_at = NOW()
                    WHERE control_key = %s;
                """, (control_key,))

                # Log the action
                cursor.execute("""
                    INSERT INTO activity_log (activity_type, activity, details, status)
                    VALUES ('collection', 'Job triggered', %s, 'info');
                """, (f'{job_type.capitalize()} collection job triggered from UI',))

                conn.commit()

                return jsonify({
                    "success": True,
                    "message": f"{job_type.capitalize()} collection job triggered",
                    "job_type": job_type
                })
        finally:
            db_pool.putconn(conn)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/activity-log', methods=['GET'])
def get_activity_log():
    """Get recent activity log entries"""
    try:
        limit = request.args.get('limit', default=50, type=int)
        activity_type = request.args.get('type', default=None, type=str)

        if activity_type:
            logs = query_db("""
                SELECT * FROM activity_log
                WHERE activity_type = %s
                ORDER BY timestamp DESC
                LIMIT %s;
            """, (activity_type, limit))
        else:
            logs = query_db("""
                SELECT * FROM activity_log
                ORDER BY timestamp DESC
                LIMIT %s;
            """, (limit,))

        return jsonify({
            "success": True,
            "logs": logs,
            "total": len(logs)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/')
def index():
    """Serve the homepage"""
    homepage_path = Path(__file__).parent / 'app' / 'pages' / 'index.html'
    if homepage_path.exists():
        return send_file(homepage_path)
    else:
        return jsonify({
            "error": "Homepage not found",
            "message": "index.html file is missing"
        }), 404


@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (HTML, CSS, JS, images)"""
    base_dir = Path(__file__).parent

    # Security check - prevent directory traversal
    if '..' in filename or filename.startswith('/'):
        return jsonify({"error": "Invalid file path"}), 400

    # Try multiple locations for files
    search_paths = [
        base_dir / filename,                    # Root level (for backward compatibility)
        base_dir / 'app' / 'pages' / filename, # HTML pages
        base_dir / 'app' / 'static' / filename # CSS, JS, images
    ]

    for file_path in search_paths:
        if file_path.exists() and file_path.is_file():
            return send_file(file_path)

    return jsonify({"error": f"File not found: {filename}"}), 404


@app.route('/api')
def api_docs():
    """API documentation"""
    return jsonify({
        "name": "Vietnamese Stock Analytics API",
        "version": "2.0.0",
        "database": "PostgreSQL",
        "endpoints": {
            "GET /api/stocks": "Get all stocks",
            "GET /api/stock/:symbol": "Get stock by symbol",
            "GET /api/stock/:symbol/current": "Get current price for stock",
            "GET /api/stock/:symbol/history?days=30": "Get historical prices",
            "GET /api/latest": "Get latest data for all stocks (dashboard format)",
            "GET /api/latest-prices?limit=100": "Get latest prices for all stocks",
            "GET /api/top-gainers?limit=10": "Get top gaining stocks",
            "GET /api/top-losers?limit=10": "Get top losing stocks",
            "GET /api/most-active?limit=10": "Get most active stocks by volume",
            "GET /api/search?q=query": "Search stocks by symbol or name",
            "GET /api/indices": "Get latest market indices",
            "GET /api/watchlist": "Get user's watchlist",
            "POST /api/watchlist": "Update user's watchlist",
            "GET /health": "Health check",
            "GET /api/system-status": "Comprehensive system status",
            "GET /api/controls": "Get all system controls",
            "PUT /api/controls/:key": "Update a control",
            "POST /api/jobs/trigger": "Trigger a collection job",
            "GET /api/activity-log": "Get activity log"
        },
        "documentation": "See README for full API documentation"
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Vietnamese Stock Analytics API Server v2.0")
    print("=" * 60)
    print("\nDatabase: PostgreSQL")
    print(f"Host: {API_SERVER['host']}")
    print(f"Port: {API_SERVER['port']}")

    # Test database connection
    try:
        result = query_db("SELECT COUNT(*) as count FROM stocks;", one=True)
        print(f"\n✅ Database connected: {result['count']} stocks loaded")
    except Exception as e:
        print(f"\n❌ Database connection failed: {e}")
        print("\nMake sure PostgreSQL is running:")
        print("  cd database && docker compose up -d")
        exit(1)

    print("\nAPI Endpoints:")
    print("  http://localhost:5000/api/stocks")
    print("  http://localhost:5000/api/latest-prices")
    print("  http://localhost:5000/api/top-gainers")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    print()

    # Run the server
    app.run(
        debug=API_SERVER['debug'],
        host=API_SERVER['host'],
        port=API_SERVER['port']
    )
