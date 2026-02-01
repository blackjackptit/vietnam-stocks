#!/usr/bin/env python3
"""
Fetch stock data by scraping public HSX/Vietnamese stock websites
Uses web scraping when APIs are geo-blocked
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time
import re
import os

class HSXWebScraper:
    """Scrape stock data from public Vietnamese financial websites"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
        })

    def clean_price(self, price_str):
        """Clean price string to float"""
        if not price_str:
            return 0.0
        # Remove commas, spaces, and convert to float
        cleaned = re.sub(r'[,\s]', '', str(price_str))
        try:
            return float(cleaned) * 1000  # Convert to VND
        except:
            return 0.0

    def get_stock_from_cafef(self, symbol):
        """Scrape stock data from cafef.vn"""
        try:
            url = f"https://s.cafef.vn/hose/{symbol}-stock-price-overview.chn"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Try to extract price data from the page
                price_elem = soup.select_one('#price-matching .match-price')
                change_elem = soup.select_one('#price-matching .change')

                if price_elem:
                    price_text = price_elem.get_text(strip=True)
                    price = self.clean_price(price_text)

                    change = 0.0
                    change_percent = 0.0

                    if change_elem:
                        change_text = change_elem.get_text(strip=True)
                        parts = change_text.split('(')
                        if len(parts) >= 2:
                            change = self.clean_price(parts[0])
                            percent_str = parts[1].replace(')', '').replace('%', '')
                            try:
                                change_percent = float(percent_str)
                            except:
                                pass

                    return {
                        'symbol': symbol,
                        'price': price,
                        'change': change,
                        'change_percent': change_percent,
                        'volume': 0,
                        'high': 0,
                        'low': 0,
                        'open': 0,
                        'timestamp': datetime.now().isoformat(),
                        'source': 'Cafef.vn'
                    }
        except Exception as e:
            pass

        return None

    def get_stock_from_vietstock(self, symbol):
        """Try to get data from vietstock.vn"""
        try:
            url = f"https://finance.vietstock.vn/{symbol}/overview.htm"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                # Parse HTML to extract stock data
                soup = BeautifulSoup(response.text, 'html.parser')

                # Look for price elements (structure may vary)
                price_elem = soup.select_one('.price-value, .txt-price, [class*="price"]')

                if price_elem:
                    price = self.clean_price(price_elem.get_text(strip=True))

                    if price > 0:
                        return {
                            'symbol': symbol,
                            'price': price,
                            'change': 0,
                            'change_percent': 0,
                            'volume': 0,
                            'high': 0,
                            'low': 0,
                            'open': 0,
                            'timestamp': datetime.now().isoformat(),
                            'source': 'Vietstock'
                        }
        except Exception as e:
            pass

        return None

    def get_stock_price(self, symbol):
        """Try multiple sources to get stock price"""

        # Try cafef.vn first
        data = self.get_stock_from_cafef(symbol)
        if data and data['price'] > 0:
            return data

        # Try vietstock.vn
        data = self.get_stock_from_vietstock(symbol)
        if data and data['price'] > 0:
            return data

        return None

def main():
    """Fetch data from HSX via web scraping"""

    print("=" * 80)
    print("📊 FETCHING HSX DATA VIA WEB SCRAPING")
    print("=" * 80)
    print("⚠️  Note: Web scraping may be slower and less reliable than APIs")
    print()

    # Test with a few stocks first
    test_symbols = ['TPB', 'VCB', 'VPB', 'ACB', 'MBB', 'STB', 'HDB', 'TCB', 'CTG', 'BID']

    print(f"Testing with {len(test_symbols)} popular stocks...")
    print()

    scraper = HSXWebScraper()
    success_count = 0

    for symbol in test_symbols:
        print(f"{symbol:6s} ", end="", flush=True)

        data = scraper.get_stock_price(symbol)

        if data and data['price'] > 0:
            # Save to file
            output_file = f'data/{symbol}_current.json'
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)

            price_display = f"{data['price']:>10,.0f}"
            change_display = f"{data['change_percent']:>+6.2f}%" if data['change_percent'] != 0 else "  ----  "
            print(f"✅ {price_display} VND ({change_display}) [{data['source']}]")
            success_count += 1
        else:
            print(f"❌ Failed to fetch")

        time.sleep(1)  # Polite delay between requests

    print()
    print("=" * 80)

    if success_count > 0:
        print(f"✅ Successfully fetched {success_count}/{len(test_symbols)} stocks")
        print()
        print("🔄 Regenerating latest_data.json...")
        os.system('python3 generate_latest_data.py')
        print()
        print("✅ DONE! Check data folder for updated files")
        print("🔄 Refresh your browser to see real prices!")
    else:
        print("❌ Could not fetch any data")
        print()
        print("Possible reasons:")
        print("  - Websites are blocking automated access")
        print("  - Need VPN to Vietnam")
        print("  - Website structure has changed")
        print()
        print("Alternative: Run this from Vietnam network or use VPN")

    print("=" * 80)

if __name__ == '__main__':
    main()
