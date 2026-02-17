#!/usr/bin/env python3
"""
Stock Data Collection Job
Collects and updates stock prices hourly using vnstock library
"""

import sys
import os
from datetime import datetime, date, timedelta
from pathlib import Path
import time

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from vnstock import Vnstock
from config import (
    get_database_connection,
    DATA_SOURCES,
    COLLECTION_CONFIG
)
from psycopg2.extras import execute_values


class StockDataCollector:
    """Collects stock data and updates database using vnstock"""

    def __init__(self):
        # Load data sources from config
        self.sources = [DATA_SOURCES['primary'], DATA_SOURCES['fallback']]
        self.timeout = DATA_SOURCES['timeout']
        self.rate_limit_delay = COLLECTION_CONFIG['rate_limit_delay']
        self.max_retries = COLLECTION_CONFIG['max_retries']
        self.db_conn = None

    def get_active_stocks(self):
        """Get list of active stock symbols from database"""
        try:
            conn = get_database_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT symbol FROM stocks
                    WHERE is_active = TRUE
                    ORDER BY symbol
                """)
                symbols = [row[0] for row in cursor.fetchall()]
            conn.close()
            return symbols
        except Exception as e:
            print(f"Error getting active stocks: {e}")
            # Fallback to default list
            return ['VNM', 'VCB', 'FPT', 'HPG', 'GAS', 'VIC', 'VHM', 'MSN',
                    'ACB', 'BID', 'CTG', 'MBB', 'STB', 'TCB', 'VPB']

    def fetch_stock_price(self, symbol):
        """Fetch price for a single stock with fallback sources"""
        for source in self.sources:
            try:
                stock = Vnstock().stock(symbol=symbol, source=source)
                end_date = datetime.now().strftime('%Y-%m-%d')
                start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

                quote = stock.quote.history(start=start_date, end=end_date)

                if quote.empty or len(quote) == 0:
                    continue

                latest = quote.iloc[-1]

                # vnstock returns prices in thousands, multiply by 1000 for VND
                close_price = float(latest['close']) * 1000
                open_price = float(latest['open']) * 1000
                high_price = float(latest['high']) * 1000
                low_price = float(latest['low']) * 1000
                volume = int(latest['volume'])

                # Calculate change from previous day
                change = 0.0
                change_percent = 0.0

                if len(quote) >= 2:
                    prev_close = float(quote.iloc[-2]['close']) * 1000
                    change = close_price - prev_close
                    change_percent = (change / prev_close) * 100

                return {
                    'symbol': symbol,
                    'price': close_price,
                    'change': change,
                    'change_percent': change_percent,
                    'volume': volume,
                    'high': high_price,
                    'low': low_price,
                    'open': open_price,
                    'source': f'vnstock/{source}'
                }

            except Exception as e:
                # Try next source
                continue

        return None

    def collect_current_prices(self):
        """Collect current prices for all active stocks"""
        print("=" * 70)
        print(f"🔄 Collecting Stock Data - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        stocks = self.get_active_stocks()
        print(f"Fetching data for {len(stocks)} stocks using vnstock...")

        collected_data = []
        success_count = 0
        failed_stocks = []

        for i, symbol in enumerate(stocks, 1):
            print(f"[{i}/{len(stocks)}] {symbol}...", end=" ", flush=True)

            try:
                data = self.fetch_stock_price(symbol)
                if data and data['price'] > 0:
                    collected_data.append(data)
                    success_count += 1
                    print(f"✓ {data['price']:,.0f} VND")
                else:
                    failed_stocks.append(symbol)
                    print("✗ (no data)")
            except Exception as e:
                failed_stocks.append(symbol)
                print(f"✗ ({str(e)[:30]})")

            # Rate limiting from config
            time.sleep(self.rate_limit_delay)

        print()
        print(f"✅ Successfully collected: {success_count}/{len(stocks)}")
        if failed_stocks:
            print(f"❌ Failed: {', '.join(failed_stocks)}")

        return collected_data

    def save_to_database(self, data_list):
        """Save collected data to PostgreSQL"""
        if not data_list:
            print("No data to save")
            return

        try:
            conn = get_database_connection()
            print(f"\n💾 Saving {len(data_list)} records to database...")

            with conn.cursor() as cursor:
                # Prepare data for insertion
                records = []
                for data in data_list:
                    # Get stock_id
                    cursor.execute(
                        "SELECT id FROM stocks WHERE symbol = %s",
                        (data['symbol'],)
                    )
                    result = cursor.fetchone()
                    if not result:
                        print(f"⚠️  Stock {data['symbol']} not found in database, skipping")
                        continue

                    stock_id = result[0]
                    today = date.today()

                    records.append((
                        stock_id,
                        today,
                        data.get('open'),
                        data.get('high'),
                        data.get('low'),
                        data.get('price'),  # close price
                        data.get('volume'),
                        data.get('change_percent')
                    ))

                # Insert or update using ON CONFLICT
                if records:
                    execute_values(
                        cursor,
                        """
                        INSERT INTO stock_prices
                            (stock_id, date, open, high, low, close, volume, change_percent)
                        VALUES %s
                        ON CONFLICT (stock_id, date)
                        DO UPDATE SET
                            open = EXCLUDED.open,
                            high = EXCLUDED.high,
                            low = EXCLUDED.low,
                            close = EXCLUDED.close,
                            volume = EXCLUDED.volume,
                            change_percent = EXCLUDED.change_percent
                        """,
                        records
                    )
                    conn.commit()
                    print(f"✅ Saved {len(records)} price records")

            conn.close()
            return True

        except Exception as e:
            print(f"❌ Database error: {e}")
            if conn:
                conn.rollback()
                conn.close()
            return False

    def run(self):
        """Run the stock data collection job"""
        try:
            # Collect data
            data = self.collect_current_prices()

            # Save to database
            if data:
                self.save_to_database(data)
                print(f"\n✅ Job completed successfully at {datetime.now().strftime('%H:%M:%S')}")
            else:
                print("\n⚠️  No data collected")

        except Exception as e:
            print(f"\n❌ Job failed: {e}")
            raise


def main():
    """Main entry point"""
    collector = StockDataCollector()
    collector.run()


if __name__ == '__main__':
    main()
