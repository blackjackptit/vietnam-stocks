#!/usr/bin/env python3
"""
Check translation coverage across all HTML files
"""
import re
import os
from collections import defaultdict

def extract_visible_text(html_content):
    """Extract visible text from HTML elements"""
    visible_texts = []

    # Patterns for common elements with visible text
    patterns = [
        (r'<h[1-6][^>]*>(.*?)</h[1-6]>', 'heading'),
        (r'<button[^>]*>(.*?)</button>', 'button'),
        (r'<a[^>]*>(.*?)</a>', 'link'),
        (r'<label[^>]*>(.*?)</label>', 'label'),
        (r'<span[^>]*>(.*?)</span>', 'span'),
        (r'<p[^>]*>(.*?)</p>', 'paragraph'),
        (r'<th[^>]*>(.*?)</th>', 'table_header'),
        (r'<div[^>]*class="[^"]*tab[^"]*"[^>]*>(.*?)</div>', 'tab'),
        (r'<div[^>]*class="[^"]*summary-label[^"]*"[^>]*>(.*?)</div>', 'label'),
        (r'placeholder="([^"]*)"', 'placeholder'),
    ]

    for pattern, element_type in patterns:
        matches = re.finditer(pattern, html_content, re.DOTALL | re.IGNORECASE)
        for match in matches:
            text = match.group(1).strip()
            # Clean HTML tags from text
            text = re.sub(r'<[^>]+>', '', text)
            text = re.sub(r'\s+', ' ', text).strip()

            # Skip empty, very short, or dynamic content
            if len(text) < 2 or text.startswith('${') or text.startswith('id=') or text.startswith('class='):
                continue
            if text.lower() in ['', '-', '...', 'n/a']:
                continue

            # Check if this element has data-i18n
            element = match.group(0)
            has_i18n = 'data-i18n' in element

            visible_texts.append({
                'text': text[:100],  # Limit length
                'type': element_type,
                'has_i18n': has_i18n,
                'element': element[:200]
            })

    return visible_texts

def analyze_file(filepath):
    """Analyze a single HTML file for translation coverage"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get all visible text
        texts = extract_visible_text(content)

        # Count data-i18n attributes
        i18n_count = content.count('data-i18n=')
        i18n_placeholder = content.count('data-i18n-placeholder=')

        # Categorize texts
        with_i18n = [t for t in texts if t['has_i18n']]
        without_i18n = [t for t in texts if not t['has_i18n']]

        # Filter out common non-translatable content
        non_translatable_patterns = [
            r'^\d+$',  # Just numbers
            r'^[A-Z]{3,4}$',  # Stock symbols
            r'^[\d\s,\.]+$',  # Numbers with formatting
            r'^[\d\-:]+$',  # Dates/times
            r'^#[0-9a-f]{6}$',  # Hex colors
            r'^\$',  # Prices
            r'^[<>]+$',  # Just brackets
            r'Loading\.\.\.',  # Already has i18n via JS
            r'^\s*$',  # Whitespace only
        ]

        actually_missing = []
        for item in without_i18n:
            text = item['text']
            is_translatable = True

            for pattern in non_translatable_patterns:
                if re.match(pattern, text, re.IGNORECASE):
                    is_translatable = False
                    break

            # Skip very common English words that might be part of URLs or IDs
            skip_words = ['http', 'localhost', '.html', '.js', '.css', 'function', 'const', 'var', 'let']
            if any(word in text.lower() for word in skip_words):
                is_translatable = False

            if is_translatable and len(text) > 3:
                actually_missing.append(item)

        return {
            'total_elements': len(texts),
            'with_i18n': len(with_i18n),
            'without_i18n': len(actually_missing),
            'i18n_attributes': i18n_count + i18n_placeholder,
            'missing_items': actually_missing[:20],  # First 20 missing items
        }

    except Exception as e:
        return {'error': str(e)}

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

    print("=" * 80)
    print("TRANSLATION COVERAGE ANALYSIS")
    print("=" * 80)
    print()

    total_stats = {
        'total_elements': 0,
        'with_i18n': 0,
        'without_i18n': 0,
        'i18n_attributes': 0,
    }

    for filename in files:
        if not os.path.exists(filename):
            print(f"⚠️  {filename}: NOT FOUND\n")
            continue

        print(f"📄 {filename}")
        print("-" * 80)

        analysis = analyze_file(filename)

        if 'error' in analysis:
            print(f"   ❌ Error: {analysis['error']}\n")
            continue

        total = analysis['total_elements']
        with_i18n = analysis['with_i18n']
        without = analysis['without_i18n']
        i18n_attrs = analysis['i18n_attributes']

        if total > 0:
            coverage = (with_i18n / total) * 100 if total > 0 else 0
        else:
            coverage = 0

        print(f"   Total user-visible elements: {total}")
        print(f"   With translations: {with_i18n}")
        print(f"   Missing translations: {without}")
        print(f"   Total data-i18n attributes: {i18n_attrs}")
        print(f"   Coverage: {coverage:.1f}%")

        if analysis['missing_items']:
            print(f"\n   ⚠️  Missing translations (showing first 10):")
            for i, item in enumerate(analysis['missing_items'][:10], 1):
                print(f"      {i}. [{item['type']}] \"{item['text'][:60]}\"")
        else:
            print(f"\n   ✅ All translatable content has data-i18n attributes!")

        print()

        # Update totals
        total_stats['total_elements'] += total
        total_stats['with_i18n'] += with_i18n
        total_stats['without_i18n'] += without
        total_stats['i18n_attributes'] += i18n_attrs

    print("=" * 80)
    print("OVERALL SUMMARY")
    print("=" * 80)
    print(f"Total elements: {total_stats['total_elements']}")
    print(f"With translations: {total_stats['with_i18n']}")
    print(f"Missing translations: {total_stats['without_i18n']}")
    print(f"Total data-i18n attributes: {total_stats['i18n_attributes']}")

    if total_stats['total_elements'] > 0:
        overall_coverage = (total_stats['with_i18n'] / total_stats['total_elements']) * 100
        print(f"Overall coverage: {overall_coverage:.1f}%")

        if overall_coverage >= 90:
            print("\n✅ EXCELLENT: Translation coverage is very high!")
        elif overall_coverage >= 70:
            print("\n👍 GOOD: Most content is translated, but some gaps remain")
        elif overall_coverage >= 50:
            print("\n⚠️  FAIR: Significant content still needs translation")
        else:
            print("\n❌ POOR: Most content is not translated")

    print("=" * 80)

if __name__ == '__main__':
    main()
