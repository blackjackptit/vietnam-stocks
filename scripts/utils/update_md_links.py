#!/usr/bin/env python3
"""
Update all links from .md to .html files
"""

import os
import re
from pathlib import Path

# Mapping of .md to .html files
MD_TO_HTML = {
    'API_SERVER_SETUP.md': 'API_SERVER_SETUP.html',
    'README_API.md': 'README_API.html',
    'FEATURES_COMPLETE.md': 'FEATURES_COMPLETE.html',
    'QUICK_START.md': 'QUICK_START.html',
    'USER_GUIDE_ADVANCED.md': 'USER_GUIDE_ADVANCED.html',
    'MACRO_FACTORS_GUIDE.md': 'MACRO_FACTORS_GUIDE.html',
    'API_ENDPOINTS.md': 'API_ENDPOINTS.html',
    'API_MIGRATION_SUMMARY.md': 'API_MIGRATION_SUMMARY.html',
    'README.md': 'README.html',
    'WATCHLIST_GUIDE.md': 'WATCHLIST_GUIDE.html',
}

def update_file(filepath):
    """Update .md links to .html in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        changes = []

        # Replace each .md link with .html
        for md_file, html_file in MD_TO_HTML.items():
            # Pattern for href="FILE.md" or href='FILE.md'
            pattern1 = f'href=["\']({md_file})["\']'
            replacement1 = f'href="{html_file}"'

            if re.search(pattern1, content):
                content = re.sub(pattern1, replacement1, content)
                changes.append(f'{md_file} → {html_file}')

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ {filepath}")
            for change in changes:
                print(f"    - {change}")
            return True
        else:
            print(f"  - {filepath} (no changes)")
            return False

    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    print("Updating .md links to .html files...\n")

    # Get all HTML files
    html_files = list(Path('.').glob('*.html'))

    updated = 0
    skipped = 0

    for html_file in html_files:
        if update_file(str(html_file)):
            updated += 1
        else:
            skipped += 1

    print(f"\n{'='*60}")
    print(f"Summary: {updated} files updated, {skipped} files skipped")
    print(f"{'='*60}")

    # Verify all HTML versions exist
    print("\nVerifying HTML files exist:")
    for md_file, html_file in MD_TO_HTML.items():
        if os.path.exists(html_file):
            print(f"  ✓ {html_file}")
        else:
            print(f"  ✗ {html_file} - MISSING!")

if __name__ == '__main__':
    main()
