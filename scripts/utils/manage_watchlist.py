#!/usr/bin/env python3
"""
Watchlist Manager
Manage your custom stock watchlist
"""

import json
import os
from pathlib import Path
from src.stock_data import STOCK_LISTS, get_all_symbols


WATCHLIST_FILE = Path('watchlist.json')


def load_watchlist():
    """Load watchlist from file"""
    if WATCHLIST_FILE.exists():
        with open(WATCHLIST_FILE, 'r') as f:
            return json.load(f)
    return []


def save_watchlist(watchlist):
    """Save watchlist to file"""
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f, indent=2)
    print(f"✅ Watchlist saved ({len(watchlist)} stocks)")


def add_stocks(symbols):
    """Add stocks to watchlist"""
    watchlist = set(load_watchlist())
    added = []

    for symbol in symbols:
        symbol = symbol.upper().strip()
        if symbol not in watchlist:
            watchlist.add(symbol)
            added.append(symbol)

    save_watchlist(sorted(list(watchlist)))

    if added:
        print(f"✅ Added: {', '.join(added)}")
    else:
        print("ℹ️  No new stocks added")


def remove_stocks(symbols):
    """Remove stocks from watchlist"""
    watchlist = set(load_watchlist())
    removed = []

    for symbol in symbols:
        symbol = symbol.upper().strip()
        if symbol in watchlist:
            watchlist.remove(symbol)
            removed.append(symbol)

    save_watchlist(sorted(list(watchlist)))

    if removed:
        print(f"✅ Removed: {', '.join(removed)}")
    else:
        print("ℹ️  No stocks removed")


def list_watchlist():
    """Display current watchlist"""
    watchlist = load_watchlist()

    if not watchlist:
        print("📭 Watchlist is empty")
        return

    print(f"\n📊 Current Watchlist ({len(watchlist)} stocks):")
    print("=" * 60)

    # Group by category
    categorized = {}
    for category, stocks in STOCK_LISTS.items():
        if category == 'all_stocks':
            continue
        matching = [s for s in watchlist if s in stocks]
        if matching:
            categorized[category] = matching

    for category, stocks in categorized.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        print(f"  {', '.join(stocks)}")

    uncategorized = [s for s in watchlist if not any(s in stocks for stocks in STOCK_LISTS.values())]
    if uncategorized:
        print(f"\nOTHER:")
        print(f"  {', '.join(uncategorized)}")

    print("\n" + "=" * 60)


def clear_watchlist():
    """Clear all stocks from watchlist"""
    save_watchlist([])
    print("✅ Watchlist cleared")


def add_category(category):
    """Add all stocks from a category"""
    if category not in STOCK_LISTS:
        print(f"❌ Unknown category: {category}")
        print(f"Available: {', '.join(STOCK_LISTS.keys())}")
        return

    stocks = STOCK_LISTS[category]
    add_stocks(stocks)


def interactive_mode():
    """Interactive menu for managing watchlist"""
    print("\n" + "=" * 60)
    print("📊 Vietnamese Stock Watchlist Manager")
    print("=" * 60)

    while True:
        print("\n🎯 Options:")
        print("  1. List watchlist")
        print("  2. Add stocks")
        print("  3. Remove stocks")
        print("  4. Add category")
        print("  5. Clear watchlist")
        print("  6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == '1':
            list_watchlist()

        elif choice == '2':
            symbols = input("Enter stock symbols (comma-separated): ").strip()
            if symbols:
                add_stocks([s.strip() for s in symbols.split(',')])

        elif choice == '3':
            symbols = input("Enter stock symbols to remove (comma-separated): ").strip()
            if symbols:
                remove_stocks([s.strip() for s in symbols.split(',')])

        elif choice == '4':
            print(f"\nAvailable categories:")
            for cat in STOCK_LISTS.keys():
                if cat != 'all_stocks':
                    print(f"  - {cat}")
            category = input("\nEnter category name: ").strip().lower()
            if category:
                add_category(category)

        elif choice == '5':
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                clear_watchlist()

        elif choice == '6':
            print("\n✅ Goodbye!")
            break

        else:
            print("❌ Invalid choice")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Manage Vietnamese stock watchlist')
    parser.add_argument('--list', action='store_true', help='List current watchlist')
    parser.add_argument('--add', nargs='+', help='Add stocks to watchlist')
    parser.add_argument('--remove', nargs='+', help='Remove stocks from watchlist')
    parser.add_argument('--category', help='Add all stocks from a category')
    parser.add_argument('--clear', action='store_true', help='Clear watchlist')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')

    args = parser.parse_args()

    if args.list:
        list_watchlist()
    elif args.add:
        add_stocks(args.add)
    elif args.remove:
        remove_stocks(args.remove)
    elif args.category:
        add_category(args.category)
    elif args.clear:
        clear_watchlist()
    elif args.interactive:
        interactive_mode()
    else:
        # Default to interactive if no args
        interactive_mode()


if __name__ == "__main__":
    main()
