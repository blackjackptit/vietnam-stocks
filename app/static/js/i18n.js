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
        'nav.portfolio_analytics': 'Portfolio Analytics',
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
        'dashboard.monitoring_desc': 'Real-time monitoring of {count} Vietnamese stocks with performance tracking',
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
        'table.t_plus': 'T+2 Valid',
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
        'table.chart': 'Chart',

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
        'portfolio.plan_generator': '📊 Investment Plan Generator',
        'portfolio.subtitle': 'Advanced portfolio analysis and optimization',
        'portfolio.analyze_button': '📈 Analyze Portfolio',
        'portfolio.investment_budget': 'Investment Budget',
        'portfolio.budget_placeholder': 'Enter amount (e.g. 10000000)',
        'portfolio.budget_hint': 'Enter the total amount you want to invest. The system will distribute it across selected stocks based on optimal allocation.',
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
        'portfolio.recommended_actions': 'Recommended Actions with New Cash Flow',
        'portfolio.recommended_positions': 'Recommended New Positions',
        'portfolio.save_plan': 'Save Plan',
        'portfolio.download_report': 'Download Report',
        'portfolio.plan_ready': 'Investment Plan Ready!',
        'portfolio.investment_plan_results': 'Investment Plan Results',
        'portfolio.saved_plans': 'My Saved Plans',
        'portfolio.my_saved_plans': 'My Saved Investment Plans',
        'portfolio.saved_plans_desc': 'Track and compare your saved investment plans. See how they perform over time with current market prices.',
        'portfolio.no_saved_plans': 'No saved plans yet. Create and save an investment plan to track its performance!',
        'portfolio.save_investment_plan': 'Save Investment Plan',
        'portfolio.plan_name': 'Plan Name',
        'portfolio.plan_notes': 'Notes (Optional)',
        'portfolio.save': 'Save',
        'portfolio.view_details': 'View Details',
        'portfolio.annualized_return': 'Annualized Return',
        'portfolio.best_performer': 'Best Performer',
        'portfolio.worst_performer': 'Worst Performer',
        'portfolio.actual_vs_expected': 'Actual vs Expected',
        'portfolio.performance_status': 'Performance Status',
        'portfolio.win_rate': 'Win Rate',
        'portfolio.avg_gain': 'Avg Gain/Stock',
        'portfolio.total_roi': 'Total ROI',
        'portfolio.risk_level': 'Risk Level',
        'portfolio.holdings_count': 'Holdings',

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
        'charts.momentum': '💪 Momentum Indicator',
        'charts.bollinger_bands': '📊 Bollinger Bands with Price',
        'charts.atr': '📈 Average True Range (ATR)',
        'charts.historical_volatility': '📉 Historical Volatility',
        'charts.multi_stock_comparison': '📊 Multi-Stock Performance Comparison',
        'charts.risk_return_scatter': '🎯 Risk-Return Scatter Plot',
        'charts.returns_distribution': '📊 Returns Distribution',
        'charts.cumulative_returns': '📈 Cumulative Returns',
        'charts.fibonacci': '🎯 Fibonacci Retracement',
        'charts.pivot_points': '📍 Pivot Points',
        'charts.elder_ray': '🌊 Elder Ray Index',

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
        'advanced.strategy_backtesting': '⏮️ Strategy Backtesting',
        'advanced.risk_management': '⚠️ Risk Management',
        'advanced.pattern_recognition': '🔍 Pattern Recognition',
        'advanced.machine_learning': '🧠 Machine Learning',
        'advanced.correlation_analysis': '🔗 Correlation Analysis',
        'advanced.budget_allocation': 'Budget Allocation & Investment Plan',

        // Advanced Features - Descriptions
        'advanced.portfolio_desc': 'Risk metrics, diversification, asset allocation, Sharpe ratio, max drawdown',
        'advanced.backtesting_desc': 'Test trading strategies, simulate trades, performance analysis',
        'advanced.risk_desc': 'VaR, CVaR, Beta, correlation matrix, volatility analysis',
        'advanced.patterns_desc': 'Chart patterns, candlestick patterns, support/resistance',
        'advanced.ml_desc': 'LSTM forecasting, ensemble models, feature importance',
        'advanced.correlation_desc': 'Stock correlations, sector analysis, pair trading opportunities',

        // Advanced Features - Info Messages
        'advanced.portfolio_info': 'Build and analyze your portfolio with advanced metrics including Sharpe ratio, maximum drawdown, and asset allocation optimization.',
        'advanced.backtesting_info': 'Test your trading strategies on historical data. See how your strategy would have performed.',
        'advanced.risk_info': 'Advanced risk metrics to help you understand and manage investment risk.',
        'advanced.patterns_info': 'Automatic detection of chart patterns and candlestick formations.',
        'advanced.ml_info': 'Advanced LSTM neural network predictions with confidence intervals.',
        'advanced.correlation_info': 'Analyze correlations between stocks for diversification and pair trading.',

        // Common Buttons & Actions
        'common.select_stocks': 'Select Stocks',
        'common.search_stocks': 'Search stocks...',
        'common.all': 'All',
        'common.clear': 'Clear',
        'common.visible': 'Visible',
        'common.selected': 'selected',
        'common.analyze': 'Analyze',
        'common.calculate': 'Calculate',
        'common.generate': 'Generate',
        'common.run': 'Run',
        'common.detect': 'Detect',
        'common.add': 'Add',
        'common.remove': 'Remove',
        'common.hold': 'HOLD',
        'common.sell_action': 'SELL',
        'common.buy_more': 'BUY MORE',

        // Form Labels & Placeholders
        'form.select_stock': 'Select Stock:',
        'form.loading': '-- Loading --',
        'form.enter_amount': 'Enter amount',
        'form.placeholder_search': 'Search...',

        // Validation Messages
        'validation.select_min_stocks': 'Please select at least {count} stocks',
        'validation.select_stock': 'Please select a stock',
        'validation.loading_data': 'Loading stock data... Please wait a moment and try again.',
        'validation.not_enough_data': 'Not enough data available for selected stocks. Please try different stocks.',

        // Chart Labels
        'chart.asset_allocation': 'Asset Allocation',
        'chart.efficient_frontier': 'Efficient Frontier',
        'chart.current_portfolio': 'Current Portfolio',
        'chart.risk_percent': 'Risk (%)',
        'chart.expected_return': 'Expected Return (%)',
        'chart.equity_curve': 'Equity Curve',
        'chart.buy_hold': 'Buy & Hold',
        'chart.portfolio_value': 'Portfolio Value (VND)',
        'chart.beta_by_stock': 'Beta by Stock',
        'chart.feature_importance': 'Feature Importance in ML Model',
        'chart.lstm_forecast': 'LSTM Neural Network Forecast',

        // Table Headers
        'table.stock': 'Stock',
        'table.shares': 'Shares',
        'table.buy_price': 'Buy Price',
        'table.current': 'Current',
        'table.profit_loss': 'Profit/Loss',
        'table.action': 'Action',
        'table.recommendation': 'Recommendation',
        'table.allocation': 'Allocation',
        'table.amount': 'Amount (VND)',
        'table.price': 'Price',
        'table.exp_return': 'Exp. Return',
        'table.risk': 'Risk',
        'table.date': 'Date',
        'table.beta': 'Beta',
        'table.volatility': 'Volatility',
        'table.var_95': 'VaR (95%)',
        'table.risk_grade': 'Risk Grade',

        // Metric Labels
        'metric.total_return': 'Total Return',
        'metric.win_rate': 'Win Rate',
        'metric.total_trades': 'Total Trades',
        'metric.avg_trade': 'Avg Trade P/L',
        'metric.model_accuracy': 'Model Accuracy',
        'metric.predicted_trend': 'Predicted Trend',
        'metric.confidence': 'Confidence',

        // Section Headers
        'section.trade_history': 'Trade History',
        'section.detected_patterns': 'Detected Patterns',
        'section.feature_importance': 'Feature Importance',
        'section.correlation_matrix': 'Correlation Matrix',
        'section.correlation_heatmap': 'Correlation Heatmap',
        'section.pair_trading': 'Pair Trading Opportunities',
        'section.allocation_breakdown': 'Allocation Breakdown',
        'section.investment_rationale': 'Investment Rationale & Evidence',
        'section.your_holdings': 'Your Current Holdings',
        'section.preferred_stocks': 'Preferred Stocks (Optional)',
        'section.smart_recommendations': 'Smart Stock Recommendations',
        'section.investment_plan': 'Recommended Investment Plan',
        'section.margin_overview': 'Margin Account Overview',
        'section.interest_cost': 'Interest Cost Analysis',
        'section.position_requirements': 'Position & Requirements',
        'section.leverage_analysis': 'Leverage Analysis',
        'section.understanding_margin': 'Understanding Margin Trading',
        'section.business_sector_analysis': '🏢 Business & Sector Analysis',
        'section.sector_diversification': '📊 Sector Diversification:',
        'section.business_overview': '💼 Business Overview:',

        // Portfolio Type
        'portfolio.select_type': 'Select Portfolio Type',
        'portfolio.existing_title': 'Existing Portfolio',
        'portfolio.existing_desc': 'Already own stocks? Track and optimize your current holdings',
        'portfolio.new_title': 'New Portfolio',
        'portfolio.new_desc': 'Starting fresh? Build an optimized portfolio from scratch',

        // Investment Budget
        'budget.enter_amount': 'Enter Your Investment Budget (VND)',
        'budget.placeholder': 'e.g., 100000000',
        'budget.example': 'Example: 100,000,000 VND (100 million)',
        'budget.additional_cash': 'Additional Cash Flow / New Investment (VND)',
        'budget.generate_plan': 'Generate Investment Plan',

        // Strategy Options
        'strategy.balanced': 'Balanced',
        'strategy.balanced_desc': 'Best risk-adjusted returns',
        'strategy.high_growth': 'High Growth',
        'strategy.high_growth_desc': 'Maximum expected returns',
        'strategy.conservative': 'Conservative',
        'strategy.conservative_desc': 'Lowest risk, stable stocks',
        'strategy.blue_chip': 'Blue Chip',
        'strategy.blue_chip_desc': 'Market leaders only',
        'strategy.select': 'Strategy:',

        // Backtest
        'backtest.run_button': 'Run Backtest',
        'backtest.sma_crossover': 'SMA Crossover (20/50)',
        'backtest.rsi_strategy': 'RSI Oversold/Overbought',
        'backtest.macd_signal': 'MACD Signal',
        'backtest.bollinger_breakout': 'Bollinger Breakout',

        // Risk Management
        'risk.calculate_button': 'Calculate Risk Metrics',
        'risk.select_stocks': 'Select Stocks:',

        // Margin Trading
        'margin.title': '💳 Margin Management',
        'margin.intro': 'Track and manage your margin account, monitor buying power, calculate margin requirements, and receive margin call warnings.',
        'margin.account_setup': '📋 Margin Account Setup',
        'margin.cash_equity': '💵 Total Cash Equity (₫)',
        'margin.cash_equity_hint': 'Your own cash invested',
        'margin.total_cash': 'Total Cash Equity (₫)',
        'margin.cash_hint': 'Your own cash invested',
        'margin.borrowed_amount': '💰 Borrowed Amount (₫)',
        'margin.borrowed_amount_hint': 'Funds borrowed from broker',
        'margin.borrowed_hint': 'Funds borrowed from broker',
        'margin.margin_ratio': '📊 Margin Ratio (%)',
        'margin.margin_ratio_hint': 'Required equity percentage (typically 50%)',
        'margin.ratio_hint': 'Required equity percentage (typically 50%)',
        'margin.interest_rate': '📈 Annual Interest Rate (%)',
        'margin.interest_hint': 'Annual borrowing cost',
        'margin.calculate_button': 'Calculate Margin Metrics',
        'margin.overview_heading': '📊 Margin Account Overview',
        'margin.warning_title': 'MARGIN CALL WARNING',
        'margin.warning_message': 'Your margin ratio is below the required level. You may receive a margin call from your broker.',
        'margin.healthy_title': 'MARGIN ACCOUNT HEALTHY',
        'margin.healthy_message': 'Your margin ratio is above the required level. Your account is in good standing.',

        // Pattern Recognition
        'patterns.info': 'Automatic detection of chart patterns and candlestick formations.',
        'patterns.detect_button': 'Detect Patterns',
        'patterns.detected_heading': 'Detected Patterns',

        // Machine Learning
        'ml.info': 'Advanced LSTM neural network predictions with confidence intervals.',
        'ml.generate_button': 'Generate ML Forecast',
        'ml.feature_importance': 'Feature Importance',
        'ml.forecast_horizon': 'Forecast Horizon:',
        'ml.7_days': '7 Days',
        'ml.14_days': '14 Days',
        'ml.30_days': '30 Days',
        'ml.60_days': '60 Days',

        // Correlation
        'correlation.info': 'Analyze correlations between stocks for diversification and pair trading.',
        'correlation.analyze_button': 'Analyze Correlations',
        'correlation.select_min_3': 'Select Stocks (min 3)',
        'correlation.matrix_heading': 'Correlation Matrix',
        'correlation.heatmap_heading': 'Correlation Heatmap',
        'correlation.pair_trading_heading': 'Pair Trading Opportunities',
        'correlation.highly_correlated': 'Highly Correlated',
        'correlation.negatively_correlated': 'Negatively Correlated',

        // Actions & Buttons
        'action.add_stock': 'Add Stock Holding',
        'action.clear_all': 'Clear All',
        'action.select_stock': 'Select Stock...',

        // Tips & Help
        'tip.add_holdings': 'Tip: Add all stocks you currently own. We\'ll calculate their current value and provide personalized recommendations.',
        'tip.preferred_stocks': 'Select stocks you want to prioritize in your portfolio. The system will include these first, then recommend additional stocks to optimize your allocation.',
        'tip.how_it_works': 'How it works: Selected preferred stocks will be included first (with at least 10% allocation each). The system will then optimize the remaining budget across other suitable stocks.',
        'tip.ai_recommendations': 'Let AI analyze all stocks and recommend the best options based on real market data, returns, and risk metrics.',
        'tip.strategy_checkbox': 'How it works: Select a strategy checkbox above. AI will analyze all stocks using real market data and automatically select the top performers for you. Results appear in "Preferred Stocks" section above.',
        'help.enter_holdings': 'Enter your existing stock holdings. We\'ll analyze them and suggest what to do with each stock (HOLD, BUY MORE, or SELL) plus recommend new additions.',
        'help.search_preferred': 'Search preferred stocks...',
        'help.recommendations_applied': 'Recommendations Applied',

        // Status Messages
        'status.loading_stocks': 'Loading stocks...',
        'status.no_data': 'Not enough data available for selected stocks. Please try different stocks.',

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
        'button.cancel': 'Cancel',
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
        'footer.api_docs': 'API Documentation',
        'footer.documentation': 'Documentation',

        // Additional Menu
        'menu.dashboards_button': '📊 Dashboards ▼',
        'home.brand_name': '📊 VNStock Analytics',

        // Tooltips and Tips
        'tooltip.api_offline': 'API server may not be running. Click to open monitor.',
        'tooltip.view_advanced_charts': 'View Advanced Charts for',
        'tip.add_all_stocks': 'Tip: Add all stocks you own. We\'ll suggest HOLD, BUY MORE, or SELL.',
        'tip.note_existing_allocation': 'Note: These are recommendations for allocating your additional cash flow. You can use this to buy more of existing holdings or add new positions.',
        'tip.note_new_allocation': 'Note: This is your recommended portfolio allocation for the specified budget.',
        'status.api_offline': 'API Offline',

        // Home descriptions
        'home.tools_description': 'Comprehensive suite of professional-grade analytics and trading tools',
        'home.dashboard_description': 'Real-time market monitoring with live data updates',
        'home.history_description': 'Track price movements, volume changes, and market trends',
        'home.forecast_description_1': 'Machine learning predictions using 7 models',
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
        'home.coverage_description': '1,553+ Vietnamese stocks and commodities with real-time data and historical analysis',
        'home.ai_description': 'Machine learning forecasts, anomaly detection, and automated investment recommendations',
        'home.professional_tools': 'Professional Tools',
        'home.tools_full_description': 'Charts, technical indicators, and risk analysis tools',

        // Tags
        'tag.realtime': 'Real-time',
        'tag.livedata': 'Live Data',
        'tag.ai_powered': 'AI Powered',
        'tag.four_models': '7 Models',
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

        // Tab Labels
        'advanced.tab.margin': '💳 Margin Management',
        'advanced.tab.patterns': 'Pattern Recognition',
        'advanced.tab.ml': '🧠 Machine Learning',
        'advanced.tab.correlation': 'Correlation Analysis',

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
        'settings.chart_update_interval': 'Chart Update Interval',
        'settings.api_timeout': 'API Timeout (ms)',
        'settings.cache_expiry': 'Cache Expiry (minutes)',
        'settings.auto_refresh': 'Enable automatic data refresh',
        'settings.api_base_url': 'API Base URL',
        'settings.enable_cache': 'Enable data caching',
        'settings.chart_theme': 'Chart Theme',
        'settings.default_chart_type': 'Default Chart Type',
        'settings.show_grid': 'Show grid lines on charts',
        'settings.animate_charts': 'Animate chart transitions',
        'settings.decimal_places': 'Price Decimal Places',
        'settings.enable_price_alerts': 'Enable price alerts',
        'settings.enable_sound': 'Enable sound notifications',
        'settings.enable_browser_notif': 'Enable browser notifications',
        'settings.alert_threshold': 'Price Change Alert Threshold (%)',
        'settings.volume_multiplier': 'Volume Alert Multiplier',
        'settings.trading_strategy': 'Default Strategy',
        'settings.stop_loss': 'Default Stop Loss (%)',
        'settings.take_profit': 'Default Take Profit (%)',
        'settings.enable_auto_trading': 'Enable automated trading (USE WITH CAUTION)',

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
        'home.dashboard_desc': 'Real-time monitoring of 1,553+ Vietnamese stocks with live updates, interactive visualization, technical scores, and comprehensive performance tracking.',
        'home.history_desc': 'Deep dive into price history with moving averages, RSI, MACD, and volume analysis. Multiple timeframes from 30 days to 1 year.',
        'home.forecast_desc': 'Machine learning predictions using 7 models. Statistical control charts with anomaly detection and investment recommendations.',
        'home.advanced_desc': 'Portfolio optimization, strategy backtesting, risk management with VaR/CVaR, ML forecasting, and pattern recognition.',
        'home.charts_desc': 'Institutional-grade charting with Ichimoku Cloud, Volume Profile, Stochastic, Fibonacci, Pivot Points, and more.',
        'home.macro_desc': 'Track global factors: oil prices, interest rates, geopolitical risks, policy changes, and their impact on Vietnamese stocks.',
        'home.alerts_desc': 'Real-time monitoring with customizable alerts. Get notified when stocks hit target prices, RSI levels, or volume spikes.',
        'home.automation_desc': 'Automated execution of trading strategies based on technical signals. Set custom rules for entry, exit, stop-loss, and position sizing.',

        // Feature text
        'home.coverage_text': '1,553+ Vietnamese stocks and commodities with real-time data and historical analysis.',
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

        // Resources Section
        'resources.subtitle': 'Everything you need to master the platform',
        'resources.quick_start_desc': 'Get up and running in minutes. Learn the basics and start analyzing stocks right away.',
        'resources.read_guide': 'Read Guide →',
        'resources.user_guide_desc': 'Master advanced features, technical indicators, and portfolio optimization strategies.',
        'resources.explore_guide': 'Explore Guide →',
        'resources.features_desc': 'Complete reference of all features, tools, and capabilities of the platform.',
        'resources.view_features': 'View Features →',
        'resources.api_desc': 'Integrate with our API, automate workflows, and build custom applications.',
        'resources.view_api': 'View API Docs →',
        'resources.macro_desc': 'Understand economic indicators and how they impact your investment decisions.',
        'resources.read_macro': 'Read Macro Guide →',
        'resources.api_readme': 'API Quick Reference',
        'resources.api_readme_desc': 'Quick reference for API endpoints, authentication, and common use cases.',
        'resources.view_readme': 'View Reference →',
        'resources.api_docs': 'API Documentation',

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
        'macro.alert.interest_rate_increase': 'Interest Rate Increase Alert',
        'macro.alert.rising_rates_negative': 'Rising interest rates negative for real estate.',

        // Macro - Navigation & Menu
        'macro.menu.price_forecasting': 'Price Forecasting',
        'macro.menu.price_alerts': 'Price Alerts',
        'macro.menu.api_docs': 'API Documentation',
        'macro.menu.quick_start': 'Quick Start',

        // Macro - Table Headers
        'macro.table.commodity': 'Commodity',
        'macro.table.current_price': 'Current Price',
        'macro.table.change': 'Change',
        'macro.table.impact_level': 'Impact Level',
        'macro.table.affected_sectors': 'Affected Sectors',
        'macro.table.sector': 'Sector',

        // Macro - Chart Titles
        'macro.chart.geopolitical_tensions': 'Regional Geopolitical Tensions - Risk Assessment',
        'macro.chart.policy_timeline': 'Policy & Regulatory Impact Timeline',
        'macro.chart.oil_vnindex': 'Oil Price vs VN-Index Correlation',
        'macro.chart.correlation_analysis': 'Factor-Sector Correlation Analysis',

        // Macro - Chart Labels
        'macro.chart.risk_probability': 'Risk Probability (%)',
        'macro.chart.market_impact': 'Market Impact Score (0-100)',
        'macro.chart.score_probability': 'Score / Probability (%)',
        'macro.chart.geopolitical_events': 'Geopolitical Events',
        'macro.chart.impact_score': 'Impact Score (0-100)',
        'macro.chart.oil_price': 'Oil Price ($)',
        'macro.chart.oil_price_barrel': 'Oil Price ($/barrel)',
        'macro.chart.vnindex': 'VN-Index',
        'macro.chart.correlation_coefficient': 'Correlation Coefficient',

        // Macro - Subheaders
        'macro.subheader.sector_impact': 'Sector Impact Analysis',
        'macro.subheader.regional_tensions': 'Regional Tensions Impact',
        'macro.subheader.policy_timeline': 'Policy Impact Timeline',

        // Macro - Environmental Factors
        'macro.factor.oil_prices': 'Global Oil Prices',
        'macro.factor.oil_desc': 'Rising oil prices increase costs for transportation, manufacturing, and utilities',
        'macro.factor.interest_rates': 'Interest Rates',
        'macro.factor.interest_desc': 'Higher interest rates increase borrowing costs, affecting real estate and banking',
        'macro.factor.exchange_rate': 'USD/VND Exchange Rate',
        'macro.factor.exchange_desc': 'Weaker VND benefits exporters but increases import costs',
        'macro.factor.china_growth': 'China Economic Growth',
        'macro.factor.china_desc': 'China slowdown affects Vietnam exports and manufacturing',
        'macro.factor.us_fed': 'US Federal Reserve Policy',
        'macro.factor.us_fed_value': 'Hawkish',
        'macro.factor.us_fed_trend': 'Tightening',
        'macro.factor.us_fed_desc': 'Fed tightening reduces foreign investment in emerging markets',
        'macro.factor.vn_inflation': 'Vietnam Inflation',
        'macro.factor.vn_inflation_desc': 'Moderate inflation affects purchasing power and consumer spending',
        'macro.factor.tech_war': 'US-China Tech War',
        'macro.factor.tech_war_value': 'High Tension',
        'macro.factor.tech_war_trend': 'Escalating',
        'macro.factor.tech_war_desc': 'Tech war creates opportunities for Vietnam manufacturing shift',
        'macro.factor.supply_chain': 'Global Supply Chain',
        'macro.factor.supply_chain_value': 'Improving',
        'macro.factor.supply_chain_trend': 'Normalizing',
        'macro.factor.supply_chain_desc': 'Supply chain recovery improves manufacturing and exports',

        // Macro - Geopolitical Risks
        'macro.geo.south_china_sea': 'South China Sea Tensions',
        'macro.geo.south_china_sea_desc': 'Ongoing territorial disputes could affect regional trade and investment',
        'macro.geo.russia_ukraine': 'Russia-Ukraine Conflict',
        'macro.geo.russia_ukraine_desc': 'War drives up energy and food prices globally',
        'macro.geo.middle_east': 'Middle East Instability',
        'macro.geo.middle_east_desc': 'Regional conflicts threaten oil supply and prices',
        'macro.geo.us_china': 'US-China Trade Relations',
        'macro.geo.us_china_desc': 'Improving relations as manufacturing shifts to Vietnam',

        // Macro - Sectors
        'macro.sector.defense': 'Defense',
        'macro.sector.maritime': 'Maritime',
        'macro.sector.tourism': 'Tourism',
        'macro.sector.energy': 'Energy',
        'macro.sector.agriculture': 'Agriculture',
        'macro.sector.commodities': 'Commodities',
        'macro.sector.oil_gas': 'Oil & Gas',
        'macro.sector.transportation': 'Transportation',
        'macro.sector.technology': 'Technology',
        'macro.sector.manufacturing': 'Manufacturing',
        'macro.sector.exports': 'Exports',
        'macro.sector.industrial': 'Industrial',
        'macro.sector.ecommerce': 'E-commerce',
        'macro.sector.fintech': 'Fintech',
        'macro.sector.utilities': 'Utilities',
        'macro.sector.banking': 'Banking',
        'macro.sector.construction': 'Construction',

        // Macro - Policy Changes
        'macro.policy.digital_tax': 'Digital Economy Tax Framework',
        'macro.policy.digital_tax_desc': 'New framework supports digital businesses with tax incentives for AI and tech innovation',
        'macro.policy.green_bonds': 'Green Bond Market Development',
        'macro.policy.green_bonds_desc': 'Government launches green bond program to fund renewable energy transition',
        'macro.policy.infrastructure': 'Infrastructure Investment Acceleration',
        'macro.policy.infrastructure_desc': 'Major infrastructure spending increase for high-speed rail and ports',
        'macro.policy.fdi_incentives': 'Foreign Investment Incentives',
        'macro.policy.fdi_incentives_desc': 'Enhanced incentives for FDI in high-tech manufacturing and semiconductors',
        'macro.policy.type_fiscal': 'Fiscal',
        'macro.policy.type_environmental': 'Environmental',
        'macro.policy.type_regulatory': 'Regulatory',

        // Macro - Commodities
        'macro.commodity.crude_oil': 'Crude Oil',
        'macro.commodity.gold': 'Gold',
        'macro.commodity.steel': 'Steel',
        'macro.commodity.natural_gas': 'Natural Gas',
        'macro.commodity.impact_oil': 'Oil & Gas (+), Airlines (-), Logistics (-)',
        'macro.commodity.impact_gold': 'Commodities (+), Safe Haven Demand',
        'macro.commodity.impact_steel': 'Steel (+), Construction (+)',
        'macro.commodity.impact_gas': 'Utilities (-), Fertilizer (-)',

        // Macro - Messages
        'macro.loading_news': 'Loading latest financial news...',
        'macro.news_load_error': 'Unable to load news. Please check your connection and try again.',

        // Common terms
        'common.sell': 'SELL',
        'common.buy': 'BUY',
        'common.affected': 'Affected',
        'common.error': 'Error',
        'common.none': 'None',
        'common.loading': 'Loading...',

        // Risk Metrics - CRITICAL FINANCIAL TERMS
        'risk.var_95': 'Value at Risk (95%)',
        'risk.cvar_95': 'CVaR (95%)',
        'risk.avg_beta': 'Average Beta',
        'risk.volatility': 'Volatility',
        'risk.breakdown': 'Risk Breakdown by Stock',
        'risk.description': 'Advanced risk metrics to help you understand and manage investment risk.',
        'risk.select_stocks': 'Select Stocks',

        // Portfolio Metrics - CRITICAL
        'portfolio.expected_return': 'Expected Return',
        'portfolio.portfolio_risk': 'Portfolio Risk (σ)',
        'portfolio.sharpe_ratio': 'Sharpe Ratio',
        'portfolio.max_drawdown': 'Max Drawdown',
        'portfolio.diversification': 'Diversification',
        'portfolio.total_value': 'Total Value',
        'portfolio.recommended_holdings': 'Recommended Holdings',
        'portfolio.investment_summary': 'Investment Summary',
        'portfolio.description': 'Build and analyze your portfolio with advanced metrics including Sharpe ratio, maximum drawdown, and asset allocation optimization.',
        'portfolio.select_stocks_label': 'Select Stocks for Portfolio',

        // Portfolio Type
        'portfolio.type_label': 'Select Portfolio Type',
        'portfolio.existing': 'Existing Portfolio',
        'portfolio.existing_desc': 'Already own stocks? Track and optimize your current holdings',
        'portfolio.new': 'New Portfolio',
        'portfolio.new_desc': 'Starting fresh? Build an optimized portfolio from scratch',

        // Backtesting
        'backtest.description': 'Test your trading strategies on historical data. See how your strategy would have performed.',
        'backtest.select_stock': 'Select Stock',
        'backtest.strategy': 'Strategy',
        'backtest.sma_crossover': 'SMA Crossover (20/50)',
        'backtest.rsi': 'RSI Oversold/Overbought',
        'backtest.macd': 'MACD Signal',
        'backtest.bollinger': 'Bollinger Breakout',
        'backtest.run': 'Run Backtest',
        'backtest.total_return': 'Total Return',
        'backtest.win_rate': 'Win Rate',
        'backtest.total_trades': 'Total Trades',
        'backtest.avg_trade': 'Avg Trade P/L',
        'backtest.trade_history': 'Trade History',

        // Alert System - CRITICAL
        'alerts.stock_symbol_label': 'Stock Symbol',
        'alerts.loading_stocks': '-- Loading stocks --',
        'alerts.alert_type_label': 'Alert Type',
        'alerts.type_price_above': 'Price Above',
        'alerts.type_price_below': 'Price Below',
        'alerts.type_change_above': 'Change % Above',
        'alerts.type_change_below': 'Change % Below',
        'alerts.type_volume_spike': 'Volume Spike',
        'alerts.type_rsi_oversold': 'RSI Oversold (<30)',
        'alerts.type_rsi_overbought': 'RSI Overbought (>70)',
        'alerts.target_value_label': 'Target Value',
        'alerts.enter_value': 'Enter value',
        'alerts.create_alert': 'Create Alert',
        'alerts.active_title': 'Active Alerts',
        'alerts.no_active': 'No active alerts. Create one above to start monitoring.',
        'alerts.triggered_title': 'Recently Triggered Alerts',
        'alerts.no_triggered': 'No triggered alerts yet.',
        'alerts.error_fill_fields': 'Please fill all fields',
        'alerts.subtitle': 'Real-Time Price Monitoring & Notifications',
        'alerts.triggered_today': 'Triggered Today',
        'alerts.stocks_monitored': 'Stocks Monitored',

        // Macro Analysis - Risk Warnings
        'macro.risk_high': 'HIGH RISK',
        'macro.risk_medium': 'MEDIUM RISK',
        'macro.risk_low': 'LOW RISK',
        'macro.risk_probability': 'Risk Probability (%)',
        'macro.market_impact': 'Market Impact Score (0-100)',
        'macro.interest_rate_alert': '🚨 Interest Rate Increase Alert',
        'macro.interest_rate_text': 'Rising interest rates negative for real estate.',
        'macro.consider_reduce': 'Consider: Reduce exposure to',
        'macro.consider_increase': 'Increase',
        'macro.news_demo_notice': 'These are sample news items for demonstration. Links redirect to VnExpress business news section for latest market updates.',

        // Trading Automation
        'automation.connection_success': '✅ Connection successful! API server is responding correctly.',
        'automation.rule_added': '✅ Rule added! Rule will be active when trading is enabled.',
        'automation.confirm_delete': '🗑️ Delete this rule?\n\nThis action cannot be undone.',

        // System Messages
        'system.api_offline': 'API server may not be running. Click to open monitor.',
        'system.collection_success': '✅ Stock collection job triggered! Check the logs above for progress.',
        'system.collection_error': '❌ Error triggering job. Make sure: 1. API server is running on port 5000, 2. Check the terminal for errors',
        'system.macro_success': '✅ Macro collection job triggered! Check the logs above for progress.',

        // Monitor Page
        'monitor.title': 'System Monitor & Settings',
        'monitor.subtitle': 'Real-time monitoring and configuration for Vietnamese Stock Analytics',
        'monitor.live': 'Live',
        'monitor.api_server': 'API Server',
        'monitor.database': 'Database',
        'monitor.scheduler': 'Scheduler',
        'monitor.data_collection': 'Data Collection',
        'monitor.active_sessions': 'Active Sessions',
        'monitor.session_stats': 'Session Stats',
        'monitor.active_users': 'Active Users & Connections',
        'monitor.user_activity': 'User Activity & Behavior',
        'monitor.collection_settings': 'Collection Settings',
        'monitor.loading_settings': 'Loading settings...',
        'monitor.quick_actions': 'Quick Actions',
        'monitor.recent_activity': 'Recent Activity',
        'monitor.auto_refresh': 'Auto-refresh every 10s',
        'monitor.collect_stock': '📈 Collect Stock Data Now',
        'monitor.collect_macro': '🌍 Collect Macro Data Now',
        'monitor.view_schedule': '📅 View Schedule',
        'monitor.view_logs': '📋 View Logs',
        'monitor.edit_settings': '🔧 Edit Settings',
        'monitor.restart_scheduler': '🔄 Restart Scheduler',
        'monitor.status': 'Status',
        'monitor.message': 'Message',
        'monitor.connection': 'Connection',
        'monitor.process_id': 'Process ID',
        'monitor.endpoint': 'Endpoint',
        'monitor.active_stocks': 'Active Stocks',
        'monitor.last_stock_update': 'Last Stock Update',
        'monitor.last_index_update': 'Last Index Update',
        'monitor.last_macro_update': 'Last Macro Update',
        'monitor.todays_updates': 'Today\'s Updates',
        'monitor.session_id': 'Session ID',
        'monitor.current_page': 'Current Page',
        'monitor.page_views': 'Page Views',
        'monitor.duration': 'Duration',
        'monitor.last_seen': 'Last Seen',
        'monitor.ip_address': 'IP Address',
        'monitor.no_active_sessions': 'No active sessions',
        'monitor.no_activity': 'No activity yet',
        'monitor.top_pages': 'Top Pages',
        'monitor.total_page_views': 'Total Page Views',
        'monitor.avg_per_session': 'Avg per Session',

        // Real-Time Dashboard
        'realtime.title': '📊 Vietnamese Stock Monitor',
        'realtime.subtitle': 'Real-time Technical Analysis Dashboard',
        'realtime.live': 'LIVE',
        'realtime.enhanced_dashboard': '🎯 Enhanced Dashboard',
        'realtime.auto_trading': '🤖 Auto Trading',
        'realtime.demo_mode': '🎮 DEMO MODE',
        'realtime.connecting': 'Connecting to server...',
        'realtime.top_recommendations': '📈 Top Recommendations',
        'realtime.score_distribution': '📊 Score Distribution',
        'realtime.technical_indicators': '🎯 Technical Indicators',
        'realtime.budget_allocation': '💰 Budget Allocation (10M VND)',
        'realtime.rsi_overview': '📉 RSI Overview',
        'realtime.market_signals': '⚡ Market Signals',
        'realtime.waiting_data': 'Waiting for data...',
        'realtime.loading_indicators': 'Loading indicators...',
        'realtime.calculating_allocation': 'Calculating allocation...',
        'realtime.analyzing_signals': 'Analyzing signals...',

        // Form Labels - General
        'form.loading': '-- Loading --',
        'form.search_placeholder': '🔍 Search stocks...',

        // Diversification Risk
        'diversification.concentration_risk': '⚠️ Concentration Risk',
        'diversification.well_diversified': '✅ Well Diversified',
        'diversification.moderate': 'ℹ️ Moderate Diversification',

        // Advanced Features - Tabs
        'advanced.tab.margin': 'Margin Management',
        'advanced.tab.patterns': 'Pattern Recognition',
        'advanced.tab.ml': '🧠 Machine Learning',
        'advanced.tab.correlation': 'Correlation Analysis',
        'advanced.tab.report': 'Portfolio Report',

        // Report Section
        'report.title': 'Portfolio Report',
        'report.info': 'Generate comprehensive portfolio analysis reports with key metrics, performance charts, and recommendations.',
        'report.settings_title': 'Report Settings',
        'report.options_title': 'Report Options',
        'report.report_type': 'Report Type',
        'report.type_summary': 'Summary Report',
        'report.type_detailed': 'Detailed Analysis',
        'report.type_performance': 'Performance Report',
        'report.type_risk': 'Risk Assessment',
        'report.time_period': 'Time Period',
        'report.period_1m': 'Last 1 Month',
        'report.period_3m': 'Last 3 Months',
        'report.period_6m': 'Last 6 Months',
        'report.period_1y': 'Last 1 Year',
        'report.period_ytd': 'Year to Date',
        'report.format': 'Export Format',
        'report.format_pdf': 'PDF Document',
        'report.format_html': 'HTML Page',
        'report.format_excel': 'Excel Spreadsheet',
        'report.include_charts': 'Include Charts & Visualizations',
        'report.include_recommendations': 'Include AI Recommendations',
        'report.generate_button': 'Generate Report',
        'report.preview_title': 'Report Preview',
        'report.download_button': 'Download Report',

        // Margin Management
        'margin.title': 'Margin Management',
        'margin.intro': 'Track and manage your margin account, monitor buying power, calculate margin requirements, and receive margin call warnings.',
        'margin.account_setup': 'Margin Account Setup',
        'margin.cash_equity': 'Total Cash Equity',
        'margin.cash_equity_hint': 'Your own cash invested',
        'margin.borrowed_amount': 'Borrowed Amount',
        'margin.borrowed_amount_hint': 'Funds borrowed from broker',
        'margin.margin_ratio': 'Margin Ratio (%)',
        'margin.margin_ratio_hint': 'Required equity percentage (typically 50%)',
        'margin.interest_rate': 'Annual Interest Rate (%)',
        'margin.interest_rate_hint': 'Annual borrowing cost',
        'margin.calculate': 'Calculate Margin Metrics',
        'margin.overview': 'Margin Account Overview',
        'margin.total_value': 'Total Portfolio Value',
        'margin.total_value_hint': 'Cash + Borrowed',
        'margin.buying_power': 'Available Buying Power',
        'margin.buying_power_hint': 'Can invest up to',
        'margin.current_ratio': 'Current Margin Ratio',
        'margin.current_ratio_hint': 'Equity / Total Value',
        'margin.daily_interest': 'Daily Interest Cost',
        'margin.daily_interest_hint': 'Per day borrowing cost',
        'margin.warning_title': 'MARGIN CALL WARNING',
        'margin.warning_text': 'Your margin ratio is below the required level. You may receive a margin call from your broker.',
        'margin.warning_details': 'Required Action',
        'margin.warning_add': 'Add',
        'margin.warning_or': 'OR',
        'margin.warning_sell': 'Sell',
        'margin.healthy_title': 'MARGIN ACCOUNT HEALTHY',
        'margin.healthy_text': 'Your margin ratio is above the required level. Your account is in good standing.',
        'margin.healthy_buffer': 'You have a',
        'margin.healthy_buffer2': 'buffer above the required margin.',
        'margin.healthy_max_loss': 'Your portfolio can decrease by up to',
        'margin.healthy_max_loss2': 'before triggering a margin call.',
        'margin.interest_analysis': 'Interest Cost Analysis',
        'margin.daily_cost': 'Daily Cost',
        'margin.weekly_cost': 'Weekly Cost',
        'margin.monthly_cost': 'Monthly Cost',
        'margin.yearly_cost': 'Yearly Cost',
        'margin.position_requirements': 'Position & Requirements',
        'margin.initial_margin': 'Initial Margin Required',
        'margin.initial_margin_hint': 'Minimum to open position',
        'margin.maintenance_margin': 'Maintenance Margin',
        'margin.maintenance_margin_hint': 'Must maintain above this',
        'margin.excess_margin': 'Excess Margin',
        'margin.excess_margin_hint': 'Safety buffer available',
        'margin.leverage_analysis': 'Leverage Analysis',
        'margin.current_leverage': 'Current Leverage',
        'margin.leverage_conservative': 'Conservative',
        'margin.leverage_moderate': 'Moderate',
        'margin.leverage_aggressive': 'Aggressive',
        'margin.max_leverage': 'Maximum Leverage',
        'margin.max_leverage_hint': 'Based on margin ratio',
        'margin.risk_level': 'Risk Level',
        'margin.risk_level_hint': 'Based on current leverage',
        'margin.risk_low': 'Low',
        'margin.risk_medium': 'Medium',
        'margin.risk_moderate': 'Moderate',
        'margin.risk_high': 'High',
        'margin.risk_very_high': 'Very High',
        'margin.education_title': 'Understanding Margin Trading',
        'margin.education_intro': 'Margin trading allows you to borrow money from your broker to purchase more stocks than you could with just your cash.',
        'margin.education_buying_power': 'Buying Power: Total amount you can invest (your cash + borrowed funds)',
        'margin.education_margin_ratio': 'Margin Ratio: Percentage of equity required (typically 50% - you can borrow up to 50% of purchase)',
        'margin.education_margin_call': 'Margin Call: When equity falls below maintenance requirement, broker may force you to add funds or sell positions',
        'margin.education_interest': 'Interest: You pay daily interest on borrowed amounts',
        'margin.education_leverage': 'Leverage: Amplifies both gains and losses - use cautiously!',
        'margin.education_warning': '⚠️ Warning: Margin trading involves significant risk. You can lose more than your initial investment.',

        // Pattern Recognition
        'pattern.title': 'Pattern Recognition',
        'pattern.intro': 'Automatic detection of chart patterns and candlestick formations.',
        'pattern.select_stock': 'Select Stock',
        'pattern.detect': 'Detect Patterns',
        'pattern.detected': 'Detected Patterns',
        'pattern.bullish': 'Bullish',
        'pattern.bearish': 'Bearish',
        'pattern.confidence': 'Confidence',

        // Machine Learning
        'ml.title': 'Machine Learning Forecasting',
        'ml.intro': 'Advanced LSTM neural network predictions with confidence intervals.',
        'ml.select_stock': 'Select Stock',
        'ml.forecast_horizon': 'Forecast Horizon',
        'ml.run_forecast': 'Run Forecast',
        'ml.accuracy': 'Model Accuracy',
        'ml.trend': 'Predicted Trend',
        'ml.confidence': 'Confidence',
        'ml.upward': 'Upward',
        'ml.downward': 'Downward',
        'ml.sideways': 'Sideways',
        'ml.feature_importance': 'Feature Importance',

        // Correlation Analysis
        'correlation.title': 'Correlation Analysis',
        'correlation.intro': 'Analyze relationships between stocks and identify pair trading opportunities.',
        'correlation.heatmap': 'Correlation Heatmap',
        'correlation.matrix': 'Correlation Matrix',
        'correlation.pair_trading': 'Pair Trading Opportunities',
        'correlation.highly_correlated': 'Highly Correlated',
        'correlation.negatively_correlated': 'Negatively Correlated',

        // Tips and Help Text
        'tip.existing_portfolio': 'Add all stocks you currently own. We\'ll calculate their current value and provide personalized recommendations.',
        'tip.preferred_stocks': 'Selected preferred stocks will be included first (with at least 10% allocation each). The system will then optimize the remaining budget across other suitable stocks.',
        'tip.smart_recommendations': 'Select a strategy checkbox above to get AI-powered stock recommendations based on real market data.',

        // Form Labels
        'form.select_stocks': 'Select Stocks for Portfolio',
        'form.select_stock': 'Select Stock',
        'form.strategy': 'Strategy',
        'form.enter_budget': 'Enter Your Investment Budget (VND)',
        'form.search_stocks': 'Search stocks...',
        'form.placeholder_budget': 'e.g., 100000000',

        // Menus
        'menu.dashboards': 'Dashboards',
        'menu.all_dashboards': 'All Dashboards',
        'menu.market_analysis': 'Market Analysis',
        'menu.investment_tools': 'Investment Tools',
        'menu.automation_alerts': 'Automation & Alerts',
        'menu.price_forecasting': 'Price Forecasting',
        'menu.price_alerts': 'Price Alerts',

        // Alert System
        'alerts.stock_symbol': 'Stock Symbol',
        'alerts.alert_type': 'Alert Type',
        'alerts.target_value': 'Target Value',
        'alerts.enter_value': 'Enter value',
        'alerts.active_alerts': 'Active Alerts'
    },

    vi: {
        // Navigation
        'nav.home': 'Trang Chủ',
        'nav.dashboard': 'Bảng Điều Khiển',
        'nav.history': 'Phân Tích Lịch Sử',
        'nav.charts': 'Biểu Đồ Nâng Cao',
        'nav.forecast': 'Dự Báo Giá',
        'nav.portfolio': 'Danh Mục Đầu Tư',
        'nav.portfolio_analytics': 'Phân Tích Danh Mục',
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
        'dashboard.monitoring_desc': 'Giám sát thời gian thực {count} cổ phiếu Việt Nam với theo dõi hiệu suất',
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
        'table.t_plus': 'T+2 Hợp Lệ',
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
        'table.chart': 'Biểu Đồ',

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
        'portfolio.plan_generator': '📊 Trình Tạo Kế Hoạch Đầu Tư',
        'portfolio.subtitle': 'Phân tích và tối ưu hóa danh mục đầu tư nâng cao',
        'portfolio.analyze_button': '📈 Phân Tích Danh Mục',
        'portfolio.investment_budget': 'Ngân Sách Đầu Tư',
        'portfolio.budget_placeholder': 'Nhập số tiền (ví dụ: 10000000)',
        'portfolio.budget_hint': 'Nhập tổng số tiền bạn muốn đầu tư. Hệ thống sẽ phân bổ nó cho các cổ phiếu đã chọn dựa trên phân bổ tối ưu.',
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
        'portfolio.recommended_actions': 'Hành Động Khuyến Nghị với Dòng Tiền Mới',
        'portfolio.recommended_positions': 'Vị Thế Mới Được Khuyến Nghị',
        'portfolio.save_plan': 'Lưu Kế Hoạch',
        'portfolio.download_report': 'Tải Báo Cáo',
        'portfolio.plan_ready': 'Kế Hoạch Đầu Tư Đã Sẵn Sàng!',
        'portfolio.investment_plan_results': 'Kết Quả Kế Hoạch Đầu Tư',
        'portfolio.saved_plans': 'Kế Hoạch Đã Lưu',
        'portfolio.my_saved_plans': 'Kế Hoạch Đầu Tư Đã Lưu Của Tôi',
        'portfolio.saved_plans_desc': 'Theo dõi và so sánh các kế hoạch đầu tư đã lưu. Xem hiệu suất của chúng theo thời gian với giá thị trường hiện tại.',
        'portfolio.no_saved_plans': 'Chưa có kế hoạch nào được lưu. Tạo và lưu kế hoạch đầu tư để theo dõi hiệu suất!',
        'portfolio.save_investment_plan': 'Lưu Kế Hoạch Đầu Tư',
        'portfolio.plan_name': 'Tên Kế Hoạch',
        'portfolio.plan_notes': 'Ghi Chú (Tùy Chọn)',
        'portfolio.save': 'Lưu',
        'portfolio.view_details': 'Xem Chi Tiết',
        'portfolio.annualized_return': 'Lợi Nhuận Hàng Năm',
        'portfolio.best_performer': 'Tốt Nhất',
        'portfolio.worst_performer': 'Tệ Nhất',
        'portfolio.actual_vs_expected': 'Thực Tế vs Dự Kiến',
        'portfolio.performance_status': 'Trạng Thái Hiệu Suất',
        'portfolio.win_rate': 'Tỷ Lệ Thắng',
        'portfolio.avg_gain': 'LN Trung Bình/CP',
        'portfolio.total_roi': 'Tổng ROI',
        'portfolio.risk_level': 'Mức Độ Rủi Ro',
        'portfolio.holdings_count': 'Số CP',

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
        'charts.momentum': '💪 Chỉ Báo Động Lượng',
        'charts.bollinger_bands': '📊 Dải Bollinger với Giá',
        'charts.atr': '📈 Phạm Vi Dao Động Thực (ATR)',
        'charts.historical_volatility': '📉 Biến Động Lịch Sử',
        'charts.multi_stock_comparison': '📊 So Sánh Hiệu Suất Đa Cổ Phiếu',
        'charts.risk_return_scatter': '🎯 Biểu Đồ Phân Tán Rủi Ro-Lợi Nhuận',
        'charts.returns_distribution': '📊 Phân Phối Lợi Nhuận',
        'charts.cumulative_returns': '📈 Lợi Nhuận Tích Lũy',
        'charts.fibonacci': '🎯 Fibonacci Retracement',
        'charts.pivot_points': '📍 Điểm Pivot',
        'charts.elder_ray': '🌊 Chỉ Số Elder Ray',

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
        'advanced.strategy_backtesting': '⏮️ Kiểm Tra Chiến Lược Ngược',
        'advanced.risk_management': '⚠️ Quản Lý Rủi Ro',
        'advanced.pattern_recognition': '🔍 Nhận Dạng Mẫu',
        'advanced.machine_learning': '🧠 Học Máy',
        'advanced.correlation_analysis': '🔗 Phân Tích Tương Quan',
        'advanced.budget_allocation': 'Phân Bổ Ngân Sách & Kế Hoạch Đầu Tư',

        // Advanced Features - Descriptions
        'advanced.portfolio_desc': 'Chỉ số rủi ro, đa dạng hóa, phân bổ tài sản, tỷ lệ Sharpe, thua lỗ tối đa',
        'advanced.backtesting_desc': 'Kiểm tra chiến lược giao dịch, mô phỏng giao dịch, phân tích hiệu suất',
        'advanced.risk_desc': 'VaR, CVaR, Beta, ma trận tương quan, phân tích biến động',
        'advanced.patterns_desc': 'Mẫu biểu đồ, mẫu nến, hỗ trợ/kháng cự',
        'advanced.ml_desc': 'Dự báo LSTM, mô hình tổng hợp, tầm quan trọng của đặc trưng',
        'advanced.correlation_desc': 'Tương quan cổ phiếu, phân tích ngành, cơ hội giao dịch cặp',

        // Advanced Features - Info Messages
        'advanced.portfolio_info': 'Xây dựng và phân tích danh mục của bạn với các chỉ số nâng cao bao gồm tỷ lệ Sharpe, thua lỗ tối đa và tối ưu hóa phân bổ tài sản.',
        'advanced.backtesting_info': 'Kiểm tra chiến lược giao dịch của bạn trên dữ liệu lịch sử. Xem chiến lược của bạn sẽ hoạt động như thế nào.',
        'advanced.risk_info': 'Các chỉ số rủi ro nâng cao giúp bạn hiểu và quản lý rủi ro đầu tư.',
        'advanced.patterns_info': 'Tự động phát hiện các mẫu biểu đồ và hình nến.',
        'advanced.ml_info': 'Dự đoán mạng nơ-ron LSTM nâng cao với khoảng tin cậy.',
        'advanced.correlation_info': 'Phân tích tương quan giữa các cổ phiếu để đa dạng hóa và giao dịch cặp.',

        // Common Buttons & Actions
        'common.select_stocks': 'Chọn Cổ Phiếu',
        'common.search_stocks': 'Tìm kiếm cổ phiếu...',
        'common.all': 'Tất Cả',
        'common.clear': 'Xóa',
        'common.visible': 'Hiển Thị',
        'common.selected': 'đã chọn',
        'common.analyze': 'Phân Tích',
        'common.calculate': 'Tính Toán',
        'common.generate': 'Tạo',
        'common.run': 'Chạy',
        'common.detect': 'Phát Hiện',
        'common.add': 'Thêm',
        'common.remove': 'Xóa',
        'common.hold': 'GIỮ',
        'common.sell_action': 'BÁN',
        'common.buy_more': 'MUA THÊM',

        // Form Labels & Placeholders
        'form.select_stock': 'Chọn Cổ Phiếu:',
        'form.loading': '-- Đang tải --',
        'form.enter_amount': 'Nhập số tiền',
        'form.placeholder_search': 'Tìm kiếm...',

        // Validation Messages
        'validation.select_min_stocks': 'Vui lòng chọn ít nhất {count} cổ phiếu',
        'validation.select_stock': 'Vui lòng chọn một cổ phiếu',
        'validation.loading_data': 'Đang tải dữ liệu cổ phiếu... Vui lòng đợi một chút và thử lại.',
        'validation.not_enough_data': 'Không đủ dữ liệu cho các cổ phiếu đã chọn. Vui lòng thử các cổ phiếu khác.',

        // Chart Labels
        'chart.asset_allocation': 'Phân Bổ Tài Sản',
        'chart.efficient_frontier': 'Biên Giới Hiệu Quả',
        'chart.current_portfolio': 'Danh Mục Hiện Tại',
        'chart.risk_percent': 'Rủi Ro (%)',
        'chart.expected_return': 'Lợi Nhuận Kỳ Vọng (%)',
        'chart.equity_curve': 'Đường Cong Vốn',
        'chart.buy_hold': 'Mua & Giữ',
        'chart.portfolio_value': 'Giá Trị Danh Mục (VND)',
        'chart.beta_by_stock': 'Beta Theo Cổ Phiếu',
        'chart.feature_importance': 'Tầm Quan Trọng Đặc Trưng Trong Mô Hình ML',
        'chart.lstm_forecast': 'Dự Báo Mạng Nơ-ron LSTM',

        // Table Headers
        'table.stock': 'Cổ Phiếu',
        'table.shares': 'Cổ Phần',
        'table.buy_price': 'Giá Mua',
        'table.current': 'Hiện Tại',
        'table.profit_loss': 'Lãi/Lỗ',
        'table.action': 'Hành Động',
        'table.recommendation': 'Khuyến Nghị',
        'table.allocation': 'Phân Bổ',
        'table.amount': 'Số Tiền (VND)',
        'table.price': 'Giá',
        'table.exp_return': 'Lợi Nhuận Kỳ Vọng',
        'table.risk': 'Rủi Ro',
        'table.date': 'Ngày',
        'table.beta': 'Beta',
        'table.volatility': 'Biến Động',
        'table.var_95': 'VaR (95%)',
        'table.risk_grade': 'Xếp Hạng Rủi Ro',

        // Metric Labels
        'metric.total_return': 'Tổng Lợi Nhuận',
        'metric.win_rate': 'Tỷ Lệ Thắng',
        'metric.total_trades': 'Tổng Số Giao Dịch',
        'metric.avg_trade': 'L/L Trung Bình',
        'metric.model_accuracy': 'Độ Chính Xác Mô Hình',
        'metric.predicted_trend': 'Xu Hướng Dự Đoán',
        'metric.confidence': 'Độ Tin Cậy',

        // Section Headers
        'section.trade_history': 'Lịch Sử Giao Dịch',
        'section.detected_patterns': 'Các Mẫu Đã Phát Hiện',
        'section.feature_importance': 'Tầm Quan Trọng Đặc Trưng',
        'section.correlation_matrix': 'Ma Trận Tương Quan',
        'section.correlation_heatmap': 'Bản Đồ Nhiệt Tương Quan',
        'section.pair_trading': 'Cơ Hội Giao Dịch Cặp',
        'section.allocation_breakdown': 'Phân Tích Phân Bổ',
        'section.investment_rationale': 'Cơ Sở & Bằng Chứng Đầu Tư',
        'section.your_holdings': 'Cổ Phiếu Hiện Tại Của Bạn',
        'section.preferred_stocks': 'Cổ Phiếu Ưu Tiên (Tùy Chọn)',
        'section.smart_recommendations': 'Khuyến Nghị Cổ Phiếu Thông Minh',
        'section.investment_plan': 'Kế Hoạch Đầu Tư Được Khuyến Nghị',
        'section.margin_overview': 'Tổng Quan Tài Khoản Ký Quỹ',
        'section.interest_cost': 'Phân Tích Chi Phí Lãi Suất',
        'section.position_requirements': 'Vị Thế & Yêu Cầu',
        'section.leverage_analysis': 'Phân Tích Đòn Bẩy',
        'section.understanding_margin': 'Hiểu Về Giao Dịch Ký Quỹ',
        'section.business_sector_analysis': '🏢 Phân Tích Doanh Nghiệp & Ngành',
        'section.sector_diversification': '📊 Đa Dạng Hóa Ngành:',
        'section.business_overview': '💼 Tổng Quan Doanh Nghiệp:',

        // Portfolio Type
        'portfolio.select_type': 'Chọn Loại Danh Mục',
        'portfolio.existing_title': 'Danh Mục Hiện Tại',
        'portfolio.existing_desc': 'Đã sở hữu cổ phiếu? Theo dõi và tối ưu hóa danh mục hiện tại của bạn',
        'portfolio.new_title': 'Danh Mục Mới',
        'portfolio.new_desc': 'Bắt đầu từ đầu? Xây dựng danh mục tối ưu từ con số không',

        // Investment Budget
        'budget.enter_amount': 'Nhập Ngân Sách Đầu Tư (VND)',
        'budget.placeholder': 'vd: 100000000',
        'budget.example': 'Ví dụ: 100,000,000 VND (100 triệu)',
        'budget.additional_cash': 'Dòng Tiền Bổ Sung / Đầu Tư Mới (VND)',
        'budget.generate_plan': 'Tạo Kế Hoạch Đầu Tư',

        // Strategy Options
        'strategy.balanced': 'Cân Bằng',
        'strategy.balanced_desc': 'Lợi nhuận điều chỉnh rủi ro tốt nhất',
        'strategy.high_growth': 'Tăng Trưởng Cao',
        'strategy.high_growth_desc': 'Lợi nhuận kỳ vọng tối đa',
        'strategy.conservative': 'Thận Trọng',
        'strategy.conservative_desc': 'Rủi ro thấp nhất, cổ phiếu ổn định',
        'strategy.blue_chip': 'Blue Chip',
        'strategy.blue_chip_desc': 'Chỉ các công ty hàng đầu',
        'strategy.select': 'Chiến Lược:',

        // Backtest
        'backtest.run_button': 'Chạy Kiểm Tra Ngược',
        'backtest.sma_crossover': 'Giao Cắt SMA (20/50)',
        'backtest.rsi_strategy': 'RSI Quá Bán/Quá Mua',
        'backtest.macd_signal': 'Tín Hiệu MACD',
        'backtest.bollinger_breakout': 'Đột Phá Bollinger',

        // Risk Management
        'risk.calculate_button': 'Tính Toán Chỉ Số Rủi Ro',
        'risk.select_stocks': 'Chọn Cổ Phiếu:',

        // Margin Trading
        'margin.title': '💳 Quản Lý Ký Quỹ',
        'margin.intro': 'Theo dõi và quản lý tài khoản ký quỹ, giám sát sức mua, tính toán yêu cầu ký quỹ và nhận cảnh báo gọi margin.',
        'margin.account_setup': '📋 Thiết Lập Tài Khoản Ký Quỹ',
        'margin.cash_equity': '💵 Tổng Vốn Tiền Mặt (₫)',
        'margin.cash_equity_hint': 'Tiền mặt của bạn đã đầu tư',
        'margin.total_cash': 'Tổng Vốn Tiền Mặt (₫)',
        'margin.cash_hint': 'Tiền mặt của bạn đã đầu tư',
        'margin.borrowed_amount': '💰 Số Tiền Vay (₫)',
        'margin.borrowed_amount_hint': 'Số tiền vay từ môi giới',
        'margin.borrowed_hint': 'Số tiền vay từ môi giới',
        'margin.margin_ratio': '📊 Tỷ Lệ Ký Quỹ (%)',
        'margin.margin_ratio_hint': 'Tỷ lệ vốn chủ sở hữu yêu cầu (thường 50%)',
        'margin.ratio_hint': 'Tỷ lệ vốn chủ sở hữu yêu cầu (thường 50%)',
        'margin.interest_rate': '📈 Lãi Suất Hàng Năm (%)',
        'margin.interest_hint': 'Chi phí vay hàng năm',
        'margin.calculate_button': 'Tính Toán Chỉ Số Ký Quỹ',
        'margin.overview_heading': '📊 Tổng Quan Tài Khoản Ký Quỹ',
        'margin.warning_title': 'CẢNH BÁO GỌI MARGIN',
        'margin.warning_message': 'Tỷ lệ ký quỹ của bạn thấp hơn mức yêu cầu. Bạn có thể nhận được cuộc gọi margin từ môi giới.',
        'margin.healthy_title': 'TÀI KHOẢN KÝ QUỸ KHỎE MẠNH',
        'margin.healthy_message': 'Tỷ lệ ký quỹ của bạn cao hơn mức yêu cầu. Tài khoản của bạn ở trạng thái tốt.',

        // Margin Account Overview
        'margin.total_value': 'Tổng Giá Trị Danh Mục',
        'margin.total_value_hint': 'Tiền mặt + Vay',
        'margin.buying_power': 'Sức Mua Khả Dụng',
        'margin.buying_power_hint': 'Có thể đầu tư tới',
        'margin.current_ratio': 'Tỷ Lệ Ký Quỹ Hiện Tại',
        'margin.current_ratio_hint': 'Vốn chủ sở hữu / Tổng giá trị',
        'margin.daily_interest': 'Chi Phí Lãi Hàng Ngày',
        'margin.daily_interest_hint': 'Chi phí vay mỗi ngày',

        // Margin Warning Details
        'margin.warning_details': 'Hành Động Cần Thiết',
        'margin.warning_add': 'Nạp thêm',
        'margin.warning_or': 'HOẶC',
        'margin.warning_sell': 'Bán',
        'margin.healthy_buffer': 'Bạn có',
        'margin.healthy_buffer2': 'dự trữ trên mức ký quỹ yêu cầu.',
        'margin.healthy_max_loss': 'Danh mục của bạn có thể giảm tới',
        'margin.healthy_max_loss2': 'trước khi kích hoạt lệnh gọi ký quỹ.',

        // Interest Cost Analysis
        'margin.interest_analysis': '💸 Phân Tích Chi Phí Lãi',
        'margin.daily_cost': 'Chi Phí Ngày',
        'margin.weekly_cost': 'Chi Phí Tuần',
        'margin.monthly_cost': 'Chi Phí Tháng',
        'margin.yearly_cost': 'Chi Phí Năm',

        // Position & Requirements
        'margin.position_requirements': '📍 Vị Thế & Yêu Cầu',
        'margin.initial_margin': 'Ký Quỹ Ban Đầu Yêu Cầu',
        'margin.initial_margin_hint': 'Tối thiểu để mở vị thế',
        'margin.maintenance_margin': 'Ký Quỹ Duy Trì',
        'margin.maintenance_margin_hint': 'Phải duy trì trên mức này',
        'margin.excess_margin': 'Ký Quỹ Dư Thừa',
        'margin.excess_margin_hint': 'Khoảng đệm an toàn',

        // Leverage Analysis
        'margin.leverage_analysis': '⚡ Phân Tích Đòn Bẩy',
        'margin.current_leverage': 'Đòn Bẩy Hiện Tại',
        'margin.leverage_conservative': 'Thận Trọng',
        'margin.leverage_moderate': 'Vừa Phải',
        'margin.leverage_aggressive': 'Mạo Hiểm',
        'margin.max_leverage': 'Đòn Bẩy Tối Đa',
        'margin.max_leverage_hint': 'Dựa trên tỷ lệ ký quỹ',
        'margin.risk_level': 'Mức Độ Rủi Ro',
        'margin.risk_level_hint': 'Dựa trên đòn bẩy hiện tại',
        'margin.risk_low': 'Thấp',
        'margin.risk_medium': 'Trung Bình',
        'margin.risk_moderate': 'Vừa Phải',
        'margin.risk_high': 'Cao',
        'margin.risk_very_high': 'Rất Cao',

        // Understanding Margin Trading
        'margin.education_title': '💡 Hiểu Về Giao Dịch Ký Quỹ',
        'margin.education_intro': 'Giao dịch ký quỹ cho phép bạn vay tiền từ môi giới để mua nhiều cổ phiếu hơn so với chỉ dùng tiền mặt của bạn.',
        'margin.education_buying_power': 'Sức Mua: Tổng số tiền bạn có thể đầu tư (tiền mặt của bạn + tiền vay)',
        'margin.education_margin_ratio': 'Tỷ Lệ Ký Quỹ: Tỷ lệ vốn chủ sở hữu yêu cầu (thường 50% - bạn có thể vay tới 50% giá trị mua)',
        'margin.education_margin_call': 'Lệnh Gọi Ký Quỹ: Khi vốn chủ sở hữu giảm xuống dưới mức duy trì, môi giới có thể buộc bạn nạp thêm tiền hoặc bán vị thế',
        'margin.education_interest': 'Lãi Suất: Bạn trả lãi hàng ngày trên số tiền vay',
        'margin.education_leverage': 'Đòn Bẩy: Phóng đại cả lãi và lỗ - sử dụng cẩn thận!',
        'margin.education_warning': '⚠️ Cảnh báo: Giao dịch ký quỹ có rủi ro đáng kể. Bạn có thể mất nhiều hơn số tiền đầu tư ban đầu.',

        // Pattern Recognition
        'patterns.info': 'Tự động phát hiện các mẫu biểu đồ và các hình thái nến.',
        'patterns.detect_button': 'Phát Hiện Mẫu',
        'patterns.detected_heading': 'Các Mẫu Đã Phát Hiện',

        // Machine Learning
        'ml.info': 'Dự đoán mạng nơ-ron LSTM nâng cao với khoảng tin cậy.',
        'ml.generate_button': 'Tạo Dự Báo ML',
        'ml.feature_importance': 'Mức Độ Quan Trọng Của Đặc Trưng',
        'ml.forecast_horizon': 'Thời Gian Dự Báo:',
        'ml.7_days': '7 Ngày',
        'ml.14_days': '14 Ngày',
        'ml.30_days': '30 Ngày',
        'ml.60_days': '60 Ngày',

        // Correlation
        'correlation.info': 'Phân tích tương quan giữa các cổ phiếu để đa dạng hóa và giao dịch cặp.',
        'correlation.analyze_button': 'Phân Tích Tương Quan',
        'correlation.select_min_3': 'Chọn Cổ Phiếu (tối thiểu 3)',
        'correlation.matrix_heading': 'Ma Trận Tương Quan',
        'correlation.heatmap_heading': 'Bản Đồ Nhiệt Tương Quan',
        'correlation.pair_trading_heading': 'Cơ Hội Giao Dịch Cặp',
        'correlation.highly_correlated': 'Tương Quan Cao',
        'correlation.negatively_correlated': 'Tương Quan Âm',

        // Actions & Buttons
        'action.add_stock': 'Thêm Cổ Phiếu Nắm Giữ',
        'action.clear_all': 'Xóa Tất Cả',
        'action.select_stock': 'Chọn Cổ Phiếu...',

        // Tips & Help
        'tip.add_holdings': 'Mẹo: Thêm tất cả cổ phiếu bạn hiện đang sở hữu. Chúng tôi sẽ tính giá trị hiện tại và đưa ra khuyến nghị cá nhân hóa.',
        'tip.preferred_stocks': 'Chọn các cổ phiếu bạn muốn ưu tiên trong danh mục. Hệ thống sẽ bao gồm chúng trước, sau đó khuyến nghị các cổ phiếu bổ sung để tối ưu hóa phân bổ.',
        'tip.how_it_works': 'Cách hoạt động: Các cổ phiếu ưu tiên đã chọn sẽ được bao gồm trước (với ít nhất 10% phân bổ mỗi cổ). Sau đó hệ thống sẽ tối ưu hóa ngân sách còn lại trên các cổ phiếu phù hợp khác.',
        'tip.ai_recommendations': 'Để AI phân tích tất cả cổ phiếu và khuyến nghị các lựa chọn tốt nhất dựa trên dữ liệu thị trường thực, lợi nhuận và chỉ số rủi ro.',
        'tip.strategy_checkbox': 'Cách hoạt động: Chọn một chiến lược ở trên. AI sẽ phân tích tất cả cổ phiếu bằng dữ liệu thị trường thực và tự động chọn những cổ phiếu hoạt động tốt nhất. Kết quả xuất hiện trong phần "Cổ Phiếu Ưu Tiên" ở trên.',
        'help.enter_holdings': 'Nhập các cổ phiếu hiện tại của bạn. Chúng tôi sẽ phân tích và gợi ý hành động cho từng cổ phiếu (GIỮ, MUA THÊM, hoặc BÁN) cộng với khuyến nghị bổ sung mới.',
        'help.search_preferred': 'Tìm kiếm cổ phiếu ưu tiên...',
        'help.recommendations_applied': 'Đã Áp Dụng Khuyến Nghị',

        // Status Messages
        'status.loading_stocks': 'Đang tải cổ phiếu...',
        'status.no_data': 'Không đủ dữ liệu cho các cổ phiếu đã chọn. Vui lòng thử các cổ phiếu khác.',

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
        'footer.api_docs': 'Tài Liệu API',
        'footer.documentation': 'Tài Liệu',

        // Additional Menu
        'menu.dashboards_button': '📊 Bảng Điều Khiển ▼',
        'home.brand_name': '📊 Phân Tích VNStock',

        // Tooltips and Tips
        'tooltip.api_offline': 'Máy chủ API có thể không chạy. Nhấp để mở màn hình giám sát.',
        'tooltip.view_advanced_charts': 'Xem Biểu Đồ Nâng Cao cho',
        'tip.add_all_stocks': 'Mẹo: Thêm tất cả cổ phiếu bạn sở hữu. Chúng tôi sẽ gợi ý GIỮ, MUA THÊM hoặc BÁN.',
        'tip.note_existing_allocation': 'Lưu ý: Đây là các khuyến nghị để phân bổ dòng tiền bổ sung của bạn. Bạn có thể sử dụng để mua thêm cổ phiếu hiện có hoặc thêm vị thế mới.',
        'tip.note_new_allocation': 'Lưu ý: Đây là phân bổ danh mục đầu tư được khuyến nghị cho ngân sách đã chỉ định.',
        'status.api_offline': 'API Ngoại Tuyến',

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
        'home.coverage_description': '1.553+ cổ phiếu và hàng hóa Việt Nam với dữ liệu thời gian thực và phân tích lịch sử',
        'home.ai_description': 'Dự báo học máy, phát hiện bất thường và khuyến nghị đầu tư tự động',
        'home.professional_tools': 'Công Cụ Chuyên Nghiệp',
        'home.tools_full_description': 'Biểu đồ, chỉ báo kỹ thuật và công cụ phân tích rủi ro',

        // Tags
        'tag.realtime': 'Thời Gian Thực',
        'tag.livedata': 'Dữ Liệu Trực Tiếp',
        'tag.ai_powered': 'Hỗ Trợ AI',
        'tag.four_models': '7 Mô Hình',
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

        // Tab Labels
        'advanced.tab.margin': '💳 Quản Lý Ký Quỹ',
        'advanced.tab.patterns': 'Nhận Dạng Mẫu',
        'advanced.tab.ml': '🧠 Học Máy',
        'advanced.tab.correlation': 'Phân Tích Tương Quan',

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
        'settings.chart_update_interval': 'Khoảng Cập Nhật Biểu Đồ',
        'settings.api_timeout': 'Thời Gian Chờ API (ms)',
        'settings.cache_expiry': 'Thời Gian Hết Hạn Bộ Nhớ Cache (phút)',
        'settings.auto_refresh': 'Bật tự động làm mới dữ liệu',
        'settings.api_base_url': 'URL Cơ Sở API',
        'settings.enable_cache': 'Bật bộ nhớ đệm dữ liệu',
        'settings.chart_theme': 'Chủ Đề Biểu Đồ',
        'settings.default_chart_type': 'Loại Biểu Đồ Mặc Định',
        'settings.show_grid': 'Hiển thị đường lưới trên biểu đồ',
        'settings.animate_charts': 'Hiệu ứng chuyển đổi biểu đồ',
        'settings.decimal_places': 'Số Chữ Số Thập Phân Giá',
        'settings.enable_price_alerts': 'Bật cảnh báo giá',
        'settings.enable_sound': 'Bật thông báo âm thanh',
        'settings.enable_browser_notif': 'Bật thông báo trình duyệt',
        'settings.alert_threshold': 'Ngưỡng Cảnh Báo Thay Đổi Giá (%)',
        'settings.volume_multiplier': 'Hệ Số Nhân Khối Lượng Cảnh Báo',
        'settings.trading_strategy': 'Chiến Lược Mặc Định',
        'settings.stop_loss': 'Cắt Lỗ Mặc Định (%)',
        'settings.take_profit': 'Chốt Lãi Mặc Định (%)',
        'settings.enable_auto_trading': 'Bật giao dịch tự động (SỬ DỤNG THẬN TRỌNG)',

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
        'home.dashboard_desc': 'Giám sát thời gian thực 1.553+ cổ phiếu Việt Nam với cập nhật trực tiếp, trực quan hóa tương tác, điểm số kỹ thuật và theo dõi hiệu suất toàn diện.',
        'home.history_desc': 'Phân tích sâu lịch sử giá với đường trung bình động, RSI, MACD và phân tích khối lượng. Nhiều khung thời gian từ 30 ngày đến 1 năm.',
        'home.forecast_desc': 'Dự đoán học máy sử dụng 4 mô hình. Biểu đồ kiểm soát thống kê với phát hiện bất thường và khuyến nghị đầu tư.',
        'home.advanced_desc': 'Tối ưu hóa danh mục, kiểm tra chiến lược ngược, quản lý rủi ro với VaR/CVaR, dự báo ML và nhận dạng mẫu.',
        'home.charts_desc': 'Biểu đồ với Ichimoku Cloud, Volume Profile, Stochastic, Fibonacci, Pivot Points và nhiều hơn nữa.',
        'home.macro_desc': 'Theo dõi các yếu tố toàn cầu: giá dầu, lãi suất, rủi ro địa chính trị, thay đổi chính sách và tác động đến cổ phiếu Việt Nam.',
        'home.alerts_desc': 'Giám sát thời gian thực với cảnh báo tùy chỉnh. Nhận thông báo khi cổ phiếu đạt giá mục tiêu, mức RSI hoặc tăng đột biến khối lượng.',
        'home.automation_desc': 'Thực thi tự động các chiến lược giao dịch dựa trên tín hiệu kỹ thuật. Đặt quy tắc tùy chỉnh cho vào lệnh, thoát lệnh, cắt lỗ và kích thước vị thế.',

        // Feature text
        'home.coverage_text': '1.553+ cổ phiếu và hàng hóa Việt Nam với dữ liệu thời gian thực và phân tích lịch sử.',
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

        // Resources Section
        'resources.subtitle': 'Mọi thứ bạn cần để thành thạo nền tảng',
        'resources.quick_start_desc': 'Bắt đầu chỉ trong vài phút. Học các kiến thức cơ bản và bắt đầu phân tích cổ phiếu ngay lập tức.',
        'resources.read_guide': 'Đọc Hướng Dẫn →',
        'resources.user_guide_desc': 'Làm chủ các tính năng nâng cao, chỉ báo kỹ thuật và chiến lược tối ưu hóa danh mục.',
        'resources.explore_guide': 'Khám Phá Hướng Dẫn →',
        'resources.features_desc': 'Tham khảo đầy đủ về tất cả tính năng, công cụ và khả năng của nền tảng.',
        'resources.view_features': 'Xem Tính Năng →',
        'resources.api_desc': 'Tích hợp với API, tự động hóa quy trình làm việc và xây dựng ứng dụng tùy chỉnh.',
        'resources.view_api': 'Xem Tài Liệu API →',
        'resources.macro_desc': 'Hiểu các chỉ số kinh tế và cách chúng ảnh hưởng đến quyết định đầu tư của bạn.',
        'resources.read_macro': 'Đọc Hướng Dẫn Vĩ Mô →',
        'resources.api_readme': 'Tham Khảo Nhanh API',
        'resources.api_readme_desc': 'Tham khảo nhanh cho các endpoint API, xác thực và trường hợp sử dụng phổ biến.',
        'resources.view_readme': 'Xem Tham Khảo →',
        'resources.api_docs': 'Tài Liệu API',

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
        'macro.alert.interest_rate_increase': 'Cảnh Báo Tăng Lãi Suất',
        'macro.alert.rising_rates_negative': 'Lãi suất tăng tiêu cực cho bất động sản.',

        // Macro - Navigation & Menu
        'macro.menu.price_forecasting': 'Dự Báo Giá',
        'macro.menu.price_alerts': 'Cảnh Báo Giá',
        'macro.menu.api_docs': 'Tài Liệu API',
        'macro.menu.quick_start': 'Bắt Đầu Nhanh',

        // Macro - Table Headers
        'macro.table.commodity': 'Hàng Hóa',
        'macro.table.current_price': 'Giá Hiện Tại',
        'macro.table.change': 'Thay Đổi',
        'macro.table.impact_level': 'Mức Độ Ảnh Hưởng',
        'macro.table.affected_sectors': 'Ngành Bị Ảnh Hưởng',
        'macro.table.sector': 'Ngành',

        // Macro - Chart Titles
        'macro.chart.geopolitical_tensions': 'Căng Thẳng Địa Chính Trị Khu Vực - Đánh Giá Rủi Ro',
        'macro.chart.policy_timeline': 'Dòng Thời Gian Ảnh Hưởng Chính Sách & Quy Định',
        'macro.chart.oil_vnindex': 'Tương Quan Giá Dầu so với VN-Index',
        'macro.chart.correlation_analysis': 'Phân Tích Tương Quan Yếu Tố-Ngành',

        // Macro - Chart Labels
        'macro.chart.risk_probability': 'Xác Suất Rủi Ro (%)',
        'macro.chart.market_impact': 'Điểm Ảnh Hưởng Thị Trường (0-100)',
        'macro.chart.score_probability': 'Điểm / Xác Suất (%)',
        'macro.chart.geopolitical_events': 'Sự Kiện Địa Chính Trị',
        'macro.chart.impact_score': 'Điểm Ảnh Hưởng (0-100)',
        'macro.chart.oil_price': 'Giá Dầu ($)',
        'macro.chart.oil_price_barrel': 'Giá Dầu ($/thùng)',
        'macro.chart.vnindex': 'VN-Index',
        'macro.chart.correlation_coefficient': 'Hệ Số Tương Quan',

        // Macro - Subheaders
        'macro.subheader.sector_impact': 'Phân Tích Ảnh Hưởng Ngành',
        'macro.subheader.regional_tensions': 'Ảnh Hưởng Căng Thẳng Khu Vực',
        'macro.subheader.policy_timeline': 'Dòng Thời Gian Ảnh Hưởng Chính Sách',

        // Macro - Environmental Factors
        'macro.factor.oil_prices': 'Giá Dầu Toàn Cầu',
        'macro.factor.oil_desc': 'Giá dầu tăng làm tăng chi phí vận tải, sản xuất và tiện ích',
        'macro.factor.interest_rates': 'Lãi Suất',
        'macro.factor.interest_desc': 'Lãi suất cao hơn tăng chi phí vay, ảnh hưởng đến bất động sản và ngân hàng',
        'macro.factor.exchange_rate': 'Tỷ Giá USD/VND',
        'macro.factor.exchange_desc': 'VND yếu có lợi cho xuất khẩu nhưng tăng chi phí nhập khẩu',
        'macro.factor.china_growth': 'Tăng Trưởng Kinh Tế Trung Quốc',
        'macro.factor.china_desc': 'Trung Quốc chậm lại ảnh hưởng đến xuất khẩu và sản xuất Việt Nam',
        'macro.factor.us_fed': 'Chính Sách Cục Dự Trữ Liên Bang Mỹ',
        'macro.factor.us_fed_value': 'Diều Hâu',
        'macro.factor.us_fed_trend': 'Thắt Chặt',
        'macro.factor.us_fed_desc': 'Fed thắt chặt làm giảm đầu tư nước ngoài vào thị trường mới nổi',
        'macro.factor.vn_inflation': 'Lạm Phát Việt Nam',
        'macro.factor.vn_inflation_desc': 'Lạm phát vừa phải ảnh hưởng đến sức mua và chi tiêu tiêu dùng',
        'macro.factor.tech_war': 'Chiến Tranh Công Nghệ Mỹ-Trung',
        'macro.factor.tech_war_value': 'Căng Thẳng Cao',
        'macro.factor.tech_war_trend': 'Leo Thang',
        'macro.factor.tech_war_desc': 'Chiến tranh công nghệ tạo cơ hội cho sự chuyển dịch sản xuất sang Việt Nam',
        'macro.factor.supply_chain': 'Chuỗi Cung Ứng Toàn Cầu',
        'macro.factor.supply_chain_value': 'Đang Cải Thiện',
        'macro.factor.supply_chain_trend': 'Bình Thường Hóa',
        'macro.factor.supply_chain_desc': 'Phục hồi chuỗi cung ứng cải thiện sản xuất và xuất khẩu',

        // Macro - Geopolitical Risks
        'macro.geo.south_china_sea': 'Căng Thẳng Biển Đông',
        'macro.geo.south_china_sea_desc': 'Tranh chấp lãnh thổ đang diễn ra có thể ảnh hưởng đến thương mại và đầu tư khu vực',
        'macro.geo.russia_ukraine': 'Xung Đột Nga-Ukraine',
        'macro.geo.russia_ukraine_desc': 'Chiến tranh làm tăng giá năng lượng và thực phẩm toàn cầu',
        'macro.geo.middle_east': 'Bất Ổn Trung Đông',
        'macro.geo.middle_east_desc': 'Xung đột khu vực đe dọa nguồn cung và giá dầu',
        'macro.geo.us_china': 'Quan Hệ Thương Mại Mỹ-Trung',
        'macro.geo.us_china_desc': 'Cải thiện quan hệ khi sản xuất chuyển sang Việt Nam',

        // Macro - Sectors
        'macro.sector.defense': 'Quốc Phòng',
        'macro.sector.maritime': 'Hàng Hải',
        'macro.sector.tourism': 'Du Lịch',
        'macro.sector.energy': 'Năng Lượng',
        'macro.sector.agriculture': 'Nông Nghiệp',
        'macro.sector.commodities': 'Hàng Hóa',
        'macro.sector.oil_gas': 'Dầu Khí',
        'macro.sector.transportation': 'Vận Tải',
        'macro.sector.technology': 'Công Nghệ',
        'macro.sector.manufacturing': 'Sản Xuất',
        'macro.sector.exports': 'Xuất Khẩu',
        'macro.sector.industrial': 'Công Nghiệp',
        'macro.sector.ecommerce': 'Thương Mại Điện Tử',
        'macro.sector.fintech': 'Công Nghệ Tài Chính',
        'macro.sector.utilities': 'Tiện Ích',
        'macro.sector.banking': 'Ngân Hàng',
        'macro.sector.construction': 'Xây Dựng',

        // Macro - Policy Changes
        'macro.policy.digital_tax': 'Khung Thuế Kinh Tế Số',
        'macro.policy.digital_tax_desc': 'Khung mới hỗ trợ doanh nghiệp số với ưu đãi thuế cho AI và đổi mới công nghệ',
        'macro.policy.green_bonds': 'Phát Triển Thị Trường Trái Phiếu Xanh',
        'macro.policy.green_bonds_desc': 'Chính phủ khởi động chương trình trái phiếu xanh để tài trợ chuyển đổi năng lượng tái tạo',
        'macro.policy.infrastructure': 'Tăng Tốc Đầu Tư Cơ Sở Hạ Tầng',
        'macro.policy.infrastructure_desc': 'Tăng chi tiêu cơ sở hạ tầng lớn cho đường sắt cao tốc và mở rộng cảng',
        'macro.policy.fdi_incentives': 'Ưu Đãi Đầu Tư Nước Ngoài',
        'macro.policy.fdi_incentives_desc': 'Tăng cường ưu đãi cho FDI trong sản xuất công nghệ cao và bán dẫn',
        'macro.policy.type_fiscal': 'Tài Chính',
        'macro.policy.type_environmental': 'Môi Trường',
        'macro.policy.type_regulatory': 'Quy Định',

        // Macro - Commodities
        'macro.commodity.crude_oil': 'Dầu Thô',
        'macro.commodity.gold': 'Vàng',
        'macro.commodity.steel': 'Thép',
        'macro.commodity.natural_gas': 'Khí Đốt Tự Nhiên',
        'macro.commodity.impact_oil': 'Dầu Khí (+), Hàng Không (-), Logistics (-)',
        'macro.commodity.impact_gold': 'Hàng Hóa (+), Nhu Cầu Trú Ẩn An Toàn',
        'macro.commodity.impact_steel': 'Thép (+), Xây Dựng (+)',
        'macro.commodity.impact_gas': 'Tiện Ích (-), Phân Bón (-)',

        // Macro - Messages
        'macro.loading_news': 'Đang tải tin tức tài chính mới nhất...',
        'macro.news_load_error': 'Không thể tải tin tức. Vui lòng kiểm tra kết nối và thử lại.',

        // Common terms
        'common.sell': 'BÁN',
        'common.buy': 'MUA',
        'common.affected': 'Ảnh Hưởng',
        'common.error': 'Lỗi',
        'common.none': 'Không có',
        'common.loading': 'Đang tải...',

        // Risk Metrics - CRITICAL FINANCIAL TERMS
        'risk.var_95': 'Giá Trị Rủi Ro (95%)',
        'risk.cvar_95': 'CVaR (95%)',
        'risk.avg_beta': 'Beta Trung Bình',
        'risk.volatility': 'Biến Động',
        'risk.breakdown': 'Phân Tích Rủi Ro Theo Cổ Phiếu',
        'risk.description': 'Chỉ số rủi ro nâng cao giúp bạn hiểu và quản lý rủi ro đầu tư.',
        'risk.select_stocks': 'Chọn Cổ Phiếu',

        // Portfolio Metrics - CRITICAL
        'portfolio.expected_return': 'Lợi Nhuận Kỳ Vọng',
        'portfolio.portfolio_risk': 'Rủi Ro Danh Mục (σ)',
        'portfolio.sharpe_ratio': 'Tỷ Lệ Sharpe',
        'portfolio.max_drawdown': 'Thua Lỗ Tối Đa',
        'portfolio.diversification': 'Đa Dạng Hóa',
        'portfolio.total_value': 'Tổng Giá Trị',
        'portfolio.recommended_holdings': 'Danh Mục Đề Xuất',
        'portfolio.investment_summary': 'Tóm Tắt Đầu Tư',
        'portfolio.description': 'Xây dựng và phân tích danh mục của bạn với các chỉ số nâng cao bao gồm tỷ lệ Sharpe, thua lỗ tối đa và tối ưu hóa phân bổ tài sản.',
        'portfolio.select_stocks_label': 'Chọn Cổ Phiếu Cho Danh Mục',

        // Portfolio Type
        'portfolio.type_label': 'Chọn Loại Danh Mục',
        'portfolio.existing': 'Danh Mục Hiện Tại',
        'portfolio.existing_desc': 'Đã sở hữu cổ phiếu? Theo dõi và tối ưu hóa danh mục hiện tại của bạn',
        'portfolio.new': 'Danh Mục Mới',
        'portfolio.new_desc': 'Bắt đầu từ đầu? Xây dựng danh mục tối ưu từ con số không',

        // Backtesting
        'backtest.description': 'Kiểm tra chiến lược giao dịch của bạn trên dữ liệu lịch sử. Xem chiến lược của bạn sẽ hoạt động như thế nào.',
        'backtest.select_stock': 'Chọn Cổ Phiếu',
        'backtest.strategy': 'Chiến Lược',
        'backtest.sma_crossover': 'Giao Cắt SMA (20/50)',
        'backtest.rsi': 'RSI Quá Bán/Quá Mua',
        'backtest.macd': 'Tín Hiệu MACD',
        'backtest.bollinger': 'Đột Phá Bollinger',
        'backtest.run': 'Chạy Kiểm Tra Ngược',
        'backtest.total_return': 'Tổng Lợi Nhuận',
        'backtest.win_rate': 'Tỷ Lệ Thắng',
        'backtest.total_trades': 'Tổng Giao Dịch',
        'backtest.avg_trade': 'L/L Trung Bình/Giao Dịch',
        'backtest.trade_history': 'Lịch Sử Giao Dịch',

        // Alert System - CRITICAL
        'alerts.stock_symbol_label': 'Mã Cổ Phiếu',
        'alerts.loading_stocks': '-- Đang tải --',
        'alerts.alert_type_label': 'Loại Cảnh Báo',
        'alerts.type_price_above': 'Giá Trên',
        'alerts.type_price_below': 'Giá Dưới',
        'alerts.type_change_above': 'Thay Đổi % Trên',
        'alerts.type_change_below': 'Thay Đổi % Dưới',
        'alerts.type_volume_spike': 'Khối Lượng Tăng Đột Biến',
        'alerts.type_rsi_oversold': 'RSI Quá Bán (<30)',
        'alerts.type_rsi_overbought': 'RSI Quá Mua (>70)',
        'alerts.target_value_label': 'Giá Trị Mục Tiêu',
        'alerts.enter_value': 'Nhập giá trị',
        'alerts.create_alert': 'Tạo Cảnh Báo',
        'alerts.active_title': 'Cảnh Báo Đang Hoạt Động',
        'alerts.no_active': 'Không có cảnh báo nào. Tạo một cái ở trên để bắt đầu giám sát.',
        'alerts.triggered_title': 'Cảnh Báo Đã Kích Hoạt Gần Đây',
        'alerts.no_triggered': 'Chưa có cảnh báo nào được kích hoạt.',
        'alerts.error_fill_fields': 'Vui lòng điền đầy đủ thông tin',
        'alerts.subtitle': 'Giám Sát Giá Thời Gian Thực & Thông Báo',
        'alerts.triggered_today': 'Đã Kích Hoạt Hôm Nay',
        'alerts.stocks_monitored': 'Cổ Phiếu Đang Giám Sát',

        // Macro Analysis - Risk Warnings
        'macro.risk_high': 'RỦI RO CAO',
        'macro.risk_medium': 'RỦI RO TRUNG BÌNH',
        'macro.risk_low': 'RỦI RO THẤP',
        'macro.risk_probability': 'Xác Suất Rủi Ro (%)',
        'macro.market_impact': 'Điểm Ảnh Hưởng Thị Trường (0-100)',
        'macro.interest_rate_alert': '🚨 Cảnh Báo Tăng Lãi Suất',
        'macro.interest_rate_text': 'Lãi suất tăng có tác động tiêu cực đến bất động sản.',
        'macro.consider_reduce': 'Cân nhắc: Giảm đầu tư vào',
        'macro.consider_increase': 'Tăng',
        'macro.news_demo_notice': 'Đây là các mục tin tức mẫu để minh họa. Liên kết chuyển hướng đến mục tin tức kinh doanh VnExpress để cập nhật thị trường mới nhất.',

        // Trading Automation
        'automation.connection_success': '✅ Kết nối thành công! Máy chủ API đang phản hồi chính xác.',
        'automation.rule_added': '✅ Đã thêm quy tắc! Quy tắc sẽ hoạt động khi bật giao dịch.',
        'automation.confirm_delete': '🗑️ Xóa quy tắc này?\n\nHành động này không thể hoàn tác.',

        // System Messages
        'system.api_offline': 'Máy chủ API có thể không chạy. Nhấp để mở giám sát.',
        'system.collection_success': '✅ Đã kích hoạt công việc thu thập cổ phiếu! Kiểm tra nhật ký ở trên để theo dõi tiến độ.',
        'system.collection_error': '❌ Lỗi kích hoạt công việc. Đảm bảo: 1. Máy chủ API đang chạy trên cổng 5000, 2. Kiểm tra terminal để xem lỗi',
        'system.macro_success': '✅ Đã kích hoạt công việc thu thập vĩ mô! Kiểm tra nhật ký ở trên để theo dõi tiến độ.',

        // Monitor Page
        'monitor.title': 'Giám Sát Hệ Thống & Cài Đặt',
        'monitor.subtitle': 'Giám sát thời gian thực và cấu hình cho Phân Tích Cổ Phiếu Việt Nam',
        'monitor.live': 'Trực Tiếp',
        'monitor.api_server': 'Máy Chủ API',
        'monitor.database': 'Cơ Sở Dữ Liệu',
        'monitor.scheduler': 'Bộ Lập Lịch',
        'monitor.data_collection': 'Thu Thập Dữ Liệu',
        'monitor.active_sessions': 'Phiên Hoạt Động',
        'monitor.session_stats': 'Thống Kê Phiên',
        'monitor.active_users': 'Người Dùng Đang Hoạt Động & Kết Nối',
        'monitor.user_activity': 'Hoạt Động & Hành Vi Người Dùng',
        'monitor.collection_settings': 'Cài Đặt Thu Thập',
        'monitor.loading_settings': 'Đang tải cài đặt...',
        'monitor.quick_actions': 'Thao Tác Nhanh',
        'monitor.recent_activity': 'Hoạt Động Gần Đây',
        'monitor.auto_refresh': 'Tự động làm mới mỗi 10 giây',
        'monitor.collect_stock': '📈 Thu Thập Dữ Liệu Cổ Phiếu Ngay',
        'monitor.collect_macro': '🌍 Thu Thập Dữ Liệu Vĩ Mô Ngay',
        'monitor.view_schedule': '📅 Xem Lịch Trình',
        'monitor.view_logs': '📋 Xem Nhật Ký',
        'monitor.edit_settings': '🔧 Chỉnh Sửa Cài Đặt',
        'monitor.restart_scheduler': '🔄 Khởi Động Lại Bộ Lập Lịch',
        'monitor.status': 'Trạng Thái',
        'monitor.message': 'Thông Báo',
        'monitor.connection': 'Kết Nối',
        'monitor.process_id': 'ID Tiến Trình',
        'monitor.endpoint': 'Điểm Cuối',
        'monitor.active_stocks': 'Cổ Phiếu Hoạt Động',
        'monitor.last_stock_update': 'Cập Nhật Cổ Phiếu Cuối',
        'monitor.last_index_update': 'Cập Nhật Chỉ Số Cuối',
        'monitor.last_macro_update': 'Cập Nhật Vĩ Mô Cuối',
        'monitor.todays_updates': 'Cập Nhật Hôm Nay',
        'monitor.session_id': 'ID Phiên',
        'monitor.current_page': 'Trang Hiện Tại',
        'monitor.page_views': 'Lượt Xem Trang',
        'monitor.duration': 'Thời Gian',
        'monitor.last_seen': 'Xem Cuối',
        'monitor.ip_address': 'Địa Chỉ IP',
        'monitor.no_active_sessions': 'Không có phiên hoạt động',
        'monitor.no_activity': 'Chưa có hoạt động',
        'monitor.top_pages': 'Trang Hàng Đầu',
        'monitor.total_page_views': 'Tổng Lượt Xem Trang',
        'monitor.avg_per_session': 'Trung Bình Mỗi Phiên',

        // Real-Time Dashboard
        'realtime.title': '📊 Giám Sát Cổ Phiếu Việt Nam',
        'realtime.subtitle': 'Bảng Điều Khiển Phân Tích Kỹ Thuật Thời Gian Thực',
        'realtime.live': 'TRỰC TIẾP',
        'realtime.enhanced_dashboard': '🎯 Bảng Điều Khiển Nâng Cao',
        'realtime.auto_trading': '🤖 Giao Dịch Tự Động',
        'realtime.demo_mode': '🎮 CHẾ ĐỘ THỬ NGHIỆM',
        'realtime.connecting': 'Đang kết nối đến máy chủ...',
        'realtime.top_recommendations': '📈 Khuyến Nghị Hàng Đầu',
        'realtime.score_distribution': '📊 Phân Phối Điểm',
        'realtime.technical_indicators': '🎯 Chỉ Báo Kỹ Thuật',
        'realtime.budget_allocation': '💰 Phân Bổ Ngân Sách (10 Triệu VNĐ)',
        'realtime.rsi_overview': '📉 Tổng Quan RSI',
        'realtime.market_signals': '⚡ Tín Hiệu Thị Trường',
        'realtime.waiting_data': 'Đang chờ dữ liệu...',
        'realtime.loading_indicators': 'Đang tải chỉ báo...',
        'realtime.calculating_allocation': 'Đang tính toán phân bổ...',
        'realtime.analyzing_signals': 'Đang phân tích tín hiệu...',

        // Form Labels - General
        'form.loading': '-- Đang tải --',
        'form.search_placeholder': '🔍 Tìm kiếm cổ phiếu...',

        // Diversification Risk
        'diversification.concentration_risk': '⚠️ Rủi Ro Tập Trung',
        'diversification.well_diversified': '✅ Đa Dạng Hóa Tốt',
        'diversification.moderate': 'ℹ️ Đa Dạng Hóa Vừa Phải',

        // Advanced Features - Tabs
        'advanced.tab.margin': 'Quản Lý Ký Quỹ',
        'advanced.tab.patterns': 'Nhận Diện Mô Hình',
        'advanced.tab.ml': '🧠 Học Máy',
        'advanced.tab.correlation': 'Phân Tích Tương Quan',
        'advanced.tab.report': 'Báo Cáo Danh Mục',

        // Report Section
        'report.title': 'Báo Cáo Danh Mục',
        'report.info': 'Tạo báo cáo phân tích danh mục toàn diện với các chỉ số chính, biểu đồ hiệu suất và khuyến nghị.',
        'report.settings_title': 'Cài Đặt Báo Cáo',
        'report.options_title': 'Tùy Chọn Báo Cáo',
        'report.report_type': 'Loại Báo Cáo',
        'report.type_summary': 'Báo Cáo Tóm Tắt',
        'report.type_detailed': 'Phân Tích Chi Tiết',
        'report.type_performance': 'Báo Cáo Hiệu Suất',
        'report.type_risk': 'Đánh Giá Rủi Ro',
        'report.time_period': 'Khoảng Thời Gian',
        'report.period_1m': '1 Tháng Gần Nhất',
        'report.period_3m': '3 Tháng Gần Nhất',
        'report.period_6m': '6 Tháng Gần Nhất',
        'report.period_1y': '1 Năm Gần Nhất',
        'report.period_ytd': 'Từ Đầu Năm',
        'report.format': 'Định Dạng Xuất',
        'report.format_pdf': 'Tài Liệu PDF',
        'report.format_html': 'Trang HTML',
        'report.format_excel': 'Bảng Tính Excel',
        'report.include_charts': 'Bao Gồm Biểu Đồ & Trực Quan',
        'report.include_recommendations': 'Bao Gồm Khuyến Nghị AI',
        'report.generate_button': 'Tạo Báo Cáo',
        'report.preview_title': 'Xem Trước Báo Cáo',
        'report.download_button': 'Tải Xuống Báo Cáo',

        // Margin Management
        'margin.title': 'Quản Lý Ký Quỹ',
        'margin.intro': 'Theo dõi và quản lý tài khoản ký quỹ, giám sát sức mua, tính toán yêu cầu ký quỹ và nhận cảnh báo margin call.',
        'margin.account_setup': 'Thiết Lập Tài Khoản Ký Quỹ',
        'margin.cash_equity': 'Tổng Vốn Tiền Mặt (₫)',
        'margin.cash_equity_hint': 'Tiền mặt của bạn đầu tư',
        'margin.borrowed_amount': 'Số Tiền Vay (₫)',
        'margin.borrowed_amount_hint': 'Tiền vay từ công ty chứng khoán',
        'margin.margin_ratio': 'Tỷ Lệ Ký Quỹ (%)',
        'margin.margin_ratio_hint': 'Tỷ lệ vốn yêu cầu (thường là 50%)',
        'margin.interest_rate': 'Lãi Suất Năm (%)',
        'margin.interest_rate_hint': 'Chi phí vay hàng năm',
        'margin.calculate': 'Tính Toán Chỉ Số Ký Quỹ',
        'margin.overview': 'Tổng Quan Tài Khoản Ký Quỹ',
        'margin.total_value': 'Tổng Giá Trị Danh Mục',
        'margin.total_value_hint': 'Tiền mặt + Tiền vay',
        'margin.buying_power': 'Sức Mua Khả Dụng',
        'margin.buying_power_hint': 'Có thể đầu tư tối đa',
        'margin.current_ratio': 'Tỷ Lệ Ký Quỹ Hiện Tại',
        'margin.current_ratio_hint': 'Vốn / Tổng Giá Trị',
        'margin.daily_interest': 'Chi Phí Lãi Hàng Ngày',
        'margin.daily_interest_hint': 'Chi phí vay mỗi ngày',
        'margin.warning_title': 'CẢNH BÁO MARGIN CALL',
        'margin.warning_text': 'Tỷ lệ ký quỹ của bạn dưới mức yêu cầu. Bạn có thể nhận được margin call từ công ty chứng khoán.',
        'margin.warning_details': 'Hành Động Cần Thiết',
        'margin.warning_add': 'Thêm',
        'margin.warning_or': 'HOẶC',
        'margin.warning_sell': 'Bán',
        'margin.healthy_title': 'TÀI KHOẢN KÝ QUỸ KHỎE MẠNH',
        'margin.healthy_text': 'Tỷ lệ ký quỹ của bạn trên mức yêu cầu. Tài khoản của bạn ở trạng thái tốt.',
        'margin.healthy_buffer': 'Bạn có',
        'margin.healthy_buffer2': 'vùng đệm trên mức ký quỹ yêu cầu.',
        'margin.healthy_max_loss': 'Danh mục của bạn có thể giảm tới',
        'margin.healthy_max_loss2': 'trước khi kích hoạt margin call.',
        'margin.interest_analysis': 'Phân Tích Chi Phí Lãi',
        'margin.daily_cost': 'Chi Phí Hàng Ngày',
        'margin.weekly_cost': 'Chi Phí Hàng Tuần',
        'margin.monthly_cost': 'Chi Phí Hàng Tháng',
        'margin.yearly_cost': 'Chi Phí Hàng Năm',
        'margin.position_requirements': 'Vị Thế & Yêu Cầu',
        'margin.initial_margin': 'Ký Quỹ Ban Đầu Yêu Cầu',
        'margin.initial_margin_hint': 'Tối thiểu để mở vị thế',
        'margin.maintenance_margin': 'Ký Quỹ Duy Trì',
        'margin.maintenance_margin_hint': 'Phải duy trì trên mức này',
        'margin.excess_margin': 'Ký Quỹ Dư Thừa',
        'margin.excess_margin_hint': 'Vùng đệm an toàn khả dụng',
        'margin.leverage_analysis': 'Phân Tích Đòn Bẩy',
        'margin.current_leverage': 'Đòn Bẩy Hiện Tại',
        'margin.leverage_conservative': 'Thận Trọng',
        'margin.leverage_moderate': 'Vừa Phải',
        'margin.leverage_aggressive': 'Mạo Hiểm',
        'margin.max_leverage': 'Đòn Bẩy Tối Đa',
        'margin.max_leverage_hint': 'Dựa trên tỷ lệ ký quỹ',
        'margin.risk_level': 'Mức Độ Rủi Ro',
        'margin.risk_level_hint': 'Dựa trên đòn bẩy hiện tại',
        'margin.risk_low': 'Thấp',
        'margin.risk_medium': 'Trung Bình',
        'margin.risk_moderate': 'Vừa Phải',
        'margin.risk_high': 'Cao',
        'margin.risk_very_high': 'Rất Cao',
        'margin.education_title': 'Hiểu Về Giao Dịch Ký Quỹ',
        'margin.education_intro': 'Giao dịch ký quỹ cho phép bạn vay tiền từ công ty chứng khoán để mua nhiều cổ phiếu hơn so với chỉ sử dụng tiền mặt của bạn.',
        'margin.education_buying_power': 'Sức Mua: Tổng số tiền bạn có thể đầu tư (tiền mặt + tiền vay)',
        'margin.education_margin_ratio': 'Tỷ Lệ Ký Quỹ: Phần trăm vốn yêu cầu (thường là 50% - bạn có thể vay tới 50% giá trị mua)',
        'margin.education_margin_call': 'Margin Call: Khi vốn giảm xuống dưới yêu cầu duy trì, công ty chứng khoán có thể buộc bạn thêm tiền hoặc bán vị thế',
        'margin.education_interest': 'Lãi Suất: Bạn trả lãi hàng ngày cho số tiền vay',
        'margin.education_leverage': 'Đòn Bẩy: Khuếch đại cả lãi lẫn lỗ - sử dụng thận trọng!',
        'margin.education_warning': '⚠️ Cảnh Báo: Giao dịch ký quỹ có rủi ro đáng kể. Bạn có thể mất nhiều hơn khoản đầu tư ban đầu.',

        // Pattern Recognition
        'pattern.title': 'Nhận Diện Mô Hình',
        'pattern.intro': 'Tự động phát hiện các mô hình biểu đồ và hình nến.',
        'pattern.select_stock': 'Chọn Cổ Phiếu',
        'pattern.detect': 'Phát Hiện Mô Hình',
        'pattern.detected': 'Mô Hình Đã Phát Hiện',
        'pattern.bullish': 'Tăng Giá',
        'pattern.bearish': 'Giảm Giá',
        'pattern.confidence': 'Độ Tin Cậy',

        // Machine Learning
        'ml.title': 'Dự Báo Học Máy',
        'ml.intro': 'Dự đoán mạng nơ-ron LSTM nâng cao với khoảng tin cậy.',
        'ml.select_stock': 'Chọn Cổ Phiếu',
        'ml.forecast_horizon': 'Thời Gian Dự Báo',
        'ml.run_forecast': 'Chạy Dự Báo',
        'ml.accuracy': 'Độ Chính Xác Mô Hình',
        'ml.trend': 'Xu Hướng Dự Đoán',
        'ml.confidence': 'Độ Tin Cậy',
        'ml.upward': 'Tăng',
        'ml.downward': 'Giảm',
        'ml.sideways': 'Đi Ngang',
        'ml.feature_importance': 'Tầm Quan Trọng Đặc Trưng',

        // Correlation Analysis
        'correlation.title': 'Phân Tích Tương Quan',
        'correlation.intro': 'Phân tích mối quan hệ giữa các cổ phiếu và xác định cơ hội giao dịch cặp.',
        'correlation.heatmap': 'Bản Đồ Nhiệt Tương Quan',
        'correlation.matrix': 'Ma Trận Tương Quan',
        'correlation.pair_trading': 'Cơ Hội Giao Dịch Cặp',
        'correlation.highly_correlated': 'Tương Quan Cao',
        'correlation.negatively_correlated': 'Tương Quan Âm',

        // Tips and Help Text
        'tip.existing_portfolio': 'Thêm tất cả cổ phiếu bạn hiện đang sở hữu. Chúng tôi sẽ tính giá trị hiện tại và đưa ra khuyến nghị cá nhân hóa.',
        'tip.preferred_stocks': 'Các cổ phiếu ưu tiên được chọn sẽ được bao gồm trước (với ít nhất 10% phân bổ mỗi cổ). Hệ thống sau đó sẽ tối ưu hóa ngân sách còn lại cho các cổ phiếu phù hợp khác.',
        'tip.smart_recommendations': 'Chọn một hộp kiểm chiến lược ở trên để nhận khuyến nghị cổ phiếu được hỗ trợ bởi AI dựa trên dữ liệu thị trường thực.',

        // Form Labels
        'form.select_stocks': 'Chọn Cổ Phiếu Cho Danh Mục',
        'form.select_stock': 'Chọn Cổ Phiếu',
        'form.strategy': 'Chiến Lược',
        'form.enter_budget': 'Nhập Ngân Sách Đầu Tư Của Bạn (VNĐ)',
        'form.search_stocks': 'Tìm kiếm cổ phiếu...',
        'form.placeholder_budget': 'vd: 100000000',

        // Menus
        'menu.dashboards': 'Bảng Điều Khiển',
        'menu.all_dashboards': 'Tất Cả Bảng Điều Khiển',
        'menu.market_analysis': 'Phân Tích Thị Trường',
        'menu.investment_tools': 'Công Cụ Đầu Tư',
        'menu.automation_alerts': 'Tự Động Hóa & Cảnh Báo',
        'menu.price_forecasting': 'Dự Báo Giá',
        'menu.price_alerts': 'Cảnh Báo Giá',

        // Alert System
        'alerts.stock_symbol': 'Mã Cổ Phiếu',
        'alerts.alert_type': 'Loại Cảnh Báo',
        'alerts.target_value': 'Giá Trị Mục Tiêu',
        'alerts.enter_value': 'Nhập giá trị',
        'alerts.active_alerts': 'Cảnh Báo Đang Hoạt Động',

        // Actions
        'action.access_pro': 'Truy Cập Pro',
        'action.analyze_factors': 'Phân Tích Yếu Tố',
        'action.analyze_history': 'Phân Tích Lịch Sử',
        'action.configure_alerts': 'Cấu Hình Cảnh Báo',
        'action.generate_forecast': 'Tạo Dự Báo',
        'action.setup_automation': 'Thiết Lập Tự Động',
        'action.view_charts': 'Xem Biểu Đồ',
        'action.view_dashboard': 'Xem Bảng Điều Khiển',

        // Advanced Features
        'advanced.title': 'Tính Năng Nâng Cao',
        'advanced.backtesting_desc': 'Kiểm tra hiệu suất chiến lược với dữ liệu lịch sử',
        'advanced.backtesting_info': 'Thông tin về kiểm tra ngược',
        'advanced.correlation_analysis': 'Phân Tích Tương Quan',
        'advanced.correlation_desc': 'Phân tích mối quan hệ giữa các cổ phiếu',
        'advanced.machine_learning': 'Học Máy',
        'advanced.ml_desc': 'Dự đoán dựa trên học máy',
        'advanced.pattern_recognition': 'Nhận Dạng Mẫu',
        'advanced.patterns_desc': 'Phát hiện các mẫu biểu đồ',
        'advanced.portfolio_desc': 'Phân tích danh mục đầu tư chi tiết',
        'advanced.risk_desc': 'Đánh giá và quản lý rủi ro',
        'advanced.risk_info': 'Thông tin về rủi ro',
        'advanced.risk_management': 'Quản Lý Rủi Ro',
        'advanced.strategy_backtesting': 'Kiểm Tra Ngược Chiến Lược',
        'advanced.tab.correlation': 'Tương Quan',
        'advanced.tab.margin': 'Ký Quỹ',
        'advanced.tab.ml': 'Học Máy',
        'advanced.tab.patterns': 'Mẫu Hình',

        // Alerts Extended
        'alerts.alert_type_label': 'Loại Cảnh Báo',
        'alerts.create_new': 'Tạo Cảnh Báo Mới',
        'alerts.recently_triggered': 'Cảnh Báo Vừa Kích Hoạt',
        'alerts.target_value_label': 'Giá Trị Mục Tiêu',
        'alerts.type_change_above': 'Thay Đổi Trên',
        'alerts.type_change_below': 'Thay Đổi Dưới',
        'alerts.type_price_above': 'Giá Trên',
        'alerts.type_price_below': 'Giá Dưới',
        'alerts.type_rsi_overbought': 'RSI Quá Mua',
        'alerts.type_rsi_oversold': 'RSI Quá Bán',
        'alerts.type_volume_spike': 'Tăng Đột Biến Khối Lượng',

        // Automation
        'automation.backtest': 'Kiểm Tra Ngược',
        'automation.risk_management': 'Quản Lý Rủi Ro',

        // Backtesting
        'backtest.bollinger_breakout': 'Đột Phá Bollinger',
        'backtest.macd_signal': 'Tín Hiệu MACD',
        'backtest.rsi_strategy': 'Chiến Lược RSI',
        'backtest.run_button': 'Chạy Kiểm Tra',
        'backtest.sma_crossover': 'Giao Cắt SMA',

        // Buttons
        'button.add_rule': 'Thêm Quy Tắc',
        'button.cancel': 'Hủy',
        'button.create_alert': 'Tạo Cảnh Báo',
        'button.delete': 'Xóa',
        'button.edit': 'Chỉnh Sửa',
        'button.reset_defaults': 'Đặt Lại Mặc Định',
        'button.save_config': 'Lưu Cấu Hình',
        'button.save_settings': 'Lưu Cài Đặt',
        'button.test_connection': 'Kiểm Tra Kết Nối',

        // Charts
        'charts.candlestick': 'Nến Nhật',
        'charts.ichimoku': 'Ichimoku',
        'charts.macd': 'MACD',
        'charts.mfi': 'MFI',
        'charts.obv': 'OBV',
        'charts.roc': 'ROC',
        'charts.rsi': 'RSI',
        'charts.stochastic': 'Stochastic',
        'charts.volume_bars': 'Thanh Khối Lượng',
        'charts.volume_profile': 'Hồ Sơ Khối Lượng',
        'charts.williams': 'Williams %R',

        // Collapsible
        'collapsible.collapse_all': 'Thu Gọn Tất Cả',
        'collapsible.expand_all': 'Mở Rộng Tất Cả',
        'collapsible.tip': 'Mẹo: Nhấp vào tiêu đề để mở rộng/thu gọn',

        // Common Extended
        'common.all': 'Tất Cả',
        'common.clear': 'Xóa',
        'common.clear_filter': 'Xóa Bộ Lọc',
        'common.selected': 'đã chọn',
        'common.visible': 'hiển thị',
        'common.loading_heatmap': 'Đang tải bản đồ nhiệt...',

        // Correlation
        'correlation.analyze_button': 'Phân Tích Tương Quan',
        'correlation.heatmap_heading': 'Bản Đồ Nhiệt Tương Quan',
        'correlation.info': 'Thông tin về phân tích tương quan',
        'correlation.matrix_heading': 'Ma Trận Tương Quan',
        'correlation.pair_trading_heading': 'Giao Dịch Cặp',
        'correlation.select_min_3': 'Vui lòng chọn ít nhất 3 cổ phiếu',

        // Dashboard Extended
        'dashboard.detailed_analysis': 'Phân Tích Chi Tiết Cổ Phiếu',
        'dashboard.heatmap': 'Bản Đồ Nhiệt',
        'dashboard.performance_heatmap': 'Bản Đồ Nhiệt Hiệu Suất',
        'dashboard.realtime': 'Thời Gian Thực',
        'dashboard.score_distribution': 'Phân Bố Điểm Số',

        // Evaluation
        'evaluation.closer_to_1_is_better': 'Càng gần 1 càng tốt',
        'evaluation.effectiveness': 'Hiệu Quả',
        'evaluation.error_distribution': 'Phân Bố Lỗi',
        'evaluation.lower_is_better': 'Càng thấp càng tốt',
        'evaluation.mae': 'MAE (Sai Số Tuyệt Đối Trung Bình)',
        'evaluation.mape': 'MAPE (Sai Số Phần Trăm Tuyệt Đối Trung Bình)',
        'evaluation.model_comparison': 'So Sánh Mô Hình',
        'evaluation.prediction_accuracy': 'Độ Chính Xác Dự Đoán',
        'evaluation.r2': 'R² (Hệ Số Xác Định)',
        'evaluation.rmse': 'RMSE (Căn Bậc Hai Sai Số Bình Phương Trung Bình)',
        'evaluation.suggested_model': 'Mô Hình Được Đề Xuất',
        'evaluation.use_this_model': 'Sử dụng mô hình này để có kết quả tốt nhất',

        // Features
        'feature.advanced_charts': 'Biểu Đồ Nâng Cao',
        'feature.advanced_charts_desc': 'Biểu đồ kỹ thuật chuyên nghiệp',
        'feature.alerts': 'Hệ Thống Cảnh Báo',
        'feature.alerts_desc': 'Cảnh báo giá và chỉ báo theo thời gian thực',
        'feature.automation': 'Tự Động Giao Dịch',
        'feature.automation_desc': 'Tự động hóa chiến lược giao dịch',
        'feature.forecasting': 'Dự Báo Giá',
        'feature.forecasting_desc': 'Dự đoán giá bằng AI',
        'feature.live_data': 'Dữ Liệu Trực Tiếp',
        'feature.live_data_desc': 'Giá cổ phiếu theo thời gian thực',
        'feature.macro_analysis': 'Phân Tích Vĩ Mô',
        'feature.macro_analysis_desc': 'Phân tích kinh tế và môi trường',
        'feature.portfolio': 'Phân Tích Danh Mục',
        'feature.portfolio_desc': 'Tối ưu hóa danh mục đầu tư',
        'feature.technical': 'Phân Tích Kỹ Thuật',
        'feature.technical_desc': 'Chỉ báo và mẫu hình kỹ thuật',

        // Footer
        'footer.copyright': '© 2024 VNStock Analytics',
        'footer.disclaimer': 'Chỉ nhằm mục đích giáo dục. Không phải lời khuyên tài chính. Giao dịch với rủi ro của riêng bạn.',

        // Forecast
        'forecast.accuracy_evaluation': 'Đánh Giá Độ Chính Xác',
        'forecast.actual_vs_predicted': 'Thực Tế so với Dự Đoán',
        'forecast.alert_generate_first': 'Vui lòng tạo dự báo trước',
        'forecast.controls': 'Điều Khiển Dự Báo',
        'forecast.days_label': 'Số Ngày Dự Báo',
        'forecast.effectiveness_score': 'Điểm Hiệu Quả',
        'forecast.forecast_comparison': 'So Sánh Dự Báo',
        'forecast.forecast_results': 'Kết Quả Dự Báo',
        'forecast.generate': 'Tạo Dự Báo',
        'forecast.model_label': 'Mô Hình Dự Báo',
        'forecast.price_forecast': 'Dự Báo Giá',
        'forecast.recommendations': 'Khuyến Nghị',
        'forecast.select_model': 'Chọn Mô Hình',
        'forecast.select_stocks': 'Chọn Cổ Phiếu Để Dự Báo',
        'forecast.title': 'Dự Báo Giá & Phân Tích',

        // Form
        'form.budget_label': 'Ngân Sách Đầu Tư',
        'form.select_stocks': 'Chọn Cổ Phiếu',

        // History
        'history.period_label': 'Khoảng Thời Gian',
        'history.period.30d': '30 Ngày',
        'history.period.60d': '60 Ngày',
        'history.period.90d': '90 Ngày',
        'history.period.180d': '6 Tháng',
        'history.period.1y': '1 Năm',

        // Home
        'home.advanced_analytics': 'Phân Tích Nâng Cao',
        'home.advanced_analytics_desc': 'Công cụ phân tích chuyên sâu',
        'home.cta': 'Bắt đầu phân tích',
        'home.features': 'Tính Năng',
        'home.hero_subtitle': 'Nền tảng phân tích và dự báo thị trường chứng khoán Việt Nam',
        'home.hero_title': 'Phân Tích Thông Minh Thị Trường Chứng Khoán Việt Nam',
        'home.subtitle': 'Công cụ phân tích chuyên nghiệp cho thị trường chứng khoán Việt Nam',
        'home.title': 'VNStock Analytics',

        // Macro
        'macro.commodities_energy': 'Hàng Hóa & Năng Lượng',
        'macro.correlation_matrix': 'Ma Trận Tương Quan',
        'macro.factor_correlation': 'Tương Quan Yếu Tố Môi Trường',
        'macro.factors_impact': 'Tác Động Yếu Tố Môi Trường',
        'macro.geopolitical_assessment': 'Đánh Giá Rủi Ro Địa Chính Trị',
        'macro.key_indicators': 'Chỉ Báo Kinh Tế Chính',
        'macro.market_sentiment': 'Tâm Lý Thị Trường Tổng Thể',
        'macro.oil_price': 'Giá Dầu Toàn Cầu',
        'macro.policy_regulatory': 'Thay Đổi Chính Sách & Quy Định',
        'macro.sentiment_based_on': 'Dựa trên: Giá dầu, căng thẳng địa chính trị, chính sách tiền tệ, chỉ số kinh tế và tin tức thị trường',
        'macro.subheader.policy_timeline': 'Dòng Thời Gian Tác Động Chính Sách',
        'macro.subheader.regional_tensions': 'Tác Động Căng Thẳng Khu Vực',
        'macro.subheader.sector_impact': 'Phân Tích Tác Động Ngành',
        'macro.tab.environment': 'Môi Trường',
        'macro.tab.news': 'Tin Tức & Sự Kiện',
        'macro.tab.overview': 'Tổng Quan',
        'macro.title': 'Phân Tích Vĩ Mô & Môi Trường',

        // Menu
        'menu.tools': 'Công Cụ',
        'menu.automation': 'Tự Động Hóa',
        'menu.platform': 'Nền Tảng',

        // Models
        'model.advanced_ensemble': 'Ensemble Nâng Cao (Trọng Số)',
        'model.arima': 'ARIMA',
        'model.ensemble': 'Ensemble (Trung Bình)',
        'model.exponential': 'Làm Mịn Hàm Mũ',
        'model.garch': 'GARCH',
        'model.gradient_boost': 'Gradient Boosting',
        'model.kalman': 'Bộ Lọc Kalman',
        'model.linear': 'Hồi Quy Tuyến Tính',
        'model.lstm': 'LSTM',
        'model.moving_average': 'Trung Bình Động',
        'model.prophet': 'Prophet',
        'model.random_forest': 'Random Forest',
        'model.sarima': 'SARIMA',
        'model.transformer': 'Transformer',
        'model.wavenet': 'WaveNet',
        'model.xgboost': 'XGBoost',

        // Portfolio
        'portfolio.allocation': 'Phân Bổ',
        'portfolio.analytics': 'Phân Tích Danh Mục',
        'portfolio.asset_allocation': 'Phân Bổ Tài Sản',
        'portfolio.balanced': 'Cân Bằng',
        'portfolio.blue_chip': 'Blue Chip',
        'portfolio.budget': 'Ngân Sách',
        'portfolio.conservative': 'Bảo Thủ',
        'portfolio.diversification_score': 'Điểm Đa Dạng Hóa',
        'portfolio.expected_return': 'Lợi Nhuận Kỳ Vọng',
        'portfolio.generate_plan': 'Tạo Kế Hoạch Đầu Tư',
        'portfolio.growth': 'Tăng Trưởng',
        'portfolio.holdings': 'Danh Mục Nắm Giữ',
        'portfolio.investment_plan': 'Kế Hoạch Đầu Tư',
        'portfolio.new_portfolio': 'Danh Mục Mới',
        'portfolio.optimize': 'Tối Ưu Hóa Danh Mục',
        'portfolio.portfolio_type': 'Loại Danh Mục',
        'portfolio.preferred_stocks': 'Cổ Phiếu Ưa Thích',
        'portfolio.report': 'Báo Cáo Danh Mục',
        'portfolio.risk_level': 'Mức Độ Rủi Ro',
        'portfolio.select_strategy': 'Chọn Chiến Lược',
        'portfolio.sharpe_ratio': 'Tỷ Lệ Sharpe',
        'portfolio.step1': 'Bước 1: Chọn Chiến Lược',
        'portfolio.step2': 'Bước 2: Loại Danh Mục',
        'portfolio.step3': 'Bước 3: Ngân Sách & Ưu Tiên',
        'portfolio.step4': 'Bước 4: Xem Xét & Tạo',
        'portfolio.strategy': 'Chiến Lược',
        'portfolio.title': 'Phân Tích Danh Mục Đầu Tư',
        'portfolio.total_value': 'Tổng Giá Trị',
        'portfolio.update_portfolio': 'Cập Nhật Danh Mục',
        'portfolio.volatility': 'Độ Biến Động',

        // Report
        'report.download': 'Tải Báo Cáo',
        'report.excel': 'Excel',
        'report.format': 'Định Dạng',
        'report.html': 'HTML',
        'report.include_charts': 'Bao Gồm Biểu Đồ',
        'report.include_recommendations': 'Bao Gồm Khuyến Nghị',
        'report.pdf': 'PDF',
        'report.settings': 'Cài Đặt Báo Cáo',

        // Section
        'section.analysis_signals': 'Phân Tích & Tín Hiệu',
        'section.price_history_analysis': 'Phân Tích Lịch Sử Giá',
        'section.price_statistics': 'Thống Kê Giá',
        'section.technical_indicators': 'Chỉ Báo Kỹ Thuật',
        'section.technical_signals': 'Tín Hiệu Kỹ Thuật',
        'section.volume_analysis': 'Phân Tích Khối Lượng',

        // Settings
        'settings.api': 'Cài Đặt API',
        'settings.api_endpoint': 'Điểm Cuối API',
        'settings.appearance': 'Giao Diện',
        'settings.currency': 'Tiền Tệ',
        'settings.data': 'Dữ Liệu',
        'settings.display': 'Hiển Thị',
        'settings.general': 'Chung',
        'settings.language': 'Ngôn Ngữ',
        'settings.notifications': 'Thông Báo',
        'settings.refresh_rate': 'Tốc Độ Làm Mới',
        'settings.theme': 'Chủ Đề',
        'settings.title': 'Cài Đặt',

        // Stats
        'stats.avg_volume': 'Khối Lượng Trung Bình',
        'stats.change': 'Thay Đổi',
        'stats.high': 'Cao',
        'stats.low': 'Thấp',
        'stats.market_cap': 'Vốn Hóa',
        'stats.price': 'Giá',
        'stats.volume': 'Khối Lượng',

        // Status
        'status.active': 'Đang Hoạt Động',
        'status.completed': 'Đã Hoàn Thành',
        'status.error': 'Lỗi',
        'status.inactive': 'Không Hoạt Động',
        'status.pending': 'Đang Chờ',
        'status.running': 'Đang Chạy',

        // Table
        'table.actions': 'Hành Động',
        'table.change': 'Thay Đổi',
        'table.chart': 'Biểu Đồ',
        'table.last_update': 'Cập Nhật Cuối',
        'table.price': 'Giá',
        'table.recommendation': 'Khuyến Nghị',
        'table.rsi': 'RSI',
        'table.score': 'Điểm',
        'table.signals': 'Tín Hiệu',
        'table.symbol': 'Mã',
        'table.t_plus': 'T+2 Hợp Lệ',
        'table.volume': 'Khối Lượng',

        // Time
        'time.1d': '1 Ngày',
        'time.1m': '1 Tháng',
        'time.1w': '1 Tuần',
        'time.1y': '1 Năm',
        'time.3m': '3 Tháng',
        'time.6m': '6 Tháng',
        'time.all': 'Tất Cả',
        'time.custom': 'Tùy Chỉnh',
        'time.ytd': 'Từ Đầu Năm',

        // Trading
        'trading.buy': 'Mua',
        'trading.hold': 'Giữ',
        'trading.sell': 'Bán',
        'trading.strong_buy': 'Mua Mạnh',
        'trading.strong_sell': 'Bán Mạnh'
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

        // Set HTML lang attribute
        document.documentElement.lang = currentLanguage;

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

    // Update HTML lang attribute
    document.documentElement.lang = lang;

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

// Format date based on current language
function formatDate(date, options = {}) {
    if (!date) return '';

    // Convert to Date object if string
    const dateObj = typeof date === 'string' ? new Date(date) : date;

    // Get locale based on current language
    const locale = currentLanguage === 'vi' ? 'vi-VN' : 'en-US';

    // Default options
    const defaultOptions = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
    };

    return dateObj.toLocaleDateString(locale, { ...defaultOptions, ...options });
}

// Format date and time based on current language
function formatDateTime(date, options = {}) {
    if (!date) return '';

    // Convert to Date object if string
    const dateObj = typeof date === 'string' ? new Date(date) : date;

    // Get locale based on current language
    const locale = currentLanguage === 'vi' ? 'vi-VN' : 'en-US';

    // Default options
    const defaultOptions = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    };

    return dateObj.toLocaleString(locale, { ...defaultOptions, ...options });
}

// Auto-initialize on page load
if (typeof window !== 'undefined') {
    // Expose functions to window for onclick handlers
    window.switchLanguage = switchLanguage;
    window.t = t;
    window.getCurrentLanguage = getCurrentLanguage;
    window.translatePage = translatePage;
    window.formatDate = formatDate;
    window.formatDateTime = formatDateTime;

    window.addEventListener('DOMContentLoaded', initI18n);
}
