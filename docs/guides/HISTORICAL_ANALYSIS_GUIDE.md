# 📈 Historical Price Analysis Dashboard - User Guide

## Overview

The Historical Analysis Dashboard provides deep insights into stock price movements over time with professional-grade technical analysis tools.

## Access

```
http://localhost:8888/dashboard_history.html
```

Or click the **"📈 View Historical Analysis"** button from any dashboard.

## Features

### 1. **Interactive Price Chart with Moving Averages**
- **Main Price Line**: Shows closing prices over selected period
- **MA20 (Blue Dotted)**: 20-day moving average (short-term trend)
- **MA50 (Red Dotted)**: 50-day moving average (long-term trend)
- **Hover to see details**: Exact prices and dates

**How to Read:**
- Price above both MAs = Bullish trend
- Price below both MAs = Bearish trend
- MA20 crosses above MA50 = Golden Cross (buy signal)
- MA20 crosses below MA50 = Death Cross (sell signal)

### 2. **Volume Analysis Chart**
- **Green Bars**: Days when price closed higher than it opened
- **Red Bars**: Days when price closed lower than it opened
- **Height**: Trading volume

**How to Read:**
- High volume + price increase = Strong buying pressure
- High volume + price decrease = Strong selling pressure
- Low volume = Weak conviction in price movement

### 3. **RSI (Relative Strength Index)**
- Measures momentum on a scale of 0-100
- **Below 30**: Oversold (potential buying opportunity)
- **Above 70**: Overbought (potential selling opportunity)
- **30-70**: Normal range

**How to Use:**
- Look for divergences (price makes new low but RSI doesn't)
- RSI crossing 30 from below = Buy signal
- RSI crossing 70 from above = Sell signal

### 4. **MACD (Moving Average Convergence Divergence)**
- **Blue Line**: MACD line
- **Red Line**: Signal line
- **Green/Red Bars**: Histogram (difference between MACD and Signal)

**How to Read:**
- MACD crosses above Signal = Bullish signal
- MACD crosses below Signal = Bearish signal
- Histogram growing = Momentum increasing
- Histogram shrinking = Momentum decreasing

### 5. **Technical Indicators Panel**
Shows current values:
- **Current Price**: Latest closing price with % change
- **RSI (14)**: Current momentum reading
- **MA20**: 20-day average
- **MA50**: 50-day average
- **Technical Score**: Combined indicator score
- **Volume**: Today's trading volume

### 6. **Analysis & Signals**
- **Recommendation Badge**: BUY / HOLD / SELL
- **Technical Score**: -100 to +100 (higher is more bullish)
- **Signal List**: All detected technical patterns

### 7. **Price Statistics**
- **Period High**: Highest price in selected timeframe
- **Period Low**: Lowest price in selected timeframe
- **Period Change**: Total % change over period
- **Avg Volume**: Average daily volume
- **Volatility**: Standard deviation of returns
- **52W Range**: Annual price range

## How to Use

### Step 1: Select a Stock
1. Use the **"Select Stock"** dropdown
2. All stocks from your watchlist are available
3. First stock is auto-selected

### Step 2: Choose Time Period
- **30 Days**: Recent short-term trends
- **60 Days**: Default, good balance (recommended)
- **90 Days**: Medium-term analysis
- **180 Days**: Half-year trends
- **1 Year**: Long-term patterns

### Step 3: Analyze the Charts

**Quick Analysis Workflow:**

1. **Look at Price Chart**
   - Is price trending up or down?
   - Where is it relative to MA20 and MA50?

2. **Check Volume**
   - Is today's volume higher than average?
   - Does volume confirm the price trend?

3. **Review RSI**
   - Is it oversold (<30) or overbought (>70)?
   - Is there a divergence with price?

4. **Examine MACD**
   - Did MACD cross the signal line recently?
   - Is momentum building or fading?

5. **Read Indicators Panel**
   - What's the technical score?
   - What's the recommendation?

6. **Check Statistics**
   - Is current price near high or low?
   - How volatile has it been?

### Step 4: Make Informed Decisions

Combine all indicators for best results:
- **Strong Buy**: Price above MAs + RSI 30-50 + MACD bullish + High volume
- **Buy**: 2-3 bullish indicators align
- **Hold**: Mixed signals or neutral indicators
- **Sell**: 2-3 bearish indicators align
- **Strong Sell**: Price below MAs + RSI 70-100 + MACD bearish + High volume

## Example Analysis

### Example 1: Bullish Setup
```
Stock: VCB
Price Chart: Price above MA20 and MA50 ✅
Volume: Increasing on up days ✅
RSI: 45 (neutral, room to move up) ✅
MACD: Histogram turning positive ✅
Statistics: Up 15% from period low ✅

Conclusion: Strong buy opportunity
```

### Example 2: Overbought Warning
```
Stock: HPG
Price Chart: Price well above MAs 🔴
Volume: Decreasing 🔴
RSI: 78 (overbought) 🔴
MACD: Histogram shrinking 🔴
Statistics: Near period high 🔴

Conclusion: Consider taking profits
```

### Example 3: Oversold Opportunity
```
Stock: FPT
Price Chart: Price near MA50 support ⚪
Volume: Decreasing on down days ✅
RSI: 28 (oversold) ✅
MACD: Starting to turn up ✅
Statistics: Near period low ✅

Conclusion: Potential buy on reversal
```

## Pro Tips

1. **Use Multiple Timeframes**
   - Check 30-day for entries
   - Check 180-day for overall trend
   - Don't fight the long-term trend

2. **Confirm with Volume**
   - Price moves without volume are suspect
   - Volume should confirm the direction

3. **Watch for Divergences**
   - Price makes new high but RSI doesn't = Bearish divergence
   - Price makes new low but RSI doesn't = Bullish divergence

4. **Respect Support/Resistance**
   - MA50 often acts as support in uptrends
   - Previous highs/lows are important levels

5. **Don't Rely on One Indicator**
   - Use at least 2-3 confirming signals
   - Technical analysis increases probability, doesn't guarantee success

6. **Check Daily**
   - Market conditions change
   - Update your analysis regularly

## Keyboard Shortcuts

- Press **F5** or click **"🔄 Refresh Data"** to reload
- Use dropdown for quick stock switching

## Understanding the Data

### Demo Mode Note
Currently using **demo data** (realistic simulated prices). The patterns and indicators work the same as with real data.

### Real Data
When connected to Vietnamese stock APIs, you'll see:
- Actual historical prices
- Real volume data
- Live technical indicators
- Accurate statistics

## Comparison with Other Dashboards

| Feature | Simple Dashboard | Enhanced Dashboard | Historical Dashboard |
|---------|-----------------|-------------------|---------------------|
| Real-time updates | ✅ | ✅ | ✅ |
| Stock picker | ❌ | ✅ | Per stock |
| Price history | ❌ | ❌ | ✅ |
| Technical charts | Basic | Multiple | Advanced |
| Volume analysis | ❌ | ✅ | ✅ Detailed |
| RSI chart | Basic | Line | Full timeline |
| MACD chart | ❌ | ❌ | ✅ |
| Statistics | Basic | ✅ | ✅ Detailed |
| Best for | Quick check | Overview | Deep analysis |

## When to Use This Dashboard

**Use Historical Analysis Dashboard when you:**
- Want to understand price trends over time
- Need to make buy/sell decisions
- Are researching a specific stock
- Want to spot technical patterns
- Need detailed indicator analysis
- Are doing fundamental + technical analysis

**Use Enhanced Dashboard when you:**
- Want to monitor multiple stocks at once
- Need a quick market overview
- Are tracking your watchlist
- Want to compare stocks side-by-side

**Use Simple Dashboard when you:**
- Just need a quick glance
- Want basic information
- Have limited screen space

## Troubleshooting

**Stock not showing in dropdown?**
- Make sure it's in your watchlist
- Add it via Enhanced Dashboard stock picker
- Or use: `python manage_watchlist.py --add SYMBOL`

**Charts not loading?**
- Check browser console for errors
- Refresh the page (F5)
- Make sure server is running

**Old data showing?**
- Click **"🔄 Refresh Data"** button
- Wait for next monitor scan (every 5 minutes)

**Indicators look wrong?**
- This is demo data with realistic patterns
- Real data will show actual market conditions
- Algorithms are the same as professional tools

## Next Steps

1. **Open the dashboard**:
   ```
   http://localhost:8888/dashboard_history.html
   ```

2. **Select a stock** from your watchlist

3. **Analyze the charts** using the guide above

4. **Compare different timeframes** (30/60/90/180 days)

5. **Cross-reference** with Enhanced Dashboard for confirmation

6. **Make informed decisions** based on multiple indicators

## Educational Resources

### Learn Technical Analysis
- **RSI**: Search "How to trade with RSI indicator"
- **MACD**: Search "MACD trading strategy"
- **Moving Averages**: Search "Moving average crossover strategy"
- **Volume Analysis**: Search "Volume price analysis"

### Vietnamese Stock Market
- Check HOSE, HNX, UPCOM websites
- Follow financial news
- Join investor communities

## Disclaimer

⚠️ **IMPORTANT**:
- Technical analysis is NOT a crystal ball
- Past performance does NOT guarantee future results
- Always do your own research
- Only invest money you can afford to lose
- Consult a licensed financial advisor
- This is for educational purposes only

---

Happy analyzing! 📈📊

For questions or issues, check:
- `QUICK_START.md` - General setup
- `FEATURES.md` - All features overview
- `WATCHLIST_GUIDE.md` - Watchlist management
