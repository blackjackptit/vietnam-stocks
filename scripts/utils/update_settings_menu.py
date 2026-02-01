#!/usr/bin/env python3
"""
Update settings page menu to match dashboard menu structure
"""

import re

# Read settings.html
with open('settings.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update CSS for menu
old_css = r"""        \.dropdown-menu\.show \{
            opacity: 1;
            visibility: visible;
            transform: translateY\(0\);
        \}

        \.dropdown-item \{
            padding: 14px 20px;
            color: #475569;
            text-decoration: none;
            display: block;
            transition: all 0\.2s;
            border-bottom: 1px solid #f1f5f9;
        \}

        \.dropdown-item:hover \{
            background: #f8fafc;
            color: #c41c16;
            padding-left: 24px;
        \}"""

new_css = """        .dropdown-menu.active {
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
        }"""

content = re.sub(
    r'\.dropdown-menu\.show \{.*?\.dropdown-item:hover \{[^}]+\}',
    new_css,
    content,
    flags=re.DOTALL
)

# Update menu button text
content = content.replace('☰ Menu', '📊 Dashboards<span id="menuArrow">▼</span>')

# Update dropdown menu HTML
old_menu = r'''<div class="dropdown-menu" id="dropdownMenu">
                    <a href="index\.html" class="dropdown-item">🏠 Home</a>
                    <a href="dashboard_main\.html" class="dropdown-item">📊 Main Dashboard</a>
                    <a href="dashboard_history\.html" class="dropdown-item">📈 Historical Analysis</a>
                    <a href="advanced_charts\.html" class="dropdown-item">📉 Advanced Charts</a>
                    <a href="price_forecast\.html" class="dropdown-item">🔮 Price Forecast</a>
                    <a href="dashboard_advanced\.html" class="dropdown-item">💹 Portfolio</a>
                    <a href="macro_analysis\.html" class="dropdown-item">🌍 Macro Analysis</a>
                    <a href="alerts_system\.html" class="dropdown-item">🔔 Alerts System</a>
                    <a href="trading_automation\.html" class="dropdown-item">🤖 Trading Automation</a>
                    <a href="settings\.html" class="dropdown-item">⚙️ Settings</a>
                </div>'''

new_menu = '''<div class="dropdown-menu" id="dropdownMenu">
                    <div class="menu-header">All Dashboards</div>

                    <div class="menu-category">📊 Market Analysis</div>
                    <div class="menu-items">
                        <a href="dashboard_main.html" class="menu-item">
                            <span class="menu-item-icon">📊</span>
                            <span>Main Dashboard</span>
                        </a>
                        <a href="dashboard_history.html" class="menu-item">
                            <span class="menu-item-icon">📈</span>
                            <span>Historical Analysis</span>
                        </a>
                        <a href="advanced_charts.html" class="menu-item">
                            <span class="menu-item-icon">📉</span>
                            <span>Advanced Charts</span>
                        </a>
                        <a href="macro_analysis.html" class="menu-item">
                            <span class="menu-item-icon">🌍</span>
                            <span>Macro Analysis</span>
                        </a>
                    </div>

                    <div class="menu-category">💹 Portfolio & Trading</div>
                    <div class="menu-items">
                        <a href="dashboard_advanced.html" class="menu-item">
                            <span class="menu-item-icon">💹</span>
                            <span>Portfolio Analytics</span>
                        </a>
                        <a href="price_forecast.html" class="menu-item">
                            <span class="menu-item-icon">🔮</span>
                            <span>Price Forecast</span>
                        </a>
                        <a href="trading_automation.html" class="menu-item">
                            <span class="menu-item-icon">🤖</span>
                            <span>Trading Automation</span>
                        </a>
                    </div>

                    <div class="menu-category">⚙️ Tools & Settings</div>
                    <div class="menu-items">
                        <a href="alerts_system.html" class="menu-item">
                            <span class="menu-item-icon">🔔</span>
                            <span>Alerts System</span>
                        </a>
                        <a href="settings.html" class="menu-item">
                            <span class="menu-item-icon">⚙️</span>
                            <span>Settings</span>
                        </a>
                        <a href="index.html" class="menu-item">
                            <span class="menu-item-icon">🏠</span>
                            <span>Home</span>
                        </a>
                    </div>
                </div>'''

content = re.sub(old_menu, new_menu, content, flags=re.DOTALL)

# Update toggleMenu function
old_toggle = r'''function toggleMenu\(\) \{
            const menu = document\.getElementById\('dropdownMenu'\);
            menu\.classList\.toggle\('show'\);
        \}'''

new_toggle = '''function toggleMenu() {
            const menu = document.getElementById('dropdownMenu');
            const arrow = document.getElementById('menuArrow');
            menu.classList.toggle('active');
            if (arrow) arrow.textContent = menu.classList.contains('active') ? '▲' : '▼';
        }'''

content = re.sub(old_toggle, new_toggle, content, flags=re.DOTALL)

# Update click outside handler
old_handler = r'''document\.addEventListener\('click', function\(event\) \{
            const menu = document\.getElementById\('dropdownMenu'\);
            const menuBtn = document\.querySelector\('\.menu-btn'\);

            if \(!menu\.contains\(event\.target\) && !menuBtn\.contains\(event\.target\)\) \{
                menu\.classList\.remove\('show'\);
            \}
        \}\);'''

new_handler = '''document.addEventListener('click', function(event) {
            const menu = document.getElementById('dropdownMenu');
            const menuBtn = event.target.closest('.menu-btn');
            if (!menuBtn && !event.target.closest('.dropdown-menu')) {
                menu.classList.remove('active');
                const arrow = document.getElementById('menuArrow');
                if (arrow) arrow.textContent = '▼';
            }
        });'''

content = re.sub(old_handler, new_handler, content, flags=re.DOTALL)

# Write back
with open('settings.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Settings menu updated successfully!")
