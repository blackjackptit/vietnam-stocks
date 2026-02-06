/**
 * Custom Dialog System - Replaces browser default alerts
 * Provides styled notifications, alerts, and confirmations
 */


// Immediately export stub functions that will be replaced
window.showAlert = window.showAlert || function(msg) { console.warn("showAlert not ready:", msg); };
window.showConfirm = window.showConfirm || function(msg) { console.warn("showConfirm not ready:", msg); return Promise.resolve(false); };
window.showDialog = window.showDialog || function(msg) { console.warn("showDialog not ready:", msg); };
window.showNotification = window.showNotification || function(msg) { console.warn("showNotification not ready:", msg); };
window.showSuccess = window.showSuccess || function(msg) { console.warn("showSuccess not ready:", msg); };
window.showError = window.showError || function(msg) { console.warn("showError not ready:", msg); };
window.showWarning = window.showWarning || function(msg) { console.warn("showWarning not ready:", msg); };
window.showInfo = window.showInfo || function(msg) { console.warn("showInfo not ready:", msg); };
// Create dialog container on page load
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        if (!document.getElementById('customDialogContainer')) {
            const container = document.createElement('div');
            container.id = 'customDialogContainer';
            document.body.appendChild(container);
        }
    });
}

/**
 * Show a success notification (auto-dismiss)
 * @param {string} message - Success message to display
 * @param {number} duration - Duration in ms (default: 3000)
 */
function showSuccess(message, duration = 3000) {
    showNotification(message, 'success', duration);
}

/**
 * Show an error notification (auto-dismiss)
 * @param {string} message - Error message to display
 * @param {number} duration - Duration in ms (default: 4000)
 */
function showError(message, duration = 4000) {
    showNotification(message, 'error', duration);
}

/**
 * Show a warning notification (auto-dismiss)
 * @param {string} message - Warning message to display
 * @param {number} duration - Duration in ms (default: 3500)
 */
function showWarning(message, duration = 3500) {
    showNotification(message, 'warning', duration);
}

/**
 * Show an info notification (auto-dismiss)
 * @param {string} message - Info message to display
 * @param {number} duration - Duration in ms (default: 3000)
 */
function showInfo(message, duration = 3000) {
    showNotification(message, 'info', duration);
}

/**
 * Show a notification toast
 * @param {string} message - Message to display
 * @param {string} type - Type: success, error, warning, info
 * @param {number} duration - Duration in ms before auto-dismiss
 */
function showNotification(message, type = 'info', duration = 3000) {
    const container = getOrCreateContainer();

    const notification = document.createElement('div');
    notification.className = `custom-notification custom-notification-${type}`;

    const icon = getIconForType(type);
    notification.innerHTML = `
        <span class="notification-icon">${icon}</span>
        <span class="notification-message">${message}</span>
        <button class="notification-close" onclick="this.parentElement.remove()">×</button>
    `;

    container.appendChild(notification);

    // Trigger animation
    setTimeout(() => notification.classList.add('show'), 10);

    // Auto-dismiss
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 300);
    }, duration);
}

/**
 * Show an alert dialog (replaces window.alert)
 * @param {string} message - Message to display
 * @param {string} title - Dialog title (optional)
 * @param {number} autoCloseDuration - Auto-close after ms (default: 3000, set to 0 to disable)
 */
function showAlert(message, title = '⚠️ Alert', autoCloseDuration = 3000) {
    return new Promise((resolve) => {
        const overlay = createOverlay();
        const dialog = document.createElement('div');
        dialog.className = 'custom-dialog';

        dialog.innerHTML = `
            <div class="dialog-header">
                <h3>${title}</h3>
            </div>
            <div class="dialog-body">
                <p>${message}</p>
            </div>
            <div class="dialog-footer">
                <button class="dialog-btn dialog-btn-primary" onclick="this.closest('.custom-dialog-overlay').remove()">OK</button>
            </div>
        `;

        overlay.appendChild(dialog);
        document.body.appendChild(overlay);

        // Trigger animation
        setTimeout(() => {
            overlay.classList.add('show');
            dialog.classList.add('show');
        }, 10);

        // Focus the OK button
        setTimeout(() => dialog.querySelector('.dialog-btn-primary').focus(), 100);

        // Auto-close after duration
        let autoCloseTimer = null;
        if (autoCloseDuration > 0) {
            autoCloseTimer = setTimeout(() => {
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(true);
                }, 300);
            }, autoCloseDuration);
        }

        // Resolve when closed
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay || e.target.classList.contains('dialog-btn')) {
                if (autoCloseTimer) clearTimeout(autoCloseTimer);
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(true);
                }, 300);
            }
        });

        // ESC key to close
        const handleEsc = (e) => {
            if (e.key === 'Escape') {
                if (autoCloseTimer) clearTimeout(autoCloseTimer);
                overlay.remove();
                document.removeEventListener('keydown', handleEsc);
                resolve(true);
            }
        };
        document.addEventListener('keydown', handleEsc);
    });
}

/**
 * Show a confirmation dialog (replaces window.confirm)
 * @param {string} message - Message to display
 * @param {string} title - Dialog title (optional)
 * @returns {Promise<boolean>} - True if confirmed, false if cancelled
 */
function showConfirm(message, title = '❓ Confirm') {
    return new Promise((resolve) => {
        const overlay = createOverlay();
        const dialog = document.createElement('div');
        dialog.className = 'custom-dialog';

        dialog.innerHTML = `
            <div class="dialog-header">
                <h3>${title}</h3>
            </div>
            <div class="dialog-body">
                <p>${message}</p>
            </div>
            <div class="dialog-footer">
                <button class="dialog-btn dialog-btn-secondary" data-action="cancel">Cancel</button>
                <button class="dialog-btn dialog-btn-primary" data-action="confirm">Confirm</button>
            </div>
        `;

        overlay.appendChild(dialog);
        document.body.appendChild(overlay);

        // Trigger animation
        setTimeout(() => {
            overlay.classList.add('show');
            dialog.classList.add('show');
        }, 10);

        // Focus the confirm button
        setTimeout(() => dialog.querySelector('[data-action="confirm"]').focus(), 100);

        // Handle button clicks
        dialog.addEventListener('click', (e) => {
            if (e.target.classList.contains('dialog-btn')) {
                const action = e.target.getAttribute('data-action');
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(action === 'confirm');
                }, 300);
            }
        });

        // Click overlay to cancel
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(false);
                }, 300);
            }
        });

        // ESC key to cancel
        const handleEsc = (e) => {
            if (e.key === 'Escape') {
                overlay.remove();
                document.removeEventListener('keydown', handleEsc);
                resolve(false);
            }
        };
        document.addEventListener('keydown', handleEsc);
    });
}

/**
 * Show a custom dialog with custom buttons
 * @param {string} message - Message to display
 * @param {Array} buttons - Array of button configs [{label, action, primary}]
 * @param {string} title - Dialog title
 * @param {number} autoCloseDuration - Auto-close after ms (default: 3000, set to 0 to disable)
 */
function showDialog(message, buttons = [{label: 'OK', action: 'ok', primary: true}], title = 'Dialog', autoCloseDuration = 3000) {
    return new Promise((resolve) => {
        const overlay = createOverlay();
        const dialog = document.createElement('div');
        dialog.className = 'custom-dialog';

        const buttonsHtml = buttons.map(btn =>
            `<button class="dialog-btn ${btn.primary ? 'dialog-btn-primary' : 'dialog-btn-secondary'}" data-action="${btn.action}">${btn.label}</button>`
        ).join('');

        dialog.innerHTML = `
            <div class="dialog-header">
                <h3>${title}</h3>
            </div>
            <div class="dialog-body">
                <p>${message}</p>
            </div>
            <div class="dialog-footer">
                ${buttonsHtml}
            </div>
        `;

        overlay.appendChild(dialog);
        document.body.appendChild(overlay);

        // Trigger animation
        setTimeout(() => {
            overlay.classList.add('show');
            dialog.classList.add('show');
        }, 10);

        // Auto-close after duration (use first button action as default)
        let autoCloseTimer = null;
        if (autoCloseDuration > 0) {
            autoCloseTimer = setTimeout(() => {
                const defaultAction = buttons[0]?.action || 'ok';
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(defaultAction);
                }, 300);
            }, autoCloseDuration);
        }

        // Handle button clicks
        dialog.addEventListener('click', (e) => {
            if (e.target.classList.contains('dialog-btn')) {
                if (autoCloseTimer) clearTimeout(autoCloseTimer);
                const action = e.target.getAttribute('data-action');
                overlay.classList.remove('show');
                dialog.classList.remove('show');
                setTimeout(() => {
                    overlay.remove();
                    resolve(action);
                }, 300);
            }
        });

        // ESC key to close
        const handleEsc = (e) => {
            if (e.key === 'Escape') {
                if (autoCloseTimer) clearTimeout(autoCloseTimer);
                overlay.remove();
                document.removeEventListener('keydown', handleEsc);
                resolve(null);
            }
        };
        document.addEventListener('keydown', handleEsc);
    });
}

// Helper functions

function getOrCreateContainer() {
    let container = document.getElementById('customDialogContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'customDialogContainer';
        document.body.appendChild(container);
    }
    return container;
}

function createOverlay() {
    const overlay = document.createElement('div');
    overlay.className = 'custom-dialog-overlay';
    return overlay;
}

function getIconForType(type) {
    const icons = {
        success: '✓',
        error: '✗',
        warning: '⚠',
        info: 'ℹ'
    };
    return icons[type] || icons.info;
}

// Inject styles
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        if (!document.getElementById('customDialogStyles')) {
            const style = document.createElement('style');
            style.id = 'customDialogStyles';
            style.textContent = `
                /* Notification Container */
                #customDialogContainer {
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    z-index: 10000;
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    max-width: 400px;
                }

                /* Notification Toast */
                .custom-notification {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    padding: 16px 20px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    border-left: 4px solid #64748b;
                    opacity: 0;
                    transform: translateX(400px);
                    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                }

                .custom-notification.show {
                    opacity: 1;
                    transform: translateX(0);
                }

                .custom-notification-success {
                    border-left-color: #10b981;
                }

                .custom-notification-error {
                    border-left-color: #ef4444;
                }

                .custom-notification-warning {
                    border-left-color: #f59e0b;
                }

                .custom-notification-info {
                    border-left-color: #3b82f6;
                }

                .notification-icon {
                    font-size: 1.5em;
                    font-weight: bold;
                    flex-shrink: 0;
                }

                .custom-notification-success .notification-icon {
                    color: #10b981;
                }

                .custom-notification-error .notification-icon {
                    color: #ef4444;
                }

                .custom-notification-warning .notification-icon {
                    color: #f59e0b;
                }

                .custom-notification-info .notification-icon {
                    color: #3b82f6;
                }

                .notification-message {
                    flex: 1;
                    color: #1e293b;
                    font-size: 0.95em;
                    line-height: 1.5;
                }

                .notification-close {
                    background: none;
                    border: none;
                    font-size: 1.5em;
                    color: #94a3b8;
                    cursor: pointer;
                    padding: 0;
                    width: 24px;
                    height: 24px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 4px;
                    transition: all 0.2s;
                }

                .notification-close:hover {
                    background: #f1f5f9;
                    color: #64748b;
                }

                /* Dialog Overlay */
                .custom-dialog-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.5);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 10001;
                    opacity: 0;
                    transition: opacity 0.3s;
                    backdrop-filter: blur(2px);
                }

                .custom-dialog-overlay.show {
                    opacity: 1;
                }

                /* Dialog Box */
                .custom-dialog {
                    background: white;
                    border-radius: 12px;
                    min-width: 400px;
                    max-width: 600px;
                    max-height: 80vh;
                    overflow-y: auto;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    transform: scale(0.9) translateY(-20px);
                    opacity: 0;
                    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                }

                .custom-dialog.show {
                    transform: scale(1) translateY(0);
                    opacity: 1;
                }

                .dialog-header {
                    padding: 24px 24px 16px;
                    border-bottom: 1px solid #e5e7eb;
                }

                .dialog-header h3 {
                    margin: 0;
                    font-size: 1.3em;
                    color: #1e293b;
                    font-weight: 700;
                }

                .dialog-body {
                    padding: 24px;
                }

                .dialog-body p {
                    margin: 0;
                    color: #475569;
                    line-height: 1.6;
                    font-size: 1em;
                }

                .dialog-footer {
                    padding: 16px 24px 24px;
                    display: flex;
                    gap: 12px;
                    justify-content: flex-end;
                }

                .dialog-btn {
                    padding: 10px 24px;
                    border: none;
                    border-radius: 8px;
                    font-size: 0.95em;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.2s;
                }

                .dialog-btn-primary {
                    background: #c41c16;
                    color: white;
                }

                .dialog-btn-primary:hover {
                    background: #991b1b;
                    transform: translateY(-1px);
                    box-shadow: 0 4px 12px rgba(196, 28, 22, 0.3);
                }

                .dialog-btn-secondary {
                    background: #e5e7eb;
                    color: #475569;
                }

                .dialog-btn-secondary:hover {
                    background: #cbd5e1;
                }

                .dialog-btn:focus {
                    outline: none;
                    box-shadow: 0 0 0 3px rgba(196, 28, 22, 0.2);
                }

                /* Mobile Responsive */
                @media (max-width: 768px) {
                    #customDialogContainer {
                        top: 10px;
                        right: 10px;
                        left: 10px;
                        max-width: none;
                    }

                    .custom-notification {
                        transform: translateY(-100px);
                    }

                    .custom-notification.show {
                        transform: translateY(0);
                    }

                    .custom-dialog {
                        min-width: 90%;
                        max-width: 90%;
                        margin: 20px;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    });
}

// Export functions to global scope
window.showNotification = showNotification;
window.showAlert = showAlert;
window.showConfirm = showConfirm;
window.showDialog = showDialog;
window.showSuccess = showSuccess;
window.showError = showError;
window.showWarning = showWarning;
window.showInfo = showInfo;
