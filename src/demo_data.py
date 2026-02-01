"""
Demo/Mock Data for Testing
Use this when VNDirect API is not accessible
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List


class DemoStockData:
    """Generate realistic demo stock data for testing"""

    # Realistic price ranges for Vietnamese stocks and commodities (in VND)
    STOCK_PRICES = {
        # Commodities (prices per gram in VND)
        'GOLD': {'base': 5500000, 'range': 500000},    # ~5.5M VND per gram
        'XAU': {'base': 5500000, 'range': 500000},     # Same as GOLD
        'SILVER': {'base': 75000, 'range': 10000},     # ~75K VND per gram
        'XAG': {'base': 75000, 'range': 10000},        # Same as SILVER

        # Vietnamese stocks
        'VPB': {'base': 23000, 'range': 2000},
        'STB': {'base': 28000, 'range': 3000},
        'HDB': {'base': 19000, 'range': 2000},
        'SHB': {'base': 14000, 'range': 1500},
        'MBB': {'base': 26000, 'range': 2500},
        'ACB': {'base': 26500, 'range': 2500},
        'FPT': {'base': 118000, 'range': 10000},
        'POW': {'base': 11500, 'range': 1000},
        'DGC': {'base': 16000, 'range': 1500},
        'GEX': {'base': 23500, 'range': 2000},
        'VCB': {'base': 90000, 'range': 8000},
        'VNM': {'base': 81000, 'range': 7000},
        'HPG': {'base': 30000, 'range': 3000},
        'VIC': {'base': 45000, 'range': 4000},
        'VHM': {'base': 55000, 'range': 5000}
    }

    @staticmethod
    def generate_current_price(symbol: str) -> Dict:
        """Generate realistic current price data"""
        if symbol not in DemoStockData.STOCK_PRICES:
            return None

        stock_info = DemoStockData.STOCK_PRICES[symbol]
        base_price = stock_info['base']
        price_range = stock_info['range']

        # Random price within range
        price = base_price + random.randint(-price_range//2, price_range//2)

        # Random daily change
        change_percent = random.uniform(-3.0, 3.0)
        change = price * (change_percent / 100)

        # Volume
        volume = random.randint(100000, 5000000) * 1000

        return {
            'symbol': symbol,
            'price': round(price, 0),
            'change': round(change, 0),
            'change_percent': round(change_percent, 2),
            'volume': volume,
            'high': round(price * 1.02, 0),
            'low': round(price * 0.98, 0),
            'open': round(price * (1 + random.uniform(-0.01, 0.01)), 0),
            'timestamp': datetime.now().isoformat(),
            'source': 'DEMO DATA'
        }

    @staticmethod
    def generate_historical_data(symbol: str, days: int = 60) -> List[Dict]:
        """Generate realistic historical price data"""
        if symbol not in DemoStockData.STOCK_PRICES:
            return []

        stock_info = DemoStockData.STOCK_PRICES[symbol]
        base_price = stock_info['base']

        history = []
        current_price = base_price

        # Generate data from oldest to newest
        for i in range(days, 0, -1):
            # Random walk
            daily_change = random.uniform(-0.03, 0.03)
            current_price *= (1 + daily_change)

            # Keep price within reasonable range
            if current_price < base_price * 0.7:
                current_price = base_price * 0.7
            elif current_price > base_price * 1.3:
                current_price = base_price * 1.3

            open_price = current_price * (1 + random.uniform(-0.01, 0.01))
            high_price = max(open_price, current_price) * (1 + random.uniform(0, 0.02))
            low_price = min(open_price, current_price) * (1 - random.uniform(0, 0.02))

            date = datetime.now() - timedelta(days=i)

            history.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': round(open_price, 0),
                'high': round(high_price, 0),
                'low': round(low_price, 0),
                'close': round(current_price, 0),
                'nmVolume': random.randint(100000, 5000000) * 1000,
                'symbol': symbol
            })

        return history


# Patch the real API with demo data
def use_demo_data():
    """Monkey patch the real stock data fetcher to use demo data"""
    import src.stock_data as stock_data_module

    original_class = stock_data_module.VNStockData

    class DemoVNStockData(original_class):
        """Demo version of VNStockData that uses mock data"""

        def get_stock_price(self, symbol: str):
            print(f"  [DEMO MODE] Generating demo data for {symbol}")
            return DemoStockData.generate_current_price(symbol)

        def get_historical_data(self, symbol: str, days: int = 30):
            return DemoStockData.generate_historical_data(symbol, days)

    # Replace the class
    stock_data_module.VNStockData = DemoVNStockData


if __name__ == "__main__":
    # Test demo data
    print("Demo Current Price:")
    print(DemoStockData.generate_current_price('VPB'))

    print("\nDemo Historical Data (last 5 days):")
    history = DemoStockData.generate_historical_data('VPB', days=5)
    for record in history:
        print(f"  {record['date']}: {record['close']} VND")
