#!/usr/bin/env python3
"""
Replace browser alerts with custom dialogs
"""

import os
import re

DASHBOARD_FILES = [
    'dashboard_main.html',
    'price_forecast.html',
    'dashboard_advanced.html',
    'settings.html',
    'trading_automation.html',
    'advanced_charts.html'
]

def add_custom_dialogs_script(content):
    """Add custom-dialogs.js script if not already present"""
    if 'custom-dialogs.js' in content:
        return content, False

    # Add before closing </head> tag
    if '</head>' in content:
        content = content.replace(
            '</head>',
            '    <script src="js/custom-dialogs.js"></script>\n</head>',
            1
        )
        return content, True

    return content, False

def replace_alerts(content, filename):
    """Replace alert() calls with showAlert() or showSuccess()/showError()"""
    changes = []

    # dashboard_main.html specific replacements
    if filename == 'dashboard_main.html':
        # Replace "select at least one stock" alert
        if "alert('Please select at least one stock to monitor');" in content:
            content = content.replace(
                "alert('Please select at least one stock to monitor');",
                "showWarning('Please select at least one stock to monitor');"
            )
            changes.append('warning for stock selection')

        # Replace success alert with showSuccess (remove restart monitor instruction)
        old_alert = r"alert\(`Watchlist saved successfully!\\n\\n\$\{result\.count\} stocks will be monitored\.\\n\\nNote: The monitor will pick up changes on the next scan \(every 15 minutes\)\.\\n\\nTo see changes immediately, restart the monitor:\\npython demo_monitor\.py --interval 15`\);"
        new_alert = "showSuccess(`Watchlist saved successfully! ${result.count} stocks will be monitored.`);"
        content = re.sub(old_alert, new_alert, content)
        changes.append('success message')

        # Replace error alerts
        content = content.replace(
            "alert('Error saving watchlist: ' + (result.error || 'Unknown error'));",
            "showError('Error saving watchlist: ' + (result.error || 'Unknown error'));"
        )
        content = content.replace(
            "alert('Error saving watchlist. Check console for details.');",
            "showError('Error saving watchlist. Check console for details.');"
        )
        if 'Error saving watchlist' in content:
            changes.append('error messages')

    # price_forecast.html specific replacements
    if filename == 'price_forecast.html':
        old_alert = r"alert\('⚠️ Please select at least one stock from the checkboxes first!\\n\\nTip: Check one or more stocks to select them\.'\);"
        new_alert = "showWarning('Please select at least one stock from the checkboxes first. Check one or more stocks to select them.');"
        content = re.sub(old_alert, new_alert, content)
        changes.append('stock selection warning')

    # settings.html specific replacements
    if filename == 'settings.html':
        # Replace confirm with showConfirm
        old_confirm = r"if \(confirm\('Are you sure you want to reset all settings to defaults\?'\)\) \{"
        new_confirm = "if (await showConfirm('Are you sure you want to reset all settings to defaults?', '🔄 Reset Settings')) {"
        content = re.sub(old_confirm, new_confirm, content)

        # Make resetSettings async
        content = content.replace(
            'function resetSettings() {',
            'async function resetSettings() {'
        )
        changes.append('reset confirmation')

    # dashboard_advanced.html specific replacements
    if filename == 'dashboard_advanced.html':
        # Replace alerts for portfolio analysis
        content = content.replace(
            "alert('Please select at least one stock for portfolio analysis');",
            "showWarning('Please select at least one stock for portfolio analysis');"
        )
        content = content.replace(
            "alert('Please enter a budget amount');",
            "showWarning('Please enter a budget amount');"
        )
        content = content.replace(
            "alert('Please select at least 2 stocks for risk analysis');",
            "showWarning('Please select at least 2 stocks for risk analysis');"
        )
        content = content.replace(
            "alert('Please select at least 2 stocks for correlation analysis');",
            "showWarning('Please select at least 2 stocks for correlation analysis');"
        )
        if 'Please select at least' in content:
            changes.append('portfolio warnings')

    # trading_automation.html specific replacements
    if filename == 'trading_automation.html':
        # Replace confirmation dialogs
        old_confirm = r"if \(confirm\('Are you sure you want to start automated trading\? This will execute real trades based on your configured strategies\.'\)\) \{"
        new_confirm = "if (await showConfirm('Are you sure you want to start automated trading? This will execute real trades based on your configured strategies.', '⚠️ Start Automated Trading')) {"
        content = re.sub(old_confirm, new_confirm, content)

        old_confirm2 = r"if \(confirm\('Are you sure you want to stop automated trading\?'\)\) \{"
        new_confirm2 = "if (await showConfirm('Are you sure you want to stop automated trading?', '🛑 Stop Trading')) {"
        content = re.sub(old_confirm2, new_confirm2, content)

        # Make functions async
        content = content.replace(
            'function startAutomation() {',
            'async function startAutomation() {'
        )
        content = content.replace(
            'function stopAutomation() {',
            'async function stopAutomation() {'
        )

        # Replace alerts
        content = content.replace(
            "alert('Automated trading started!');",
            "showSuccess('Automated trading started!');"
        )
        content = content.replace(
            "alert('Automated trading stopped.');",
            "showInfo('Automated trading stopped.');"
        )
        changes.append('trading automation dialogs')

    # advanced_charts.html specific replacements
    if filename == 'advanced_charts.html':
        content = content.replace(
            "alert('Please select at least one stock');",
            "showWarning('Please select at least one stock');"
        )
        if 'Please select at least one stock' in content:
            changes.append('stock selection warning')

    # Generic replacements for remaining alerts
    # Replace remaining alert() with showAlert()
    content = re.sub(
        r"alert\((['\"][^'\"]*['\"])\);",
        r"showAlert(\1);",
        content
    )

    return content, changes

def update_file(filepath):
    """Update a single file"""
    print(f"Processing {filepath}...")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        all_changes = []

        # Add custom dialogs script
        content, script_added = add_custom_dialogs_script(content)
        if script_added:
            all_changes.append('added custom-dialogs.js')

        # Replace alerts
        content, alert_changes = replace_alerts(content, filepath)
        all_changes.extend(alert_changes)

        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ Updated: {', '.join(all_changes)}")
            return True
        else:
            print(f"  - No changes needed")
            return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("Replacing browser alerts with custom dialogs...\n")

    updated = 0
    for file in DASHBOARD_FILES:
        if os.path.exists(file):
            if update_file(file):
                updated += 1
        else:
            print(f"  - File not found: {file}")

    print(f"\n{'='*50}")
    print(f"Summary: {updated} files updated")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
