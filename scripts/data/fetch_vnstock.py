#!/usr/bin/env python3
"""
Fetch REAL stock data using vnstock library
Vietnamese stock market data fetcher - works without VPN!
"""

import json
from datetime import datetime, timedelta
import time
import os
from vnstock import Vnstock

def fetch_stock_data(symbol, source='VCI'):
    """
    Fetch current stock data using vnstock

    Args:
        symbol: Stock symbol (e.g., 'TPB', 'VCB')
        source: Data source ('VCI', 'TCBS', or 'MSN')

    Returns:
        Dict with stock data or None if failed
    """
    try:
        stock = Vnstock().stock(symbol=symbol, source=source)

        # Get last 5 days of data to calculate change
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
            'timestamp': datetime.now().isoformat(),
            'source': 'vnstock/' + source
        }

    except Exception as e:
        print(f"  Error: {e}")
        return None

def fetch_all_stocks():
    """Fetch data for all stocks using vnstock"""

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
    print("📊 FETCHING REAL STOCK DATA USING VNSTOCK")
    print("=" * 80)
    print(f"Total stocks: {len(all_symbols)}")
    print("Data source: vnstock library (Vietnamese stock market)")
    print()

    success_count = 0
    failed_stocks = []

    for i, symbol in enumerate(all_symbols, 1):
        print(f"[{i:3d}/{len(all_symbols)}] {symbol:6s} ", end="", flush=True)

        # Try VCI first, fallback to TCBS
        data = fetch_stock_data(symbol, source='VCI')

        if not data:
            # Try TCBS as fallback
            data = fetch_stock_data(symbol, source='TCBS')

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

        # Rate limiting - be polite to the API
        time.sleep(0.5)

    print()
    print("=" * 80)
    print(f"✅ SUCCESS: {success_count}/{len(all_symbols)} stocks fetched")

    if failed_stocks:
        print(f"❌ FAILED: {len(failed_stocks)} stocks")
        if len(failed_stocks) <= 20:
            print(f"   {', '.join(failed_stocks)}")
        else:
            print(f"   {', '.join(failed_stocks[:20])} ... and {len(failed_stocks)-20} more")

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
        print("📊 Real market data from vnstock is now loaded")
        print("🔄 Refresh your browser to see REAL prices!")
        print()
        print("📝 Note: Prices are from the latest available trading day")
        print("=" * 80)

if __name__ == '__main__':
    fetch_all_stocks()
