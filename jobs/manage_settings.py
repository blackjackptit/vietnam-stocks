#!/usr/bin/env python3
"""
Settings Manager for Data Collection
View and update automation settings interactively
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import (
    DATA_COLLECTION,
    MARKET_HOURS,
    DATA_SOURCES,
    COLLECTION_CONFIG
)


def print_current_settings():
    """Display current settings"""
    print("=" * 80)
    print("📊 DATA COLLECTION AUTOMATION SETTINGS")
    print("=" * 80)
    print()

    # Global status
    status = "✅ ENABLED" if DATA_COLLECTION['enabled'] else "❌ DISABLED"
    print(f"Overall Status: {status}")
    print()

    # Stock collection
    print("─" * 80)
    print("📈 STOCK DATA COLLECTION")
    print("─" * 80)
    stock = DATA_COLLECTION['stock']
    print(f"  Enabled: {'✅ Yes' if stock['enabled'] else '❌ No'}")
    print(f"  Interval: {stock['interval']} seconds ({stock['interval'] // 60} minutes)")
    print(f"  Market Hours Only: {'Yes' if stock['market_hours_only'] else 'No'}")
    print(f"  End of Day Collection: {'Yes' if stock['end_of_day'] else 'No'}")
    print()

    # Indices collection
    print("─" * 80)
    print("📊 MARKET INDICES COLLECTION")
    print("─" * 80)
    indices = DATA_COLLECTION['indices']
    print(f"  Enabled: {'✅ Yes' if indices['enabled'] else '❌ No'}")
    print(f"  Interval: {indices['interval']} seconds ({indices['interval'] // 60} minutes)")
    print(f"  Market Hours Only: {'Yes' if indices['market_hours_only'] else 'No'}")
    print()

    # Macro collection
    print("─" * 80)
    print("🌍 MACRO INDICATORS COLLECTION")
    print("─" * 80)
    macro = DATA_COLLECTION['macro']
    print(f"  Enabled: {'✅ Yes' if macro['enabled'] else '❌ No'}")
    print(f"  Interval: {macro['interval']} seconds ({macro['interval'] // 3600} hours)")
    print(f"  Daily Update: {'Yes' if macro['daily_update'] else 'No'}")
    if macro['daily_update']:
        print(f"  Daily Update Time: {macro['daily_update_hour']}:00")
    print()

    # Market hours
    print("─" * 80)
    print("🕐 MARKET HOURS")
    print("─" * 80)
    print(f"  Trading Days: {MARKET_HOURS['days']}")
    print(f"  Open Hour: {MARKET_HOURS['open_hour']}:00")
    print(f"  Close Hour: {MARKET_HOURS['close_hour']}:00")
    print()

    # Data sources
    print("─" * 80)
    print("🔌 DATA SOURCES")
    print("─" * 80)
    print(f"  Primary Source: {DATA_SOURCES['primary']}")
    print(f"  Fallback Source: {DATA_SOURCES['fallback']}")
    print(f"  API Timeout: {DATA_SOURCES['timeout']} seconds")
    print()

    # Collection config
    print("─" * 80)
    print("⚙️  COLLECTION CONFIGURATION")
    print("─" * 80)
    print(f"  Rate Limit Delay: {COLLECTION_CONFIG['rate_limit_delay']} seconds")
    print(f"  Max Retries: {COLLECTION_CONFIG['max_retries']}")
    print(f"  Log File: {COLLECTION_CONFIG['log_file']}")
    print(f"  Log Level: {COLLECTION_CONFIG['log_level']}")
    print()

    print("=" * 80)


def show_quick_settings():
    """Show commonly changed settings"""
    print()
    print("=" * 80)
    print("⚡ QUICK SETTINGS GUIDE")
    print("=" * 80)
    print()
    print("Edit .env file to change these settings:")
    print()

    print("🔧 Enable/Disable Features:")
    print("  AUTO_COLLECT_ENABLED=true|false       - Master switch")
    print("  STOCK_COLLECTION_ENABLED=true|false   - Stock data collection")
    print("  INDEX_COLLECTION_ENABLED=true|false   - Market indices")
    print("  MACRO_COLLECTION_ENABLED=true|false   - Macro indicators")
    print()

    print("⏱️  Update Frequencies:")
    print("  STOCK_COLLECTION_INTERVAL=3600         - Stock data (seconds)")
    print("  INDEX_COLLECTION_INTERVAL=1800         - Indices (seconds)")
    print("  MACRO_COLLECTION_INTERVAL=3600         - Macro data (seconds)")
    print()

    print("🕐 Market Hours:")
    print("  MARKET_OPEN_HOUR=9                     - Market opens at 9 AM")
    print("  MARKET_CLOSE_HOUR=15                   - Market closes at 3 PM")
    print("  MARKET_DAYS=mon-fri                    - Trading days")
    print()

    print("📊 Common Presets:")
    print()
    print("  Aggressive (Every 30 min during market):")
    print("    STOCK_COLLECTION_INTERVAL=1800")
    print("    INDEX_COLLECTION_INTERVAL=900")
    print()
    print("  Standard (Hourly during market):")
    print("    STOCK_COLLECTION_INTERVAL=3600")
    print("    INDEX_COLLECTION_INTERVAL=1800")
    print()
    print("  Conservative (Every 2 hours):")
    print("    STOCK_COLLECTION_INTERVAL=7200")
    print("    INDEX_COLLECTION_INTERVAL=3600")
    print()

    print("After editing .env, restart the scheduler:")
    print("  ./jobs/manage_scheduler.sh restart")
    print()
    print("=" * 80)


def validate_settings():
    """Validate current settings"""
    print()
    print("=" * 80)
    print("✅ SETTINGS VALIDATION")
    print("=" * 80)
    print()

    issues = []
    warnings = []

    # Check if anything is enabled
    if not DATA_COLLECTION['enabled']:
        issues.append("Automated collection is disabled globally")

    if DATA_COLLECTION['enabled']:
        if not any([
            DATA_COLLECTION['stock']['enabled'],
            DATA_COLLECTION['indices']['enabled'],
            DATA_COLLECTION['macro']['enabled']
        ]):
            warnings.append("All collection types are disabled")

    # Check intervals
    if DATA_COLLECTION['stock']['interval'] < 300:  # Less than 5 minutes
        warnings.append("Stock collection interval is very frequent (< 5 minutes)")

    if DATA_COLLECTION['indices']['interval'] < 300:
        warnings.append("Indices collection interval is very frequent (< 5 minutes)")

    # Check market hours
    if MARKET_HOURS['open_hour'] >= MARKET_HOURS['close_hour']:
        issues.append("Market open hour must be before close hour")

    # Print results
    if not issues and not warnings:
        print("✅ All settings are valid!")
    else:
        if issues:
            print("❌ ISSUES:")
            for issue in issues:
                print(f"  • {issue}")
            print()

        if warnings:
            print("⚠️  WARNINGS:")
            for warning in warnings:
                print(f"  • {warning}")
            print()

    print("=" * 80)


def show_schedule_preview():
    """Show when jobs will run"""
    print()
    print("=" * 80)
    print("📅 SCHEDULE PREVIEW")
    print("=" * 80)
    print()

    if not DATA_COLLECTION['enabled']:
        print("❌ Automated collection is disabled")
        print()
        print("=" * 80)
        return

    print("Based on current settings, jobs will run:")
    print()

    # Stock collection
    if DATA_COLLECTION['stock']['enabled']:
        stock = DATA_COLLECTION['stock']
        interval_min = stock['interval'] // 60
        interval_hours = stock['interval'] // 3600

        if stock['market_hours_only']:
            if interval_hours >= 1:
                print(f"📈 Stock Data: Every {interval_hours} hour(s)")
            else:
                print(f"📈 Stock Data: Every {interval_min} minute(s)")
            print(f"   During: {MARKET_HOURS['days']} {MARKET_HOURS['open_hour']}:00 - {MARKET_HOURS['close_hour']}:00")

            if stock['end_of_day']:
                print(f"   Plus: End of day at {MARKET_HOURS['close_hour']}:30")
        else:
            print(f"📈 Stock Data: Every {interval_min} minutes (24/7)")
        print()

    # Indices collection
    if DATA_COLLECTION['indices']['enabled']:
        indices = DATA_COLLECTION['indices']
        interval_min = indices['interval'] // 60

        if indices['market_hours_only']:
            print(f"📊 Market Indices: Every {interval_min} minute(s)")
            print(f"   During: {MARKET_HOURS['days']} {MARKET_HOURS['open_hour']}:00 - {MARKET_HOURS['close_hour']}:00")
        else:
            print(f"📊 Market Indices: Every {interval_min} minutes (24/7)")
        print()

    # Macro collection
    if DATA_COLLECTION['macro']['enabled']:
        macro = DATA_COLLECTION['macro']
        interval_hours = macro['interval'] // 3600

        if macro['daily_update']:
            print(f"🌍 Macro Data: Daily at {macro['daily_update_hour']}:00")

        if macro['interval'] > 0 and macro['interval'] != 86400:
            print(f"🌍 Macro Data: Also every {interval_hours} hour(s)")
        print()

    print("=" * 80)


def main():
    """Main menu"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Manage data collection settings',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python manage_settings.py              # Show all settings
  python manage_settings.py --quick      # Show quick settings guide
  python manage_settings.py --validate   # Validate settings
  python manage_settings.py --schedule   # Preview schedule
  python manage_settings.py --all        # Show everything
        """
    )

    parser.add_argument('--quick', action='store_true',
                       help='Show quick settings guide')
    parser.add_argument('--validate', action='store_true',
                       help='Validate settings')
    parser.add_argument('--schedule', action='store_true',
                       help='Preview collection schedule')
    parser.add_argument('--all', action='store_true',
                       help='Show all information')

    args = parser.parse_args()

    if args.all:
        print_current_settings()
        show_schedule_preview()
        validate_settings()
        show_quick_settings()
    elif args.quick:
        show_quick_settings()
    elif args.validate:
        validate_settings()
    elif args.schedule:
        show_schedule_preview()
    else:
        # Default: show current settings
        print_current_settings()
        print()
        print("💡 Tip: Use --help to see more options")
        print("   Use --quick for quick settings guide")
        print("   Use --all to see everything")


if __name__ == '__main__':
    main()
