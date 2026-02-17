# Vietnamese Stock Analytics - API Reference

Complete REST API documentation for the Vietnamese Stock Analytics Platform.

**Base URL**: `http://localhost:5000` (development) or your deployment URL

---

## Table of Contents

1. [Authentication](#authentication)
2. [Stock Endpoints](#stock-endpoints)
3. [Market Endpoints](#market-endpoints)
4. [System Endpoints](#system-endpoints)
5. [Session Endpoints](#session-endpoints)
6. [Error Handling](#error-handling)
7. [Rate Limiting](#rate-limiting)

---

## Authentication

Currently, the API does not require authentication for read operations. Write operations (watchlist updates) use session-based storage.

**Future**: JWT-based authentication will be added for user-specific features.

---

## Stock Endpoints

### GET /api/stocks

Get list of all stocks in the database.

**Query Parameters**:
- `limit` (integer, optional): Maximum number of results. Default: 100
- `category` (string, optional): Filter by category (e.g., 'blue_chips', 'banks')
- `exchange` (string, optional): Filter by exchange ('HOSE', 'HNX', 'UPCOM')

**Response**: `200 OK`
```json
{
  "success": true,
  "stocks": [
    {
      "symbol": "VNM",
      "name": "Vinamilk",
      "exchange": "HOSE",
      "sector": "Consumer Goods",
      "category": "blue_chips",
      "market_cap": 123456789.00
    }
  ],
  "count": 31
}
```

**Error Responses**:
- `500 Internal Server Error`: Database connection error

---

### GET /api/stock/:symbol

Get detailed information for a specific stock.

**Path Parameters**:
- `symbol` (string, required): Stock symbol (e.g., 'VNM', 'FPT')

**Response**: `200 OK`
```json
{
  "success": true,
  "symbol": "VNM",
  "name": "Vinamilk",
  "date": "2026-02-17",
  "open": 85701.81,
  "high": 86242.23,
  "low": 83282.43,
  "price": 84985.62,
  "volume": 1901737,
  "change": -716.19,
  "change_percent": -0.6405
}
```

**Error Responses**:
- `404 Not Found`: Stock symbol not found
- `500 Internal Server Error`: Database error

---

### GET /api/stock/:symbol/history

Get historical price data for a stock.

**Path Parameters**:
- `symbol` (string, required): Stock symbol

**Query Parameters**:
- `days` (integer, optional): Number of days of history. Default: 30, Max: 365
  - Values < 1 return `400 Bad Request`
  - Values > 365 are automatically capped to 365

**Response**: `200 OK`
```json
{
  "success": true,
  "symbol": "VNM",
  "data": [
    {
      "date": "2026-01-19",
      "open": 85381.71,
      "high": 86315.70,
      "low": 85518.09,
      "close": 86100.51,
      "volume": 4352173,
      "change": 718.80,
      "change_percent": 1.5079
    }
  ],
  "count": 30
}
```

**Error Responses**:
- `400 Bad Request`: Invalid days parameter
- `500 Internal Server Error`: Failed to fetch historical data

---

### GET /api/latest

Get latest prices for all active stocks.

**Response**: `200 OK`
```json
{
  "success": true,
  "all_results": {
    "VNM": {
      "symbol": "VNM",
      "name": "Vinamilk",
      "date": "2026-02-17",
      "open": 85701.81,
      "high": 86242.23,
      "low": 83282.43,
      "close": 84985.62,
      "price": 84985.62,
      "volume": 1901737,
      "change": -716.19,
      "change_percent": -0.6405
    }
  },
  "timestamp": "2026-02-17T10:06:04.096234",
  "total": 1
}
```

---

### GET /api/latest-prices

Get latest prices (alternative format).

**Query Parameters**:
- `limit` (integer, optional): Maximum number of stocks. Default: 100

**Response**: Similar to `/api/latest` but in array format

---

### GET /api/stock-categories

Get list of stock categories with counts.

**Response**: `200 OK`
```json
{
  "success": true,
  "categories": {
    "blue_chips": ["VNM", "VCB", "FPT"],
    "banks": ["VCB", "ACB", "BID"],
    "tech": ["FPT", "CMG"]
  },
  "count": 3
}
```

---

### GET /api/stock-names

Get mapping of stock symbols to full names.

**Response**: `200 OK`
```json
{
  "VNM": "Vinamilk",
  "VCB": "Vietcombank",
  "FPT": "FPT Corporation"
}
```

---

## Market Endpoints

### GET /api/indices

Get latest market indices (VN-INDEX, VN30, HNX-INDEX).

**Response**: `200 OK`
```json
{
  "success": true,
  "indices": [
    {
      "index_code": "VN-INDEX",
      "index_name": "VN Index",
      "value": 1234.56,
      "change": 5.67,
      "change_percent": 0.46,
      "volume": 456789000,
      "date": "2026-02-17"
    }
  ]
}
```

---

### GET /api/watchlist

Get user's watchlist (from session storage).

**Response**: `200 OK`
```json
{
  "watchlist": ["VNM", "VCB", "FPT"],
  "is_default": false,
  "count": 3
}
```

**Notes**:
- If no watchlist is saved, returns default watchlist with `is_default: true`
- Default watchlist: ['VNM', 'VCB', 'FPT', 'HPG', 'VIC', 'VHM', 'GAS', 'ACB', 'BID', 'MSN']

---

### POST /api/watchlist

Update user's watchlist.

**Request Body**:
```json
{
  "watchlist": ["VNM", "FPT", "HPG"]
}
```

or simply:
```json
["VNM", "FPT", "HPG"]
```

**Response**: `200 OK`
```json
{
  "success": true,
  "message": "Watchlist updated successfully",
  "watchlist": ["VNM", "FPT", "HPG"],
  "count": 3
}
```

**Error Responses**:
- `400 Bad Request`: Invalid data format
- `500 Internal Server Error`: Server error

---

## System Endpoints

### GET /health

Health check endpoint for monitoring.

**Response**: `200 OK`
```json
{
  "status": "healthy",
  "database": "connected",
  "stocks": 31,
  "timestamp": "2026-02-17T07:06:22.106194"
}
```

**Error Responses**:
- `500 Internal Server Error`: System unhealthy
```json
{
  "status": "unhealthy",
  "error": "Database connection failed",
  "timestamp": "2026-02-17T07:06:22.106194"
}
```

---

### GET /api/system-status

Comprehensive system status including scheduler and data collection.

**Response**: `200 OK`
```json
{
  "timestamp": "2026-02-17T10:00:00",
  "overall": "healthy",
  "api": {
    "status": "online",
    "message": "API server is running"
  },
  "database": {
    "status": "connected",
    "message": "31 active stocks",
    "stock_count": 31,
    "latest_data": "2026-02-17"
  },
  "scheduler": {
    "status": "running",
    "message": "Scheduler is running (PID: 12345)",
    "pid": 12345
  },
  "data_collection": {
    "last_stock_update": "2026-02-17",
    "last_index_update": "2026-02-17",
    "last_macro_update": "2026-02-16",
    "stock_count_today": 29
  }
}
```

---

### GET /api/activity-log

Get system activity logs.

**Query Parameters**:
- `limit` (integer, optional): Maximum number of log entries. Default: 50
- `type` (string, optional): Filter by activity type ('system', 'collection', 'user', 'alert')

**Response**: `200 OK`
```json
{
  "success": true,
  "logs": [
    {
      "id": 1,
      "activity_type": "system",
      "activity": "Database migration",
      "details": "Added system_controls and activity_log tables",
      "status": "success",
      "timestamp": "2026-02-17T10:04:02",
      "user_id": null,
      "metadata": {}
    }
  ],
  "total": 1
}
```

---

### GET /api/controls

Get all system control settings.

**Response**: `200 OK`
```json
{
  "success": true,
  "settings": [],
  "signals": [],
  "states": [],
  "total": 8
}
```

---

### POST /api/jobs/trigger

Trigger a data collection job manually.

**Request Body**:
```json
{
  "job_type": "stock"
}
```

**Valid job types**: `"stock"`, `"macro"`

**Response**: `200 OK`
```json
{
  "success": true,
  "message": "Stock collection job triggered",
  "job_type": "stock"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid job type

---

## Session Endpoints

### GET /api/sessions/active

Get active planning sessions.

### GET /api/sessions/activity

Get recent session activity.

**Query Parameters**:
- `limit` (integer, optional): Maximum number of activities. Default: 20

### GET /api/sessions/stats

Get session statistics.

---

## Error Handling

All API endpoints follow consistent error response format:

### Standard Error Response
```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

### Common HTTP Status Codes

- `200 OK`: Request successful
- `400 Bad Request`: Invalid request parameters or body
- `404 Not Found`: Requested resource not found
- `500 Internal Server Error`: Server-side error

### Error Logging

All errors are logged server-side with:
- Timestamp
- Error type (ValueError, Exception, etc.)
- Stack trace (for debugging)
- Request context

Use `logger.error()` in production for troubleshooting.

---

## Rate Limiting

### Stock Data Collection

- **Guest Users**: 20 requests/minute (vnstock API limit)
- **Community Users**: 60 requests/minute (requires free API key)
- **Sponsor Users**: 180-600 requests/minute

### API Endpoints

No rate limiting currently implemented. Consider adding rate limiting for production:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["200 per hour", "50 per minute"]
)
```

---

## CORS Configuration

CORS is configured in `api/__init__.py`:

```python
CORS(app, resources={r"/*": {"origins": CORS_ORIGINS}}, supports_credentials=True)
```

**Allowed Origins** (from `config.py`):
- `http://localhost:8888`
- `http://127.0.0.1:8888`

For production, update `CORS_ORIGINS` in `.env`:
```bash
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

---

## Best Practices

### Request Headers

Always include:
```
Content-Type: application/json
Accept: application/json
```

### Error Handling in Client Code

```javascript
try {
  const response = await fetch('/api/stocks');
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data = await response.json();
  // Handle success
} catch (error) {
  console.error('API error:', error);
  // Show user-friendly error message
}
```

### Pagination

For large datasets, always use `limit` parameter:
```
GET /api/stocks?limit=50
GET /api/stock/VNM/history?days=30
```

---

## Support

- **Documentation**: `/docs/api/`
- **GitHub Issues**: Report bugs and request features
- **Email**: Contact your development team

---

**Last Updated**: February 17, 2026
**API Version**: 1.0
**Maintained by**: Vietnamese Stock Analytics Team
