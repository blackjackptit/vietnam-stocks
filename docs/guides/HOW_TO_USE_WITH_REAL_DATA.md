# How to Use With Real Vietnamese Stock Data

The VNDirect API requires Vietnam network access. Here are your options:

## Option 1: Use VPN with Vietnam Server (Recommended)

### Free VPN Options:
- **ProtonVPN** - Has Vietnam servers on paid plan
- **Windscribe** - Offers Vietnam location
- **NordVPN** - Multiple Vietnam servers

### Steps:
1. Connect to VPN with Vietnam server
2. Run: `python monitor.py --scan-once`
3. Wait for real data to load

## Option 2: Run From Vietnam Network

If you're physically in Vietnam:
```bash
python monitor.py --scan-once
python monitor.py --interval 15  # Continuous monitoring
```

## Option 3: Use Alternative APIs

### SSI iBoard API (Alternative)

Edit `src/stock_data.py` and add:

```python
SSI_API = "https://iboard-api.ssi.com.vn/statistics/charts/symbols/{symbol}"

def get_stock_price_ssi(self, symbol: str):
    """Get price from SSI API"""
    try:
        url = self.SSI_API.format(symbol=symbol)
        response = self.session.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Parse SSI response format
            return {
                'symbol': symbol,
                'price': data.get('price'),
                # ... map other fields
            }
    except Exception as e:
        print(f"Error: {e}")
    return None
```

### Web Scraping (Last Resort)

You can scrape data from:
- https://www.cophieu68.vn/
- https://www.vndirect.com.vn/
- https://chart.vps.com.vn/

**Note:** Respect robots.txt and rate limits.

## Option 4: Use Demo Mode for Learning

```bash
python demo_monitor.py --scan-once
python demo_monitor.py --interval 15
```

This uses realistic mock data to:
- ✅ Learn how the tool works
- ✅ Test strategies without real data
- ✅ Understand technical indicators
- ✅ See recommendation logic

## Option 5: Manual Data Entry

Create a file `data/manual_prices.json`:

```json
{
  "VPB": {"price": 23500, "volume": 1500000},
  "FPT": {"price": 118500, "volume": 890000},
  "STB": {"price": 28300, "volume": 2100000}
}
```

Then load it in the tool (requires minor code modification).

## Option 6: Use Excel/CSV Import

1. Export data from SSI iBoard or VNDirect
2. Save as CSV:
   ```
   Symbol,Price,Change%,Volume
   VPB,23500,+2.5,1500000
   FPT,118500,-1.2,890000
   ```
3. Import in Python and run analysis

## Check If API Is Working

Test connection:

```bash
python3 << 'EOF'
from src.stock_data import VNStockData

fetcher = VNStockData()
result = fetcher.get_stock_price('VCB')

if result:
    print(f"✅ API working! VCB: {result['price']} VND")
else:
    print("❌ API not accessible from your location")
    print("Use VPN with Vietnam server or demo mode")
EOF
```

## Real-Time Data Sources (When API Works)

Once connected to Vietnam network, the tool will fetch from:

### VNDirect API
- **Endpoint:** `https://finfo-api.vndirect.com.vn/v4/stock_prices`
- **Coverage:** HSX, HNX, UPCOM
- **Delay:** ~15 minutes
- **Free:** Yes
- **Rate Limit:** ~100 requests/minute

### What You'll Get:
```json
{
  "symbol": "VPB",
  "price": 23500,
  "change": 550,
  "change_percent": 2.4,
  "volume": 1850000000,
  "high": 23800,
  "low": 23100,
  "open": 23200
}
```

## Broker Platforms with APIs

If you have an account with these brokers, they may offer API access:

1. **SSI Securities**
   - iBoard API
   - Trading API (for customers)

2. **VNDirect**
   - Financial Info API (what we use)
   - Trading API (for customers)

3. **TCBS**
   - Market data API
   - Trading API

4. **HSC**
   - Limited API access

**Contact your broker** to request API credentials.

## Compare: Demo vs Real Data

| Feature | Demo Mode | Real API |
|---------|-----------|----------|
| Price data | Simulated | Live prices |
| Historical data | Generated | Actual history |
| Volume | Random | Real trading volume |
| Indicators | Calculated correctly | Calculated correctly |
| Recommendations | Based on demo | Based on real market |
| Learning | ✅ Perfect | ✅ Perfect |
| Trading | ❌ Don't use | ✅ Can use |

## Recommended Workflow

### For Learning (Week 1-2)
```bash
# Use demo mode to learn the tool
python demo_monitor.py --scan-once
python demo_monitor.py --interval 15
```

### For Analysis (Week 3+)
```bash
# Connect VPN to Vietnam
# Then use real data
python monitor.py --scan-once
python monitor.py --interval 15
```

### For Trading (When Ready)
1. Paper trade for 1 month (simulated)
2. Start with 5M VND real money
3. Monitor with real-time tool
4. Follow recommendations but verify manually
5. Set stop-loss at -10%

## Troubleshooting Real API

### Connection Timeout
```
Error: Connection timeout
```
**Solution:** Use VPN with Vietnam server

### Rate Limiting
```
Error: 429 Too Many Requests
```
**Solution:** Increase sleep time between requests in code

### Invalid Symbol
```
Error: No data for symbol
```
**Solution:** Check symbol is correct (uppercase, HSX/HNX listing)

### API Changed
If API stops working:
1. Check VNDirect website for announcements
2. Try alternative endpoints
3. Use web scraping as backup
4. Switch to SSI API

## Next Steps

1. **Try demo mode now:**
   ```bash
   python demo_monitor.py --scan-once
   ```

2. **Get VPN with Vietnam server** (for real data)

3. **Open broker account:**
   - SSI Securities
   - VNDirect
   - TCBS

4. **Start paper trading** (practice without real money)

5. **When comfortable, invest small** (1-2M VND first)

---

**Current Status:** Demo mode working ✅

**To use real data:** Get Vietnam IP (VPN or local network)
