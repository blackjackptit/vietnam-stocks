#!/usr/bin/env python3
"""
Generate latest_data.json from all *_current.json files
"""
import json
import os
from datetime import datetime
import glob

def generate_latest_data():
    """Aggregate all current stock data into latest_data.json"""
    data_dir = 'data'
    latest_data = {
        'timestamp': datetime.now().isoformat(),
        'total_stocks': 0,
        'stocks': {}
    }

    # Find all *_current.json files
    current_files = glob.glob(os.path.join(data_dir, '*_current.json'))

    for file_path in current_files:
        try:
            with open(file_path, 'r') as f:
                stock_data = json.load(f)
                symbol = stock_data.get('symbol')
                if symbol:
                    latest_data['stocks'][symbol] = stock_data
                    latest_data['total_stocks'] += 1
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Save to latest_data.json
    output_file = os.path.join(data_dir, 'latest_data.json')
    with open(output_file, 'w') as f:
        json.dump(latest_data, f, indent=2)

    print(f"✅ Generated {output_file}")
    print(f"   Total stocks: {latest_data['total_stocks']}")
    print(f"   Timestamp: {latest_data['timestamp']}")

    return latest_data

if __name__ == '__main__':
    generate_latest_data()
