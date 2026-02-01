# Quick Start Guide - Vietnamese Stock Monitor

Get started in 5 minutes!

## Installation

```bash
cd ~/projects/vietnam-stocks
pip install -r requirements.txt
```

## Test the Tool

### 1. Check Available Stocks

```bash
python monitor.py --list-stocks
```

You'll see stock categories like `blue_chips`, `banks`, `tech`, `affordable`, etc.

### 2. Run Your First Scan

```bash
python monitor.py --scan-once --watchlist "VPB,FPT,STB"
```

This will:
- ✅ Fetch real-time prices from VNDirect API
- ✅ Calculate RSI, MACD, Moving Averages
- ✅ Provide BUY/SELL recommendations
- ✅ Suggest how to invest 10M VND

**Expected Output:**
```
==========================================
STOCK SCAN - 2025-01-30 15:30:00
==========================================

Analyzing VPB...
  Price: 23,500 VND (+2.50%)
  🟢 Recommendation: BUY (Score: 25)
  RSI: 45.2
  🟢 Price above MA20 and MA50 (bullish)

==========================================
💰 INVESTMENT SUGGESTION FOR 10M VND
==========================================

  VPB
    Price: 23,500 VND
    Buy: 85 shares
    Cost: 2,004,763 VND
    Reason: BUY (Score: 25)
...
```

### 3. Start Continuous Monitoring

```bash
python monitor.py --interval 15
```

The tool will scan every 15 minutes and log results.

Press `Ctrl+C` to stop.

## Common Use Cases

### Monitor Affordable Stocks (Default)

Perfect for 10M VND budget:

```bash
python monitor.py --scan-once
```

Monitors: VPB, STB, HDB, SHB, MBB, ACB, FPT, POW, DGC, GEX

### Monitor Blue Chips

```bash
python monitor.py --scan-once --watchlist blue_chips
```

Monitors: VCB, VHM, VIC, VNM, HPG, GAS, MSN, TCB, VPB, MBB

### Monitor Tech Stocks

```bash
python monitor.py --scan-once --watchlist tech
```

Monitors: FPT, CMG, VGI, SAM, ITD, ELC, SGT, ICT, DGW, CTR

### Custom Watchlist

```bash
python monitor.py --scan-once --watchlist "FPT,VNM,HPG,VCB"
```

### Different Budget

```bash
python monitor.py --scan-once --budget 20000000  # 20M VND
```

## Understanding Results

### Recommendations

| Symbol | Meaning |
|--------|---------|
| 🟢🟢 | **STRONG BUY** - Multiple bullish signals |
| 🟢 | **BUY** - Bullish trend detected |
| ⚪ | **HOLD** - Mixed/neutral signals |
| 🔴 | **SELL** - Bearish trend |
| 🔴🔴 | **STRONG SELL** - Multiple bearish signals |

### Key Indicators

**RSI (Relative Strength Index)**
- Below 30: Oversold → Potential buy
- 30-70: Normal range
- Above 70: Overbought → Potential sell

**Moving Averages**
- Price > MA20 > MA50: Strong uptrend 📈
- Price < MA20 < MA50: Strong downtrend 📉

**Score System**
- 40+: Strong buy territory
- 20-40: Buy zone
- -20 to 20: Neutral
- Below -20: Sell zone

## Files Generated

### Logs
```
logs/monitor_20250130.log
```
Contains timestamped monitoring activity.

### Scan Results
```
output/scan_20250130_153000.json
```
JSON file with complete analysis data.

### Portfolio
```
data/portfolio.json
```
Your holdings and transactions (created after you simulate buying).

## Troubleshooting

### API Connection Issues

If you see "Could not fetch data" errors:

**Issue:** VNDirect API may be blocked or down

**Solutions:**
1. Check internet connection
2. Try again in a few minutes (rate limiting)
3. VNDirect API might require Vietnam IP address

**Alternative:** Use VPN with Vietnam server or try from Vietnam network.

### No Recommendations

If no stocks show BUY signals:
- Market might be overbought
- Try different watchlist
- Check individual stock details in logs

### Permission Denied

```bash
chmod +x monitor.py
```

## Next Steps

1. **Learn Technical Analysis** - Understand RSI, MACD, Bollinger Bands
2. **Paper Trading** - Test strategies without real money
3. **Open Brokerage Account** - SSI, VNDirect, TCBS, etc.
4. **Start Small** - Begin with 1-2 stocks
5. **Set Stop-Loss** - Protect against big losses (-10% to -15%)

## Safety Tips

⚠️ **Before You Invest:**

1. **This is NOT financial advice** - Tool is educational only
2. **Do your research** - Read company reports, financial news
3. **Diversify** - Don't put all money in one stock
4. **Use stop-loss** - Set exit points before buying
5. **Think long-term** - Don't panic sell on red days
6. **Only invest what you can afford to lose**

## Example Investment Strategy (10M VND)

Based on tool recommendations:

1. **Select 5 stocks** with BUY or STRONG BUY ratings
2. **Allocate 2M VND each** (20% per stock)
3. **Set stop-loss** at -10% for each
4. **Review weekly** using the monitor
5. **Rebalance monthly** based on new signals

## Getting Help

### View Full Documentation
```bash
cat README.md
```

### Check Logs
```bash
tail -f logs/monitor_$(date +%Y%m%d).log
```

### Test Individual Modules

```bash
# Test data fetcher
python src/stock_data.py

# Test technical analysis
python src/technical_analysis.py

# Test portfolio
python src/portfolio.py
```

## Advanced: Continuous Monitoring

Run the monitor as a background service:

```bash
# Start monitoring in background
nohup python monitor.py --interval 15 > monitor.out 2>&1 &

# Check if running
ps aux | grep monitor.py

# Stop monitoring
pkill -f monitor.py
```

## What Makes This Tool Useful?

✅ **Free & Open Source** - No subscription fees
✅ **Real-time Data** - From VNDirect API
✅ **Technical Analysis** - RSI, MACD, MA, Bollinger Bands
✅ **Automated Scanning** - Set and forget
✅ **Budget-Aware** - Optimized for 10M VND
✅ **Actionable Advice** - Specific buy recommendations
✅ **Risk Management** - Shows when to avoid stocks

---

**Ready to start monitoring?**

```bash
python monitor.py --scan-once
```

Good luck and invest wisely! 📊💰
