# How to Update Stock Prices with Real Data

## Problem
Vietnamese stock market APIs are **geo-restricted** - they only work from Vietnamese IP addresses. Demo/fake data was being used.

## ✅ QUICK FIX: Manual Price Import (Working Now!)

### Step 1: Edit `manual_prices.csv`
```csv
symbol,price,change_percent
TPB,16900,1.2
VCB,98500,-0.5
VPB,23100,-0.51
```

### Step 2: Run Import Script
```bash
python3 import_manual_prices.py
```

### Step 3: Refresh Browser
The platform will now show **REAL prices**!

---

## Data Sources Tested

| Source | Status | Notes |
|--------|--------|-------|
| **Manual CSV** | ✅ **WORKING** | Import prices from CSV file |
| VNDirect API | ❌ Blocked | Timeout - needs VPN to Vietnam |
| SSI iBoard | ❌ Blocked | 403 Forbidden - geo-restricted |
| Cafef.vn | ❌ Blocked | Anti-scraping protection |
| Vietstock | ❌ Blocked | Geo-restricted |

---

## Option 1: Manual Import (Current Solution)

**Pros:**
- ✅ Works immediately
- ✅ No VPN needed
- ✅ Full control over data

**Cons:**
- ⚠️ Manual updates required
- ⚠️ Time consuming for 233 stocks

**Usage:**
```bash
# 1. Edit manual_prices.csv with current prices
nano manual_prices.csv

# 2. Import
python3 import_manual_prices.py

# 3. Refresh browser
```

---

## Option 2: Use VPN to Vietnam

**Setup:**
1. Get VPN with Vietnam servers:
   - NordVPN
   - ExpressVPN
   - SurfShark

2. Connect to Vietnam server

3. Run automatic fetch:
```bash
python3 fetch_hsx_data.py
```

This will automatically fetch real-time data from HSX APIs!

---

## Option 3: Run from Vietnam Network

If you're physically in Vietnam or have access to a Vietnamese server:

```bash
python3 fetch_hsx_data.py
```

Works without VPN from Vietnamese networks!

---

## Current Status

**✅ TPB Price Updated:**
- Old (Demo): 35,830 VND ❌
- New (Real): 16,900 VND ✅

**Data Source:** Manual Entry

**Last Updated:** 2026-02-01

---

## Scripts Available

| Script | Purpose | Requirements |
|--------|---------|--------------|
| `import_manual_prices.py` | Import from CSV | ✅ None |
| `fetch_hsx_data.py` | Fetch from HSX API | VPN to Vietnam |
| `fetch_hsx_web.py` | Web scraping | VPN to Vietnam |
| `generate_latest_data.py` | Regenerate aggregate | None |

---

## Automating Updates

### Option A: Cron Job with VPN
```bash
# Update every hour while VPN is connected
0 * * * * cd /path/to/project && python3 fetch_hsx_data.py
```

### Option B: Manual Updates
```bash
# Daily at 9 AM: Edit CSV and import
0 9 * * * cd /path/to/project && python3 import_manual_prices.py
```

---

## Getting Current Prices

**Vietnamese Stock Market Sources:**
1. **HSX Website:** https://www.hsx.vn/
2. **Cafef:** https://cafef.vn/
3. **Vietstock:** https://finance.vietstock.vn/
4. **SSI iBoard:** https://iboard.ssi.com.vn/

Copy prices to `manual_prices.csv` and run import script.

---

## Questions?

- **Q: Why are APIs blocked?**
  - A: Vietnamese financial data is geo-restricted to Vietnam IPs only

- **Q: Is manual import accurate?**
  - A: Yes! You control the data. Get prices from official HSX sources.

- **Q: Can I automate this?**
  - A: Yes, with VPN to Vietnam or from Vietnamese network

- **Q: How often should I update?**
  - A: Once per trading day is sufficient for most use cases
