# 🚀 Quick Start Guide

## Current Status

✅ Real-time server is running on port 8888 (PID: 18522)
✅ Enhanced dashboard is ready
✅ 200+ Vietnamese stocks available

## 📱 Access Your Dashboards

### Enhanced Dashboard (Recommended)
```
http://localhost:8888/dashboard_enhanced.html
```
**Features:**
- Stock picker with 200+ stocks
- 6 different chart types
- Custom watchlist
- Detailed analysis table

### Historical Analysis Dashboard (NEW!)
```
http://localhost:8888/dashboard_history.html
```
**Features:**
- Price history charts with moving averages
- Volume analysis
- RSI & MACD indicators
- Detailed statistics
- Multiple timeframes (30/60/90/180/365 days)
- Deep technical analysis

### Original Dashboard
```
http://localhost:8888/dashboard_realtime.html
```
**Features:**
- Simple, focused view
- Quick market overview
- Real-time updates

## 🎯 Choose Stocks to Monitor

### Option 1: Use the Web UI
1. Open: `http://localhost:8888/dashboard_enhanced.html`
2. Scroll to "Select Stocks to Monitor" section
3. Use search box or category filters
4. Click stocks to select/deselect
5. Click "Apply Watchlist" button

### Option 2: Use CLI Tool
```bash
# Interactive menu
python manage_watchlist.py --interactive

# Or use quick commands:
python manage_watchlist.py --add VCB HPG FPT MSN
python manage_watchlist.py --category banks
python manage_watchlist.py --list
```

## 🔄 Monitor Your Stocks

The monitor is already running and scanning every 15 minutes.

To check it's running:
```bash
ps aux | grep demo_monitor
```

To see the latest scan results:
```bash
ls -lt output/scan_*.json | head -1
```

To view logs:
```bash
tail -f logs/monitor_*.log
```

## 📊 Understanding the Dashboard

### Top Section: Market Summary
- **Monitoring**: Total stocks in your watchlist
- **Strong Buy**: Stocks with score > 40
- **Buy**: Stocks with score 20-40
- **Hold**: Stocks with score -20 to 20
- **Sell**: Stocks with score < -20
- **Avg Score**: Average technical score

### Performance Heatmap
- Each cell is a stock
- Color intensity = magnitude of price change
- Green = positive, Red = negative
- Click to see details

### Score Distribution Chart
- Bar chart of technical analysis scores
- Higher is better
- Color-coded by recommendation

### RSI Distribution
- Line chart showing momentum
- < 30 = oversold (potential buy)
- > 70 = overbought (potential sell)

### Sector Performance
- Pie chart of your portfolio sectors
- Shows diversification

### Price & Volume Chart
- Combined view of price and trading volume
- High volume + price change = strong signal

### Detailed Stock Table
- Complete metrics for each stock
- Click column headers to sort
- Shows top signals for each stock

## 🛠️ Common Commands

### Server Management
```bash
# Check if server is running
ps aux | grep realtime_server

# View server logs
tail -f realtime.log

# Restart server
./start_enhanced.sh

# Stop server
kill $(cat realtime.pid)
```

### Monitor Management
```bash
# Check monitor status
ps aux | grep demo_monitor

# View monitor logs
tail -f logs/monitor_*.log

# Start monitor (15 min interval)
python demo_monitor.py --interval 15

# Run one-time scan
python demo_monitor.py --scan-once
```

### Watchlist Management
```bash
# View current watchlist
python manage_watchlist.py --list

# Add stocks
python manage_watchlist.py --add VCB HPG FPT

# Add entire category
python manage_watchlist.py --category blue_chips

# Remove stocks
python manage_watchlist.py --remove VCB

# Clear all
python manage_watchlist.py --clear

# Interactive mode
python manage_watchlist.py --interactive
```

## 📁 Important Files

```
Output Files:
  output/scan_*.json          # Scan results (updated every 15 min)

Configuration:
  watchlist.json              # Your custom watchlist

Logs:
  realtime.log                # Server logs
  logs/monitor_*.log          # Monitor logs

Dashboards:
  dashboard_enhanced.html     # Enhanced dashboard (recommended)
  dashboard_realtime.html     # Simple dashboard
```

## 🎨 Stock Categories

Use these category names with the CLI:
- `blue_chips` - Top 20 largest companies
- `banks` - 28 banking stocks
- `real_estate` - 40 real estate stocks
- `tech` - 30 technology stocks
- `consumer` - 30 consumer goods stocks
- `oil_gas` - 19 oil & gas stocks
- `securities` - 19 securities firms
- `utilities` - 20 utility companies
- `transport` - 20 transport companies
- `affordable` - 20 lower-priced stocks

## 🚀 Recommended Workflow

1. **Choose Your Focus**
   ```bash
   python manage_watchlist.py --category banks
   python manage_watchlist.py --add FPT HPG VNM
   ```

2. **Open Dashboard**
   ```
   http://localhost:8888/dashboard_enhanced.html
   ```

3. **Analyze the Heatmap**
   - Look for green (gaining) stocks
   - Check sector distribution

4. **Review Score Chart**
   - Focus on high scores (> 20)
   - Check recommendation badges

5. **Deep Dive in Table**
   - Sort by score or RSI
   - Read technical signals
   - Make informed decisions

6. **Monitor Continuously**
   - Dashboard updates every 2 seconds
   - New scans every 15 minutes
   - Watch for signal changes

## 💡 Pro Tips

1. **Start Small**: Begin with 10-15 stocks you know
2. **Use Categories**: Filter by sector for focused analysis
3. **Check Volume**: High volume = more reliable signals
4. **Combine Indicators**: Don't rely on a single metric
5. **Set Alerts**: Note stocks near key levels (RSI 30/70)
6. **Review History**: Check past scans in output/ folder

## ❓ Troubleshooting

**Dashboard not loading?**
```bash
# Check server status
ps aux | grep realtime_server

# Restart if needed
./start_enhanced.sh
```

**No data showing?**
```bash
# Check if monitor is running
ps aux | grep demo_monitor

# Run a scan manually
python demo_monitor.py --scan-once
```

**Watchlist not saving?**
```bash
# Check file permissions
ls -l watchlist.json

# Verify content
cat watchlist.json
```

## 📞 Next Steps

Ready to customize? Check out:
- `FEATURES.md` - Detailed feature documentation
- `ENHANCEMENTS_SUMMARY.md` - What's new overview

Enjoy your enhanced Vietnamese stock monitoring system! 🎉
