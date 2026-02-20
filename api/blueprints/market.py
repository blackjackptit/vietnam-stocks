"""
Market indices and watchlist endpoints.
2 routes: /api/indices, /api/watchlist
"""

import logging
from flask import Blueprint, jsonify, request

from api.helpers import query_db
from api.extensions import watchlist_storage

logger = logging.getLogger(__name__)

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


@market_bp.route('/api/watchlist', methods=['GET', 'POST'])
def handle_watchlist():
    """Get or update user watchlist

    CORS is handled automatically by flask-cors in api/__init__.py
    No need for manual OPTIONS handling or Access-Control headers
    """
    if request.method == 'GET':
        # Return current watchlist as array (for frontend compatibility)
        # If empty, return a default watchlist with popular stocks
        if not watchlist_storage:
            default_watchlist = ['VNM', 'VCB', 'FPT', 'HPG', 'VIC', 'VHM', 'GAS', 'ACB', 'BID', 'MSN']
            logger.info("Returning default watchlist (no saved watchlist found)")
            # Return metadata to indicate this is default data
            return jsonify({
                'watchlist': default_watchlist,
                'is_default': True,
                'count': len(default_watchlist)
            })

        logger.debug(f"Returning saved watchlist with {len(watchlist_storage)} stocks")
        return jsonify({
            'watchlist': watchlist_storage,
            'is_default': False,
            'count': len(watchlist_storage)
        })

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
        except ValueError as e:
            logger.warning(f"Invalid watchlist data format: {e}")
            return jsonify({
                'success': False,
                'error': f'Invalid data format: {str(e)}'
            }), 400
        except Exception as e:
            logger.error(f"Unexpected error updating watchlist: {e}", exc_info=True)
            return jsonify({
                'success': False,
                'error': 'An internal error occurred while updating watchlist'
            }), 500


@market_bp.route('/api/macro-indicators', methods=['GET'])
def get_macro_indicators():
    """Get latest macro economic indicators"""
    try:
        indicators = query_db("""
            SELECT
                id,
                indicator_type,
                country,
                date,
                value,
                unit,
                source,
                created_at
            FROM macro_indicators
            ORDER BY indicator_type, date DESC;
        """)

        # Group by indicator type and get latest
        latest_indicators = {}
        for indicator in indicators:
            key = indicator['indicator_type']
            if key not in latest_indicators:
                latest_indicators[key] = indicator

        return jsonify({
            "success": True,
            "indicators": list(latest_indicators.values()),
            "count": len(latest_indicators)
        })
    except Exception as e:
        logger.error(f"Error retrieving macro indicators: {e}", exc_info=True)
        return jsonify({
            "success": False,
            "error": f"Failed to retrieve macro indicators: {str(e)}"
        }), 500
