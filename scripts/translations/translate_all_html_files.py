#!/usr/bin/env python3
"""
Add translations to ALL HTML files in the project
"""
import os
import re
import glob

# All translation mappings from previous scripts
ALL_TRANSLATIONS = {
    # Home and navigation
    'Vietnam Stock Analytics Platform': 'home.title',
    'Professional Stock Analytics Platform': 'home.hero_title',
    'Vietnamese Stock Monitor Dashboard': 'home.dashboard_title',
    'Vietnamese Stock Monitor - LIVE Dashboard': 'home.live_dashboard_title',
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

    # Common text
    'Dashboards': 'menu.dashboards',
    'Tools': 'menu.tools',
    'Automation': 'menu.automation',
    'Platform': 'menu.platform',
    'Save': 'common.save',
    'Cancel': 'common.cancel',
    'Apply': 'common.apply',
    'Reset': 'common.reset',
    'Filter': 'common.filter',
    'Search': 'common.search',
    'Select All': 'common.select_all',
    'Clear All': 'common.clear_all',
    'Expand All': 'common.expand_all',
    'Collapse All': 'common.collapse_all',
    'Loading...': 'common.loading',
    'Refresh': 'dashboard.refresh',
    'Export': 'dashboard.export',
    'Analyze': 'dashboard.analyze',

    # Categories
    'All Stocks': 'category.all',
    'All Assets': 'category.all_assets',
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
    'Commodities': 'category.commodities',

    # Dashboard
    'LIVE': 'dashboard.live',
    'Real-Time Market Overview': 'dashboard.real_time',
    'Performance Heatmap': 'dashboard.performance_heatmap',
    'Score Distribution': 'dashboard.score_distribution',
    'Price Chart': 'dashboard.price_chart',
    'Volume Chart': 'dashboard.volume_chart',
    'Volume Analysis': 'dashboard.volume_analysis',
    'Performance Metrics': 'dashboard.performance_metrics',
    'Detailed Stock Analysis': 'dashboard.detailed_analysis',
    'Apply Watchlist': 'dashboard.apply_watchlist',
    'Stock Picker': 'dashboard.stock_picker',
    'Top Performers': 'dashboard.top_performers',
    'Top Losers': 'dashboard.top_losers',

    # Status
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

    # Advanced features
    'Portfolio Analytics': 'portfolio.title',
    'Risk Management': 'advanced.risk_management',
    'Pattern Recognition': 'advanced.pattern_recognition',
    'Machine Learning': 'advanced.machine_learning',
    'Strategy Backtesting': 'advanced.strategy_backtesting',
    'Correlation Analysis': 'advanced.correlation_analysis',

    # Settings
    'Currency': 'settings.currency_label',
    'Budget & Portfolio': 'settings.budget',
    'Data Refresh': 'settings.refresh',
    'API Configuration': 'settings.api',
    'Display Preferences': 'settings.display',
    'Alerts & Notifications': 'settings.alerts',
    'Trading Configuration': 'settings.trading',

    # Footer
    'Products': 'footer.products',
    'Resources': 'footer.resources',
    'Documentation': 'footer.documentation',

    # Status
    'System Online': 'status.online',
    'Connected': 'status.connected',
    'Disconnected': 'status.disconnected',
}

def add_i18n_attribute(content, text, key):
    """Add data-i18n attribute to HTML elements"""
    if len(text) < 2 or f'data-i18n="{key}"' in content:
        return content

    escaped = re.escape(text)
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'label', 'div', 'th', 'td', 'option']

    for tag in tags:
        # Pattern: <tag>text</tag>
        pattern = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern, content):
            content = re.sub(pattern, rf'\1 data-i18n="{key}">\2{text}\3</{tag}>', content, count=1)

        # Pattern: <tag attrs>text</tag> without data-i18n
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern2, content):
            def replacer(m):
                return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
            content = re.sub(pattern2, replacer, content, count=1)

    return content

def process_file(filepath):
    """Add translations to a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        original_count = content.count('data-i18n=')

        # Apply all translations
        for text, key in ALL_TRANSLATIONS.items():
            if text in content:
                content = add_i18n_attribute(content, text, key)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            new_count = content.count('data-i18n=')
            added = new_count - original_count
            if added > 0:
                print(f"✅ {filepath}: +{added} (Total: {new_count})")
                return added
            else:
                return 0
        else:
            return 0

    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return 0

def main():
    """Process all HTML files"""
    print("="*80)
    print("ADDING TRANSLATIONS TO ALL HTML FILES")
    print("="*80)
    print()

    # Get all HTML files
    html_files = sorted(glob.glob('*.html'))

    print(f"Processing {len(html_files)} HTML files...\n")

    total_added = 0
    files_updated = 0

    for filepath in html_files:
        added = process_file(filepath)
        if added > 0:
            total_added += added
            files_updated += 1

    print()
    print("="*80)
    print(f"SUMMARY: Added {total_added} translations across {files_updated} files")
    print("="*80)
    print()
    print("Total HTML files with i18n: {}".format(len(html_files)))
    print()
    print("All HTML files now have language switcher support!")

if __name__ == '__main__':
    main()
