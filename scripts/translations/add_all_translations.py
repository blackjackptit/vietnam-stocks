#!/usr/bin/env python3
"""
Add comprehensive data-i18n attributes to all missing content
"""
import re
import os

# Complete mapping of text to translation keys
COMPREHENSIVE_MAPPINGS = {
    # Home page
    'Professional Stock Analytics Platform': 'home.hero_title',
    'Institutional-grade tools for Vietnamese market investors': 'home.hero_subtitle',
    'Trading & Analytics Tools': 'home.trading_tools',
    'AI Price Forecast': 'home.ai_forecast',
    'Advanced Analytics': 'home.advanced_analytics',
    'Professional Charts': 'home.professional_charts',
    'Macro Analysis': 'home.macro_analysis',
    'Price Alerts': 'home.price_alerts',
    'Why Choose Our Platform': 'home.why_choose',
    'Comprehensive Coverage': 'home.comprehensive',
    'AI-Powered Insights': 'home.ai_insights',
    'Real-Time Data': 'home.real_time',
    'Advanced Tools': 'home.advanced_tools',

    # Menu items
    'Dashboards': 'menu.dashboards',
    'All Dashboards': 'menu.all_dashboards',
    '📊 Market Analysis': 'menu.market_analysis',
    '💼 Investment Tools': 'menu.investment_tools',
    '🔔 Automation & Alerts': 'menu.automation_alerts',
    '⚙️ Configuration': 'menu.configuration',
    'Tools': 'menu.tools',
    'Automation': 'menu.automation',
    'Platform': 'menu.platform',
    'Market Analysis': 'menu.market_analysis',
    'Investment Tools': 'menu.investment_tools',
    'Automation & Alerts': 'menu.automation_alerts',
    'Configuration': 'menu.configuration',

    # Page headings
    '📊 Main Dashboard - Real-Time Market Overview': 'page.main_dashboard',
    'Historical Price Analysis': 'page.historical_price',
    '📊 Advanced Charts & Technical Analysis': 'page.advanced_charts',
    '🚀 Advanced Analytics Dashboard': 'page.advanced_analytics',
    '🔔 Price Alerts System': 'page.price_alerts_system',
    '🤖 Automated Trading Configuration': 'page.trading_automation',

    # Charts
    '🕯️ Candlestick Chart with Moving Averages': 'charts.candlestick',
    '📊 Volume Bars': 'charts.volume_bars',
    '📊 Volume Profile': 'charts.volume_profile',
    '💹 On-Balance Volume (OBV)': 'charts.obv',
    '💰 Money Flow Index (MFI)': 'charts.mfi',
    '☁️ Ichimoku Cloud': 'charts.ichimoku',
    '📈 Stochastic Oscillator': 'charts.stochastic',
    '📉 Williams %R': 'charts.williams',
    '🎯 Rate of Change (ROC)': 'charts.roc',
    '📈 MACD': 'charts.macd',
    '📈 RSI (Relative Strength Index)': 'charts.rsi',

    # Sections
    '📂 Filter by Category': 'filter.by_category',
    'Filter by Category': 'filter.by_category',
    '📊 Technical Indicators': 'section.technical_indicators',
    'Technical Indicators': 'section.technical_indicators',
    '📊 Volume Analysis': 'section.volume_analysis',
    '🎯 Analysis & Signals': 'section.analysis_signals',
    'Analysis & Signals': 'section.analysis_signals',
    '📊 Price Statistics': 'section.price_statistics',
    'Price Statistics': 'section.price_statistics',
    '📊 Technical Signals': 'section.technical_signals',
    'Technical Signals': 'section.technical_signals',
    '📊 Current Stock Information': 'section.current_stock_info',
    'Current Stock Information': 'section.current_stock_info',
    '🎯 Forecast Metrics': 'section.forecast_metrics',
    'Forecast Metrics': 'section.forecast_metrics',
    '🤖 Model Comparison': 'section.model_comparison',
    'Model Comparison': 'section.model_comparison',
    '📋 Daily Predictions': 'section.daily_predictions',
    'Daily Predictions': 'section.daily_predictions',
    '🤖 AI Investment Recommendations': 'section.ai_recommendations',
    'AI Investment Recommendations': 'section.ai_recommendations',
    '🎯 Statistical Process Control Chart & Anomaly Detection': 'section.spc_chart',

    # Advanced features
    '🎯 Advanced Features': 'advanced.title',
    'Advanced Features': 'advanced.title',
    '📊 Portfolio Analytics': 'advanced.portfolio_analytics',
    '⏮️ Strategy Backtesting': 'advanced.strategy_backtesting',
    'Strategy Backtesting': 'advanced.strategy_backtesting',
    '⚠️ Risk Management': 'advanced.risk_management',
    '🔍 Pattern Recognition': 'advanced.pattern_recognition',
    'Pattern Recognition': 'advanced.pattern_recognition',
    '🤖 Machine Learning': 'advanced.machine_learning',
    'Machine Learning': 'advanced.machine_learning',
    '🔗 Correlation Analysis': 'advanced.correlation_analysis',
    'Correlation Analysis': 'advanced.correlation_analysis',
    '💰 Budget Allocation & Investment Plan': 'advanced.budget_allocation',
    'Budget Allocation & Investment Plan': 'advanced.budget_allocation',

    # Alerts
    '➕ Create New Alert': 'alerts.create_new',
    'Create New Alert': 'alerts.create_new',
    '🔥 Recently Triggered Alerts': 'alerts.recently_triggered',
    'Recently Triggered Alerts': 'alerts.recently_triggered',
    '📋 Active Alerts': 'alerts.active_alerts',

    # Trading
    '📊 System Status': 'trading.system_status',
    'System Status': 'trading.system_status',
    '🔌 Broker API Configuration': 'trading.broker_api',
    'Broker API Configuration': 'trading.broker_api',
    '📋 Trading Rules': 'trading.rules',
    'Trading Rules': 'trading.rules',
    'Active Rules': 'trading.active_rules',
    '🛡️ Risk Management': 'advanced.risk_management',
    '📜 Trade Execution Log': 'trading.execution_log',
    'Trade Execution Log': 'trading.execution_log',
    '🧪 Backtesting & Simulation': 'trading.backtest_simulation',
    'Backtesting & Simulation': 'trading.backtest_simulation',
    '🧪 Backtest Results': 'trading.backtest_results',
    'Backtest Results': 'trading.backtest_results',
    '📈 Equity Curve': 'trading.equity_curve',
    'Equity Curve': 'trading.equity_curve',

    # Settings
    '⚙️ Settings': 'settings.title',
    '💰 Budget & Portfolio': 'settings.budget',
    '🔄 Data Refresh': 'settings.refresh',
    '🔌 API Configuration': 'settings.api',
    '🎨 Display Preferences': 'settings.display',
    '🔔 Alerts & Notifications': 'settings.alerts',
    '📊 Trading Configuration': 'settings.trading',

    # Buttons
    '🔔 Create Alert': 'button.create_alert',
    'Reset to Defaults': 'button.reset_defaults',
    'Save Settings': 'button.save_settings',
    '📊 Dashboards ▼': 'menu.dashboards',

    # Menu links
    '📊 VNStock Analytics': 'home.title',
    '📉 Advanced Charts': 'nav.charts',
    '🔮 Price Forecasting': 'nav.forecast',
    'Price Forecasting': 'nav.forecast',
    '🌍 Macro Analysis': 'nav.macro',
    '🔔 Price Alerts': 'alerts.title',
    '🔮 Price Forecast': 'nav.forecast',
}

def add_i18n_to_html(content, text, key):
    """Add data-i18n attribute to HTML elements"""
    escaped = re.escape(text)

    # Try different tag patterns
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'button', 'a', 'span', 'div', 'label', 'p']

    for tag in tags:
        # Pattern: <tag>text</tag> without data-i18n
        pattern = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern, content) and f'data-i18n="{key}"' not in content:
            replacement = rf'\1 data-i18n="{key}">\2{text}\3</{tag}>'
            content = re.sub(pattern, replacement, content, count=1)

        # Pattern: <tag attrs>text</tag> without data-i18n
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern2, content):
            def replacer(m):
                return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
            content = re.sub(pattern2, replacer, content, count=1)

    return content

def process_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        original_count = content.count('data-i18n=')

        # Add all mappings
        for text, key in COMPREHENSIVE_MAPPINGS.items():
            if text in content and f'data-i18n="{key}"' not in content:
                content = add_i18n_to_html(content, text, key)

        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            new_count = content.count('data-i18n=')
            added = new_count - original_count
            print(f"✅ {filepath}: Added {added} attributes (Total: {new_count})")
            return True
        else:
            print(f"⏭️  {filepath}: No new attributes")
            return False

    except Exception as e:
        print(f"❌ Error {filepath}: {e}")
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

    print("Adding comprehensive translations to all HTML files...\n")

    updated = 0
    for filename in files:
        if os.path.exists(filename):
            if process_file(filename):
                updated += 1
        else:
            print(f"⚠️  Not found: {filename}")

    print(f"\n📊 Updated {updated} files")
    print("\nRe-run check_translations.py to verify coverage!")

if __name__ == '__main__':
    main()
