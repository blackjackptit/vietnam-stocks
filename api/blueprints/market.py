"""
Market indices and watchlist endpoints.
2 routes: /api/indices, /api/watchlist
"""

from flask import Blueprint, jsonify, request

from api.helpers import query_db
from api.extensions import watchlist_storage

market_bp = Blueprint('market', __name__)


@market_bp.route('/api/indices', methods=['GET'])
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


@market_bp.route('/api/watchlist', methods=['GET', 'POST', 'OPTIONS'])
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
