# Testing Checklist - New Portfolio Flow

## Setup
1. **Hard refresh** browser: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows/Linux)
2. Open browser console (F12 or Cmd+Option+I)

## Test 1: Default State (Smart Strategies + Balanced)

**Expected behavior on page load:**
- [ ] Smart Strategies card should be highlighted (purple border, light purple background)
- [ ] Manual Selection card should be unhighlighted (gray border, white background)
- [ ] Strategy options should be visible below Smart Strategies
- [ ] **Balanced strategy should show a checkmark** (✓ in white circle on top-right)
- [ ] Balanced strategy card should have white border and shadow
- [ ] Console should show: `✅ Auto-selected Balanced strategy as default`
- [ ] Console should show: `🎯 Initialized with Smart Strategies (Balanced) as default`

**What you should see:**
```
Step 1: Choose Your Approach
  [🤖 Smart Strategies - HIGHLIGHTED with purple border]
  [✋ Manual Selection - unhighlighted]

  Below Smart Strategies:
    ⚖️ Balanced ← WITH CHECKMARK ✓
    📈 High Growth
    🛡️ Conservative
    ⭐ Blue Chip
```

## Test 2: Switch to Manual Selection

**Steps:**
1. Click "Manual Selection" card

**Expected:**
- [ ] Manual Selection card highlights (blue border, light blue background)
- [ ] Smart Strategies card unhighlights
- [ ] Strategy checkboxes disappear
- [ ] Stock selection grid appears
- [ ] **All strategy checkmarks disappear** (including Balanced)
- [ ] Console shows: `📊 Approach: Manual Selection`

## Test 3: Switch Back to Smart Strategies

**Steps:**
1. Click "Smart Strategies" card

**Expected:**
- [ ] Smart Strategies card highlights again
- [ ] Manual Selection unhighlights
- [ ] Strategy checkboxes reappear
- [ ] **Balanced is NOT checked** (because we switched away and back)
- [ ] User must manually select a strategy

**Note:** Balanced only auto-selects on initial page load, not when switching back.

## Test 4: Generate Plan with Smart Strategy

**Steps:**
1. Make sure Smart Strategies is selected with Balanced checked
2. Enter budget: `100000000` → should format to `100,000,000`
3. Click "🚀 Generate Plan & Analysis"

**Expected:**
- [ ] Page scrolls down to results
- [ ] Purple banner appears: "✅ Portfolio Plan Ready"
- [ ] Banner shows: "Strategy: ⚖️ Balanced Strategy"
- [ ] Metrics cards display (Portfolio Value, Expected Return, etc.)
- [ ] Download button is visible in the banner
- [ ] Console shows:
  ```
  📊 Strategy Selected: balanced
  📊 Strategy Name: ⚖️ Balanced Strategy
  ✅ Saved strategy to results: {strategy: "balanced", strategyName: "⚖️ Balanced Strategy"}
  ```

## Test 5: Download Report

**Steps:**
1. Click "💾 Download Report" button in the purple banner
2. When prompted, enter `1` for PDF

**Expected:**
- [ ] Alert: "📄 Generating PDF... Please wait."
- [ ] PDF downloads with filename like `portfolio-report-1738698765432.pdf`
- [ ] Open PDF and verify:
  - [ ] Blue header shows "Portfolio Report"
  - [ ] Below date, see: "Strategy: ⚖️ Balanced Strategy" in white text
  - [ ] Metrics section shows actual portfolio data
  - [ ] Holdings table shows stocks
- [ ] Alert: "✅ PDF report downloaded successfully!"

## Test 6: Try Other Strategies

**Steps:**
1. Refresh page (will default to Balanced again)
2. Click "📈 High Growth" strategy
3. Enter budget: `50000000`
4. Generate plan
5. Download report

**Expected:**
- [ ] Only High Growth is checked (Balanced unchecks automatically)
- [ ] Results banner shows: "Strategy: 📈 High Growth Strategy"
- [ ] PDF shows: "Strategy: 📈 High Growth Strategy"

## Test 7: Manual Selection

**Steps:**
1. Refresh page
2. Click "Manual Selection" card
3. Check some stocks (e.g., VCB, FPT, VNM)
4. Enter budget: `75000000`
5. Generate plan
6. Download report

**Expected:**
- [ ] Results banner shows: "Strategy: Manual Selection"
- [ ] Console shows: `📊 Strategy Name: Manual Selection`
- [ ] PDF shows: "Strategy: Manual Selection"

## Test 8: Switch Between Strategies

**Steps:**
1. With Smart Strategies selected and Balanced checked
2. Click "Conservative" strategy
3. Verify Balanced unchecks and Conservative checks
4. Click "Blue Chip"
5. Verify Conservative unchecks and Blue Chip checks

**Expected:**
- [ ] Only one strategy is checked at a time (radio button behavior)
- [ ] Checkmarks move correctly
- [ ] White borders/shadows move correctly

## Console Logs to Watch For

✅ **Good logs:**
```
🚀 Page initialized
✅ Auto-selected Balanced strategy as default
🎯 Initialized with Smart Strategies (Balanced) as default
📊 Strategy Selected: balanced
📊 Strategy Name: ⚖️ Balanced Strategy
✅ Saved strategy to results
📄 Building report with strategy
```

❌ **Problem logs:**
```
⚠️ Clearing pre-checked strategy (should only happen once on load)
Strategy Selected: null (means no strategy was captured)
```

## Visual Checklist

### Step 1 Area (Choose Approach)
- [ ] Two large cards side by side
- [ ] Cards change appearance when clicked
- [ ] Selected card has colored border and gradient background
- [ ] Unselected card is plain white with gray border

### Smart Strategy Options
- [ ] 4 colorful gradient cards in a grid
- [ ] Each shows emoji + title + description
- [ ] Checkmark appears in top-right when selected
- [ ] Selected card has white border and shadow
- [ ] Cards are slightly transparent (opacity 0.7) when not selected
- [ ] Selected card is full opacity (1.0)

### Manual Selection Area
- [ ] Search box at top
- [ ] Control buttons (All, Clear, Visible)
- [ ] Stock grid with checkboxes
- [ ] Counter showing "X selected"

### Step 2 (Budget Input)
- [ ] Large text input
- [ ] Auto-formats with commas as you type
- [ ] "VND" label on the right
- [ ] Light blue background box

### Step 3 (Generate Button)
- [ ] Large green gradient button
- [ ] Text: "🚀 Generate Plan & Analysis"
- [ ] Full width
- [ ] Stands out clearly

### Results Banner
- [ ] Purple gradient background
- [ ] White text
- [ ] Left side: "✅ Portfolio Plan Ready" + strategy name
- [ ] Right side: White "💾 Download Report" button
- [ ] Button has hover effect (scales up slightly)

## Common Issues & Solutions

### Issue: Balanced not checked on load
**Solution:** Hard refresh browser to clear cache

### Issue: Checkmark not visible
**Solution:**
- Check browser console for errors
- Verify CSS loaded correctly
- Try clicking strategy manually to see if checkmark appears

### Issue: "Strategy: null" in reports
**Solution:**
- Verify a strategy is checked before generating
- Check console for strategy capture logs

### Issue: Download button doesn't work
**Solution:**
- Check if `portfolioAnalysisResults.analyzed` is true
- Run `console.log(portfolioAnalysisResults)` to verify data exists

## Browser Compatibility

Test in:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari

## Mobile Responsive (Optional)
- [ ] Cards stack vertically on small screens
- [ ] Buttons are touch-friendly
- [ ] Text is readable
