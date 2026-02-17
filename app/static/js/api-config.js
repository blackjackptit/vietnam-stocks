/**
 * API Configuration
 * Ensures all API calls go to the correct port (5000)
 */

// Determine the correct API base URL
const API_BASE_URL = (() => {
    const hostname = window.location.hostname;

    // For localhost/127.0.0.1, always use port 5000
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return 'http://localhost:5000';
    }

    // For production or other hosts, use current origin
    return window.location.origin;
})();

// Make it globally available
window.API_BASE_URL = API_BASE_URL;

/**
 * Helper function to make API calls with correct base URL
 * @param {string} endpoint - API endpoint (e.g., '/api/stock-categories')
 * @param {object} options - Fetch options
 * @returns {Promise} Fetch promise
 */
window.apiFetch = function(endpoint, options = {}) {
    const url = endpoint.startsWith('http') ? endpoint : `${API_BASE_URL}${endpoint}`;
    // Remove verbose API call logging (use browser DevTools Network tab instead)
    return fetch(url, options);
};

console.log(`✓ API Configuration loaded. Base URL: ${API_BASE_URL}`);
