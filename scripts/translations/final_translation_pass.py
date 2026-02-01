#!/usr/bin/env python3
"""
Final comprehensive translation pass - capture ALL remaining text
"""
import re
import os
import hashlib

def generate_key(text):
    """Generate a unique key for text"""
    # Clean text
    clean = re.sub(r'[^\w\s]', '', text.lower())
    clean = re.sub(r'\s+', '_', clean.strip())

    # Categorize by first word or pattern
    if any(word in text.lower() for word in ['chart', 'graph', 'plot']):
        prefix = 'chart'
    elif any(word in text.lower() for word in ['button', 'click', 'press']):
        prefix = 'button'
    elif any(word in text.lower() for word in ['label', 'field', 'input']):
        prefix = 'label'
    elif any(word in text.lower() for word in ['error', 'warning', 'alert']):
        prefix = 'msg'
    else:
        prefix = 'text'

    # Create unique hash-based key
    hash_val = hashlib.md5(text.encode()).hexdigest()[:8]
    return f'{prefix}.{clean[:30]}_{hash_val}'

def extract_all_text(content):
    """Extract ALL visible text from HTML"""
    texts = []

    # Patterns for all possible elements
    patterns = [
        (r'<h[1-6][^>]*>([^<]+)</h[1-6]>', 'heading'),
        (r'<button[^>]*>([^<]+)</button>', 'button'),
        (r'<a[^>]*>([^<]+)</a>', 'link'),
        (r'<label[^>]*>([^<]+)</label>', 'label'),
        (r'<span[^>]*>([^<]+)</span>', 'span'),
        (r'<p[^>]*>([^<]+)</p>', 'paragraph'),
        (r'<th[^>]*>([^<]+)</th>', 'table_header'),
        (r'<td[^>]*>([^<]+)</td>', 'table_cell'),
        (r'<div[^>]*class="[^"]*card-title[^"]*"[^>]*>([^<]+)</div>', 'card_title'),
        (r'<div[^>]*class="[^"]*stat-label[^"]*"[^>]*>([^<]+)</div>', 'stat_label'),
        (r'<div[^>]*class="[^"]*menu-category[^"]*"[^>]*>([^<]+)</div>', 'menu_category'),
        (r'<div[^>]*class="[^"]*filter-tab[^"]*"[^>]*>([^<]+)</div>', 'filter_tab'),
        (r'<option[^>]*>([^<]+)</option>', 'option'),
        (r'<li[^>]*>([^<]+)</li>', 'list_item'),
    ]

    for pattern, elem_type in patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            full_element = match.group(0)
            text = match.group(1).strip()

            # Skip if already has data-i18n
            if 'data-i18n' in full_element:
                continue

            # Skip empty or very short
            if len(text) < 2:
                continue

            # Skip dynamic content markers
            if any(marker in text for marker in ['${', 'id=', 'class=', '...', 'function', 'var ', 'const ']):
                continue

            # Skip pure numbers or symbols
            if re.match(r'^[\d\s\-:.,]+$', text):
                continue

            texts.append({
                'text': text,
                'type': elem_type,
                'element': full_element[:200]
            })

    return texts

def add_i18n_simple(content, text, key):
    """Add data-i18n to elements containing text"""
    if f'data-i18n="{key}"' in content:
        return content

    escaped = re.escape(text)
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'label', 'div', 'option', 'th', 'td', 'li']

    for tag in tags:
        # <tag>text</tag>
        pattern = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern, content):
            content = re.sub(pattern, rf'\1 data-i18n="{key}">\2{text}\3</{tag}>', content, count=1)

        # <tag attrs>text</tag>
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern2, content):
            def replacer(m):
                return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
            content = re.sub(pattern2, replacer, content, count=1)

    return content

def process_file(filepath, translations_map):
    """Process file and generate translations"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        original_count = content.count('data-i18n=')

        # Extract all text without translations
        all_texts = extract_all_text(content)

        added_count = 0
        for item in all_texts:
            text = item['text']

            # Generate unique key
            key = generate_key(text)

            # Add to content
            new_content = add_i18n_simple(content, text, key)
            if new_content != content:
                content = new_content
                added_count += 1

                # Store translation
                if key not in translations_map:
                    translations_map[key] = text

        # Write back
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            new_count = content.count('data-i18n=')
            print(f"✅ {filepath}: +{added_count} (Total: {new_count})")
            return added_count
        else:
            print(f"⏭️  {filepath}: No new translations")
            return 0

    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return 0

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

    print("="*80)
    print("FINAL COMPREHENSIVE TRANSLATION PASS")
    print("="*80)
    print()

    translations_map = {}
    total_added = 0

    for filename in files:
        if os.path.exists(filename):
            added = process_file(filename, translations_map)
            total_added += added
        else:
            print(f"⚠️  {filename}: Not found")

    print()
    print("="*80)
    print(f"SUMMARY: Added {total_added} new translations")
    print(f"Total unique keys: {len(translations_map)}")
    print("="*80)

    # Save translations for manual review
    if translations_map:
        with open('new_translations.txt', 'w', encoding='utf-8') as f:
            f.write("# New translations to add to i18n.js\n\n")
            f.write("English keys:\n")
            for key, text in sorted(translations_map.items()):
                f.write(f"'{key}': '{text}',\n")
            f.write("\n# Add Vietnamese translations manually\n")
        print(f"\n📝 New translations saved to: new_translations.txt")

if __name__ == '__main__':
    main()
