#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collect historical stock data for stocks with insufficient data
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta
import time

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from vnstock import Vnstock
from config import get_database_connection

def collect_historical_data(symbol, days=90):
    """Collect historical data for a specific stock"""
    print(f"\nCollecting {days} days of historical data for {symbol}...")

    try:
        # Initialize vnstock
        stock = Vnstock().stock(symbol=symbol, source='VCI')

        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Fetch historical data
        df = stock.quote.history(
            start=start_date.strftime('%Y-%m-%d'),
            end=end_date.strftime('%Y-%m-%d')
        )

        if df is None or df.empty:
            print(f"  No data available for {symbol}")
            return 0

        print(f"  Fetched {len(df)} records")

        # Save to database
        conn = get_database_connection()
        cursor = conn.cursor()

        # Get stock ID
        cursor.execute("SELECT id FROM stocks WHERE symbol = %s;", (symbol,))
        result = cursor.fetchone()
        if not result:
            print(f"  Stock {symbol} not found in database")
            conn.close()
            return 0

        stock_id = result[0]

        # Prepare data for insertion
        inserted = 0
        for _, row in df.iterrows():
            try:
                cursor.execute("""
                    INSERT INTO stock_prices (stock_id, date, open, high, low, close, volume, change_percent)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (stock_id, date) DO UPDATE SET
                        open = EXCLUDED.open,
                        high = EXCLUDED.high,
                        low = EXCLUDED.low,
                        close = EXCLUDED.close,
                        volume = EXCLUDED.volume,
                        change_percent = EXCLUDED.change_percent;
                """, (
                    stock_id,
                    row['time'],
                    row.get('open', 0),
                    row.get('high', 0),
                    row.get('low', 0),
                    row.get('close', 0),
                    row.get('volume', 0),
                    row.get('changePercent', 0)
                ))
                inserted += 1
            except Exception as e:
                print(f"  Error inserting row: {e}")
                continue

        conn.commit()
        cursor.close()
        conn.close()

        print(f"  Saved {inserted} records to database")
        return inserted

    except Exception as e:
        print(f"  Error collecting data for {symbol}: {e}")
        return 0


def main():
    """Main execution"""
    print("=" * 70)
    print(" Collecting Historical Stock Data")
    print("=" * 70)

    # Get stocks with insufficient data (less than 30 days)
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.symbol, s.name, COUNT(sp.id) as data_points
        FROM stocks s
        LEFT JOIN stock_prices sp ON s.id = sp.stock_id
        WHERE s.is_active = TRUE
          AND s.symbol !~ '^[0-9]'  -- Exclude bonds/certificates (start with numbers)
          AND LENGTH(s.symbol) <= 5  -- Real stocks have 3-5 character symbols
        GROUP BY s.id, s.symbol, s.name
        HAVING COUNT(sp.id) < 30
        ORDER BY s.symbol;
    """)

    stocks = cursor.fetchall()
    conn.close()

    if not stocks:
        print("\nAll stocks have sufficient historical data!")
        return

    print(f"\nFound {len(stocks)} stocks with insufficient data (< 30 days)")
    print("\nCollecting 90 days of historical data for each stock...\n")

    success_count = 0
    fail_count = 0

    for symbol, name, current_points in stocks:
        print(f"\n{symbol} ({name})")
        print(f"  Current data points: {current_points}")

        inserted = collect_historical_data(symbol, days=90)

        if inserted > 0:
            success_count += 1
        else:
            fail_count += 1

        # Rate limiting
        time.sleep(3.5)

    print("\n" + "=" * 70)
    print(f"Collection complete!")
    print(f"  Success: {success_count} stocks")
    print(f"  Failed: {fail_count} stocks")
    print("=" * 70)


if __name__ == '__main__':
    main()
