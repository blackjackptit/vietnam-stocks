/**
 * Currency Conversion and Formatting Utilities
 */

// Exchange rates relative to VND (Vietnamese Dong)
// These should be updated regularly - ideally from an API
const EXCHANGE_RATES = {
    VND: 1,
    USD: 0.000041,     // 1 VND = 0.000041 USD (approx 24,400 VND = 1 USD)
    EUR: 0.000038,     // 1 VND = 0.000038 EUR
    GBP: 0.000033,     // 1 VND = 0.000033 GBP
    JPY: 0.0061,       // 1 VND = 0.0061 JPY
    CNY: 0.00029,      // 1 VND = 0.00029 CNY
    KRW: 0.055,        // 1 VND = 0.055 KRW
    THB: 0.0014,       // 1 VND = 0.0014 THB
    SGD: 0.000055,     // 1 VND = 0.000055 SGD
    AUD: 0.000063,     // 1 VND = 0.000063 AUD
    CAD: 0.000056,     // 1 VND = 0.000056 CAD
    CHF: 0.000036      // 1 VND = 0.000036 CHF
};

// Currency symbols
const CURRENCY_SYMBOLS = {
    VND: '₫',
    USD: '$',
    EUR: '€',
    GBP: '£',
    JPY: '¥',
    CNY: '¥',
    KRW: '₩',
    THB: '฿',
    SGD: 'S$',
    AUD: 'A$',
    CAD: 'C$',
    CHF: 'CHF'
};

// Currency names
const CURRENCY_NAMES = {
    VND: 'Vietnamese Dong',
    USD: 'US Dollar',
    EUR: 'Euro',
    GBP: 'British Pound',
    JPY: 'Japanese Yen',
    CNY: 'Chinese Yuan',
    KRW: 'Korean Won',
    THB: 'Thai Baht',
    SGD: 'Singapore Dollar',
    AUD: 'Australian Dollar',
    CAD: 'Canadian Dollar',
    CHF: 'Swiss Franc'
};

/**
 * Get user's preferred currency from settings
 * @returns {string} Currency code (default: VND)
 */
function getUserCurrency() {
    try {
        const settings = JSON.parse(localStorage.getItem('platformSettings'));
        return settings?.currency || 'VND';
    } catch {
        return 'VND';
    }
}

/**
 * Convert amount from VND to target currency
 * @param {number} amountVND - Amount in VND
 * @param {string} targetCurrency - Target currency code
 * @returns {number} Converted amount
 */
function convertFromVND(amountVND, targetCurrency = null) {
    const currency = targetCurrency || getUserCurrency();
    const rate = EXCHANGE_RATES[currency] || 1;
    return amountVND * rate;
}

/**
 * Convert amount from source currency to VND
 * @param {number} amount - Amount in source currency
 * @param {string} sourceCurrency - Source currency code
 * @returns {number} Amount in VND
 */
function convertToVND(amount, sourceCurrency) {
    const rate = EXCHANGE_RATES[sourceCurrency] || 1;
    return amount / rate;
}

/**
 * Convert between any two currencies
 * @param {number} amount - Amount to convert
 * @param {string} from - Source currency code
 * @param {string} to - Target currency code
 * @returns {number} Converted amount
 */
function convertCurrency(amount, from, to) {
    // Convert to VND first, then to target currency
    const vndAmount = convertToVND(amount, from);
    return convertFromVND(vndAmount, to);
}

/**
 * Format number as currency
 * @param {number} amount - Amount to format
 * @param {string} currency - Currency code (optional, uses user setting)
 * @param {object} options - Formatting options
 * @returns {string} Formatted currency string
 */
function formatCurrency(amount, currency = null, options = {}) {
    const curr = currency || getUserCurrency();
    const symbol = CURRENCY_SYMBOLS[curr] || curr;

    const defaults = {
        minimumFractionDigits: curr === 'VND' || curr === 'JPY' || curr === 'KRW' ? 0 : 2,
        maximumFractionDigits: curr === 'VND' || curr === 'JPY' || curr === 'KRW' ? 0 : 2,
        useSymbol: true,
        useGrouping: true
    };

    const opts = { ...defaults, ...options };

    // Format number
    const formatted = amount.toLocaleString('en-US', {
        minimumFractionDigits: opts.minimumFractionDigits,
        maximumFractionDigits: opts.maximumFractionDigits,
        useGrouping: opts.useGrouping
    });

    // Add currency symbol
    if (opts.useSymbol) {
        // For currencies that use suffix (like VND)
        if (curr === 'VND') {
            return `${formatted}${symbol}`;
        }
        // For currencies that use prefix (like USD, EUR)
        return `${symbol}${formatted}`;
    }

    return `${formatted} ${curr}`;
}

/**
 * Format price with automatic currency conversion
 * @param {number} priceVND - Price in VND
 * @param {string} targetCurrency - Target currency (optional, uses user setting)
 * @returns {string} Formatted price string
 */
function formatPrice(priceVND, targetCurrency = null) {
    const currency = targetCurrency || getUserCurrency();
    const convertedPrice = convertFromVND(priceVND, currency);
    return formatCurrency(convertedPrice, currency);
}

/**
 * Get currency symbol
 * @param {string} currency - Currency code (optional, uses user setting)
 * @returns {string} Currency symbol
 */
function getCurrencySymbol(currency = null) {
    const curr = currency || getUserCurrency();
    return CURRENCY_SYMBOLS[curr] || curr;
}

/**
 * Get currency name
 * @param {string} currency - Currency code (optional, uses user setting)
 * @returns {string} Currency name
 */
function getCurrencyName(currency = null) {
    const curr = currency || getUserCurrency();
    return CURRENCY_NAMES[curr] || curr;
}

/**
 * Get exchange rate for currency
 * @param {string} currency - Currency code
 * @returns {number} Exchange rate relative to VND
 */
function getExchangeRate(currency) {
    return EXCHANGE_RATES[currency] || 1;
}

/**
 * Format number with appropriate decimals for currency
 * @param {number} value - Value to format
 * @param {string} currency - Currency code (optional, uses user setting)
 * @returns {string} Formatted value
 */
function formatValue(value, currency = null) {
    const curr = currency || getUserCurrency();

    // No decimals for VND, JPY, KRW
    if (curr === 'VND' || curr === 'JPY' || curr === 'KRW') {
        return Math.round(value).toLocaleString('en-US');
    }

    // 2 decimals for other currencies
    return value.toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

/**
 * Parse currency string to number
 * @param {string} currencyString - Currency string (e.g., "$1,234.56")
 * @returns {number} Numeric value
 */
function parseCurrency(currencyString) {
    // Remove currency symbols and commas
    return parseFloat(currencyString.replace(/[^\d.-]/g, '')) || 0;
}

/**
 * Update all currency displays on page
 * Should be called when user changes currency setting
 */
function updateCurrencyDisplays() {
    // Find all elements with data-price-vnd attribute
    document.querySelectorAll('[data-price-vnd]').forEach(element => {
        const priceVND = parseFloat(element.getAttribute('data-price-vnd'));
        if (!isNaN(priceVND)) {
            element.textContent = formatPrice(priceVND);
        }
    });

    // Find all elements with data-currency attribute
    document.querySelectorAll('[data-currency]').forEach(element => {
        const amount = parseFloat(element.getAttribute('data-currency'));
        const currency = element.getAttribute('data-currency-code') || getUserCurrency();
        if (!isNaN(amount)) {
            element.textContent = formatCurrency(amount, currency);
        }
    });
}

/**
 * Initialize currency system
 * Auto-updates displays when settings change
 */
function initCurrency() {
    // Listen for settings changes
    window.addEventListener('storage', (e) => {
        if (e.key === 'platformSettings') {
            updateCurrencyDisplays();
        }
    });

    // Initial update
    updateCurrencyDisplays();
}

// Auto-initialize
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', initCurrency);
}
