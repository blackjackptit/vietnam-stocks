# Dashboard Advanced - Business Logic Architecture

## Overview
The Dashboard Advanced page is a multi-tab analytics platform for Vietnamese stock portfolio management. All tabs share data through global JavaScript variables.

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              PORTFOLIO ANALYTICS TAB                         │
│  - Select stocks from portfolio                              │
│  - Click "Analyze Portfolio" button                          │
│  - Runs analyzePortfolio() function                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           GLOBAL DATA STORE (JavaScript)                     │
│                                                              │
│  portfolioAnalysisResults = {                                │
│    analyzed: true/false,                                     │
│    strategy: "balanced"|"growth"|"conservative"|"bluechip",  │
│    strategyName: "⚖️ Balanced Strategy" or null,            │
│    portfolioValue: number,                                   │
│    totalReturn: percentage,                                  │
│    riskLevel: percentage,                                    │
│    sharpeRatio: number,                                      │
│    maxDrawdown: percentage,                                  │
│    diversification: percentage,                              │
│    holdings: [                                               │
│      { symbol, shares, price, value, weight, return }        │
│    ],                                                        │
│    sectors: { "Banking": 35, "Technology": 25, ... },       │
│    performance: { bestPerformer, worstPerformer, ... },      │
│    timestamp: Date                                           │
│  }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              PORTFOLIO REPORT TAB                            │
│  - Click "Generate Report" button                            │
│  - Reads data from portfolioAnalysisResults                  │
│  - Generates HTML preview                                    │
│  - Download as PDF/HTML/Excel                                │
└─────────────────────────────────────────────────────────────┘
```

## Key Components

### 1. Global Variables (Shared State)
Location: `dashboard_advanced.html` lines 1697-1718

```javascript
let allStocks = [];              // All available stocks
let stockData = {};              // Stock price/historical data cache
let currentPortfolioStocks = []; // Currently selected stocks
let charts = {};                 // Chart.js instances
let stockNames = {};             // Symbol to name mapping

// Main data store for portfolio analysis
let portfolioAnalysisResults = {
  analyzed: false,  // Flag indicating if analysis has been run
  strategy: null,   // Selected strategy: "balanced", "growth", "conservative", "bluechip"
  strategyName: null, // Display name: "⚖️ Balanced Strategy" or "Manual Selection"
  portfolioValue: 0,
  totalReturn: 0,
  riskLevel: 0,
  sharpeRatio: 0,
  maxDrawdown: 0,
  diversification: 0,
  holdings: [],
  sectors: {},
  performance: {},
  timestamp: null
};
```

### 2. Portfolio Analytics Tab (Data Source)

**Location:** Lines 869-900 (UI), Lines 2290-2445 (Logic)

**Function:** `analyzePortfolio()`
- Collects selected stocks
- Performs analysis (currently mock calculations)
- **Saves results to `portfolioAnalysisResults`**
- Updates UI with metrics
- Renders allocation charts

**Key Code:**
```javascript
async function analyzePortfolio() {
  // ... select stocks ...

  // Perform analysis
  const mockValue = 1000000 + Math.random() * 500000;
  const mockReturn = 10 + Math.random() * 10;
  // ... more calculations ...

  // SAVE TO GLOBAL STATE
  portfolioAnalysisResults = {
    analyzed: true,
    portfolioValue: totalValue,
    holdings: finalSelectedStocks.map(symbol => ({
      symbol, shares, price, value, weight, return
    })),
    sectors: calculateSectorAllocation(stocks),
    // ... more data ...
    timestamp: new Date()
  };
}
```

### 3. Portfolio Report Tab (Data Consumer)

**Location:** Lines 1590-1664 (UI), Lines 4100-4846 (Logic)

**Functions:**
- `generateReport()` - Creates HTML preview
- `downloadReport()` - Exports to PDF/HTML/Excel

**Key Code:**
```javascript
async function generateReport() {
  // CHECK IF DATA EXISTS
  if (!portfolioAnalysisResults.analyzed) {
    showAlert('Please run Portfolio Analysis first!');
    return;
  }

  // USE REAL DATA
  const data = portfolioAnalysisResults;
  buildReportHTML(data);
}
```

**PDF Generation (jsPDF):**
```javascript
// PDF uses real data
const metrics = [
  ['Portfolio Value', formatCurrency(data.portfolioValue), ...],
  ['Total Return', `${data.totalReturn}%`, ...],
  // ...
];

const holdings = data.holdings.map(h => [
  h.symbol, h.shares, h.price, h.value, h.weight, h.return
]);
```

## Tab Interconnections

### Navigation Between Tabs
```javascript
function switchTab(tabName) {
  // Hide all tabs
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.remove('active');
  });

  // Show selected tab
  document.getElementById(tabName).classList.add('active');
}
```

### Data Sharing Pattern
1. **Portfolio Analytics** tab writes data
2. **Global object** stores data
3. **Portfolio Report** tab reads data
4. Other tabs can also read from the same global object

## Current Implementation Status

### ✅ Implemented
- Global data structure (`portfolioAnalysisResults`)
- Data saving in `analyzePortfolio()`
- Data validation in report generation
- Strategy selection capture and integration (Balanced, Growth, Conservative, Blue Chip)
- Strategy display in HTML reports
- Strategy display in PDF exports
- Strategy display in Excel exports
- Investment budget input with thousand separator formatting
- PDF export with real data (using jsPDF)
- Excel export with real data (all sheets)
- Sector allocation calculation

### ⚠️ Mock/Simulated
- Stock price data (uses random numbers)
- Returns calculation (random ±30%)
- Risk metrics (random values)
- Sharpe ratio (calculated from mock data)

### 🔮 Future Enhancements
- Connect to real API endpoints:
  - `GET /api/stocks/{symbol}/current` - Current prices
  - `GET /api/stocks/{symbol}/history` - Historical data
- Real portfolio calculations:
  - Actual returns from historical data
  - True volatility/risk metrics
  - Correlation matrix
- Database storage:
  - Save portfolio configurations
  - Store analysis history
  - User preferences

## How to Use (User Workflow)

1. **Analyze Portfolio (Required First)**
   - Go to "Portfolio Analytics" tab
   - Select stocks (manually or via strategy)
   - Click "Analyze Portfolio"
   - View results on screen

2. **Generate Report (After Analysis)**
   - Go to "Portfolio Report" tab
   - Select report type and settings
   - Click "Generate Report"
   - Preview appears on screen
   - Click "Download" for PDF/HTML/Excel

3. **Excel Export**
   - Multi-sheet workbook
   - Summary, Holdings, Sectors, Performance
   - Opens in Excel/Google Sheets

4. **PDF Export**
   - Uses jsPDF library (no HTML conversion)
   - Professional layout with tables
   - Ready to print/share

## Error Handling

### Missing Data Check
```javascript
if (!portfolioAnalysisResults.analyzed) {
  showAlert('⚠️ Please run Portfolio Analysis first!

  1. Go to "Portfolio Analytics" tab
  2. Select stocks and click "Analyze Portfolio"
  3. Return here to generate report');
  return;
}
```

### Library Loading Check
```javascript
console.log('📚 Checking export libraries...');
console.log('  - jsPDF:', typeof window.jspdf !== 'undefined' ? '✅ loaded' : '❌ not loaded');
console.log('  - XLSX:', typeof XLSX !== 'undefined' ? '✅ loaded' : '❌ not loaded');
```

## File Structure

```
/dashboard_advanced.html
├── HTML Structure (lines 1-855)
│   ├── Tab Navigation (858-867)
│   ├── Portfolio Analytics Tab (869-900)
│   └── Portfolio Report Tab (1590-1664)
│
├── JavaScript Logic (1696-5100)
│   ├── Global Variables (1697-1718)
│   ├── Portfolio Analysis (2290-2445)
│   ├── Report Generation (4100-4846)
│   └── PDF/Excel Export (4846-5100)
│
└── External Libraries
    ├── Chart.js (charting)
    ├── jsPDF (PDF generation)
    ├── html2pdf (fallback PDF)
    └── XLSX (Excel export)
```

## Debug Console Commands

```javascript
// Check if analysis has been run
window.portfolioAnalysisResults = portfolioAnalysisResults;
console.log(portfolioAnalysisResults);

// Check holdings data
console.log(portfolioAnalysisResults.holdings);

// Force reset analysis flag
portfolioAnalysisResults.analyzed = false;

// View current portfolio stocks
console.log(currentPortfolioStocks);

// Check selected strategy
console.log(portfolioAnalysisResults.strategy);
console.log(portfolioAnalysisResults.strategyName);
```

## Strategy Integration

The system supports four investment strategies that guide stock selection:

### Available Strategies

1. **⚖️ Balanced Strategy** (`balanced`)
   - Best risk-adjusted returns
   - Combines growth and stability
   - Suitable for moderate risk tolerance

2. **📈 High Growth Strategy** (`growth`)
   - Maximum expected returns
   - Focus on high-growth stocks
   - Higher risk tolerance required

3. **🛡️ Conservative Strategy** (`conservative`)
   - Lowest risk, stable stocks
   - Capital preservation focus
   - Lower expected returns

4. **⭐ Blue Chip Strategy** (`bluechip`)
   - Market leaders only
   - Large-cap, established companies
   - Balanced risk-return profile

### Strategy Data Flow

1. User selects strategy checkbox in Portfolio Analytics tab (lines 1052-1093)
2. Strategy captured in `analyzePortfolio()` function:
   ```javascript
   const selectedStrategyCheckbox = document.querySelector('.strategy-checkbox:checked');
   const strategyValue = selectedStrategyCheckbox ? selectedStrategyCheckbox.value : null;
   const strategyName = strategyValue ? strategyNames[strategyValue] : 'Manual Selection';
   ```
3. Strategy saved to `portfolioAnalysisResults` object
4. Strategy displayed in:
   - HTML report preview (line 4234)
   - PDF export header (line 5005)
   - Excel summary sheet (line 5173)

### Manual Selection

If no strategy is selected, the system uses `strategyName: 'Manual Selection'` to indicate user manually chose stocks without AI recommendations.

## Performance Considerations

1. **Data Caching:** Results stored in memory, no re-analysis needed
2. **PDF Generation:** Direct jsPDF (faster than HTML conversion)
3. **Excel Generation:** Client-side (no server round-trip)
4. **Charts:** Destroyed and recreated to prevent memory leaks

## Security Notes

- All processing is client-side (JavaScript)
- No sensitive data sent to server
- Portfolio data stays in browser memory
- Exports are generated locally

---

**Last Updated:** 2026-02-04
**Version:** 2.0
**Maintainer:** VNStock Analytics Team
