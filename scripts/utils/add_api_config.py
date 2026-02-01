#!/usr/bin/env python3
"""
Add api-config.js to all HTML pages before other scripts
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
    'settings.html',
    'test_language.html'
]

def add_api_config_script(content):
    """Add api-config.js script if not already present"""
    if 'api-config.js' in content:
        return content, False

    # Add before any other script tags or before closing </head>
    # Priority: before stock-categories.js or before any script
    patterns = [
        (r'(<script src="js/stock-categories\.js"></script>)', r'<script src="js/api-config.js"></script>\n    \1'),
        (r'(<script src="js/data-api\.js"></script>)', r'<script src="js/api-config.js"></script>\n    \1'),
        (r'(<script src="js/i18n\.js"></script>)', r'<script src="js/api-config.js"></script>\n    \1'),
        (r'(</head>)', r'    <script src="js/api-config.js"></script>\n\1')
    ]

    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            return content, True

    return content, False

def update_file(filepath):
    """Update a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        content, added = add_api_config_script(content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filepath} - added api-config.js")
            return True
        else:
            print(f"  - {filepath} - already has api-config.js")
            return False

    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    print("Adding api-config.js to all dashboard pages...\n")

    updated = 0
    for file in DASHBOARD_FILES:
        if os.path.exists(file):
            if update_file(file):
                updated += 1
        else:
            print(f"  - {file} not found")

    print(f"\n{'='*60}")
    print(f"Summary: {updated} files updated")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
