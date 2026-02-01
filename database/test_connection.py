#!/usr/bin/env python3
"""
Test script to verify PostgreSQL database connection and query data.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import sys

# Database connection parameters
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'vnstock_db',
    'user': 'vnstock_user',
    'password': 'vnstock_password_change_in_production'
}

def test_connection():
    """Test database connection and run sample queries."""
    try:
        # Connect to database
        print("🔌 Connecting to PostgreSQL database...")
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Connection successful!\n")

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            # Test 1: Count stocks
            print("📊 Test 1: Count stocks")
            cursor.execute("SELECT COUNT(*) as total FROM stocks;")
            result = cursor.fetchone()
            print(f"   Total stocks: {result['total']}\n")

            # Test 2: Get top 5 stocks
            print("📈 Test 2: Get stock list (top 5)")
            cursor.execute("""
                SELECT symbol, name, exchange, sector, category
                FROM stocks
                ORDER BY symbol
                LIMIT 5;
            """)
            stocks = cursor.fetchall()
            for stock in stocks:
                print(f"   {stock['symbol']:5} | {stock['name']:25} | {stock['exchange']:4} | {stock['sector']}")
            print()

            # Test 3: Get latest prices
            print("💰 Test 3: Get latest stock prices")
            cursor.execute("""
                SELECT symbol, name, price, change_percent, volume
                FROM latest_stock_prices
                ORDER BY symbol
                LIMIT 5;
            """)
            prices = cursor.fetchall()
            for price in prices:
                symbol = price['symbol'] if price['symbol'] else 'N/A'
                name = price['name'] if price['name'] else 'N/A'
                current_price = f"{price['price']:,.2f}" if price['price'] else 'N/A'
                change = f"{price['change_percent']:+.2f}%" if price['change_percent'] else 'N/A'
                vol = f"{price['volume']:,}" if price['volume'] else 'N/A'
                print(f"   {symbol:5} | {name:25} | {current_price:>12} | {change:>8} | Vol: {vol}")
            print()

            # Test 4: Get market indices
            print("📊 Test 4: Get market indices")
            cursor.execute("""
                SELECT index_code, index_name, value, change_percent
                FROM market_indices
                ORDER BY index_code;
            """)
            indices = cursor.fetchall()
            for idx in indices:
                print(f"   {idx['index_code']:10} | {idx['index_name']:20} | {idx['value']:>10.2f} | {idx['change_percent']:+.2f}%")
            print()

            # Test 5: Get table counts
            print("📋 Test 5: Database statistics")
            cursor.execute("""
                SELECT
                    schemaname,
                    tablename,
                    n_live_tup as row_count
                FROM pg_stat_user_tables
                WHERE schemaname = 'public'
                ORDER BY tablename;
            """)
            tables = cursor.fetchall()
            print("   Table Name                    | Rows")
            print("   " + "-" * 45)
            for table in tables:
                print(f"   {table['tablename']:30} | {table['row_count']:>6}")
            print()

        conn.close()
        print("✅ All tests passed! Database is working correctly.")
        return True

    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("   VNStock Analytics - PostgreSQL Database Test")
    print("=" * 60)
    print()

    success = test_connection()
    sys.exit(0 if success else 1)
