/**
 * Open Source Assistant - UI Enhancements
 * Phase 1: Typing Animation, Timestamps, Code Highlighting, Toasts, Micro-interactions
 */

// ============================================
// 1. TOAST NOTIFICATION SYSTEM
// ============================================
class ToastManager {
    constructor() {
        this.container = this.createContainer();
        this.toasts = [];
    }

    createContainer() {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            display: flex;
            flex-direction: column;
            gap: 10px;
            pointer-events: none;
        `;
        document.body.appendChild(container);
        return container;
    }

    show(message, type = 'info', duration = 4000) {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.style.cssText = `
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 12px 16px;
            min-width: 280px;
            max-width: 400px;
            box-shadow: var(--shadow-lg);
            display: flex;
            align-items: center;
            gap: 12px;
            animation: slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            pointer-events: auto;
            backdrop-filter: blur(10px);
        `;

        const icons = {
            success: '<i class="fas fa-check-circle" style="color: #10b981;"></i>',
            error: '<i class="fas fa-exclamation-circle" style="color: #ef4444;"></i>',
            info: '<i class="fas fa-info-circle" style="color: #3b82f6;"></i>',
            warning: '<i class="fas fa-exclamation-triangle" style="color: #f59e0b;"></i>'
        };

        toast.innerHTML = `
            ${icons[type] || icons.info}
            <span style="flex: 1; color: var(--text-primary); font-size: 0.9rem;">${message}</span>
            <button onclick="this.parentElement.remove()" style="background: none; border: none; color: var(--text-tertiary); cursor: pointer; padding: 4px;">
                <i class="fas fa-times"></i>
            </button>
        `;

        this.container.appendChild(toast);
        this.toasts.push(toast);

        setTimeout(() => {
            toast.style.animation = 'slideOut 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            setTimeout(() => {
                toast.remove();
                this.toasts = this.toasts.filter(t => t !== toast);
            }, 300);
        }, duration);
    }
}

// Initialize toast manager
const toast = new ToastManager();

// Add toast animations to CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }

    /* Typing indicator */
    .typing-indicator {
        display: inline-flex;
        gap: 4px;
        padding: 8px 12px;
    }

    .typing-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--text-tertiary);
        animation: typingBounce 1.4s infinite ease-in-out;
    }

    .typing-dot:nth-child(1) { animation-delay: 0s; }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }

    @keyframes typingBounce {
        0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
        30% { transform: translateY(-10px); opacity: 1; }
    }

    /* Message timestamp */
    .message-timestamp {
        font-size: 0.7rem;
        color: var(--text-tertiary);
        margin-top: 4px;
        opacity: 0.7;
    }

    /* Code block enhancements */
    .code-block-wrapper {
        position: relative;
        margin: 12px 0;
    }

    .copy-code-btn {
        position: absolute;
        top: 8px;
        right: 8px;
        background: rgba(0, 0, 0, 0.6);
        border: none;
        color: white;
        padding: 6px 12px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 0.75rem;
        opacity: 0;
        transition: opacity 0.2s, background 0.2s;
    }

    .code-block-wrapper:hover .copy-code-btn {
        opacity: 1;
    }

    .copy-code-btn:hover {
        background: rgba(0, 0, 0, 0.8);
    }

    .copy-code-btn.copied {
        background: #10b981 !important;
    }

    /* Enhanced button hover effects */
    .icon-btn, .send-btn, .suggestion-btn, .nav-link {
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .icon-btn:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }

    .icon-btn:active {
        transform: translateY(0);
    }

    .send-btn:hover {
        transform: scale(1.05);
    }

    .send-btn:active {
        transform: scale(0.95);
    }

    .suggestion-btn:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: var(--shadow-sm);
    }

    .nav-link:hover {
        transform: translateX(4px);
    }

    /* Ripple effect */
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple 0.6s ease-out;
        pointer-events: none;
    }

    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }

    /* Prism.js theme overrides for better integration */
    pre[class*="language-"] {
        margin: 0;
        border-radius: 8px;
        font-size: 0.85rem;
    }

    code[class*="language-"] {
        font-family: 'Fira Code', 'Consolas', 'Monaco', monospace;
    }
`;
document.head.appendChild(style);

// ============================================
// 2. TYPING INDICATOR
// ============================================
function createTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;
    return indicator;
}

// ============================================
// 3. MESSAGE TIMESTAMPS
// ============================================
function getRelativeTime(timestamp) {
    const now = new Date();
    const then = new Date(timestamp);
    const seconds = Math.floor((now - then) / 1000);

    if (seconds < 60) return 'Just now';
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
    if (seconds < 604800) return `${Math.floor(seconds / 86400)}d ago`;

    return then.toLocaleDateString();
}

function addTimestamp(messageElement) {
    const timestamp = new Date();
    const timestampEl = document.createElement('div');
    timestampEl.className = 'message-timestamp';
    timestampEl.textContent = getRelativeTime(timestamp);
    timestampEl.title = timestamp.toLocaleString();

    // Store timestamp for updates
    timestampEl.dataset.timestamp = timestamp.toISOString();

    messageElement.querySelector('.message-bubble').appendChild(timestampEl);
}

// Update timestamps every minute
setInterval(() => {
    document.querySelectorAll('.message-timestamp').forEach(el => {
        if (el.dataset.timestamp) {
            el.textContent = getRelativeTime(el.dataset.timestamp);
        }
    });
}, 60000);

// ============================================
// 4. CODE SYNTAX HIGHLIGHTING
// ============================================
function enhanceCodeBlocks() {
    // Wait for Prism to be available
    if (typeof Prism === 'undefined') {
        setTimeout(enhanceCodeBlocks, 100);
        return;
    }

    document.querySelectorAll('pre code').forEach(block => {
        if (block.parentElement.classList.contains('code-block-wrapper')) return;

        // Wrap in container
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        block.parentElement.parentElement.insertBefore(wrapper, block.parentElement);
        wrapper.appendChild(block.parentElement);

        // Add copy button
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-code-btn';
        copyBtn.innerHTML = '<i class="fas fa-copy"></i> Copy';
        copyBtn.onclick = () => {
            navigator.clipboard.writeText(block.textContent).then(() => {
                copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                copyBtn.classList.add('copied');
                toast.show('Code copied to clipboard!', 'success', 2000);

                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="fas fa-copy"></i> Copy';
                    copyBtn.classList.remove('copied');
                }, 2000);
            });
        };
        wrapper.appendChild(copyBtn);

        // Apply syntax highlighting
        Prism.highlightElement(block);
    });
}

// ============================================
// 5. RIPPLE EFFECT
// ============================================
function createRipple(event) {
    const button = event.currentTarget;
    const ripple = document.createElement('span');
    ripple.className = 'ripple';

    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';

    const computedStyle = window.getComputedStyle(button);
    if (computedStyle.position === 'static') {
        button.style.position = 'relative';
    }
    button.style.overflow = 'hidden';
    button.appendChild(ripple);

    setTimeout(() => ripple.remove(), 600);
}

// Add ripple effect to buttons
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.icon-btn, .send-btn, .suggestion-btn').forEach(btn => {
        btn.addEventListener('click', createRipple);
    });
});

// ============================================
// 6. ENHANCED MESSAGE OBSERVER
// ============================================
const messageObserver = new MutationObserver((mutations) => {
    mutations.forEach(mutation => {
        mutation.addedNodes.forEach(node => {
            if (node.classList && node.classList.contains('message-row')) {
                // Add timestamp
                addTimestamp(node);

                // Enhance code blocks after a short delay
                setTimeout(() => enhanceCodeBlocks(), 100);
            }
        });
    });
});

// Start observing
document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-messages');
    if (chatContainer) {
        messageObserver.observe(chatContainer, {
            childList: true,
            subtree: true
        });

        // Enhance existing messages
        document.querySelectorAll('.message-row').forEach(msg => {
            addTimestamp(msg);
        });
        enhanceCodeBlocks();
    }
});

// ============================================
// 7. UTILITY FUNCTIONS
// ============================================
window.showToast = (message, type, duration) => toast.show(message, type, duration);
window.createTypingIndicator = createTypingIndicator;

// Show welcome toast
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        toast.show('Welcome to Open Source Assistant! 👋', 'info', 3000);
    }, 500);
});

console.log('✨ UI Enhancements loaded successfully!');
