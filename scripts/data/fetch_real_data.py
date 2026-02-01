#!/usr/bin/env python3
"""
Fetch REAL current stock data from VNDirect API
Replaces demo/fake data with actual market prices
"""

import sys
import os
import json
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from src.stock_data import VNStockData

def fetch_real_data():
    """Fetch real data for all stocks"""

    # Load stock list
    with open('data/stock_categories.json', 'r') as f:
        categories = json.load(f)

    # Get all unique stock symbols
    all_symbols = set()
    for category, stocks in categories['categories'].items():
        if category != 'commodities':  # Skip commodities for now
            all_symbols.update(stocks)

    all_symbols = sorted(list(all_symbols))

    print("=" * 70)
    print(f"🔄 Fetching REAL market data for {len(all_symbols)} stocks")
    print("=" * 70)
    print()

    # Initialize fetcher
    fetcher = VNStockData()

    # Fetch data
    success_count = 0
    failed_stocks = []

    for i, symbol in enumerate(all_symbols, 1):
        print(f"[{i}/{len(all_symbols)}] Fetching {symbol}...", end=" ")

        try:
            data = fetcher.get_stock_price(symbol)

            if data:
                # Save to file
                output_file = f'data/{symbol}_current.json'
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=2)

                print(f"✅ {data['price']:,} VND ({data['change_percent']:+.2f}%)")
                success_count += 1
            else:
                print(f"❌ Failed")
                failed_stocks.append(symbol)

        except Exception as e:
            print(f"❌ Error: {e}")
            failed_stocks.append(symbol)

    print()
    print("=" * 70)
    print(f"✅ Successfully fetched {success_count}/{len(all_symbols)} stocks")

    if failed_stocks:
        print(f"❌ Failed: {len(failed_stocks)} stocks")
        print(f"   {', '.join(failed_stocks[:10])}" + (" ..." if len(failed_stocks) > 10 else ""))

    print("=" * 70)
    print()
    print("🔄 Regenerating latest_data.json...")

    # Regenerate latest_data.json
    os.system('python3 generate_latest_data.py')

    print()
    print("✅ DONE! Real market data is now loaded.")
    print("   Refresh your browser to see real prices!")

if __name__ == '__main__':
    fetch_real_data()
