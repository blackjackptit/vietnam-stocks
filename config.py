"""
Configuration file for VNStock Analytics Platform
Contains database, API, and application settings
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# ════════════════════════════════════════════════════════════════
# DATABASE CONFIGURATION (PostgreSQL)
# ════════════════════════════════════════════════════════════════

DATABASE = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'database': os.getenv('DB_NAME', 'vnstock_db'),
    'user': os.getenv('DB_USER', 'vnstock_user'),
    'password': os.getenv('DB_PASSWORD', 'vnstock_password_change_in_production'),
}

# Database connection string
DATABASE_URL = (
    f"postgresql://{DATABASE['user']}:{DATABASE['password']}"
    f"@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
)

# Connection pool settings
DATABASE_POOL = {
    'min_connections': int(os.getenv('DB_POOL_MIN', 2)),
    'max_connections': int(os.getenv('DB_POOL_MAX', 20)),
    'idle_timeout': int(os.getenv('DB_POOL_IDLE_TIMEOUT', 30000)),
}

# ════════════════════════════════════════════════════════════════
# API SERVER CONFIGURATION
# ════════════════════════════════════════════════════════════════

API_SERVER = {
    'host': os.getenv('API_HOST', '0.0.0.0'),
    'port': int(os.getenv('API_PORT', 5000)),
    'debug': os.getenv('DEBUG', 'False').lower() == 'true',
}

# CORS settings
CORS_ORIGINS = [
    'http://localhost:8888',
    'http://127.0.0.1:8888',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# ════════════════════════════════════════════════════════════════
# APPLICATION SETTINGS
# ════════════════════════════════════════════════════════════════

# Environment
ENVIRONMENT = os.getenv('NODE_ENV', 'development')

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'info').upper()

# Security
SECRET_KEY = os.getenv('JWT_SECRET', 'change_this_to_a_random_secret_key')
SESSION_SECRET = os.getenv('SESSION_SECRET', 'change_this_to_another_random_secret')

# ════════════════════════════════════════════════════════════════
# DATA DIRECTORIES
# ════════════════════════════════════════════════════════════════

DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'
STATIC_DIR = BASE_DIR / 'static'
TEMPLATES_DIR = BASE_DIR / 'templates'

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# ════════════════════════════════════════════════════════════════
# DATA REFRESH INTERVALS (in seconds)
# ════════════════════════════════════════════════════════════════

REFRESH_INTERVALS = {
    'prices': int(os.getenv('PRICE_UPDATE_INTERVAL', 300)),        # 5 minutes
    'indicators': int(os.getenv('INDICATOR_UPDATE_INTERVAL', 3600)), # 1 hour
    'forecasts': int(os.getenv('FORECAST_UPDATE_INTERVAL', 86400)),  # 24 hours
}

# ════════════════════════════════════════════════════════════════
# DATA COLLECTION AUTOMATION SETTINGS
# ════════════════════════════════════════════════════════════════

DATA_COLLECTION = {
    # Global enable/disable
    'enabled': os.getenv('AUTO_COLLECT_ENABLED', 'true').lower() == 'true',

    # Stock data collection
    'stock': {
        'enabled': os.getenv('STOCK_COLLECTION_ENABLED', 'true').lower() == 'true',
        'interval': int(os.getenv('STOCK_COLLECTION_INTERVAL', 3600)),  # seconds
        'market_hours_only': os.getenv('STOCK_COLLECTION_MARKET_HOURS_ONLY', 'true').lower() == 'true',
        'end_of_day': os.getenv('STOCK_COLLECTION_END_OF_DAY', 'true').lower() == 'true',
    },

    # Market indices collection
    'indices': {
        'enabled': os.getenv('INDEX_COLLECTION_ENABLED', 'true').lower() == 'true',
        'interval': int(os.getenv('INDEX_COLLECTION_INTERVAL', 1800)),  # seconds
        'market_hours_only': os.getenv('INDEX_COLLECTION_MARKET_HOURS_ONLY', 'false').lower() == 'true',
    },

    # Macro indicators collection
    'macro': {
        'enabled': os.getenv('MACRO_COLLECTION_ENABLED', 'true').lower() == 'true',
        'interval': int(os.getenv('MACRO_COLLECTION_INTERVAL', 3600)),  # seconds
        'daily_update': os.getenv('MACRO_DAILY_UPDATE', 'true').lower() == 'true',
        'daily_update_hour': int(os.getenv('MACRO_DAILY_UPDATE_HOUR', 6)),
    },
}

# Market hours configuration
MARKET_HOURS = {
    'open_hour': int(os.getenv('MARKET_OPEN_HOUR', 9)),
    'close_hour': int(os.getenv('MARKET_CLOSE_HOUR', 15)),
    'days': os.getenv('MARKET_DAYS', 'mon-fri'),
}

# Data source configuration
DATA_SOURCES = {
    'primary': os.getenv('STOCK_DATA_SOURCE_PRIMARY', 'VCI'),
    'fallback': os.getenv('STOCK_DATA_SOURCE_FALLBACK', 'TCBS'),
    'timeout': int(os.getenv('STOCK_DATA_TIMEOUT', 30)),
}

# Rate limiting and retry configuration
COLLECTION_CONFIG = {
    'rate_limit_delay': float(os.getenv('COLLECTION_RATE_LIMIT_DELAY', 0.3)),
    'max_retries': int(os.getenv('COLLECTION_MAX_RETRIES', 3)),
    'log_file': os.getenv('COLLECTION_LOG_FILE', '/tmp/stock_scheduler.log'),
    'log_level': os.getenv('COLLECTION_LOG_LEVEL', 'INFO'),
}

# ════════════════════════════════════════════════════════════════
# STOCK DATA SETTINGS
# ════════════════════════════════════════════════════════════════

# Default stock list
DEFAULT_STOCKS = [
    'VNM', 'VIC', 'VCB', 'FPT', 'HPG', 'GAS', 'MSN', 'VHM', 'TCB', 'VRE',
    'MWG', 'PLX', 'VPB', 'BID', 'CTG', 'POW', 'SAB', 'MBB', 'ACB', 'SSI',
    'HDB', 'VJC', 'PDR', 'NVL', 'DXG', 'KDH', 'CMG', 'REE', 'PNJ', 'HNG', 'DCM'
]

# Exchange categories
EXCHANGES = {
    'HOSE': 'Ho Chi Minh Stock Exchange',
    'HNX': 'Hanoi Stock Exchange',
    'UPCOM': 'Unlisted Public Company Market',
}

# ════════════════════════════════════════════════════════════════
# ML MODEL SETTINGS
# ════════════════════════════════════════════════════════════════

ML_MODELS = [
    'linear',
    'ma',
    'exp',
    'arima',
    'lstm',
    'prophet',
    'sarima',
    'garch',
    'xgboost',
    'random-forest',
    'gradient-boost',
    'kalman',
    'wavenet',
    'transformer',
    'ensemble',
    'advanced-ensemble',
]

# Default forecast days
FORECAST_DAYS = 7

# ════════════════════════════════════════════════════════════════
# CACHE SETTINGS
# ════════════════════════════════════════════════════════════════

CACHE_ENABLED = True
CACHE_TTL = {
    'stock_list': 3600,        # 1 hour
    'stock_prices': 300,       # 5 minutes
    'indicators': 1800,        # 30 minutes
    'forecasts': 7200,         # 2 hours
}

# ════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════

def get_database_connection():
    """
    Get database connection using psycopg2

    Usage:
        import psycopg2
        from config import get_database_connection

        conn = get_database_connection()
        cursor = conn.cursor()
        # ... use connection ...
        conn.close()
    """
    try:
        import psycopg2
        return psycopg2.connect(**DATABASE)
    except ImportError:
        raise ImportError("psycopg2 is not installed. Run: pip install psycopg2-binary")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to database: {e}")


def get_database_pool():
    """
    Get database connection pool

    Usage:
        from psycopg2 import pool
        from config import get_database_pool

        db_pool = get_database_pool()
        conn = db_pool.getconn()
        # ... use connection ...
        db_pool.putconn(conn)
    """
    try:
        from psycopg2 import pool
        return pool.SimpleConnectionPool(
            DATABASE_POOL['min_connections'],
            DATABASE_POOL['max_connections'],
            **DATABASE
        )
    except ImportError:
        raise ImportError("psycopg2 is not installed. Run: pip install psycopg2-binary")
    except Exception as e:
        raise ConnectionError(f"Failed to create connection pool: {e}")


def load_env_file(env_path=None):
    """
    Load environment variables from .env file

    Args:
        env_path: Path to .env file (default: BASE_DIR / '.env')
    """
    if env_path is None:
        env_path = BASE_DIR / '.env'

    if not env_path.exists():
        print(f"Warning: .env file not found at {env_path}")
        return

    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())


# Load .env file if it exists
load_env_file()


# ════════════════════════════════════════════════════════════════
# CONFIGURATION SUMMARY
# ════════════════════════════════════════════════════════════════

def print_config():
    """Print current configuration (useful for debugging)"""
    print("=" * 60)
    print("VNStock Analytics - Configuration")
    print("=" * 60)
    print(f"Environment: {ENVIRONMENT}")
    print(f"Debug Mode: {API_SERVER['debug']}")
    print(f"\nDatabase:")
    print(f"  Host: {DATABASE['host']}")
    print(f"  Port: {DATABASE['port']}")
    print(f"  Database: {DATABASE['database']}")
    print(f"  User: {DATABASE['user']}")
    print(f"\nAPI Server:")
    print(f"  Host: {API_SERVER['host']}")
    print(f"  Port: {API_SERVER['port']}")
    print(f"\nData Directories:")
    print(f"  Data: {DATA_DIR}")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    # Print configuration when run directly
    print_config()

    # Test database connection
    print("\nTesting database connection...")
    try:
        conn = get_database_connection()
        print("✅ Database connection successful!")

        # Test query
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stocks;")
        count = cursor.fetchone()[0]
        print(f"✅ Found {count} stocks in database")

        conn.close()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\nMake sure PostgreSQL is running:")
        print("  cd database && docker compose up -d")
