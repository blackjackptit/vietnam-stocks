# API Port Fix - Complete

## Problem:
API calls were going to port 8888 instead of port 5000:
```
❌ http://localhost:8888/api/stock-categories
✅ http://localhost:5000/api/stock-categories (correct)
```

## Root Cause:
- Users accessing pages via `http://localhost:8888`
- Relative URLs like `fetch('/api/stock-categories')` resolved to current origin (port 8888)
- API server running on port 5000, so calls failed

## Solution Implemented:

### 1. Created API Configuration (`js/api-config.js`)
```javascript
const API_BASE_URL = (() => {
    const hostname = window.location.hostname;

    // For localhost, always use port 5000
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return 'http://localhost:5000';
    }

    // For production, use current origin
    return window.location.origin;
})();

window.API_BASE_URL = API_BASE_URL;
```

### 2. Updated All Fetch Calls
**Before:**
```javascript
fetch('/api/stock-categories')
```

**After:**
```javascript
fetch(`${window.API_BASE_URL || ''}/api/stock-categories`)
```

### 3. Files Fixed:

#### JavaScript Files:
- ✅ `js/stock-categories.js` - loadStockCategories()
- ✅ `js/data-api.js` - baseURL configuration

#### HTML Dashboard Files (9 files):
- ✅ `index.html`
- ✅ `dashboard_main.html`
- ✅ `dashboard_history.html`
- ✅ `dashboard_advanced.html`
- ✅ `advanced_charts.html`
- ✅ `price_forecast.html`
- ✅ `alerts_system.html`
- ✅ `trading_automation.html`
- ✅ `dashboard_realtime.html`

### 4. Script Execution Order:
```html
<head>
    <!-- MUST be first - Sets API_BASE_URL -->
    <script src="js/api-config.js"></script>

    <!-- Then other scripts can use API_BASE_URL -->
    <script src="js/stock-categories.js"></script>
    <script src="js/data-api.js"></script>
    <script src="js/i18n.js"></script>
    <script src="js/currency.js"></script>
</head>
```

## Testing:

### 1. Check Browser Console
Open any dashboard and press F12:
```
✓ API Configuration loaded. Base URL: http://localhost:5000
✓ Stock Categories loaded from API: 233 total stocks
```

### 2. Check Network Tab
1. Open DevTools (F12)
2. Go to Network tab
3. Reload page
4. Look for API calls:
   - ✅ Should see: `http://localhost:5000/api/stock-categories`
   - ❌ Should NOT see: `http://localhost:8888/api/stock-categories`

### 3. Test from Both Ports
```bash
# From port 8888
http://localhost:8888/dashboard_main.html
# API calls should go to port 5000 ✅

# From port 5000
http://localhost:5000/dashboard_main.html
# API calls should go to port 5000 ✅
```

## Verification Commands:

### Check if API server is running:
```bash
curl http://localhost:5000/api/stock-categories | head -20
# Should return JSON with stock categories
```

### Check which ports are in use:
```bash
lsof -i :5000    # API server
lsof -i :8888    # Web server (optional)
```

### Test API endpoint directly:
```bash
# Stock categories
curl http://localhost:5000/api/stock-categories | jq '.total_stocks'
# Should output: 233

# Stock names
curl http://localhost:5000/api/stock-names | jq 'keys | length'
# Should output: 113
```

## How It Works:

### Page Load Sequence:
1. **User opens:** `http://localhost:8888/dashboard_main.html`
2. **api-config.js loads:** Detects hostname = 'localhost'
3. **Sets global:** `window.API_BASE_URL = 'http://localhost:5000'`
4. **All fetch calls use:** `fetch(\`${window.API_BASE_URL}/api/...\`)`
5. **Result:** All API calls go to port 5000 ✅

### Fallback for Production:
```javascript
// On localhost: Uses port 5000
window.API_BASE_URL = 'http://localhost:5000'

// On production (e.g., example.com): Uses current origin
window.API_BASE_URL = 'https://example.com'
```

## Common Issues:

### Issue 1: API calls still go to 8888
**Solution:** Hard refresh to clear cache
```
Chrome/Edge: Ctrl+Shift+R
Firefox: Ctrl+F5
Mac: Cmd+Shift+R
```

### Issue 2: "API_BASE_URL is not defined"
**Cause:** api-config.js not loaded first
**Solution:** Check script order in HTML `<head>`:
```html
<!-- api-config.js MUST be first -->
<script src="js/api-config.js"></script>
<script src="js/stock-categories.js"></script>
```

### Issue 3: Network error / CORS
**Cause:** API server not running
**Solution:** Start API server:
```bash
cd /Users/nghia.dinh/Projects/vietnam-stocks
./start_api.sh
```

## Files Modified Summary:

**Created:**
- `js/api-config.js`
- `fix_api_urls.py` (utility script)

**Updated:**
- `js/stock-categories.js`
- `js/data-api.js`
- 9 dashboard HTML files

**Added Script Tag to:**
- All 11 dashboard pages (including test_language.html and settings.html)

## Status:

✅ **API Port Fixed** - All calls use port 5000
✅ **Works from any port** - 8888, 5000, or production
✅ **Console logging** - Shows API base URL on load
✅ **Tested** - All dashboard pages verified

## Access Instructions:

**Recommended:** Use port 5000 directly
```
http://localhost:5000/dashboard_main.html
http://localhost:5000/settings.html
http://localhost:5000/test_language.html
```

**Also works:** Port 8888 (API calls redirect to 5000)
```
http://localhost:8888/dashboard_main.html
```

---

**Last Updated:** January 31, 2026
**Fix Applied:** All fetch('/api/...') calls now use API_BASE_URL
**Status:** ✅ COMPLETE
