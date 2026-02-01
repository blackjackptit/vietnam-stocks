# 📖 Advanced User Guide - Vietnamese Stock Platform

## Table of Contents

1. [Getting Started](#getting-started)
2. [Portfolio Management](#portfolio-management)
3. [Strategy Development](#strategy-development)
4. [Risk Analysis](#risk-analysis)
5. [Price Alerts](#price-alerts)
6. [Advanced Techniques](#advanced-techniques)
7. [Best Practices](#best-practices)

---

## Getting Started

### Quick Access
Visit: `http://localhost:8888/index.html`

### Available Dashboards
1. **Enhanced Dashboard** - Visual monitoring
2. **Historical Analysis** - Deep dive analysis
3. **Price Forecast** - AI predictions
4. **Advanced Analytics** - Professional tools (NEW!)
5. **Price Alerts** - Monitoring system (NEW!)

---

## Portfolio Management

### Building Your First Portfolio

**Step 1: Access Portfolio Analytics**
```
Navigate to: Dashboard > Advanced Analytics > Portfolio Analytics
```

**Step 2: Select Stocks**
1. Choose 8-15 stocks from different sectors
2. Hold Ctrl/Cmd to select multiple
3. Ensure diversification:
   - 2-3 Blue Chips (stability)
   - 2-3 Banks (dividends)
   - 2-3 Tech stocks (growth)
   - 1-2 Commodities (hedge)

**Step 3: Analyze Metrics**
Review the calculated metrics:
- **Expected Return**: Target 10-15% annually
- **Sharpe Ratio**: Aim for > 1.0
- **Max Drawdown**: Keep under -20%
- **Diversification**: Target > 80%

**Step 4: Optimize**
- If Sharpe < 1.0: Add safer stocks
- If Drawdown > -20%: Reduce volatile stocks
- If Diversification < 70%: Add uncorrelated stocks

### Example Good Portfolio

```
Blue Chips (30%):
- VCB: 10%
- VNM: 10%
- GAS: 10%

Growth Stocks (40%):
- FPT: 15%
- VHM: 15%
- MWG: 10%

Defensive (20%):
- SAB: 10%
- MSN: 10%

Commodities (10%):
- GOLD: 10%
```

**Expected Metrics:**
- Return: 12-14%
- Sharpe: 1.2-1.5
- Max DD: -15% to -18%
- Diversification: 85%+

---

## Strategy Development

### Backtesting Your Strategy

**Step 1: Choose a Strategy**
Navigate to: Advanced Analytics > Backtesting

**Available Strategies:**
1. **SMA Crossover (20/50)** - Best for trending markets
2. **RSI Oversold/Overbought** - Best for range-bound markets
3. **MACD Signal** - Best for momentum trading
4. **Bollinger Breakout** - Best for volatility breakouts

**Step 2: Select Test Stock**
Pick a liquid stock with good history:
- Blue chips: VCB, HPG, FPT
- High volume: MWG, MSN, VHM

**Step 3: Run Backtest**
Click "Run Backtest" and review:

**Good Results:**
- Total Return > 15%
- Win Rate > 55%
- Avg Trade > 1%
- < 30 trades per year

**Poor Results:**
- Total Return < 5%
- Win Rate < 45%
- Avg Trade < 0.5%
- > 100 trades per year

**Step 4: Compare to Buy & Hold**
- Strategy should beat buy-and-hold
- Consider transaction costs
- Check consistency across different stocks

### Strategy Optimization Tips

**For SMA Crossover:**
- Works best in trending markets
- Reduce trades by using longer periods
- Combine with trend filter

**For RSI:**
- Oversold < 30, Overbought > 70
- Add confirmation (volume spike)
- Use in sideways markets

**For MACD:**
- Fast crossovers for active trading
- Slow crossovers for fewer trades
- Combine with price action

**For Bollinger:**
- Wait for strong breakout
- Confirm with volume
- Use with volatility filter

---

## Risk Analysis

### Calculating Portfolio Risk

**Step 1: Select Your Stocks**
Navigate to: Advanced Analytics > Risk Management

**Step 2: Review Metrics**

**Value at Risk (VaR)**
- Shows maximum expected loss at 95% confidence
- Example: VaR = -8.5%
  - Meaning: 95% chance you won't lose more than 8.5%
  - 5% chance you might lose more

**What's Good?**
- VaR < -8%: Low risk ✅
- VaR -8% to -12%: Medium risk ⚠️
- VaR > -12%: High risk ❌

**Conditional VaR (CVaR)**
- Average loss in worst 5% scenarios
- Always worse than VaR
- Better measure of tail risk

**Beta**
- Measures volatility vs market
- Beta = 1.0: Same as market
- Beta > 1.0: More volatile
- Beta < 1.0: Less volatile

**Step 3: Risk Grading**

Review each stock's risk grade:

**Low Risk (Good for core holdings):**
- Beta < 0.8
- VaR < -8%
- Volatility < 20%
- Examples: VCB, VNM, SAB

**Medium Risk (Good for growth):**
- Beta 0.8-1.2
- VaR -8% to -12%
- Volatility 20-30%
- Examples: FPT, MWG, HPG

**High Risk (Small positions only):**
- Beta > 1.2
- VaR > -12%
- Volatility > 30%
- Examples: Small caps, commodities

### Portfolio Risk Management Rules

1. **Diversification**:
   - Minimum 8 stocks
   - Maximum 15 stocks
   - Max 15% per position

2. **Sector Allocation**:
   - Max 30% per sector
   - At least 3 sectors
   - Include defensive stocks

3. **Risk Limits**:
   - Portfolio VaR < -10%
   - Average Beta 0.8-1.2
   - Max drawdown tolerance: -20%

4. **Rebalancing**:
   - Quarterly review
   - Rebalance if position > 20%
   - Trim winners, add to losers

---

## Price Alerts

### Setting Up Effective Alerts

**Step 1: Access Alerts System**
Navigate to: `alerts_system.html`

**Step 2: Choose Alert Type**

**Price Alerts:**
```
Use for:
- Buy orders: "Price Below" target entry
- Sell orders: "Price Above" target exit
- Stop loss: "Price Below" protection level
```

**Example:**
```
Stock: VCB
Type: Price Below
Value: 85000
Action: Buy signal when undervalued
```

**Change % Alerts:**
```
Use for:
- Breakout detection: "Change Above" 3-5%
- Crash warnings: "Change Below" -3 to -5%
- Volatility spikes
```

**Example:**
```
Stock: FPT
Type: Change Above
Value: 5
Action: Momentum breakout signal
```

**Volume Spike Alerts:**
```
Use for:
- Unusual activity detection
- Institutional buying
- News-driven moves
```

**RSI Alerts:**
```
Use for:
- Oversold: Buy opportunity
- Overbought: Sell signal
- Trend exhaustion
```

**Example:**
```
Stock: HPG
Type: RSI Oversold
Action: Buy when RSI < 30
```

### Alert Strategy Examples

**Day Trading Setup:**
```
1. VCB - Change Above 2%
2. VCB - Change Below -2%
3. VCB - Volume Spike
```

**Swing Trading Setup:**
```
1. FPT - Price Below 110000 (buy)
2. FPT - Price Above 130000 (sell)
3. FPT - RSI Oversold
```

**Long-Term Investing:**
```
1. VNM - Price Below 75000 (accumulate)
2. VNM - Price Above 95000 (consider selling)
3. VNM - Change Below -5% (crisis opportunity)
```

**Watchlist Monitoring:**
```
Set alerts for top 10 stocks:
- Price: ±10% from current
- RSI: Oversold/Overbought
- Change: ±5% moves
```

---

## Advanced Techniques

### 1. Pattern Recognition Trading

**Setup:**
1. Navigate to Advanced Analytics > Pattern Recognition
2. Select your target stock
3. Click "Detect Patterns"

**Trading Patterns:**

**Bullish Patterns (Buy Signals):**
- Ascending Triangle
- Cup and Handle
- Double Bottom
- Bullish Engulfing
- Hammer

**Action:** Buy when pattern completes with volume

**Bearish Patterns (Sell Signals):**
- Descending Triangle
- Head and Shoulders
- Double Top
- Bearish Engulfing
- Shooting Star

**Action:** Sell or avoid when pattern forms

**Pattern Trading Rules:**
1. Only trade high confidence (>80%)
2. Confirm with volume
3. Set stop loss below support
4. Target next resistance level

### 2. Correlation Analysis for Diversification

**Setup:**
1. Navigate to Advanced Analytics > Correlation Analysis
2. Select 10-15 stocks
3. Click "Analyze Correlations"

**Reading the Matrix:**

**High Positive Correlation (+0.7 to +1.0):**
- Stocks move together
- Don't provide diversification
- Example: VCB and TCB (both banks)

**Action:** Avoid multiple highly correlated stocks

**Low Correlation (-0.3 to +0.3):**
- Stocks move independently
- Great for diversification
- Example: FPT (tech) and SAB (consumer)

**Action:** Build portfolio with low correlations

**Negative Correlation (-0.7 to -1.0):**
- Stocks move opposite
- Natural hedge
- Example: GOLD and equities in crisis

**Action:** Use for hedging

**Diversification Strategy:**
```
1. Find 10 stocks with correlations < 0.5
2. Equal weight each position (10%)
3. Review monthly
4. Replace highly correlated stocks
```

### 3. ML Forecasting for Entry/Exit

**Setup:**
1. Navigate to Advanced Analytics > Machine Learning
2. Select stock
3. Choose horizon (30 days recommended)
4. Click "Generate ML Forecast"

**Interpreting Results:**

**High Confidence (>80%):**
- Strong signal
- High model accuracy
- Trade with conviction

**Medium Confidence (60-80%):**
- Moderate signal
- Use with other indicators
- Reduce position size

**Low Confidence (<60%):**
- Weak signal
- Avoid trading
- Wait for better setup

**Trading Rules:**
```
Upward Trend + Confidence >75%:
→ BUY signal

Downward Trend + Confidence >75%:
→ SELL signal

Unclear Trend or Confidence <60%:
→ HOLD / No trade
```

**Feature Importance:**
Look at which features matter:
- If Price/Volume dominant: Momentum-driven
- If RSI/MACD dominant: Technical-driven
- If all balanced: Complex patterns

### 4. Risk-Adjusted Portfolio Construction

**Goal:** Maximize Sharpe Ratio

**Steps:**
1. Start with 10 candidate stocks
2. Check correlations (want < 0.5)
3. Calculate individual Sharpe ratios
4. Build portfolio with top 5-8 stocks
5. Adjust weights for optimal Sharpe

**Target Allocation:**
```
High Sharpe (>1.5): 15-20% each
Medium Sharpe (1.0-1.5): 10-15% each
Low Sharpe (<1.0): 5-10% each
```

**Efficient Frontier:**
- Find optimal risk/return point
- Current portfolio should be on/near frontier
- Move up frontier for higher returns
- Move left for lower risk

---

## Best Practices

### Daily Routine

**Morning (9:00 AM):**
```
1. Check alerts (5 min)
2. Review Enhanced Dashboard heatmap (5 min)
3. Read triggered alerts (5 min)
4. Update watchlist if needed (5 min)
```

**Mid-Day (12:00 PM):**
```
1. Check major movers (3 min)
2. Review positions vs targets (5 min)
3. Adjust stop losses if needed (5 min)
```

**Evening (6:00 PM):**
```
1. Full portfolio review (10 min)
2. Analyze day's patterns (10 min)
3. Plan tomorrow's trades (10 min)
4. Update alerts as needed (5 min)
```

### Weekly Routine

**Monday:**
- Review last week's performance
- Check all alert triggers
- Update watchlist

**Wednesday:**
- Analyze mid-week trends
- Review ML forecasts
- Check pattern signals

**Friday:**
- Portfolio risk review
- Rebalance if needed
- Set weekend alerts

### Monthly Routine

**First Week:**
- Full portfolio audit
- Risk metrics review
- Correlation analysis
- Performance report

**Second Week:**
- Strategy backtesting
- ML forecast refresh
- Alert optimization

**Third Week:**
- Pattern analysis
- Sector rotation review
- Diversification check

**Fourth Week:**
- Rebalancing execution
- Tax loss harvesting (if applicable)
- Next month planning

### Risk Management Checklist

**Before Every Trade:**
- [ ] Position size < 15%
- [ ] Stop loss set
- [ ] Take profit target defined
- [ ] Risk/reward > 2:1
- [ ] Fits portfolio strategy

**Portfolio Level:**
- [ ] VaR < -10%
- [ ] Sharpe > 1.0
- [ ] Max drawdown < -20%
- [ ] Diversification > 80%
- [ ] At least 8 positions

**Regular Reviews:**
- [ ] Daily: Alerts check
- [ ] Weekly: Performance review
- [ ] Monthly: Full audit
- [ ] Quarterly: Rebalancing
- [ ] Annually: Strategy review

---

## Common Mistakes to Avoid

### 1. Over-Trading
❌ Trading every signal
✅ Trade only high-confidence setups

### 2. Ignoring Risk
❌ No stop losses
✅ Always protect capital

### 3. Poor Diversification
❌ All tech stocks
✅ Multiple sectors, low correlation

### 4. Emotional Trading
❌ Panic selling, FOMO buying
✅ Follow your system

### 5. No Strategy
❌ Random buying
✅ Backtest before trading

### 6. Over-Leveraging
❌ Too much in single position
✅ Max 15% per stock

### 7. Ignoring Fees
❌ Day trading without considering costs
✅ Account for commissions

### 8. No Record Keeping
❌ No trade journal
✅ Track every trade

---

## Success Tips

### For Beginners
1. Start with demo mode
2. Paper trade for 3 months
3. Start small (< 10% real money)
4. Focus on blue chips
5. Use simple strategies

### For Intermediate
1. Develop your system
2. Backtest thoroughly
3. Keep detailed records
4. Diversify properly
5. Manage risk actively

### For Advanced
1. Optimize strategies
2. Use ML forecasting
3. Advanced risk management
4. Portfolio optimization
5. Systematic approach

---

## Troubleshooting

### Problem: Alerts Not Triggering
**Solution:**
- Check browser allows notifications
- Ensure tab stays open
- Verify alert conditions are correct
- Check internet connection

### Problem: Slow Performance
**Solution:**
- Reduce number of stocks
- Clear browser cache
- Close unused tabs
- Check server load

### Problem: Inaccurate Forecasts
**Solution:**
- Use longer historical period
- Combine multiple models
- Add confirmation indicators
- Remember: No model is perfect

### Problem: High Portfolio Risk
**Solution:**
- Add more stocks (10-15)
- Reduce volatile positions
- Add defensive stocks
- Increase commodities allocation

---

## Summary

**To become a successful investor using this platform:**

1. **Learn the Tools**: Understand each feature
2. **Develop a Strategy**: Backtest before trading
3. **Manage Risk**: Use VaR, stop losses, diversification
4. **Stay Disciplined**: Follow your system
5. **Keep Learning**: Markets always change

**Key Metrics to Watch:**
- Portfolio Sharpe Ratio: > 1.0
- Max Drawdown: < -20%
- Win Rate: > 55%
- Diversification: > 80%

**Remember:**
- Start small
- Be patient
- Never risk more than you can lose
- This is a marathon, not a sprint

**Happy Investing! 📈💰🚀**
