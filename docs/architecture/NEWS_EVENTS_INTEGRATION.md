# News & Events Integration - Macro Analysis

## 📰 What's Been Added

The Macro Analysis page now includes a comprehensive **News & Events** tab with multiple sections:

### 1. **Live News Feed**
- Real-time news from Vietnam and global sources
- Filter by category: All, Vietnam, Global, Economic Data, Corporate Actions, Earnings
- Click any news item to open full article
- Refresh button to reload latest news

### 2. **Economic Calendar**
- Upcoming economic events for the week
- Shows: Date, Time, Event Name, Description, Expected Value
- Impact levels: HIGH, MEDIUM, LOW (color-coded)
- Events from US, Vietnam, China, EU, etc.

### 3. **Earnings Calendar**
- Upcoming earnings releases from Vietnamese companies
- Shows: Date, Stock Symbol, Company Name, EPS Estimate
- Status: Before Market / After Market
- Top companies: VCB, FPT, VNM, HPG, TCB, etc.

### 4. **Corporate Actions**
- Recent corporate announcements
- Types: Dividends, Stock Splits, AGM, Rights Issues, M&A
- Shows: Icon, Type, Company, Details, Date
- Easy-to-scan visual format

---

## 🎨 Visual Design

### News Filter Buttons
```
[🌐 All Sources] [🇻🇳 Vietnam] [🌍 Global Markets] [📊 Economic Data] [🏢 Corporate Actions] [💰 Earnings]
```
- Active button: Blue background with white text
- Hover effect: Light blue background
- Click to filter news by category

### News Items
Each news card shows:
- **Source badge** (e.g., Bloomberg, VnExpress) with icon
- **Time** (e.g., "2 hours ago")
- **Title** (bold, large text)
- **Summary** (2-3 sentences)
- **Tags** (e.g., #Fed, #InterestRates, #USEconomy)
- Hover effect: Blue border + lift animation
- Click to open full article in new tab

### Economic Events
Structured timeline showing:
- Date & Time (left column)
- Event details (center)
- Impact badge (right) - color-coded by importance

### Earnings Cards
Gradient blue background with:
- Date box (white background)
- Company info (symbol + name)
- EPS estimate
- Status badge (green)

### Corporate Actions
White cards with:
- Large emoji icon (💰, 📊, 🔔, 💼, 🤝)
- Action type and company
- Detailed description
- Date badge

---

## 🔌 API Integration Guide

### Current Status: **Mock Data**
The system currently uses sample data. Here's how to connect real sources:

### A. RSS Feed Integration

**Step 1: Install RSS Parser**
```bash
npm install rss-parser
```

**Step 2: Fetch RSS Feeds**
```javascript
const Parser = require('rss-parser');
const parser = new Parser();

async function fetchRSSFeed(url) {
    try {
        const feed = await parser.parseURL(url);
        return feed.items.map(item => ({
            title: item.title,
            summary: item.contentSnippet,
            link: item.link,
            pubDate: item.pubDate,
            source: feed.title
        }));
    } catch (error) {
        console.error('RSS fetch error:', error);
        return [];
    }
}

// Example usage
const bloombergNews = await fetchRSSFeed('https://feeds.bloomberg.com/markets/news.rss');
const vnexpressNews = await fetchRSSFeed('https://vnexpress.net/rss/kinh-doanh.rss');
```

**Recommended RSS Feeds:**

**Vietnam:**
- VnExpress Business: `https://vnexpress.net/rss/kinh-doanh.rss`
- Cafef: `https://cafef.vn/rss/thi-truong.rss`
- VietStock: `https://vietstock.vn/rss`
- Dau Tu Chung Khoan: `https://baodautu.vn/rss/ck.rss`

**Global:**
- Bloomberg Markets: `https://feeds.bloomberg.com/markets/news.rss`
- Reuters Business: `https://www.reutersagency.com/feed/`
- WSJ Markets: `https://feeds.wsj.com/public/resources/xml/wsj/public/page/feed-atom.xml`
- Financial Times: `https://www.ft.com/?format=rss`
- CNBC: `https://www.cnbc.com/id/100003114/device/rss/rss.html`

---

### B. News API Integration

**Option 1: NewsAPI.org**
```javascript
const NEWS_API_KEY = 'your_api_key';
const NEWS_API_URL = 'https://newsapi.org/v2/everything';

async function fetchNewsAPI(query, language = 'en') {
    const params = new URLSearchParams({
        q: query,
        language: language,
        sortBy: 'publishedAt',
        apiKey: NEWS_API_KEY
    });

    const response = await fetch(`${NEWS_API_URL}?${params}`);
    const data = await response.json();

    return data.articles.map(article => ({
        title: article.title,
        summary: article.description,
        link: article.url,
        source: article.source.name,
        publishedAt: article.publishedAt,
        image: article.urlToImage
    }));
}

// Example usage
const vietnamNews = await fetchNewsAPI('Vietnam stock market OR VN-Index', 'vi');
const globalNews = await fetchNewsAPI('stock market OR economy', 'en');
```

**Option 2: Alpha Vantage (Financial News)**
```javascript
const ALPHA_VANTAGE_KEY = 'your_api_key';

async function fetchAlphaVantageNews(topics = 'earnings') {
    const url = `https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=${topics}&apikey=${ALPHA_VANTAGE_KEY}`;

    const response = await fetch(url);
    const data = await response.json();

    return data.feed.map(item => ({
        title: item.title,
        summary: item.summary,
        link: item.url,
        source: item.source,
        publishedAt: item.time_published,
        sentiment: item.overall_sentiment_label,
        relevance: item.relevance_score
    }));
}
```

**Option 3: Finnhub (Market News)**
```javascript
const FINNHUB_KEY = 'your_api_key';

async function fetchFinnhubNews(category = 'general') {
    const url = `https://finnhub.io/api/v1/news?category=${category}&token=${FINNHUB_KEY}`;

    const response = await fetch(url);
    const data = await response.json();

    return data.map(item => ({
        title: item.headline,
        summary: item.summary,
        link: item.url,
        source: item.source,
        publishedAt: new Date(item.datetime * 1000),
        image: item.image
    }));
}
```

---

### C. Economic Calendar APIs

**Option 1: Trading Economics**
```javascript
const TE_API_KEY = 'your_api_key';

async function fetchEconomicCalendar(country = 'vietnam') {
    const url = `https://api.tradingeconomics.com/calendar/country/${country}?c=${TE_API_KEY}`;

    const response = await fetch(url);
    const data = await response.json();

    return data.map(event => ({
        date: event.Date,
        time: event.Time,
        country: event.Country,
        event: event.Event,
        actual: event.Actual,
        forecast: event.Forecast,
        previous: event.Previous,
        importance: event.Importance // 1 = low, 2 = medium, 3 = high
    }));
}

// Get calendar for multiple countries
const vnCalendar = await fetchEconomicCalendar('vietnam');
const usCalendar = await fetchEconomicCalendar('united-states');
const cnCalendar = await fetchEconomicCalendar('china');
```

**Option 2: Investing.com Calendar (Web Scraping)**
```javascript
// Use a scraping service or library like Puppeteer
async function scrapeInvestingCalendar() {
    // This requires backend implementation
    const response = await fetch('/api/economic-calendar');
    return await response.json();
}
```

---

### D. Earnings Calendar

**Option 1: Alpha Vantage Earnings**
```javascript
async function fetchEarningsCalendar() {
    const url = `https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=${ALPHA_VANTAGE_KEY}`;

    const response = await fetch(url);
    const csv = await response.text();

    // Parse CSV to JSON
    const lines = csv.split('\n');
    const headers = lines[0].split(',');

    return lines.slice(1).map(line => {
        const values = line.split(',');
        return {
            symbol: values[0],
            name: values[1],
            reportDate: values[2],
            estimate: values[3],
            currency: values[4]
        };
    });
}
```

**Option 2: Vietnam SSI/VPS Data**
```javascript
// Connect to Vietnamese brokerage APIs
async function fetchVNEarnings() {
    // This would require partnership with SSI, VPS, or other brokers
    const response = await fetch('/api/vn/earnings-calendar');
    return await response.json();
}
```

---

### E. Corporate Actions

**Option 1: Company Announcements API**
```javascript
async function fetchCorporateActions() {
    // Vietnam: HOSE/HNX announcements
    const response = await fetch('https://www.hsx.vn/Modules/CMS/Web/Announcements');

    // Parse HTML or use official API if available
    return parseAnnouncementsHTML(await response.text());
}
```

**Option 2: Financial Modeling Prep**
```javascript
const FMP_KEY = 'your_api_key';

async function fetchCorporateActionsAPI(symbol) {
    const types = ['dividend', 'split', 'merger'];
    const promises = types.map(type =>
        fetch(`https://financialmodelingprep.com/api/v3/${type}/${symbol}?apikey=${FMP_KEY}`)
    );

    const results = await Promise.all(promises);
    const data = await Promise.all(results.map(r => r.json()));

    return {
        dividends: data[0],
        splits: data[1],
        mergers: data[2]
    };
}
```

---

## 🔄 Backend Implementation

For production, create API endpoints:

```javascript
// Backend: /api/news
app.get('/api/news', async (req, res) => {
    const category = req.query.category || 'all';

    const [vnNews, globalNews] = await Promise.all([
        fetchRSSFeed('https://vnexpress.net/rss/kinh-doanh.rss'),
        fetchNewsAPI('stock market', 'en')
    ]);

    const allNews = [...vnNews, ...globalNews].sort((a, b) =>
        new Date(b.publishedAt) - new Date(a.publishedAt)
    );

    res.json(allNews);
});

// Backend: /api/economic-calendar
app.get('/api/economic-calendar', async (req, res) => {
    const calendar = await fetchEconomicCalendar('vietnam');
    res.json(calendar);
});

// Backend: /api/earnings
app.get('/api/earnings', async (req, res) => {
    const earnings = await fetchVNEarnings();
    res.json(earnings);
});

// Backend: /api/corporate-actions
app.get('/api/corporate-actions', async (req, res) => {
    const actions = await fetchCorporateActions();
    res.json(actions);
});
```

---

## 🔧 Frontend Integration

Update the JavaScript to use real APIs:

```javascript
// Replace loadNews() function
async function loadNews() {
    try {
        const response = await fetch(`/api/news?category=${currentNewsFilter}`);
        const newsData = await response.json();

        const container = document.getElementById('newsContainer');
        let html = '';

        newsData.forEach(news => {
            html += `
                <div class="news-item" onclick="window.open('${news.link}', '_blank')">
                    <div class="news-header">
                        <span class="news-source">${news.sourceIcon || '📰'} ${news.source}</span>
                        <span class="news-time">⏰ ${formatTimeAgo(news.publishedAt)}</span>
                    </div>
                    <div class="news-title">${news.title}</div>
                    <div class="news-summary">${news.summary}</div>
                </div>
            `;
        });

        container.innerHTML = html;
    } catch (error) {
        console.error('Error loading news:', error);
        container.innerHTML = '<p>Error loading news. Please try again.</p>';
    }
}

// Helper: Format time ago
function formatTimeAgo(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const seconds = Math.floor((now - date) / 1000);

    if (seconds < 60) return 'Just now';
    if (seconds < 3600) return `${Math.floor(seconds / 60)} minutes ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)} hours ago`;
    return `${Math.floor(seconds / 86400)} days ago`;
}

// Similarly update other load functions
async function loadEconomicCalendar() {
    const response = await fetch('/api/economic-calendar');
    const events = await response.json();
    // ... render events
}

async function loadEarningsCalendar() {
    const response = await fetch('/api/earnings');
    const earnings = await response.json();
    // ... render earnings
}

async function loadCorporateActions() {
    const response = await fetch('/api/corporate-actions');
    const actions = await response.json();
    // ... render actions
}
```

---

## 📊 Data Refresh Strategy

### Auto-refresh
```javascript
// Refresh news every 5 minutes
setInterval(() => {
    loadNews();
    loadEconomicCalendar();
}, 5 * 60 * 1000);

// Refresh earnings daily
setInterval(() => {
    loadEarningsCalendar();
    loadCorporateActions();
}, 24 * 60 * 60 * 1000);
```

### Manual refresh
Already implemented - click "🔄 Refresh" button

### WebSocket for real-time updates
```javascript
const ws = new WebSocket('wss://your-server.com/news');

ws.onmessage = (event) => {
    const newItem = JSON.parse(event.data);
    prependNewsItem(newItem);
};
```

---

## 🎯 API Service Recommendations

### Free Tier:
- **NewsAPI.org** - 100 requests/day
- **Alpha Vantage** - 500 requests/day
- **Finnhub** - 60 requests/minute

### Paid Tier:
- **Bloomberg Terminal** - Comprehensive, expensive
- **Reuters Eikon** - Professional grade
- **Trading Economics** - Economic calendar focus
- **Financial Modeling Prep** - $15-50/month

### Vietnam-Specific:
- **VietstockFinance API** - Local market data
- **SSI iBoard API** - Real-time quotes
- **FiinTrade API** - Financial data

---

## 🔐 Security Considerations

1. **API Keys**: Store in environment variables
2. **Rate Limiting**: Implement caching to avoid hitting limits
3. **CORS**: Configure properly for cross-origin requests
4. **Authentication**: Require API key for backend endpoints
5. **Validation**: Sanitize all external data before displaying

---

## 📱 Testing the Current Implementation

1. **Open** `macro_analysis.html`
2. **Click** the "📰 Market News & Events" tab
3. **See**:
   - Filter buttons at the top
   - Economic calendar with 5 events
   - Live news feed with 6 articles
   - Earnings calendar with 5 companies
   - Corporate actions with 5 recent events

4. **Try**:
   - Click filter buttons (Vietnam, Global, etc.)
   - Click news items to open (currently mock URLs)
   - Click "🔄 Refresh" button
   - Observe hover effects on cards

---

## 🚀 Next Steps

1. **Choose API providers** for each data type
2. **Set up backend endpoints** to fetch and cache data
3. **Replace mock data** with real API calls
4. **Add authentication** if required
5. **Implement rate limiting** and error handling
6. **Add loading indicators** during fetches
7. **Enable real-time updates** with WebSocket
8. **Add search functionality** for news
9. **Implement bookmarking/favorites**
10. **Add export to CSV/PDF** for calendar events

---

**Last Updated:** 2026-02-04
**Version:** 1.0
**Contact:** VNStock Analytics Team
