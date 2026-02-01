#!/usr/bin/env python3
"""
Sync stock data from JSON files to PostgreSQL database
Loads current prices and historical data into database
"""

import json
import os
from datetime import datetime
from pathlib import Path
from config import get_database_connection
from psycopg2.extras import execute_values

def load_current_prices():
    """Load current stock prices from JSON files into database"""
    data_dir = Path(__file__).parent / 'data'
    conn = get_database_connection()
    cursor = conn.cursor()

    updated_count = 0
    error_count = 0

    print("Loading current prices into database...")

    for json_file in data_dir.glob('*_current.json'):
        try:
            with open(json_file) as f:
                data = json.load(f)

            symbol = data['symbol']
            price = data.get('price', 0)
            change = data.get('change', 0)
            change_percent = data.get('change_percent', 0)
            volume = data.get('volume', 0)
            high = data.get('high', price)
            low = data.get('low', price)
            open_price = data.get('open', price)

            # Get stock_id
            cursor.execute("SELECT id FROM stocks WHERE symbol = %s", (symbol,))
            result = cursor.fetchone()

            if not result:
                print(f"  ⚠️  Stock {symbol} not found in database, skipping...")
                error_count += 1
                continue

            stock_id = result[0]
            today = datetime.now().date()

            # Insert/update current price
            cursor.execute("""
                INSERT INTO stock_prices (stock_id, date, open, high, low, close, volume, change, change_percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (stock_id, date)
                DO UPDATE SET
                    open = EXCLUDED.open,
                    high = EXCLUDED.high,
                    low = EXCLUDED.low,
                    close = EXCLUDED.close,
                    volume = EXCLUDED.volume,
                    change = EXCLUDED.change,
                    change_percent = EXCLUDED.change_percent,
                    updated_at = NOW();
            """, (stock_id, today, open_price, high, low, price, volume, change, change_percent))

            updated_count += 1
            if updated_count % 10 == 0:
                print(f"  Loaded {updated_count} stocks...")

        except Exception as e:
            print(f"  ❌ Error loading {json_file.name}: {e}")
            error_count += 1
            continue

    conn.commit()
    conn.close()

    print(f"\n✅ Current prices loaded: {updated_count} stocks")
    if error_count > 0:
        print(f"⚠️  Errors: {error_count} stocks")

    return updated_count


def load_historical_prices(limit_per_stock=30):
    """Load historical stock prices from JSON files into database"""
    data_dir = Path(__file__).parent / 'data'
    conn = get_database_connection()
    cursor = conn.cursor()

    updated_count = 0
    error_count = 0

    print(f"\nLoading historical prices (last {limit_per_stock} days per stock)...")

    for json_file in data_dir.glob('*_history.json'):
        try:
            with open(json_file) as f:
                history_data = json.load(f)

            if not history_data or len(history_data) == 0:
                continue

            # Get symbol from first entry
            symbol = json_file.stem.replace('_history', '')

            # Get stock_id
            cursor.execute("SELECT id FROM stocks WHERE symbol = %s", (symbol,))
            result = cursor.fetchone()

            if not result:
                continue

            stock_id = result[0]

            # Prepare batch insert data (take last N days)
            values = []
            for entry in history_data[-limit_per_stock:]:
                try:
                    date_str = entry.get('date', entry.get('time', ''))
                    if not date_str:
                        continue

                    # Parse date
                    if 'T' in date_str:
                        date = datetime.fromisoformat(date_str.replace('Z', '+00:00')).date()
                    else:
                        date = datetime.strptime(date_str, '%Y-%m-%d').date()

                    open_price = float(entry.get('open', 0))
                    high = float(entry.get('high', 0))
                    low = float(entry.get('low', 0))
                    close = float(entry.get('close', entry.get('price', 0)))
                    volume = int(entry.get('volume', 0))
                    change = float(entry.get('change', 0))
                    change_percent = float(entry.get('change_percent', 0))

                    values.append((stock_id, date, open_price, high, low, close, volume, change, change_percent))
                except Exception as e:
                    continue

            if values:
                # Batch insert with conflict resolution
                execute_values(cursor, """
                    INSERT INTO stock_prices (stock_id, date, open, high, low, close, volume, change, change_percent)
                    VALUES %s
                    ON CONFLICT (stock_id, date)
                    DO UPDATE SET
                        open = EXCLUDED.open,
                        high = EXCLUDED.high,
                        low = EXCLUDED.low,
                        close = EXCLUDED.close,
                        volume = EXCLUDED.volume,
                        change = EXCLUDED.change,
                        change_percent = EXCLUDED.change_percent,
                        updated_at = NOW();
                """, values)

                updated_count += 1
                if updated_count % 10 == 0:
                    print(f"  Loaded history for {updated_count} stocks...")

        except Exception as e:
            print(f"  ❌ Error loading {json_file.name}: {e}")
            error_count += 1
            continue

    conn.commit()
    conn.close()

    print(f"\n✅ Historical data loaded: {updated_count} stocks")
    if error_count > 0:
        print(f"⚠️  Errors: {error_count} stocks")

    return updated_count


def main():
    """Main sync function"""
    print("=" * 60)
    print("  Syncing Stock Data: JSON Files → PostgreSQL")
    print("=" * 60)
    print()

    try:
        # Load current prices
        current_count = load_current_prices()

        # Load historical prices
        history_count = load_historical_prices(limit_per_stock=30)

        print("\n" + "=" * 60)
        print("  ✅ Sync Complete!")
        print("=" * 60)
        print(f"  Current prices: {current_count} stocks")
        print(f"  Historical data: {history_count} stocks")
        print("=" * 60)

        # Show sample data
        print("\nSample data from database:")
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.symbol, sp.date, sp.close, sp.volume
            FROM stock_prices sp
            JOIN stocks s ON sp.stock_id = s.id
            ORDER BY sp.date DESC
            LIMIT 5;
        """)
        print("\n  Symbol | Date       | Price    | Volume")
        print("  " + "-" * 45)
        for row in cursor.fetchall():
            print(f"  {row[0]:6} | {row[1]} | {row[2]:8.0f} | {row[3]:,}")
        conn.close()

        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
