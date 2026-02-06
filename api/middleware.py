"""
Before/after request hooks for session tracking.
"""

from flask import request
from api.extensions import active_sessions, activity_lock, SESSION_TIMEOUT
from api.helpers import get_or_create_session, log_activity


def register_middleware(app):
    """Register before/after request hooks on the Flask app."""

    @app.before_request
    def track_request():
        """Track all page requests"""
        # Skip tracking for static files and API status checks
        if (request.path.startswith('/static') or
            request.path.startswith('/css') or
            request.path.startswith('/js') or
            request.path.endswith('.svg') or
            request.path.endswith('.png') or
            request.path.endswith('.jpg')):
            return

        session_id = get_or_create_session()

        # Track page views for HTML pages
        if request.path.endswith('.html') or request.path == '/' or request.path == '/index.html':
            page_name = request.path.split('/')[-1] or 'index.html'
            with activity_lock:
                active_sessions[session_id]['page_views'] += 1
                active_sessions[session_id]['current_page'] = page_name
            log_activity(session_id, 'page_view', page=page_name)

        # Track API calls
        elif request.path.startswith('/api/'):
            endpoint = request.path.replace('/api/', '')
            log_activity(session_id, 'api_call', details=endpoint)

        # Store session_id for response
        request.session_id = session_id

    @app.after_request
    def after_request(response):
        """Set session cookie"""
        if hasattr(request, 'session_id'):
            response.set_cookie('session_id', request.session_id, max_age=SESSION_TIMEOUT, samesite='Lax')
        return response
