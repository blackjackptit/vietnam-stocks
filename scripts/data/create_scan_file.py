#!/usr/bin/env python3
"""
Create a scan file with all stock data for the dashboard
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    data_dir = Path('data')
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    # Load watchlist
    with open('watchlist.json', 'r') as f:
        watchlist = json.load(f)

    print(f"📊 Creating scan file for {len(watchlist)} stocks...")

    all_results = {}

    for symbol in watchlist:
        current_file = data_dir / f"{symbol}_current.json"
        if current_file.exists():
            with open(current_file, 'r') as f:
                stock_data = json.load(f)
                all_results[symbol] = stock_data

    # Create scan result
    scan_result = {
        'timestamp': datetime.now().isoformat(),
        'recommendations': {
            'strong_buy': [],
            'buy': [],
            'hold': [],
            'sell': []
        },
        'all_results': all_results
    }

    # Save to output directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = output_dir / f"scan_{timestamp}.json"

    with open(output_file, 'w') as f:
        json.dump(scan_result, f, indent=2)

    print(f"✅ Created scan file: {output_file}")
    print(f"   Contains data for {len(all_results)} stocks")

if __name__ == "__main__":
    main()
