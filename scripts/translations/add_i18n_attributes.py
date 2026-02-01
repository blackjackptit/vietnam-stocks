#!/usr/bin/env python3
"""
Add data-i18n attributes to HTML files for translation support
"""
import re
import os

# Mapping of English text to translation keys
TEXT_TO_KEY = {
    # Navigation
    'Home': 'nav.home',
    'Main Dashboard': 'nav.dashboard',
    'Historical Analysis': 'nav.history',
    'Advanced Charts': 'nav.charts',
    'Price Forecast': 'nav.forecast',
    'Portfolio': 'nav.portfolio',
    'Portfolio Analytics': 'portfolio.title',
    'Macro Analysis': 'nav.macro',
    'Alerts System': 'nav.alerts',
    'Trading Automation': 'nav.automation',
    'Settings': 'nav.settings',
    'Menu': 'nav.menu',

    # Common buttons
    'Loading...': 'common.loading',
    'Save': 'common.save',
    'Cancel': 'common.cancel',
    'Confirm': 'common.confirm',
    'Delete': 'common.delete',
    'Edit': 'common.edit',
    'Apply': 'common.apply',
    'Reset': 'common.reset',
    'Search': 'common.search',
    'Filter': 'common.filter',
    'Select All': 'common.select_all',
    'Clear All': 'common.clear_all',
    'OK': 'common.ok',
    'Close': 'common.close',

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

    # Dashboard
    'LIVE': 'dashboard.live',
    'Real-Time Market Overview': 'dashboard.real_time',
    'Apply Watchlist': 'dashboard.apply_watchlist',
    'Stock Picker': 'dashboard.stock_picker',
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
    'Select Stocks': 'dashboard.select_stocks',
    'Select Time Period': 'dashboard.select_time_period',
    'Generate Forecast': 'dashboard.generate_forecast',
    'Analyze': 'dashboard.analyze',
    'Refresh': 'dashboard.refresh',
    'Export': 'dashboard.export',
    'Watchlist': 'dashboard.watchlist',
    'Portfolio Summary': 'dashboard.portfolio_summary',
    'Total Value': 'dashboard.total_value',
    'Total Gain/Loss': 'dashboard.total_gain',
    'Diversification': 'dashboard.diversification',
    'Risk Analysis': 'dashboard.risk_analysis',
    'Sector Allocation': 'dashboard.sector_allocation',
    'Top Performers': 'dashboard.top_performers',
    'Top Losers': 'dashboard.top_losers',

    # Historical
    'Analyze historical stock performance and trends': 'history.subtitle',
    'Last 7 Days': 'history.last_7_days',
    'Last 30 Days': 'history.last_30_days',
    'Last 90 Days': 'history.last_90_days',
    'Last Year': 'history.last_year',
    'Custom Range': 'history.custom_range',
    'From Date': 'history.from_date',
    'To Date': 'history.to_date',
    'Compare Stocks': 'history.compare_stocks',
    'View Details': 'history.view_details',

    # Forecast
    'Predict future stock prices using historical data': 'forecast.subtitle',
    'Select Stock': 'forecast.select_stock',
    'Forecast Period': 'forecast.forecast_period',
    '7 Days': 'forecast.7_days',
    '30 Days': 'forecast.30_days',
    '90 Days': 'forecast.90_days',
    'Price Prediction': 'forecast.prediction',
    'Confidence Level': 'forecast.confidence',
    'Trend': 'forecast.trend',

    # Portfolio
    'Advanced portfolio analysis and optimization': 'portfolio.subtitle',
    'Enter Budget': 'portfolio.enter_budget',
    'Budget Amount': 'portfolio.budget_amount',
    'Currency': 'portfolio.currency',
    'Select Assets': 'portfolio.select_assets',
    'Asset Allocation': 'portfolio.allocation',
    'Optimize Portfolio': 'portfolio.optimize',
    'Rebalance': 'portfolio.rebalance',
    'Performance': 'portfolio.performance',
    'Returns': 'portfolio.returns',
    'Volatility': 'portfolio.volatility',
    'Sharpe Ratio': 'portfolio.sharpe_ratio',

    # Alerts
    'Set up price alerts and notifications': 'alerts.subtitle',
    'Create Alert': 'alerts.create_alert',
    'Active Alerts': 'alerts.active_alerts',
    'Alert History': 'alerts.alert_history',
    'Stock': 'alerts.stock',
    'Condition': 'alerts.condition',
    'Target Price': 'alerts.target_price',
    'Current Price': 'alerts.current_price',
    'Status': 'alerts.status',
    'Triggered': 'alerts.triggered',
    'Pending': 'alerts.pending',
    'Price Above': 'alerts.price_above',
    'Price Below': 'alerts.price_below',
    'Percent Change': 'alerts.percent_change',
    'Volume Spike': 'alerts.volume_spike',

    # Automation
    'Automate your trading strategies': 'automation.subtitle',
    'Create Strategy': 'automation.create_strategy',
    'Active Strategies': 'automation.active_strategies',
    'Strategy Name': 'automation.strategy_name',
    'Entry Conditions': 'automation.entry_conditions',
    'Exit Conditions': 'automation.exit_conditions',
    'Risk Management': 'automation.risk_management',
    'Stop Loss': 'automation.stop_loss',
    'Take Profit': 'automation.take_profit',
    'Position Size': 'automation.position_size',
    'Backtest': 'automation.backtest',
    'Activate': 'automation.activate',
    'Deactivate': 'automation.deactivate',

    # Home
    'Vietnam Stock Analytics Platform': 'home.title',
    'Professional stock market analysis and trading tools': 'home.subtitle',
    'Welcome to Vietnam Stock Analytics': 'home.welcome',
    'Total Stocks': 'home.total_stocks',
    'Total Assets': 'home.total_assets',
    'Categories': 'home.categories',
    'Get Started': 'home.get_started',
    'Features': 'home.features',
    'Learn More': 'home.learn_more',

    # Settings
    'Configure your preferences and platform settings': 'settings.subtitle',
    'Budget & Portfolio': 'settings.budget',
    'Data Refresh': 'settings.refresh',
    'API Configuration': 'settings.api',
    'Display Preferences': 'settings.display',
    'Alerts & Notifications': 'settings.alerts',
    'Trading Configuration': 'settings.trading',

    # Footer
    '© 2024 Vietnam Stock Analytics Platform': 'footer.copyright',
    'Dashboard': 'footer.dashboard',
    'Documentation': 'footer.docs',
}

def add_i18n_to_element(html_content):
    """Add data-i18n attributes to HTML elements"""
    modified = html_content

    for text, key in TEXT_TO_KEY.items():
        # Escape special regex characters in text
        escaped_text = re.escape(text)

        # Pattern for elements without data-i18n
        # Match: <tag>Text</tag> where tag doesn't already have data-i18n
        patterns = [
            # Headers (h1-h6)
            (rf'(<h[1-6](?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</h[1-6]>)',
             rf'\1{text}\2'.replace(f'<h', f'<h').replace('>', f' data-i18n="{key}">', 1)),

            # Buttons
            (rf'(<button(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</button>)',
             rf'\1{text}\2'.replace('<button', '<button').replace('>', f' data-i18n="{key}">', 1)),

            # Links
            (rf'(<a(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</a>)',
             rf'\1{text}\2'.replace('<a', '<a').replace('>', f' data-i18n="{key}">', 1)),

            # Spans
            (rf'(<span(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</span>)',
             rf'\1{text}\2'.replace('<span', '<span').replace('>', f' data-i18n="{key}">', 1)),

            # Divs
            (rf'(<div(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</div>)',
             rf'\1{text}\2'.replace('<div', '<div').replace('>', f' data-i18n="{key}">', 1)),

            # Paragraphs
            (rf'(<p(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</p>)',
             rf'\1{text}\2'.replace('<p', '<p').replace('>', f' data-i18n="{key}">', 1)),

            # Labels
            (rf'(<label(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</label>)',
             rf'\1{text}\2'.replace('<label', '<label').replace('>', f' data-i18n="{key}">', 1)),

            # Option elements
            (rf'(<option(?![^>]*data-i18n)[^>]*>)\s*{escaped_text}\s*(</option>)',
             rf'\1{text}\2'.replace('<option', '<option').replace('>', f' data-i18n="{key}">', 1)),
        ]

        for pattern, replacement in patterns:
            # Find and replace each occurrence
            matches = list(re.finditer(pattern, modified, re.IGNORECASE))
            for match in reversed(matches):  # Reverse to maintain positions
                matched_text = match.group(0)
                # Extract tag and add data-i18n
                if 'data-i18n' not in matched_text:
                    new_text = re.sub(r'(<\w+)', rf'\1 data-i18n="{key}"', matched_text, count=1)
                    modified = modified[:match.start()] + new_text + modified[match.end():]

    return modified

def process_html_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add i18n attributes
        modified_content = add_i18n_to_element(content)

        if modified_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"✅ Updated: {filepath}")
            return True
        else:
            print(f"⏭️  Skipped (no changes): {filepath}")
            return False
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    """Process all HTML dashboard files"""
    html_files = [
        'index.html',
        'dashboard_main.html',
        'dashboard_history.html',
        'advanced_charts.html',
        'price_forecast.html',
        'dashboard_advanced.html',
        'alerts_system.html',
        'trading_automation.html',
        'settings.html',
        'test_language.html',
    ]

    updated = 0
    for filename in html_files:
        if os.path.exists(filename):
            if process_html_file(filename):
                updated += 1
        else:
            print(f"⚠️  File not found: {filename}")

    print(f"\n📊 Summary: Updated {updated} files")

if __name__ == '__main__':
    main()
