"""
Database query helpers and session management functions.
"""

from datetime import datetime
from flask import request
from psycopg2.extras import RealDictCursor
import uuid

import api.extensions as ext
from api.extensions import (
    active_sessions, recent_activity,
    activity_lock, SESSION_TIMEOUT
)


def query_db(query, args=(), one=False):
    """Execute query and return results"""
    conn = ext.db_pool.getconn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, args)
            # Commit for INSERT/UPDATE/DELETE queries
            if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                conn.commit()
                return None
            # Fetch results for SELECT queries
            if one:
                return cursor.fetchone()
            return cursor.fetchall()
    finally:
        ext.db_pool.putconn(conn)


def get_or_create_session():
    """Get existing session or create new one"""
    session_id = request.cookies.get('session_id')

    if not session_id or session_id not in active_sessions:
        session_id = str(uuid.uuid4())
        with activity_lock:
            active_sessions[session_id] = {
                'id': session_id,
                'created_at': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'ip_address': request.remote_addr,
                'user_agent': request.headers.get('User-Agent', 'Unknown'),
                'page_views': 0,
                'actions': [],
                'current_page': None
            }

    # Update last seen
    with activity_lock:
        active_sessions[session_id]['last_seen'] = datetime.now().isoformat()

    return session_id


def log_activity(session_id, activity_type, page=None, details=None):
    """Log user activity"""
    with activity_lock:
        activity = {
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'type': activity_type,
            'page': page,
            'details': details,
            'ip': request.remote_addr
        }
        recent_activity.append(activity)

        # Keep only last 100 activities
        if len(recent_activity) > 100:
            recent_activity.pop(0)

        # Update session actions
        if session_id in active_sessions:
            active_sessions[session_id]['actions'].append({
                'type': activity_type,
                'page': page,
                'timestamp': datetime.now().isoformat()
            })

            # Keep only last 20 actions per session
            if len(active_sessions[session_id]['actions']) > 20:
                active_sessions[session_id]['actions'].pop(0)


def get_or_create_plan_owner():
    """Get existing plan owner ID or create a new one (long-lived, persists across sessions)"""
    owner_id = request.cookies.get('plan_owner_id')
    if not owner_id:
        # Fall back to session_id cookie for backward compatibility with existing plans
        owner_id = request.cookies.get('session_id')
    if not owner_id:
        owner_id = str(uuid.uuid4())
    return owner_id


def cleanup_old_sessions():
    """Remove inactive sessions"""
    with activity_lock:
        now = datetime.now()
        expired = []
        for session_id, session_data in active_sessions.items():
            last_seen = datetime.fromisoformat(session_data['last_seen'])
            if (now - last_seen).seconds > SESSION_TIMEOUT:
                expired.append(session_id)

        for session_id in expired:
            del active_sessions[session_id]
