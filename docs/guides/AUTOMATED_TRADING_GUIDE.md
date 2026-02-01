# 🤖 Automated Trading Guide

## Overview

The Automated Trading system allows you to configure buy/sell rules and let the platform execute trades on your behalf based on technical analysis indicators.

## ⚠️ IMPORTANT WARNINGS

**READ THIS BEFORE ENABLING AUTOMATED TRADING:**

1. **Risk of Loss**: Automated trading can result in significant financial losses. Only trade with money you can afford to lose.

2. **Test First**: ALWAYS run backtests and paper trading before enabling live trading.

3. **Monitor Regularly**: Even with automation, you must monitor your positions and the system's performance.

4. **API Security**: Your broker API keys are sensitive. Keep them secure and never share them.

5. **Not Financial Advice**: This system is for educational purposes. Consult a licensed financial advisor.

6. **Market Conditions**: Automated rules may not adapt well to unusual market conditions.

## Access the System

```
http://localhost:8888/trading_automation.html
```

Or click **"🤖 Automated Trading"** from any dashboard or the homepage.

---

## Features

### 1. **API Configuration**

Connect to your broker's trading API:

- **Supported Brokers**:
  - VNDirect
  - SSI Securities
  - VPS Securities
  - TCBS
  - Custom API

- **Required Information**:
  - API Key (from your broker)
  - API Secret (from your broker)
  - Account Number
  - API Endpoint (if custom)

**How to Get API Keys:**
1. Log in to your broker's website
2. Go to Settings → API/Trading API
3. Generate new API key pair
4. Copy and save securely
5. Enter in the platform

### 2. **Trading Rules**

Configure automated buy/sell conditions:

#### **Rule Format:**
```
[ACTION] IF [CONDITIONS] THEN [EXECUTION]
```

#### **Examples:**

**Buy Rules:**
```
BUY IF RSI < 30 AND Score > 20 THEN 1000 shares
BUY IF Price > MA50 AND MACD > Signal THEN ₫5,000,000
BUY IF MA20 crosses above MA50 THEN 50% of max position
```

**Sell Rules:**
```
SELL IF RSI > 70 OR Profit > 10% THEN 100%
SELL IF Price < MA20 AND Loss > 3% THEN All shares
SELL IF MACD crosses below Signal THEN 50% of position
```

#### **Available Conditions:**

**Price Indicators:**
- `Price > MA20` - Price above 20-day moving average
- `Price < MA50` - Price below 50-day moving average
- `MA20 > MA50` - Golden cross area
- `MA20 < MA50` - Death cross area

**Momentum:**
- `RSI < 30` - Oversold
- `RSI > 70` - Overbought
- `RSI between 40 and 60` - Neutral zone

**MACD:**
- `MACD > Signal` - Bullish
- `MACD < Signal` - Bearish
- `MACD crosses above Signal` - Buy signal
- `MACD crosses below Signal` - Sell signal

**Technical Score:**
- `Score > 40` - Strong buy zone
- `Score < -40` - Strong sell zone
- `Score between -20 and 20` - Neutral

**Position:**
- `Profit > 10%` - Take profit condition
- `Loss > 3%` - Stop loss condition
- `Holding time > 30 days` - Time-based exit

**Logical Operators:**
- `AND` - Both conditions must be true
- `OR` - Either condition must be true
- `NOT` - Condition must be false

#### **Execution Options:**

**Fixed Shares:**
- `1000 shares` - Buy/sell exactly 1000 shares

**Fixed Amount:**
- `₫5,000,000` - Invest exactly 5 million VND

**Percentage:**
- `50%` - Half of max position or current holding
- `100%` - All available or all shares

### 3. **Risk Management**

Critical safety settings:

#### **Position Limits:**
- **Max Position Size**: Maximum investment per trade (e.g., ₫10,000,000)
- **Max Open Positions**: Maximum concurrent holdings (e.g., 5 stocks)

#### **Loss Protection:**
- **Stop Loss %**: Auto-sell if loss exceeds (e.g., 3%)
- **Max Daily Loss %**: Stop all trading if daily loss exceeds (e.g., 5%)

#### **Profit Taking:**
- **Take Profit %**: Auto-sell when profit reaches (e.g., 10%)

#### **Cooldown:**
- **Cooldown Period**: Wait time between trades on same stock (e.g., 15 minutes)

**Recommended Settings:**
```
Max Position Size: ₫10,000,000 (adjust based on capital)
Max Daily Loss: 5%
Stop Loss: 3%
Take Profit: 10%
Max Open Positions: 5
Cooldown Period: 15 minutes
```

### 4. **Backtesting**

Test your rules on historical data BEFORE going live:

#### **How to Backtest:**
1. Configure your trading rules
2. Set risk management parameters
3. Select backtesting period (30/60/90/180/365 days)
4. Click **"▶️ Run Backtest"**
5. Review results

#### **Backtest Metrics:**
- **Total Trades**: Number of trades executed
- **Win Rate**: Percentage of profitable trades
- **Profit/Loss**: Total P&L in VND
- **Sharpe Ratio**: Risk-adjusted return (>1 is good)
- **Max Drawdown**: Largest peak-to-trough decline

#### **What to Look For:**
- Win rate > 55%
- Sharpe ratio > 1.0
- Max drawdown < 20%
- Consistent performance across different periods
- Reasonable number of trades (not too many or too few)

### 5. **Master Trading Switch**

The on/off control for the entire system:

**OFF (Default):**
- Rules are configured but not active
- No trades are executed
- Safe mode for testing and configuration

**ON (Live Trading):**
- Rules are active
- System monitors market every scan
- Trades are executed automatically
- ⚠️ REAL MONEY AT RISK

**Before Enabling:**
1. ✅ API configured and tested
2. ✅ Trading rules added and reviewed
3. ✅ Risk management configured
4. ✅ Backtest completed with good results
5. ✅ You understand the risks

---

## Step-by-Step Setup

### Step 1: Configure API

1. Open: http://localhost:8888/trading_automation.html
2. Select your broker
3. Enter API Key and Secret
4. Enter Account Number
5. Click **"🔍 Test Connection"**
6. Verify connection successful
7. Click **"💾 Save Configuration"**

### Step 2: Add Trading Rules

1. Click **"➕ Add New Rule"**
2. Enter rule in format: `[ACTION] IF [CONDITIONS] THEN [EXECUTION]`
3. Example: `BUY IF RSI < 30 AND Score > 20 THEN 1000 shares`
4. Verify rule is added to list
5. Repeat for all desired rules

**Recommended Starter Rules:**
```
BUY IF RSI < 30 AND Price > MA50 THEN 500 shares
SELL IF RSI > 70 THEN 100%
SELL IF Loss > 3% THEN 100%
SELL IF Profit > 10% THEN 100%
```

### Step 3: Set Risk Management

1. Set **Max Position Size**: ₫10,000,000
2. Set **Max Daily Loss**: 5%
3. Set **Stop Loss**: 3%
4. Set **Take Profit**: 10%
5. Set **Max Open Positions**: 5
6. Set **Cooldown Period**: 15 minutes
7. Click **"💾 Save Risk Settings"**

### Step 4: Backtest Your Strategy

1. Select backtesting period: 60 days
2. Click **"▶️ Run Backtest"**
3. Wait for results
4. Review metrics:
   - Is win rate > 55%?
   - Is Sharpe ratio > 1.0?
   - Is max drawdown acceptable?
5. If good, proceed. If not, adjust rules and retest.

### Step 5: Paper Trading (Recommended)

Before live trading, test with paper trading:
1. Keep master switch OFF
2. Monitor what trades WOULD have been made
3. Track paper performance for 1-2 weeks
4. Verify system works as expected

### Step 6: Enable Live Trading

**Final Checklist:**
- [ ] API tested and working
- [ ] Rules configured and reviewed
- [ ] Risk management set
- [ ] Backtest shows positive results
- [ ] Paper trading completed
- [ ] I understand I can lose money
- [ ] I'm ready to monitor the system

**If all checked:**
1. Toggle **Master Trading Switch** to ON
2. Confirm the warning
3. System is now LIVE
4. Monitor regularly

---

## How It Works

### Monitoring Cycle

```
Every 5 minutes:
1. Monitor scans stocks (already running)
2. Technical analysis calculated
3. Automation system checks rules
4. If conditions met → Execute trade
5. Record trade in log
6. Update positions
7. Check risk limits
```

### Trade Execution Flow

```
1. Rule condition triggers
   ↓
2. Check risk limits (position size, daily loss, etc.)
   ↓
3. If OK → Prepare order
   ↓
4. Send order to broker API
   ↓
5. Receive confirmation
   ↓
6. Log trade
   ↓
7. Update positions
   ↓
8. Apply cooldown period
```

### Risk Protection

The system has multiple safety layers:

1. **Pre-Trade Checks:**
   - Is trading enabled?
   - Is API connected?
   - Within position limits?
   - Within daily loss limit?
   - Cooldown period passed?

2. **During Trade:**
   - Order validation
   - Price checks
   - Quantity checks

3. **Post-Trade:**
   - Stop loss monitoring
   - Take profit monitoring
   - Portfolio rebalancing

---

## Trading Scenarios

### Scenario 1: Oversold Buy

**Setup:**
```
Rule: BUY IF RSI < 30 AND Score > 20 THEN 1000 shares
Risk: Stop Loss 3%, Take Profit 10%
```

**What Happens:**
1. Monitor detects VCB with RSI 28, Score 35
2. Conditions met → Trigger buy rule
3. Check: Position size OK? Daily loss OK? → YES
4. Execute: Buy 1000 VCB shares
5. Monitor position with 3% stop loss, 10% take profit
6. Apply 15-minute cooldown on VCB

### Scenario 2: Overbought Sell

**Setup:**
```
Rule: SELL IF RSI > 70 THEN 100%
```

**What Happens:**
1. You hold 1000 HPG shares
2. Monitor detects HPG RSI = 72
3. Conditions met → Trigger sell rule
4. Execute: Sell all 1000 HPG shares
5. Lock in profit/loss
6. Free up capital for new opportunities

### Scenario 3: Stop Loss Protection

**Setup:**
```
Risk Management: Stop Loss 3%
```

**What Happens:**
1. You buy FPT at ₫100,000/share
2. Price drops to ₫97,000 (3% loss)
3. Stop loss triggered automatically
4. System sells entire position
5. Loss limited to 3%
6. Capital preserved for better opportunities

---

## Best Practices

### 1. Start Small
- Test with small position sizes first
- Increase gradually as you gain confidence
- Don't risk more than 2-5% per trade

### 2. Diversify Rules
- Have multiple rule types (RSI, MACD, MA)
- Don't rely on a single indicator
- Balance buy and sell rules

### 3. Monitor Daily
- Check trade log every day
- Review performance weekly
- Adjust rules based on results

### 4. Keep Learning
- Study successful trades
- Analyze losing trades
- Refine your strategy over time

### 5. Respect Risk Limits
- NEVER disable stop losses
- NEVER exceed position limits
- NEVER chase losses

### 6. Stay Informed
- Market news affects automation
- Disable during major events
- Be ready to intervene manually

---

## Troubleshooting

### API Connection Failed
**Problem**: Can't connect to broker API

**Solutions**:
1. Check API key is correct
2. Verify API secret is correct
3. Check account number
4. Ensure API is enabled in broker settings
5. Check internet connection

### Rules Not Triggering
**Problem**: Conditions met but no trade executed

**Solutions**:
1. Verify master switch is ON
2. Check API connection
3. Review risk limits (may be hit)
4. Check cooldown period
5. Verify rule syntax is correct

### Unexpected Trades
**Problem**: System made a trade you didn't expect

**Solutions**:
1. Review trade log to see which rule triggered
2. Check rule conditions carefully
3. May need to refine rule logic
4. Consider adding more conditions

### System Stopped Trading
**Problem**: No trades happening

**Possible Reasons**:
1. Daily loss limit reached (safety feature)
2. Max positions reached
3. All stocks in cooldown
4. Market conditions don't match any rules
5. API connection lost

**Actions**:
1. Check system status
2. Review risk limits
3. Test API connection
4. Check trade log for errors

---

## FAQ

**Q: Can I modify rules while trading is enabled?**
A: Yes, but changes take effect on next scan. Be careful.

**Q: What if I lose internet connection?**
A: System stops executing new trades. Existing positions remain.

**Q: Can I override automated decisions manually?**
A: Yes, you can always trade manually in your broker platform.

**Q: How much does API trading cost?**
A: Check with your broker. Some charge per API call or have monthly fees.

**Q: Can I use multiple brokers?**
A: Not simultaneously in current version. Pick one.

**Q: What's the minimum capital needed?**
A: Depends on your broker's minimum order size. Recommend ≥₫50,000,000.

**Q: Can I copy someone else's rules?**
A: Yes, but always backtest first. What works for others may not work for you.

**Q: Is this legal?**
A: Yes, using broker APIs for automated trading is legal. Check your broker's terms.

---

## Advanced Topics

### Custom Indicators

You can reference any technical indicator the system calculates:
- RSI (14-period)
- MA20, MA50 (moving averages)
- EMA12, EMA26 (exponential moving averages)
- MACD, Signal, Histogram
- Technical Score (-100 to +100)
- Volume
- Price High/Low
- Bollinger Bands (if implemented)

### Complex Rules

Combine multiple conditions with logic:

```
BUY IF (RSI < 30 OR Score > 40) AND MA20 > MA50 AND Volume > AvgVolume THEN ₫10,000,000
```

### Dynamic Position Sizing

Adjust size based on confidence:

```
BUY IF Score > 60 THEN ₫20,000,000
BUY IF Score > 40 THEN ₫10,000,000
BUY IF Score > 20 THEN ₫5,000,000
```

### Time-Based Rules

Add time conditions:

```
SELL IF Holding time > 30 days AND Profit > 0 THEN 100%
```

---

## Security & Privacy

### API Key Storage
- Keys encrypted before storage
- Never transmitted in plain text
- Stored locally on your machine
- Not shared with third parties

### Data Security
- All trading data stays local
- No external analytics/tracking
- Your strategies are private
- You control everything

### Best Practices
1. Use API keys with trading-only permissions
2. Don't share your API keys
3. Rotate keys periodically
4. Revoke keys if compromised
5. Use strong passwords

---

## Support & Resources

### Documentation
- `QUICK_START.md` - Getting started
- `FEATURES.md` - All features
- `HISTORICAL_ANALYSIS_GUIDE.md` - Technical analysis
- `WATCHLIST_GUIDE.md` - Stock selection

### Getting Help
1. Review this guide thoroughly
2. Check FAQ section
3. Review trade logs for clues
4. Test in backtesting mode
5. Start with conservative settings

---

## Disclaimer

⚠️ **IMPORTANT LEGAL NOTICE**:

This automated trading system is provided **AS-IS** for educational and informational purposes only.

- **Not Financial Advice**: Nothing here constitutes financial, investment, or trading advice.
- **No Guarantees**: Past performance does not guarantee future results.
- **Risk of Loss**: You can lose money trading stocks. Only trade with money you can afford to lose.
- **Your Responsibility**: All trading decisions and outcomes are your sole responsibility.
- **No Liability**: The creators assume no liability for any losses incurred.
- **Professional Advice**: Consult a licensed financial advisor before trading.
- **Legal Compliance**: Ensure compliance with all applicable laws and regulations.
- **Broker Terms**: Follow your broker's terms of service for API usage.

**BY USING THIS SYSTEM, YOU ACKNOWLEDGE AND ACCEPT ALL RISKS.**

---

**Happy Trading! 🤖📈💰**

*Remember: The best traders combine automated systems with human judgment. Stay informed, stay cautious, and trade responsibly.*
