# 📋 Watchlist Feature - Quick Guide

## ✅ Bug Fixed: Watchlist Now Works!

The issue where selecting stocks in the dashboard didn't update the charts has been **fixed**!

## How It Works Now

### 1. **Select Stocks in Dashboard**
1. Open the enhanced dashboard:
   ```
   http://localhost:8888/dashboard_enhanced.html
   ```

2. Use the stock picker:
   - Search for stocks by symbol
   - Filter by category (Banks, Tech, etc.)
   - Click stocks to select/deselect
   - Use "Select All" or "Clear All" buttons

3. Click **"Apply Watchlist"** button
   - Your selection is saved to `watchlist.json`
   - You'll see a confirmation message
   - The monitor will pick up changes on the next scan

### 2. **Monitor Picks Up Changes Automatically**
- The monitor now **reloads the watchlist** before each scan
- Changes are applied automatically every 5 minutes (current setting)
- No need to restart the monitor!

### 3. **See Results in Dashboard**
- Charts update automatically when new scan completes
- Performance heatmap shows only your selected stocks
- All visualizations use your custom watchlist

## Current Status

✅ **Monitor Running**: Scanning every **5 minutes**
✅ **Watchlist Active**: Currently monitoring **5 stocks**:
- VCB (Vietcombank)
- HPG (Hoa Phat Group)
- FPT (FPT Corporation)
- VNM (Vinamilk)
- GAS (PetroVietnam Gas)

✅ **Dashboards Live**:
- Enhanced: http://localhost:8888/dashboard_enhanced.html
- Original: http://localhost:8888/dashboard_realtime.html

## How to Use

### Quick Method (Web UI)
1. Open enhanced dashboard
2. Select stocks in the picker
3. Click "Apply Watchlist"
4. Wait for next scan (every 5 minutes)
5. Charts update automatically

### CLI Method
```bash
# Add specific stocks
python manage_watchlist.py --add VCB HPG FPT MSN VNM

# Add entire category
python manage_watchlist.py --category blue_chips

# List current watchlist
python manage_watchlist.py --list

# Interactive mode
python manage_watchlist.py --interactive
```

## What Was Fixed

### Before (Broken)
- Dashboard saved to localStorage only
- Monitor used hardcoded stock list
- No sync between dashboard and monitor
- Charts didn't reflect selections

### After (Fixed)
✅ Dashboard saves to `watchlist.json` file
✅ Monitor loads from `watchlist.json`
✅ Monitor reloads on each scan
✅ Charts update with selected stocks
✅ No restart needed

## Technical Details

### File Location
```
vietnam-stocks/
└── watchlist.json          # Your custom watchlist
```

### API Endpoints
- `POST /api/watchlist` - Save watchlist (from dashboard)
- `GET /api/watchlist` - Load watchlist
- `GET /api/latest` - Get latest scan results

### Monitor Behavior
```
Every 5 minutes:
1. Reload watchlist.json
2. Scan selected stocks
3. Run technical analysis
4. Save results to output/scan_*.json
5. Dashboard auto-updates
```

## Examples

### Example 1: Monitor Blue Chip Stocks
```bash
# Via CLI
python manage_watchlist.py --category blue_chips
```
Or in dashboard: Click "Blue Chips" filter → Select All → Apply

### Example 2: Monitor Specific Stocks
```bash
# Via CLI
python manage_watchlist.py --add VCB TCB MBB ACB STB
```
Or in dashboard: Search and click each stock → Apply

### Example 3: Monitor Affordable Stocks
```bash
# Via CLI
python manage_watchlist.py --category affordable
```
Or in dashboard: Click "Affordable" filter → Select All → Apply

## Tips

1. **Start with 10-20 stocks** - Don't overwhelm yourself
2. **Use categories** - Good starting point for diversification
3. **Mix sectors** - Banks + Tech + Consumer for balance
4. **Watch the heatmap** - Quick visual overview
5. **Check every scan** - Dashboard updates every 5 minutes

## Troubleshooting

**Charts not updating?**
- Wait for next scan (check timestamp in dashboard)
- Current scan interval: 5 minutes
- Check watchlist: `cat watchlist.json`

**Want immediate results?**
```bash
# Trigger manual scan
python demo_monitor.py --scan-once
```

**Change scan interval?**
```bash
# Stop current monitor
pkill -f demo_monitor

# Start with different interval (in minutes)
python demo_monitor.py --interval 10
```

**Reset to default stocks?**
```bash
python manage_watchlist.py --clear
python manage_watchlist.py --category affordable
```

## Performance Notes

- **5-minute scans**: Good for active monitoring
- **15-minute scans**: Better for battery life
- **30-minute scans**: Good for long-term holds

Current setting: **5 minutes** (as requested)

To change:
```bash
pkill -f demo_monitor
python demo_monitor.py --interval 15  # 15 minutes
```

## Next Steps

1. **Open dashboard**: http://localhost:8888/dashboard_enhanced.html
2. **Select stocks** you want to monitor
3. **Click "Apply Watchlist"**
4. **Wait ~5 minutes** for next scan
5. **Watch charts update** automatically

Enjoy your customized Vietnamese stock monitoring system! 🎉
