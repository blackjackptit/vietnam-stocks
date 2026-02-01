#!/usr/bin/env python3
"""
Vietnamese Stock Monitor
Monitor stocks every 15 minutes and provide recommendations
"""

import sys
import os
import time
from datetime import datetime
import json

sys.path.insert(0, os.path.dirname(__file__))

from src.stock_data import VNStockData, STOCK_LISTS
from src.technical_analysis import TechnicalAnalyzer
from src.portfolio import Portfolio


class StockMonitor:
    """Monitor Vietnamese stocks and provide recommendations"""

    def __init__(self, budget: float = 10_000_000, watchlist: list = None):
        """
        Initialize monitor

        Args:
            budget: Investment budget in VND
            watchlist: List of stocks to monitor (default: load from watchlist.json or affordable stocks)
        """
        self.fetcher = VNStockData()
        self.analyzer = TechnicalAnalyzer()
        self.portfolio = Portfolio(budget=budget)

        # Initialize log file before loading watchlist
        self.log_file = f"logs/monitor_{datetime.now().strftime('%Y%m%d')}.log"
        os.makedirs("logs", exist_ok=True)

        # Load watchlist
        self.watchlist = watchlist or self.load_watchlist() or STOCK_LISTS['affordable']

    def load_watchlist(self):
        """Load watchlist from watchlist.json file"""
        watchlist_file = 'watchlist.json'
        if os.path.exists(watchlist_file):
            try:
                with open(watchlist_file, 'r') as f:
                    watchlist = json.load(f)
                if watchlist:
                    print(f"📋 Loaded {len(watchlist)} stocks from watchlist.json")
                    return watchlist
            except Exception as e:
                print(f"⚠️ Error loading watchlist: {e}")
        return None

    def log(self, message: str):
        """Log message to file and print"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')

    def analyze_stock(self, symbol: str) -> dict:
        """Analyze a single stock"""
        self.log(f"\nAnalyzing {symbol}...")

        # Get current price
        current_data = self.fetcher.get_stock_price(symbol)
        if not current_data:
            self.log(f"  ❌ Could not fetch data for {symbol}")
            return None

        # Get historical data
        historical = self.fetcher.get_historical_data(symbol, days=60)
        if len(historical) < 20:
            self.log(f"  ⚠️ Insufficient historical data for {symbol}")
            return current_data

        # Perform technical analysis
        analysis = self.analyzer.analyze_stock(historical)

        if 'error' in analysis:
            self.log(f"  ⚠️ Analysis error: {analysis['error']}")
            return current_data

        # Combine data
        result = {
            **current_data,
            'analysis': analysis
        }

        # Display results
        self.log(f"  Price: {current_data['price']:,.0f} VND ({current_data['change_percent']:+.2f}%)")
        self.log(f"  {analysis['emoji']} Recommendation: {analysis['recommendation']} (Score: {analysis['score']})")

        if analysis.get('indicators', {}).get('rsi'):
            self.log(f"  RSI: {analysis['indicators']['rsi']:.1f}")

        for signal in analysis['signals'][:3]:  # Show top 3 signals
            self.log(f"  {signal}")

        return result

    def scan_and_recommend(self):
        """Scan watchlist and provide top recommendations"""
        # Reload watchlist from file in case it changed
        watchlist = self.load_watchlist()
        if watchlist:
            self.watchlist = watchlist

        self.log("=" * 70)
        self.log(f"STOCK SCAN - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log("=" * 70)
        self.log(f"Monitoring {len(self.watchlist)} stocks: {', '.join(self.watchlist[:5])}{'...' if len(self.watchlist) > 5 else ''}")

        recommendations = {
            'strong_buy': [],
            'buy': [],
            'hold': [],
            'sell': []
        }

        # Analyze each stock
        all_results = {}
        for symbol in self.watchlist:
            result = self.analyze_stock(symbol)
            if result and 'analysis' in result:
                all_results[symbol] = result

                recommendation = result['analysis']['recommendation']
                if 'STRONG BUY' in recommendation:
                    recommendations['strong_buy'].append(result)
                elif 'BUY' in recommendation:
                    recommendations['buy'].append(result)
                elif 'SELL' in recommendation:
                    recommendations['sell'].append(result)
                else:
                    recommendations['hold'].append(result)

            time.sleep(1)  # Rate limiting

        # Generate report
        self.log("\n" + "=" * 70)
        self.log("RECOMMENDATIONS SUMMARY")
        self.log("=" * 70)

        # Strong Buy
        if recommendations['strong_buy']:
            self.log(f"\n🟢🟢 STRONG BUY ({len(recommendations['strong_buy'])} stocks):")
            for stock in sorted(recommendations['strong_buy'], key=lambda x: x['analysis']['score'], reverse=True):
                self.log(f"  • {stock['symbol']}: {stock['price']:,.0f} VND (Score: {stock['analysis']['score']})")

        # Buy
        if recommendations['buy']:
            self.log(f"\n🟢 BUY ({len(recommendations['buy'])} stocks):")
            for stock in sorted(recommendations['buy'], key=lambda x: x['analysis']['score'], reverse=True):
                self.log(f"  • {stock['symbol']}: {stock['price']:,.0f} VND (Score: {stock['analysis']['score']})")

        # Investment suggestion
        top_picks = recommendations['strong_buy'][:3] + recommendations['buy'][:2]
        if top_picks:
            self.log("\n" + "=" * 70)
            self.log("💰 INVESTMENT SUGGESTION FOR 10M VND BUDGET")
            self.log("=" * 70)

            current_prices = {stock['symbol']: stock['price'] for stock in all_results.values()}
            top_symbols = [stock['symbol'] for stock in top_picks]

            allocation = self.portfolio.suggest_allocation(top_symbols, current_prices)

            if 'suggestions' in allocation:
                self.log(f"\nAvailable: {allocation['available_budget']:,.0f} VND")
                self.log("\nSuggested allocation:")

                for suggestion in allocation['suggestions']:
                    symbol = suggestion['symbol']
                    stock_data = all_results.get(symbol, {})
                    analysis = stock_data.get('analysis', {})

                    self.log(f"\n  {symbol}")
                    self.log(f"    Price: {suggestion['price']:,.0f} VND")
                    self.log(f"    Buy: {suggestion['shares']} shares")
                    self.log(f"    Cost: {suggestion['total_cost']:,.0f} VND")
                    if analysis:
                        self.log(f"    Reason: {analysis['recommendation']} (Score: {analysis['score']})")
                        self.log(f"    Key signals: {', '.join(analysis['signals'][:2])}")

                self.log(f"\nTotal: {allocation['total_allocated']:,.0f} VND")
                self.log(f"Remaining: {allocation['available_budget'] - allocation['total_allocated']:,.0f} VND")

        # Risk warning
        self.log("\n" + "=" * 70)
        self.log("⚠️  IMPORTANT DISCLAIMER")
        self.log("=" * 70)
        self.log("This is NOT financial advice. Stock trading involves significant risk.")
        self.log("Past performance does not guarantee future results.")
        self.log("Always do your own research and consult a licensed financial advisor.")
        self.log("Only invest money you can afford to lose.")

        # Save results
        output_file = f"output/scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.makedirs("output", exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'recommendations': recommendations,
                'all_results': all_results
            }, f, indent=2, ensure_ascii=False)

        self.log(f"\nResults saved to: {output_file}")

        return recommendations

    def monitor_continuous(self, interval_minutes: int = 15):
        """
        Monitor stocks continuously

        Args:
            interval_minutes: Minutes between scans
        """
        self.log(f"\n🚀 Starting continuous monitoring (every {interval_minutes} minutes)")
        self.log(f"Watchlist: {', '.join(self.watchlist)}")
        self.log(f"Press Ctrl+C to stop\n")

        try:
            while True:
                self.scan_and_recommend()

                next_scan = datetime.now().timestamp() + (interval_minutes * 60)
                self.log(f"\nNext scan at: {datetime.fromtimestamp(next_scan).strftime('%H:%M:%S')}")
                self.log("Sleeping...")

                time.sleep(interval_minutes * 60)

        except KeyboardInterrupt:
            self.log("\n\n✋ Monitoring stopped by user")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Monitor Vietnamese stocks")
    parser.add_argument('--budget', type=float, default=10_000_000, help='Budget in VND (default: 10,000,000)')
    parser.add_argument('--interval', type=int, default=15, help='Monitoring interval in minutes (default: 15)')
    parser.add_argument('--watchlist', help='Comma-separated list of stock symbols (default: affordable stocks)')
    parser.add_argument('--scan-once', action='store_true', help='Run scan once and exit')
    parser.add_argument('--list-stocks', action='store_true', help='List available stock categories')

    args = parser.parse_args()

    if args.list_stocks:
        print("\n📊 Available Stock Lists:\n")
        for category, stocks in STOCK_LISTS.items():
            print(f"{category.upper()}:")
            print(f"  {', '.join(stocks)}\n")
        return

    # Parse watchlist
    watchlist = None
    if args.watchlist:
        if args.watchlist in STOCK_LISTS:
            watchlist = STOCK_LISTS[args.watchlist]
            print(f"Using {args.watchlist} watchlist: {', '.join(watchlist)}")
        else:
            watchlist = [s.strip().upper() for s in args.watchlist.split(',')]
            print(f"Custom watchlist: {', '.join(watchlist)}")

    # Create monitor
    monitor = StockMonitor(budget=args.budget, watchlist=watchlist)

    if args.scan_once:
        # Run once and exit
        monitor.scan_and_recommend()
    else:
        # Continuous monitoring
        monitor.monitor_continuous(interval_minutes=args.interval)


if __name__ == "__main__":
    main()
