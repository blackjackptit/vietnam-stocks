#!/usr/bin/env python3
"""
Test script for the news API endpoint
Run this after starting the server: python3 api_server.py
Then: python3 test_news_api.py
"""

import requests

def test_news_api():
    """Test the /api/news endpoint"""

    print("Testing News API Endpoint")
    print("=" * 60)

    try:
        # Test the endpoint
        response = requests.get('http://localhost:5000/api/news?limit=5', timeout=10)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()

            print(f"Success: {data.get('success')}")
            print(f"Total Articles: {data.get('total')}")
            print(f"Cache Info: {data.get('cache_info')}")
            print("\nArticles:")
            print("-" * 60)

            for i, article in enumerate(data.get('news', []), 1):
                print(f"\n{i}. {article.get('title')}")
                print(f"   Date: {article.get('date')}")
                print(f"   Source: {article.get('source')}")
                print(f"   Sentiment: {article.get('sentiment')}")
                print(f"   Impact: {article.get('impact')}")
                print(f"   Affected Stocks: {', '.join(article.get('affected_stocks', []))}")
                print(f"   URL: {article.get('url')}")

            print("\n" + "=" * 60)
            print("✅ News API is working correctly!")

        else:
            print(f"❌ Error: {response.text}")

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure api_server.py is running:")
        print("   python3 api_server.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_news_api()
