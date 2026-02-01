# Language Switcher Issue - FIXED

## Problems Identified:

### 1. ❌ API Port Issue
**Problem:** API calls were going to port 8888 instead of 5000

**Root Cause:**
- User accessing pages via `http://localhost:8888`
- API server running on `http://localhost:5000`
- `baseURL` was set to `window.location.origin` (port 8888)
- API calls like `/api/stock-categories` went to wrong port

**Solution:**
Created `js/api-config.js` that:
- Detects if on localhost
- Always uses port 5000 for API calls
- Provides `window.apiFetch()` helper function
- Added to all 11 dashboard pages

### 2. ❌ Language Switcher Not Working
**Problem:** Clicking EN/VI buttons didn't change language

**Root Causes:**
1. No `data-i18n` attributes on page elements
2. Event listeners not properly attached
3. No visual feedback when switching

**Solutions Implemented:**

#### A. Fixed Event Listeners
```javascript
// Before: onclick="switchLanguage('en')" (didn't work)
// After: btn.addEventListener('click', () => switchLanguage('en'))
```

#### B. Added Console Logging
```javascript
console.log(`Switching language to: ${lang}`);
console.log(`Translated ${count} elements to ${lang}`);
```

#### C. Need to Add Translation Attributes
Pages need `data-i18n` attributes on elements:
```html
<h1 data-i18n="nav.dashboard">Main Dashboard</h1>
<button data-i18n="common.save">Save</button>
```

---

## How to Test Language Switching:

### Option 1: Use Test Page (Recommended)
```bash
# Open test page with translations
http://localhost:5000/test_language.html
# OR
http://localhost:8888/test_language.html
```

This page has data-i18n attributes and will show translations working.

### Option 2: Check Console Logs
1. Open any dashboard
2. Open browser console (F12)
3. Click EN/VI buttons
4. Look for logs:
   - "Switching language to: vi"
   - "Translated X elements to vi"
   - "✓ Language switcher added next to menu"

### Option 3: Check localStorage
```javascript
// In browser console
localStorage.getItem('language') // Should show 'en' or 'vi'
```

---

## Files Modified:

### Created:
- `js/api-config.js` - API port configuration
- `test_language.html` - Test page with translations

### Updated:
- `js/i18n.js` - Fixed event listeners, added logging
- `js/data-api.js` - Fixed baseURL to use port 5000
- 11 HTML files - Added api-config.js script

---

## Next Steps to Complete Language Support:

### 1. Add data-i18n Attributes to Dashboard Pages

Example for `dashboard_main.html`:
```html
<!-- Page title -->
<h1 data-i18n="dashboard.real_time">Real-Time Market Overview</h1>

<!-- Buttons -->
<button data-i18n="dashboard.apply_watchlist">Apply Watchlist</button>
<button data-i18n="common.select_all">Select All</button>
<button data-i18n="common.clear_all">Clear All</button>

<!-- Status -->
<span data-i18n="dashboard.live">LIVE</span>
```

### 2. Add Placeholders
```html
<input data-i18n-placeholder="common.search" placeholder="Search">
```

### 3. Add Category Filters
```html
<div data-i18n="category.blue_chips">Blue Chips</div>
<div data-i18n="category.banks">Banks</div>
```

---

## Current Status:

✅ API Configuration Fixed - Port 5000 always used
✅ Language Switcher Displays - EN/VI buttons visible
✅ Event Listeners Working - Clicks registered
✅ Language State Changing - localStorage updated
✅ Test Page Working - Shows translations

⏳ Main Dashboard Pages - Need data-i18n attributes added

---

## Access URLs:

**Use Port 5000 for API access:**
- ✅ http://localhost:5000/dashboard_main.html
- ✅ http://localhost:5000/test_language.html
- ✅ http://localhost:5000/settings.html

**Port 8888 also works now** (API calls redirect to 5000):
- ✅ http://localhost:8888/dashboard_main.html
- ✅ http://localhost:8888/test_language.html

---

## Technical Details:

### api-config.js
```javascript
const API_BASE_URL = hostname === 'localhost'
    ? 'http://localhost:5000'  // Always use 5000 for API
    : window.location.origin;   // Use current for production

window.apiFetch = function(endpoint, options) {
    return fetch(`${API_BASE_URL}${endpoint}`, options);
};
```

### Usage in Pages
```javascript
// Old way (broken with wrong port):
fetch('/api/stock-categories')

// New way (works from any port):
apiFetch('/api/stock-categories')

// Or use window.API_BASE_URL:
fetch(`${API_BASE_URL}/api/stock-categories`)
```

---

**Last Updated:** January 31, 2026
**Status:** API Fixed ✅ | Language Switcher Functional ✅ | Translations Need Attributes ⏳
