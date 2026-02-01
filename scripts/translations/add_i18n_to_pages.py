#!/usr/bin/env python3
"""
Add i18n support to all dashboard pages
"""

import os
import re

DASHBOARD_FILES = [
    'index.html',
    'dashboard_main.html',
    'dashboard_history.html',
    'advanced_charts.html',
    'price_forecast.html',
    'dashboard_advanced.html',
    'macro_analysis.html',
    'alerts_system.html',
    'trading_automation.html',
    'settings.html'
]

def add_i18n_script(content):
    """Add i18n.js and currency.js scripts if not present"""
    if 'i18n.js' in content:
        return content, False

    # Add before closing </head> tag
    if '</head>' in content:
        scripts = '''    <script src="js/i18n.js"></script>
    <script src="js/currency.js"></script>
'''
        content = content.replace('</head>', scripts + '</head>', 1)
        return content, True

    return content, False

def check_settings_in_menu(content):
    """Check if settings link exists in dropdown menu"""
    if '<a href="settings.html"' in content and 'dropdown-item' in content:
        return True
    return False

def update_file(filepath):
    """Update a single file"""
    print(f"Processing {filepath}...")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        changes = []

        # Add i18n script
        content, added = add_i18n_script(content)
        if added:
            changes.append('added i18n & currency scripts')

        # Check settings link
        has_settings = check_settings_in_menu(content)
        if not has_settings:
            print(f"  ⚠️  Warning: Settings link may not be in menu")
        else:
            print(f"  ✓ Settings link found")

        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ Updated: {', '.join(changes)}")
            return True
        else:
            print(f"  - No changes needed")
            return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("Adding i18n support to dashboard pages...\n")

    updated = 0
    for file in DASHBOARD_FILES:
        if os.path.exists(file):
            if update_file(file):
                updated += 1
        else:
            print(f"  - File not found: {file}")

    print(f"\n{'='*50}")
    print(f"Summary: {updated} files updated")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
