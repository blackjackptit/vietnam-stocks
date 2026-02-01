#!/usr/bin/env python3
"""
Generate demo data for all stocks in watchlist
"""

import json
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

from src.demo_data import DemoStockData

def main():
    # Load watchlist
    watchlist_file = Path('watchlist.json')
    if not watchlist_file.exists():
        print("❌ watchlist.json not found")
        return

    with open(watchlist_file, 'r') as f:
        watchlist = json.load(f)

    print(f"📊 Generating demo data for {len(watchlist)} stocks...")

    # Create data directory if it doesn't exist
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)

    # Generate data for each stock
    success_count = 0
    demo = DemoStockData()

    for symbol in watchlist:
        try:
            # Generate current price
            current_price = demo.generate_current_price(symbol)
            if current_price is None:
                # For stocks not in STOCK_PRICES, use default pricing
                import random
                base_price = random.randint(10000, 100000)
                change_percent = random.uniform(-3.0, 3.0)
                change = base_price * (change_percent / 100)
                current_price = {
                    'symbol': symbol,
                    'price': round(base_price, 0),
                    'change': round(change, 0),
                    'change_percent': round(change_percent, 2),
                    'volume': random.randint(100000, 5000000) * 1000,
                    'high': round(base_price * 1.02, 0),
                    'low': round(base_price * 0.98, 0),
                    'open': round(base_price * (1 + random.uniform(-0.01, 0.01)), 0),
                    'timestamp': DemoStockData.generate_current_price('VCB')['timestamp'],
                    'source': 'DEMO DATA'
                }

            # Generate historical data
            historical_data = demo.generate_historical_data(symbol, days=90)
            if not historical_data:
                # Generate default historical data
                from datetime import datetime, timedelta
                historical_data = []
                base_price = current_price['price']
                for i in range(90, 0, -1):
                    date = datetime.now() - timedelta(days=i)
                    price = base_price * (1 + random.uniform(-0.02, 0.02))
                    historical_data.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'close': round(price, 0),
                        'open': round(price * (1 + random.uniform(-0.01, 0.01)), 0),
                        'high': round(price * 1.02, 0),
                        'low': round(price * 0.98, 0),
                        'volume': random.randint(100000, 5000000) * 1000
                    })

            # Save current price
            current_file = data_dir / f"{symbol}_current.json"
            with open(current_file, 'w') as f:
                json.dump(current_price, f, indent=2)

            # Save historical data
            history_file = data_dir / f"{symbol}_history.json"
            with open(history_file, 'w') as f:
                json.dump(historical_data, f, indent=2)

            success_count += 1
            if success_count % 20 == 0:
                print(f"  ✓ Generated data for {success_count} stocks...")

        except Exception as e:
            print(f"  ⚠️  Error generating data for {symbol}: {e}")

    print(f"\n✅ Successfully generated demo data for {success_count}/{len(watchlist)} stocks")
    print(f"📁 Data saved to: {data_dir.absolute()}")

if __name__ == "__main__":
    main()
