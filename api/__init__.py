"""
Application factory for Vietnamese Stock Analytics API.
"""

from flask import Flask
from flask_cors import CORS

from config import get_database_pool, CORS_ORIGINS
import api.extensions as ext
from api.middleware import register_middleware
from api.blueprints import all_blueprints


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'vnstock-analytics-secret-key-2024'

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": CORS_ORIGINS}}, supports_credentials=True)

    # Initialize database pool
    ext.db_pool = get_database_pool()

    # Register before/after request hooks
    register_middleware(app)

    # Register all blueprints
    for bp in all_blueprints:
        app.register_blueprint(bp)

    return app
