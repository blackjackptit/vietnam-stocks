/**
 * Collapsible Sections - Reusable Component
 * Makes card sections collapsible across all pages
 */

// Add collapsible styles dynamically
function addCollapsibleStyles() {
    if (document.getElementById('collapsible-styles')) return; // Already added

    const style = document.createElement('style');
    style.id = 'collapsible-styles';
    style.textContent = `
        /* Collapsible section styles */
        .card.collapsible h2,
        .card.collapsible h3 {
            cursor: pointer;
            user-select: none;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: background 0.2s;
            position: relative;
            margin: -10px -10px 20px -10px;
            padding: 10px 10px 20px 10px;
            border-radius: 8px 8px 0 0;
        }

        .card.collapsible h2:hover,
        .card.collapsible h3:hover {
            background: #f8fafc;
        }

        .card.collapsible h2::after,
        .card.collapsible h3::after {
            content: '▼';
            font-size: 0.9em;
            color: #64748b;
            transition: transform 0.3s;
            flex-shrink: 0;
            margin-left: 10px;
        }

        .card.collapsible.collapsed h2::after,
        .card.collapsible.collapsed h3::after {
            transform: rotate(-90deg);
        }

        .card.collapsible.collapsed h2,
        .card.collapsible.collapsed h3 {
            margin-bottom: -10px;
            border-bottom: none;
        }

        .card-content {
            overflow: hidden;
            transition: max-height 0.4s ease-out, opacity 0.4s ease-out;
        }

        .card.collapsible.collapsed .card-content {
            max-height: 0 !important;
            opacity: 0;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Quick actions bar */
        .quick-actions-bar {
            display: none;
            margin-bottom: 15px;
            padding: 12px 20px;
            background: linear-gradient(135deg, #c41c16 0%, #7f1d1d 100%);
            border-radius: 10px;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(196, 28, 22, 0.3);
        }

        .quick-actions-bar.active {
            display: flex;
        }

        .quick-actions-bar .tip {
            color: white;
            font-weight: 600;
            font-size: 0.95em;
        }

        .quick-actions-bar .actions {
            display: flex;
            gap: 10px;
        }

        .quick-actions-bar button {
            padding: 8px 16px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9em;
            transition: all 0.2s;
        }

        .quick-actions-bar button:hover {
            background: rgba(255,255,255,0.35);
            transform: translateY(-1px);
        }

        .quick-actions-bar button:active {
            transform: translateY(0);
        }

        @media (max-width: 768px) {
            .quick-actions-bar {
                flex-direction: column;
                gap: 10px;
                padding: 15px;
            }

            .quick-actions-bar .actions {
                width: 100%;
            }

            .quick-actions-bar button {
                flex: 1;
            }
        }
    `;
    document.head.appendChild(style);
}

// Toggle section expand/collapse
function toggleSection(header) {
    const card = header.closest('.card');
    const content = card.querySelector('.card-content');

    if (!content) return;

    if (card.classList.contains('collapsed')) {
        // Expand
        card.classList.remove('collapsed');
        content.style.maxHeight = content.scrollHeight + 'px';

        // After transition, set to 'none' to allow dynamic resizing
        setTimeout(() => {
            if (!card.classList.contains('collapsed')) {
                content.style.maxHeight = 'none';
            }
        }, 400);
    } else {
        // Collapse
        content.style.maxHeight = content.scrollHeight + 'px';
        content.offsetHeight; // Force reflow

        requestAnimationFrame(() => {
            card.classList.add('collapsed');
        });
    }
}

// Initialize collapsible sections
function initializeCollapsibleSections() {
    document.querySelectorAll('.card.collapsible:not(.collapsed) .card-content').forEach(content => {
        content.style.maxHeight = 'none';
    });
}

// Expand all sections
function expandAllSections() {
    document.querySelectorAll('.card.collapsible.collapsed').forEach(card => {
        const header = card.querySelector('h2, h3');
        if (header) toggleSection(header);
    });
}

// Collapse all sections
function collapseAllSections() {
    document.querySelectorAll('.card.collapsible:not(.collapsed)').forEach(card => {
        const header = card.querySelector('h2, h3');
        if (header) toggleSection(header);
    });
}

// Show quick actions bar
function showQuickActionsBar() {
    const bar = document.querySelector('.quick-actions-bar');
    if (bar) {
        bar.classList.add('active');
    }
}

// Hide quick actions bar
function hideQuickActionsBar() {
    const bar = document.querySelector('.quick-actions-bar');
    if (bar) {
        bar.classList.remove('active');
    }
}

// Auto-make all cards collapsible
function makeCardsCollapsible(options = {}) {
    const {
        expandFirst = 2, // Number of first cards to keep expanded
        addQuickActions = true, // Whether to add quick actions bar
        selector = '.card' // CSS selector for cards
    } = options;

    document.querySelectorAll(selector).forEach((card, index) => {
        // Skip if already collapsible
        if (card.classList.contains('collapsible')) return;

        // Add collapsible class
        card.classList.add('collapsible');

        // Collapse by default (except first N cards)
        if (index >= expandFirst) {
            card.classList.add('collapsed');
        }

        // Get header and content
        const header = card.querySelector('h2, h3');
        if (!header) return;

        // Wrap content if not already wrapped
        if (!card.querySelector('.card-content')) {
            const content = document.createElement('div');
            content.className = 'card-content';

            // Move all children except header into card-content
            Array.from(card.children).forEach(child => {
                if (child !== header) {
                    content.appendChild(child);
                }
            });

            card.appendChild(content);
        }

        // Add click handler
        header.onclick = function() { toggleSection(this); };
    });

    // Add quick actions bar if requested and not already present
    if (addQuickActions && !document.querySelector('.quick-actions-bar')) {
        addQuickActionsBar();
    }

    // Initialize collapsible sections
    setTimeout(initializeCollapsibleSections, 100);
}

// Add quick actions bar to page
function addQuickActionsBar() {
    // Find container (try common container classes/ids)
    const container = document.querySelector('.container, .main-content, main, #app') || document.body;

    // Create quick actions bar
    const bar = document.createElement('div');
    bar.className = 'quick-actions-bar active';
    bar.innerHTML = `
        <div class="tip" data-i18n="collapsible.tip">💡 Tip: Click section headers to expand/collapse</div>
        <div class="actions">
            <button onclick="expandAllSections()" data-i18n="collapsible.expand_all">Expand All</button>
            <button onclick="collapseAllSections()" data-i18n="collapsible.collapse_all">Collapse All</button>
        </div>
    `;

    // Insert at the beginning of container
    if (container.firstChild) {
        container.insertBefore(bar, container.firstChild);
    } else {
        container.appendChild(bar);
    }
}

// Auto-initialize when DOM is ready
function autoInit() {
    addCollapsibleStyles();

    // Wait a bit for content to load, then make cards collapsible
    setTimeout(() => {
        const cardCount = document.querySelectorAll('.card').length;
        if (cardCount > 0) {
            makeCardsCollapsible();
        }
    }, 500);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoInit);
} else {
    autoInit();
}

// Export functions to global scope
window.toggleSection = toggleSection;
window.initializeCollapsibleSections = initializeCollapsibleSections;
window.expandAllSections = expandAllSections;
window.collapseAllSections = collapseAllSections;
window.showQuickActionsBar = showQuickActionsBar;
window.hideQuickActionsBar = hideQuickActionsBar;
window.makeCardsCollapsible = makeCardsCollapsible;
