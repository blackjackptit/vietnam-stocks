"""
Blueprint registry. Import and collect all blueprints for registration.
"""

from api.blueprints.stocks import stocks_bp
from api.blueprints.market import market_bp
from api.blueprints.news import news_bp
from api.blueprints.system import system_bp
from api.blueprints.sessions import sessions_bp
from api.blueprints.investment import investment_bp
from api.blueprints.static_pages import static_pages_bp

all_blueprints = [
    # API blueprints MUST come before static_pages (which has catch-all route)
    stocks_bp,
    market_bp,
    news_bp,
    system_bp,
    sessions_bp,
    investment_bp,
    # Static pages must be last (has catch-all route that matches any path)
    static_pages_bp,
]
