/**
 * Data API - Centralized API calls for real data (no fake/random data)
 */

const DataAPI = {
    // Base configuration - Always use port 5000 for API calls
    baseURL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://localhost:5000'
        : window.location.origin,

    /**
     * Fetch watchlist from API
     */
    async getWatchlist() {
        try {
            const response = await fetch(`${this.baseURL}/api/watchlist`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching watchlist:', error);
            return [];
        }
    },

    /**
     * Save watchlist to API
     */
    async saveWatchlist(watchlist) {
        try {
            const response = await fetch(`${this.baseURL}/api/watchlist`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(watchlist)
            });
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error saving watchlist:', error);
            throw error;
        }
    },

    /**
     * Get stock names mapping
     */
    async getStockNames() {
        try {
            const response = await fetch(`${this.baseURL}/stock_names.json`);
            if (!response.ok) {
                console.warn('Stock names file not found, trying API endpoint');
                const apiResponse = await fetch(`${this.baseURL}/api/stock-names`);
                return await apiResponse.json();
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching stock names:', error);
            return {};
        }
    },

    /**
     * Get current price data for a stock
     */
    async getCurrentPrice(symbol) {
        try {
            // Try API endpoint first (real-time data from database)
            const response = await fetch(`${this.baseURL}/api/stock/${symbol}/current`);
            if (response.ok) {
                const result = await response.json();
                if (result.success) {
                    return result;
                }
            }

            // Fallback to static JSON file if API fails
            const fallbackResponse = await fetch(`${this.baseURL}/data/${symbol}_current.json`);
            if (fallbackResponse.ok) {
                return await fallbackResponse.json();
            }

            throw new Error(`No data for ${symbol}`);
        } catch (error) {
            console.error(`Error fetching current price for ${symbol}:`, error);
            return null;
        }
    },

    /**
     * Get historical data for a stock
     */
    async getHistoricalData(symbol, days = 365) {
        try {
            // Try API endpoint first (real-time data from database)
            const response = await fetch(`${this.baseURL}/api/stock/${symbol}/history?days=${days}`);
            if (response.ok) {
                const result = await response.json();
                if (result.success && result.data && result.data.length > 0) {
                    return result.data;
                }
            }

            // Fallback to static JSON file if API fails
            const fallbackResponse = await fetch(`${this.baseURL}/data/${symbol}_history.json`);
            if (fallbackResponse.ok) {
                return await fallbackResponse.json();
            }

            throw new Error(`No history for ${symbol}`);
        } catch (error) {
            console.error(`Error fetching history for ${symbol}:`, error);
            return [];
        }
    },

    /**
     * Get multiple stocks' current data
     */
    async getMultipleCurrentPrices(symbols) {
        const promises = symbols.map(symbol => this.getCurrentPrice(symbol));
        const results = await Promise.allSettled(promises);

        return results
            .map((result, index) => ({
                symbol: symbols[index],
                data: result.status === 'fulfilled' ? result.value : null
            }))
            .filter(item => item.data !== null);
    },

    /**
     * Get multiple stocks' historical data
     */
    async getMultipleHistoricalData(symbols) {
        const promises = symbols.map(symbol => this.getHistoricalData(symbol));
        const results = await Promise.allSettled(promises);

        return results
            .map((result, index) => ({
                symbol: symbols[index],
                data: result.status === 'fulfilled' ? result.value : []
            }))
            .filter(item => item.data.length > 0);
    },

    /**
     * Get automation config
     */
    async getAutomationConfig() {
        try {
            const response = await fetch(`${this.baseURL}/api/automation`);
            if (!response.ok) return { enabled: false };
            return await response.json();
        } catch (error) {
            console.error('Error fetching automation config:', error);
            return { enabled: false };
        }
    },

    /**
     * Save automation config
     */
    async saveAutomationConfig(config) {
        try {
            const response = await fetch(`${this.baseURL}/api/automation`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(config)
            });
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error saving automation config:', error);
            throw error;
        }
    },

    /**
     * Calculate technical indicators from real data
     */
    calculateIndicators(historicalData, period = 14) {
        if (!historicalData || historicalData.length === 0) {
            return null;
        }

        const closes = historicalData.map(d => d.close);
        const volumes = historicalData.map(d => d.volume);

        // RSI calculation
        const rsi = this.calculateRSI(closes, period);

        // Moving averages
        const sma20 = this.calculateSMA(closes, 20);
        const sma50 = this.calculateSMA(closes, 50);
        const sma200 = this.calculateSMA(closes, 200);

        // Volume average
        const avgVolume = volumes.reduce((a, b) => a + b, 0) / volumes.length;

        // Price change
        const currentPrice = closes[closes.length - 1];
        const previousPrice = closes[closes.length - 2];
        const priceChange = currentPrice - previousPrice;
        const priceChangePercent = (priceChange / previousPrice) * 100;

        return {
            rsi: rsi[rsi.length - 1],
            sma20: sma20[sma20.length - 1],
            sma50: sma50[sma50.length - 1],
            sma200: sma200[sma200.length - 1],
            avgVolume,
            currentPrice,
            priceChange,
            priceChangePercent
        };
    },

    /**
     * Calculate RSI (Relative Strength Index)
     */
    calculateRSI(closes, period = 14) {
        const rsi = [];
        const gains = [];
        const losses = [];

        // Calculate gains and losses
        for (let i = 1; i < closes.length; i++) {
            const change = closes[i] - closes[i - 1];
            gains.push(change > 0 ? change : 0);
            losses.push(change < 0 ? -change : 0);
        }

        // Calculate average gains and losses
        for (let i = 0; i < gains.length; i++) {
            if (i < period - 1) {
                rsi.push(null);
            } else if (i === period - 1) {
                const avgGain = gains.slice(0, period).reduce((a, b) => a + b, 0) / period;
                const avgLoss = losses.slice(0, period).reduce((a, b) => a + b, 0) / period;
                const rs = avgGain / avgLoss;
                rsi.push(100 - (100 / (1 + rs)));
            } else {
                const prevRSI = rsi[i - 1];
                const prevAvgGain = ((prevRSI - 100) * period - 100) / ((100 / (100 - prevRSI)) - 1);
                const prevAvgLoss = prevAvgGain / ((100 / (100 - prevRSI)) - 1);
                const avgGain = (prevAvgGain * (period - 1) + gains[i]) / period;
                const avgLoss = (prevAvgLoss * (period - 1) + losses[i]) / period;
                const rs = avgGain / avgLoss;
                rsi.push(100 - (100 / (1 + rs)));
            }
        }

        return rsi;
    },

    /**
     * Calculate Simple Moving Average
     */
    calculateSMA(data, period) {
        const sma = [];
        for (let i = 0; i < data.length; i++) {
            if (i < period - 1) {
                sma.push(null);
            } else {
                const sum = data.slice(i - period + 1, i + 1).reduce((a, b) => a + b, 0);
                sma.push(sum / period);
            }
        }
        return sma;
    },

    /**
     * Format price for display
     */
    formatPrice(price) {
        return new Intl.NumberFormat('vi-VN').format(Math.round(price));
    },

    /**
     * Format percentage for display
     */
    formatPercent(percent) {
        return `${percent >= 0 ? '+' : ''}${percent.toFixed(2)}%`;
    },

    /**
     * Get display name for stock
     */
    getStockDisplayName(symbol, stockNames) {
        const name = stockNames[symbol];
        return name ? `${symbol} - ${name}` : symbol;
    }
};

// Make available globally
window.DataAPI = DataAPI;
