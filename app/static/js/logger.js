/**
 * Conditional logging utility for production
 * Only logs in debug mode (set DEBUG in config.py or via DEBUG env var)
 */

const DEBUG_MODE = window.DEBUG || false;

const logger = {
    /**
     * Log debug information (only in debug mode)
     */
    debug: function(...args) {
        if (DEBUG_MODE) {
            console.log('[DEBUG]', ...args);
        }
    },

    /**
     * Log info messages (only in debug mode)
     */
    info: function(...args) {
        if (DEBUG_MODE) {
            console.log('[INFO]', ...args);
        }
    },

    /**
     * Log warnings (always shown)
     */
    warn: function(...args) {
        console.warn('[WARN]', ...args);
    },

    /**
     * Log errors (always shown)
     */
    error: function(...args) {
        console.error('[ERROR]', ...args);
    }
};

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = logger;
}

// Make available globally
window.logger = logger;
