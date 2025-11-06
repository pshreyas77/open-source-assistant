document.addEventListener('DOMContentLoaded', function() {

    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-btn');
    const resetButton = document.getElementById('reset-btn');
    const loadingOverlay = document.getElementById('loading-overlay');
    const suggestionButtons = document.querySelectorAll('.suggestion-btn');

    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';

        if (this.value === '') {
            this.style.height = 'auto';
        }
    });

    let conversationId = null;

    function initializeConversation() {
        showLoading();

        fetch('/start-conversation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            hideLoading();
            if (data.status === "success") {
                conversationId = data.conversation_id;
                console.log("Conversation started with ID:", conversationId);

                //addMessage('assistant', 'Hello! I\'m your Open Source Contribution Assistant. How can I help you today?');
            } else {
                throw new Error(data.message || 'Failed to start conversation');
            }
        })
        .catch(error => {
            hideLoading();
            console.error('Error starting conversation:', error);
            addMessage('assistant', 'Sorry, there was an error connecting to the server. Please try refreshing the page.');
        });
    }

    function resetConversation() {
        showLoading();

        fetch('/api/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            hideLoading();
            if (data.status === "success") {

                chatMessages.innerHTML = '';

                initializeConversation();
            } else {
                throw new Error(data.message || 'Failed to reset conversation');
            }
        })
        .catch(error => {
            hideLoading();
            console.error('Error resetting conversation:', error);
            addMessage('assistant', 'Error resetting conversation: ' + error.message);
        });
    }

    function addMessage(sender, text) {
        const row = document.createElement('div');
        row.className = 'flex items-start gap-3';

        const avatar = document.createElement('div');
        avatar.className = `h-9 w-9 rounded-md grid place-items-center flex-shrink-0 ${sender === 'user' ? 'bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-200' : 'bg-brand-600 text-white'}`;
        const icon = document.createElement('i');
        icon.className = sender === 'user' ? 'fas fa-user' : 'fas fa-robot';
        avatar.appendChild(icon);

        const content = document.createElement('div');
        content.className = `max-w-prose rounded-lg px-4 py-3 ${sender === 'user' ? 'bg-neutral-100 dark:bg-neutral-800' : 'bg-neutral-100 dark:bg-neutral-800'}`;
        content.innerHTML = processMarkdown(text);

        row.appendChild(avatar);
        row.appendChild(content);
        chatMessages.appendChild(row);

        styleMarkdown(content);
        addSyntaxHighlighting();
        makeLinksExternal();
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function processMarkdown(text) {
        return marked.parse(text);
    }

    function escapeHTML(text) {
        return text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    function addSyntaxHighlighting() {
        const pres = document.querySelectorAll('pre');
        pres.forEach(pre => {
            pre.classList.add('bg-neutral-900','text-neutral-100','rounded-md','p-4','overflow-x-auto','text-sm');
        });
        const codes = document.querySelectorAll('pre code, code');
        codes.forEach(code => {
            code.classList.add('font-mono');
        });
    }

    function makeLinksExternal() {
        const links = document.querySelectorAll('.message-content a');
        links.forEach(link => {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        });
    }

    function showLoading() { loadingOverlay.classList.remove('hidden'); }

    function hideLoading() { loadingOverlay.classList.add('hidden'); }

    function styleMarkdown(root) {
        // Headings
        root.querySelectorAll('h1').forEach(el => el.classList.add('text-2xl','font-semibold','mt-2','mb-3'));
        root.querySelectorAll('h2').forEach(el => el.classList.add('text-xl','font-semibold','mt-2','mb-2'));
        root.querySelectorAll('h3').forEach(el => el.classList.add('text-lg','font-semibold','mt-2','mb-2'));
        // Paragraphs
        root.querySelectorAll('p').forEach(el => el.classList.add('leading-relaxed','my-2'));
        // Lists
        root.querySelectorAll('ul').forEach(el => el.classList.add('list-disc','ml-6','my-2','space-y-1'));
        root.querySelectorAll('ol').forEach(el => el.classList.add('list-decimal','ml-6','my-2','space-y-1'));
        // Links
        root.querySelectorAll('a').forEach(el => el.classList.add('text-brand-600','hover:underline'));
        // Blockquotes
        root.querySelectorAll('blockquote').forEach(el => el.classList.add('border-l-4','border-brand-500','pl-4','italic','my-3','text-neutral-600','dark:text-neutral-300'));
        // Tables
        root.querySelectorAll('table').forEach(table => {
            table.classList.add('w-full','text-left','text-sm','my-3','border-collapse');
            table.querySelectorAll('th').forEach(th => th.classList.add('border','border-neutral-200','dark:border-neutral-800','px-3','py-2','bg-neutral-100','dark:bg-neutral-800','font-semibold'));
            table.querySelectorAll('td').forEach(td => td.classList.add('border','border-neutral-200','dark:border-neutral-800','px-3','py-2'));
        });
        // Inline code
        root.querySelectorAll('p > code, li > code').forEach(el => el.classList.add('bg-neutral-200','dark:bg-neutral-800','px-1.5','py-0.5','rounded','text-sm'));
        // Horizontal rule
        root.querySelectorAll('hr').forEach(el => el.classList.add('my-4','border-neutral-200','dark:border-neutral-800'));
    }

    function sendMessage() {
        const message = userInput.value.trim();

        if (!message) return;

        userInput.value = '';
        userInput.style.height = 'auto';

        addMessage('user', message);

        userInput.disabled = true;
        sendButton.disabled = true;

        showLoading();

        if (!conversationId) {
            initializeConversation();

            setTimeout(() => {
                getChatResponse(message);
            }, 1000);
        } else {
            getChatResponse(message);
        }
    }

    function getChatResponse(message) {
        fetch('/api/chat', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                conversation_id: conversationId,
                question: message,
                use_realtime: true
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            hideLoading();

            if (data.error) {
                throw new Error(data.error);
            }

            addMessage('assistant', data.answer);

            userInput.disabled = false;
            sendButton.disabled = false;
            userInput.focus();
        })
        .catch(error => {
            hideLoading();
            console.error('Error:', error);
            addMessage('assistant', 'Sorry, there was an error: ' + error.message);
            userInput.disabled = false;
            sendButton.disabled = false;
        });
    }

    sendButton.addEventListener('click', sendMessage);

    userInput.addEventListener('keydown', function(event) {

        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    resetButton.addEventListener('click', resetConversation);

    suggestionButtons.forEach(button => {
        button.addEventListener('click', function() {
            userInput.value = this.textContent;
            userInput.dispatchEvent(new Event('input')); 
            sendMessage();
        });
    });

    initializeConversation();

    userInput.focus();
});