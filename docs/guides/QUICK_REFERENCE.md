# VNStock Analytics - Quick Reference

## 🎨 Colors (White, Black, Red Theme)

| Usage | Color | Hex |
|-------|-------|-----|
| Primary Red | Main buttons, accents | `#dc2626` |
| Dark Red | Hover states | `#991b1b` |
| Light Red BG | Selected cards | `#fee2e2`, `#fecaca` |
| White | Backgrounds | `#ffffff` |
| Dark Text | Headings | `#1f2937` |
| Medium Gray | Secondary text | `#64748b` |
| Light Gray BG | Page background | `#f8fafc` |
| Borders | Dividers | `#e5e7eb` |

## 📦 Common Components

### Card
```html
<div class="card">
    <h2>Title</h2>
    <p>Content</p>
</div>
```

### Collapsible Card
```html
<div class="card collapsible">
    <h3>Title</h3>
    <div class="card-content">
        Content
    </div>
</div>
```

### Grid (2 columns)
```html
<div class="grid">
    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
</div>
```

### Full Width in Grid
```html
<div class="grid">
    <div class="card" style="grid-column: span 2;">
        Full width content
    </div>
</div>
```

### Primary Button
```html
<button style="padding: 12px 24px; background: #dc2626; color: white;
    border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
    Button Text
</button>
```

## 📜 Script Loading

**Always use this order:**
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

⚠️ **Important:** Use `js/` path, NOT `../static/js/`

## 🔔 Notifications

```javascript
showSuccess('Success message!');
showError('Error message');
showWarning('Warning message');
showInfo('Info message');

await showAlert('Message', 'Title');
const confirmed = await showConfirm('Are you sure?', 'Confirm');
```

## 🔄 Collapsible Sections

**HTML:**
```html
<div class="card collapsible">
    <h3>Section Title</h3>
    <div class="card-content">
        <!-- Collapsible content -->
    </div>
</div>
```

**JavaScript:**
```javascript
if (typeof initializeCollapsibleSections === 'function') {
    initializeCollapsibleSections();
}
```

## 📐 Layout Sizes

- Container max-width: `1360px`
- Navigation height: `72px`
- Card padding: `25px`
- Grid gap: `20px`
- Border radius: `8px` - `12px`

## 📱 Responsive

```css
@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}
```

## 🎯 Common Patterns

### Load Data & Display
```javascript
async function loadData() {
    const container = document.getElementById('container');
    container.innerHTML = '<div class="loading">Loading...</div>';

    try {
        const data = await fetchData();
        container.innerHTML = renderData(data);
    } catch (error) {
        console.error('Error:', error);
        showError('Failed to load data');
    }
}
```

### Initialize Page
```javascript
async function init() {
    await loadData();

    if (typeof initializeCollapsibleSections === 'function') {
        initializeCollapsibleSections();
    }
}

document.addEventListener('DOMContentLoaded', init);
```

## 🎨 Gradients

- **Red Gradient:** `linear-gradient(135deg, #dc2626 0%, #ef4444 100%)`
- **Light Red BG:** `linear-gradient(135deg, #fee2e2 0%, #fecaca 100%)`

## ✨ Effects

- **Card hover:** `transform: translateY(-5px)`
- **Button hover:** `background: #991b1b; transform: translateY(-1px)`
- **Transition:** `transition: all 0.3s ease`
- **Shadow:** `box-shadow: 0 4px 12px rgba(0,0,0,0.15)`

## 📏 Text Alignment

- **Headings (h1-h3):** Always left-aligned
- **Body text:** Left-aligned
- **Center only:** Loading messages, empty states

## 📊 Chart Container
```html
<div class="chart-container">
    <canvas id="chartId"></canvas>
</div>
```

```css
.chart-container {
    height: 400px;
}
```

## 🏷️ Common Emojis

- 📊 Charts/Analytics
- 📈 Growth
- 📉 Decline
- ✅ Success
- ❌ Error
- ⚠️ Warning
- 🎯 Target
- 💰 Money
- 🔍 Search
- ⚖️ Balance
- 🛡️ Conservative
- ⭐ Premium
- 🚀 Generate

## ⚡ Performance Tips

1. Lazy load charts
2. Debounce search inputs
3. Use pagination for large lists
4. Cache API responses
5. Check function exists: `if (typeof func === 'function')`

## 🐛 Debugging

```javascript
console.log('🚀 Function started');
console.log('Debug info:', { variable1, variable2 });
console.error('❌ Error:', error);
```

---

For detailed information, see [STYLES_GUIDE.md](./STYLES_GUIDE.md)
