# API Server Setup Guide

This guide explains how to run the API server for the Vietnamese Stock Analytics Platform.

## Overview

The platform now loads stock data from API endpoints instead of hardcoded values. This makes it easy to:
- ✅ Add/remove stocks without changing code
- ✅ Update stock names instantly
- ✅ Modify categories dynamically
- ✅ Maintain data centrally

## Quick Start

### 1. Install Dependencies

```bash
pip install flask flask-cors
```

### 2. Run the API Server

```bash
python api_server.py
```

The server will start on `http://localhost:5000`

### 3. Open Your Dashboard

Open any dashboard in your browser:
- http://localhost:5000/dashboard_main.html
- http://localhost:5000/dashboard_history.html
- etc.

The dashboards will automatically load data from the API!

## API Endpoints

### Stock Categories
```
GET http://localhost:5000/api/stock-categories
```
Returns all stock symbols organized by categories.

### Stock Names
```
GET http://localhost:5000/api/stock-names
```
Returns mapping of stock symbols to company names.

### Watchlist
```
GET http://localhost:5000/api/watchlist
POST http://localhost:5000/api/watchlist
```
Get or update the user's watchlist.

### Historical Data
```
GET http://localhost:5000/api/historical/:symbol?days=90
```
Get historical price data for a specific stock.

## Data Files

All data is stored in JSON files in the `data/` directory:

```
data/
├── stock_categories.json    # Stock categories (233 stocks)
├── stock_names.json         # Stock name mappings
├── watchlist.json           # User watchlist
├── latest_data.json         # Latest stock prices
└── {SYMBOL}_history.json    # Historical data per stock
```

## Updating Stock Data

### Add a New Stock

1. **Edit `data/stock_categories.json`:**
```json
{
  "categories": {
    "blue_chips": ["VCB", "VHM", "NEW_STOCK", ...],
    ...
  }
}
```

2. **Edit `data/stock_names.json`:**
```json
{
  "NEW_STOCK": "New Company - Công ty CP Mới",
  ...
}
```

3. **Clear cache (optional):**
```bash
curl -X POST http://localhost:5000/api/clear-cache
```

4. **Refresh your browser** - The new stock appears immediately!

### Remove a Stock

1. Remove the symbol from `data/stock_categories.json`
2. Remove the entry from `data/stock_names.json`
3. Clear cache and refresh

### Update Stock Names

1. Edit `data/stock_names.json`
2. Clear cache
3. Refresh browser

**No code changes needed!**

## Production Deployment

### Option 1: Use Gunicorn (Recommended)

```bash
# Install gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
```

### Option 2: Use Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api_server:app"]
```

Build and run:
```bash
docker build -t vnstock-api .
docker run -p 5000:5000 vnstock-api
```

### Option 3: Use systemd (Linux)

Create `/etc/systemd/system/vnstock-api.service`:
```ini
[Unit]
Description=Vietnamese Stock Analytics API
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/vietnam-stocks
Environment="PATH=/usr/local/bin"
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 api_server:app

[Install]
WantedBy=multi-user.target
```

Start the service:
```bash
sudo systemctl start vnstock-api
sudo systemctl enable vnstock-api
```

## Nginx Configuration (Optional)

If you want to serve the API through Nginx:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        root /var/www/vietnam-stocks;
        index index.html;
        try_files $uri $uri/ =404;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /data {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
    }
}
```

## Testing the API

### Test Categories Endpoint
```bash
curl http://localhost:5000/api/stock-categories | jq
```

### Test Stock Names
```bash
curl http://localhost:5000/api/stock-names | jq
```

### Test Watchlist
```bash
# Get watchlist
curl http://localhost:5000/api/watchlist

# Update watchlist
curl -X POST http://localhost:5000/api/watchlist \
  -H "Content-Type: application/json" \
  -d '["VCB", "VHM", "VIC", "FPT"]'
```

### Test Health Check
```bash
curl http://localhost:5000/health
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use a different port
python api_server.py --port 5001
```

### CORS Issues
The server has CORS enabled by default. If you still have issues:
1. Check browser console for errors
2. Verify `flask-cors` is installed
3. Check API server logs

### Data Not Updating
1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Clear server cache:
   ```bash
   curl -X POST http://localhost:5000/api/clear-cache
   ```
3. Restart the API server

### File Not Found Errors
Make sure all required JSON files exist in the `data/` directory:
```bash
ls -la data/
```

Required files:
- `stock_categories.json`
- `stock_names.json`
- `watchlist.json` (optional, will be created automatically)

## Development Tips

### Auto-Reload Changes
The Flask development server auto-reloads when you change Python code.

To reload data files without restarting:
```bash
curl -X POST http://localhost:5000/api/clear-cache
```

### View Server Logs
All requests are logged to console. Watch for:
- ✓ 200 OK - Success
- ⚠️ 404 Not Found - File missing
- ❌ 500 Internal Server Error - Check JSON syntax

### JSON Validation
Before updating data files, validate JSON:
```bash
# Install jq
sudo apt install jq  # Linux
brew install jq      # Mac

# Validate JSON
cat data/stock_categories.json | jq
```

## Next Steps

1. **Implement Real Data Fetching:**
   - Connect to actual stock market APIs
   - Update `latest_data.json` periodically
   - Implement historical data fetching

2. **Add Database:**
   - Move from JSON files to PostgreSQL/MySQL
   - Better performance for large datasets
   - Query optimization

3. **Add Authentication:**
   - User accounts
   - Personal watchlists
   - API key management

4. **Add Caching:**
   - Redis for better performance
   - Cache frequently accessed data
   - Reduce database queries

## Support

For issues or questions:
1. Check the logs in the terminal where API server is running
2. Verify JSON file syntax
3. Clear cache and restart server
4. Check browser console for frontend errors

---

**Your stock data is now API-driven! Easy to maintain and update.** 🎉
