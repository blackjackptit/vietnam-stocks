#!/usr/bin/env python3
"""
Complete all translations - Extract ALL text and add translations
"""
import re
import os
import json
from collections import OrderedDict

# Comprehensive mappings for ALL content
ALL_TRANSLATIONS = {
    # Navigation and Menu
    '📊 Dashboards ▼': 'menu.dashboards_button',
    '📊 VNStock Analytics': 'home.brand_name',
    '📉 Advanced Charts': 'nav.charts',
    '🔮 Price Forecasting': 'nav.forecast',
    '🌍 Macro Analysis': 'nav.macro',
    '🔔 Price Alerts': 'alerts.page_title',
    'Advanced Charts': 'nav.charts',
    'Price Forecasting': 'nav.forecast',
    'Macro Analysis': 'nav.macro',

    # Home page content
    'Institutional-grade tools for Vietnamese market investors': 'home.hero_subtitle',
    'Comprehensive suite of professional-grade analytics and trading tools': 'home.tools_description',
    'Real-time market monitoring with live data updates': 'home.dashboard_description',
    'Track price movements, volume changes, and market trends': 'home.history_description',
    'Machine learning predictions using 4 models': 'home.forecast_description_1',
    'Statistical control charts with anomaly detection and investment recommendations': 'home.forecast_description_2',
    'Portfolio optimization, strategy backtesting, risk management with VaR/CVaR': 'home.advanced_description_1',
    'ML forecasting, and pattern recognition': 'home.advanced_description_2',
    'Institutional-grade charting with Ichimoku Cloud, Volume Profile, Stochastic': 'home.charts_description_1',
    'Fibonacci, Pivot Points, and more': 'home.charts_description_2',
    'Track global factors: oil prices, interest rates, geopolitical risks': 'home.macro_description_1',
    'policy changes, and their impact on Vietnamese stocks': 'home.macro_description_2',
    'Real-time monitoring with customizable alerts': 'home.alerts_description_1',
    'Get notified when stocks hit target prices, RSI levels, or volume spikes': 'home.alerts_description_2',
    'Automated execution of trading strategies based on technical signals': 'home.automation_description_1',
    'Set custom rules for entry, exit, stop-loss, and position sizing': 'home.automation_description_2',
    'Professional-grade tools trusted by serious investors': 'home.trusted_description',
    '233 Vietnamese stocks and commodities with real-time data and historical analysis': 'home.coverage_description',
    'Machine learning forecasts, anomaly detection, and automated investment recommendations': 'home.ai_description',
    'Professional Tools': 'home.professional_tools',
    'Institutional-grade charts, technical indicators, and risk analysis tools': 'home.tools_full_description',

    # Tags and badges
    'Real-time': 'tag.realtime',
    'Live Data': 'tag.livedata',
    'AI Powered': 'tag.ai_powered',
    '4 Models': 'tag.four_models',
    '7-90 Days': 'tag.forecast_range',
    'Portfolio': 'tag.portfolio',
    'Backtesting': 'tag.backtesting',
    'Risk VaR': 'tag.risk_var',
    'Candlestick': 'tag.candlestick',
    'Ichimoku': 'tag.ichimoku',
    '20+ Indicators': 'tag.indicators',
    'Oil Impact': 'tag.oil_impact',
    'Geopolitics': 'tag.geopolitics',
    'Policy': 'tag.policy',
    'Notifications': 'tag.notifications',
    'Custom': 'tag.custom',
    'Rules': 'tag.rules',
    'Auto-Trade': 'tag.autotrade',
    'NEW': 'tag.new',
    'PRO': 'tag.pro',

    # Actions
    'View Dashboard →': 'action.view_dashboard',
    'Analyze History →': 'action.analyze_history',
    'Generate Forecast →': 'action.generate_forecast',
    'Access Pro Tools →': 'action.access_pro',
    'View Charts →': 'action.view_charts',
    'Analyze Factors →': 'action.analyze_factors',
    'Configure Alerts →': 'action.configure_alerts',
    'Setup Automation →': 'action.setup_automation',

    # Page sections
    'Dashboards': 'menu.dashboards',
    'Tools': 'menu.tools',
    'Automation': 'menu.automation',
    'Platform': 'menu.platform',

    # Settings page
    'Currency': 'settings.currency_label',
    'Total Investment Budget': 'settings.total_budget',
    'Risk Tolerance': 'settings.risk_tolerance',
    'Maximum Position Size (%)': 'settings.max_position',
    'Dashboard Refresh Interval': 'settings.refresh_interval',
    'Real-time Update Frequency': 'settings.realtime_frequency',
    'API Endpoint': 'settings.api_endpoint',
    'API Key': 'settings.api_key',
    'Theme': 'settings.theme',
    'Chart Type': 'settings.chart_type',
    'Default Time Range': 'settings.default_timerange',
    'Enable Price Alerts': 'settings.enable_alerts',
    'Alert Notification Method': 'settings.alert_method',
    'Enable Auto-Trading': 'settings.enable_autotrading',
    'Maximum Daily Trades': 'settings.max_daily_trades',
    'Default Order Type': 'settings.default_order_type',

    # Options
    'Low': 'option.low',
    'Medium': 'option.medium',
    'High': 'option.high',
    'Light': 'option.light',
    'Dark': 'option.dark',
    'Candlestick': 'option.candlestick',
    'Line': 'option.line',
    'Email': 'option.email',
    'Browser': 'option.browser',
    'Market': 'option.market',
    'Limit': 'option.limit',

    # Advanced features
    '📊 Price History & Technical Analysis': 'section.price_history_analysis',
    'Price History & Technical Analysis': 'section.price_history_analysis',
    '📈 Price Forecast with Confidence Interval': 'section.forecast_confidence',
    'Price Forecast with Confidence Interval': 'section.forecast_confidence',
    '📋 Trade History': 'section.trade_history',
    'Trade History': 'section.trade_history',

    # Buttons
    '🔍 Test Connection': 'button.test_connection',
    '💾 Save Configuration': 'button.save_config',
    '➕ Add New Rule': 'button.add_rule',
    '✏️ Edit': 'button.edit',
    '🗑️ Delete': 'button.delete',
    '▶️ Activate': 'button.activate',
    '⏸️ Pause': 'button.pause',
    '🔄 Refresh Data': 'button.refresh_data',

    # Footer
    'Products': 'footer.products',
    'Resources': 'footer.resources',
    'Market Overview': 'footer.market_overview',
    'AI Forecast': 'footer.ai_forecast',
    'Quick Start Guide': 'footer.quick_start',
    'Features': 'footer.features',
    'User Guide': 'footer.user_guide',
    'Macro Guide': 'footer.macro_guide',

    # Status and labels
    'System Online': 'status.online',
    'Connected': 'status.connected',
    'Disconnected': 'status.disconnected',
    'Active': 'status.active',
    'Inactive': 'status.inactive',
    'Running': 'status.running',
    'Stopped': 'status.stopped',

    # Time ranges
    '1 minute': 'timerange.1min',
    '5 minutes': 'timerange.5min',
    '15 minutes': 'timerange.15min',
    '30 minutes': 'timerange.30min',
    '1 hour': 'timerange.1hour',
    '4 hours': 'timerange.4hours',
    '1 day': 'timerange.1day',
    '1 week': 'timerange.1week',
    '1 month': 'timerange.1month',

    # Numbers and stats
    'Stocks & Assets': 'stats.stocks_assets',
    'Indicators': 'stats.indicators',
    'AI Models': 'stats.ai_models',

    # Descriptions
    'For educational and informational purposes only': 'disclaimer.educational',
    'All investments carry risk': 'disclaimer.risk',
    'Past performance does not guarantee future results': 'disclaimer.performance',
    'This is not financial advice': 'disclaimer.not_advice',
    'always do your own research and consult licensed financial advisors': 'disclaimer.dyor',
    'before making investment decisions': 'disclaimer.before_invest',

    # Links
    '🏠 Home': 'nav.home_icon',
    'Dashboard': 'footer.dashboard',
    'Documentation': 'footer.documentation',
}

# Vietnamese translations for new keys
VIETNAMESE_TRANSLATIONS = {
    'menu.dashboards_button': '📊 Bảng Điều Khiển ▼',
    'home.brand_name': '📊 Phân Tích VNStock',
    'home.tools_description': 'Bộ công cụ phân tích và giao dịch cấp chuyên nghiệp toàn diện',
    'home.dashboard_description': 'Giám sát thị trường thời gian thực với cập nhật dữ liệu trực tiếp',
    'home.history_description': 'Theo dõi biến động giá, thay đổi khối lượng và xu hướng thị trường',
    'home.forecast_description_1': 'Dự đoán học máy sử dụng 4 mô hình',
    'home.forecast_description_2': 'Biểu đồ kiểm soát thống kê với phát hiện bất thường và khuyến nghị đầu tư',
    'home.advanced_description_1': 'Tối ưu hóa danh mục, kiểm tra chiến lược ngược, quản lý rủi ro với VaR/CVaR',
    'home.advanced_description_2': 'Dự báo ML và nhận dạng mẫu',
    'home.charts_description_1': 'Biểu đồ cấp tổ chức với Ichimoku Cloud, Volume Profile, Stochastic',
    'home.charts_description_2': 'Fibonacci, Pivot Points và nhiều hơn nữa',
    'home.macro_description_1': 'Theo dõi các yếu tố toàn cầu: giá dầu, lãi suất, rủi ro địa chính trị',
    'home.macro_description_2': 'thay đổi chính sách và tác động của chúng đến cổ phiếu Việt Nam',
    'home.alerts_description_1': 'Giám sát thời gian thực với cảnh báo tùy chỉnh',
    'home.alerts_description_2': 'Nhận thông báo khi cổ phiếu đạt giá mục tiêu, mức RSI hoặc tăng đột biến khối lượng',
    'home.automation_description_1': 'Thực thi tự động các chiến lược giao dịch dựa trên tín hiệu kỹ thuật',
    'home.automation_description_2': 'Đặt quy tắc tùy chỉnh cho vào lệnh, thoát lệnh, cắt lỗ và kích thước vị thế',
    'home.trusted_description': 'Công cụ cấp chuyên nghiệp được tin tưởng bởi các nhà đầu tư nghiêm túc',
    'home.coverage_description': '233 cổ phiếu và hàng hóa Việt Nam với dữ liệu thời gian thực và phân tích lịch sử',
    'home.ai_description': 'Dự báo học máy, phát hiện bất thường và khuyến nghị đầu tư tự động',
    'home.professional_tools': 'Công Cụ Chuyên Nghiệp',
    'home.tools_full_description': 'Biểu đồ cấp tổ chức, chỉ báo kỹ thuật và công cụ phân tích rủi ro',

    'tag.realtime': 'Thời Gian Thực',
    'tag.livedata': 'Dữ Liệu Trực Tiếp',
    'tag.ai_powered': 'Hỗ Trợ AI',
    'tag.four_models': '4 Mô Hình',
    'tag.forecast_range': '7-90 Ngày',
    'tag.portfolio': 'Danh Mục',
    'tag.backtesting': 'Kiểm Tra Ngược',
    'tag.risk_var': 'Rủi Ro VaR',
    'tag.candlestick': 'Nến',
    'tag.ichimoku': 'Ichimoku',
    'tag.indicators': '20+ Chỉ Báo',
    'tag.oil_impact': 'Tác Động Dầu',
    'tag.geopolitics': 'Địa Chính Trị',
    'tag.policy': 'Chính Sách',
    'tag.notifications': 'Thông Báo',
    'tag.custom': 'Tùy Chỉnh',
    'tag.rules': 'Quy Tắc',
    'tag.autotrade': 'Giao Dịch Tự Động',
    'tag.new': 'MỚI',
    'tag.pro': 'PRO',

    'action.view_dashboard': 'Xem Bảng Điều Khiển →',
    'action.analyze_history': 'Phân Tích Lịch Sử →',
    'action.generate_forecast': 'Tạo Dự Báo →',
    'action.access_pro': 'Truy Cập Công Cụ Pro →',
    'action.view_charts': 'Xem Biểu Đồ →',
    'action.analyze_factors': 'Phân Tích Các Yếu Tố →',
    'action.configure_alerts': 'Cấu Hình Cảnh Báo →',
    'action.setup_automation': 'Thiết Lập Tự Động →',

    'settings.currency_label': 'Tiền Tệ',
    'settings.total_budget': 'Tổng Ngân Sách Đầu Tư',
    'settings.risk_tolerance': 'Dung Sai Rủi Ro',
    'settings.max_position': 'Kích Thước Vị Thế Tối Đa (%)',
    'settings.refresh_interval': 'Khoảng Làm Mới Bảng Điều Khiển',
    'settings.realtime_frequency': 'Tần Suất Cập Nhật Thời Gian Thực',
    'settings.api_endpoint': 'Điểm Cuối API',
    'settings.api_key': 'Khóa API',
    'settings.theme': 'Giao Diện',
    'settings.chart_type': 'Loại Biểu Đồ',
    'settings.default_timerange': 'Phạm Vi Thời Gian Mặc Định',
    'settings.enable_alerts': 'Bật Cảnh Báo Giá',
    'settings.alert_method': 'Phương Thức Thông Báo Cảnh Báo',
    'settings.enable_autotrading': 'Bật Giao Dịch Tự Động',
    'settings.max_daily_trades': 'Số Giao Dịch Tối Đa Hàng Ngày',
    'settings.default_order_type': 'Loại Lệnh Mặc Định',

    'option.low': 'Thấp',
    'option.medium': 'Trung Bình',
    'option.high': 'Cao',
    'option.light': 'Sáng',
    'option.dark': 'Tối',
    'option.candlestick': 'Nến',
    'option.line': 'Đường',
    'option.email': 'Email',
    'option.browser': 'Trình Duyệt',
    'option.market': 'Thị Trường',
    'option.limit': 'Giới Hạn',

    'section.price_history_analysis': '📊 Lịch Sử Giá & Phân Tích Kỹ Thuật',
    'section.forecast_confidence': '📈 Dự Báo Giá với Khoảng Tin Cậy',
    'section.trade_history': '📋 Lịch Sử Giao Dịch',

    'button.test_connection': '🔍 Kiểm Tra Kết Nối',
    'button.save_config': '💾 Lưu Cấu Hình',
    'button.add_rule': '➕ Thêm Quy Tắc Mới',
    'button.edit': '✏️ Chỉnh Sửa',
    'button.delete': '🗑️ Xóa',
    'button.activate': '▶️ Kích Hoạt',
    'button.pause': '⏸️ Tạm Dừng',
    'button.refresh_data': '🔄 Làm Mới Dữ Liệu',

    'footer.products': 'Sản Phẩm',
    'footer.resources': 'Tài Nguyên',
    'footer.market_overview': 'Tổng Quan Thị Trường',
    'footer.ai_forecast': 'Dự Báo AI',
    'footer.quick_start': 'Hướng Dẫn Bắt Đầu Nhanh',
    'footer.features': 'Tính Năng',
    'footer.user_guide': 'Hướng Dẫn Người Dùng',
    'footer.macro_guide': 'Hướng Dẫn Vĩ Mô',
    'footer.dashboard': 'Bảng Điều Khiển',
    'footer.documentation': 'Tài Liệu',

    'status.online': 'Hệ Thống Trực Tuyến',
    'status.connected': 'Đã Kết Nối',
    'status.disconnected': 'Mất Kết Nối',
    'status.active': 'Hoạt Động',
    'status.inactive': 'Không Hoạt Động',
    'status.running': 'Đang Chạy',
    'status.stopped': 'Đã Dừng',

    'timerange.1min': '1 phút',
    'timerange.5min': '5 phút',
    'timerange.15min': '15 phút',
    'timerange.30min': '30 phút',
    'timerange.1hour': '1 giờ',
    'timerange.4hours': '4 giờ',
    'timerange.1day': '1 ngày',
    'timerange.1week': '1 tuần',
    'timerange.1month': '1 tháng',

    'stats.stocks_assets': 'Cổ Phiếu & Tài Sản',
    'stats.indicators': 'Chỉ Báo',
    'stats.ai_models': 'Mô Hình AI',

    'disclaimer.educational': 'Chỉ dành cho mục đích giáo dục và thông tin',
    'disclaimer.risk': 'Tất cả đầu tư đều có rủi ro',
    'disclaimer.performance': 'Hiệu suất trong quá khứ không đảm bảo kết quả tương lai',
    'disclaimer.not_advice': 'Đây không phải là lời khuyên tài chính',
    'disclaimer.dyor': 'luôn tự nghiên cứu và tham khảo cố vấn tài chính có giấy phép',
    'disclaimer.before_invest': 'trước khi đưa ra quyết định đầu tư',

    'nav.home_icon': '🏠 Trang Chủ',
}

def add_i18n_attribute(content, text, key):
    """Add data-i18n attribute to HTML elements"""
    if len(text) < 2:
        return content

    escaped = re.escape(text)
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'button', 'a', 'label', 'div', 'option', 'th', 'td', 'li']

    for tag in tags:
        # Check if already has this data-i18n
        if f'data-i18n="{key}"' in content:
            continue

        # Pattern 1: <tag>text</tag>
        pattern1 = rf'(<{tag})>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern1, content):
            replacement = rf'\1 data-i18n="{key}">\2{text}\3</{tag}>'
            content = re.sub(pattern1, replacement, content, count=1)

        # Pattern 2: <tag attrs>text</tag>
        pattern2 = rf'(<{tag}\s+(?![^>]*data-i18n)[^>]*?)>(\s*){escaped}(\s*)</{tag}>'
        if re.search(pattern2, content):
            def replacer(m):
                return f'{m.group(1)} data-i18n="{key}">{m.group(2)}{text}{m.group(3)}</{tag}>'
            content = re.sub(pattern2, replacer, content, count=1)

    return content

def process_file(filepath):
    """Process HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        original_count = content.count('data-i18n=')

        # Apply all translations
        for text, key in ALL_TRANSLATIONS.items():
            if text in content:
                content = add_i18n_attribute(content, text, key)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            new_count = content.count('data-i18n=')
            added = new_count - original_count
            print(f"✅ {filepath}: +{added} attributes (Total: {new_count})")
            return added
        else:
            print(f"⏭️  {filepath}: No new attributes")
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
    print("COMPLETING ALL TRANSLATIONS")
    print("="*80)
    print()

    # Process HTML files
    total_added = 0
    for filename in files:
        if os.path.exists(filename):
            added = process_file(filename)
            total_added += added
        else:
            print(f"⚠️  {filename}: Not found")

    print()
    print("="*80)
    print(f"SUMMARY: Added {total_added} new translation attributes")
    print("="*80)
    print()
    print("Next: Update js/i18n.js with new Vietnamese translations")
    print("Run: python3 check_translations.py to verify coverage")

if __name__ == '__main__':
    main()
