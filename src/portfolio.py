"""
Portfolio Management for Vietnamese Stocks
Track holdings, calculate P&L, manage budget
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class Portfolio:
    """Manage stock portfolio"""

    def __init__(self, budget: float = 10_000_000, portfolio_file: str = "data/portfolio.json"):
        """
        Initialize portfolio

        Args:
            budget: Initial budget in VND
            portfolio_file: Path to portfolio JSON file
        """
        self.budget = budget
        self.initial_budget = budget
        self.portfolio_file = portfolio_file
        self.holdings = {}  # symbol -> {shares, avg_price, total_cost}
        self.transactions = []
        self.load_portfolio()

    def load_portfolio(self):
        """Load portfolio from file"""
        if os.path.exists(self.portfolio_file):
            try:
                with open(self.portfolio_file, 'r') as f:
                    data = json.load(f)
                    self.budget = data.get('budget', self.budget)
                    self.initial_budget = data.get('initial_budget', self.initial_budget)
                    self.holdings = data.get('holdings', {})
                    self.transactions = data.get('transactions', [])
            except Exception as e:
                print(f"Error loading portfolio: {e}")

    def save_portfolio(self):
        """Save portfolio to file"""
        os.makedirs(os.path.dirname(self.portfolio_file), exist_ok=True)

        data = {
            'budget': self.budget,
            'initial_budget': self.initial_budget,
            'holdings': self.holdings,
            'transactions': self.transactions,
            'last_updated': datetime.now().isoformat()
        }

        with open(self.portfolio_file, 'w') as f:
            json.dump(data, f, indent=2)

    def buy_stock(self, symbol: str, price: float, shares: int, fee_percent: float = 0.15) -> Dict:
        """
        Buy stock

        Args:
            symbol: Stock symbol
            price: Purchase price per share
            shares: Number of shares
            fee_percent: Trading fee percentage

        Returns:
            Transaction result
        """
        total_cost = price * shares
        fee = total_cost * (fee_percent / 100)
        total_with_fee = total_cost + fee

        if total_with_fee > self.budget:
            return {
                'success': False,
                'message': f"Insufficient funds. Need {total_with_fee:,.0f} VND, have {self.budget:,.0f} VND"
            }

        # Update holdings
        if symbol in self.holdings:
            holding = self.holdings[symbol]
            total_shares = holding['shares'] + shares
            total_investment = holding['total_cost'] + total_with_fee
            avg_price = total_investment / total_shares

            self.holdings[symbol] = {
                'shares': total_shares,
                'avg_price': round(avg_price, 2),
                'total_cost': total_investment
            }
        else:
            self.holdings[symbol] = {
                'shares': shares,
                'avg_price': price,
                'total_cost': total_with_fee
            }

        # Update budget
        self.budget -= total_with_fee

        # Record transaction
        transaction = {
            'type': 'BUY',
            'symbol': symbol,
            'price': price,
            'shares': shares,
            'fee': fee,
            'total': total_with_fee,
            'timestamp': datetime.now().isoformat()
        }
        self.transactions.append(transaction)

        self.save_portfolio()

        return {
            'success': True,
            'message': f"Bought {shares} shares of {symbol} at {price:,.0f} VND",
            'transaction': transaction,
            'remaining_budget': self.budget
        }

    def sell_stock(self, symbol: str, price: float, shares: int, fee_percent: float = 0.15) -> Dict:
        """
        Sell stock

        Args:
            symbol: Stock symbol
            price: Selling price per share
            shares: Number of shares
            fee_percent: Trading fee percentage

        Returns:
            Transaction result
        """
        if symbol not in self.holdings:
            return {'success': False, 'message': f"Don't own {symbol}"}

        holding = self.holdings[symbol]
        if holding['shares'] < shares:
            return {
                'success': False,
                'message': f"Insufficient shares. Have {holding['shares']}, trying to sell {shares}"
            }

        total_revenue = price * shares
        fee = total_revenue * (fee_percent / 100)
        total_after_fee = total_revenue - fee

        # Calculate profit/loss
        cost_basis = holding['avg_price'] * shares
        profit_loss = total_after_fee - cost_basis
        profit_loss_percent = (profit_loss / cost_basis) * 100

        # Update holdings
        holding['shares'] -= shares
        if holding['shares'] == 0:
            del self.holdings[symbol]
        else:
            self.holdings[symbol] = holding

        # Update budget
        self.budget += total_after_fee

        # Record transaction
        transaction = {
            'type': 'SELL',
            'symbol': symbol,
            'price': price,
            'shares': shares,
            'fee': fee,
            'total': total_after_fee,
            'profit_loss': profit_loss,
            'profit_loss_percent': round(profit_loss_percent, 2),
            'timestamp': datetime.now().isoformat()
        }
        self.transactions.append(transaction)

        self.save_portfolio()

        return {
            'success': True,
            'message': f"Sold {shares} shares of {symbol} at {price:,.0f} VND",
            'profit_loss': profit_loss,
            'profit_loss_percent': profit_loss_percent,
            'transaction': transaction,
            'remaining_budget': self.budget
        }

    def get_portfolio_value(self, current_prices: Dict[str, float]) -> Dict:
        """
        Calculate current portfolio value

        Args:
            current_prices: Dictionary mapping symbols to current prices

        Returns:
            Portfolio valuation
        """
        holdings_value = 0
        holdings_details = []

        for symbol, holding in self.holdings.items():
            current_price = current_prices.get(symbol, holding['avg_price'])
            market_value = current_price * holding['shares']
            profit_loss = market_value - holding['total_cost']
            profit_loss_percent = (profit_loss / holding['total_cost']) * 100

            holdings_details.append({
                'symbol': symbol,
                'shares': holding['shares'],
                'avg_price': holding['avg_price'],
                'current_price': current_price,
                'cost': holding['total_cost'],
                'value': market_value,
                'profit_loss': profit_loss,
                'profit_loss_percent': round(profit_loss_percent, 2)
            })

            holdings_value += market_value

        total_value = self.budget + holdings_value
        total_profit_loss = total_value - self.initial_budget
        total_profit_loss_percent = (total_profit_loss / self.initial_budget) * 100

        return {
            'cash': self.budget,
            'holdings_value': holdings_value,
            'total_value': total_value,
            'total_profit_loss': total_profit_loss,
            'total_profit_loss_percent': round(total_profit_loss_percent, 2),
            'holdings': holdings_details
        }

    def suggest_allocation(self, target_stocks: List[str], current_prices: Dict[str, float]) -> Dict:
        """
        Suggest how to allocate budget across stocks

        Args:
            target_stocks: List of stock symbols to invest in
            current_prices: Current prices of stocks

        Returns:
            Allocation suggestion
        """
        available = self.budget
        num_stocks = len(target_stocks)

        if num_stocks == 0 or available < 1_000_000:
            return {'error': 'Insufficient budget or no stocks selected'}

        allocation_per_stock = available / num_stocks
        suggestions = []

        for symbol in target_stocks:
            price = current_prices.get(symbol, 0)
            if price == 0:
                continue

            # Calculate how many shares we can buy
            # Account for trading fee (0.15%)
            max_shares = int((allocation_per_stock * 0.9985) / price)

            if max_shares > 0:
                total_cost = price * max_shares * 1.0015  # Including fee

                suggestions.append({
                    'symbol': symbol,
                    'price': price,
                    'shares': max_shares,
                    'total_cost': total_cost
                })

        return {
            'available_budget': available,
            'allocation_per_stock': allocation_per_stock,
            'suggestions': suggestions,
            'total_allocated': sum(s['total_cost'] for s in suggestions)
        }


if __name__ == "__main__":
    # Example usage
    portfolio = Portfolio(budget=10_000_000)

    print(f"Initial budget: {portfolio.budget:,.0f} VND")

    # Simulate buying
    result = portfolio.buy_stock('VCB', 90_000, 50)
    print(f"\n{result['message']}")
    print(f"Remaining: {result['remaining_budget']:,.0f} VND")

    # Check portfolio value
    current_prices = {'VCB': 92_000}
    valuation = portfolio.get_portfolio_value(current_prices)
    print(f"\nPortfolio value: {valuation['total_value']:,.0f} VND")
    print(f"P/L: {valuation['total_profit_loss']:,.0f} VND ({valuation['total_profit_loss_percent']:.2f}%)")
