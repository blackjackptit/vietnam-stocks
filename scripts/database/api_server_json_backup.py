#!/usr/bin/env python3
"""
Simple API Server for Vietnamese Stock Analytics Platform
Serves stock categories, names, and other data from JSON files
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)

# Enable CORS for all routes - allow requests from port 8888
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:8888", "http://127.0.0.1:8888", "*"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# In-memory cache
_cache = {}


def load_json_file(filename):
    """Load JSON file from data directory with caching"""
    cache_key = f"file:{filename}"

    if cache_key in _cache:
        return _cache[cache_key]

    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            _cache[cache_key] = data
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Error parsing {filename}")
        return None


@app.route('/api/stock-categories', methods=['GET'])
def get_stock_categories():
    """Get all stock categories"""
    data = load_json_file('stock_categories.json')

    if data:
        return jsonify(data)
    else:
        return jsonify({
            "success": False,
            "error": "Failed to load categories"
        }), 500


@app.route('/api/stock-names', methods=['GET'])
def get_stock_names():
    """Get stock symbol to name mappings"""
    data = load_json_file('stock_names.json')

    if data:
        return jsonify(data)
    else:
        return jsonify({}), 200


@app.route('/api/stock-info/<symbol>', methods=['GET'])
def get_stock_info(symbol):
    """Get detailed info for a specific stock"""
    stocks_info = load_json_file('stocks_info.json')

    if stocks_info and symbol in stocks_info:
        return jsonify({
            "success": True,
            **stocks_info[symbol]
        })
    else:
        return jsonify({
            "success": False,
            "error": "Stock not found"
        }), 404


@app.route('/api/stocks-info', methods=['GET'])
def get_all_stocks_info():
    """Get detailed info for all stocks"""
    stocks_info = load_json_file('stocks_info.json')

    if stocks_info:
        return jsonify({
            "success": True,
            "stocks": stocks_info,
            "total": len(stocks_info),
            "last_updated": datetime.now().isoformat()
        })
    else:
        return jsonify({
            "success": False,
            "error": "Failed to load stock information"
        }), 500


@app.route('/api/watchlist', methods=['GET', 'POST'])
def handle_watchlist():
    """Get or update user watchlist"""
    watchlist_file = os.path.join(DATA_DIR, 'watchlist.json')

    if request.method == 'GET':
        # Load watchlist
        try:
            if os.path.exists(watchlist_file):
                with open(watchlist_file, 'r') as f:
                    watchlist = json.load(f)
                return jsonify(watchlist)
            else:
                # Return default watchlist
                return jsonify(['VPB', 'STB', 'HDB', 'SHB', 'MBB', 'ACB', 'FPT', 'POW', 'DGC', 'GEX'])
        except:
            return jsonify([])

    elif request.method == 'POST':
        # Update watchlist
        try:
            watchlist = request.json

            if not isinstance(watchlist, list):
                return jsonify({
                    "success": False,
                    "error": "Watchlist must be an array"
                }), 400

            with open(watchlist_file, 'w') as f:
                json.dump(watchlist, f, indent=2)

            return jsonify({
                "success": True,
                "count": len(watchlist),
                "message": "Watchlist updated successfully"
            })
        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500


@app.route('/api/latest', methods=['GET'])
def get_latest_data():
    """Get latest stock data (placeholder - implement your data fetching logic)"""
    # This is a placeholder - implement your actual data fetching logic
    latest_file = os.path.join(DATA_DIR, 'latest_data.json')

    if os.path.exists(latest_file):
        with open(latest_file, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({
            "error": "No data available yet"
        }), 404


@app.route('/data/<path:filename>', methods=['GET'])
def serve_data_file(filename):
    """Serve data files (for historical data, etc.)"""
    response = send_from_directory(DATA_DIR, filename)
    # Ensure CORS headers are present
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/api/historical/<symbol>', methods=['GET'])
def get_historical_data(symbol):
    """Get historical data for a stock"""
    days = request.args.get('days', default=90, type=int)

    # Try to load from {SYMBOL}_history.json
    history_file = f"{symbol}_history.json"
    data = load_json_file(history_file)

    if data:
        # Return last N days
        if isinstance(data, list):
            return jsonify(data[-days:])
        else:
            return jsonify(data)
    else:
        return jsonify({
            "error": f"No historical data found for {symbol}"
        }), 404


@app.route('/api/clear-cache', methods=['POST'])
def clear_cache():
    """Clear the data cache (useful after updating JSON files)"""
    global _cache
    _cache = {}
    return jsonify({
        "success": True,
        "message": "Cache cleared successfully"
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })


@app.route('/')
def index():
    """API documentation"""
    return jsonify({
        "name": "Vietnamese Stock Analytics API",
        "version": "1.0.0",
        "endpoints": {
            "GET /api/stock-categories": "Get all stock categories",
            "GET /api/stock-names": "Get stock symbol to name mappings",
            "GET /api/stock-info/:symbol": "Get detailed info for a stock",
            "GET /api/stocks-info": "Get info for all stocks",
            "GET /api/watchlist": "Get user watchlist",
            "POST /api/watchlist": "Update user watchlist",
            "GET /api/latest": "Get latest stock data",
            "GET /api/historical/:symbol": "Get historical data for a stock",
            "POST /api/clear-cache": "Clear data cache",
            "GET /health": "Health check"
        },
        "documentation": "/api-docs"
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Vietnamese Stock Analytics API Server")
    print("=" * 60)
    print("\nStarting server...")
    print(f"Data directory: {DATA_DIR}")
    print("\nAPI Endpoints:")
    print("  http://localhost:5000/api/stock-categories")
    print("  http://localhost:5000/api/stock-names")
    print("  http://localhost:5000/api/watchlist")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    print()

    # Run the server
    app.run(debug=True, host='0.0.0.0', port=5000)
