"""
Static file serving and API documentation.
3 routes: /, static files, /api docs
"""

from flask import Blueprint, jsonify, send_file
from pathlib import Path

static_pages_bp = Blueprint('static_pages', __name__)

# Base directory for resolving file paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent


@static_pages_bp.route('/')
def index():
    """Serve the homepage"""
    homepage_path = BASE_DIR / 'app' / 'pages' / 'index.html'
    if homepage_path.exists():
        return send_file(homepage_path)
    else:
        return jsonify({
            "error": "Homepage not found",
            "message": "index.html file is missing"
        }), 404


@static_pages_bp.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (HTML, CSS, JS, images)"""
    # Security check - prevent directory traversal
    if '..' in filename or filename.startswith('/'):
        return jsonify({"error": "Invalid file path"}), 400

    # Try multiple locations for files
    search_paths = [
        BASE_DIR / filename,                    # Root level (for backward compatibility)
        BASE_DIR / 'app' / 'pages' / filename,  # HTML pages
        BASE_DIR / 'app' / 'static' / filename   # CSS, JS, images
    ]

    for file_path in search_paths:
        if file_path.exists() and file_path.is_file():
            return send_file(file_path)

    return jsonify({"error": f"File not found: {filename}"}), 404


@static_pages_bp.route('/api')
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
            "GET /api/news?limit=10&refresh=false": "Get latest financial news",
            "GET /health": "Health check",
            "GET /api/system-status": "Comprehensive system status",
            "GET /api/controls": "Get all system controls",
            "PUT /api/controls/:key": "Update a control",
            "POST /api/jobs/trigger": "Trigger a collection job",
            "GET /api/activity-log": "Get activity log"
        },
        "documentation": "See README for full API documentation"
    })
