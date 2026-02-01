#!/usr/bin/env python3
"""
Add data-i18n attributes to HTML files - Simple approach
"""
import re
import os

def add_data_i18n(content, text, key, tag=''):
    """Add data-i18n attribute to elements containing specific text"""
    if not tag:
        # Try multiple tags
        tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'button', 'a', 'span', 'div', 'p', 'label', 'option', 'th', 'td', 'li']
        for t in tags:
            content = add_data_i18n(content, text, key, t)
        return content

    # Pattern: <tag ...>Text</tag> where tag doesn't have data-i18n
    # Case-insensitive match for text
    pattern = rf'<{tag}(\s[^>]*?)>(\s*){re.escape(text)}(\s*)</{tag}>'

    def replacer(match):
        attrs = match.group(1)
        before_space = match.group(2)
        after_space = match.group(3)
        # Check if already has data-i18n
        if 'data-i18n' in attrs:
            return match.group(0)
        # Add data-i18n attribute
        return f'<{tag}{attrs} data-i18n="{key}">{before_space}{text}{after_space}</{tag}>'

    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE)

    # Also handle self-contained pattern without existing attributes
    pattern2 = rf'<{tag}>(\s*){re.escape(text)}(\s*)</{tag}>'

    def replacer2(match):
        before_space = match.group(1)
        after_space = match.group(2)
        return f'<{tag} data-i18n="{key}">{before_space}{text}{after_space}</{tag}>'

    content = re.sub(pattern2, replacer2, content, flags=re.IGNORECASE)

    return content

# Main mapping
TRANSLATIONS = {
    # Page titles and headings
    'Vietnam Stock Analytics Platform': 'home.title',
    'Main Dashboard': 'nav.dashboard',
    'Historical Analysis': 'nav.history',
    'Price Forecast': 'nav.forecast',
    'Portfolio Analytics': 'portfolio.title',
    'Alerts System': 'nav.alerts',
    'Trading Automation': 'nav.automation',
    'Settings': 'nav.settings',

    # Subtitles
    'Professional stock market analysis and trading tools': 'home.subtitle',
    'Analyze historical stock performance and trends': 'history.subtitle',
    'Predict future stock prices using historical data': 'forecast.subtitle',
    'Advanced portfolio analysis and optimization': 'portfolio.subtitle',
    'Set up price alerts and notifications': 'alerts.subtitle',
    'Automate your trading strategies': 'automation.subtitle',
    'Configure your preferences and platform settings': 'settings.subtitle',

    # Common buttons
    'Apply Watchlist': 'dashboard.apply_watchlist',
    'Stock Picker': 'dashboard.stock_picker',
    'Select All': 'common.select_all',
    'Clear All': 'common.clear_all',
    'Save': 'common.save',
    'Cancel': 'common.cancel',
    'Apply': 'common.apply',
    'Reset': 'common.reset',
    'Filter': 'common.filter',
    'Analyze': 'dashboard.analyze',
    'Refresh': 'dashboard.refresh',
    'Export': 'dashboard.export',

    # Dashboard sections
    'Real-Time Market Overview': 'dashboard.real_time',
    'Price Overview': 'dashboard.price_overview',
    'Price Chart': 'dashboard.price_chart',
    'Volume Chart': 'dashboard.volume_chart',
    'Volume Analysis': 'dashboard.volume_analysis',
    'Performance Metrics': 'dashboard.performance_metrics',
    'Market Indicators': 'dashboard.market_indicators',
    'Stock Comparison': 'dashboard.stock_comparison',
    'Technical Indicators': 'dashboard.technical_indicators',
    'Moving Averages': 'dashboard.moving_averages',
    'Trend Analysis': 'dashboard.trend_analysis',
    'Portfolio Summary': 'dashboard.portfolio_summary',
    'Total Value': 'dashboard.total_value',
    'Risk Analysis': 'dashboard.risk_analysis',
    'Sector Allocation': 'dashboard.sector_allocation',
    'Top Performers': 'dashboard.top_performers',
    'Top Losers': 'dashboard.top_losers',

    # Categories
    'All Assets': 'category.all_assets',
    'All Stocks': 'category.all',
    'Commodities': 'category.commodities',
    'Blue Chips': 'category.blue_chips',
    'Banks': 'category.banks',
    'Real Estate': 'category.real_estate',
    'Technology': 'category.tech',
    'Consumer': 'category.consumer',
    'Oil & Gas': 'category.oil_gas',
    'Affordable': 'category.affordable',
    'Industrial': 'category.industrial',
    'Transportation': 'category.transportation',
    'Utilities': 'category.utilities',

    # Time periods
    'Last 7 Days': 'history.last_7_days',
    'Last 30 Days': 'history.last_30_days',
    'Last 90 Days': 'history.last_90_days',
    'Last Year': 'history.last_year',
    'Custom Range': 'history.custom_range',

    # Forecast
    'Select Stock': 'forecast.select_stock',
    'Forecast Period': 'forecast.forecast_period',
    'Generate Forecast': 'dashboard.generate_forecast',
    'Price Prediction': 'forecast.prediction',
    'Confidence Level': 'forecast.confidence',

    # Portfolio
    'Enter Budget': 'portfolio.enter_budget',
    'Budget Amount': 'portfolio.budget_amount',
    'Select Assets': 'portfolio.select_assets',
    'Asset Allocation': 'portfolio.allocation',
    'Optimize Portfolio': 'portfolio.optimize',

    # Alerts
    'Create Alert': 'alerts.create_alert',
    'Active Alerts': 'alerts.active_alerts',
    'Alert History': 'alerts.alert_history',
    'Target Price': 'alerts.target_price',
    'Current Price': 'alerts.current_price',

    # Automation
    'Create Strategy': 'automation.create_strategy',
    'Active Strategies': 'automation.active_strategies',
    'Strategy Name': 'automation.strategy_name',
    'Entry Conditions': 'automation.entry_conditions',
    'Exit Conditions': 'automation.exit_conditions',
    'Risk Management': 'automation.risk_management',
    'Stop Loss': 'automation.stop_loss',
    'Take Profit': 'automation.take_profit',
    'Backtest': 'automation.backtest',

    # Settings sections
    'Budget & Portfolio': 'settings.budget',
    'Data Refresh': 'settings.refresh',
    'API Configuration': 'settings.api',
    'Display Preferences': 'settings.display',
    'Alerts & Notifications': 'settings.alerts',
    'Trading Configuration': 'settings.trading',

    # Home
    'Total Stocks': 'home.total_stocks',
    'Total Assets': 'home.total_assets',
    'Get Started': 'home.get_started',

    # Special
    'LIVE': 'dashboard.live',
}

def process_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Apply all translations
        for text, key in TRANSLATIONS.items():
            content = add_data_i18n(content, text, key)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            # Count changes
            original_count = original.count('data-i18n')
            new_count = content.count('data-i18n')
            added = new_count - original_count

            print(f"✅ {filepath}: Added {added} data-i18n attributes")
            return True
        else:
            print(f"⏭️  {filepath}: No changes")
            return False

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    files = [
        'index.html',
        'dashboard_main.html',
        'dashboard_history.html',
        'advanced_charts.html',
        'price_forecast.html',
        'dashboard_advanced.html',
        'alerts_system.html',
        'trading_automation.html',
        'settings.html',
    ]

    print("Adding data-i18n attributes to HTML files...\n")

    updated = 0
    for filename in files:
        if os.path.exists(filename):
            if process_file(filename):
                updated += 1
        else:
            print(f"⚠️  File not found: {filename}")

    print(f"\n📊 Summary: Updated {updated} files")

if __name__ == '__main__':
    main()
