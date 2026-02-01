#!/usr/bin/env python3
"""
Complete Stock Data Fetcher - Fetch ALL stocks with vnstock
Fetches both current prices and historical data for all Vietnamese stocks
"""

import json
from datetime import datetime, timedelta
import time
import os
from vnstock import Vnstock

def fetch_current_price(symbol, source='VCI'):
    """Fetch current price data"""
    try:
        stock = Vnstock().stock(symbol=symbol, source=source)
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

        quote = stock.quote.history(start=start_date, end=end_date)

        if quote.empty or len(quote) == 0:
            return None

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
        return None

def fetch_historical_data(symbol, source='VCI', days=90):
    """Fetch historical data"""
    try:
        stock = Vnstock().stock(symbol=symbol, source=source)
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        history = stock.quote.history(start=start_date, end=end_date)

        if history.empty or len(history) == 0:
            return None

        # Convert to our format
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

    # Get all stocks (excluding commodities)
    all_symbols = set()
    for category, stocks in categories_data['categories'].items():
        if category != 'commodities':
            all_symbols.update(stocks)

    all_symbols = sorted(list(all_symbols))

    # Check what we already have
    existing_current = set()
    existing_history = set()
    needs_current = []
    needs_history = []

    for symbol in all_symbols:
        current_file = f'data/{symbol}_current.json'
        history_file = f'data/{symbol}_history.json'

        # Check if current data exists and is from vnstock
        if os.path.exists(current_file):
            try:
                with open(current_file) as f:
                    data = json.load(f)
                    if 'vnstock' in data.get('source', ''):
                        existing_current.add(symbol)
                    else:
                        needs_current.append(symbol)
            except:
                needs_current.append(symbol)
        else:
            needs_current.append(symbol)

        # Check if history data exists
        if os.path.exists(history_file):
            existing_history.add(symbol)
        else:
            needs_history.append(symbol)

    print("=" * 80)
    print("📊 COMPLETE STOCK DATA FETCH")
    print("=" * 80)
    print(f"Total stocks: {len(all_symbols)}")
    print(f"\nCurrent prices:")
    print(f"  ✅ Already have (vnstock): {len(existing_current)}")
    print(f"  🔄 Need to fetch: {len(needs_current)}")
    print(f"\nHistorical data:")
    print(f"  ✅ Already have: {len(existing_history)}")
    print(f"  🔄 Need to fetch: {len(needs_history)}")
    print("=" * 80)
    print()

    # Fetch current prices
    if needs_current:
        print(f"📈 Fetching current prices for {len(needs_current)} stocks...")
        print()

        current_success = 0
        current_failed = []

        for i, symbol in enumerate(needs_current, 1):
            print(f"[{i:3d}/{len(needs_current)}] {symbol:6s} ", end="", flush=True)

            # Try VCI first
            data = fetch_current_price(symbol, source='VCI')

            if not data:
                # Try TCBS as fallback
                data = fetch_current_price(symbol, source='TCBS')

            if data and data['price'] > 0:
                # Save to file
                output_file = f'data/{symbol}_current.json'
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=2)

                price_display = f"{data['price']:>10,.0f}"
                change_display = f"{data['change_percent']:>+6.2f}%"
                color = "✅" if data['change_percent'] >= 0 else "🔴"

                print(f"{color} {price_display} VND ({change_display})")
                current_success += 1
            else:
                print(f"❌ No data")
                current_failed.append(symbol)

            # Rate limiting
            time.sleep(0.5)

        print()
        print(f"✅ Current prices: {current_success}/{len(needs_current)} fetched")
        if current_failed:
            print(f"❌ Failed: {', '.join(current_failed)}")
        print()

    # Fetch historical data
    if needs_history:
        print(f"📚 Fetching historical data for {len(needs_history)} stocks...")
        print()

        history_success = 0
        history_failed = []

        for i, symbol in enumerate(needs_history, 1):
            print(f"[{i:3d}/{len(needs_history)}] {symbol:6s} ", end="", flush=True)

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
                history_success += 1
            else:
                print(f"❌ No data")
                history_failed.append(symbol)

            # Rate limiting
            time.sleep(0.5)

        print()
        print(f"✅ Historical data: {history_success}/{len(needs_history)} fetched")
        if history_failed:
            print(f"❌ Failed: {', '.join(history_failed)}")
        print()

    # Regenerate latest_data.json
    if current_success > 0 or history_success > 0:
        print("🔄 Regenerating latest_data.json...")
        os.system('python3 generate_latest_data.py')
        print()

    print("=" * 80)
    print("✅ COMPLETE!")
    print("=" * 80)
    print(f"📊 Current prices: {len(existing_current) + current_success}/{len(all_symbols)}")
    print(f"📚 Historical data: {len(existing_history) + history_success}/{len(all_symbols)}")
    print("=" * 80)
    print()
    print("🎉 All available stock data has been fetched!")
    print("🔄 Refresh your browser to see updated data!")
    print()

if __name__ == '__main__':
    main()
