/**
 * VNStock Analytics - Consistent Logo Component
 * Provides a unified logo across all pages
 */

// SVG Logo Icon
const VNSTOCK_LOGO_SVG = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32" style="vertical-align: middle;">
  <!-- Background -->
  <rect width="64" height="64" rx="12" fill="#c41c16"/>

  <!-- Chart bars -->
  <rect x="12" y="36" width="8" height="16" fill="#ffffff" opacity="0.9"/>
  <rect x="22" y="28" width="8" height="24" fill="#ffffff"/>
  <rect x="32" y="20" width="8" height="32" fill="#ffffff" opacity="0.9"/>
  <rect x="42" y="32" width="8" height="20" fill="#ffffff"/>

  <!-- Trend line -->
  <path d="M 10 45 L 22 35 L 36 25 L 50 30"
        stroke="#fbbf24"
        stroke-width="3"
        stroke-linecap="round"
        stroke-linejoin="round"
        fill="none"/>

  <!-- Arrow up -->
  <polygon points="50,30 47,34 53,34" fill="#fbbf24"/>
</svg>
`;

// Initialize logo on all pages
function initVNStockLogo() {
    // Find all logo sections
    const logoSections = document.querySelectorAll('.logo-section, .logo-container');

    logoSections.forEach(section => {
        // Find the logo icon element or create one
        let logoIcon = section.querySelector('.logo-icon');

        if (logoIcon) {
            // Replace emoji with SVG
            logoIcon.innerHTML = VNSTOCK_LOGO_SVG;
            logoIcon.style.display = 'inline-flex';
            logoIcon.style.alignItems = 'center';
        } else {
            // Check if there's already an SVG or img
            const existingSvg = section.querySelector('svg');
            const existingImg = section.querySelector('img');

            if (!existingSvg && !existingImg) {
                // Create logo icon element
                const newLogoIcon = document.createElement('span');
                newLogoIcon.className = 'logo-icon';
                newLogoIcon.innerHTML = VNSTOCK_LOGO_SVG;
                newLogoIcon.style.display = 'inline-flex';
                newLogoIcon.style.alignItems = 'center';

                // Insert at the beginning of logo section
                section.insertBefore(newLogoIcon, section.firstChild);
            }
        }

        // Update logo text if needed
        const logoText = section.querySelector('.logo-text');
        if (logoText) {
            // Remove any emoji from text
            logoText.textContent = logoText.textContent.replace(/📊|🏛️|💹/g, '').trim();

            // Ensure it says "VNStock Analytics"
            if (!logoText.textContent.includes('VNStock')) {
                logoText.textContent = 'VNStock Analytics';
            }
        }
    });
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initVNStockLogo);
} else {
    initVNStockLogo();
}

// Export for manual initialization if needed
window.initVNStockLogo = initVNStockLogo;
window.VNSTOCK_LOGO_SVG = VNSTOCK_LOGO_SVG;
