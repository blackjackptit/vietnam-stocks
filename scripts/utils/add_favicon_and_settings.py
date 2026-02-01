#!/usr/bin/env python3
"""
Script to add favicon and settings link to all HTML pages
"""

import os
import re

# HTML files to update
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

DOC_FILES = [
    'README.html',
    'README_API.html',
    'QUICK_START.html',
    'WATCHLIST_GUIDE.html',
    'USER_GUIDE_ADVANCED.html',
    'API_ENDPOINTS.html',
    'API_SERVER_SETUP.html',
    'API_MIGRATION_SUMMARY.html',
    'FEATURES_COMPLETE.html',
    'MACRO_FACTORS_GUIDE.html'
]

FAVICON_LINK = '    <link rel="icon" type="image/svg+xml" href="favicon.svg">'

def add_favicon(content):
    """Add favicon link to HTML head if not already present"""
    if 'favicon.svg' in content:
        return content, False

    # Add favicon after the title tag or at end of head
    if '<title>' in content:
        content = re.sub(
            r'(<title>.*?</title>)',
            r'\1\n' + FAVICON_LINK,
            content,
            count=1
        )
        return content, True
    elif '</head>' in content:
        content = content.replace('</head>', FAVICON_LINK + '\n</head>', 1)
        return content, True

    return content, False

def add_settings_to_menu(content):
    """Add settings link to dropdown menu if not present"""
    if 'settings.html' in content and '<a href="settings.html"' in content:
        return content, False

    # Find the dropdown menu section and add settings before closing
    settings_link = '                    <a href="settings.html" class="dropdown-item">⚙️ Settings</a>'

    # Look for the closing div of dropdown menu
    pattern = r'(</div>\s*</div>\s*</div>\s*</nav>)'

    if re.search(pattern, content):
        # Insert settings link before the closing divs
        content = re.sub(
            r'(\s*)(</div>\s*</div>\s*</div>\s*</nav>)',
            r'\n' + settings_link + r'\n\1\2',
            content,
            count=1
        )
        return content, True

    return content, False

def update_file(filepath):
    """Update a single HTML file"""
    print(f"Processing {filepath}...")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Add favicon
        content, favicon_added = add_favicon(content)

        # Add settings link (only for dashboard files, not docs)
        settings_added = False
        if filepath in DASHBOARD_FILES and filepath != 'settings.html':
            content, settings_added = add_settings_to_menu(content)

        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            changes = []
            if favicon_added:
                changes.append("favicon")
            if settings_added:
                changes.append("settings link")

            print(f"  ✓ Updated: {', '.join(changes)}")
            return True
        else:
            print(f"  - No changes needed")
            return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("Adding favicon and settings link to HTML files...\n")

    updated = 0
    skipped = 0

    # Update dashboard files
    print("=== Dashboard Files ===")
    for file in DASHBOARD_FILES:
        if os.path.exists(file):
            if update_file(file):
                updated += 1
            else:
                skipped += 1
        else:
            print(f"  - File not found: {file}")
            skipped += 1

    # Update doc files (favicon only)
    print("\n=== Documentation Files ===")
    for file in DOC_FILES:
        if os.path.exists(file):
            if update_file(file):
                updated += 1
            else:
                skipped += 1
        else:
            print(f"  - File not found: {file}")
            skipped += 1

    print(f"\n{'='*50}")
    print(f"Summary: {updated} files updated, {skipped} skipped")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
