#!/usr/bin/env python3
"""
Convert all Markdown files to HTML pages with consistent styling
"""

import os
import re
from pathlib import Path

# HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Vietnamese Stock Analytics</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
            background: #f8fafc;
            color: #333333;
            line-height: 1.6;
        }

        /* Sticky Navigation */
        .top-nav {
            position: sticky;
            top: 0;
            background: #ffffff;
            border-bottom: 1px solid #e5e7eb;
            z-index: 1000;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .nav-container {
            max-width: 1360px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 72px;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-text {
            font-size: 1.3em;
            font-weight: 700;
            color: #c41c16;
            text-decoration: none;
        }

        .page-title {
            font-size: 1.1em;
            font-weight: 600;
            color: #64748b;
            border-left: 2px solid #e5e7eb;
            padding-left: 16px;
        }

        .nav-menu {
            position: relative;
        }

        .menu-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: #c41c16;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            font-size: 0.95em;
            transition: all 0.3s;
        }

        .menu-btn:hover {
            background: #991b1b;
            transform: translateY(-1px);
        }

        .dropdown-menu {
            position: absolute;
            top: calc(100% + 10px);
            right: 0;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            min-width: 280px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s;
            z-index: 1001;
        }

        .dropdown-menu.active {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .menu-header {
            padding: 16px 20px;
            border-bottom: 1px solid #e5e7eb;
            font-weight: 700;
            color: #1e293b;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .menu-category {
            padding: 12px 20px 8px;
            font-weight: 700;
            color: #64748b;
            font-size: 0.75em;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            border-top: 1px solid #e5e7eb;
        }

        .menu-category:first-child {
            border-top: none;
        }

        .menu-items {
            padding: 0 0 8px;
        }

        .menu-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 20px;
            color: #475569;
            text-decoration: none;
            transition: all 0.2s;
            font-weight: 500;
        }

        .menu-item:hover {
            background: #fef2f2;
            color: #c41c16;
        }

        .menu-item-icon {
            font-size: 1.2em;
            width: 24px;
            text-align: center;
        }

        /* Content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 32px 24px;
        }

        .content-card {
            background: white;
            padding: 48px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        /* Markdown Styles */
        .markdown-content h1 {
            color: #1e293b;
            font-size: 2.5em;
            margin-bottom: 24px;
            font-weight: 700;
            letter-spacing: -0.5px;
            padding-bottom: 16px;
            border-bottom: 3px solid #c41c16;
        }

        .markdown-content h2 {
            color: #1e293b;
            font-size: 2em;
            margin-top: 48px;
            margin-bottom: 20px;
            font-weight: 700;
            letter-spacing: -0.3px;
        }

        .markdown-content h3 {
            color: #334155;
            font-size: 1.5em;
            margin-top: 32px;
            margin-bottom: 16px;
            font-weight: 600;
        }

        .markdown-content h4 {
            color: #475569;
            font-size: 1.2em;
            margin-top: 24px;
            margin-bottom: 12px;
            font-weight: 600;
        }

        .markdown-content p {
            margin-bottom: 16px;
            color: #475569;
            font-size: 1.05em;
        }

        .markdown-content ul, .markdown-content ol {
            margin-bottom: 16px;
            padding-left: 32px;
            color: #475569;
        }

        .markdown-content li {
            margin-bottom: 8px;
        }

        .markdown-content code {
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            color: #c41c16;
        }

        .markdown-content pre {
            background: #1e293b;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin-bottom: 24px;
            border: 1px solid #334155;
        }

        .markdown-content pre code {
            background: none;
            padding: 0;
            color: #e2e8f0;
            font-size: 0.95em;
        }

        .markdown-content a {
            color: #c41c16;
            text-decoration: none;
            font-weight: 500;
        }

        .markdown-content a:hover {
            text-decoration: underline;
        }

        .markdown-content blockquote {
            border-left: 4px solid #c41c16;
            padding-left: 20px;
            margin: 24px 0;
            color: #64748b;
            font-style: italic;
        }

        .markdown-content table {
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
        }

        .markdown-content table th {
            background: #f8fafc;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            color: #475569;
            border: 1px solid #e2e8f0;
        }

        .markdown-content table td {
            padding: 12px;
            border: 1px solid #e2e8f0;
            color: #64748b;
        }

        .markdown-content table tr:hover {
            background: #f8fafc;
        }

        .markdown-content hr {
            border: none;
            border-top: 2px solid #e5e7eb;
            margin: 40px 0;
        }

        .markdown-content img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 24px 0;
        }

        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 32px;
            right: 32px;
            padding: 12px 20px;
            background: #c41c16;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(196, 28, 22, 0.3);
            transition: all 0.3s;
            opacity: 0;
            visibility: hidden;
        }

        .back-to-top.visible {
            opacity: 1;
            visibility: visible;
        }

        .back-to-top:hover {
            background: #991b1b;
            transform: translateY(-2px);
        }

        /* Footer */
        .footer {
            background: #1e293b;
            color: #cbd5e1;
            padding: 40px 24px 24px;
            margin-top: 60px;
        }

        .footer-container {
            max-width: 1360px;
            margin: 0 auto;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }

        .footer-section h3 {
            color: white;
            font-size: 1.1em;
            margin-bottom: 12px;
            font-weight: 700;
        }

        .footer-links {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 8px;
        }

        .footer-links a {
            color: #cbd5e1;
            text-decoration: none;
            transition: color 0.2s;
            font-size: 0.9em;
        }

        .footer-links a:hover {
            color: #f59e0b;
        }

        .footer-bottom {
            border-top: 1px solid #334155;
            padding-top: 20px;
            text-align: center;
            color: #94a3b8;
            font-size: 0.85em;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="top-nav">
        <div class="nav-container">
            <div class="logo-section">
                <a href="index.html" class="logo-text">📊 VNStock Analytics</a>
                <span class="page-title">Documentation</span>
            </div>
            <div class="nav-menu">
                <button class="menu-btn" onclick="toggleMenu()">
                    📊 Dashboards
                    <span id="menuArrow">▼</span>
                </button>
                <div class="dropdown-menu" id="dropdownMenu">
                    <div class="menu-header">All Dashboards</div>

                    <div class="menu-category">📊 Market Analysis</div>
                    <div class="menu-items">
                        <a href="dashboard_main.html" class="menu-item">
                            <span class="menu-item-icon">📊</span>
                            <span>Main Dashboard</span>
                        </a>
                        <a href="dashboard_history.html" class="menu-item">
                            <span class="menu-item-icon">📊</span>
                            <span>Historical Analysis</span>
                        </a>
                        <a href="advanced_charts.html" class="menu-item">
                            <span class="menu-item-icon">📉</span>
                            <span>Advanced Charts</span>
                        </a>
                    </div>

                    <div class="menu-category">💼 Investment Tools</div>
                    <div class="menu-items">
                        <a href="price_forecast.html" class="menu-item">
                            <span class="menu-item-icon">🔮</span>
                            <span>Price Forecasting</span>
                        </a>
                        <a href="dashboard_advanced.html" class="menu-item">
                            <span class="menu-item-icon">💼</span>
                            <span>Portfolio Analytics</span>
                        </a>
                        <a href="macro_analysis.html" class="menu-item">
                            <span class="menu-item-icon">🌍</span>
                            <span>Macro Analysis</span>
                        </a>
                    </div>

                    <div class="menu-category">🔔 Automation & Alerts</div>
                    <div class="menu-items">
                        <a href="alerts_system.html" class="menu-item">
                            <span class="menu-item-icon">🔔</span>
                            <span>Price Alerts</span>
                        </a>
                        <a href="trading_automation.html" class="menu-item">
                            <span class="menu-item-icon">🤖</span>
                            <span>Trading Automation</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <div class="container">
        <div class="content-card">
            <div class="markdown-content">
{content}
            </div>
        </div>
    </div>

    <!-- Back to top button -->
    <button class="back-to-top" id="backToTop" onclick="scrollToTop()">↑ Top</button>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-section">
                    <h3>Dashboards</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="dashboard_main.html">Main Dashboard</a></li>
                        <li><a href="dashboard_history.html">Historical Analysis</a></li>
                        <li><a href="advanced_charts.html">Advanced Charts</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Tools</h3>
                    <ul class="footer-links">
                        <li><a href="price_forecast.html">Price Forecasting</a></li>
                        <li><a href="dashboard_advanced.html">Portfolio Analytics</a></li>
                        <li><a href="macro_analysis.html">Macro Analysis</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Automation</h3>
                    <ul class="footer-links">
                        <li><a href="alerts_system.html">Price Alerts</a></li>
                        <li><a href="trading_automation.html">Trading Automation</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Documentation</h3>
                    <ul class="footer-links">
                        <li><a href="README.html">README</a></li>
                        <li><a href="QUICK_START.html">Quick Start</a></li>
                        <li><a href="API_SERVER_SETUP.html">API Setup</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>© 2024 Vietnam Stock Analytics Platform</p>
                <p style="margin-top: 8px;">For educational purposes only. Not financial advice. Trade at your own risk.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            const menu = document.getElementById('dropdownMenu');
            const arrow = document.getElementById('menuArrow');
            menu.classList.toggle('active');
            arrow.textContent = menu.classList.contains('active') ? '▲' : '▼';
        }

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const menu = document.getElementById('dropdownMenu');
            const menuBtn = event.target.closest('.menu-btn');
            if (!menuBtn && !event.target.closest('.dropdown-menu')) {
                menu.classList.remove('active');
                const arrow = document.getElementById('menuArrow');
                if (arrow) arrow.textContent = '▼';
            }
        });

        // Back to top button
        window.addEventListener('scroll', function() {
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    </script>
</body>
</html>"""


def markdown_to_html(md_content):
    """Convert markdown to HTML (basic conversion)"""
    html = md_content

    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Code blocks
    html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'__(.+?)__', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'_(.+?)_', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)

    # Images
    html = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1">', html)

    # Horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    html = re.sub(r'^\*\*\*$', r'<hr>', html, flags=re.MULTILINE)

    # Lists (unordered)
    lines = html.split('\n')
    in_ul = False
    result = []

    for line in lines:
        if re.match(r'^[\*\-\+] ', line):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            item = re.sub(r'^[\*\-\+] ', '', line)
            result.append(f'<li>{item}</li>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            result.append(line)

    if in_ul:
        result.append('</ul>')

    html = '\n'.join(result)

    # Paragraphs
    paragraphs = html.split('\n\n')
    html_paragraphs = []

    for para in paragraphs:
        para = para.strip()
        if para and not any(para.startswith(tag) for tag in ['<h', '<ul', '<ol', '<pre', '<hr', '<blockquote']):
            if not para.startswith('<'):
                para = f'<p>{para}</p>'
        if para:
            html_paragraphs.append(para)

    html = '\n'.join(html_paragraphs)

    return html


def extract_title(md_content):
    """Extract title from markdown content"""
    match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Documentation"


def convert_md_file(md_path, output_dir='.'):
    """Convert a single markdown file to HTML"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        title = extract_title(md_content)
        html_content = markdown_to_html(md_content)

        html_output = HTML_TEMPLATE.format(
            title=title,
            content=html_content
        )

        # Output filename
        output_filename = Path(md_path).stem + '.html'
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

        print(f"✓ {Path(md_path).name} → {output_filename}")
        return True

    except Exception as e:
        print(f"✗ {Path(md_path).name} - Error: {e}")
        return False


def main():
    """Convert all markdown files in current directory"""
    print("=" * 60)
    print("Converting Markdown Files to HTML")
    print("=" * 60)
    print()

    md_files = sorted(Path('.').glob('*.md'))

    if not md_files:
        print("No markdown files found in current directory")
        return

    print(f"Found {len(md_files)} markdown files\n")

    success_count = 0
    for md_file in md_files:
        if convert_md_file(md_file):
            success_count += 1

    print()
    print("=" * 60)
    print(f"Complete: {success_count}/{len(md_files)} files converted")
    print("=" * 60)


if __name__ == '__main__':
    main()
