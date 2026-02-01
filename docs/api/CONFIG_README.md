# Configuration Guide

## Overview

The VNStock Analytics platform uses a centralized configuration system through `config.py` and `.env` files.

## Configuration Files

### 1. `config.py` - Main Configuration Module

Central configuration file that loads settings from environment variables and provides helper functions.

**Import in your Python scripts:**
```python
from config import DATABASE, API_SERVER, get_database_connection
```

**Available Settings:**

- `DATABASE` - PostgreSQL database connection settings
- `DATABASE_URL` - Full PostgreSQL connection string
- `DATABASE_POOL` - Connection pool settings
- `API_SERVER` - API server configuration
- `CORS_ORIGINS` - Allowed CORS origins
- `DATA_DIR` - Data directory path
- `OUTPUT_DIR` - Output directory path
- `REFRESH_INTERVALS` - Data refresh intervals
- `DEFAULT_STOCKS` - List of default stock symbols
- `ML_MODELS` - Available ML models

### 2. `.env` - Environment Variables

Contains sensitive configuration like database passwords. This file should NOT be committed to git.

**Location:** `/Users/nghia.dinh/Projects/vietnam-stocks/.env`

**Template:** See `.env.example` for all available variables

### 3. `.env.example` - Environment Template

Template file showing all available environment variables. Copy this to `.env` and customize.

```bash
cp .env.example .env
# Edit .env with your values
```

## Database Configuration

### Connection Settings

The database configuration is loaded from environment variables:

```python
DATABASE = {
    'host': 'localhost',      # DB_HOST
    'port': 5432,             # DB_PORT
    'database': 'vnstock_db', # DB_NAME
    'user': 'vnstock_user',   # DB_USER
    'password': '...',        # DB_PASSWORD
}
```

### Using Database Connection

**Simple Connection:**
```python
from config import get_database_connection

# Get connection
conn = get_database_connection()

# Use connection
cursor = conn.cursor()
cursor.execute("SELECT * FROM stocks LIMIT 5;")
results = cursor.fetchall()

# Close connection
conn.close()
```

**Connection Pool (Recommended for production):**
```python
from config import get_database_pool

# Create pool (do this once at startup)
db_pool = get_database_pool()

# Get connection from pool
conn = db_pool.getconn()

# Use connection
cursor = conn.cursor()
cursor.execute("SELECT * FROM stocks;")
results = cursor.fetchall()

# Return connection to pool
db_pool.putconn(conn)

# When shutting down
db_pool.closeall()
```

**Using psycopg2.extras.RealDictCursor:**
```python
from psycopg2.extras import RealDictCursor
from config import get_database_connection

conn = get_database_connection()

with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute("SELECT * FROM stocks LIMIT 5;")
    stocks = cursor.fetchall()

    # Results are dictionaries
    for stock in stocks:
        print(f"{stock['symbol']} - {stock['name']}")

conn.close()
```

## API Server Configuration

**Settings:**
```python
API_SERVER = {
    'host': '0.0.0.0',  # Bind to all interfaces
    'port': 5000,       # API port
    'debug': False,     # Debug mode
}
```

**CORS Origins:**
```python
CORS_ORIGINS = [
    'http://localhost:8888',
    'http://127.0.0.1:8888',
]
```

## Usage Examples

### Example 1: Simple Database Query

```python
#!/usr/bin/env python3
from config import get_database_connection
from psycopg2.extras import RealDictCursor

def get_all_stocks():
    conn = get_database_connection()

    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("""
            SELECT symbol, name, exchange, sector
            FROM stocks
            ORDER BY symbol;
        """)
        stocks = cursor.fetchall()

    conn.close()
    return stocks

if __name__ == '__main__':
    stocks = get_all_stocks()
    for stock in stocks:
        print(f"{stock['symbol']:5} | {stock['name']:30} | {stock['exchange']}")
```

### Example 2: Inserting Data

```python
#!/usr/bin/env python3
from config import get_database_connection
from datetime import datetime

def save_stock_price(symbol, date, open_price, high, low, close, volume):
    conn = get_database_connection()
    cursor = conn.cursor()

    # Get stock_id
    cursor.execute("SELECT id FROM stocks WHERE symbol = %s", (symbol,))
    result = cursor.fetchone()

    if not result:
        print(f"Stock {symbol} not found")
        return False

    stock_id = result[0]

    # Insert price
    cursor.execute("""
        INSERT INTO stock_prices
        (stock_id, date, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (stock_id, date)
        DO UPDATE SET
            open = EXCLUDED.open,
            high = EXCLUDED.high,
            low = EXCLUDED.low,
            close = EXCLUDED.close,
            volume = EXCLUDED.volume;
    """, (stock_id, date, open_price, high, low, close, volume))

    conn.commit()
    conn.close()
    return True

if __name__ == '__main__':
    save_stock_price('VNM', datetime.now().date(), 85000, 86000, 84000, 85500, 1000000)
    print("Price saved successfully")
```

### Example 3: Using Config in Flask App

```python
#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from config import API_SERVER, CORS_ORIGINS, get_database_pool

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": CORS_ORIGINS}})

# Create connection pool at startup
db_pool = get_database_pool()

@app.route('/api/stocks')
def get_stocks():
    conn = db_pool.getconn()

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM stocks ORDER BY symbol;")
            stocks = cursor.fetchall()
        return jsonify(stocks)
    finally:
        db_pool.putconn(conn)

if __name__ == '__main__':
    app.run(
        host=API_SERVER['host'],
        port=API_SERVER['port'],
        debug=API_SERVER['debug']
    )
```

## Environment Variables Reference

### Database Settings
- `DB_HOST` - Database host (default: localhost)
- `DB_PORT` - Database port (default: 5432)
- `DB_NAME` - Database name (default: vnstock_db)
- `DB_USER` - Database user (default: vnstock_user)
- `DB_PASSWORD` - Database password

### Connection Pool Settings
- `DB_POOL_MIN` - Minimum connections (default: 2)
- `DB_POOL_MAX` - Maximum connections (default: 20)
- `DB_POOL_IDLE_TIMEOUT` - Idle timeout in ms (default: 30000)

### API Settings
- `API_HOST` - API server host (default: 0.0.0.0)
- `API_PORT` - API server port (default: 5000)

### Application Settings
- `NODE_ENV` - Environment (development/production)
- `LOG_LEVEL` - Logging level (debug/info/warning/error)
- `DEBUG` - Enable debug mode (true/false)

### Security Settings
- `JWT_SECRET` - JWT secret key
- `SESSION_SECRET` - Session secret key

### Data Refresh Intervals (seconds)
- `PRICE_UPDATE_INTERVAL` - Price update interval (default: 300)
- `INDICATOR_UPDATE_INTERVAL` - Indicator update interval (default: 3600)
- `FORECAST_UPDATE_INTERVAL` - Forecast update interval (default: 86400)

## Testing Configuration

### Test Database Connection

```bash
# Activate virtual environment
source venv/bin/activate

# Run config test
python config.py
```

**Expected Output:**
```
============================================================
VNStock Analytics - Configuration
============================================================
Environment: development
Debug Mode: False

Database:
  Host: localhost
  Port: 5432
  Database: vnstock_db
  User: vnstock_user

API Server:
  Host: 0.0.0.0
  Port: 5000

Data Directories:
  Data: /Users/nghia.dinh/Projects/vietnam-stocks/data
  Output: /Users/nghia.dinh/Projects/vietnam-stocks/output
============================================================

Testing database connection...
✅ Database connection successful!
✅ Found 31 stocks in database
```

### Debug Configuration

```python
from config import print_config

# Print all configuration values
print_config()
```

## Production Checklist

Before deploying to production:

1. ✅ Copy `.env.example` to `.env`
2. ⚠️ Change `DB_PASSWORD` to a secure password
3. ⚠️ Generate secure values for `JWT_SECRET` and `SESSION_SECRET`
4. ⚠️ Set `NODE_ENV=production`
5. ⚠️ Set `DEBUG=false`
6. ⚠️ Configure `CORS_ORIGINS` to allow only your domain
7. ✅ Enable SSL for database connections
8. ✅ Set up connection pooling
9. ✅ Configure proper logging
10. ✅ Set up database backups

## Security Notes

### Do NOT commit to Git:
- `.env` file (contains passwords and secrets)
- Any file with credentials

### Git Configuration:

Add to `.gitignore`:
```
.env
*.key
*.pem
secrets/
```

### Generate Secure Secrets:

```python
import secrets

# Generate JWT secret
jwt_secret = secrets.token_urlsafe(32)
print(f"JWT_SECRET={jwt_secret}")

# Generate session secret
session_secret = secrets.token_urlsafe(32)
print(f"SESSION_SECRET={session_secret}")
```

## Troubleshooting

### Connection Refused Error

```
psycopg2.OperationalError: connection refused
```

**Solution:**
```bash
# Check if PostgreSQL is running
docker compose ps

# Start PostgreSQL
cd database && docker compose up -d

# Test connection
docker exec vnstock_postgres pg_isready -U vnstock_user -d vnstock_db
```

### Module Not Found Error

```
ModuleNotFoundError: No module named 'psycopg2'
```

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install psycopg2
pip install psycopg2-binary
```

### Environment Variables Not Loading

**Solution:**
1. Make sure `.env` file exists in project root
2. Check file permissions: `chmod 600 .env`
3. Verify format: `KEY=value` (no spaces around =)
4. Restart your application after changes

## Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

## Support

For database setup issues, see:
- `database/README.md` - Database documentation
- `database/SETUP_COMPLETE.md` - Quick start guide
