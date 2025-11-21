#!/usr/bin/env python3
"""
Script to add Node.js button and enhancement libraries to index.html
"""

# Read the HTML file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Node.js button after JavaScript button
old_buttons = '''                    <button class="suggestion-btn" onclick="setInput('Find JavaScript projects')">
                        JavaScript
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Show good first issues in react')">'''

new_buttons = '''                    <button class="suggestion-btn" onclick="setInput('Find JavaScript projects')">
                        JavaScript
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Find Node.js projects')">
                        Node.js
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Show good first issues in react')">'''

content = content.replace(old_buttons, new_buttons)

# Add Prism.js before </head>
prism_libs = '''    <!-- Prism.js for code syntax highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
</head>'''

content = content.replace('</head>', prism_libs)

# Add enhancements.js before </body>
enhancements_script = '''    <script src="/static/enhancements.js"></script>
</body>'''

content = content.replace('</body>', enhancements_script)

# Write back
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully added Node.js button and enhancement libraries to index.html")
