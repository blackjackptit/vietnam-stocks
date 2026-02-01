#!/usr/bin/env python3
"""
Fetch REAL stock data from HSX (Ho Chi Minh Stock Exchange)
Uses official HSX API endpoints
"""

import requests
import json
from datetime import datetime
import time
import os

class HSXDataFetcher:
    """Fetch data from HSX official sources"""

    # HSX API endpoints
    HSX_BASE = "https://iboard.hsx.vn"
    HSX_PRICE_API = "https://iboard.hsx.vn/securities/snapshot"
    HSX_LIST_API = "https://iboard.hsx.vn/securities/list"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.hsx.vn/'
        })

    def get_stock_price(self, symbol):
        """Get current price for a stock from HSX"""
        try:
            # Try HSX iBoard API
            url = f"{self.HSX_PRICE_API}?symbol={symbol}"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                # Parse HSX response format
                if data and 'data' in data:
                    stock = data['data']

                    return {
                        'symbol': symbol,
                        'price': float(stock.get('lastPrice', 0)) * 1000,  # HSX shows in thousands
                        'change': float(stock.get('change', 0)) * 1000,
                        'change_percent': float(stock.get('changePc', 0)),
                        'volume': int(stock.get('totalVol', 0)),
                        'high': float(stock.get('highPrice', 0)) * 1000,
                        'low': float(stock.get('lowPrice', 0)) * 1000,
                        'open': float(stock.get('openPrice', 0)) * 1000,
                        'timestamp': datetime.now().isoformat(),
                        'source': 'HSX'
                    }
        except Exception as e:
            print(f"HSX API error for {symbol}: {e}")

        # Try alternative: SSI iBoard (has HSX data)
        try:
            url = f"https://iboard-api.ssi.com.vn/statistics/charts/symbols/{symbol}"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                if data and 'data' in data:
                    stock = data['data'][0] if isinstance(data['data'], list) else data['data']

                    return {
                        'symbol': symbol,
                        'price': float(stock.get('closePrice', 0)) * 1000,
                        'change': float(stock.get('change', 0)) * 1000,
                        'change_percent': float(stock.get('changePc', 0)),
                        'volume': int(stock.get('totalVol', 0)),
                        'high': float(stock.get('highPrice', 0)) * 1000,
                        'low': float(stock.get('lowPrice', 0)) * 1000,
                        'open': float(stock.get('openPrice', 0)) * 1000,
                        'timestamp': datetime.now().isoformat(),
                        'source': 'SSI/HSX'
                    }
        except Exception as e:
            print(f"SSI API error for {symbol}: {e}")

        return None

def fetch_hsx_stocks():
    """Fetch data for all HSX stocks"""

    # Load stock categories
    with open('data/stock_categories.json', 'r') as f:
        categories_data = json.load(f)

    # Get all stocks (excluding commodities)
    all_symbols = set()
    for category, stocks in categories_data['categories'].items():
        if category != 'commodities':
            all_symbols.update(stocks)

    all_symbols = sorted(list(all_symbols))

    print("=" * 80)
    print("📊 FETCHING REAL DATA FROM HSX")
    print("=" * 80)
    print(f"Total stocks: {len(all_symbols)}")
    print()

    fetcher = HSXDataFetcher()

    success_count = 0
    failed_stocks = []

    for i, symbol in enumerate(all_symbols, 1):
        print(f"[{i}/{len(all_symbols)}] {symbol:6s} ", end="", flush=True)

        try:
            data = fetcher.get_stock_price(symbol)

            if data and data['price'] > 0:
                # Save to file
                output_file = f'data/{symbol}_current.json'
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=2)

                price_display = f"{data['price']:>10,.0f}"
                change_display = f"{data['change_percent']:>+6.2f}%"
                color = "✅" if data['change_percent'] >= 0 else "🔴"

                print(f"{color} {price_display} VND ({change_display}) [{data['source']}]")
                success_count += 1
            else:
                print(f"❌ No data")
                failed_stocks.append(symbol)

            # Rate limiting
            time.sleep(0.3)

        except Exception as e:
            print(f"❌ Error: {e}")
            failed_stocks.append(symbol)

    print()
    print("=" * 80)
    print(f"✅ SUCCESS: {success_count}/{len(all_symbols)} stocks fetched")

    if failed_stocks:
        print(f"❌ FAILED: {len(failed_stocks)} stocks")
        print(f"   {', '.join(failed_stocks[:20])}" + (" ..." if len(failed_stocks) > 20 else ""))

    print("=" * 80)

    if success_count > 0:
        print()
        print("🔄 Regenerating latest_data.json...")
        os.system('python3 generate_latest_data.py')

        print()
        print("=" * 80)
        print("✅ COMPLETE!")
        print("=" * 80)
        print()
        print("📊 Real market data is now loaded from HSX")
        print("🔄 Refresh your browser to see real prices!")
        print()
    else:
        print()
        print("⚠️  No data was fetched. Possible reasons:")
        print("   - HSX API is blocked from your location")
        print("   - Need VPN connection to Vietnam")
        print("   - API endpoints may have changed")

if __name__ == '__main__':
    fetch_hsx_stocks()
