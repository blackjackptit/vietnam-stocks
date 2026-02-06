"""
News endpoint.
1 route: /api/news
"""

from flask import Blueprint, jsonify, request
from datetime import datetime

from src.news_fetcher import get_news_fetcher

news_bp = Blueprint('news', __name__)


@news_bp.route('/api/news', methods=['GET'])
def get_news():
    """Get latest financial news from Vietnamese sources"""
    try:
        limit = request.args.get('limit', default=10, type=int)
        force_refresh = request.args.get('refresh', default='false', type=str).lower() == 'true'

        # Fetch news from aggregated sources
        news_fetcher = get_news_fetcher()
        articles = news_fetcher.fetch_all_news(limit=limit, force_refresh=force_refresh)

        return jsonify({
            "success": True,
            "news": articles,
            "total": len(articles),
            "timestamp": datetime.now().isoformat(),
            "cache_info": "News cached for 15 minutes"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "fallback": []
        }), 500
