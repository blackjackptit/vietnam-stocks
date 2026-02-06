# Dashboard Advanced - Vietnamese Translation Status

## Summary

Machine Learning icon updated from 🤖 to 🧠 (brain icon) - **✅ COMPLETE**

Added **90+ translation keys** to i18n.js for dashboard_advanced.html content.

## Completed Translations

### ✅ Feature Box Titles & Descriptions (6 items)
- Portfolio Analytics description
- Strategy Backtesting description
- Risk Management description
- Pattern Recognition description
- Machine Learning description
- Correlation Analysis description

All feature boxes now have `data-i18n` attributes on both titles and descriptions.

### ✅ Translation Keys Added to i18n.js (90+ keys)

**Advanced Features (12 keys)**
- `advanced.portfolio_desc` - Portfolio description
- `advanced.backtesting_desc` - Backtesting description
- `advanced.risk_desc` - Risk description
- `advanced.patterns_desc` - Patterns description
- `advanced.ml_desc` - ML description
- `advanced.correlation_desc` - Correlation description
- Plus 6 info messages for alerts

**Common Actions (18 keys)**
- `common.select_stocks`, `common.search_stocks`
- `common.all`, `common.clear`, `common.visible`, `common.selected`
- `common.analyze`, `common.calculate`, `common.generate`, `common.run`, `common.detect`
- `common.add`, `common.remove`
- `common.hold`, `common.sell_action`, `common.buy_more`

**Form Elements (4 keys)**
- `form.select_stock`, `form.loading`
- `form.enter_amount`, `form.placeholder_search`

**Validation Messages (4 keys)**
- `validation.select_min_stocks`
- `validation.select_stock`
- `validation.loading_data`
- `validation.not_enough_data`

**Chart Labels (11 keys)**
- Asset Allocation, Efficient Frontier, Current Portfolio
- Risk %, Expected Return %, Equity Curve
- Buy & Hold, Portfolio Value, Beta by Stock
- Feature Importance, LSTM Forecast

**Table Headers (14 keys)**
- Stock, Shares, Buy Price, Current, Profit/Loss
- Action, Recommendation, Allocation, Amount
- Price, Exp. Return, Risk, Date
- Beta, Volatility, VaR, Risk Grade

**Metric Labels (7 keys)**
- Total Return, Win Rate, Total Trades, Avg Trade P/L
- Model Accuracy, Predicted Trend, Confidence

**Section Headers (8 keys)**
- Trade History, Detected Patterns, Feature Importance
- Correlation Matrix, Correlation Heatmap, Pair Trading
- Allocation Breakdown, Investment Rationale

**Total**: 90+ keys with both English and Vietnamese translations

## Partially Complete

### ⚠️ Feature Box Descriptions - HTML Updated
- 6 feature boxes now have `data-i18n` attributes
- Both titles and descriptions are translatable

## Remaining Work (100+ items)

### 🔴 High Priority - User-Facing UI

1. **Button Labels** (30+ items)
   - Lines 884-887: All, Clear, Visible, selected count
   - Lines 892: Analyze Portfolio
   - Lines 979: Add Stock Holding
   - Lines 1001: Clear All, count labels
   - Lines 1086: Generate Investment Plan
   - Lines 1142: Run Backtest
   - Lines 1198: Calculate Risk Metrics
   - Lines 1297: Calculate Margin Metrics
   - Lines 1467, 1509, 1563: Detect/Generate/Analyze buttons

2. **Form Labels & Inputs** (25+ items)
   - Lines 877: Select Stocks for Portfolio
   - Lines 881: Search placeholders (multiple)
   - Lines 938: Select Portfolio Type
   - Lines 1078: Enter Investment Budget
   - Lines 1126-1137: Stock/Strategy selectors
   - Lines 1183-1193: Select Stocks controls
   - Lines 1246-1292: Margin account input fields

3. **Alert Messages** (15+ items)
   - Lines 873, 1121, 1179, 1236: Feature info alerts
   - Lines 1459, 1488, 1544: Pattern/ML/Correlation alerts
   - Lines 2046, 2196, 2402: Validation errors
   - Lines 3086, 3154, 3195, 3305: Stock selection errors

4. **Portfolio Type Cards** (4 items)
   - Lines 947-948: Existing Portfolio card
   - Lines 960-961: New Portfolio card

5. **Section Headers without data-i18n** (10+ items)
   - Lines 912, 971, 988, 1016, 1096, 1102, 1107
   - Lines 1168, 1225, 1303
   - Lines 1358, 1381, 1404, 1438

### 🟡 Medium Priority - Helper Text

6. **Help Text & Tips** (20+ items)
   - Lines 973, 982, 990, 1010, 1018, 1073, 1090
   - Lines 1253, 1265, 1279, 1292
   - Lines 1385-1392, 1415-1417
   - Lines 1440-1448: Educational content

7. **Strategy Options** (8 items)
   - Lines 1027-1028: Balanced strategy
   - Lines 1038-1039: High Growth strategy
   - Lines 1049-1050: Conservative strategy
   - Lines 1060-1061: Blue Chip strategy

8. **Recommendations & Actions** (10+ items)
   - Lines 2652, 2656, 2660, 2664: Stock recommendations
   - Lines 2699-2700: Action section titles
   - Lines 2730-2793: Business analysis

### 🟢 Low Priority - Footer & Navigation

9. **Menu Items** (4 items)
   - Lines 756: Dashboards menu button
   - Lines 782: Price Forecasting
   - Lines 798: Price Alerts
   - Lines 3633-3634: API Docs, Quick Start

10. **Footer** (2 items)
    - Line 3640: Copyright text

### 📊 Chart Content (Dynamic)

11. **Chart Titles in JavaScript** (10+ items)
    - Lines 2092, 2116, 2032: Asset Allocation, Efficient Frontier, Equity Curve
    - Lines 3110, 3123: Beta charts
    - Lines 3255: LSTM Forecast
    - Lines 3294: Feature Importance

12. **Table Headers in JavaScript** (15+ items)
    - Lines 2629-2634: Portfolio table headers
    - Lines 2713-2719: Investment plan headers
    - Lines 3066, 3130: Trade/Risk table headers

## Implementation Strategy

### Phase 1: Critical UI Elements (30 min)
- Update all button labels
- Update form labels
- Update alert messages
- Update placeholders

### Phase 2: Section Headers & Navigation (20 min)
- Add data-i18n to all section headers
- Update menu items
- Update portfolio type cards

### Phase 3: Help Text & Descriptions (20 min)
- Update all tip/help text
- Update educational content
- Update strategy descriptions

### Phase 4: Dynamic Content (30 min)
- Update JavaScript-rendered content
- Update chart titles
- Update table headers generated by JS

### Phase 5: Testing (20 min)
- Test language switching
- Verify all translations display correctly
- Check for "undefined" or missing translations

**Total Estimated Time**: 2 hours

## Files Modified So Far

1. `app/static/js/i18n.js` - Added 90+ translation keys (English + Vietnamese)
2. `app/pages/dashboard_advanced.html` - Updated 6 feature box elements

## Next Steps

1. **Immediate**: Update button labels and form inputs (highest visibility)
2. **Short-term**: Add data-i18n to section headers and alert messages
3. **Medium-term**: Update JavaScript-rendered content (charts, tables)
4. **Final**: Comprehensive testing and refinement

## Notes

- Translation keys follow pattern: `category.item`
- All keys have both English and Vietnamese translations
- Using `data-i18n` attribute for HTML elements
- Using `t()` function for JavaScript-rendered content
- Fallback to English if translation missing
