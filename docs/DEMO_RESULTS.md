# Demo Scan Results - What You Just Saw

## Summary

The tool successfully scanned **10 affordable Vietnamese stocks** and provided:

### 🟢 BUY Recommendations
- **MBB** (Military Bank): 26,040 VND
  - Score: 35 (Bullish)
  - RSI: 16.4 (Oversold - good buying opportunity)
  - MA20 > MA50 (Golden cross - uptrend)
  - **Evidence:** RSI below 30 indicates oversold condition, historically good entry point

### Investment Allocation (10M VND Budget)
```
Stock: MBB
Price: 26,040 VND
Shares to buy: 383
Total cost: 9,988,280 VND
Remaining: 11,720 VND
```

### ⚪ HOLD Recommendations
- **VPB** (25 score), **HDB** (15 score), **POW** (15 score), **DGC** (20 score)
- **ACB**, **FPT**, **STB**, **GEX**

### 🔴 SELL/AVOID
- **SHB** (-35 score): Death cross, bearish trend
- **FPT** (-35 score): Below moving averages, MACD bearish

## Technical Evidence Explained

### Why MBB Got "BUY" Rating

1. **RSI = 16.4** (Oversold)
   - Below 30 = oversold territory
   - Historically means price has dropped too much
   - Often bounces back up

2. **Golden Cross Pattern**
   - MA20 above MA50
   - Indicates upward trend momentum
   - Bullish signal

3. **Score = 35** (Buy Zone)
   - Calculated from multiple indicators
   - 20-40 = Buy territory
   - 40+ = Strong Buy

### Indicators Breakdown

| Indicator | What It Measures | Bullish Signal | Bearish Signal |
|-----------|------------------|----------------|----------------|
| **RSI** | Overbought/Oversold | < 30 | > 70 |
| **MA20/MA50** | Trend direction | Price > MA20 > MA50 | Price < MA20 < MA50 |
| **MACD** | Momentum | Positive histogram | Negative histogram |
| **Bollinger Bands** | Volatility | Near lower band | Near upper band |

## What This Means for Your 10M VND

Based on this scan:

### Conservative Strategy (Lower Risk)
```
Diversify across 3-5 stocks:
- MBB: 3M VND (120 shares)
- VPB: 2M VND (85 shares)  
- HDB: 2M VND (110 shares)
- POW: 2M VND (180 shares)
- Cash: 1M VND (emergency reserve)
```

### Aggressive Strategy (Higher Risk)
```
Concentrate on top pick:
- MBB: 9M VND (345 shares)
- Cash: 1M VND (for averaging down)
```

### Recommended: Moderate Strategy
```
- MBB: 4M VND (153 shares) - Top pick
- VPB: 3M VND (125 shares) - Good score
- HDB: 2M VND (110 shares) - Stable bank
- Cash: 1M VND - Wait for better opportunities
```

## Real-World Application

### If This Was Real Data:

**Step 1:** Open brokerage account (SSI, VNDirect, TCBS)

**Step 2:** Transfer 10M VND to trading account

**Step 3:** Place limit orders:
```
Buy MBB at 26,040 VND (or lower)
Quantity: 153 shares
Total: ~4M VND
```

**Step 4:** Set stop-loss:
```
If MBB drops to 23,436 VND (-10%), sell automatically
This limits loss to 400K VND
```

**Step 5:** Monitor daily with this tool:
```bash
python demo_monitor.py --scan-once
```

**Step 6:** Review weekly, adjust based on new signals

## Understanding the Scoring System

### How Score is Calculated:

```python
Starting score: 0

Bullish signals (add points):
+ RSI < 30 (oversold): +20
+ Price > MA20 > MA50: +15
+ MA20 > MA50 (golden cross): +10
+ MACD positive: +10
+ Near lower Bollinger Band: +15
+ High volume: +5

Bearish signals (subtract points):
- RSI > 70 (overbought): -20
- Price < MA20 < MA50: -15
- MA20 < MA50 (death cross): -10
- MACD negative: -10
- Near upper Bollinger Band: -15

Final score range: -100 to +100
```

### Score Interpretation:

| Score Range | Recommendation | Action |
|-------------|----------------|--------|
| 40+ | STRONG BUY 🟢🟢 | High confidence buy |
| 20-40 | BUY 🟢 | Good entry point |
| -20 to 20 | HOLD ⚪ | Wait and watch |
| -40 to -20 | SELL 🔴 | Consider exiting |
| < -40 | STRONG SELL 🔴🔴 | Exit position |

## Files Generated

### 1. Log File
```
logs/monitor_20260131.log
```
Contains timestamped analysis of each stock.

### 2. JSON Results
```
output/scan_20260131_001647.json
```
Complete data in JSON format for further analysis.

### 3. Portfolio File
```
data/portfolio.json
```
(Created when you simulate buying/selling)

## Next Steps

### Option A: Learn More (Recommended First)
```bash
# Run more demo scans
python demo_monitor.py --scan-once --watchlist "VCB,FPT,VNM,HPG"
python demo_monitor.py --scan-once --watchlist blue_chips
python demo_monitor.py --scan-once --watchlist tech
```

### Option B: Set Up Real Data
1. Get VPN with Vietnam server
2. Connect to Vietnam
3. Run: `python monitor.py --scan-once`
4. See real market recommendations

### Option C: Paper Trading
1. Track demo recommendations
2. Pretend to buy/sell
3. Record results
4. Learn from mistakes (no real money lost)

## Important Disclaimers

⚠️ **This Demo Used Simulated Data**
- Prices are realistic but not real
- Technical indicators are correctly calculated
- Recommendations follow same logic as real data
- DO NOT trade based on demo data

⚠️ **When Using Real Data**
- Always verify recommendations manually
- Check company fundamentals
- Read recent news
- Set stop-loss limits
- Only invest what you can afford to lose

⚠️ **No Guarantees**
- Past performance ≠ future results
- Technical analysis isn't perfect
- Markets are unpredictable
- You may lose money

## Questions & Answers

**Q: Why did MBB get BUY recommendation?**
A: RSI = 16.4 (oversold), Golden Cross pattern, positive technical signals

**Q: Should I buy MBB now?**
A: This is demo data. For real trading, check actual current price, company news, and financial reports.

**Q: How often should I run scans?**
A: Every 15 minutes during trading hours (9AM-3PM Vietnam time)

**Q: Can I trust these recommendations?**
A: Use as one input among many. Always do your own research.

**Q: What if a BUY stock goes down?**
A: Set stop-loss at -10%. If it drops 10%, sell automatically to limit losses.

**Q: How long should I hold?**
A: Minimum 1-3 months for technical trading. Check fundamentals for long-term.

## Real Success Factors

Technical analysis is just 30% of success:

1. **Technical Analysis** (30%) - What this tool does
2. **Fundamental Analysis** (30%) - Company financials, P/E ratio, earnings
3. **Market Sentiment** (20%) - News, economic conditions
4. **Risk Management** (20%) - Stop-loss, position sizing, diversification

**Use this tool for #1, but learn #2, #3, and #4 too!**

---

**Ready for next scan?**

```bash
python demo_monitor.py --scan-once --watchlist blue_chips
```

Or read the full guide:
```bash
cat README.md
cat HOW_TO_USE_WITH_REAL_DATA.md
```
