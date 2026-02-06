"""
Session tracking endpoints.
3 routes: /api/sessions/active, /api/sessions/activity, /api/sessions/stats
"""

from flask import Blueprint, jsonify, request
from datetime import datetime
from collections import defaultdict

from api.extensions import active_sessions, recent_activity, activity_lock
from api.helpers import cleanup_old_sessions

sessions_bp = Blueprint('sessions', __name__)


@sessions_bp.route('/api/sessions/active', methods=['GET'])
def get_active_sessions():
    """Get all active sessions"""
    cleanup_old_sessions()

    with activity_lock:
        sessions = []
        for session_id, session_data in active_sessions.items():
            # Calculate session duration
            created = datetime.fromisoformat(session_data['created_at'])
            last_seen = datetime.fromisoformat(session_data['last_seen'])
            duration = int((last_seen - created).total_seconds())

            sessions.append({
                'id': session_id[:8] + '...',  # Truncate for privacy
                'created_at': session_data['created_at'],
                'last_seen': session_data['last_seen'],
                'duration': duration,
                'page_views': session_data['page_views'],
                'current_page': session_data['current_page'],
                'ip_address': session_data['ip_address'],
                'user_agent': session_data['user_agent'][:100]  # Truncate user agent
            })

        # Sort by last seen (most recent first)
        sessions.sort(key=lambda x: x['last_seen'], reverse=True)

    return jsonify({
        'success': True,
        'total_sessions': len(sessions),
        'sessions': sessions,
        'timestamp': datetime.now().isoformat()
    })


@sessions_bp.route('/api/sessions/activity', methods=['GET'])
def get_recent_activity():
    """Get recent user activity"""
    limit = request.args.get('limit', 50, type=int)

    with activity_lock:
        # Get most recent activities
        activities = recent_activity[-limit:][::-1]  # Reverse to show newest first

    return jsonify({
        'success': True,
        'total': len(recent_activity),
        'activities': activities,
        'timestamp': datetime.now().isoformat()
    })


@sessions_bp.route('/api/sessions/stats', methods=['GET'])
def get_session_stats():
    """Get session statistics"""
    cleanup_old_sessions()

    with activity_lock:
        total_sessions = len(active_sessions)
        total_page_views = sum(s['page_views'] for s in active_sessions.values())

        # Page view counts
        page_counts = defaultdict(int)
        for activity in recent_activity:
            if activity['type'] == 'page_view' and activity['page']:
                page_counts[activity['page']] += 1

        # Most popular pages
        popular_pages = sorted(page_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Recent activity types
        activity_types = defaultdict(int)
        for activity in recent_activity[-100:]:
            activity_types[activity['type']] += 1

    return jsonify({
        'success': True,
        'total_sessions': total_sessions,
        'total_page_views': total_page_views,
        'avg_page_views': round(total_page_views / max(total_sessions, 1), 2),
        'popular_pages': [{'page': p[0], 'views': p[1]} for p in popular_pages],
        'activity_types': dict(activity_types),
        'timestamp': datetime.now().isoformat()
    })
