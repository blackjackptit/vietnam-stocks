#!/usr/bin/env python3
"""
Add i18n support to ALL HTML files in the project
"""
import os
import re

def add_i18n_scripts_to_head(content):
    """Add i18n script tags to <head> if not present"""
    if 'js/i18n.js' in content:
        return content, False  # Already has i18n

    # Find the </head> tag
    head_match = re.search(r'</head>', content, re.IGNORECASE)
    if not head_match:
        return content, False

    # Scripts to add before </head>
    scripts = '''    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <script src="js/api-config.js"></script>
    <script src="js/i18n.js"></script>
    <script src="js/currency.js"></script>
'''

    # Check if favicon already exists
    if 'favicon.svg' in content:
        scripts = '''    <script src="js/api-config.js"></script>
    <script src="js/i18n.js"></script>
    <script src="js/currency.js"></script>
'''

    # Insert before </head>
    pos = head_match.start()
    new_content = content[:pos] + scripts + content[pos:]

    return new_content, True

def process_html_file(filepath):
    """Add i18n support to a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add scripts to head
        new_content, modified = add_i18n_scripts_to_head(content)

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filepath}: Added i18n support")
            return True
        else:
            print(f"⏭️  {filepath}: Already has i18n")
            return False

    except Exception as e:
        print(f"❌ {filepath}: Error - {e}")
        return False

def main():
    """Process all HTML files"""
    print("="*80)
    print("ADDING I18N SUPPORT TO ALL HTML FILES")
    print("="*80)
    print()

    # Find all HTML files
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html'):
            html_files.append(file)

    html_files.sort()

    print(f"Found {len(html_files)} HTML files\n")

    updated = 0
    skipped = 0

    for filepath in html_files:
        if process_html_file(filepath):
            updated += 1
        else:
            skipped += 1

    print()
    print("="*80)
    print(f"SUMMARY: Updated {updated} files, Skipped {skipped} files")
    print("="*80)
    print()
    print("Next steps:")
    print("1. Run: python3 add_all_translations.py")
    print("2. Test language switching on all pages")

if __name__ == '__main__':
    main()
