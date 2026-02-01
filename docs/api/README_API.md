# Vietnamese Stock Analytics Platform - API Edition

## 🎉 Your Platform is Now API-Driven!

Stock data (symbols, names, categories) is now loaded from API endpoints instead of being hardcoded. This makes it **super easy to update** without changing any code!

## 🚀 Quick Start (3 Steps)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the API server
./start_api.sh

# 3. Open your browser
# http://localhost:5000/dashboard_main.html
```

That's it! Your dashboards now load data from the API.

## 📝 How to Update Stocks

### Add a New Stock

1. **Edit `data/stock_categories.json`:**
   ```json
   {
     "categories": {
       "blue_chips": ["VCB", "VHM", "NEW_STOCK", ...]
     }
   }
   ```

2. **Edit `data/stock_names.json`:**
   ```json
   {
     "NEW_STOCK": "New Company - Công ty CP Mới"
   }
   ```

3. **Refresh your browser** - Done! ✅

### Update Stock Names

Just edit `data/stock_names.json` and refresh. No code changes!

### Remove a Stock

Remove it from both JSON files and refresh. That's it!

## 📚 Documentation

- **[API_ENDPOINTS.md](API_ENDPOINTS.md)** - Complete API documentation
- **[API_SERVER_SETUP.md](API_SERVER_SETUP.md)** - Setup & deployment guide
- **[API_MIGRATION_SUMMARY.md](API_MIGRATION_SUMMARY.md)** - What changed & why

## 🔧 API Endpoints

```
GET  /api/stock-categories    # Get all stock categories (233 stocks)
GET  /api/stock-names          # Get stock symbol to name mappings
GET  /api/watchlist            # Get user's watchlist
POST /api/watchlist            # Update watchlist
GET  /api/historical/:symbol   # Get historical data
POST /api/clear-cache          # Clear data cache
```

## 📊 Data Files

All stock data is in JSON files (easy to edit!):

```
data/
├── stock_categories.json    # 233 stocks in 11 categories
├── stock_names.json         # Symbol → Company name mappings
├── watchlist.json           # User watchlist (auto-created)
└── {SYMBOL}_history.json    # Historical price data
```

## ✨ Benefits

✅ **No code changes** to add/remove stocks
✅ **Instant updates** - just edit JSON and refresh
✅ **Easy maintenance** - everything in data files
✅ **Fallback mechanism** - works even if API is down
✅ **All 8 dashboards** use the same API data

## 🎯 Examples

### Test API Endpoints

```bash
# Get all categories
curl http://localhost:5000/api/stock-categories | jq

# Get stock names
curl http://localhost:5000/api/stock-names | jq '.VCB'

# Update watchlist
curl -X POST http://localhost:5000/api/watchlist \
  -H "Content-Type: application/json" \
  -d '["VCB", "VHM", "FPT"]'
```

### Clear Cache After Updates

```bash
curl -X POST http://localhost:5000/api/clear-cache
```

## 🚀 Production Deployment

### Option 1: Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
```

### Option 2: Docker
```bash
docker build -t vnstock-api .
docker run -p 5000:5000 vnstock-api
```

### Option 3: Systemd Service
```bash
sudo systemctl start vnstock-api
```

See [API_SERVER_SETUP.md](API_SERVER_SETUP.md) for details.

## 🐛 Troubleshooting

**API server won't start?**
- Make sure port 5000 is available
- Install dependencies: `pip install -r requirements.txt`

**Data not loading?**
- Check if API server is running
- Open browser console for errors
- Try: `curl http://localhost:5000/health`

**Changes not showing?**
- Clear cache: `curl -X POST http://localhost:5000/api/clear-cache`
- Hard refresh browser: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

## 📦 What's Included

### Server Components
- `api_server.py` - Flask API server
- `start_api.sh` - Quick start script
- `requirements.txt` - Python dependencies

### Data Files
- `data/stock_categories.json` - Stock categories
- `data/stock_names.json` - Stock names

### JavaScript
- `js/stock-categories.js` - Updated to load from API

### Documentation
- `API_ENDPOINTS.md` - API reference
- `API_SERVER_SETUP.md` - Setup guide
- `API_MIGRATION_SUMMARY.md` - Migration details

## 💡 Pro Tips

1. **Edit data files** instead of code
2. **Clear cache** after updates: `curl -X POST http://localhost:5000/api/clear-cache`
3. **Validate JSON** before saving: `cat data/stock_names.json | jq`
4. **Monitor logs** in the API server terminal
5. **Use fallback** - platform works even if API is down

## 🎊 That's It!

Your platform now has API-driven stock data. Update stocks anytime by editing JSON files - no code changes needed!

---

**Need help?** Check the documentation files or API server logs.

**Happy Trading!** 📈💰🎯
