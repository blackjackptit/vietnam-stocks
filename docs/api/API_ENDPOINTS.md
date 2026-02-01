# API Endpoints Documentation

This document describes all API endpoints that should be implemented for the Vietnamese Stock Analytics Platform.

## 1. Stock Categories API

**Endpoint:** `GET /api/stock-categories`

**Description:** Returns all stock symbols organized by categories.

**Response Format:**
```json
{
  "success": true,
  "categories": {
    "commodities": ["GOLD", "SILVER", "XAU", "XAG"],
    "blue_chips": ["VCB", "VHM", "VIC", "VNM", "HPG", "GAS", "MSN", "TCB", ...],
    "banks": ["VCB", "TCB", "MBB", "VPB", "CTG", "BID", "ACB", ...],
    "real_estate": ["VHM", "VIC", "NVL", "PDR", "DXG", "KDH", ...],
    "tech": ["FPT", "CMG", "VGI", "SAM", "ITD", "ELC", ...],
    "consumer": ["VNM", "MSN", "MWG", "PNJ", "SAB", "VHC", ...],
    "oil_gas": ["GAS", "PLX", "PVD", "PVS", "PVT", ...],
    "affordable": ["VPB", "STB", "HDB", "SHB", "MBB", ...],
    "industrial": ["HPG", "HSG", "NKG", "VCS", "TVN", ...],
    "transportation": ["VJC", "HVN", "VTP", "VSC", "GMD", ...],
    "utilities": ["POW", "GAS", "NT2", "REE", "PC1", ...]
  },
  "total_stocks": 233,
  "last_updated": "2024-01-31T10:00:00Z"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Failed to load categories"
}
```

---

## 2. Stock Names API

**Endpoint:** `GET /api/stock-names`

**Description:** Returns mapping of stock symbols to their full company names.

**Response Format:**
```json
{
  "VCB": "Vietcombank - Ngân hàng TMCP Ngoại Thương Việt Nam",
  "VHM": "Vinhomes - Công ty CP Vinhomes",
  "VIC": "Vingroup - Tập đoàn Vingroup",
  "VNM": "Vinamilk - Công ty CP Sữa Việt Nam",
  "HPG": "Hòa Phát - Tập đoàn Hòa Phát",
  "GAS": "PV Gas - Tổng Công ty Khí Việt Nam",
  "MSN": "Masan Group - Tập đoàn Masan",
  "TCB": "Techcombank - Ngân hàng TMCP Kỹ Thương Việt Nam",
  "VPB": "VPBank - Ngân hàng TMCP Việt Nam Thịnh Vượng",
  "MBB": "MBBank - Ngân hàng TMCP Quân Đội",
  ...
}
```

**Example:**
```javascript
// Usage in frontend
const stockNames = await fetch('/api/stock-names').then(r => r.json());
console.log(stockNames['VCB']); // "Vietcombank - Ngân hàng TMCP Ngoại Thương Việt Nam"
```

---

## 3. Stock Info API

**Endpoint:** `GET /api/stock-info/:symbol`

**Description:** Returns detailed information about a specific stock.

**Parameters:**
- `symbol` (required): Stock symbol (e.g., "VCB", "HPG")

**Response Format:**
```json
{
  "success": true,
  "symbol": "VCB",
  "name": "Vietcombank - Ngân hàng TMCP Ngoại Thương Việt Nam",
  "name_en": "Joint Stock Commercial Bank for Foreign Trade of Vietnam",
  "exchange": "HOSE",
  "industry": "Banking",
  "sector": "Financials",
  "categories": ["blue_chips", "banks"],
  "market_cap": 150000000000000,
  "outstanding_shares": 3700000000,
  "listed_date": "2009-07-14",
  "website": "https://www.vietcombank.com.vn",
  "description": "Vietcombank is one of the largest commercial banks in Vietnam...",
  "address": "198 Trần Quang Khải, Hoàn Kiếm, Hà Nội",
  "phone": "+84 24 3942 5932",
  "email": "info@vietcombank.com.vn"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Stock not found"
}
```

---

## 4. All Stocks Info API

**Endpoint:** `GET /api/stocks-info`

**Description:** Returns detailed information for all stocks at once.

**Response Format:**
```json
{
  "success": true,
  "stocks": {
    "VCB": {
      "name": "Vietcombank - Ngân hàng TMCP Ngoại Thương Việt Nam",
      "exchange": "HOSE",
      "industry": "Banking",
      "sector": "Financials",
      "categories": ["blue_chips", "banks"],
      "market_cap": 150000000000000,
      "listed_date": "2009-07-14"
    },
    "VHM": {
      "name": "Vinhomes - Công ty CP Vinhomes",
      "exchange": "HOSE",
      "industry": "Real Estate",
      "sector": "Real Estate",
      "categories": ["blue_chips", "real_estate"],
      "market_cap": 200000000000000,
      "listed_date": "2018-05-16"
    },
    ...
  },
  "total": 233,
  "last_updated": "2024-01-31T10:00:00Z"
}
```

---

## 5. Watchlist API

**Endpoint:** `GET /api/watchlist`

**Description:** Returns the user's current watchlist.

**Response Format:**
```json
["VCB", "VHM", "VIC", "VNM", "HPG", "GAS", "MSN", "TCB", "VPB", "MBB"]
```

**Update Watchlist:**

**Endpoint:** `POST /api/watchlist`

**Request Body:**
```json
["VCB", "VHM", "VIC", "VNM", "HPG"]
```

**Response:**
```json
{
  "success": true,
  "count": 5,
  "message": "Watchlist updated successfully"
}
```

---

## 6. Latest Stock Data API

**Endpoint:** `GET /api/latest`

**Description:** Returns the latest price and analysis data for all stocks.

**Response Format:**
```json
{
  "timestamp": "2024-01-31T10:30:00Z",
  "all_results": {
    "VCB": {
      "symbol": "VCB",
      "price": 95500,
      "change": 500,
      "change_percent": 0.53,
      "volume": 2500000,
      "open": 95000,
      "high": 96000,
      "low": 94500,
      "analysis": {
        "score": 25,
        "recommendation": "BUY",
        "emoji": "🟢",
        "signals": [
          "🟢 RSI at 45 (Neutral)",
          "🟢 Price above MA20",
          "🟢 Volume increasing"
        ],
        "indicators": {
          "rsi": 45,
          "ma20": 93000,
          "ma50": 90000,
          "macd": 150,
          "macd_signal": 120
        }
      }
    },
    ...
  }
}
```

---

## 7. Historical Data API

**Endpoint:** `GET /api/historical/:symbol`

**Description:** Returns historical OHLCV data for a specific stock.

**Parameters:**
- `symbol` (required): Stock symbol
- `days` (optional): Number of days to retrieve (default: 90)

**Response Format:**
```json
[
  {
    "date": "2024-01-31",
    "open": 95000,
    "high": 96000,
    "low": 94500,
    "close": 95500,
    "volume": 2500000
  },
  {
    "date": "2024-01-30",
    "open": 94500,
    "high": 95500,
    "low": 94000,
    "close": 95000,
    "volume": 2800000
  },
  ...
]
```

---

## Implementation Priority

### High Priority (Required for basic functionality):
1. ✅ `/api/stock-categories` - Stock organization
2. ✅ `/api/stock-names` - Display names
3. ✅ `/api/latest` - Real-time data
4. ✅ `/api/watchlist` (GET/POST) - User preferences

### Medium Priority (Enhanced features):
5. `/api/stock-info/:symbol` - Detailed information
6. `/api/stocks-info` - Bulk information

### Already Implemented:
- Historical data is currently loaded from `data/{SYMBOL}_history.json`
- Current price data from `data/{SYMBOL}_current.json`

---

## Data Storage Recommendations

### Option 1: JSON Files (Current)
```
data/
  ├── stock_categories.json      # Categories data
  ├── stock_names.json           # Name mappings
  ├── stock_info.json            # Detailed info for all stocks
  ├── VCB_current.json           # Current price data
  ├── VCB_history.json           # Historical data
  └── ...
```

### Option 2: Database (Recommended for production)
```sql
-- Stocks table
CREATE TABLE stocks (
    symbol VARCHAR(10) PRIMARY KEY,
    name VARCHAR(200),
    name_en VARCHAR(200),
    exchange VARCHAR(10),
    industry VARCHAR(50),
    sector VARCHAR(50),
    market_cap BIGINT,
    listed_date DATE
);

-- Categories table
CREATE TABLE stock_categories (
    symbol VARCHAR(10),
    category VARCHAR(50),
    PRIMARY KEY (symbol, category),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);

-- Price data table
CREATE TABLE stock_prices (
    symbol VARCHAR(10),
    date DATE,
    open DECIMAL(12,2),
    high DECIMAL(12,2),
    low DECIMAL(12,2),
    close DECIMAL(12,2),
    volume BIGINT,
    PRIMARY KEY (symbol, date)
);
```

---

## Update Instructions

To update stock data:

1. **Add/Remove Stocks:**
   - Update `/api/stock-categories` endpoint data
   - Add stock info to `/api/stock-names` endpoint
   - No code changes needed!

2. **Modify Categories:**
   - Edit categories in the API response
   - Changes reflect immediately on all dashboards

3. **Update Stock Names:**
   - Modify name mappings in API
   - All dashboards will show updated names

4. **Example API Response File:**

Create `data/stock_categories.json`:
```json
{
  "categories": {
    "commodities": ["GOLD", "SILVER", "XAU", "XAG"],
    "blue_chips": ["VCB", "VHM", "VIC", ...],
    ...
  }
}
```

Create `data/stock_names.json`:
```json
{
  "VCB": "Vietcombank - Ngân hàng TMCP Ngoại Thương Việt Nam",
  "VHM": "Vinhomes - Công ty CP Vinhomes",
  ...
}
```

Then serve these files via the API endpoints!
