#!/usr/bin/env python3
"""
Script to add cross-platform CSS to index.html
"""

# Read the HTML file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if cross-platform.css is already added
if 'cross-platform.css' not in content:
    # Add cross-platform CSS after styles.css
    old_css = '<link rel="stylesheet" href="/static/styles.css">'
    new_css = '''<link rel="stylesheet" href="/static/styles.css">
    <link rel="stylesheet" href="/static/cross-platform.css">'''
    
    content = content.replace(old_css, new_css)
    
    # Write back
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Successfully added cross-platform.css to index.html")
else:
    print("ℹ️  cross-platform.css already added")
