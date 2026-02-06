#!/usr/bin/env python3
"""
Vietnamese Stock Analytics API Server
Backward-compatible shim — delegates to api/ package.
Use run.py as the primary entry point.
"""

from config import API_SERVER
from api import create_app
from api.helpers import query_db

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("Vietnamese Stock Analytics API Server v2.0")
    print("=" * 60)
    print("\nDatabase: PostgreSQL")
    print(f"Host: {API_SERVER['host']}")
    print(f"Port: {API_SERVER['port']}")

    # Test database connection
    try:
        with app.app_context():
            result = query_db("SELECT COUNT(*) as count FROM stocks;", one=True)
            print(f"\n✅ Database connected: {result['count']} stocks loaded")
    except Exception as e:
        print(f"\n❌ Database connection failed: {e}")
        print("\nMake sure PostgreSQL is running:")
        print("  cd database && docker compose up -d")
        exit(1)

    print("\nAPI Endpoints:")
    print("  http://localhost:5000/api/stocks")
    print("  http://localhost:5000/api/latest-prices")
    print("  http://localhost:5000/api/top-gainers")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    print()

    # Run the server
    app.run(
        debug=API_SERVER['debug'],
        host=API_SERVER['host'],
        port=API_SERVER['port']
    )
