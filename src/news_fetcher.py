#!/usr/bin/env python3
"""
Vietnamese Financial News Fetcher
Fetches real news from VnExpress and other Vietnamese financial news sources
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict
import re

class NewsArticle:
    def __init__(self, title: str, url: str, description: str = "",
                 date: str = None, source: str = "VnExpress"):
        self.title = title
        self.url = url
        self.description = description
        self.date = date or datetime.now().strftime('%Y-%m-%d')
        self.source = source
        self.sentiment = self._analyze_sentiment()
        self.impact = self._estimate_impact()
        self.affected_stocks = self._extract_stocks()

    def _analyze_sentiment(self) -> str:
        """Simple sentiment analysis based on keywords"""
        text = (self.title + " " + self.description).lower()

        positive_words = ['tăng', 'lợi nhuận', 'tăng trưởng', 'mở rộng', 'thành công',
                         'phát triển', 'khả quan', 'cải thiện', 'đột phá', 'hợp tác']
        negative_words = ['giảm', 'lỗ', 'khó khăn', 'sụt giảm', 'khủng hoảng',
                         'thất bại', 'đình trệ', 'rủi ro', 'bất ổn', 'giảm sút']

        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)

        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        return 'neutral'

    def _estimate_impact(self) -> str:
        """Estimate market impact based on title keywords"""
        text = (self.title + " " + self.description).lower()

        high_impact = ['ngân hàng nhà nước', 'chính phủ', 'fed', 'lãi suất',
                      'gdp', 'tỷ giá', 'xuất khẩu', 'nhập khẩu']

        if any(word in text for word in high_impact):
            return 'High'

        return 'Medium'

    def _extract_stocks(self) -> List[str]:
        """Extract stock symbols from title and description"""
        text = self.title + " " + self.description

        # Common Vietnamese stock symbols pattern (3 letters, uppercase)
        symbols = re.findall(r'\b([A-Z]{3})\b', text)

        # Filter to known major stocks only
        known_stocks = ['VNM', 'VCB', 'FPT', 'HPG', 'VIC', 'VHM', 'GAS', 'MSN',
                       'ACB', 'BID', 'TCB', 'MBB', 'VPB', 'CTG', 'STB', 'MWG',
                       'VRE', 'PLX', 'POW', 'SAB', 'SSI', 'HDB', 'VJC', 'GMD']

        return [s for s in symbols if s in known_stocks]

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON response"""
        return {
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'date': self.date,
            'source': self.source,
            'sentiment': self.sentiment,
            'impact': self.impact,
            'affected_stocks': self.affected_stocks
        }


class VnExpressFetcher:
    """Fetches news from VnExpress business section"""

    BASE_URL = "https://vnexpress.net"
    BUSINESS_URL = "https://vnexpress.net/kinh-doanh"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

    def fetch_news(self, limit: int = 10) -> List[NewsArticle]:
        """Fetch latest business news from VnExpress"""
        try:
            response = self.session.get(self.BUSINESS_URL, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            articles = []

            # VnExpress uses article.item-news class for news items
            news_items = soup.find_all('article', class_='item-news', limit=limit * 2)

            for item in news_items:
                if len(articles) >= limit:
                    break

                try:
                    # Find title and link
                    title_tag = item.find('h3', class_='title-news') or item.find('h2', class_='title-news')
                    if not title_tag:
                        continue

                    link_tag = title_tag.find('a')
                    if not link_tag:
                        continue

                    title = link_tag.get('title', '').strip()
                    url = link_tag.get('href', '').strip()

                    if not title or not url:
                        continue

                    # Make URL absolute
                    if url.startswith('/'):
                        url = self.BASE_URL + url

                    # Find description
                    desc_tag = item.find('p', class_='description')
                    description = desc_tag.get_text(strip=True) if desc_tag else ""

                    # Find date
                    date_tag = item.find('span', class_='time')
                    date_str = None
                    if date_tag:
                        date_text = date_tag.get_text(strip=True)
                        # Parse Vietnamese date format
                        date_str = self._parse_date(date_text)

                    article = NewsArticle(
                        title=title,
                        url=url,
                        description=description,
                        date=date_str,
                        source="VnExpress"
                    )

                    articles.append(article)

                except Exception as e:
                    # Skip individual items that fail
                    continue

            return articles

        except Exception as e:
            print(f"Error fetching VnExpress news: {e}")
            return []

    def _parse_date(self, date_text: str) -> str:
        """Parse Vietnamese date format to ISO format"""
        try:
            # Format like "15 giờ trước", "2 ngày trước", "Thứ hai, 3/2/2026"
            if 'giờ trước' in date_text:
                hours = int(re.search(r'(\d+)', date_text).group(1))
                date = datetime.now() - timedelta(hours=hours)
                return date.strftime('%Y-%m-%d')
            elif 'ngày trước' in date_text:
                days = int(re.search(r'(\d+)', date_text).group(1))
                date = datetime.now() - timedelta(days=days)
                return date.strftime('%Y-%m-%d')
            elif 'phút trước' in date_text:
                return datetime.now().strftime('%Y-%m-%d')
            else:
                # Try to parse date format like "3/2/2026"
                match = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_text)
                if match:
                    day, month, year = match.groups()
                    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        except:
            pass

        return datetime.now().strftime('%Y-%m-%d')


class CafeFFinanceFetcher:
    """Fetches news from CafeF finance section"""

    BASE_URL = "https://cafef.vn"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

    def fetch_news(self, limit: int = 5) -> List[NewsArticle]:
        """Fetch latest financial news from CafeF"""
        try:
            response = self.session.get(self.BASE_URL, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            articles = []

            # CafeF uses different structure, find article links
            news_items = soup.find_all('h3', limit=limit * 2)

            for item in news_items:
                if len(articles) >= limit:
                    break

                try:
                    link_tag = item.find('a')
                    if not link_tag:
                        continue

                    title = link_tag.get('title', '').strip() or link_tag.get_text(strip=True)
                    url = link_tag.get('href', '').strip()

                    if not title or not url:
                        continue

                    # Make URL absolute
                    if url.startswith('/'):
                        url = self.BASE_URL + url

                    article = NewsArticle(
                        title=title,
                        url=url,
                        description="",
                        date=datetime.now().strftime('%Y-%m-%d'),
                        source="CafeF"
                    )

                    articles.append(article)

                except Exception:
                    continue

            return articles

        except Exception as e:
            print(f"Error fetching CafeF news: {e}")
            return []


class AggregatedNewsFetcher:
    """Aggregates news from multiple sources"""

    def __init__(self):
        self.vnexpress = VnExpressFetcher()
        self.cafef = CafeFFinanceFetcher()
        self._cache = []
        self._cache_time = None
        self._cache_duration = timedelta(minutes=15)  # Cache for 15 minutes

    def fetch_all_news(self, limit: int = 10, force_refresh: bool = False) -> List[Dict]:
        """Fetch news from all sources with caching"""

        # Return cached data if still valid
        if not force_refresh and self._cache and self._cache_time:
            if datetime.now() - self._cache_time < self._cache_duration:
                return self._cache[:limit]

        # Fetch fresh news
        all_articles = []

        # Fetch from VnExpress (primary source)
        vnexpress_articles = self.vnexpress.fetch_news(limit=limit)
        all_articles.extend(vnexpress_articles)

        # Optionally add CafeF articles
        # cafef_articles = self.cafef.fetch_news(limit=max(5, limit // 2))
        # all_articles.extend(cafef_articles)

        # Convert to dict and cache
        self._cache = [article.to_dict() for article in all_articles]
        self._cache_time = datetime.now()

        return self._cache[:limit]


# Global instance for reuse
_news_fetcher = None

def get_news_fetcher() -> AggregatedNewsFetcher:
    """Get or create global news fetcher instance"""
    global _news_fetcher
    if _news_fetcher is None:
        _news_fetcher = AggregatedNewsFetcher()
    return _news_fetcher
