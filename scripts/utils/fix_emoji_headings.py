#!/usr/bin/env python3
"""
Fix headings with emojis that don't have data-i18n yet
"""
import re
import os

def fix_file(filepath):
    """Add data-i18n to headings with emojis"""
    mappings = [
        ('📈 Performance Heatmap', 'dashboard.performance_heatmap'),
        ('📊 Score Distribution', 'dashboard.score_distribution'),
        ('🕯️ Price & Volume Analysis', 'dashboard.price_volume_analysis'),
        ('📉 RSI Distribution', 'dashboard.rsi_distribution'),
        ('🎯 Sector Performance', 'dashboard.sector_performance'),
        ('📋 Detailed Stock Analysis', 'dashboard.detailed_analysis'),
        ('🎯 Select Stocks to Monitor', 'dashboard.select_stocks_monitor'),
    ]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        for text, key in mappings:
            # Pattern: <tag>emoji text</tag> without data-i18n
            pattern = rf'(<h[1-6])>(\s*){re.escape(text)}(\s*)</h[1-6]>'
            replacement = rf'\1 data-i18n="{key}">\2{text}\3</h\1>'

            # Check if already has data-i18n
            if f'data-i18n="{key}"' not in content:
                content = re.sub(pattern, replacement, content)

                # Also try with existing attributes
                pattern2 = rf'(<h[1-6]\s+(?![^>]*data-i18n)[^>]*?)>(\s*){re.escape(text)}(\s*)</h[1-6]>'
                def replace2(m):
                    return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</h>'
                content = re.sub(pattern2, replace2, content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            orig_count = original.count('data-i18n')
            new_count = content.count('data-i18n')
            added = new_count - orig_count
            print(f"✅ {filepath}: Added {added} emoji heading translations")
            return True
        else:
            print(f"⏭️  {filepath}: No emoji headings to update")
            return False

    except Exception as e:
        print(f"❌ Error: {filepath}: {e}")
        return False

def main():
    files = [
        'dashboard_main.html',
        'dashboard_history.html',
        'advanced_charts.html',
        'price_forecast.html',
        'dashboard_advanced.html',
    ]

    print("Fixing emoji headings...\n")

    updated = 0
    for filename in files:
        if os.path.exists(filename):
            if fix_file(filename):
                updated += 1
        else:
            print(f"⚠️  Not found: {filename}")

    print(f"\n📊 Updated {updated} files")

if __name__ == '__main__':
    main()
