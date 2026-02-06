# Development Checklist

## 📄 Creating a New Page

- [ ] Use proper DOCTYPE and meta tags
- [ ] Set page title: `<title>Page Name - VNStock Analytics</title>`
- [ ] Include favicon: `<link rel="icon" type="image/svg+xml" href="favicon.svg">`
- [ ] Load Chart.js if charts needed: `<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>`
- [ ] Load scripts in correct order (see QUICK_REFERENCE.md)
- [ ] Use `js/` path for scripts, NOT `../static/js/`
- [ ] Include top navigation with logo and menu
- [ ] Set page background to `#f8fafc`
- [ ] Use `.container` with max-width `1360px`
- [ ] Include footer at bottom
- [ ] Add responsive breakpoints for mobile (`max-width: 768px`)

## 🎨 Styling Components

- [ ] Cards use white background, 12px radius, 25px padding
- [ ] Primary buttons use `#dc2626` background
- [ ] Use red gradients for selected states
- [ ] Borders use `#e5e7eb`
- [ ] Headings use `#1f2937`
- [ ] Secondary text uses `#64748b`
- [ ] **All headings (h1, h2, h3) are LEFT-ALIGNED (never center)**
- [ ] Add hover effects (translateY, box-shadow)
- [ ] Include transitions: `transition: all 0.3s ease`

## 📦 Making Sections Collapsible

- [ ] Add `.collapsible` class to card
- [ ] Wrap content in `.card-content` div
- [ ] Ensure `js/collapsible.js` is loaded
- [ ] Call `initializeCollapsibleSections()` after DOM loads
- [ ] Test collapse/expand functionality

## 🔄 Loading Data from API

- [ ] Show loading indicator while fetching
- [ ] Use try-catch for error handling
- [ ] Log errors to console with `console.error()`
- [ ] Display user-friendly error messages
- [ ] Check if data exists before rendering
- [ ] Handle empty data states

## 📊 Adding Charts

- [ ] Create chart container with `.chart-container` class
- [ ] Set height (400px normal, 500px large)
- [ ] Add canvas with unique ID
- [ ] Load Chart.js library
- [ ] Initialize chart after data loads
- [ ] Use responsive: true option
- [ ] Match color scheme (red for primary)

## 🎯 Interactive Elements

- [ ] Add onclick handlers to buttons
- [ ] Validate form inputs before submission
- [ ] Show success/error messages after actions
- [ ] Use `showSuccess()`, `showError()` for notifications
- [ ] Use `showConfirm()` for destructive actions
- [ ] Disable buttons during async operations
- [ ] Re-enable buttons after completion

## 🔍 Search/Filter Features

- [ ] Debounce input (300ms minimum)
- [ ] Show "No results" message when empty
- [ ] Clear button to reset filters
- [ ] Preserve filter state during operations
- [ ] Update URL params for shareable filters (optional)

## 📱 Responsive Design

- [ ] Test on mobile (< 768px)
- [ ] Change grid to single column on mobile
- [ ] Reduce padding on mobile (20px → 15px)
- [ ] Ensure buttons are touch-friendly (min 44px height)
- [ ] Check text readability on small screens
- [ ] Test dropdown menus on mobile

## ✅ Form Validation

- [ ] Check required fields before submission
- [ ] Validate data types (numbers, emails, etc.)
- [ ] Show inline error messages
- [ ] Prevent double submission
- [ ] Clear validation errors on input change
- [ ] Focus first error field

## 🚀 Performance

- [ ] Minimize DOM queries (cache selectors)
- [ ] Use event delegation for lists
- [ ] Lazy load heavy content
- [ ] Paginate large datasets
- [ ] Debounce scroll/resize handlers
- [ ] Cache API responses when appropriate
- [ ] Remove event listeners when not needed

## 🐛 Debugging

- [ ] Add console.log at function start
- [ ] Log key variables and state
- [ ] Use descriptive log messages with emojis
- [ ] Add error boundaries (try-catch)
- [ ] Check browser console for errors
- [ ] Test in different browsers
- [ ] Verify script loading order

## 🔒 Security

- [ ] Sanitize user input before display
- [ ] Validate data on backend
- [ ] Use parameterized queries
- [ ] Prevent XSS (no innerHTML with user data)
- [ ] Prevent SQL injection
- [ ] Use HTTPS for API calls
- [ ] Don't expose sensitive data in console

## 📝 Code Quality

- [ ] Use meaningful variable names
- [ ] Add comments for complex logic
- [ ] Keep functions small and focused
- [ ] Remove commented-out code
- [ ] Remove console.logs before production
- [ ] Follow consistent indentation
- [ ] Use semicolons consistently

## 🧪 Testing Checklist

- [ ] Test with empty data
- [ ] Test with large datasets
- [ ] Test error scenarios
- [ ] Test all buttons and links
- [ ] Test form submission
- [ ] Test responsive layouts
- [ ] Test browser back button
- [ ] Test page refresh

## 🎨 Color Check

- [ ] Primary actions use `#dc2626`
- [ ] Hover states use `#991b1b`
- [ ] Selected cards use light red gradient
- [ ] Text contrast meets WCAG standards
- [ ] Success messages use `#10b981`
- [ ] Error messages use `#ef4444`
- [ ] Borders use `#e5e7eb`

## 📋 Before Committing

- [ ] Test all functionality
- [ ] Check console for errors
- [ ] Verify responsive design
- [ ] Remove debug console.logs
- [ ] Check for broken links
- [ ] Verify script paths are correct (`js/`)
- [ ] Test collapsible sections
- [ ] Check notification messages
- [ ] Verify charts render correctly
- [ ] Test with different data sets

## 🚨 Common Issues to Avoid

- ❌ Using `../static/js/` instead of `js/`
- ❌ Forgetting to initialize collapsible sections
- ❌ Missing try-catch blocks for async operations
- ❌ Not checking if functions exist before calling
- ❌ Hardcoding colors instead of using theme colors
- ❌ Center-aligning headings (all titles should be left-aligned)
- ❌ Missing loading states
- ❌ Not handling empty data
- ❌ Forgetting responsive styles
- ❌ Missing error messages
- ❌ Not validating user input

## 📚 Reference Files

- [STYLES_GUIDE.md](./STYLES_GUIDE.md) - Comprehensive style guide
- [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) - Quick reference card
- [DEVELOPMENT_CHECKLIST.md](./DEVELOPMENT_CHECKLIST.md) - This file

---

**Pro Tip:** Print this checklist and check off items as you work!
