# Vietnamese Stock Monitor & Analyzer

**Automated stock monitoring and technical analysis tool for Vietnamese stock markets (HSX, HNX, UPCOM)**

⚠️ **IMPORTANT: This is NOT financial advice. For educational purposes only.**

## Features

- 📊 **Real-time Stock Data** - Fetch live prices from VNDirect API
- 📈 **Technical Analysis** - RSI, MACD, Moving Averages, Bollinger Bands
- 💰 **Portfolio Management** - Track holdings, P&L, and budget
- 🔔 **Automated Monitoring** - Scan stocks every 15 minutes
- 🎯 **Buy Recommendations** - Algorithmic scoring and suggestions
- 💵 **Budget Allocation** - Smart allocation for 10M VND budget

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run a Single Scan

```bash
python monitor.py --scan-once
```

This will:
- Analyze 10 affordable Vietnamese stocks
- Calculate technical indicators
- Provide BUY/SELL/HOLD recommendations
- Suggest optimal allocation for 10M VND budget

### 3. Continuous Monitoring (Every 15 Minutes)

```bash
python monitor.py --interval 15
```

Press `Ctrl+C` to stop monitoring.

## Usage Examples

### Basic Monitoring

```bash
# Scan once and exit
python monitor.py --scan-once

# Monitor every 15 minutes (default)
python monitor.py

# Monitor every 30 minutes
python monitor.py --interval 30

# Custom budget
python monitor.py --budget 20000000  # 20M VND
```

### Custom Watchlist

```bash
# Use predefined list
python monitor.py --watchlist blue_chips

# Custom symbols
python monitor.py --watchlist "VCB,VNM,HPG,FPT"

# List available stock categories
python monitor.py --list-stocks
```

### Available Stock Lists

| Category | Stocks |
|----------|--------|
| `blue_chips` | VCB, VHM, VIC, VNM, HPG, GAS, MSN, TCB, VPB, MBB |
| `banks` | VCB, TCB, MBB, VPB, CTG, BID, ACB, STB, HDB, TPB |
| `real_estate` | VHM, VIC, NVL, PDR, DXG, KDH, BCM, DIG, HDG, NLG |
| `tech` | FPT, CMG, VGI, SAM, ITD, ELC, SGT, ICT, DGW, CTR |
| `consumer` | VNM, MSN, MWG, PNJ, SAB, VHC, DGC, KDC, FRT, DBC |
| `industrial` | HPG, HSG, NKG, DCM, DPM, POW, PVD, VSH, GMD, AAA |
| `affordable` | VPB, STB, HDB, SHB, MBB, ACB, FPT, POW, DGC, GEX |

## Understanding the Output

### Recommendation Levels

| Emoji | Recommendation | Score Range | Meaning |
|-------|---------------|-------------|---------|
| 🟢🟢 | STRONG BUY | 40+ | Multiple bullish indicators |
| 🟢 | BUY | 20-40 | Bullish trend |
| ⚪ | HOLD | -20 to 20 | Neutral/mixed signals |
| 🔴 | SELL | -40 to -20 | Bearish trend |
| 🔴🔴 | STRONG SELL | < -40 | Multiple bearish indicators |

### Technical Indicators

**RSI (Relative Strength Index)**
- < 30: Oversold (potential buy)
- 30-70: Neutral
- > 70: Overbought (potential sell)

**Moving Averages**
- Price > MA20 > MA50: Bullish trend
- Price < MA20 < MA50: Bearish trend
- MA20 crossing MA50: Trend change

**MACD**
- Positive histogram: Bullish momentum
- Negative histogram: Bearish momentum

**Bollinger Bands**
- Price near lower band: Oversold
- Price near upper band: Overbought

### Sample Output

```
==========================================
STOCK SCAN - 2025-01-30 15:00:00
==========================================

Analyzing VPB...
  Price: 23,500 VND (+2.50%)
  🟢 Recommendation: BUY (Score: 25)
  RSI: 45.2
  🟢 RSI neutral
  🟢 Price above MA20 and MA50 (bullish)
  🟢 MA20 above MA50 (golden cross area)

==========================================
RECOMMENDATIONS SUMMARY
==========================================

🟢🟢 STRONG BUY (2 stocks):
  • VPB: 23,500 VND (Score: 35)
  • STB: 28,300 VND (Score: 42)

🟢 BUY (3 stocks):
  • HDB: 19,200 VND (Score: 28)
  • FPT: 118,500 VND (Score: 22)
  • ACB: 26,800 VND (Score: 21)

==========================================
💰 INVESTMENT SUGGESTION FOR 10M VND BUDGET
==========================================

Available: 10,000,000 VND

Suggested allocation:

  VPB
    Price: 23,500 VND
    Buy: 85 shares
    Cost: 2,004,763 VND
    Reason: STRONG BUY (Score: 35)

  STB
    Price: 28,300 VND
    Buy: 70 shares
    Cost: 1,985,945 VND
    Reason: STRONG BUY (Score: 42)

  HDB
    Price: 19,200 VND
    Buy: 104 shares
    Cost: 2,001,920 VND
    Reason: BUY (Score: 28)

  FPT
    Price: 118,500 VND
    Buy: 16 shares
    Cost: 1,899,624 VND
    Reason: BUY (Score: 22)

  ACB
    Price: 26,800 VND
    Buy: 74 shares
    Cost: 1,988,736 VND
    Reason: BUY (Score: 21)

Total: 9,880,988 VND
Remaining: 119,012 VND
```

## Project Structure

```
vietnam-stocks/
├── monitor.py              # Main monitoring script
├── src/
│   ├── stock_data.py       # Fetch stock data from VNDirect API
│   ├── technical_analysis.py  # Technical indicators & analysis
│   └── portfolio.py        # Portfolio management
├── data/
│   └── portfolio.json      # Your portfolio (holdings, transactions)
├── logs/
│   └── monitor_*.log       # Monitoring logs
├── output/
│   └── scan_*.json         # Scan results (JSON format)
└── requirements.txt        # Python dependencies
```

## API Modules

### 1. Stock Data (`src/stock_data.py`)

```python
from src.stock_data import VNStockData

fetcher = VNStockData()

# Get current price
data = fetcher.get_stock_price('VCB')
print(f"{data['symbol']}: {data['price']} VND")

# Get multiple stocks
stocks = fetcher.get_multiple_stocks(['VCB', 'VNM', 'HPG'])

# Search stocks
results = fetcher.search_stocks('Vinamilk')

# Get historical data (60 days)
history = fetcher.get_historical_data('VCB', days=60)
```

### 2. Technical Analysis (`src/technical_analysis.py`)

```python
from src.technical_analysis import TechnicalAnalyzer

analyzer = TechnicalAnalyzer()

# Calculate RSI
prices = [100, 102, 105, 103, 108, ...]
rsi = analyzer.calculate_rsi(prices, period=14)

# Calculate Moving Averages
ma20 = analyzer.calculate_moving_average(prices, 20)
ema12 = analyzer.calculate_ema(prices, 12)

# Full analysis
historical_data = fetcher.get_historical_data('VCB')
analysis = analyzer.analyze_stock(historical_data)

print(f"Recommendation: {analysis['recommendation']}")
print(f"Score: {analysis['score']}")
print(f"RSI: {analysis['indicators']['rsi']}")
```

### 3. Portfolio Management (`src/portfolio.py`)

```python
from src.portfolio import Portfolio

# Create portfolio with 10M VND
portfolio = Portfolio(budget=10_000_000)

# Buy stocks
result = portfolio.buy_stock('VCB', price=90000, shares=50)
if result['success']:
    print(f"Bought! Remaining: {result['remaining_budget']}")

# Sell stocks
result = portfolio.sell_stock('VCB', price=95000, shares=25)
print(f"Profit: {result['profit_loss']} VND")

# Get portfolio value
current_prices = {'VCB': 92000}
valuation = portfolio.get_portfolio_value(current_prices)
print(f"Total value: {valuation['total_value']} VND")
print(f"P/L: {valuation['total_profit_loss_percent']}%")

# Get allocation suggestion
allocation = portfolio.suggest_allocation(['VCB', 'VNM'], current_prices)
```

## Trading Strategy (Built-in Algorithm)

The tool uses a multi-factor scoring system:

### Bullish Signals (+points)
- RSI < 30 (oversold): +20
- Price > MA20 > MA50: +15
- MA20 > MA50 (golden cross): +10
- MACD positive: +10
- Price near lower Bollinger Band: +15
- High volume: +5

### Bearish Signals (-points)
- RSI > 70 (overbought): -20
- Price < MA20 < MA50: -15
- MA20 < MA50 (death cross): -10
- MACD negative: -10
- Price near upper Bollinger Band: -15

**Total Score:** -100 (very bearish) to +100 (very bullish)

## Data Source

- **Primary API:** VNDirect Financial Info API
- **Coverage:** HSX, HNX, UPCOM exchanges
- **Update Frequency:** Real-time (15-minute delay)
- **Historical Data:** Up to 60 days

## Limitations & Risks

⚠️ **IMPORTANT DISCLAIMERS**

1. **Not Financial Advice**
   - This tool is for educational and research purposes only
   - Always consult a licensed financial advisor before investing

2. **Market Risks**
   - Stock prices can go down as well as up
   - Past performance does not predict future results
   - You may lose some or all of your investment

3. **Technical Limitations**
   - API data may have delays or inaccuracies
   - Technical indicators are not foolproof
   - No algorithm can predict market movements perfectly

4. **Trading Fees**
   - Tool assumes 0.15% trading fee
   - Actual fees may vary by broker
   - Tax implications not included

5. **10M VND Budget Considerations**
   - Diversification is limited with small budget
   - Cannot buy expensive blue chips (VCB, VHM)
   - Focus on affordable stocks (< 30,000 VND/share)

## Investment Tips for Beginners

### Do's ✅
- Start small and learn
- Diversify across 5-10 stocks
- Set stop-loss limits (e.g., -10%)
- Research company fundamentals
- Keep emergency fund separate
- Think long-term (6+ months)
- Use limit orders, not market orders

### Don'ts ❌
- Don't invest borrowed money
- Don't chase "hot tips"
- Don't panic sell on red days
- Don't put all money in one stock
- Don't day trade without experience
- Don't ignore fees and taxes
- Don't expect quick profits

## Recommended Brokers in Vietnam

- **SSI Securities** - Low fees, good platform
- **VNDirect** - Best research, mobile app
- **TCBS** - Modern interface, fast execution
- **HSC** - Good customer service
- **FPTS** - FPT subsidiary, reliable

## Advanced Usage

### Create Custom Analysis

```python
from src.stock_data import VNStockData
from src.technical_analysis import TechnicalAnalyzer

fetcher = VNStockData()
analyzer = TechnicalAnalyzer()

# Analyze specific stock
symbol = 'FPT'
historical = fetcher.get_historical_data(symbol, days=90)
analysis = analyzer.analyze_stock(historical)

# Custom logic
if analysis['indicators']['rsi'] < 35 and analysis['score'] > 20:
    print(f"🟢 {symbol} looks promising!")
    print(f"   RSI: {analysis['indicators']['rsi']}")
    print(f"   Score: {analysis['score']}")
```

### Export Results to Excel

```python
import json
import csv

# Load scan results
with open('output/scan_20250130_150000.json') as f:
    data = json.load(f)

# Export to CSV
with open('stocks_analysis.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Symbol', 'Price', 'Change%', 'RSI', 'Score', 'Recommendation'])

    for symbol, stock in data['all_results'].items():
        writer.writerow([
            symbol,
            stock['price'],
            stock['change_percent'],
            stock['analysis']['indicators']['rsi'],
            stock['analysis']['score'],
            stock['analysis']['recommendation']
        ])
```

## Troubleshooting

### API Not Responding

```bash
# Test API connection
python -c "from src.stock_data import VNStockData; print(VNStockData().get_stock_price('VCB'))"
```

### No Data for Stock

- Check symbol is correct (uppercase)
- Some small-cap stocks may not have data
- Try different stock from STOCK_LISTS

### Insufficient Historical Data

- Stock may be newly listed
- Try reducing analysis period
- Use stocks with > 60 days trading history

## Future Enhancements

- [ ] Web interface dashboard
- [ ] Email/Telegram alerts
- [ ] Fundamental analysis (P/E, EPS)
- [ ] Machine learning predictions
- [ ] Backtesting framework
- [ ] News sentiment analysis
- [ ] Multi-broker API support

## Contributing

This is a personal project but improvements welcome:
- Better technical indicators
- More accurate API parsing
- Risk management features
- Performance optimizations

## Legal & Compliance

- Tool complies with VNDirect API terms of use
- No proprietary data redistribution
- Personal use only
- Check local securities laws before automated trading

## Support

For issues or questions:
1. Check logs in `logs/` directory
2. Review API documentation
3. Test with known working stock (e.g., VCB)

---

**Made with 📊 for Vietnamese retail investors**

Remember: **Invest wisely, diversify, and never risk more than you can afford to lose!**
