#!/usr/bin/env python3
import os
import re

def markdown_to_html_simple(md_content):
    """Simple markdown to HTML converter"""
    html = md_content
    
    # Code blocks first (to avoid interfering with other patterns)
    html = re.sub(r'```(\w+)?\n(.*?)\n```', lambda m: f'<pre><code>{m.group(2)}</code></pre>', html, flags=re.DOTALL)
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Lists
    lines = html.split('\n')
    result = []
    in_list = False
    
    for line in lines:
        if re.match(r'^[\*\-] ', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            item = re.sub(r'^[\*\-] ', '', line)
            result.append(f'<li>{item}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            if line.strip() and not line.startswith('<'):
                result.append(f'<p>{line}</p>')
            else:
                result.append(line)
    
    if in_list:
        result.append('</ul>')
    
    return '\n'.join(result)

def get_title(md_content):
    match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    return match.group(1).strip() if match else "Documentation"

# Process each file
import glob
for md_file in sorted(glob.glob('*.md')):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        title = get_title(md_content)
        body = markdown_to_html_simple(md_content)
        html_file = md_file.replace('.md', '.html')
        
        # Write template with content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>{title}</title>
<link rel="stylesheet" href="docs-style.css">
</head><body>
<nav class="top-nav"><div class="nav-container">
<a href="index.html" class="logo-text">📊 VNStock Analytics</a>
<span class="page-title">Documentation</span>
</div></nav>
<div class="container"><div class="content-card markdown-content">
{body}
</div></div>
<footer class="footer"><div class="footer-container">
<p>© 2024 Vietnam Stock Analytics Platform</p>
</div></footer>
</body></html>''')
        
        print(f"✓ {md_file} → {html_file}")
    except Exception as e:
        print(f"✗ {md_file} - {e}")
