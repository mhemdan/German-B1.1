#!/usr/bin/env python3
"""
Convert Lektion#4 Markdown files to HTML for GitHub Pages
"""

import os
import re
import sys
import markdown
from pathlib import Path

# Configuration
INPUT_DIR = "Lektion#4"  # Lektion#4 directory
EXTENSIONS = [
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.nl2br',
]

# CSS styles for the HTML files
CSS_STYLES = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 24px;
        margin-bottom: 16px;
        font-weight: 600;
        line-height: 1.25;
    }
    h1 {
        font-size: 2em;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 0.3em;
    }
    h2 {
        font-size: 1.5em;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 0.3em;
    }
    h3 {
        font-size: 1.25em;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 20px;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px 12px;
        text-align: left;
    }
    th {
        background-color: #f6f8fa;
        font-weight: 600;
    }
    tr:nth-child(even) {
        background-color: #f6f8fa;
    }
    blockquote {
        padding: 0 1em;
        color: #6a737d;
        border-left: 0.25em solid #dfe2e5;
        margin: 0 0 16px 0;
    }
    .vocabulary {
        color: #e53935;
        font-weight: bold;
    }
    .grammar {
        color: #1e88e5;
        font-weight: bold;
    }
    .example {
        color: #43a047;
        font-weight: bold;
    }
    .communication {
        color: #8e24aa;
        font-weight: bold;
    }
    hr {
        height: 0.25em;
        padding: 0;
        margin: 24px 0;
        background-color: #e1e4e8;
        border: 0;
    }
    code {
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        background-color: rgba(27, 31, 35, 0.05);
        padding: 0.2em 0.4em;
        border-radius: 3px;
    }
    pre {
        background-color: #f6f8fa;
        border-radius: 3px;
        padding: 16px;
        overflow: auto;
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }
    .correct {
        color: #43a047;
    }
    .incorrect {
        color: #e53935;
        text-decoration: line-through;
    }
    a {
        color: #0366d6;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    /* Navigation bar */
    .navbar {
        background-color: #3f51b5;
        color: white;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    .navbar a {
        color: white;
        margin-right: 15px;
        text-decoration: none;
    }
    .navbar a:hover {
        text-decoration: underline;
    }
</style>
"""

# HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css_styles}
</head>
<body>
    <div class="navbar">
        <a href="../index.html">Home</a>
        <a href="../Lektion%231/README.html">Lektion 1</a>
        <a href="../Lektion%232/README.html">Lektion 2</a>
        <a href="../Lektion%233/README.html">Lektion 3</a>
        <a href="../Lektion%234/README.html">Lektion 4</a>
        <a href="../reference_docs/README.html">Reference</a>
    </div>
    {content}
</body>
</html>
"""

def convert_md_to_html(md_file_path):
    """Convert a Markdown file to HTML."""
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title from the first heading
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(md_file_path)
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=EXTENSIONS)
    
    # Replace span style color tags with class-based styling
    html_content = re.sub(
        r'<span style="color:red;">(.*?)</span>', 
        r'<span class="vocabulary">\1</span>', 
        html_content
    )
    html_content = re.sub(
        r'<span style="color:blue;">(.*?)</span>', 
        r'<span class="grammar">\1</span>', 
        html_content
    )
    html_content = re.sub(
        r'<span style="color:green;">(.*?)</span>', 
        r'<span class="example">\1</span>', 
        html_content
    )
    html_content = re.sub(
        r'<span style="color:purple;">(.*?)</span>', 
        r'<span class="communication">\1</span>', 
        html_content
    )
    
    # Fix internal links (.md to .html) and encode special characters in URLs
    def url_encode_path(match):
        path = match.group(1)
        # URL encode the # character in paths
        path = path.replace('#', '%23')
        return f'href="{path}.html"'
    
    html_content = re.sub(r'href="([^"]+)\.md"', url_encode_path, html_content)
    
    # Create the complete HTML document
    html_document = HTML_TEMPLATE.format(
        title=title,
        css_styles=CSS_STYLES,
        content=html_content
    )
    
    # Determine the output path
    html_file_path = str(md_file_path).replace('.md', '.html')
    
    # Write the HTML file
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_document)
    
    print(f"Converted {md_file_path} to {html_file_path}")
    return html_file_path

def find_md_files(directory):
    """Find all Markdown files in the given directory and its subdirectories."""
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                md_files.append(os.path.join(root, file))
    return md_files

def main():
    """Main function to convert all Markdown files to HTML."""
    print("Converting Lektion#4 Markdown files to HTML...")
    
    # Find all Markdown files
    md_files = find_md_files(INPUT_DIR)
    print(f"Found {len(md_files)} Markdown files")
    
    # Convert each Markdown file to HTML
    converted_files = []
    for md_file in md_files:
        try:
            html_file = convert_md_to_html(md_file)
            converted_files.append(html_file)
        except Exception as e:
            print(f"Error converting {md_file}: {e}")
    
    print(f"Successfully converted {len(converted_files)} files to HTML")
    print("Done!")

if __name__ == "__main__":
    main()
