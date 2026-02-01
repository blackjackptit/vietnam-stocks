#!/usr/bin/env python3
"""
Vietnamese Stock Analytics API Server
Serves stock data from PostgreSQL database
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
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


@app.route('/')
def index():
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
            "GET /api/latest-prices?limit=100": "Get latest prices for all stocks",
            "GET /api/top-gainers?limit=10": "Get top gaining stocks",
            "GET /api/top-losers?limit=10": "Get top losing stocks",
            "GET /api/most-active?limit=10": "Get most active stocks by volume",
            "GET /api/search?q=query": "Search stocks by symbol or name",
            "GET /api/indices": "Get latest market indices",
            "GET /health": "Health check"
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
