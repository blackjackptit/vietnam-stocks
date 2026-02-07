"""
Shared state and extensions for the API server.
Database pool, session storage, and watchlist storage.
"""

import threading

# Database connection pool (initialized in create_app)
db_pool = None

# In-memory session storage
active_sessions = {}  # session_id: session_data
recent_activity = []  # List of recent page views and actions
activity_lock = threading.Lock()
SESSION_TIMEOUT = 1800  # 30 minutes

# Long-lived cookie for plan ownership (1 year)
PLAN_COOKIE_MAX_AGE = 365 * 24 * 3600

# Simple in-memory watchlist storage (for demo purposes)
watchlist_storage = []
