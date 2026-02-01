#!/usr/bin/env python3
"""
API Connectivity Test
Tests connectivity to Vietnamese stock data APIs
"""

import requests
import json
from datetime import datetime

def test_vndirect():
    """Test VNDirect API"""
    print("=" * 70)
    print("Testing VNDirect API")
    print("=" * 70)

    try:
        url = "https://finfo-api.vndirect.com.vn/v4/stock_prices"
        params = {'symbols': 'VNM', 'sort': 'date', 'size': 1}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://vndirect.com.vn/'
        }

        print(f"URL: {url}")
        print(f"Params: {params}")
        print("Sending request (30s timeout)...")

        response = requests.get(url, params=params, headers=headers, timeout=30)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS! Received data:")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
            return True
        else:
            print(f"❌ FAILED: Status {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False

    except requests.exceptions.Timeout:
        print("❌ TIMEOUT: Connection timed out after 30 seconds")
        print("   This suggests the API is not reachable from your network")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"❌ CONNECTION ERROR: {e}")
        print("   The API server may be down or blocking your IP")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def test_ssi():
    """Test SSI API"""
    print("\n" + "=" * 70)
    print("Testing SSI API")
    print("=" * 70)

    try:
        url = "https://iboard-api.ssi.com.vn/statistics/charts/stock"
        params = {'symbols': 'VNM', 'resolution': 'D', 'limit': 1}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json'
        }

        print(f"URL: {url}")
        print(f"Params: {params}")
        print("Sending request (30s timeout)...")

        response = requests.get(url, params=params, headers=headers, timeout=30)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS! Received data:")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
            return True
        else:
            print(f"❌ FAILED: Status {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False

    except requests.exceptions.Timeout:
        print("❌ TIMEOUT: Connection timed out after 30 seconds")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"❌ CONNECTION ERROR: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def test_basic_connectivity():
    """Test basic internet connectivity"""
    print("\n" + "=" * 70)
    print("Testing Basic Internet Connectivity")
    print("=" * 70)

    try:
        response = requests.get("https://www.google.com", timeout=10)
        if response.status_code == 200:
            print("✅ Internet connection is working")
            return True
        else:
            print("⚠️  Unusual response from google.com")
            return False
    except Exception as e:
        print(f"❌ No internet connection: {e}")
        return False


def main():
    print("\n" + "=" * 70)
    print("📡 Vietnamese Stock API Connectivity Test")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Test basic connectivity
    internet_ok = test_basic_connectivity()

    if not internet_ok:
        print("\n❌ Cannot proceed without internet connection")
        return

    # Test VNDirect
    vndirect_ok = test_vndirect()

    # Test SSI
    ssi_ok = test_ssi()

    # Summary
    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"Internet: {'✅ Working' if internet_ok else '❌ Failed'}")
    print(f"VNDirect API: {'✅ Working' if vndirect_ok else '❌ Failed'}")
    print(f"SSI API: {'✅ Working' if ssi_ok else '❌ Failed'}")

    if not vndirect_ok and not ssi_ok:
        print("\n⚠️  TROUBLESHOOTING:")
        print("   1. Check if you're behind a firewall/VPN")
        print("   2. Vietnamese stock APIs may be geo-restricted")
        print("   3. Try running from a Vietnamese IP address")
        print("   4. APIs may be temporarily down")
        print("   5. Consider using a VPN with Vietnamese server")
    elif vndirect_ok or ssi_ok:
        print("\n✅ At least one API is working!")
        print("   The data collection jobs should work now.")

    print("=" * 70)


if __name__ == '__main__':
    main()
