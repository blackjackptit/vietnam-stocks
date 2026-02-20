// Stock Categories - Loaded from API
window.STOCK_CATEGORIES = {
    commodities: [],
    blue_chips: [],
    banks: [],
    real_estate: [],
    tech: [],
    consumer: [],
    oil_gas: [],
    affordable: [],
    industrial: [],
    transportation: [],
    utilities: [],
    all: []
};

window.TOTAL_STOCKS_COUNT = 0;

// Make categoriesLoaded available globally
window.categoriesLoaded = false;

// Fallback data if API is unavailable
const FALLBACK_CATEGORIES = {
    commodities: ['GOLD', 'SILVER', 'XAU', 'XAG'],
    blue_chips: ['VCB', 'VHM', 'VIC', 'VNM', 'HPG', 'GAS', 'MSN', 'TCB', 'VPB', 'MBB', 'BID', 'CTG', 'VRE', 'SAB', 'PLX', 'MWG', 'SSI', 'FPT', 'VJC', 'GVR', 'POW', 'VCI', 'NVL', 'HDB', 'TPB', 'HVN', 'PVD'],
    banks: ['VCB', 'TCB', 'MBB', 'VPB', 'CTG', 'BID', 'ACB', 'STB', 'HDB', 'TPB', 'VIB', 'MSB', 'SHB', 'EIB', 'LPB', 'OCB', 'VAB', 'VBB', 'BAB', 'BVB', 'NVB', 'PGB', 'SGB', 'ABB', 'NAB'],
    real_estate: ['VHM', 'VIC', 'NVL', 'PDR', 'DXG', 'KDH', 'BCM', 'DIG', 'HDG', 'NLG', 'DXS', 'SCR', 'CEO', 'HDC', 'LDG', 'QCG', 'TCH', 'TDH', 'AGG', 'CII', 'HQC', 'IDC', 'IJC', 'KBC', 'LHG', 'NBB', 'NTL', 'OGC', 'PPI', 'SZL', 'TDC', 'TIX', 'VCG', 'VPI', 'VRE', 'ASM', 'C32', 'CCL', 'CTD', 'DPR', 'FCN', 'HUT', 'ITA', 'LCG', 'NHA', 'NTL', 'PIT', 'PTL', 'SJS', 'TDM', 'THG', 'UIC'],
    tech: ['FPT', 'CMG', 'VGI', 'SAM', 'ITD', 'ELC', 'SGT', 'ICT', 'DGW', 'CTR', 'FOX', 'VNT', 'SHI', 'SVT', 'ONE', 'VTP', 'SGN', 'CMX', 'TTN', 'NET', 'ITC', 'SCS', 'MMC', 'TDG', 'STG', 'VIT', 'DAG', 'AST', 'ALT', 'PTI', 'TEG'],
    consumer: ['VNM', 'MSN', 'MWG', 'PNJ', 'SAB', 'VHC', 'DGC', 'KDC', 'FRT', 'DBC', 'MCH', 'VCF', 'QNS', 'BBC', 'VGC', 'ASP', 'SAV', 'ANV', 'ACL', 'DRC', 'BBC', 'TRI', 'VTO', 'HNG', 'VNE', 'TLG', 'PAN', 'LAF', 'SBT', 'TAC', 'TCM', 'VFG', 'AGF', 'HAG', 'SJD', 'CHP', 'VHG', 'KLF', 'HT1', 'SRC'],
    oil_gas: ['GAS', 'PLX', 'PVD', 'PVS', 'PVT', 'PVB', 'PVG', 'PVC', 'PVX', 'BSR', 'OIL', 'PVE', 'PVA', 'PVO', 'PCT', 'CNG', 'GEG', 'PTB', 'PTC'],
    affordable: ['VPB', 'STB', 'HDB', 'SHB', 'MBB', 'ACB', 'FPT', 'POW', 'DGC', 'GEX', 'MSB', 'VIB', 'TPB', 'OCB', 'LPB', 'EIB', 'VCI', 'SHS', 'AGR', 'AAM', 'DCM', 'DPM', 'DGW', 'PVT', 'BMI', 'BMP', 'CMG', 'PHR', 'DBD', 'NT2', 'REE', 'VSH', 'BWE', 'TNG', 'QCG', 'HVN', 'VJC', 'PAN', 'GMD', 'VCS'],
    industrial: ['HPG', 'HSG', 'NKG', 'VCS', 'TVN', 'DTL', 'TLH', 'VGS', 'HT1', 'TIS', 'VIS', 'DGW', 'TMP', 'POM', 'TRA', 'AAA', 'AAT', 'CSV', 'KSB', 'SBT', 'FIT', 'PHR', 'DCM', 'DPM', 'BMP', 'DGC', 'DDG', 'BMI', 'HMC', 'C32', 'LBM', 'VGC'],
    transportation: ['VJC', 'HVN', 'VTP', 'VSC', 'GMD', 'VOS', 'HAH', 'PHP', 'SCS', 'VST', 'TCL', 'VFC', 'SFI', 'TMS', 'DVP', 'PJT', 'ACV', 'STG', 'VTO', 'MWG'],
    utilities: ['POW', 'GAS', 'NT2', 'REE', 'PC1', 'PPC', 'VSH', 'BWE', 'SBA', 'TNG', 'HND', 'TBC', 'HJS', 'SJD', 'SJE'],
    all: []
};

// Helper function to apply fallback data
function applyFallbackCategories() {
    console.log('📦 Applying fallback stock categories...');
    window.STOCK_CATEGORIES = { ...FALLBACK_CATEGORIES };
    const allStockSymbols = [...new Set(Object.entries(window.STOCK_CATEGORIES)
        .filter(([key]) => key !== 'commodities' && key !== 'all')
        .flatMap(([_, symbols]) => symbols))];
    window.STOCK_CATEGORIES.all = allStockSymbols.sort();
    window.TOTAL_STOCKS_COUNT = [...new Set([...allStockSymbols, ...window.STOCK_CATEGORIES.commodities])].length;
    window.categoriesLoaded = true;
    console.log(`✅ Stock Categories loaded from fallback: ${window.TOTAL_STOCKS_COUNT} total stocks`);
    console.log('Categories loaded flag:', window.categoriesLoaded);
}

// Load stock categories from API
async function loadStockCategories() {
    // Don't use early timeout - wait for API response
    // The fallback is already applied on page load, so we just need to try to replace it

    try {
        // Use API_BASE_URL to ensure correct port (5000)
        const apiUrl = window.API_BASE_URL ? `${window.API_BASE_URL}/api/stock-categories` : '/api/stock-categories';
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 5000); // 5 second timeout for API

        const response = await fetch(apiUrl, { signal: controller.signal });
        clearTimeout(timeout);

        const data = await response.json();

        if (data && data.categories) {
            window.STOCK_CATEGORIES = data.categories;

            // Use total_stocks from API if available, otherwise calculate
            if (data.total_stocks) {
                window.TOTAL_STOCKS_COUNT = data.total_stocks;
            } else {
                // Build 'all' category (excluding commodities)
                const allStockSymbols = [...new Set(Object.entries(window.STOCK_CATEGORIES)
                    .filter(([key]) => key !== 'commodities' && key !== 'all')
                    .flatMap(([_, symbols]) => symbols))];
                window.STOCK_CATEGORIES.all = allStockSymbols.sort();

                // Calculate total count
                window.TOTAL_STOCKS_COUNT = [...new Set([...allStockSymbols, ...(window.STOCK_CATEGORIES.commodities || [])])].length;
            }

            window.categoriesLoaded = true;
            console.log(`✓ Stock Categories loaded from API: ${window.TOTAL_STOCKS_COUNT} total stocks`);

            // Trigger page refresh event to update UI with new data
            window.dispatchEvent(new Event('categoriesUpdated'));
            return true;
        }
    } catch (error) {
        console.warn('Failed to load categories from API, using fallback data:', error);
    }

    // Fallback to hardcoded data if not already loaded
    if (!window.categoriesLoaded) {
        applyFallbackCategories();
    }
    return false;
}

// Auto-load on script load
if (typeof window !== 'undefined') {
    console.log('🚀 stock-categories.js script loaded and executing...');
    // Load fallback immediately so data is available synchronously
    applyFallbackCategories();

    // Then try to load from API in the background (will replace fallback if successful)
    loadStockCategories().catch(err => {
        console.error('Error loading stock categories from API:', err);
        // Fallback already applied, so we're good
    });
    console.log('✓ stock-categories.js initialization complete');
}
