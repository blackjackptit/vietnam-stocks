# Strategy Integration - UI Flow Guide

## How to See the Strategy in Reports

### Step 1: Portfolio Analytics Tab - Select Strategy

1. Navigate to the **"Portfolio Analytics"** tab in the dashboard
2. Scroll down to the **"Smart Stock Recommendations"** section (purple boxes)
3. You'll see 4 strategy checkboxes:
   - ⚖️ **Balanced** - Best risk-adjusted returns
   - 📈 **High Growth** - Maximum expected returns
   - 🛡️ **Conservative** - Lowest risk, stable stocks
   - ⭐ **Blue Chip** - Market leaders only

4. **Click ONE strategy checkbox** (they work like radio buttons - only one can be selected)
   - The selected strategy will show a checkmark
   - The label will be highlighted

### Step 2: Enter Budget and Analyze

1. Scroll down to **"Investment Budget"** field (blue box)
2. Enter your investment amount (e.g., `100,000,000`)
   - It will auto-format with commas: `100,000,000`
3. Click the **"📈 Analyze Portfolio"** button

### Step 3: Check Console (Optional - for debugging)

Open browser console (F12 or Cmd+Option+I) and look for:
```
📊 Strategy Selected: balanced
📊 Strategy Name: ⚖️ Balanced Strategy
✅ Saved strategy to results: {strategy: "balanced", strategyName: "⚖️ Balanced Strategy"}
```

### Step 4: Portfolio Report Tab - Generate Report

1. Navigate to the **"Portfolio Report"** tab
2. Choose your report settings:
   - Report Type (Summary, Detailed, Performance, Risk)
   - Time Period (1m, 3m, 6m, 1y, YTD)
   - Export Format (PDF, HTML, Excel)
3. Click **"📄 Generate Report"** button

### Step 5: See Strategy in Report Preview

**In the HTML preview**, you should see:
```
📄 Portfolio Summary Report
Generated on February 4, 2026 | Period: Last 3 Months
Strategy: ⚖️ Balanced Strategy  ← THIS LINE (in purple text)
```

The strategy line appears:
- **Below the date/period line**
- **In purple color** (#8b5cf6)
- **Bold font** (font-weight: 600)
- **Only if a strategy was selected** (shows nothing if manual selection)

### Step 6: Download Report

Click **"💾 Download Report"** button

**In PDF:**
- Strategy appears in the blue header section
- Below the date
- In white text on blue background

**In Excel:**
- Open the downloaded Excel file
- Go to **"Summary"** sheet
- Row 4 shows: `Strategy: ⚖️ Balanced Strategy`

## Troubleshooting

### "I don't see the strategy in my report"

**Possible causes:**

1. **Browser cache** - You need to hard refresh:
   - **Windows/Linux**: Ctrl + Shift + R
   - **Mac**: Cmd + Shift + R
   - Or: Clear browser cache and reload

2. **No strategy selected** - If you didn't click a strategy checkbox:
   - The system treats it as "Manual Selection"
   - Strategy line won't appear (by design)
   - Solution: Go back to Analytics tab, select a strategy, re-analyze

3. **Old analysis data** - You ran analysis BEFORE the code was updated:
   - Solution: Go to Analytics tab and run "Analyze Portfolio" again
   - This will save the strategy to the results object

4. **JavaScript error** - Check browser console:
   - Press F12 (Windows/Linux) or Cmd+Option+I (Mac)
   - Look for red error messages
   - Share any errors you see

### "My strategy checkbox doesn't stay selected"

This is expected behavior:
- Strategy checkboxes work like radio buttons
- Only ONE can be selected at a time
- When you click a new strategy, the previous one unchecks automatically
- After clicking "Analyze Portfolio", the checkbox should remain checked

### "Console logs show 'Strategy Selected: null'"

This means:
- No strategy checkbox was selected when you clicked Analyze
- The system will treat this as "Manual Selection"
- To fix: Select a strategy checkbox first, then click Analyze

## Technical Details

### Data Flow

```
User clicks strategy →
  Checkbox gets :checked state →
    analyzePortfolio() captures strategy →
      Saves to portfolioAnalysisResults.strategy →
        generateReport() reads strategy →
          Displays in HTML/PDF/Excel
```

### Where Strategy Appears in Code

1. **Capture**: `dashboard_advanced.html` line 2398-2406
2. **Storage**: `dashboard_advanced.html` line 2466-2467
3. **HTML display**: `dashboard_advanced.html` line 4249
4. **PDF display**: `dashboard_advanced.html` line 5005
5. **Excel display**: `dashboard_advanced.html` line 5173

### Console Debug Commands

```javascript
// Check if strategy was saved
console.log(portfolioAnalysisResults.strategy);
console.log(portfolioAnalysisResults.strategyName);

// Check full analysis data
console.log(portfolioAnalysisResults);

// Check if analysis was run
console.log(portfolioAnalysisResults.analyzed);
```

## What You Should See

### Before Analysis
- Portfolio Report tab shows alert: "⚠️ No Portfolio Data Available!"

### After Analysis (with strategy selected)
- Portfolio Report preview shows: `Strategy: ⚖️ Balanced Strategy` (purple text)
- PDF header includes strategy name
- Excel Summary sheet row 4 shows strategy

### After Analysis (without strategy selected)
- Portfolio Report preview shows NO strategy line
- Reports work normally, just no strategy indicated
- This is correct behavior for manual stock selection

## Need Help?

If you're still not seeing the strategy after:
1. Hard refreshing the browser
2. Selecting a strategy checkbox
3. Clicking "Analyze Portfolio"
4. Going to Report tab
5. Clicking "Generate Report"

Then please share:
- Browser console output (especially any errors)
- Screenshot of the Portfolio Analytics tab (showing strategy checkboxes)
- Screenshot of the Report Preview tab (showing the generated report)
