#!/usr/bin/env python3
"""
Fix historical data - Refetch all history files with correct pricing from vnstock
"""

import json
from datetime import datetime, timedelta
import time
import os
from vnstock import Vnstock

def fetch_historical_data(symbol, source='VCI', days=90):
    """Fetch historical data with correct pricing"""
    try:
        stock = Vnstock().stock(symbol=symbol, source=source)
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        history = stock.quote.history(start=start_date, end=end_date)

        if history.empty or len(history) == 0:
            return None

        # Convert to our format with correct pricing (multiply by 1000)
        result = []
        for idx, row in history.iterrows():
            result.append({
                'date': row['time'].strftime('%Y-%m-%d') if hasattr(row['time'], 'strftime') else str(row['time'])[:10],
                'close': float(row['close']) * 1000,
                'open': float(row['open']) * 1000,
                'high': float(row['high']) * 1000,
                'low': float(row['low']) * 1000,
                'volume': int(row['volume'])
            })

        return result
    except Exception as e:
        return None

def main():
    # Load stock categories
    with open('data/stock_categories.json', 'r') as f:
        categories_data = json.load(f)

    # Get all stocks
    all_symbols = set()
    for category, stocks in categories_data['categories'].items():
        if category != 'commodities':
            all_symbols.update(stocks)

    all_symbols = sorted(list(all_symbols))

    print("=" * 80)
    print("🔄 FIXING HISTORICAL DATA PRICES")
    print("=" * 80)
    print(f"Refetching history for {len(all_symbols)} stocks with correct pricing...")
    print("=" * 80)
    print()

    success_count = 0
    failed_stocks = []

    for i, symbol in enumerate(all_symbols, 1):
        print(f"[{i:3d}/{len(all_symbols)}] {symbol:6s} ", end="", flush=True)

        # Try VCI first
        data = fetch_historical_data(symbol, source='VCI', days=90)

        if not data:
            # Try TCBS as fallback
            data = fetch_historical_data(symbol, source='TCBS', days=90)

        if data and len(data) > 0:
            # Save to file
            output_file = f'data/{symbol}_history.json'
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)

            print(f"✅ {len(data):3d} days")
            success_count += 1
        else:
            print(f"❌ No data")
            failed_stocks.append(symbol)

        # Rate limiting
        time.sleep(0.5)

    print()
    print("=" * 80)
    print(f"✅ SUCCESS: {success_count}/{len(all_symbols)} history files fixed")
    if failed_stocks:
        print(f"❌ FAILED: {', '.join(failed_stocks)}")
    print("=" * 80)
    print()
    print("🔄 Regenerating latest_data.json...")
    os.system('python3 generate_latest_data.py')
    print()
    print("=" * 80)
    print("✅ COMPLETE! All history files now have correct pricing.")
    print("🔄 Refresh your browser to see corrected charts!")
    print("=" * 80)

if __name__ == '__main__':
    main()
