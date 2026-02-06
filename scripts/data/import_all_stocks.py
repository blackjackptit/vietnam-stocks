#!/usr/bin/env python3
"""
Import ALL stocks - Fetch real price data for all 202 stocks
Combines data fetching and database insertion
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from datetime import datetime, timedelta
import time
from vnstock import Vnstock
from config import get_database_connection

def fetch_stock_data(symbol, source='VCI'):
    """Fetch current stock data using vnstock"""
    try:
        stock = Vnstock().stock(symbol=symbol, source=source)

        # Get last 5 days of data
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

        quote = stock.quote.history(start=start_date, end=end_date)

        if quote.empty or len(quote) == 0:
            return None

        # Get latest data
        latest = quote.iloc[-1]

        # vnstock returns prices in thousands, multiply by 1000 for VND
        close_price = float(latest['close']) * 1000
        open_price = float(latest['open']) * 1000
        high_price = float(latest['high']) * 1000
        low_price = float(latest['low']) * 1000
        volume = int(latest['volume'])

        # Calculate change
        change = 0.0
        change_percent = 0.0

        if len(quote) >= 2:
            prev_close = float(quote.iloc[-2]['close']) * 1000
            change = close_price - prev_close
            change_percent = (change / prev_close) * 100

        return {
            'symbol': symbol,
            'price': close_price,
            'open': open_price,
            'high': high_price,
            'low': low_price,
            'volume': volume,
            'change': change,
            'change_percent': change_percent,
            'source': f'vnstock/{source}'
        }

    except Exception as e:
        return None

def save_to_database(symbol, data):
    """Save stock price to database"""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        # Get stock_id
        cursor.execute("SELECT id FROM stocks WHERE symbol = %s", (symbol,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            return False

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
        """, (stock_id, today, data['open'], data['high'], data['low'],
              data['price'], data['volume'], data['change'], data['change_percent']))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print(f"\n  DB Error: {e}")
        return False

def import_all_stocks():
    """Import all stocks from database"""

    conn = get_database_connection()
    cursor = conn.cursor()

    # Get all active stocks
    cursor.execute("""
        SELECT symbol, name FROM stocks
        WHERE is_active = TRUE
        ORDER BY symbol
    """)

    stocks = cursor.fetchall()
    conn.close()

    print("═" * 80)
    print("    📊 IMPORTING ALL STOCKS - FETCHING REAL PRICE DATA")
    print("═" * 80)
    print(f"Total stocks: {len(stocks)}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("═" * 80)
    print()

    success_count = 0
    failed_count = 0
    failed_stocks = []

    for i, (symbol, name) in enumerate(stocks, 1):
        # Skip commodities
        if symbol in ['GOLD', 'SILVER', 'XAU', 'XAG']:
            print(f"[{i:3d}/{len(stocks)}] {symbol:6s} ⊗ Skipped (commodity)")
            continue

        print(f"[{i:3d}/{len(stocks)}] {symbol:6s} ", end="", flush=True)

        # Try VCI first
        data = fetch_stock_data(symbol, source='VCI')

        # Fallback to TCBS
        if not data:
            print("VCI failed, trying TCBS... ", end="", flush=True)
            time.sleep(0.5)
            data = fetch_stock_data(symbol, source='TCBS')

        # Fallback to MSN
        if not data:
            print("TCBS failed, trying MSN... ", end="", flush=True)
            time.sleep(0.5)
            data = fetch_stock_data(symbol, source='MSN')

        if data:
            # Save to database
            if save_to_database(symbol, data):
                print(f"✅ {data['price']:>10,.0f} VND  {data['change_percent']:>+6.2f}%")
                success_count += 1
            else:
                print(f"⚠️  Fetched but DB save failed")
                failed_count += 1
                failed_stocks.append(symbol)
        else:
            print(f"❌ Failed (all sources)")
            failed_count += 1
            failed_stocks.append(symbol)

        # Progress update every 20 stocks
        if i % 20 == 0:
            print(f"\n   Progress: {success_count} success, {failed_count} failed\n")

        # Rate limiting
        time.sleep(0.3)

    print()
    print("═" * 80)
    print("    ✅ IMPORT COMPLETE")
    print("═" * 80)
    print(f"Success: {success_count} stocks")
    print(f"Failed:  {failed_count} stocks")
    print(f"Total:   {len(stocks)} stocks")
    print(f"Success Rate: {(success_count/len(stocks)*100):.1f}%")

    if failed_stocks:
        print(f"\nFailed stocks: {', '.join(failed_stocks)}")

    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("═" * 80)

if __name__ == "__main__":
    import_all_stocks()
