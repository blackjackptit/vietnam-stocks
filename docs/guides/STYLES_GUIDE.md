# VNStock Analytics - Styles & Design Guide

## Color Palette

### Primary Colors
- **Primary Red**: `#dc2626` (buttons, accents, active states)
- **Dark Red**: `#991b1b` (hover states, darker accents)
- **Light Red**: `#ef4444` (gradient end)
- **Background Red**: `#fee2e2`, `#fecaca` (light backgrounds, selected cards)

### Neutral Colors
- **White**: `#ffffff` (backgrounds, text on dark)
- **Black**: `#000000` (not commonly used, prefer dark grays)
- **Dark Gray**: `#1f2937`, `#111827` (headings, primary text)
- **Medium Gray**: `#64748b`, `#6b7280` (secondary text, labels)
- **Light Gray**: `#f8fafc` (page backgrounds)
- **Border Gray**: `#e5e7eb`, `#e2e8f0` (borders, dividers)

### Semantic Colors
- **Success Green**: `#10b981` (positive indicators, success messages)
- **Error Red**: `#ef4444` (errors, negative indicators)
- **Warning Orange**: `#f59e0b` (warnings, caution)
- **Info Blue**: `#3b82f6` (information, links)

## Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
```

### Font Sizes
- **Extra Large Heading**: `2em` - `2.5em` (page titles)
- **Large Heading (h2)**: `1.5em` - `1.8em` (section titles)
- **Medium Heading (h3)**: `1.125em` - `1.3em` (subsection titles)
- **Body Text**: `0.9em` - `1em` (paragraphs, labels)
- **Small Text**: `0.8em` - `0.85em` (hints, secondary info)

### Font Weights
- **Normal**: `400` (body text)
- **Medium**: `500` - `600` (labels, secondary headings)
- **Bold**: `700` (headings, emphasis)

### Text Alignment
- **All headings (h1, h2, h3)**: Left-aligned (never center)
- **Section titles**: Left-aligned
- **Body text**: Left-aligned
- **Only center**: Loading messages, empty states, error messages

## Layout Patterns

### Page Structure
```html
<body>
    <nav class="top-nav">
        <!-- Navigation -->
    </nav>

    <div class="container">
        <!-- Page content -->
    </div>

    <footer class="footer">
        <!-- Footer -->
    </footer>
</body>
```

### Container
```css
.container {
    max-width: 1360px;
    margin: 0 auto;
    padding: 20px 24px;
}
```

### Grid Layout (2 columns)
```css
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-bottom: 20px;
}

@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}
```

### Full Width Element in Grid
```html
<div class="grid">
    <div class="card" style="grid-column: span 2;">
        <!-- Full width card -->
    </div>
</div>
```

## Component Patterns

### Card
```css
.card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
}

.card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
```

### Collapsible Card
```html
<div class="card collapsible">
    <h3>Section Title</h3>
    <div class="card-content">
        <!-- Content that can be collapsed -->
    </div>
</div>
```

**Requirements:**
1. Include `js/collapsible.js` script
2. Call `initializeCollapsibleSections()` after DOM load
3. Card must have `.collapsible` class
4. Content must be wrapped in `.card-content`

### Primary Button
```css
.btn-primary {
    padding: 12px 24px;
    background: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    font-size: 0.95em;
    transition: all 0.3s;
}

.btn-primary:hover {
    background: #991b1b;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
}
```

### Secondary Button
```css
.btn-secondary {
    padding: 10px 20px;
    background: #e5e7eb;
    color: #475569;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
}

.btn-secondary:hover {
    background: #cbd5e1;
}
```

### Input Field
```css
input[type="text"],
input[type="number"],
select {
    width: 100%;
    padding: 12px 16px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    font-size: 1em;
    transition: border-color 0.2s;
}

input:focus,
select:focus {
    outline: none;
    border-color: #dc2626;
}
```

### Tab Navigation
```html
<div class="tabs">
    <div class="tab active" data-tab="overview" onclick="switchTab('overview')">
        Overview
    </div>
    <div class="tab" data-tab="analysis" onclick="switchTab('analysis')">
        Analysis
    </div>
</div>

<div class="tab-content active" id="overview">
    <!-- Tab content -->
</div>
```

```css
.tabs {
    display: flex;
    gap: 8px;
    border-bottom: 2px solid #e5e7eb;
    margin-bottom: 24px;
}

.tab {
    padding: 12px 24px;
    cursor: pointer;
    border-bottom: 3px solid transparent;
    transition: all 0.3s;
}

.tab.active {
    border-bottom-color: #dc2626;
    color: #dc2626;
    font-weight: 600;
}
```

### Navigation Bar
```css
.top-nav {
    position: sticky;
    top: 0;
    background: #ffffff;
    border-bottom: 1px solid #e5e7eb;
    z-index: 1000;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.nav-container {
    max-width: 1360px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 72px;
}

.logo-text {
    font-size: 1.3em;
    font-weight: 700;
    color: #c41c16;
    text-decoration: none;
}
```

### Dropdown Menu
```css
.dropdown-menu {
    position: absolute;
    top: calc(100% + 10px);
    right: 0;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    min-width: 280px;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: all 0.3s ease;
}

.dropdown-menu.active {
    max-height: 600px;
    opacity: 1;
}
```

## Interactive Elements

### Notification/Toast
Use custom notification system (requires `js/custom-dialogs.js`):

```javascript
showSuccess('Operation completed successfully!');
showError('An error occurred');
showWarning('Please review your input');
showInfo('Information message');
```

### Alert Dialog
```javascript
await showAlert('Message', 'Title');
```

### Confirmation Dialog
```javascript
const confirmed = await showConfirm('Are you sure?', 'Confirm Action');
if (confirmed) {
    // User clicked confirm
}
```

### Loading States
```html
<div class="loading">Loading data...</div>
```

```css
.loading {
    text-align: center;
    padding: 40px;
    color: #64748b;
    font-style: italic;
}
```

## Charts

### Chart Container
```html
<div class="chart-container">
    <canvas id="chartId"></canvas>
</div>
```

```css
.chart-container {
    position: relative;
    height: 400px;
    width: 100%;
    margin-top: 20px;
}

.chart-container.large {
    height: 500px;
}
```

## Tables

### Stock Table
```html
<div style="overflow-x: auto; width: 100%;">
    <table class="stock-table" style="width: 100%;">
        <thead>
            <tr>
                <th>Symbol</th>
                <th>Price</th>
                <th>Change</th>
            </tr>
        </thead>
        <tbody>
            <!-- Table rows -->
        </tbody>
    </table>
</div>
```

```css
.stock-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
}

.stock-table th {
    background: #f8fafc;
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
    color: #1f2937;
    border-bottom: 2px solid #e5e7eb;
}

.stock-table td {
    padding: 12px 16px;
    border-bottom: 1px solid #f1f5f9;
}
```

## Gradients

### Red Gradient (Primary)
```css
background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
```

### Light Red Gradient (Backgrounds)
```css
background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
```

### Purple Gradient (Accents)
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## Icons & Emojis

Use emojis for visual elements:
- 📊 Charts, Analytics
- 📈 Growth, Increase
- 📉 Decline, Decrease
- ✅ Success, Completed
- ❌ Error, Failed
- ⚠️ Warning
- 🎯 Target, Goals
- 💰 Money, Investment
- 🔍 Search
- ⚖️ Balance
- 🛡️ Safety, Conservative
- ⭐ Premium, Blue Chip
- 🚀 Launch, Generate

## Script Loading Order

Always load scripts in this order:
```html
<script src="js/collapsible.js"></script>
<script src="js/logo.js"></script>
<script src="js/api-config.js"></script>
<script src="js/stock-categories.js"></script>
<script src="js/data-api.js"></script>
<script src="js/custom-dialogs.js"></script>
<script src="js/i18n.js"></script>
<script src="js/currency.js"></script>
```

**Important:** Always use `js/` path (not `../static/js/`)

## Responsive Design

### Breakpoints
- **Mobile**: `max-width: 768px`
- **Tablet**: `769px - 1024px`
- **Desktop**: `1025px+`

### Mobile Adjustments
```css
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }

    .grid {
        grid-template-columns: 1fr;
    }

    .card {
        padding: 20px;
    }

    h1 {
        font-size: 1.8em;
    }
}
```

## Animations

### Transitions
```css
transition: all 0.3s ease;
transition: transform 0.3s ease;
transition: opacity 0.3s ease;
```

### Hover Effects
```css
.card:hover {
    transform: translateY(-5px);
}

.btn:hover {
    transform: translateY(-1px);
}
```

## Box Shadows

### Light Shadow (Cards)
```css
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
```

### Medium Shadow (Hover)
```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
```

### Heavy Shadow (Modals, Dropdowns)
```css
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
```

### Colored Shadow (Primary Buttons)
```css
box-shadow: 0 4px 16px rgba(220, 38, 38, 0.4);
```

## Border Radius

- **Small**: `6px` - `8px` (buttons, inputs)
- **Medium**: `10px` - `12px` (cards, containers)
- **Large**: `15px` - `20px` (special cards)
- **Circle**: `50%` (icons, badges)

## Spacing

### Padding
- **Tight**: `8px` - `12px`
- **Normal**: `16px` - `20px`
- **Comfortable**: `24px` - `30px`

### Margin
- **Small**: `10px` - `15px`
- **Medium**: `20px` - `30px`
- **Large**: `40px` - `60px`

### Gap (Grid/Flex)
- **Tight**: `8px` - `12px`
- **Normal**: `16px` - `20px`
- **Wide**: `24px` - `30px`

## Best Practices

### HTML Structure
1. Always wrap content in semantic containers
2. Use collapsible cards for long sections
3. Include loading states for async content
4. Add `data-i18n` attributes for translatable text

### CSS
1. Use utility-first approach when possible
2. Keep specificity low (avoid deep nesting)
3. Use CSS variables for repeated values
4. Include hover states for interactive elements
5. Always add responsive breakpoints

### JavaScript
1. Check for function existence before calling: `if (typeof func === 'function')`
2. Use async/await for data loading
3. Add console.log for debugging key operations
4. Handle errors with try-catch blocks
5. Update UI state after data changes

### Performance
1. Lazy load charts and heavy content
2. Debounce search/filter inputs
3. Use pagination for large datasets
4. Minimize DOM manipulations
5. Cache API responses when possible

## Common Patterns

### Success Message After Action
```javascript
try {
    // Perform action
    await someAction();
    showSuccess('Action completed successfully!');
} catch (error) {
    console.error('Error:', error);
    showError('Failed to complete action: ' + error.message);
}
```

### Loading Indicator
```javascript
const container = document.getElementById('container');
container.innerHTML = '<div class="loading">Loading data...</div>';

try {
    const data = await fetchData();
    container.innerHTML = renderData(data);
} catch (error) {
    container.innerHTML = '<p style="color: #ef4444;">Error loading data</p>';
}
```

### Collapsible Section Initialization
```javascript
async function init() {
    await loadData();

    // Initialize collapsible sections
    if (typeof initializeCollapsibleSections === 'function') {
        initializeCollapsibleSections();
    }
}

document.addEventListener('DOMContentLoaded', init);
```

## File Organization

```
vietnam-stocks/
├── app/
│   ├── pages/           # HTML pages (use js/ for script paths)
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   └── ...
│   └── static/          # Static assets
│       ├── js/          # JavaScript files
│       ├── css/         # CSS files
│       └── images/      # Images
├── api_server.py        # Flask backend
└── STYLES_GUIDE.md      # This file
```

## Color Usage Guidelines

### When to Use Red
- Primary actions (Generate, Submit, Save)
- Active states (selected tabs, active filters)
- Important indicators (alerts, errors)
- Branding elements (logo, headlines)

### When to Use Gray
- Secondary actions (Cancel, Reset)
- Inactive states
- Borders and dividers
- Secondary text

### When to Use White
- Page backgrounds
- Card backgrounds
- Text on dark backgrounds

### When to Use Green
- Success messages
- Positive metrics (profit, growth)
- Confirmation indicators

## Accessibility

1. **Contrast**: Ensure text has sufficient contrast (minimum 4.5:1)
2. **Focus States**: Always provide visible focus indicators
3. **Alt Text**: Add alt text to images (when used)
4. **Keyboard Navigation**: Ensure all interactive elements are keyboard accessible
5. **Labels**: Associate labels with form inputs

---

**Last Updated**: February 2026
**Version**: 1.0
