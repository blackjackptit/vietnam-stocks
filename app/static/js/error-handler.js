/**
 * Global error handling utilities
 * Provides user-friendly error messages and fallback behavior
 */

/**
 * Show user-friendly error message in a container
 * @param {HTMLElement} container - DOM element to show error in
 * @param {string} message - Custom error message (optional)
 */
function showErrorMessage(container, message = 'Failed to load data') {
    if (!container) return;

    container.innerHTML = `
        <div style="
            grid-column: 1/-1;
            text-align: center;
            padding: 40px;
            background: #fef2f2;
            border-radius: 8px;
            border: 1px solid #fecaca;
        ">
            <p style="color: #dc2626; font-size: 1.1em; margin-bottom: 10px;">
                ⚠️ ${message}
            </p>
            <p style="color: #64748b; margin-bottom: 15px;">
                Please check your connection and try again
            </p>
            <button
                onclick="location.reload()"
                style="
                    background: #c41c16;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 0.95em;
                "
            >
                🔄 Reload Page
            </button>
        </div>
    `;
}

/**
 * Wrap async initialization functions with error handling
 * @param {Function} initFn - Async init function to wrap
 * @param {Object} options - Configuration options
 * @returns {Function} Wrapped function with error handling
 */
function withErrorBoundary(initFn, options = {}) {
    const {
        errorContainer = 'mainContent',  // ID of container to show errors
        errorMessage = 'Failed to initialize page',
        onError = null  // Custom error handler
    } = options;

    return async function(...args) {
        try {
            await initFn(...args);
        } catch (error) {
            console.error('Initialization error:', error);

            // Call custom error handler if provided
            if (typeof onError === 'function') {
                onError(error);
            }

            // Show user-friendly error
            const container = document.getElementById(errorContainer);
            showErrorMessage(container, errorMessage);
        }
    };
}

/**
 * Handle API errors with retry logic
 * @param {Function} apiFn - API function that returns a Promise
 * @param {Object} options - Retry options
 * @returns {Promise} Result or throws error after retries
 */
async function withRetry(apiFn, options = {}) {
    const {
        retries = 3,
        delay = 1000,
        onRetry = null
    } = options;

    let lastError;

    for (let attempt = 0; attempt < retries; attempt++) {
        try {
            return await apiFn();
        } catch (error) {
            lastError = error;

            if (attempt < retries - 1) {
                if (typeof onRetry === 'function') {
                    onRetry(attempt + 1, retries);
                }
                // Wait before retrying
                await new Promise(resolve => setTimeout(resolve, delay * (attempt + 1)));
            }
        }
    }

    throw lastError;
}

/**
 * Global unhandled promise rejection handler
 */
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);

    // Prevent default behavior (logging to console) in production
    if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
        event.preventDefault();

        // Show user-friendly error notification
        if (typeof showNotification === 'function') {
            showNotification('An unexpected error occurred. Please refresh the page.', 'error');
        }
    }
});

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { showErrorMessage, withErrorBoundary, withRetry };
}

// Make available globally
window.ErrorHandler = {
    showErrorMessage,
    withErrorBoundary,
    withRetry
};
