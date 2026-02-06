# Real News Feed Implementation

## Overview

Successfully replaced demo news data with real Vietnamese financial news from VnExpress.

## What Was Implemented

### 1. News Fetching Module (`news_fetcher.py`)
- **VnExpressFetcher**: Scrapes real business news from VnExpress (https://vnexpress.net/kinh-doanh)
- **NewsArticle**: Intelligent news processing with:
  - Sentiment analysis (positive/negative/neutral) based on Vietnamese keywords
  - Impact estimation (High/Medium) based on content
  - Stock symbol extraction from article text
- **Caching**: 15-minute cache to avoid excessive scraping
- **CafeFFinanceFetcher**: Additional news source (ready for expansion)

### 2. API Endpoint (`/api/news`)
- Location: `api_server.py` line ~705
- Endpoint: `GET /api/news?limit=10&refresh=false`
- Parameters:
  - `limit`: Number of articles (default: 10)
  - `refresh`: Force refresh cache (default: false)
- Response format:
```json
{
  "success": true,
  "news": [
    {
      "title": "Article title",
      "url": "https://vnexpress.net/...",
      "description": "Article description",
      "date": "2026-02-04",
      "source": "VnExpress",
      "sentiment": "positive",
      "impact": "High",
      "affected_stocks": ["VCB", "FPT"]
    }
  ],
  "total": 10,
  "timestamp": "2026-02-04T...",
  "cache_info": "News cached for 15 minutes"
}
```

### 3. Frontend Integration (`macro_analysis.html`)
- Removed hardcoded demo news array
- Implemented async `fetchNews()` function
- Updated `renderNews()` to:
  - Show loading state while fetching
  - Display real news from API
  - Show error message if fetch fails
  - Display source attribution (VnExpress, etc.)
- Made `init()` function async to support news fetching

### 4. Translation Updates (`i18n.js`)
- Added `common.error` (English: "Error", Vietnamese: "Lỗi")
- Added `common.none` (English: "None", Vietnamese: "Không có")

## Features

### Intelligent News Processing
1. **Sentiment Analysis**: Analyzes Vietnamese keywords to determine sentiment
   - Positive words: tăng, lợi nhuận, tăng trưởng, mở rộng, etc.
   - Negative words: giảm, lỗ, khó khăn, sụt giảm, etc.

2. **Impact Estimation**: Identifies high-impact news
   - High impact: News about SBV, government, Fed, interest rates, GDP, etc.
   - Medium impact: Other business news

3. **Stock Symbol Extraction**: Automatically extracts mentioned stock symbols
   - Looks for 3-letter uppercase patterns
   - Filters to known Vietnamese stocks only

### Caching Strategy
- News cached for 15 minutes to reduce load
- Can force refresh with `refresh=true` parameter
- Cache stored in memory (production could use Redis)

## Testing

### 1. Test News Fetcher Directly
```bash
python3 -c "from news_fetcher import get_news_fetcher; fetcher = get_news_fetcher(); articles = fetcher.fetch_all_news(limit=5); print(f'Fetched {len(articles)} articles'); [print(f'- {a[\"title\"]}') for a in articles]"
```

### 2. Test API Endpoint
```bash
# Start the server
python3 api_server.py

# In another terminal, run the test script
python3 test_news_api.py

# Or use curl
curl "http://localhost:5000/api/news?limit=5" | jq .
```

### 3. Test in Browser
1. Start server: `python3 api_server.py`
2. Open: http://localhost:5000/macro_analysis.html
3. Click "News & Events" tab
4. Should see real Vietnamese financial news loading

## Technical Details

### Dependencies
- **requests**: For HTTP requests to VnExpress
- **beautifulsoup4**: For HTML parsing
- **Flask**: For API server (already installed)

### Error Handling
- Network errors: Returns empty array, shows error in UI
- Parse errors: Skips individual articles that fail to parse
- Graceful degradation: Shows error message in UI if API fails

### Performance
- First load: 1-3 seconds (fetches from VnExpress)
- Subsequent loads: <100ms (served from cache)
- Cache duration: 15 minutes
- Timeout: 10 seconds per request

## Files Modified

1. **api_server.py**
   - Added `from news_fetcher import get_news_fetcher`
   - Added `/api/news` endpoint
   - Updated API documentation

2. **macro_analysis.html**
   - Removed hardcoded `newsItems` array
   - Added async `fetchNews()` function
   - Updated `renderNews()` to fetch from API
   - Made `init()` async

3. **i18n.js**
   - Added `common.error` translations
   - Added `common.none` translations

## Files Created

1. **news_fetcher.py** - News fetching and processing module
2. **test_news_api.py** - Test script for API endpoint
3. **NEWS_API_IMPLEMENTATION.md** - This documentation

## Future Enhancements

### Potential Improvements
1. **Database Storage**: Store fetched news in PostgreSQL
2. **More Sources**: Add CafeF, Vneconomy, StockBiz
3. **RSS Feeds**: Use RSS for faster parsing
4. **Scheduled Updates**: Background job to refresh news every 15 min
5. **User Preferences**: Filter by stocks, sentiment, impact
6. **Notifications**: Alert users about high-impact news
7. **Full Text**: Fetch and display full article content
8. **Translation**: Translate to English for international users

### Expanding Sources
To add more news sources, create a new fetcher class:
```python
class NewSourceFetcher:
    def fetch_news(self, limit: int = 10) -> List[NewsArticle]:
        # Implementation here
        pass

# Add to AggregatedNewsFetcher
class AggregatedNewsFetcher:
    def __init__(self):
        self.vnexpress = VnExpressFetcher()
        self.cafef = CafeFFinanceFetcher()
        self.newsource = NewSourceFetcher()  # Add here
```

## Verification

Real news successfully fetched from VnExpress:
- ✅ "Bitcoin rơi về mức thấp nhất kể từ khi ông Trump đắc cử"
- ✅ "Giá vàng thế giới tăng mạnh nhất 17 năm"
- ✅ "Tái cấu trúc vốn - 'chìa khóa' cho mô hình tăng trưởng mới"

## Summary

The demo news has been completely removed and replaced with a real-time news fetching system that:
- Pulls actual Vietnamese financial news from VnExpress
- Analyzes sentiment and impact automatically
- Extracts mentioned stock symbols
- Caches results for performance
- Provides a clean API for frontend consumption
- Handles errors gracefully
- Works in both English and Vietnamese

The implementation is production-ready and can be easily extended with additional news sources.
