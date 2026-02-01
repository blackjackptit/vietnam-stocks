#!/usr/bin/env python3
"""
Fix all API fetch calls to use API_BASE_URL for correct port (5000)
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
    'dashboard_realtime.html'
]

def fix_api_calls(content):
    """Replace fetch('/api/...') with fetch using API_BASE_URL"""
    changes = []

    # Pattern 1: fetch('/api/endpoint')
    pattern1 = r"fetch\('(/api/[^']+)'\)"
    replacement1 = r"fetch(`${window.API_BASE_URL || ''}\1`)"

    if re.search(pattern1, content):
        content = re.sub(pattern1, replacement1, content)
        changes.append('fixed fetch with single quotes')

    # Pattern 2: fetch("/api/endpoint")
    pattern2 = r'fetch\("(/api/[^"]+)"\)'
    replacement2 = r'fetch(`${window.API_BASE_URL || ""}\1`)'

    if re.search(pattern2, content):
        content = re.sub(pattern2, replacement2, content)
        changes.append('fixed fetch with double quotes')

    # Pattern 3: await fetch('/api/endpoint', options)
    pattern3 = r"fetch\('(/api/[^']+)',\s*\{"
    replacement3 = r"fetch(`${window.API_BASE_URL || ''}\1`, {"

    if re.search(pattern3, content):
        content = re.sub(pattern3, replacement3, content)
        changes.append('fixed fetch with options (single quotes)')

    # Pattern 4: await fetch("/api/endpoint", options)
    pattern4 = r'fetch\("(/api/[^"]+)",\s*\{'
    replacement4 = r'fetch(`${window.API_BASE_URL || ""}\1`, {'

    if re.search(pattern4, content):
        content = re.sub(pattern4, replacement4, content)
        changes.append('fixed fetch with options (double quotes)')

    return content, changes

def update_file(filepath):
    """Update a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        content, changes = fix_api_calls(content)

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
    print("Fixing API fetch calls to use port 5000...\n")

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
    print("\nAll API calls now use: fetch(`${window.API_BASE_URL}/api/...`)")
    print("This ensures API calls always go to port 5000")

if __name__ == '__main__':
    main()
