#!/usr/bin/env python3
"""
Import stock prices from manual CSV file
Use this when APIs are blocked
"""

import csv
import json
from datetime import datetime
import os

def import_from_csv(csv_file='manual_prices.csv'):
    """
    Import prices from CSV file

    CSV format:
    symbol,price,change_percent
    TPB,16900,1.2
    VCB,98500,-0.5
    """

    if not os.path.exists(csv_file):
        print(f"❌ File not found: {csv_file}")
        print()
        print("Create a file called 'manual_prices.csv' with format:")
        print("symbol,price,change_percent")
        print("TPB,16900,1.2")
        print("VCB,98500,-0.5")
        return

    success_count = 0

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            symbol = row['symbol'].strip().upper()
            price = float(row['price'])
            change_percent = float(row.get('change_percent', 0))

            # Calculate change
            change = price * change_percent / 100

            data = {
                'symbol': symbol,
                'price': price,
                'change': change,
                'change_percent': change_percent,
                'volume': 0,
                'high': 0,
                'low': 0,
                'open': 0,
                'timestamp': datetime.now().isoformat(),
                'source': 'Manual Entry'
            }

            # Save to file
            output_file = f'data/{symbol}_current.json'
            with open(output_file, 'w') as out:
                json.dump(data, out, indent=2)

            print(f"✅ {symbol:6s} {price:>10,.0f} VND ({change_percent:+.2f}%)")
            success_count += 1

    print()
    print(f"✅ Imported {success_count} stocks")
    print()
    print("🔄 Regenerating latest_data.json...")
    os.system('python3 generate_latest_data.py')
    print()
    print("✅ DONE! Refresh your browser to see updated prices")

if __name__ == '__main__':
    import_from_csv()
