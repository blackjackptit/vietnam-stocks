# Vietnamese Stock Monitor - Enhanced Features

## What's New

### 1. Complete Stock Database (200+ Stocks)

The system now includes **ALL major Vietnamese stocks** across multiple categories:

- **Blue Chips** (20 stocks): VCB, VHM, VIC, VNM, HPG, GAS, MSN, TCB, VPB, MBB, etc.
- **Banks** (28 stocks): VCB, TCB, MBB, VPB, CTG, BID, ACB, STB, HDB, TPB, VIB, MSB, etc.
- **Real Estate** (40 stocks): VHM, VIC, NVL, PDR, DXG, KDH, BCM, DIG, HDG, NLG, etc.
- **Technology** (30 stocks): FPT, CMG, VGI, SAM, ITD, ELC, SGT, ICT, DGW, CTR, etc.
- **Consumer** (30 stocks): VNM, MSN, MWG, PNJ, SAB, VHC, DGC, KDC, FRT, DBC, etc.
- **Oil & Gas** (19 stocks): GAS, PLX, PVD, PVS, PVT, PVB, PVG, PVC, PVX, BSR, etc.
- **Securities** (19 stocks): SSI, VND, VCI, HCM, BSI, MBS, VIX, SHS, AGR, FTS, etc.
- **Utilities** (20 stocks): POW, NT2, REE, GEG, GEX, PC1, VSH, BWE, EVE, HT1, etc.
- **Transport** (20 stocks): VJC, HVN, GMD, ACV, HAH, PHP, VOS, VSC, STG, TMS, etc.

### 2. Interactive Stock Picker

Choose exactly which stocks you want to monitor:

- **Search functionality** - Find stocks by symbol
- **Category filters** - Filter by sector (Banks, Tech, Real Estate, etc.)
- **Select/Deselect** - Click to add/remove stocks from your watchlist
- **Quick actions** - Select All / Clear All buttons
- **Persistent storage** - Your selections are saved automatically

### 3. Enhanced Visualizations

#### Performance Heatmap
- Color-coded grid showing all stocks
- Green = positive performance, Red = negative
- Intensity indicates magnitude of change
- Quick visual overview of market sentiment

#### Score Distribution Chart
- Bar chart showing technical analysis scores
- Color-coded by recommendation (Buy/Hold/Sell)
- Easy identification of top opportunities

#### RSI Distribution
- Line chart tracking RSI values across stocks
- Shows overbought (>70) and oversold (<30) zones
- Helps identify reversal opportunities

#### Sector Performance
- Doughnut chart showing sector distribution
- Understand your portfolio composition
- Identify sector concentration

#### Price & Volume Analysis
- Dual-axis chart combining price and volume
- Identify high-activity stocks
- Spot unusual volume patterns

#### Detailed Stock Table
- Comprehensive metrics for each stock
- Sortable columns
- Live updates with technical signals
- Recommendation badges

### 4. Custom Watchlist Management

Command-line tool for managing your watchlist:

```bash
# Interactive mode
python manage_watchlist.py --interactive

# Add specific stocks
python manage_watchlist.py --add VCB HPG FPT

# Add entire category
python manage_watchlist.py --category banks

# Remove stocks
python manage_watchlist.py --remove VCB HPG

# List current watchlist
python manage_watchlist.py --list

# Clear all
python manage_watchlist.py --clear
```

## How to Use

### Quick Start

1. **Start the enhanced dashboard:**
   ```bash
   ./start_enhanced.sh
   ```

2. **Start the monitor (in another terminal):**
   ```bash
   python demo_monitor.py --interval 15
   ```

3. **Open the enhanced dashboard:**
   ```
   http://localhost:8888/dashboard_enhanced.html
   ```

### Customizing Your Watchlist

#### Method 1: Using the Dashboard
1. Open the enhanced dashboard
2. Use the search box to find stocks
3. Click on stocks to select/deselect
4. Click "Apply Watchlist" button
5. Your selection is saved automatically

#### Method 2: Using the CLI Tool
```bash
# Interactive mode with menu
python manage_watchlist.py --interactive

# Or use command-line arguments
python manage_watchlist.py --add VCB VHM HPG GAS FPT
python manage_watchlist.py --category blue_chips
python manage_watchlist.py --list
```

### Understanding the Metrics

#### Technical Score (-100 to +100)
- **> 40**: STRONG BUY - Multiple bullish signals
- **20 to 40**: BUY - Some bullish signals
- **-20 to 20**: HOLD - Neutral or mixed signals
- **< -20**: SELL - Bearish signals

#### RSI (Relative Strength Index)
- **< 30**: Oversold - Potential buying opportunity
- **30-70**: Normal range
- **> 70**: Overbought - Potential profit taking

#### Signals
- **Golden Cross**: Short-term MA crosses above long-term MA (Bullish)
- **Death Cross**: Short-term MA crosses below long-term MA (Bearish)
- **RSI Oversold/Overbought**: RSI extreme values
- **Price above/below MA**: Trend indicators
- **MACD Bullish/Bearish**: Momentum indicators

## API Endpoints

The real-time server provides several API endpoints:

- `GET /api/latest` - Get latest scan results
- `GET /api/stocks` - Get all available stocks by category
- `GET /api/watchlist` - Get current watchlist

## Dashboard Comparison

### Original Dashboard (`dashboard_realtime.html`)
- Simple, focused view
- 10 default stocks
- Basic charts (Score, RSI)
- Good for quick checks

### Enhanced Dashboard (`dashboard_enhanced.html`)
- Full stock picker (200+ stocks)
- Multiple visualization types
- Detailed table view
- Customizable watchlist
- Advanced analytics

## Files Structure

```
vietnam-stocks/
├── src/
│   ├── stock_data.py          # Expanded with 200+ stocks
│   ├── technical_analysis.py
│   ├── portfolio.py
│   └── demo_data.py
├── dashboard_realtime.html    # Original dashboard
├── dashboard_enhanced.html    # NEW: Enhanced dashboard
├── realtime_server.py         # Updated with new API endpoints
├── monitor.py
├── demo_monitor.py
├── manage_watchlist.py        # NEW: Watchlist CLI tool
├── start_enhanced.sh          # NEW: Enhanced startup script
├── watchlist.json             # Your custom watchlist (auto-created)
└── output/                    # Scan results
```

## Tips

1. **Start with a category** - Select a category like "affordable" or "banks" to focus your analysis
2. **Use the heatmap** - Quickly identify hot and cold stocks
3. **Monitor 20-30 stocks** - Too many stocks can be overwhelming
4. **Combine indicators** - Don't rely on a single metric
5. **Save multiple watchlists** - Use different files for different strategies

## Troubleshooting

**Dashboard shows no stocks:**
- Make sure you've selected stocks in the picker
- Click "Apply Watchlist" button
- Refresh the page

**Monitor not finding stocks:**
- Check that watchlist.json exists
- Verify stock symbols are correct (uppercase)
- Run `python manage_watchlist.py --list` to see current list

**Server won't start:**
- Kill existing process: `kill $(cat realtime.pid)`
- Check port 8888 is not in use: `lsof -i:8888`

## Future Enhancements

Possible additions:
- Candlestick charts for individual stocks
- Correlation matrix between stocks
- News integration
- Alert system for price targets
- Portfolio tracking with P&L
- Export to Excel/CSV
- Mobile-responsive design
