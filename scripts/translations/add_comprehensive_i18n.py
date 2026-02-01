#!/usr/bin/env python3
"""
Comprehensively add data-i18n attributes to ALL user-facing text in HTML files
"""
import re
import os

# Comprehensive translation mapping
TRANSLATIONS = {
    # Descriptions and subtitles
    'Real-time monitoring of 233 Vietnamese stocks with performance tracking': 'dashboard.monitoring_desc',
    'Select Stocks to Monitor': 'dashboard.select_stocks_monitor',
    'Search stocks by symbol or name...': 'dashboard.search_placeholder',
    'Customize your watchlist with stocks and commodities': 'dashboard.customize_watchlist',
    'Selected Assets:': 'dashboard.selected_assets',
    'items': 'common.items',

    # Chart titles
    'Performance Heatmap': 'dashboard.performance_heatmap',
    'Score Distribution': 'dashboard.score_distribution',
    'Price & Volume Analysis': 'dashboard.price_volume_analysis',
    'RSI Distribution': 'dashboard.rsi_distribution',
    'Sector Performance': 'dashboard.sector_performance',
    'Detailed Stock Analysis': 'dashboard.detailed_analysis',

    # Buttons
    'Expand All': 'common.expand_all',
    'Collapse All': 'common.collapse_all',

    # Market summary labels
    'Monitoring': 'dashboard.monitoring',
    'Strong Buy': 'dashboard.strong_buy',
    'Buy': 'dashboard.buy',
    'Hold': 'dashboard.hold',
    'Sell': 'dashboard.sell',
    'Avg Score': 'dashboard.avg_score',

    # Table headers
    'Symbol': 'table.symbol',
    'Price': 'table.price',
    'Change': 'table.change',
    'Volume': 'table.volume',
    'Score': 'table.score',
    'RSI': 'table.rsi',
    'Recommendation': 'table.recommendation',
    'Signals': 'table.signals',
    'Date': 'table.date',
    'Open': 'table.open',
    'High': 'table.high',
    'Low': 'table.low',
    'Close': 'table.close',
    'Action': 'table.action',
    'Type': 'table.type',
    'Name': 'table.name',
    'Value': 'table.value',
    'Quantity': 'table.quantity',
    'Average Price': 'table.avg_price',
    'Total Cost': 'table.total_cost',
    'Current Value': 'table.current_value',
    'Profit/Loss': 'table.profit_loss',
    'Return': 'table.return',

    # Loading messages
    'Loading...': 'common.loading',
    'Loading heatmap...': 'common.loading_heatmap',
    'Waiting for data...': 'common.waiting_data',
    'Loading stock data...': 'common.loading_stock_data',

    # Time periods (short versions)
    '7D': 'period.7d',
    '30D': 'period.30d',
    '90D': 'period.90d',
    '1Y': 'period.1y',

    # Previously added translations
    'Vietnam Stock Analytics Platform': 'home.title',
    'Main Dashboard': 'nav.dashboard',
    'Historical Analysis': 'nav.history',
    'Price Forecast': 'nav.forecast',
    'Portfolio Analytics': 'portfolio.title',
    'Alerts System': 'nav.alerts',
    'Trading Automation': 'nav.automation',
    'Settings': 'nav.settings',
    'Professional stock market analysis and trading tools': 'home.subtitle',
    'Analyze historical stock performance and trends': 'history.subtitle',
    'Predict future stock prices using historical data': 'forecast.subtitle',
    'Advanced portfolio analysis and optimization': 'portfolio.subtitle',
    'Set up price alerts and notifications': 'alerts.subtitle',
    'Automate your trading strategies': 'automation.subtitle',
    'Configure your preferences and platform settings': 'settings.subtitle',
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
    'Last 7 Days': 'history.last_7_days',
    'Last 30 Days': 'history.last_30_days',
    'Last 90 Days': 'history.last_90_days',
    'Last Year': 'history.last_year',
    'Custom Range': 'history.custom_range',
    'Select Stock': 'forecast.select_stock',
    'Forecast Period': 'forecast.forecast_period',
    'Generate Forecast': 'dashboard.generate_forecast',
    'Price Prediction': 'forecast.prediction',
    'Confidence Level': 'forecast.confidence',
    'Enter Budget': 'portfolio.enter_budget',
    'Budget Amount': 'portfolio.budget_amount',
    'Select Assets': 'portfolio.select_assets',
    'Asset Allocation': 'portfolio.allocation',
    'Optimize Portfolio': 'portfolio.optimize',
    'Create Alert': 'alerts.create_alert',
    'Active Alerts': 'alerts.active_alerts',
    'Alert History': 'alerts.alert_history',
    'Target Price': 'alerts.target_price',
    'Current Price': 'alerts.current_price',
    'Create Strategy': 'automation.create_strategy',
    'Active Strategies': 'automation.active_strategies',
    'Strategy Name': 'automation.strategy_name',
    'Entry Conditions': 'automation.entry_conditions',
    'Exit Conditions': 'automation.exit_conditions',
    'Risk Management': 'automation.risk_management',
    'Stop Loss': 'automation.stop_loss',
    'Take Profit': 'automation.take_profit',
    'Backtest': 'automation.backtest',
    'Budget & Portfolio': 'settings.budget',
    'Data Refresh': 'settings.refresh',
    'API Configuration': 'settings.api',
    'Display Preferences': 'settings.display',
    'Alerts & Notifications': 'settings.alerts',
    'Trading Configuration': 'settings.trading',
    'Total Stocks': 'home.total_stocks',
    'Total Assets': 'home.total_assets',
    'Get Started': 'home.get_started',
    'LIVE': 'dashboard.live',
    '💎 Commodities': 'category.commodities',
}

def add_i18n_attribute(content, text, key):
    """Add data-i18n attribute to elements containing text"""

    # Skip if text is too short or contains only special characters
    if len(text.strip()) < 2:
        return content

    escaped = re.escape(text)

    # List of tag types to process
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'label',
            'th', 'td', 'div', 'li', 'option']

    for tag in tags:
        # Pattern 1: <tag>Text</tag> (no attributes, no data-i18n)
        pattern1 = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        def replace1(m):
            return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
        content = re.sub(pattern1, replace1, content)

        # Pattern 2: <tag attrs>Text</tag> (has attributes, no data-i18n)
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        def replace2(m):
            return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
        content = re.sub(pattern2, replace2, content)

        # Pattern 3: For placeholder attributes
        if 'placeholder' in text.lower() or '...' in text:
            pattern3 = rf'(placeholder=)"([^"]*{re.escape(text.replace("...", ""))}[^"]*)"'
            def replace3(m):
                return f'{m.group(1)}"{m.group(2)}" data-i18n-placeholder="{key}"'
            content = re.sub(pattern3, replace3, content, flags=re.IGNORECASE)

    return content

def process_file(filepath):
    """Process single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Apply all translations
        for text, key in TRANSLATIONS.items():
            content = add_i18n_attribute(content, text, key)

        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            # Count additions
            orig_count = original.count('data-i18n')
            new_count = content.count('data-i18n')
            added = new_count - orig_count

            print(f"✅ {filepath}: Added {added} data-i18n attributes (Total: {new_count})")
            return True
        else:
            print(f"⏭️  {filepath}: No new attributes added")
            return False

    except Exception as e:
        print(f"❌ Error: {filepath}: {e}")
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
        'test_language.html',
    ]

    print("Adding comprehensive data-i18n attributes...\n")

    updated = 0
    for filename in files:
        if os.path.exists(filename):
            if process_file(filename):
                updated += 1
        else:
            print(f"⚠️  Not found: {filename}")

    print(f"\n📊 Updated {updated} files")

if __name__ == '__main__':
    main()
