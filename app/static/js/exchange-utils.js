/**
 * Exchange Utilities for Stock Filtering and Display
 * Provides consistent exchange filtering and display across all pages
 */

// Exchange information
const EXCHANGES = {
    'HOSE': { name: 'Ho Chi Minh Stock Exchange', icon: '🏛️', color: '#3b82f6' },
    'HNX': { name: 'Hanoi Stock Exchange', icon: '📍', color: '#10b981' },
    'UPCOM': { name: 'Unlisted Public Companies', icon: '⭐', color: '#f59e0b' }
};

/**
 * Get exchange display name with icon
 */
function getExchangeDisplay(exchange) {
    if (!exchange) return 'N/A';
    const ex = EXCHANGES[exchange.toUpperCase()];
    return ex ? `${ex.icon} ${exchange.toUpperCase()}` : exchange;
}

/**
 * Get exchange color
 */
function getExchangeColor(exchange) {
    if (!exchange) return '#cbd5e1';
    const ex = EXCHANGES[exchange.toUpperCase()];
    return ex ? ex.color : '#cbd5e1';
}

/**
 * Get exchange badge HTML
 */
function getExchangeBadge(exchange) {
    const color = getExchangeColor(exchange);
    const display = getExchangeDisplay(exchange);
    return `<span style="display: inline-block; padding: 4px 10px; background: ${color}15; border: 1px solid ${color}; border-radius: 4px; color: ${color}; font-weight: 600; font-size: 0.85em;">${display}</span>`;
}

/**
 * Create exchange filter dropdown
 */
function createExchangeFilter(filterId = 'exchangeFilter', onChangeCallback = null) {
    const changeHandler = onChangeCallback ? `filterByExchange('${filterId}', '${onChangeCallback}')` : `filterByExchange('${filterId}')`;
    const html = `
        <select id="${filterId}" style="padding: 12px 16px; border: 2px solid #e5e7eb; border-radius: 8px; font-size: 1em; cursor: pointer; font-family: inherit;"
                onchange="${changeHandler}">
            <option value="">All Exchanges</option>
            <option value="HOSE">🏛️ HOSE (Ho Chi Minh)</option>
            <option value="HNX">📍 HNX (Hanoi)</option>
            <option value="UPCOM">⭐ UPCOM (Unlisted)</option>
        </select>
    `;
    return html;
}

/**
 * Create exchange filter buttons (alternative UI)
 */
function createExchangeFilterButtons(filterId = 'exchangeFilterButtons', onChangeCallback = null) {
    const changeHandler = onChangeCallback ? `filterStocksByExchange('${filterId}', '${onChangeCallback}')` : `filterStocksByExchange('${filterId}')`;
    const html = `
        <div id="${filterId}" style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="exchange-filter-btn active" onclick="${changeHandler}; this.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active')); this.classList.add('active');" data-exchange="" style="padding: 8px 16px; background: #f3f4f6; border: 2px solid #3b82f6; color: #1f2937; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.2s;">All</button>
            <button class="exchange-filter-btn" onclick="${changeHandler}; this.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active')); this.classList.add('active');" data-exchange="HOSE" style="padding: 8px 16px; background: #f3f4f6; border: 2px solid #3b82f6; color: #1f2937; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.2s;">🏛️ HOSE</button>
            <button class="exchange-filter-btn" onclick="${changeHandler}; this.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active')); this.classList.add('active');" data-exchange="HNX" style="padding: 8px 16px; background: #f3f4f6; border: 2px solid #3b82f6; color: #1f2937; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.2s;">📍 HNX</button>
            <button class="exchange-filter-btn" onclick="${changeHandler}; this.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active')); this.classList.add('active');" data-exchange="UPCOM" style="padding: 8px 16px; background: #f3f4f6; border: 2px solid #3b82f6; color: #1f2937; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.2s;">⭐ UPCOM</button>
        </div>
    `;
    return html;
}

/**
 * Filter stocks by exchange
 */
function filterByExchange(filterId, callbackFn = null) {
    const select = document.getElementById(filterId);
    if (!select) return;

    const exchange = select.value;
    console.log('Filtering by exchange:', exchange);

    if (callbackFn && typeof window[callbackFn] === 'function') {
        window[callbackFn](exchange);
    }
}

/**
 * Add exchange column to stock table
 */
function addExchangeColumnToTable(tableId, stockDataMap) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const headers = table.querySelectorAll('thead th');
    const lastHeader = headers[headers.length - 1];

    // Add exchange header
    const exchangeHeader = document.createElement('th');
    exchangeHeader.style.cssText = 'padding: 12px; text-align: left; font-weight: 600; color: #1e293b;';
    exchangeHeader.textContent = 'Exchange';
    lastHeader.parentNode.insertBefore(exchangeHeader, lastHeader);

    // Add exchange data to rows
    const rows = table.querySelectorAll('tbody tr');
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        if (cells.length > 0) {
            const symbolCell = cells[0];
            const symbol = symbolCell.textContent.trim();
            const exchange = stockDataMap[symbol] || 'N/A';

            const exchangeCell = document.createElement('td');
            exchangeCell.style.cssText = 'padding: 12px; color: #64748b;';
            exchangeCell.innerHTML = getExchangeBadge(exchange);

            cells[cells.length - 1].parentNode.insertBefore(exchangeCell, cells[cells.length - 1]);
        }
    });
}

/**
 * Update stock checkbox with exchange info
 */
function updateCheckboxWithExchange(containerId, allStocksData) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const checkboxes = container.querySelectorAll('.checkbox-item');
    checkboxes.forEach(item => {
        const label = item.querySelector('label');
        if (label) {
            const stockSymbol = label.htmlFor.split('_')[1];
            const stockData = allStocksData[stockSymbol];
            if (stockData && stockData.exchange) {
                const exchange = getExchangeDisplay(stockData.exchange);
                const originalText = label.textContent.split('(')[0].trim();
                label.textContent = `${originalText} (${exchange})`;
                label.title = `${stockData.name || ''} - ${stockData.exchange}`;
            }
        }
    });
}

/**
 * Get all stocks with exchange data
 */
async function getStocksWithExchange() {
    try {
        const response = await fetch('/api/stocks');
        const data = await response.json();

        if (data.success && data.stocks) {
            const stockMap = {};
            data.stocks.forEach(stock => {
                stockMap[stock.symbol] = stock;
            });
            return stockMap;
        }
    } catch (error) {
        console.error('Error fetching stocks with exchange:', error);
    }
    return {};
}

/**
 * Filter checkbox items by exchange
 */
function filterCheckboxesByExchange(containerId, allStocksData, exchange) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const items = container.querySelectorAll('.checkbox-item');
    let visibleCount = 0;

    items.forEach(item => {
        const checkbox = item.querySelector('input[type="checkbox"]');
        if (!checkbox) return;

        const symbol = checkbox.value;
        const stockData = allStocksData[symbol];
        const itemExchange = stockData ? stockData.exchange : '';

        if (!exchange || itemExchange === exchange) {
            item.style.display = '';
            visibleCount++;
        } else {
            item.style.display = 'none';
        }
    });

    console.log(`Showing ${visibleCount} stocks for exchange: ${exchange || 'All'}`);
}

/**
 * Filter select dropdown options by exchange
 */
function filterSelectByExchange(selectId, allStocksData, exchange) {
    const select = document.getElementById(selectId);
    if (!select) return;

    const options = select.querySelectorAll('option');
    let visibleCount = 0;

    options.forEach(option => {
        if (option.value === '') return; // Keep the default empty option

        const stockData = allStocksData[option.value];
        const optionExchange = stockData ? stockData.exchange : '';

        if (!exchange || optionExchange === exchange) {
            option.style.display = '';
            visibleCount++;
        } else {
            option.style.display = 'none';
        }
    });

    console.log(`Showing ${visibleCount} stocks in dropdown for exchange: ${exchange || 'All'}`);
}

/**
 * Filter stocks by exchange (generic function for both checkboxes and selects)
 */
function filterStocksByExchange(containerId, callbackFn = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const exchange = container.getAttribute('data-exchange') || '';
    console.log('Filtering by exchange:', exchange);

    if (callbackFn && typeof window[callbackFn] === 'function') {
        window[callbackFn](exchange);
    }
}

export {
    EXCHANGES,
    getExchangeDisplay,
    getExchangeColor,
    getExchangeBadge,
    createExchangeFilter,
    filterByExchange,
    addExchangeColumnToTable,
    updateCheckboxWithExchange,
    getStocksWithExchange,
    filterCheckboxesByExchange
};
