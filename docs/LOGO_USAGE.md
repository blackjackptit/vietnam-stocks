# VNStock Analytics - Logo Usage Guide

## Brand Identity

**Official Name:** VNStock Analytics
**Color Scheme:** Red (#c41c16), Black, White
**Tagline:** Professional Trading & Investment Tools

## Logo Files

### Favicon
- **File:** `favicon.svg`
- **Size:** 64x64px
- **Format:** SVG (vector)
- **Background:** Red (#c41c16)
- **Elements:** White chart bars with golden trend line

### Usage in HTML
```html
<link rel="icon" type="image/svg+xml" href="favicon.svg">
```

## Logo Component

### Automatic Implementation
All pages automatically load the logo via `js/logo.js`, which:
1. Replaces emoji icons (📊) with the SVG logo
2. Ensures consistent sizing (32x32px)
3. Applies hover effects
4. Standardizes the text to "VNStock Analytics"

### Manual HTML Structure
```html
<div class="logo-section">
    <span class="logo-icon">
        <!-- SVG will be inserted here by logo.js -->
    </span>
    <span class="logo-text">VNStock Analytics</span>
</div>
```

### CSS Classes
- `.logo-section` / `.logo-container` - Container for logo elements
- `.logo-icon` - SVG icon wrapper (32x32px)
- `.logo-text` - Brand name with red gradient text

## Logo Specifications

### Colors
- **Primary Red:** #c41c16
- **Dark Red:** #7f1d1d
- **White:** #ffffff
- **Accent Gold:** #fbbf24 (trend line)

### Sizing
- **Favicon:** 64x64px
- **Navigation Logo:** 32x32px
- **Large Logo:** 48x48px (for landing pages)

### Design Elements
1. **Red Background:** Rounded rectangle (12px radius)
2. **Chart Bars:** 4 white bars of varying heights
3. **Trend Line:** Golden upward line with arrow
4. **Style:** Modern, professional, financial

## Implementation Checklist

✅ All pages include `favicon.svg` in head
✅ All pages load `js/logo.js` for consistency
✅ All pages use "VNStock Analytics" branding
✅ Logo uses red gradient text effect
✅ Hover effects applied to logo
✅ Consistent 32x32px sizing in navigation

## Files Updated

### HTML Pages
- index.html
- dashboard_main.html
- dashboard_advanced.html
- dashboard_history.html
- advanced_charts.html
- price_forecast.html
- macro_analysis.html
- alerts_system.html
- trading_automation.html

### Asset Files
- favicon.svg
- js/logo.js
- css/theme.css

## Maintenance

To update the logo:
1. Edit `favicon.svg` for the main icon
2. Update `VNSTOCK_LOGO_SVG` constant in `js/logo.js`
3. Clear browser cache to see changes

## Brand Guidelines

### Do's ✅
- Use the official SVG logo
- Maintain the red color scheme
- Keep "VNStock Analytics" name consistent
- Use proper spacing around logo
- Ensure logo is clickable (links to index.html)

### Don'ts ❌
- Don't use emoji icons (📊, 💹, etc.)
- Don't alter the logo colors
- Don't distort the aspect ratio
- Don't use inconsistent names
- Don't create custom versions

## Technical Notes

The logo initialization happens automatically via:
```javascript
// In js/logo.js
window.initVNStockLogo();
```

This runs on DOMContentLoaded and ensures all logo instances are consistent.

---

**Last Updated:** 2026-02-01
**Version:** 1.0
**Status:** ✅ Implemented Across All Pages
