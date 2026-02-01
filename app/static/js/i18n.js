/**
 * Internationalization (i18n) Support
 * English and Vietnamese language support
 */

// Translation dictionaries
const translations = {
    en: {
        // Navigation
        'nav.home': 'Home',
        'nav.dashboard': 'Main Dashboard',
        'nav.history': 'Historical Analysis',
        'nav.charts': 'Advanced Charts',
        'nav.forecast': 'Price Forecast',
        'nav.portfolio': 'Portfolio',
        'nav.macro': 'Macro Analysis',
        'nav.alerts': 'Alerts System',
        'nav.automation': 'Trading Automation',
        'nav.settings': 'Settings',
        'nav.menu': 'Menu',

        // Common
        'common.loading': 'Loading...',
        'common.last_updated': 'Last Updated',
        'common.analysis_date': 'Analysis Date',
        'common.save': 'Save',
        'common.cancel': 'Cancel',
        'common.confirm': 'Confirm',
        'common.delete': 'Delete',
        'common.edit': 'Edit',
        'common.apply': 'Apply',
        'common.reset': 'Reset',
        'common.search': 'Search',
        'common.filter': 'Filter',
        'common.select_all': 'Select All',
        'common.clear_all': 'Clear All',
        'common.select_visible': 'Select Visible',
        'common.ok': 'OK',
        'common.close': 'Close',

        // Stock Categories
        'category.all_assets': 'All Assets',
        'category.all': 'All Stocks',
        'category.commodities': 'Commodities',
        'category.blue_chips': 'Blue Chips',
        'category.banks': 'Banks',
        'category.real_estate': 'Real Estate',
        'category.tech': 'Technology',
        'category.consumer': 'Consumer',
        'category.oil_gas': 'Oil & Gas',
        'category.affordable': 'Affordable',
        'category.industrial': 'Industrial',
        'category.transportation': 'Transportation',
        'category.utilities': 'Utilities',

        // Alerts & Notifications
        'alert.success': 'Success',
        'alert.error': 'Error',
        'alert.warning': 'Warning',
        'alert.info': 'Information',
        'alert.confirm': 'Confirm',

        // Messages
        'msg.watchlist_saved': 'Watchlist saved successfully! {count} stocks will be monitored.',
        'msg.select_stock': 'Please select at least one stock',
        'msg.select_a_stock': 'Please select a stock',
        'msg.select_stocks_plural': 'Please select at least {count} stocks',
        'msg.select_min_2_stocks': 'Please select at least 2 stocks to compare',
        'msg.select_max_10_stocks': 'Please select maximum 10 stocks for better visualization',
        'msg.no_historical_data': 'No historical data available for selected stocks',
        'msg.no_data_for_stock': 'No historical data available for {stock}. This stock may not have history data yet.',
        'msg.not_enough_data': 'Not enough data for {stock} in selected timeframe ({timeframe}). Try a shorter timeframe.',
        'msg.error_loading_data': 'Error loading data for {stock}: {error}',
        'msg.enter_budget': 'Please enter a budget amount',
        'msg.settings_saved': 'Settings saved successfully!',
        'msg.settings_reset': 'Settings reset to defaults!',
        'msg.confirm_reset': 'Are you sure you want to reset all settings to defaults?',

        // Dashboard
        'dashboard.live': 'LIVE',
        'dashboard.real_time': 'Real-Time Market Overview',
        'dashboard.selected': 'selected',
        'dashboard.stocks': 'stocks',
        'dashboard.apply_watchlist': 'Apply Watchlist',
        'dashboard.stock_picker': 'Stock Picker',
        'dashboard.price_overview': 'Price Overview',
        'dashboard.price_chart': 'Price Chart',
        'dashboard.volume_chart': 'Volume Chart',
        'dashboard.volume_analysis': 'Volume Analysis',
        'dashboard.performance_metrics': 'Performance Metrics',
        'dashboard.market_indicators': 'Market Indicators',
        'dashboard.stock_comparison': 'Stock Comparison',
        'dashboard.technical_indicators': 'Technical Indicators',
        'dashboard.moving_averages': 'Moving Averages',
        'dashboard.trend_analysis': 'Trend Analysis',
        'dashboard.select_stocks': 'Select Stocks',
        'dashboard.select_time_period': 'Select Time Period',
        'dashboard.generate_forecast': 'Generate Forecast',
        'dashboard.analyze': 'Analyze',
        'dashboard.refresh': 'Refresh',
        'dashboard.export': 'Export',
        'dashboard.watchlist': 'Watchlist',
        'dashboard.portfolio_summary': 'Portfolio Summary',
        'dashboard.total_value': 'Total Value',
        'dashboard.total_gain': 'Total Gain/Loss',
        'dashboard.diversification': 'Diversification',
        'dashboard.risk_analysis': 'Risk Analysis',
        'dashboard.sector_allocation': 'Sector Allocation',
        'dashboard.top_performers': 'Top Performers',
        'dashboard.top_losers': 'Top Losers',
        'dashboard.monitoring_desc': 'Real-time monitoring of 233 Vietnamese stocks with performance tracking',
        'dashboard.select_stocks_monitor': 'Select Stocks to Monitor',
        'dashboard.search_placeholder': 'Search stocks by symbol or name...',
        'dashboard.customize_watchlist': 'Customize your watchlist with stocks and commodities',
        'dashboard.selected_assets': 'Selected Assets:',
        'dashboard.performance_heatmap': 'Performance Heatmap',
        'dashboard.score_distribution': 'Score Distribution',
        'dashboard.price_volume_analysis': 'Price & Volume Analysis',
        'dashboard.rsi_distribution': 'RSI Distribution',
        'dashboard.sector_performance': 'Sector Performance',
        'dashboard.detailed_analysis': 'Detailed Stock Analysis',
        'dashboard.monitoring': 'Monitoring',
        'dashboard.strong_buy': 'Strong Buy',
        'dashboard.buy': 'Buy',
        'dashboard.hold': 'Hold',
        'dashboard.sell': 'Sell',
        'dashboard.avg_score': 'Avg Score',

        // Common
        'common.items': 'items',
        'common.expand_all': 'Expand All',
        'common.collapse_all': 'Collapse All',
        'common.clear_filter': 'Clear Filter',
        'common.select_stocks_to_begin': 'Select stocks to begin',
        'common.no_stocks_selected': 'No stocks selected',
        'common.search_stocks_placeholder': 'Search stocks by symbol or name...',
        'common.loading_heatmap': 'Loading heatmap...',
        'common.waiting_data': 'Waiting for data...',
        'common.loading_stock_data': 'Loading stock data...',

        // Table headers
        'table.symbol': 'Symbol',
        'table.stock': 'Stock',
        'table.price': 'Price',
        'table.change': 'Change',
        'table.volume': 'Volume',
        'table.score': 'Score',
        'table.rsi': 'RSI',
        'table.recommendation': 'Recommendation',
        'table.signals': 'Signals',
        'table.date': 'Date',
        'table.open': 'Open',
        'table.high': 'High',
        'table.low': 'Low',
        'table.close': 'Close',
        'table.action': 'Action',
        'table.type': 'Type',
        'table.name': 'Name',
        'table.value': 'Value',
        'table.quantity': 'Quantity',
        'table.avg_price': 'Average Price',
        'table.total_cost': 'Total Cost',
        'table.current_value': 'Current Value',
        'table.profit_loss': 'Profit/Loss',
        'table.return': 'Return',
        'table.last_update': 'Last Update',
        'table.timestamp': 'Timestamp',

        // Time periods
        'period.7d': '7D',
        'period.30d': '30D',
        'period.90d': '90D',
        'period.1y': '1Y',

        // Historical Analysis
        'history.title': 'Historical Analysis',
        'history.subtitle': 'Analyze historical stock performance and trends',
        'history.select_period': 'Select Time Period',
        'history.last_7_days': 'Last 7 Days',
        'history.last_30_days': 'Last 30 Days',
        'history.last_60_days': 'Last 60 Days',
        'history.last_90_days': 'Last 90 Days',
        'history.last_6_months': 'Last 6 Months',
        'history.last_year': 'Last Year',
        'history.time_period': 'Time Period:',
        'history.custom_range': 'Custom Range',
        'history.from_date': 'From Date',
        'history.to_date': 'To Date',
        'history.compare_stocks': 'Compare Stocks',
        'history.view_details': 'View Details',

        // Price Forecast
        'forecast.title': 'Price Forecast',
        'forecast.subtitle': 'Predict future stock prices using historical data',
        'forecast.select_stock': 'Select Stock',
        'forecast.forecast_period': 'Forecast Period',
        'forecast.7_days': '7 Days',
        'forecast.30_days': '30 Days',
        'forecast.90_days': '90 Days',
        'forecast.prediction': 'Price Prediction',
        'forecast.confidence': 'Confidence Level',
        'forecast.trend': 'Trend',
        'forecast.upward': 'Upward',
        'forecast.downward': 'Downward',
        'forecast.neutral': 'Neutral',

        // Portfolio/Advanced
        'portfolio.title': 'Portfolio Analytics',
        'portfolio.subtitle': 'Advanced portfolio analysis and optimization',
        'portfolio.enter_budget': 'Enter Budget',
        'portfolio.budget_amount': 'Budget Amount',
        'portfolio.currency': 'Currency',
        'portfolio.select_assets': 'Select Assets',
        'portfolio.allocation': 'Asset Allocation',
        'portfolio.optimize': 'Optimize Portfolio',
        'portfolio.rebalance': 'Rebalance',
        'portfolio.performance': 'Performance',
        'portfolio.returns': 'Returns',
        'portfolio.volatility': 'Volatility',
        'portfolio.sharpe_ratio': 'Sharpe Ratio',

        // Alerts System
        'alerts.title': 'Alerts System',
        'alerts.subtitle': 'Set up price alerts and notifications',
        'alerts.create_alert': 'Create Alert',
        'alerts.active_alerts': 'Active Alerts',
        'alerts.alert_history': 'Alert History',
        'alerts.stock': 'Stock',
        'alerts.condition': 'Condition',
        'alerts.target_price': 'Target Price',
        'alerts.current_price': 'Current Price',
        'alerts.status': 'Status',
        'alerts.triggered': 'Triggered',
        'alerts.pending': 'Pending',
        'alerts.price_above': 'Price Above',
        'alerts.price_below': 'Price Below',
        'alerts.percent_change': 'Percent Change',
        'alerts.volume_spike': 'Volume Spike',

        // Trading Automation
        'automation.title': 'Trading Automation',
        'automation.subtitle': 'Automate your trading strategies',
        'automation.create_strategy': 'Create Strategy',
        'automation.active_strategies': 'Active Strategies',
        'automation.strategy_name': 'Strategy Name',
        'automation.entry_conditions': 'Entry Conditions',
        'automation.exit_conditions': 'Exit Conditions',
        'automation.risk_management': 'Risk Management',
        'automation.stop_loss': 'Stop Loss',
        'automation.take_profit': 'Take Profit',
        'automation.position_size': 'Position Size',
        'automation.backtest': 'Backtest',
        'automation.activate': 'Activate',
        'automation.deactivate': 'Deactivate',

        // Home/Index
        'home.title': 'VNStock Analytics',
        'home.subtitle': 'Professional stock market analysis and trading tools',
        'home.welcome': 'Welcome to VNStock Analytics',
        'home.total_stocks': 'Total Stocks',
        'home.total_assets': 'Total Assets',
        'home.categories': 'Categories',
        'home.get_started': 'Get Started',
        'home.features': 'Features',
        'home.learn_more': 'Learn More',
        'home.hero_title': 'Professional Stock Analytics Platform',
        'home.hero_subtitle': 'Tools for Vietnamese market investors',
        'home.trading_tools': 'Trading & Analytics Tools',
        'home.ai_forecast': 'AI Price Forecast',
        'home.advanced_analytics': 'Advanced Analytics',
        'home.professional_charts': 'Professional Charts',
        'home.macro_analysis': 'Macro Analysis',
        'home.price_alerts': 'Price Alerts',
        'home.why_choose': 'Why Choose Our Platform',
        'home.comprehensive': 'Comprehensive Coverage',
        'home.ai_insights': 'AI-Powered Insights',
        'home.real_time': 'Real-Time Data',
        'home.advanced_tools': 'Advanced Tools',

        // Menu Categories
        'menu.dashboards': 'Dashboards',
        'menu.market_analysis': 'Market Analysis',
        'menu.investment_tools': 'Investment Tools',
        'menu.automation_alerts': 'Automation & Alerts',
        'menu.configuration': 'Configuration',
        'menu.tools': 'Tools',
        'menu.automation': 'Automation',
        'menu.platform': 'Platform',
        'menu.all_dashboards': 'All Dashboards',

        // Page Headings
        'page.main_dashboard': 'Main Dashboard - Real-Time Market Overview',
        'page.historical_price': 'Historical Price Analysis',
        'page.advanced_charts': 'Advanced Charts & Technical Analysis',
        'page.advanced_analytics': 'Advanced Analytics Dashboard',
        'page.price_alerts_system': 'Price Alerts System',
        'page.trading_automation': 'Automated Trading Configuration',

        // Charts and Analysis
        'charts.candlestick': 'Candlestick Chart with Moving Averages',
        'charts.volume_bars': 'Volume Bars',
        'charts.volume_profile': 'Volume Profile',
        'charts.obv': 'On-Balance Volume (OBV)',
        'charts.mfi': 'Money Flow Index (MFI)',
        'charts.ichimoku': 'Ichimoku Cloud',
        'charts.stochastic': 'Stochastic Oscillator',
        'charts.williams': 'Williams %R',
        'charts.roc': 'Rate of Change (ROC)',
        'charts.macd': 'MACD',
        'charts.rsi': 'RSI (Relative Strength Index)',

        // Filters and Sections
        'filter.by_category': 'Filter by Category',
        'section.technical_indicators': 'Technical Indicators',
        'section.volume_analysis': 'Volume Analysis',
        'section.analysis_signals': 'Analysis & Signals',
        'section.price_statistics': 'Price Statistics',
        'section.technical_signals': 'Technical Signals',
        'section.current_stock_info': 'Current Stock Information',
        'section.forecast_metrics': 'Forecast Metrics',
        'section.model_comparison': 'Model Comparison',
        'section.daily_predictions': 'Daily Predictions',
        'section.ai_recommendations': 'AI Investment Recommendations',
        'section.spc_chart': 'Statistical Process Control Chart & Anomaly Detection',
        'section.about_control_charts': 'About Control Charts',
        'section.about_control_charts_desc': 'Control charts show price movements with statistical control limits (mean ± 3σ). AI-powered anomaly detection identifies unusual patterns and provides investment recommendations.',
        'section.prediction_evaluation': 'Prediction Accuracy Evaluation',
        'section.about_prediction_evaluation': 'About Prediction Evaluation',
        'section.about_prediction_evaluation_desc': 'Compare predicted prices with actual historical prices to evaluate forecast effectiveness. Lower error metrics (MAE, RMSE, MAPE) and higher R² indicate better prediction accuracy.',

        // Prediction Evaluation
        'evaluation.select_model': 'Select Model to Evaluate:',
        'evaluation.update': 'Update',
        'evaluation.suggested_model': 'Suggested Model',
        'evaluation.best_performer': 'Best Performer',
        'evaluation.based_on_metrics': 'Based on accuracy metrics',
        'evaluation.use_this_model': 'Use This Model',
        'evaluation.why_suggested': 'Why this model?',
        'evaluation.suggestion_reason': 'This model achieved the best overall accuracy with lowest error rates (MAE, RMSE, MAPE) and highest R² score among all evaluated models.',
        'evaluation.mae': 'MAE (Mean Absolute Error)',
        'evaluation.rmse': 'RMSE (Root Mean Square Error)',
        'evaluation.mape': 'MAPE (Mean Absolute % Error)',
        'evaluation.r2': 'R² (Coefficient of Determination)',
        'evaluation.effectiveness_score': 'Effectiveness Score',
        'evaluation.error_distribution': 'Error Distribution',
        'evaluation.predicted_vs_actual': 'Predicted vs Actual Prices',
        'evaluation.prediction_quality': 'Prediction Quality',
        'evaluation.overall_effectiveness': 'Overall Effectiveness',
        'evaluation.lower_is_better': 'Lower is better',
        'evaluation.closer_to_1_is_better': 'Closer to 1 is better',
        'evaluation.model_suffix': 'Model',
        'evaluation.highly_reliable': 'Model predictions are highly reliable. You can confidently use these forecasts for decision-making.',
        'evaluation.reasonably_accurate': 'Model predictions are reasonably accurate. Consider them as one factor in your investment decisions.',
        'evaluation.moderate_accuracy': 'Model predictions show moderate accuracy. Use with caution and combine with other analysis methods.',
        'evaluation.low_accuracy': 'Model predictions have low accuracy. Do not rely heavily on these forecasts. More data or different models may be needed.',
        'evaluation.rating.excellent': 'Excellent',
        'evaluation.rating.good': 'Good',
        'evaluation.rating.fair': 'Fair',
        'evaluation.rating.poor': 'Poor',
        'evaluation.recommendation_label': 'Recommendation:',
        'evaluation.error_range': 'Error Range (Actual - Predicted)',
        'evaluation.frequency': 'Frequency',

        // Table Headers
        'table.predicted_price': 'Predicted Price',
        'table.predicted_price_vnd': 'Predicted Price (VND)',
        'table.lower_bound': 'Lower Bound',
        'table.lower_bound_vnd': 'Lower Bound (VND)',
        'table.upper_bound': 'Upper Bound',
        'table.upper_bound_vnd': 'Upper Bound (VND)',
        'table.confidence': 'Confidence',

        // Forecast Labels
        'forecast.ai_powered': 'AI-Powered Stock Price Prediction',
        'forecast.prediction_model': 'Prediction Model',
        'forecast.technical_indicators': 'Technical Indicators Supporting Forecast',
        'forecast.section_title': 'Price Forecast',
        'forecast.select_stocks_settings': 'Select Stocks & Settings',
        'forecast.period_label': 'Forecast Period',
        'forecast.next_7_days': 'Next 7 Days',
        'forecast.next_14_days': 'Next 14 Days',
        'forecast.next_30_days': 'Next 30 Days',
        'forecast.next_60_days': 'Next 60 Days',
        'forecast.next_90_days': 'Next 90 Days',
        'forecast.generate_button': 'Generate Forecast',
        'forecast.disclaimer_title': 'Disclaimer:',
        'forecast.disclaimer_text': 'Price forecasts are predictions based on historical data and technical indicators. They are NOT guarantees of future performance. Always do your own research and consult a financial advisor.',
        'forecast.loading_stocks': 'Loading stocks...',
        'forecast.please_wait': 'Please wait while we load stock data from the API',
        'forecast.selected_label': 'Selected:',
        'forecast.none': 'None',
        'forecast.n_selected': '{count} selected',
        'forecast.alert_generate_first': 'Please generate a forecast first before changing the evaluation model.',

        // Model Names
        'model.ensemble': 'Ensemble (All Models Average)',
        'model.advanced_ensemble': 'Advanced Ensemble (Weighted)',
        'model.linear': 'Linear Regression',
        'model.ma': 'Moving Average',
        'model.exp': 'Exponential Smoothing',
        'model.arima': 'ARIMA',
        'model.sarima': 'SARIMA (Seasonal ARIMA)',
        'model.garch': 'GARCH (Volatility Modeling)',
        'model.lstm': 'LSTM (Long Short-Term Memory)',
        'model.prophet': 'Prophet (Facebook)',
        'model.xgboost': 'XGBoost',
        'model.random_forest': 'Random Forest',
        'model.gradient_boost': 'Gradient Boosting',
        'model.kalman': 'Kalman Filter',
        'model.wavenet': 'WaveNet',
        'model.transformer': 'Transformer',

        // Model Groups
        'model.group.ensemble': 'Ensemble Models',
        'model.group.traditional': 'Traditional Models',
        'model.group.timeseries': 'Advanced Time Series',
        'model.group.ml': 'Machine Learning',
        'model.group.advanced': 'Advanced Models',

        // Collapsible Sections
        'collapsible.tip': 'Tip: Click section headers to expand/collapse',
        'collapsible.expand_all': 'Expand All',
        'collapsible.collapse_all': 'Collapse All',

        // Advanced Features
        'advanced.title': 'Advanced Features',
        'advanced.portfolio_analytics': 'Portfolio Analytics',
        'advanced.strategy_backtesting': 'Strategy Backtesting',
        'advanced.risk_management': 'Risk Management',
        'advanced.pattern_recognition': 'Pattern Recognition',
        'advanced.machine_learning': 'Machine Learning',
        'advanced.correlation_analysis': 'Correlation Analysis',
        'advanced.budget_allocation': 'Budget Allocation & Investment Plan',

        // Alerts
        'alerts.create_new': 'Create New Alert',
        'alerts.recently_triggered': 'Recently Triggered Alerts',

        // Trading
        'trading.system_status': 'System Status',
        'trading.settings_status': 'Settings & Status',
        'trading.broker_api': 'Broker API Configuration',
        'trading.rules': 'Trading Rules',
        'trading.active_rules': 'Active Rules',
        'trading.execution_log': 'Trade Execution Log',
        'trading.backtest_simulation': 'Backtesting & Simulation',
        'trading.backtest_results': 'Backtest Results',
        'trading.equity_curve': 'Equity Curve',
        'trading.broker': 'Broker',
        'trading.select_broker': '-- Select Broker --',
        'trading.broker_hint': 'Choose your brokerage firm',
        'trading.api_secret': 'API Secret',
        'trading.api_secret_placeholder': 'Enter your API secret',
        'trading.api_secret_hint': 'Your broker\'s API secret (encrypted)',
        'trading.account_number': 'Account Number',
        'trading.account_number_placeholder': 'Trading account number',
        'trading.api_endpoint': 'API Endpoint (Optional)',
        'trading.api_endpoint_placeholder': 'https://api.broker.com',
        'trading.api_endpoint_hint': 'Custom API endpoint if using custom broker',
        'trading.max_position_size': 'Max Position Size (VND)',
        'trading.max_daily_loss': 'Max Daily Loss (%)',
        'trading.stop_loss_pct': 'Stop Loss (%)',
        'trading.take_profit_pct': 'Take Profit (%)',
        'trading.max_open_positions': 'Max Open Positions',
        'trading.cooldown_period': 'Cooldown Period (minutes)',
        'trading.backtest_period': 'Backtesting Period',
        'trading.last_30_days': 'Last 30 Days',
        'trading.last_90_days': 'Last 90 Days',
        'trading.last_6_months': 'Last 6 Months',
        'trading.last_year': 'Last Year',
        'trading.monthly_returns': 'Monthly Returns',
        'trading.win_loss_distribution': 'Win/Loss Distribution',
        'trading.hint_max_position': 'Maximum investment per trade',
        'trading.hint_max_daily_loss': 'Stop trading if daily loss exceeds this',
        'trading.hint_stop_loss': 'Auto-sell if loss exceeds this',
        'trading.hint_take_profit': 'Auto-sell if profit reaches this',
        'trading.hint_max_positions': 'Maximum concurrent holdings',
        'trading.hint_cooldown': 'Wait time between trades on same stock',
        'trading.save_risk_settings': 'Save Risk Settings',
        'trading.backtest_description': 'Test your trading rules on historical data before enabling live trading.',
        'trading.run_backtest': 'Run Backtest',
        'trading.view_results': 'View Results',
        'trading.warning_banner': 'WARNING: Automated trading involves significant risk. Only enable with proper testing and risk management. You can lose money.',
        'trading.alert_configure_api': 'Please configure and test API connection first!',
        'trading.confirm_enable_title': 'Enable automated trading?',
        'trading.confirm_enable_message': 'This will allow the system to execute real trades based on your rules.\n\nAre you sure?',
        'trading.alert_fill_broker': 'Please fill in broker and API key',
        'trading.alert_run_backtest_first': 'Please run a backtest first!',
        'trading.error_generating_backtest': 'Error generating backtest:',
        'trading.error_displaying_results': 'Error displaying results. Check console for details.',
        'trading.success_trading_enabled': 'Automated trading ENABLED\n\nThe system will now execute trades according to your rules.',
        'trading.success_trading_disabled': 'Automated trading DISABLED\n\nNo trades will be executed.',
        'trading.success_api_saved': 'API configuration saved!\n\nYour credentials are encrypted and stored securely.',
        'trading.success_rule_deleted': 'Rule deleted',
        'trading.success_risk_saved': 'Risk management settings saved!',

        // Buttons
        'button.create_alert': 'Create Alert',
        'button.reset_defaults': 'Reset to Defaults',
        'button.save_settings': 'Save Settings',

        // Settings
        'settings.title': 'Settings',
        'settings.subtitle': 'Configure your preferences and platform settings',
        'settings.budget': 'Budget & Portfolio',
        'settings.refresh': 'Data Refresh',
        'settings.api': 'API Configuration',
        'settings.display': 'Display Preferences',
        'settings.alerts': 'Alerts & Notifications',
        'settings.trading': 'Trading Configuration',

        // Footer
        'footer.copyright': '© 2024 VNStock Analytics',
        'footer.home': 'Home',
        'footer.dashboard': 'Dashboard',
        'footer.docs': 'Documentation',
        'footer.products': 'Products',
        'footer.resources': 'Resources',
        'footer.market_overview': 'Market Overview',
        'footer.ai_forecast': 'AI Forecast',
        'footer.quick_start': 'Quick Start Guide',
        'footer.features': 'Features',
        'footer.user_guide': 'User Guide',
        'footer.macro_guide': 'Macro Guide',
        'footer.documentation': 'Documentation',

        // Additional Menu
        'menu.dashboards_button': '📊 Dashboards ▼',
        'home.brand_name': '📊 VNStock Analytics',

        // Home descriptions
        'home.tools_description': 'Comprehensive suite of professional-grade analytics and trading tools',
        'home.dashboard_description': 'Real-time market monitoring with live data updates',
        'home.history_description': 'Track price movements, volume changes, and market trends',
        'home.forecast_description_1': 'Machine learning predictions using 4 models',
        'home.forecast_description_2': 'Statistical control charts with anomaly detection and investment recommendations',
        'home.advanced_description_1': 'Portfolio optimization, strategy backtesting, risk management with VaR/CVaR',
        'home.advanced_description_2': 'ML forecasting, and pattern recognition',
        'home.charts_description_1': 'Charting with Ichimoku Cloud, Volume Profile, Stochastic',
        'home.charts_description_2': 'Fibonacci, Pivot Points, and more',
        'home.macro_description_1': 'Track global factors: oil prices, interest rates, geopolitical risks',
        'home.macro_description_2': 'policy changes, and their impact on Vietnamese stocks',
        'home.alerts_description_1': 'Real-time monitoring with customizable alerts',
        'home.alerts_description_2': 'Get notified when stocks hit target prices, RSI levels, or volume spikes',
        'home.automation_description_1': 'Automated execution of trading strategies based on technical signals',
        'home.automation_description_2': 'Set custom rules for entry, exit, stop-loss, and position sizing',
        'home.trusted_description': 'Professional-grade tools trusted by serious investors',
        'home.coverage_description': '233 Vietnamese stocks and commodities with real-time data and historical analysis',
        'home.ai_description': 'Machine learning forecasts, anomaly detection, and automated investment recommendations',
        'home.professional_tools': 'Professional Tools',
        'home.tools_full_description': 'Charts, technical indicators, and risk analysis tools',

        // Tags
        'tag.realtime': 'Real-time',
        'tag.livedata': 'Live Data',
        'tag.ai_powered': 'AI Powered',
        'tag.four_models': '4 Models',
        'tag.forecast_range': '7-90 Days',
        'tag.portfolio': 'Portfolio',
        'tag.backtesting': 'Backtesting',
        'tag.risk_var': 'Risk VaR',
        'tag.candlestick': 'Candlestick',
        'tag.ichimoku': 'Ichimoku',
        'tag.indicators': '20+ Indicators',
        'tag.oil_impact': 'Oil Impact',
        'tag.geopolitics': 'Geopolitics',
        'tag.policy': 'Policy',
        'tag.notifications': 'Notifications',
        'tag.custom': 'Custom',
        'tag.rules': 'Rules',
        'tag.autotrade': 'Auto-Trade',
        'tag.new': 'NEW',
        'tag.pro': 'PRO',

        // Actions
        'action.view_dashboard': 'View Dashboard →',
        'action.analyze_history': 'Analyze History →',
        'action.generate_forecast': 'Generate Forecast →',
        'action.access_pro': 'Access Pro Tools →',
        'action.view_charts': 'View Charts →',
        'action.analyze_factors': 'Analyze Factors →',
        'action.configure_alerts': 'Configure Alerts →',
        'action.setup_automation': 'Setup Automation →',

        // Settings labels
        'settings.currency_label': 'Currency',
        'settings.total_budget': 'Total Investment Budget',
        'settings.risk_tolerance': 'Risk Tolerance',
        'settings.max_position': 'Maximum Position Size (%)',
        'settings.refresh_interval': 'Dashboard Refresh Interval',
        'settings.realtime_frequency': 'Real-time Update Frequency',
        'settings.api_endpoint': 'API Endpoint',
        'settings.api_key': 'API Key',
        'settings.theme': 'Theme',
        'settings.chart_type': 'Chart Type',
        'settings.default_timerange': 'Default Time Range',
        'settings.enable_alerts': 'Enable Price Alerts',
        'settings.alert_method': 'Alert Notification Method',
        'settings.enable_autotrading': 'Enable Auto-Trading',
        'settings.max_daily_trades': 'Maximum Daily Trades',
        'settings.default_order_type': 'Default Order Type',

        // Options
        'option.low': 'Low',
        'option.medium': 'Medium',
        'option.high': 'High',
        'option.light': 'Light',
        'option.dark': 'Dark',
        'option.candlestick': 'Candlestick',
        'option.line': 'Line',
        'option.email': 'Email',
        'option.browser': 'Browser',
        'option.market': 'Market',
        'option.limit': 'Limit',

        // Additional sections
        'section.price_history_analysis': '📊 Price History & Technical Analysis',
        'section.forecast_confidence': '📈 Price Forecast with Confidence Interval',
        'section.trade_history': '📋 Trade History',

        // Additional buttons
        'button.test_connection': '🔍 Test Connection',
        'button.save_config': '💾 Save Configuration',
        'button.add_rule': '➕ Add New Rule',
        'button.edit': '✏️ Edit',
        'button.delete': '🗑️ Delete',
        'button.activate': '▶️ Activate',
        'button.pause': '⏸️ Pause',
        'button.refresh_data': '🔄 Refresh Data',

        // Status
        'status.online': 'System Online',
        'status.connected': 'Connected',
        'status.disconnected': 'Disconnected',
        'status.active': 'Active',
        'status.inactive': 'Inactive',
        'status.running': 'Running',
        'status.stopped': 'Stopped',

        // Time ranges
        'timerange.1min': '1 minute',
        'timerange.5min': '5 minutes',
        'timerange.15min': '15 minutes',
        'timerange.30min': '30 minutes',
        'timerange.1hour': '1 hour',
        'timerange.4hours': '4 hours',
        'timerange.1day': '1 day',
        'timerange.1week': '1 week',
        'timerange.1month': '1 month',

        // Stats
        'stats.stocks_assets': 'Stocks & Assets',
        'stats.indicators': 'Indicators',
        'stats.ai_models': 'AI Models',

        // Disclaimers
        'disclaimer.title': 'Important Disclaimer',
        'disclaimer.educational': 'This platform is for educational and informational purposes only',
        'disclaimer.risk': 'All investments carry risk',
        'disclaimer.performance': 'Past performance does not guarantee future results',
        'disclaimer.not_advice': 'This is not financial advice',
        'disclaimer.dyor': 'always do your own research and consult licensed financial advisors',
        'disclaimer.before_invest': 'before making investment decisions',

        // Icons
        'nav.home_icon': '🏠 Home',
        'alerts.page_title': '🔔 Price Alerts',

        // Card descriptions
        'home.dashboard_desc': 'Real-time monitoring of 233 Vietnamese stocks with live updates, interactive visualization, technical scores, and comprehensive performance tracking.',
        'home.history_desc': 'Deep dive into price history with moving averages, RSI, MACD, and volume analysis. Multiple timeframes from 30 days to 1 year.',
        'home.forecast_desc': 'Machine learning predictions using 4 models. Statistical control charts with anomaly detection and investment recommendations.',
        'home.advanced_desc': 'Portfolio optimization, strategy backtesting, risk management with VaR/CVaR, ML forecasting, and pattern recognition.',
        'home.charts_desc': 'Institutional-grade charting with Ichimoku Cloud, Volume Profile, Stochastic, Fibonacci, Pivot Points, and more.',
        'home.macro_desc': 'Track global factors: oil prices, interest rates, geopolitical risks, policy changes, and their impact on Vietnamese stocks.',
        'home.alerts_desc': 'Real-time monitoring with customizable alerts. Get notified when stocks hit target prices, RSI levels, or volume spikes.',
        'home.automation_desc': 'Automated execution of trading strategies based on technical signals. Set custom rules for entry, exit, stop-loss, and position sizing.',

        // Feature text
        'home.coverage_text': '233 Vietnamese stocks and commodities with real-time data and historical analysis.',
        'home.ai_text': 'Machine learning forecasts, anomaly detection, and automated investment recommendations.',
        'home.tools_text': '30+ technical indicators, advanced charts, and institutional-grade analytics.',
        'home.risk_text': 'VaR, CVaR, portfolio optimization, and comprehensive risk analysis tools.',

        // Tags
        'tag.realtime_updates': 'Real-time Updates',
        'tag.9_categories': '9 Categories',
        'tag.ma20_50': 'MA20/50',
        'tag.macd': 'MACD',

        // CTA
        'cta.title': 'Start Analyzing Today',
        'cta.subtitle': 'Join thousands of investors using professional analytics',
        'cta.view_features': 'View All Features',

        // Footer
        'footer.copyright_full': '© 2026 VNStock Analytics. Built with advanced AI and data analytics.',
        'footer.disclaimer': 'For educational purposes only. Not financial advice. Trade at your own risk.',

        // Macro Analysis
        'macro.title': 'Macroeconomic & Environmental Analysis',
        'macro.subtitle': 'Global Factors Impact on Vietnamese Market',
        'macro.last_updated': 'Last Updated',
        'macro.market_sentiment': 'Overall Market Sentiment',
        'macro.sentiment_based_on': 'Based on: Oil prices, geopolitical tensions, monetary policy, economic indicators, and market news',
        'macro.key_indicators': 'Key Economic Indicators',
        'macro.tab.factors': 'Environmental Factors',
        'macro.tab.commodities': 'Commodities Impact',
        'macro.tab.geopolitical': 'Geopolitical Risks',
        'macro.tab.policy': 'Policy Changes',
        'macro.tab.news': 'News & Events',
        'macro.tab.correlation': 'Factor Correlation',

        // Macro sections
        'macro.factors_impact': 'Environmental Factors Impact',
        'macro.commodities_energy': 'Commodities & Energy Impact',
        'macro.sector_impact': 'Sector Impact Analysis',
        'macro.geopolitical_assessment': 'Geopolitical Risk Assessment',
        'macro.regional_tensions': 'Regional Tensions Impact',
        'macro.policy_regulatory': 'Policy & Regulatory Changes',
        'macro.policy_timeline': 'Policy Impact Timeline',
        'macro.market_news': 'Market News & Events',
        'macro.factor_correlation': 'Environmental Factor Correlation',
        'macro.correlation_desc': 'How different environmental factors correlate with Vietnamese stock market sectors',
        'macro.correlation_matrix': 'Correlation Matrix',

        // Macro table headers
        'macro.commodity': 'Commodity',
        'macro.current_price': 'Current Price',
        'macro.impact_level': 'Impact Level',
        'macro.affected_sectors': 'Affected Sectors',

        // Macro metrics
        'macro.oil_price': 'Global Oil Price',
        'macro.gdp_growth': 'VN GDP Growth',
        'macro.inflation': 'Inflation Rate',
        'macro.exchange_rate': 'USD/VND Rate',
        'macro.interest_rate': 'Interest Rate',

        // Macro sentiment
        'macro.sentiment.neutral': 'Neutral',
        'macro.sentiment.bullish': 'Bullish',
        'macro.sentiment.bearish': 'Bearish',
        'macro.sentiment.positive': 'POSITIVE',
        'macro.sentiment.negative': 'NEGATIVE',

        // Macro levels
        'macro.level.high': 'High',
        'macro.level.medium': 'Medium',
        'macro.level.low': 'Low',

        // Macro impact
        'macro.impact.positive': 'Positive',
        'macro.impact.negative': 'Negative',
        'macro.impact_label': 'Impact',

        // Macro risk assessment
        'macro.risk.probability': 'Probability',
        'macro.risk.sectors': 'Sectors',
        'macro.risk.affected_stocks': 'Affected Stocks',

        // Macro factor labels
        'macro.factor.positively_affected': 'Positively Affected',
        'macro.factor.negatively_affected': 'Negatively Affected',

        // Macro policy fields
        'macro.policy.date': 'Date',
        'macro.policy.type': 'Type',
        'macro.policy.description': 'Description',
        'macro.policy.affected_sectors': 'Affected Sectors',
        'macro.policy.stocks': 'Stocks',

        // Macro alert messages
        'macro.alert.high_oil': 'High Oil Price Alert',
        'macro.alert.geopolitical_risk': 'Geopolitical Risk',
        'macro.alert.consider': 'Consider',

        // Common terms
        'common.sell': 'SELL',
        'common.buy': 'BUY',
        'common.affected': 'Affected'
    },

    vi: {
        // Navigation
        'nav.home': 'Trang Chủ',
        'nav.dashboard': 'Bảng Điều Khiển',
        'nav.history': 'Phân Tích Lịch Sử',
        'nav.charts': 'Biểu Đồ Nâng Cao',
        'nav.forecast': 'Dự Báo Giá',
        'nav.portfolio': 'Danh Mục Đầu Tư',
        'nav.macro': 'Phân Tích Vĩ Mô',
        'nav.alerts': 'Hệ Thống Cảnh Báo',
        'nav.automation': 'Tự Động Giao Dịch',
        'nav.settings': 'Cài Đặt',
        'nav.menu': 'Menu',

        // Common
        'common.loading': 'Đang tải...',
        'common.last_updated': 'Cập Nhật Lần Cuối',
        'common.analysis_date': 'Ngày Phân Tích',
        'common.save': 'Lưu',
        'common.cancel': 'Hủy',
        'common.confirm': 'Xác Nhận',
        'common.delete': 'Xóa',
        'common.edit': 'Chỉnh Sửa',
        'common.apply': 'Áp Dụng',
        'common.reset': 'Đặt Lại',
        'common.search': 'Tìm Kiếm',
        'common.filter': 'Lọc',
        'common.select_all': 'Chọn Tất Cả',
        'common.clear_all': 'Xóa Tất Cả',
        'common.select_visible': 'Chọn Hiển Thị',
        'common.ok': 'Đồng Ý',
        'common.close': 'Đóng',

        // Stock Categories
        'category.all_assets': 'Tất Cả Tài Sản',
        'category.all': 'Tất Cả Cổ Phiếu',
        'category.commodities': 'Hàng Hóa',
        'category.blue_chips': 'Cổ Phiếu Blue Chip',
        'category.banks': 'Ngân Hàng',
        'category.real_estate': 'Bất Động Sản',
        'category.tech': 'Công Nghệ',
        'category.consumer': 'Tiêu Dùng',
        'category.oil_gas': 'Dầu Khí',
        'category.affordable': 'Giá Phải Chăng',
        'category.industrial': 'Công Nghiệp',
        'category.transportation': 'Vận Tải',
        'category.utilities': 'Tiện Ích',

        // Alerts & Notifications
        'alert.success': 'Thành Công',
        'alert.error': 'Lỗi',
        'alert.warning': 'Cảnh Báo',
        'alert.info': 'Thông Tin',
        'alert.confirm': 'Xác Nhận',

        // Messages
        'msg.watchlist_saved': 'Danh sách theo dõi đã được lưu! {count} cổ phiếu sẽ được giám sát.',
        'msg.select_stock': 'Vui lòng chọn ít nhất một cổ phiếu',
        'msg.select_a_stock': 'Vui lòng chọn một cổ phiếu',
        'msg.select_stocks_plural': 'Vui lòng chọn ít nhất {count} cổ phiếu',
        'msg.select_min_2_stocks': 'Vui lòng chọn ít nhất 2 cổ phiếu để so sánh',
        'msg.select_max_10_stocks': 'Vui lòng chọn tối đa 10 cổ phiếu để hiển thị tốt hơn',
        'msg.no_historical_data': 'Không có dữ liệu lịch sử cho các cổ phiếu đã chọn',
        'msg.no_data_for_stock': 'Không có dữ liệu lịch sử cho {stock}. Cổ phiếu này có thể chưa có dữ liệu lịch sử.',
        'msg.not_enough_data': 'Không đủ dữ liệu cho {stock} trong khung thời gian đã chọn ({timeframe}). Hãy thử khung thời gian ngắn hơn.',
        'msg.error_loading_data': 'Lỗi tải dữ liệu cho {stock}: {error}',
        'msg.enter_budget': 'Vui lòng nhập số tiền ngân sách',
        'msg.settings_saved': 'Cài đặt đã được lưu thành công!',
        'msg.settings_reset': 'Cài đặt đã được đặt lại về mặc định!',
        'msg.confirm_reset': 'Bạn có chắc chắn muốn đặt lại tất cả cài đặt về mặc định không?',

        // Dashboard
        'dashboard.live': 'TRỰC TIẾP',
        'dashboard.real_time': 'Tổng Quan Thị Trường Thời Gian Thực',
        'dashboard.selected': 'đã chọn',
        'dashboard.stocks': 'cổ phiếu',
        'dashboard.apply_watchlist': 'Áp Dụng Danh Sách',
        'dashboard.stock_picker': 'Chọn Cổ Phiếu',
        'dashboard.price_overview': 'Tổng Quan Giá',
        'dashboard.price_chart': 'Biểu Đồ Giá',
        'dashboard.volume_chart': 'Biểu Đồ Khối Lượng',
        'dashboard.volume_analysis': 'Phân Tích Khối Lượng',
        'dashboard.performance_metrics': 'Chỉ Số Hiệu Suất',
        'dashboard.market_indicators': 'Chỉ Báo Thị Trường',
        'dashboard.stock_comparison': 'So Sánh Cổ Phiếu',
        'dashboard.technical_indicators': 'Chỉ Báo Kỹ Thuật',
        'dashboard.moving_averages': 'Trung Bình Động',
        'dashboard.trend_analysis': 'Phân Tích Xu Hướng',
        'dashboard.select_stocks': 'Chọn Cổ Phiếu',
        'dashboard.select_time_period': 'Chọn Khoảng Thời Gian',
        'dashboard.generate_forecast': 'Tạo Dự Báo',
        'dashboard.analyze': 'Phân Tích',
        'dashboard.refresh': 'Làm Mới',
        'dashboard.export': 'Xuất',
        'dashboard.watchlist': 'Danh Sách Theo Dõi',
        'dashboard.portfolio_summary': 'Tóm Tắt Danh Mục',
        'dashboard.total_value': 'Tổng Giá Trị',
        'dashboard.total_gain': 'Tổng Lãi/Lỗ',
        'dashboard.diversification': 'Đa Dạng Hóa',
        'dashboard.risk_analysis': 'Phân Tích Rủi Ro',
        'dashboard.sector_allocation': 'Phân Bổ Ngành',
        'dashboard.top_performers': 'Tăng Mạnh Nhất',
        'dashboard.top_losers': 'Giảm Mạnh Nhất',
        'dashboard.monitoring_desc': 'Giám sát thời gian thực 233 cổ phiếu Việt Nam với theo dõi hiệu suất',
        'dashboard.select_stocks_monitor': 'Chọn Cổ Phiếu Để Giám Sát',
        'dashboard.search_placeholder': 'Tìm kiếm cổ phiếu theo mã hoặc tên...',
        'dashboard.customize_watchlist': 'Tùy chỉnh danh sách theo dõi của bạn với cổ phiếu và hàng hóa',
        'dashboard.selected_assets': 'Tài Sản Đã Chọn:',
        'dashboard.performance_heatmap': 'Bản Đồ Nhiệt Hiệu Suất',
        'dashboard.score_distribution': 'Phân Bố Điểm Số',
        'dashboard.price_volume_analysis': 'Phân Tích Giá & Khối Lượng',
        'dashboard.rsi_distribution': 'Phân Bố RSI',
        'dashboard.sector_performance': 'Hiệu Suất Ngành',
        'dashboard.detailed_analysis': 'Phân Tích Cổ Phiếu Chi Tiết',
        'dashboard.monitoring': 'Đang Giám Sát',
        'dashboard.strong_buy': 'Mua Mạnh',
        'dashboard.buy': 'Mua',
        'dashboard.hold': 'Giữ',
        'dashboard.sell': 'Bán',
        'dashboard.avg_score': 'Điểm TB',

        // Common
        'common.items': 'mục',
        'common.expand_all': 'Mở Rộng Tất Cả',
        'common.collapse_all': 'Thu Gọn Tất Cả',
        'common.clear_filter': 'Xóa Bộ Lọc',
        'common.select_stocks_to_begin': 'Chọn cổ phiếu để bắt đầu',
        'common.no_stocks_selected': 'Chưa chọn cổ phiếu nào',
        'common.search_stocks_placeholder': 'Tìm kiếm cổ phiếu theo mã hoặc tên...',
        'common.loading_heatmap': 'Đang tải bản đồ nhiệt...',
        'common.waiting_data': 'Đang chờ dữ liệu...',
        'common.loading_stock_data': 'Đang tải dữ liệu cổ phiếu...',

        // Table headers
        'table.symbol': 'Mã',
        'table.stock': 'Cổ Phiếu',
        'table.price': 'Giá',
        'table.change': 'Thay Đổi',
        'table.volume': 'Khối Lượng',
        'table.score': 'Điểm',
        'table.rsi': 'RSI',
        'table.recommendation': 'Khuyến Nghị',
        'table.signals': 'Tín Hiệu',
        'table.date': 'Ngày',
        'table.open': 'Mở Cửa',
        'table.high': 'Cao Nhất',
        'table.low': 'Thấp Nhất',
        'table.close': 'Đóng Cửa',
        'table.action': 'Hành Động',
        'table.type': 'Loại',
        'table.name': 'Tên',
        'table.value': 'Giá Trị',
        'table.quantity': 'Số Lượng',
        'table.avg_price': 'Giá Trung Bình',
        'table.total_cost': 'Tổng Chi Phí',
        'table.current_value': 'Giá Trị Hiện Tại',
        'table.profit_loss': 'Lãi/Lỗ',
        'table.return': 'Lợi Nhuận',
        'table.last_update': 'Cập Nhật Cuối',
        'table.timestamp': 'Thời Gian',

        // Time periods
        'period.7d': '7N',
        'period.30d': '30N',
        'period.90d': '90N',
        'period.1y': '1N',

        // Historical Analysis
        'history.title': 'Phân Tích Lịch Sử',
        'history.subtitle': 'Phân tích hiệu suất và xu hướng lịch sử của cổ phiếu',
        'history.select_period': 'Chọn Khoảng Thời Gian',
        'history.last_7_days': '7 Ngày Qua',
        'history.last_30_days': '30 Ngày Qua',
        'history.last_60_days': '60 Ngày Qua',
        'history.last_90_days': '90 Ngày Qua',
        'history.last_6_months': '6 Tháng Qua',
        'history.last_year': 'Năm Ngoái',
        'history.time_period': 'Khoảng Thời Gian:',
        'history.custom_range': 'Khoảng Tùy Chỉnh',
        'history.from_date': 'Từ Ngày',
        'history.to_date': 'Đến Ngày',
        'history.compare_stocks': 'So Sánh Cổ Phiếu',
        'history.view_details': 'Xem Chi Tiết',

        // Price Forecast
        'forecast.title': 'Dự Báo Giá',
        'forecast.subtitle': 'Dự đoán giá cổ phiếu tương lai dựa trên dữ liệu lịch sử',
        'forecast.select_stock': 'Chọn Cổ Phiếu',
        'forecast.forecast_period': 'Kỳ Dự Báo',
        'forecast.7_days': '7 Ngày',
        'forecast.30_days': '30 Ngày',
        'forecast.90_days': '90 Ngày',
        'forecast.prediction': 'Dự Đoán Giá',
        'forecast.confidence': 'Mức Độ Tin Cậy',
        'forecast.trend': 'Xu Hướng',
        'forecast.upward': 'Tăng',
        'forecast.downward': 'Giảm',
        'forecast.neutral': 'Trung Lập',

        // Portfolio/Advanced
        'portfolio.title': 'Phân Tích Danh Mục',
        'portfolio.subtitle': 'Phân tích và tối ưu hóa danh mục đầu tư nâng cao',
        'portfolio.enter_budget': 'Nhập Ngân Sách',
        'portfolio.budget_amount': 'Số Tiền Ngân Sách',
        'portfolio.currency': 'Tiền Tệ',
        'portfolio.select_assets': 'Chọn Tài Sản',
        'portfolio.allocation': 'Phân Bổ Tài Sản',
        'portfolio.optimize': 'Tối Ưu Danh Mục',
        'portfolio.rebalance': 'Cân Bằng Lại',
        'portfolio.performance': 'Hiệu Suất',
        'portfolio.returns': 'Lợi Nhuận',
        'portfolio.volatility': 'Biến Động',
        'portfolio.sharpe_ratio': 'Tỷ Lệ Sharpe',

        // Alerts System
        'alerts.title': 'Hệ Thống Cảnh Báo',
        'alerts.subtitle': 'Thiết lập cảnh báo giá và thông báo',
        'alerts.create_alert': 'Tạo Cảnh Báo',
        'alerts.active_alerts': 'Cảnh Báo Đang Hoạt Động',
        'alerts.alert_history': 'Lịch Sử Cảnh Báo',
        'alerts.stock': 'Cổ Phiếu',
        'alerts.condition': 'Điều Kiện',
        'alerts.target_price': 'Giá Mục Tiêu',
        'alerts.current_price': 'Giá Hiện Tại',
        'alerts.status': 'Trạng Thái',
        'alerts.triggered': 'Đã Kích Hoạt',
        'alerts.pending': 'Chờ Xử Lý',
        'alerts.price_above': 'Giá Trên',
        'alerts.price_below': 'Giá Dưới',
        'alerts.percent_change': 'Thay Đổi Phần Trăm',
        'alerts.volume_spike': 'Tăng Đột Biến Khối Lượng',

        // Trading Automation
        'automation.title': 'Tự Động Giao Dịch',
        'automation.subtitle': 'Tự động hóa chiến lược giao dịch của bạn',
        'automation.create_strategy': 'Tạo Chiến Lược',
        'automation.active_strategies': 'Chiến Lược Đang Hoạt Động',
        'automation.strategy_name': 'Tên Chiến Lược',
        'automation.entry_conditions': 'Điều Kiện Vào Lệnh',
        'automation.exit_conditions': 'Điều Kiện Thoát Lệnh',
        'automation.risk_management': 'Quản Lý Rủi Ro',
        'automation.stop_loss': 'Cắt Lỗ',
        'automation.take_profit': 'Chốt Lời',
        'automation.position_size': 'Khối Lượng Vị Thế',
        'automation.backtest': 'Kiểm Tra Ngược',
        'automation.activate': 'Kích Hoạt',
        'automation.deactivate': 'Tắt',

        // Home/Index
        'home.title': 'VNStock Analytics',
        'home.subtitle': 'Công cụ phân tích và giao dịch thị trường chứng khoán chuyên nghiệp',
        'home.welcome': 'Chào Mừng Đến Với VNStock Analytics',
        'home.total_stocks': 'Tổng Số Cổ Phiếu',
        'home.total_assets': 'Tổng Số Tài Sản',
        'home.categories': 'Danh Mục',
        'home.get_started': 'Bắt Đầu',
        'home.features': 'Tính Năng',
        'home.learn_more': 'Tìm Hiểu Thêm',
        'home.hero_title': 'Nền Tảng Phân Tích Cổ Phiếu Chuyên Nghiệp',
        'home.hero_subtitle': 'Công cụ cho nhà đầu tư thị trường Việt Nam',
        'home.trading_tools': 'Công Cụ Giao Dịch & Phân Tích',
        'home.ai_forecast': 'Dự Báo Giá AI',
        'home.advanced_analytics': 'Phân Tích Nâng Cao',
        'home.professional_charts': 'Biểu Đồ Chuyên Nghiệp',
        'home.macro_analysis': 'Phân Tích Vĩ Mô',
        'home.price_alerts': 'Cảnh Báo Giá',
        'home.why_choose': 'Tại Sao Chọn Nền Tảng Của Chúng Tôi',
        'home.comprehensive': 'Bao Phủ Toàn Diện',
        'home.ai_insights': 'Thông Tin Hỗ Trợ AI',
        'home.real_time': 'Dữ Liệu Thời Gian Thực',
        'home.advanced_tools': 'Công Cụ Nâng Cao',

        // Menu Categories
        'menu.dashboards': 'Bảng Điều Khiển',
        'menu.market_analysis': 'Phân Tích Thị Trường',
        'menu.investment_tools': 'Công Cụ Đầu Tư',
        'menu.automation_alerts': 'Tự Động & Cảnh Báo',
        'menu.configuration': 'Cấu Hình',
        'menu.tools': 'Công Cụ',
        'menu.automation': 'Tự Động Hóa',
        'menu.platform': 'Nền Tảng',
        'menu.all_dashboards': 'Tất Cả Bảng Điều Khiển',

        // Page Headings
        'page.main_dashboard': 'Bảng Điều Khiển Chính - Tổng Quan Thị Trường Thời Gian Thực',
        'page.historical_price': 'Phân Tích Giá Lịch Sử',
        'page.advanced_charts': 'Biểu Đồ Nâng Cao & Phân Tích Kỹ Thuật',
        'page.advanced_analytics': 'Bảng Điều Khiển Phân Tích Nâng Cao',
        'page.price_alerts_system': 'Hệ Thống Cảnh Báo Giá',
        'page.trading_automation': 'Cấu Hình Giao Dịch Tự Động',

        // Charts and Analysis
        'charts.candlestick': 'Biểu Đồ Nến với Đường Trung Bình Động',
        'charts.volume_bars': 'Cột Khối Lượng',
        'charts.volume_profile': 'Hồ Sơ Khối Lượng',
        'charts.obv': 'Khối Lượng Cân Bằng (OBV)',
        'charts.mfi': 'Chỉ Số Dòng Tiền (MFI)',
        'charts.ichimoku': 'Mây Ichimoku',
        'charts.stochastic': 'Bộ Dao Động Stochastic',
        'charts.williams': 'Williams %R',
        'charts.roc': 'Tốc Độ Thay Đổi (ROC)',
        'charts.macd': 'MACD',
        'charts.rsi': 'RSI (Chỉ Số Sức Mạnh Tương Đối)',

        // Filters and Sections
        'filter.by_category': 'Lọc Theo Danh Mục',
        'section.technical_indicators': 'Chỉ Báo Kỹ Thuật',
        'section.volume_analysis': 'Phân Tích Khối Lượng',
        'section.analysis_signals': 'Phân Tích & Tín Hiệu',
        'section.price_statistics': 'Thống Kê Giá',
        'section.technical_signals': 'Tín Hiệu Kỹ Thuật',
        'section.current_stock_info': 'Thông Tin Cổ Phiếu Hiện Tại',
        'section.forecast_metrics': 'Chỉ Số Dự Báo',
        'section.model_comparison': 'So Sánh Mô Hình',
        'section.daily_predictions': 'Dự Đoán Hàng Ngày',
        'section.ai_recommendations': 'Khuyến Nghị Đầu Tư AI',
        'section.spc_chart': 'Biểu Đồ Kiểm Soát Quá Trình Thống Kê & Phát Hiện Bất Thường',
        'section.about_control_charts': 'Về Biểu Đồ Kiểm Soát',
        'section.about_control_charts_desc': 'Biểu đồ kiểm soát hiển thị biến động giá với giới hạn kiểm soát thống kê (trung bình ± 3σ). Phát hiện bất thường bằng AI xác định các mẫu bất thường và cung cấp khuyến nghị đầu tư.',
        'section.prediction_evaluation': 'Đánh Giá Độ Chính Xác Dự Đoán',
        'section.about_prediction_evaluation': 'Về Đánh Giá Dự Đoán',
        'section.about_prediction_evaluation_desc': 'So sánh giá dự đoán với giá thực tế lịch sử để đánh giá hiệu quả dự báo. Chỉ số lỗi thấp hơn (MAE, RMSE, MAPE) và R² cao hơn cho thấy độ chính xác dự đoán tốt hơn.',

        // Prediction Evaluation
        'evaluation.select_model': 'Chọn Mô Hình Đánh Giá:',
        'evaluation.update': 'Cập Nhật',
        'evaluation.suggested_model': 'Mô Hình Đề Xuất',
        'evaluation.best_performer': 'Hiệu Suất Tốt Nhất',
        'evaluation.based_on_metrics': 'Dựa trên các chỉ số độ chính xác',
        'evaluation.use_this_model': 'Sử Dụng Mô Hình Này',
        'evaluation.why_suggested': 'Tại sao đề xuất mô hình này?',
        'evaluation.suggestion_reason': 'Mô hình này đạt độ chính xác tổng thể tốt nhất với tỷ lệ lỗi thấp nhất (MAE, RMSE, MAPE) và điểm R² cao nhất trong tất cả các mô hình được đánh giá.',
        'evaluation.mae': 'MAE (Sai Số Tuyệt Đối Trung Bình)',
        'evaluation.rmse': 'RMSE (Căn Bậc Hai Sai Số Bình Phương)',
        'evaluation.mape': 'MAPE (Sai Số % Tuyệt Đối Trung Bình)',
        'evaluation.r2': 'R² (Hệ Số Xác Định)',
        'evaluation.effectiveness_score': 'Điểm Hiệu Quả',
        'evaluation.error_distribution': 'Phân Bố Lỗi',
        'evaluation.predicted_vs_actual': 'Giá Dự Đoán vs Thực Tế',
        'evaluation.prediction_quality': 'Chất Lượng Dự Đoán',
        'evaluation.overall_effectiveness': 'Hiệu Quả Tổng Thể',
        'evaluation.lower_is_better': 'Càng thấp càng tốt',
        'evaluation.closer_to_1_is_better': 'Càng gần 1 càng tốt',
        'evaluation.model_suffix': 'Mô Hình',
        'evaluation.highly_reliable': 'Dự đoán của mô hình rất đáng tin cậy. Bạn có thể tự tin sử dụng các dự báo này để ra quyết định.',
        'evaluation.reasonably_accurate': 'Dự đoán của mô hình khá chính xác. Hãy xem xét chúng như một yếu tố trong quyết định đầu tư của bạn.',
        'evaluation.moderate_accuracy': 'Dự đoán của mô hình cho thấy độ chính xác vừa phải. Sử dụng thận trọng và kết hợp với các phương pháp phân tích khác.',
        'evaluation.low_accuracy': 'Dự đoán của mô hình có độ chính xác thấp. Đừng quá phụ thuộc vào các dự báo này. Có thể cần thêm dữ liệu hoặc các mô hình khác.',
        'evaluation.rating.excellent': 'Xuất Sắc',
        'evaluation.rating.good': 'Tốt',
        'evaluation.rating.fair': 'Khá',
        'evaluation.rating.poor': 'Kém',
        'evaluation.recommendation_label': 'Khuyến Nghị:',
        'evaluation.error_range': 'Phạm Vi Lỗi (Thực Tế - Dự Đoán)',
        'evaluation.frequency': 'Tần Suất',

        // Table Headers
        'table.predicted_price': 'Giá Dự Đoán',
        'table.predicted_price_vnd': 'Giá Dự Đoán (VNĐ)',
        'table.lower_bound': 'Giới Hạn Dưới',
        'table.lower_bound_vnd': 'Giới Hạn Dưới (VNĐ)',
        'table.upper_bound': 'Giới Hạn Trên',
        'table.upper_bound_vnd': 'Giới Hạn Trên (VNĐ)',
        'table.confidence': 'Độ Tin Cậy',

        // Forecast Labels
        'forecast.ai_powered': 'Dự Đoán Giá Cổ Phiếu Bằng AI',
        'forecast.prediction_model': 'Mô Hình Dự Đoán',
        'forecast.technical_indicators': 'Chỉ Báo Kỹ Thuật Hỗ Trợ Dự Báo',
        'forecast.section_title': 'Dự Báo Giá',
        'forecast.select_stocks_settings': 'Chọn Cổ Phiếu & Cài Đặt',
        'forecast.period_label': 'Kỳ Dự Báo',
        'forecast.next_7_days': '7 Ngày Tới',
        'forecast.next_14_days': '14 Ngày Tới',
        'forecast.next_30_days': '30 Ngày Tới',
        'forecast.next_60_days': '60 Ngày Tới',
        'forecast.next_90_days': '90 Ngày Tới',
        'forecast.generate_button': 'Tạo Dự Báo',
        'forecast.disclaimer_title': 'Tuyên Bố Miễn Trừ:',
        'forecast.disclaimer_text': 'Dự báo giá là dự đoán dựa trên dữ liệu lịch sử và các chỉ báo kỹ thuật. Chúng KHÔNG phải là bảo đảm về hiệu suất tương lai. Luôn tự nghiên cứu và tham khảo ý kiến cố vấn tài chính.',
        'forecast.loading_stocks': 'Đang tải cổ phiếu...',
        'forecast.please_wait': 'Vui lòng đợi trong khi chúng tôi tải dữ liệu cổ phiếu từ API',
        'forecast.selected_label': 'Đã Chọn:',
        'forecast.none': 'Không',
        'forecast.n_selected': '{count} đã chọn',
        'forecast.alert_generate_first': 'Vui lòng tạo dự báo trước khi thay đổi mô hình đánh giá.',

        // Model Names
        'model.ensemble': 'Ensemble (Trung Bình Tất Cả Mô Hình)',
        'model.advanced_ensemble': 'Ensemble Nâng Cao (Có Trọng Số)',
        'model.linear': 'Hồi Quy Tuyến Tính',
        'model.ma': 'Trung Bình Động',
        'model.exp': 'Làm Mịn Hàm Mũ',
        'model.arima': 'ARIMA',
        'model.sarima': 'SARIMA (ARIMA Theo Mùa)',
        'model.garch': 'GARCH (Mô Hình Biến Động)',
        'model.lstm': 'LSTM (Bộ Nhớ Dài Ngắn)',
        'model.prophet': 'Prophet (Facebook)',
        'model.xgboost': 'XGBoost',
        'model.random_forest': 'Rừng Ngẫu Nhiên',
        'model.gradient_boost': 'Tăng Cường Gradient',
        'model.kalman': 'Bộ Lọc Kalman',
        'model.wavenet': 'WaveNet',
        'model.transformer': 'Transformer',

        // Model Groups
        'model.group.ensemble': 'Mô Hình Ensemble',
        'model.group.traditional': 'Mô Hình Truyền Thống',
        'model.group.timeseries': 'Chuỗi Thời Gian Nâng Cao',
        'model.group.ml': 'Học Máy',
        'model.group.advanced': 'Mô Hình Nâng Cao',

        // Collapsible Sections
        'collapsible.tip': 'Mẹo: Nhấp vào tiêu đề phần để mở rộng/thu gọn',
        'collapsible.expand_all': 'Mở Rộng Tất Cả',
        'collapsible.collapse_all': 'Thu Gọn Tất Cả',

        // Advanced Features
        'advanced.title': 'Tính Năng Nâng Cao',
        'advanced.portfolio_analytics': 'Phân Tích Danh Mục',
        'advanced.strategy_backtesting': 'Kiểm Tra Chiến Lược Ngược',
        'advanced.risk_management': 'Quản Lý Rủi Ro',
        'advanced.pattern_recognition': 'Nhận Dạng Mẫu',
        'advanced.machine_learning': 'Học Máy',
        'advanced.correlation_analysis': 'Phân Tích Tương Quan',
        'advanced.budget_allocation': 'Phân Bổ Ngân Sách & Kế Hoạch Đầu Tư',

        // Alerts
        'alerts.create_new': 'Tạo Cảnh Báo Mới',
        'alerts.recently_triggered': 'Cảnh Báo Được Kích Hoạt Gần Đây',

        // Trading
        'trading.system_status': 'Trạng Thái Hệ Thống',
        'trading.settings_status': 'Cài Đặt & Trạng Thái',
        'trading.broker_api': 'Cấu Hình API Môi Giới',
        'trading.rules': 'Quy Tắc Giao Dịch',
        'trading.active_rules': 'Quy Tắc Đang Hoạt Động',
        'trading.execution_log': 'Nhật Ký Thực Thi Giao Dịch',
        'trading.backtest_simulation': 'Mô Phỏng & Kiểm Tra Ngược',
        'trading.backtest_results': 'Kết Quả Kiểm Tra Ngược',
        'trading.equity_curve': 'Đường Cong Vốn Chủ Sở Hữu',
        'trading.broker': 'Môi Giới',
        'trading.select_broker': '-- Chọn Môi Giới --',
        'trading.broker_hint': 'Chọn công ty chứng khoán của bạn',
        'trading.api_secret': 'API Secret',
        'trading.api_secret_placeholder': 'Nhập API secret của bạn',
        'trading.api_secret_hint': 'API secret của môi giới (được mã hóa)',
        'trading.account_number': 'Số Tài Khoản',
        'trading.account_number_placeholder': 'Số tài khoản giao dịch',
        'trading.api_endpoint': 'API Endpoint (Tùy Chọn)',
        'trading.api_endpoint_placeholder': 'https://api.moigioi.com',
        'trading.api_endpoint_hint': 'API endpoint tùy chỉnh nếu dùng môi giới riêng',
        'trading.max_position_size': 'Khối Lượng Vị Thế Tối Đa (VNĐ)',
        'trading.max_daily_loss': 'Thua Lỗ Tối Đa Mỗi Ngày (%)',
        'trading.stop_loss_pct': 'Cắt Lỗ (%)',
        'trading.take_profit_pct': 'Chốt Lời (%)',
        'trading.max_open_positions': 'Số Lệnh Mở Tối Đa',
        'trading.cooldown_period': 'Thời Gian Nghỉ (phút)',
        'trading.backtest_period': 'Kỳ Kiểm Tra Ngược',
        'trading.last_30_days': '30 Ngày Qua',
        'trading.last_90_days': '90 Ngày Qua',
        'trading.last_6_months': '6 Tháng Qua',
        'trading.last_year': 'Năm Ngoái',
        'trading.monthly_returns': 'Lợi Nhuận Hàng Tháng',
        'trading.win_loss_distribution': 'Phân Bổ Thắng/Thua',
        'trading.hint_max_position': 'Số tiền đầu tư tối đa mỗi giao dịch',
        'trading.hint_max_daily_loss': 'Dừng giao dịch nếu thua lỗ trong ngày vượt quá giới hạn này',
        'trading.hint_stop_loss': 'Tự động bán nếu thua lỗ vượt quá giới hạn này',
        'trading.hint_take_profit': 'Tự động bán khi lợi nhuận đạt mức này',
        'trading.hint_max_positions': 'Số lệnh giữ đồng thời tối đa',
        'trading.hint_cooldown': 'Thời gian chờ giữa các giao dịch trên cùng một cổ phiếu',
        'trading.save_risk_settings': 'Lưu Cài Đặt Rủi Ro',
        'trading.backtest_description': 'Kiểm tra quy tắc giao dịch của bạn trên dữ liệu lịch sử trước khi kích hoạt giao dịch thực.',
        'trading.run_backtest': 'Chạy Kiểm Tra',
        'trading.view_results': 'Xem Kết Quả',
        'trading.warning_banner': 'CẢNH BÁO: Giao dịch tự động có rủi ro đáng kể. Chỉ kích hoạt sau khi kiểm tra kỹ lưỡng và quản lý rủi ro đúng cách. Bạn có thể mất tiền.',
        'trading.alert_configure_api': 'Vui lòng cấu hình và kiểm tra kết nối API trước!',
        'trading.confirm_enable_title': 'Kích hoạt giao dịch tự động?',
        'trading.confirm_enable_message': 'Điều này sẽ cho phép hệ thống thực hiện giao dịch thực dựa trên quy tắc của bạn.\n\nBạn có chắc chắn?',
        'trading.alert_fill_broker': 'Vui lòng điền thông tin môi giới và API key',
        'trading.alert_run_backtest_first': 'Vui lòng chạy kiểm tra ngược trước!',
        'trading.error_generating_backtest': 'Lỗi tạo kiểm tra ngược:',
        'trading.error_displaying_results': 'Lỗi hiển thị kết quả. Kiểm tra console để biết chi tiết.',
        'trading.success_trading_enabled': 'Giao dịch tự động ĐÃ KÍCH HOẠT\n\nHệ thống sẽ thực hiện giao dịch theo quy tắc của bạn.',
        'trading.success_trading_disabled': 'Giao dịch tự động ĐÃ TẮT\n\nKhông có giao dịch nào được thực hiện.',
        'trading.success_api_saved': 'Cấu hình API đã lưu!\n\nThông tin của bạn đã được mã hóa và lưu trữ an toàn.',
        'trading.success_rule_deleted': 'Đã xóa quy tắc',
        'trading.success_risk_saved': 'Đã lưu cài đặt quản lý rủi ro!',

        // Buttons
        'button.create_alert': 'Tạo Cảnh Báo',
        'button.reset_defaults': 'Đặt Lại Mặc Định',
        'button.save_settings': 'Lưu Cài Đặt',

        // Settings
        'settings.title': 'Cài Đặt',
        'settings.subtitle': 'Cấu hình tùy chọn và cài đặt nền tảng của bạn',
        'settings.budget': 'Ngân Sách & Danh Mục',
        'settings.refresh': 'Làm Mới Dữ Liệu',
        'settings.api': 'Cấu Hình API',
        'settings.display': 'Tùy Chọn Hiển Thị',
        'settings.alerts': 'Cảnh Báo & Thông Báo',
        'settings.trading': 'Cấu Hình Giao Dịch',

        // Footer
        'footer.copyright': '© 2024 VNStock Analytics',
        'footer.home': 'Trang Chủ',
        'footer.dashboard': 'Bảng Điều Khiển',
        'footer.docs': 'Tài Liệu',
        'footer.products': 'Sản Phẩm',
        'footer.resources': 'Tài Nguyên',
        'footer.market_overview': 'Tổng Quan Thị Trường',
        'footer.ai_forecast': 'Dự Báo AI',
        'footer.quick_start': 'Hướng Dẫn Bắt Đầu Nhanh',
        'footer.features': 'Tính Năng',
        'footer.user_guide': 'Hướng Dẫn Người Dùng',
        'footer.macro_guide': 'Hướng Dẫn Vĩ Mô',
        'footer.documentation': 'Tài Liệu',

        // Additional Menu
        'menu.dashboards_button': '📊 Bảng Điều Khiển ▼',
        'home.brand_name': '📊 Phân Tích VNStock',

        // Home descriptions
        'home.tools_description': 'Bộ công cụ phân tích và giao dịch cấp chuyên nghiệp toàn diện',
        'home.dashboard_description': 'Giám sát thị trường thời gian thực với cập nhật dữ liệu trực tiếp',
        'home.history_description': 'Theo dõi biến động giá, thay đổi khối lượng và xu hướng thị trường',
        'home.forecast_description_1': 'Dự đoán học máy sử dụng 4 mô hình',
        'home.forecast_description_2': 'Biểu đồ kiểm soát thống kê với phát hiện bất thường và khuyến nghị đầu tư',
        'home.advanced_description_1': 'Tối ưu hóa danh mục, kiểm tra chiến lược ngược, quản lý rủi ro với VaR/CVaR',
        'home.advanced_description_2': 'Dự báo ML và nhận dạng mẫu',
        'home.charts_description_1': 'Biểu đồ với Ichimoku Cloud, Volume Profile, Stochastic',
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
        'home.tools_full_description': 'Biểu đồ, chỉ báo kỹ thuật và công cụ phân tích rủi ro',

        // Tags
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

        // Actions
        'action.view_dashboard': 'Xem Bảng Điều Khiển →',
        'action.analyze_history': 'Phân Tích Lịch Sử →',
        'action.generate_forecast': 'Tạo Dự Báo →',
        'action.access_pro': 'Truy Cập Công Cụ Pro →',
        'action.view_charts': 'Xem Biểu Đồ →',
        'action.analyze_factors': 'Phân Tích Các Yếu Tố →',
        'action.configure_alerts': 'Cấu Hình Cảnh Báo →',
        'action.setup_automation': 'Thiết Lập Tự Động →',

        // Settings labels
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

        // Options
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

        // Additional sections
        'section.price_history_analysis': '📊 Lịch Sử Giá & Phân Tích Kỹ Thuật',
        'section.forecast_confidence': '📈 Dự Báo Giá với Khoảng Tin Cậy',
        'section.trade_history': '📋 Lịch Sử Giao Dịch',

        // Additional buttons
        'button.test_connection': '🔍 Kiểm Tra Kết Nối',
        'button.save_config': '💾 Lưu Cấu Hình',
        'button.add_rule': '➕ Thêm Quy Tắc Mới',
        'button.edit': '✏️ Chỉnh Sửa',
        'button.delete': '🗑️ Xóa',
        'button.activate': '▶️ Kích Hoạt',
        'button.pause': '⏸️ Tạm Dừng',
        'button.refresh_data': '🔄 Làm Mới Dữ Liệu',

        // Status
        'status.online': 'Hệ Thống Trực Tuyến',
        'status.connected': 'Đã Kết Nối',
        'status.disconnected': 'Mất Kết Nối',
        'status.active': 'Hoạt Động',
        'status.inactive': 'Không Hoạt Động',
        'status.running': 'Đang Chạy',
        'status.stopped': 'Đã Dừng',

        // Time ranges
        'timerange.1min': '1 phút',
        'timerange.5min': '5 phút',
        'timerange.15min': '15 phút',
        'timerange.30min': '30 phút',
        'timerange.1hour': '1 giờ',
        'timerange.4hours': '4 giờ',
        'timerange.1day': '1 ngày',
        'timerange.1week': '1 tuần',
        'timerange.1month': '1 tháng',

        // Stats
        'stats.stocks_assets': 'Cổ Phiếu & Tài Sản',
        'stats.indicators': 'Chỉ Báo',
        'stats.ai_models': 'Mô Hình AI',

        // Disclaimers
        'disclaimer.title': 'Tuyên Bố Quan Trọng',
        'disclaimer.educational': 'Nền tảng này chỉ dành cho mục đích giáo dục và thông tin',
        'disclaimer.risk': 'Tất cả đầu tư đều có rủi ro',
        'disclaimer.performance': 'Hiệu suất trong quá khứ không đảm bảo kết quả tương lai',
        'disclaimer.not_advice': 'Đây không phải là lời khuyên tài chính',
        'disclaimer.dyor': 'luôn tự nghiên cứu và tham khảo cố vấn tài chính có giấy phép',
        'disclaimer.before_invest': 'trước khi đưa ra quyết định đầu tư',

        // Icons
        'nav.home_icon': '🏠 Trang Chủ',
        'alerts.page_title': '🔔 Cảnh Báo Giá',

        // Card descriptions
        'home.dashboard_desc': 'Giám sát thời gian thực 233 cổ phiếu Việt Nam với cập nhật trực tiếp, trực quan hóa tương tác, điểm số kỹ thuật và theo dõi hiệu suất toàn diện.',
        'home.history_desc': 'Phân tích sâu lịch sử giá với đường trung bình động, RSI, MACD và phân tích khối lượng. Nhiều khung thời gian từ 30 ngày đến 1 năm.',
        'home.forecast_desc': 'Dự đoán học máy sử dụng 4 mô hình. Biểu đồ kiểm soát thống kê với phát hiện bất thường và khuyến nghị đầu tư.',
        'home.advanced_desc': 'Tối ưu hóa danh mục, kiểm tra chiến lược ngược, quản lý rủi ro với VaR/CVaR, dự báo ML và nhận dạng mẫu.',
        'home.charts_desc': 'Biểu đồ với Ichimoku Cloud, Volume Profile, Stochastic, Fibonacci, Pivot Points và nhiều hơn nữa.',
        'home.macro_desc': 'Theo dõi các yếu tố toàn cầu: giá dầu, lãi suất, rủi ro địa chính trị, thay đổi chính sách và tác động đến cổ phiếu Việt Nam.',
        'home.alerts_desc': 'Giám sát thời gian thực với cảnh báo tùy chỉnh. Nhận thông báo khi cổ phiếu đạt giá mục tiêu, mức RSI hoặc tăng đột biến khối lượng.',
        'home.automation_desc': 'Thực thi tự động các chiến lược giao dịch dựa trên tín hiệu kỹ thuật. Đặt quy tắc tùy chỉnh cho vào lệnh, thoát lệnh, cắt lỗ và kích thước vị thế.',

        // Feature text
        'home.coverage_text': '233 cổ phiếu và hàng hóa Việt Nam với dữ liệu thời gian thực và phân tích lịch sử.',
        'home.ai_text': 'Dự báo học máy, phát hiện bất thường và khuyến nghị đầu tư tự động.',
        'home.tools_text': '30+ chỉ báo kỹ thuật, biểu đồ nâng cao và phân tích chuyên nghiệp.',
        'home.risk_text': 'VaR, CVaR, tối ưu hóa danh mục và công cụ phân tích rủi ro toàn diện.',

        // Tags
        'tag.realtime_updates': 'Cập Nhật Thời Gian Thực',
        'tag.9_categories': '9 Danh Mục',
        'tag.ma20_50': 'MA20/50',
        'tag.macd': 'MACD',

        // CTA
        'cta.title': 'Bắt Đầu Phân Tích Ngay Hôm Nay',
        'cta.subtitle': 'Tham gia hàng nghìn nhà đầu tư sử dụng công cụ phân tích chuyên nghiệp',
        'cta.view_features': 'Xem Tất Cả Tính Năng',

        // Footer
        'footer.copyright_full': '© 2026 VNStock Analytics. Được xây dựng với AI và phân tích dữ liệu tiên tiến.',
        'footer.disclaimer': 'Chỉ dành cho mục đích giáo dục. Không phải lời khuyên tài chính. Giao dịch có rủi ro.',

        // Macro Analysis
        'macro.title': 'Phân Tích Kinh Tế Vĩ Mô & Môi Trường',
        'macro.subtitle': 'Các Yếu Tố Toàn Cầu Ảnh Hưởng Đến Thị Trường Việt Nam',
        'macro.last_updated': 'Cập Nhật Lần Cuối',
        'macro.market_sentiment': 'Tâm Lý Thị Trường Tổng Thể',
        'macro.sentiment_based_on': 'Dựa trên: Giá dầu, căng thẳng địa chính trị, chính sách tiền tệ, chỉ số kinh tế và tin tức thị trường',
        'macro.key_indicators': 'Chỉ Số Kinh Tế Chính',
        'macro.tab.factors': 'Yếu Tố Môi Trường',
        'macro.tab.commodities': 'Tác Động Hàng Hóa',
        'macro.tab.geopolitical': 'Rủi Ro Địa Chính Trị',
        'macro.tab.policy': 'Thay Đổi Chính Sách',
        'macro.tab.news': 'Tin Tức & Sự Kiện',
        'macro.tab.correlation': 'Tương Quan Yếu Tố',

        // Macro sections
        'macro.factors_impact': 'Tác Động Yếu Tố Môi Trường',
        'macro.commodities_energy': 'Tác Động Hàng Hóa & Năng Lượng',
        'macro.sector_impact': 'Phân Tích Tác Động Ngành',
        'macro.geopolitical_assessment': 'Đánh Giá Rủi Ro Địa Chính Trị',
        'macro.regional_tensions': 'Tác Động Căng Thẳng Khu Vực',
        'macro.policy_regulatory': 'Thay Đổi Chính Sách & Quy Định',
        'macro.policy_timeline': 'Tiến Trình Tác Động Chính Sách',
        'macro.market_news': 'Tin Tức & Sự Kiện Thị Trường',
        'macro.factor_correlation': 'Tương Quan Yếu Tố Môi Trường',
        'macro.correlation_desc': 'Mối tương quan giữa các yếu tố môi trường với các ngành thị trường chứng khoán Việt Nam',
        'macro.correlation_matrix': 'Ma Trận Tương Quan',

        // Macro table headers
        'macro.commodity': 'Hàng Hóa',
        'macro.current_price': 'Giá Hiện Tại',
        'macro.impact_level': 'Mức Độ Tác Động',
        'macro.affected_sectors': 'Ngành Ảnh Hưởng',

        // Macro metrics
        'macro.oil_price': 'Giá Dầu Toàn Cầu',
        'macro.gdp_growth': 'Tăng Trưởng GDP VN',
        'macro.inflation': 'Tỷ Lệ Lạm Phát',
        'macro.exchange_rate': 'Tỷ Giá USD/VND',
        'macro.interest_rate': 'Lãi Suất',

        // Macro sentiment
        'macro.sentiment.neutral': 'Trung Lập',
        'macro.sentiment.bullish': 'Tăng Giá',
        'macro.sentiment.bearish': 'Giảm Giá',
        'macro.sentiment.positive': 'TÍCH CỰC',
        'macro.sentiment.negative': 'TIÊU CỰC',

        // Macro levels
        'macro.level.high': 'Cao',
        'macro.level.medium': 'Trung Bình',
        'macro.level.low': 'Thấp',

        // Macro impact
        'macro.impact.positive': 'Tích Cực',
        'macro.impact.negative': 'Tiêu Cực',
        'macro.impact_label': 'Tác Động',

        // Macro risk assessment
        'macro.risk.probability': 'Xác Suất',
        'macro.risk.sectors': 'Ngành',
        'macro.risk.affected_stocks': 'Cổ Phiếu Ảnh Hưởng',

        // Macro factor labels
        'macro.factor.positively_affected': 'Ảnh Hưởng Tích Cực',
        'macro.factor.negatively_affected': 'Ảnh Hưởng Tiêu Cực',

        // Macro policy fields
        'macro.policy.date': 'Ngày',
        'macro.policy.type': 'Loại',
        'macro.policy.description': 'Mô Tả',
        'macro.policy.affected_sectors': 'Ngành Ảnh Hưởng',
        'macro.policy.stocks': 'Cổ Phiếu',

        // Macro alert messages
        'macro.alert.high_oil': 'Cảnh Báo Giá Dầu Cao',
        'macro.alert.geopolitical_risk': 'Rủi Ro Địa Chính Trị',
        'macro.alert.consider': 'Nên Xem Xét',

        // Common terms
        'common.sell': 'BÁN',
        'common.buy': 'MUA',
        'common.affected': 'Ảnh Hưởng'
    }
};

// Current language
let currentLanguage = 'en';

/**
 * Initialize i18n system
 */
let i18nInitialized = false;

function initI18n() {
    // Prevent double initialization
    if (i18nInitialized) {
        console.log('i18n already initialized');
        return;
    }

    try {
        // Load saved language preference
        const saved = localStorage.getItem('language');
        if (saved && translations[saved]) {
            currentLanguage = saved;
        }

        // Apply translations
        translatePage();

        // Create language switcher if not exists
        createLanguageSwitcher();

        i18nInitialized = true;
        console.log('✓ i18n system initialized');
    } catch (error) {
        console.error('Error initializing i18n:', error);
    }
}

/**
 * Get translation for a key
 * @param {string} key - Translation key (e.g., 'nav.home')
 * @param {object} params - Parameters for interpolation
 * @returns {string} Translated text
 */
function t(key, params = {}) {
    let text = translations[currentLanguage][key] || translations['en'][key] || key;

    // Replace parameters {param} with values
    Object.keys(params).forEach(param => {
        text = text.replace(`{${param}}`, params[param]);
    });

    return text;
}

/**
 * Switch language
 * @param {string} lang - Language code ('en' or 'vi')
 */
function switchLanguage(lang) {
    if (!translations[lang]) {
        console.error(`Language ${lang} not supported`);
        return;
    }

    console.log(`Switching language to: ${lang}`);
    currentLanguage = lang;
    localStorage.setItem('language', lang);

    // Re-translate page
    translatePage();

    // Update switcher UI
    updateLanguageSwitcher();

    // Visual feedback
    showLanguageChangeNotification(lang);
}

/**
 * Translate all elements with data-i18n attribute
 */
function translatePage() {
    let translatedCount = 0;

    // Translate text content (excluding option and optgroup - they have special handling below)
    document.querySelectorAll('[data-i18n]:not(option):not(optgroup)').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const text = t(key);

        // Check if we should translate innerHTML or just text
        if (element.hasAttribute('data-i18n-html')) {
            element.innerHTML = text;
        } else {
            element.textContent = text;
        }
        translatedCount++;
    });

    // Translate placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        element.placeholder = t(key);
        translatedCount++;
    });

    // Translate titles
    document.querySelectorAll('[data-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-i18n-title');
        element.title = t(key);
        translatedCount++;
    });

    // Special handling for optgroup labels
    document.querySelectorAll('optgroup[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const text = t(key);
        // Extract emoji if present in current label
        const currentLabel = element.getAttribute('label');
        const emojiMatch = currentLabel.match(/^([\u{1F000}-\u{1F9FF}]+)\s*/u);
        if (emojiMatch) {
            element.setAttribute('label', emojiMatch[1] + ' ' + text);
        } else {
            element.setAttribute('label', text);
        }
        translatedCount++;
    });

    // Special handling for option elements
    document.querySelectorAll('option[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const text = t(key);
        // Extract emoji if present in current text
        const currentText = element.textContent;
        const emojiMatch = currentText.match(/^([\u{1F000}-\u{1F9FF}]+)\s*/u);
        if (emojiMatch) {
            element.textContent = emojiMatch[1] + ' ' + text;
        } else {
            element.textContent = text;
        }
        translatedCount++;
    });

    console.log(`Translated ${translatedCount} elements to ${currentLanguage}`);
}

/**
 * Create language switcher button
 */
function createLanguageSwitcher() {
    try {
        // Check if already exists
        if (document.getElementById('languageSwitcher')) {
            console.log('Language switcher already exists');
            return;
        }

        // Find nav container
        const navContainer = document.querySelector('.nav-container');
        if (!navContainer) {
            console.warn('Nav container not found');
            return;
        }

    // Create switcher
    const switcher = document.createElement('div');
    switcher.id = 'languageSwitcher';
    switcher.className = 'language-switcher';

    // Create buttons with event listeners instead of onclick
    const enBtn = document.createElement('button');
    enBtn.className = `lang-btn ${currentLanguage === 'en' ? 'active' : ''}`;
    enBtn.textContent = 'EN';
    enBtn.addEventListener('click', () => switchLanguage('en'));

    const viBtn = document.createElement('button');
    viBtn.className = `lang-btn ${currentLanguage === 'vi' ? 'active' : ''}`;
    viBtn.textContent = 'VI';
    viBtn.addEventListener('click', () => switchLanguage('vi'));

    switcher.appendChild(enBtn);
    switcher.appendChild(viBtn);

    // Check if menu exists
    const navMenu = navContainer.querySelector('.nav-menu');

    if (!navMenu) {
        // No menu found, just append switcher to nav container
        navContainer.appendChild(switcher);
        console.log('✓ Language switcher added to nav');
        return;
    }

    // Check if menu is already wrapped in nav-right-section
    let rightSection = navContainer.querySelector('.nav-right-section');

    if (!rightSection) {
        // Create wrapper for language switcher and menu
        rightSection = document.createElement('div');
        rightSection.className = 'nav-right-section';

        // Get the parent of navMenu and replace navMenu with rightSection
        const parent = navMenu.parentElement;
        parent.replaceChild(rightSection, navMenu);

        // Now add menu to rightSection
        rightSection.appendChild(navMenu);
    } else {
        // rightSection already exists
        // Check if navMenu is inside it
        if (navMenu.parentElement !== rightSection) {
            // Remove navMenu from its current parent and add to rightSection
            navMenu.parentElement.removeChild(navMenu);
            rightSection.appendChild(navMenu);
        }
    }

    // Now add switcher before menu
    // At this point navMenu should be a child of rightSection
    try {
        // Verify parent-child relationship before insertion
        if (navMenu.parentElement === rightSection) {
            rightSection.insertBefore(switcher, navMenu);
            console.log('✓ Language switcher added next to menu');
        } else {
            // Fallback: append to rightSection
            rightSection.appendChild(switcher);
            console.log('✓ Language switcher appended to nav section');
        }
    } catch (insertError) {
        // Last resort: just append to rightSection
        console.warn('Failed to insert before menu, appending instead:', insertError);
        rightSection.appendChild(switcher);
        console.log('✓ Language switcher added to nav section (fallback)');
    }

    // Inject styles if not already present
    if (!document.getElementById('languageSwitcherStyles')) {
        const style = document.createElement('style');
        style.id = 'languageSwitcherStyles';
        style.textContent = `
            /* Ensure nav-container has proper flex layout */
            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 16px;
            }

            /* Group language switcher and menu together */
            .language-switcher {
                display: flex;
                gap: 4px;
                background: #f1f5f9;
                padding: 4px;
                border-radius: 8px;
                margin-right: 12px;
            }

            .lang-btn {
                padding: 8px 14px;
                background: transparent;
                border: none;
                border-radius: 6px;
                font-weight: 600;
                font-size: 0.9em;
                color: #64748b;
                cursor: pointer;
                transition: all 0.2s;
                min-width: 40px;
            }

            .lang-btn:hover {
                background: #e2e8f0;
                color: #475569;
            }

            .lang-btn.active {
                background: #c41c16;
                color: white;
            }

            /* Wrapper to keep language switcher and menu together */
            .nav-right-section {
                display: flex;
                align-items: center;
                gap: 12px;
            }

            @media (max-width: 768px) {
                .language-switcher {
                    padding: 3px;
                    margin-right: 8px;
                }

                .lang-btn {
                    padding: 6px 10px;
                    font-size: 0.8em;
                    min-width: 35px;
                }
            }
        `;
        document.head.appendChild(style);
    }
    } catch (error) {
        console.error('Error creating language switcher:', error);
    }
}

/**
 * Update language switcher button states
 */
function updateLanguageSwitcher() {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        const lang = btn.textContent.toLowerCase();
        if (lang === currentLanguage) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

/**
 * Show language change notification
 */
function showLanguageChangeNotification(lang) {
    const langName = lang === 'en' ? 'English' : 'Tiếng Việt';

    // Use custom dialog if available, otherwise console
    if (typeof showInfo === 'function') {
        showInfo(`Language changed to ${langName}`);
    } else {
        console.log(`✓ Language changed to ${langName}`);
    }
}

/**
 * Get current language
 */
function getCurrentLanguage() {
    return currentLanguage;
}

// Auto-initialize on page load
if (typeof window !== 'undefined') {
    // Expose functions to window for onclick handlers
    window.switchLanguage = switchLanguage;
    window.t = t;
    window.getCurrentLanguage = getCurrentLanguage;
    window.translatePage = translatePage;

    window.addEventListener('DOMContentLoaded', initI18n);
}
