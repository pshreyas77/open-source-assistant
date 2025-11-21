#!/usr/bin/env python3
"""
Script to add MySQL button to quick actions in index.html
"""

# Read the HTML file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add MySQL button after Node.js button
old_buttons = '''                    <button class="suggestion-btn" onclick="setInput('Find Node.js projects')">
                        Node.js
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Show good first issues in react')">'''

new_buttons = '''                    <button class="suggestion-btn" onclick="setInput('Find Node.js projects')">
                        Node.js
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Find MySQL projects')">
                        MySQL
                    </button>
                    <button class="suggestion-btn" onclick="setInput('Show good first issues in react')">'''

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)
    
    # Write back
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Successfully added MySQL button to quick actions")
else:
    print("⚠️  Could not find the right location. MySQL button might already exist or HTML structure changed.")
