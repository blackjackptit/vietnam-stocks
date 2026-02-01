#!/usr/bin/env python3
"""
Add COMPLETE translations to ALL visible text in all HTML files
"""
import re
import os

# Comprehensive mapping of ALL English text to translation keys
COMPLETE_TRANSLATIONS = {
    # Card descriptions
    'Real-time monitoring of 233 Vietnamese stocks with live updates, interactive visualization, technical scores, and comprehensive performance tracking.': 'home.dashboard_desc',
    'Deep dive into price history with moving averages, RSI, MACD, and volume analysis. Multiple timeframes from 30 days to 1 year.': 'home.history_desc',
    'Machine learning predictions using 4 models. Statistical control charts with anomaly detection and investment recommendations.': 'home.forecast_desc',
    'Portfolio optimization, strategy backtesting, risk management with VaR/CVaR, ML forecasting, and pattern recognition.': 'home.advanced_desc',
    'Institutional-grade charting with Ichimoku Cloud, Volume Profile, Stochastic, Fibonacci, Pivot Points, and more.': 'home.charts_desc',
    'Track global factors: oil prices, interest rates, geopolitical risks, policy changes, and their impact on Vietnamese stocks.': 'home.macro_desc',
    'Real-time monitoring with customizable alerts. Get notified when stocks hit target prices, RSI levels, or volume spikes.': 'home.alerts_desc',
    'Automated execution of trading strategies based on technical signals. Set custom rules for entry, exit, stop-loss, and position sizing.': 'home.automation_desc',

    # Feature descriptions
    '233 Vietnamese stocks and commodities with real-time data and historical analysis.': 'home.coverage_text',
    'Machine learning forecasts, anomaly detection, and automated investment recommendations.': 'home.ai_text',
    '30+ technical indicators, advanced charts, and institutional-grade analytics.': 'home.tools_text',
    'VaR, CVaR, portfolio optimization, and comprehensive risk analysis tools.': 'home.risk_text',

    # Tags
    'Real-time Updates': 'tag.realtime_updates',
    '9 Categories': 'tag.9_categories',
    'MA20/50': 'tag.ma20_50',
    'MACD': 'tag.macd',
    'Oil Impact': 'tag.oil_impact',
    'Geopolitics': 'tag.geopolitics',
    'Policy': 'tag.policy',
    'Notifications': 'tag.notifications',
    'Custom': 'tag.custom',
    'Rules': 'tag.rules',
    'Auto-Trade': 'tag.autotrade',

    # CTA Section
    'Start Analyzing Today': 'cta.title',
    'Join thousands of investors using professional analytics': 'cta.subtitle',
    'View All Features': 'cta.view_features',

    # Footer
    '© 2024 Vietnam Stock Analytics Platform. Built with advanced AI and data analytics.': 'footer.copyright_full',
    'For educational purposes only. Not financial advice. Trade at your own risk.': 'footer.disclaimer',

    # Already mapped
    'Vietnam Stock Analytics Platform': 'home.title',
    'Professional Stock Analytics Platform': 'home.hero_title',
    'Main Dashboard': 'nav.dashboard',
    'Historical Analysis': 'nav.history',
    'Advanced Charts': 'nav.charts',
    'Price Forecast': 'nav.forecast',
    'Portfolio Analytics': 'portfolio.title',
    'Alerts System': 'nav.alerts',
    'Trading Automation': 'nav.automation',
    'Settings': 'nav.settings',
    'Macro Analysis': 'nav.macro',
    'Home': 'nav.home',
    'Dashboards': 'menu.dashboards',
    'Tools': 'menu.tools',
    'Automation': 'menu.automation',
    'Platform': 'menu.platform',
    'All Stocks': 'category.all',
    'Blue Chips': 'category.blue_chips',
    'Banks': 'category.banks',
    'Real Estate': 'category.real_estate',
    'Technology': 'category.tech',
    'Consumer': 'category.consumer',
    'Oil & Gas': 'category.oil_gas',
    'Commodities': 'category.commodities',
    'LIVE': 'dashboard.live',
    'Real-Time Market Overview': 'dashboard.real_time',
    'Performance Heatmap': 'dashboard.performance_heatmap',
    'Save': 'common.save',
    'Cancel': 'common.cancel',
    'Apply': 'common.apply',
    'Reset': 'common.reset',
    'Filter': 'common.filter',
    'Select All': 'common.select_all',
    'Clear All': 'common.clear_all',
    'Monitoring': 'dashboard.monitoring',
    'Strong Buy': 'dashboard.strong_buy',
    'Buy': 'dashboard.buy',
    'Hold': 'dashboard.hold',
    'Sell': 'dashboard.sell',
    'Symbol': 'table.symbol',
    'Price': 'table.price',
    'Change': 'table.change',
    'Volume': 'table.volume',
    'Get Started': 'home.get_started',
    'Products': 'footer.products',
    'Resources': 'footer.resources',
    'Market Overview': 'footer.market_overview',
    'AI Forecast': 'footer.ai_forecast',
    'Quick Start Guide': 'footer.quick_start',
    'Features': 'footer.features',
    'User Guide': 'footer.user_guide',
    'Macro Guide': 'footer.macro_guide',
    'System Status': 'trading.system_status',
}

def add_i18n_to_element(content, text, key):
    """Add data-i18n attribute to HTML elements containing text"""
    if len(text) < 2:
        return content

    # Check if already has this translation
    if f'data-i18n="{key}"' in content:
        return content

    escaped = re.escape(text)

    # Try different tags
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'label', 'div']

    for tag in tags:
        # Pattern 1: <tag>text</tag>
        pattern1 = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern1, content):
            content = re.sub(pattern1, rf'\1 data-i18n="{key}">\2{text}\3</{tag}>', content, count=1)
            return content

        # Pattern 2: <tag attrs>text</tag> without data-i18n
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern2, content):
            def replacer(m):
                return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
            content = re.sub(pattern2, replacer, content, count=1)
            return content

    return content

def process_file(filepath):
    """Add all translations to a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        original_count = content.count('data-i18n=')

        # Apply all translations
        for text, key in COMPLETE_TRANSLATIONS.items():
            if text in content:
                content = add_i18n_to_element(content, text, key)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            new_count = content.count('data-i18n=')
            added = new_count - original_count
            if added > 0:
                print(f"✅ {filepath}: +{added} attributes (Total: {new_count})")
                return added

        return 0

    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return 0

def main():
    """Process all HTML files"""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    html_files.sort()

    print("="*80)
    print("ADDING COMPLETE TRANSLATIONS TO ALL HTML FILES")
    print("="*80)
    print()

    total_added = 0
    files_updated = 0

    for filepath in html_files:
        added = process_file(filepath)
        if added > 0:
            total_added += added
            files_updated += 1

    print()
    print("="*80)
    print(f"Added {total_added} translations across {files_updated} files")
    print("="*80)

if __name__ == '__main__':
    main()
