#!/usr/bin/env python3
"""
Script to create enhanced grammar HTML files from markdown files.
This script takes a markdown file and converts it to an enhanced HTML file
with improved styling, navigation, and interactive elements.
"""

import os
import sys
import re
import argparse
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔄 {title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}
        h1 {{
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        h2 {{
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        h3 {{
            font-size: 1.25em;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #f6f8fa;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background-color: #f6f8fa;
        }}
        blockquote {{
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin: 0 0 16px 0;
        }}
        .vocabulary {{
            color: #e53935;
            font-weight: bold;
        }}
        .grammar {{
            color: #1e88e5;
            font-weight: bold;
        }}
        .example {{
            color: #43a047;
            font-weight: bold;
        }}
        .communication {{
            color: #8e24aa;
            font-weight: bold;
        }}
        hr {{
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }}
        code {{
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            background-color: rgba(27, 31, 35, 0.05);
            padding: 0.2em 0.4em;
            border-radius: 3px;
        }}
        pre {{
            background-color: #f6f8fa;
            border-radius: 3px;
            padding: 16px;
            overflow: auto;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        }}
        .correct {{
            color: #43a047;
        }}
        .incorrect {{
            color: #e53935;
            text-decoration: line-through;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        /* Navigation bar */
        .navbar {{
            background-color: #3f51b5;
            color: white;
            padding: 10px 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }}
        .navbar a {{
            color: white;
            margin-right: 15px;
            text-decoration: none;
        }}
        .navbar a:hover {{
            text-decoration: underline;
        }}
        /* Mind map styling */
        .mind-map {{
            font-family: monospace;
            white-space: pre;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.3;
        }}
        /* Memory trick box */
        .memory-trick {{
            background-color: #fff8e1;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        /* Fun examples box */
        .fun-examples {{
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        /* Grammar connection box */
        .grammar-connection {{
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        /* Communication phrases box */
        .communication-box {{
            background-color: #f3e5f5;
            border-left: 4px solid #9c27b0;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        /* What I can do now box */
        .can-do-box {{
            background-color: #e8eaf6;
            border: 2px solid #3f51b5;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        /* Emoji for fun */
        .emoji {{
            font-size: 1.2em;
        }}
        /* Quick reference box */
        .quick-reference {{
            background-color: #e8f5e9;
            border: 2px solid #4caf50;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="navbar">
        <a href="../../">Home</a>
        <a href="../../Lektion%231/README.html">Lektion 1</a>
        <a href="../../Lektion%232/README.html">Lektion 2</a>
        <a href="../../Lektion%233/README.html">Lektion 3</a>
        <a href="../../Lektion%234/README.html">Lektion 4</a>
        <a href="../../reference_docs/README.html">Reference</a>
    </div>

    {content}
</body>
</html>
"""

def extract_title(content):
    """Extract the title from the markdown content."""
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1)
    return "Grammar"

def create_mind_map(lesson_number):
    """Create a mind map based on the lesson number."""
    if lesson_number == 1:
        return """<h2>🧩 Grammar Mind Map: How Everything Connects</h2>
    <div class="mind-map">
                    ┌─── A1: Simple Present Tense
                    │
PRÄTERITUM ─────────┼─── A2: Perfekt (haben/sein + PP)
                    │
                    └─── B1.1: Präteritum (simple past)

                    ┌─── A1: Basic Time Expressions
                    │
ALS ────────────────┼─── A2: wenn (repeated events)
                    │
                    └─── B1.1: als (one-time past events)

                    ┌─── A1: Present Tense
                    │
PLUSQUAMPERFEKT ────┼─── A2: Perfekt (haben/sein + PP)
                    │
                    └─── B1.1: Plusquamperfekt (had done)
    </div>"""
    elif lesson_number == 2:
        return """<h2>🧩 Grammar Mind Map: How Everything Connects</h2>
    <div class="mind-map">
                    ┌─── A1: Einfache Sätze mit "und"
                    │
OBWOHL ─────────────┼─── A2: Nebensätze mit "weil", "dass"
                    │
                    └─── B1.1: Gegensätze mit "obwohl"

                    ┌─── A1: Adjektive (gut, schlecht)
                    │
GRADPARTIKELN ──────┼─── A2: Adverbien (sehr, ziemlich)
                    │
                    └─── B1.1: Gradpartikeln (echt, total, nicht so)

                    ┌─── A1: Personalpronomen (ich, du, er)
                    │
RELATIVPRONOMEN ────┼─── A2: Possessivpronomen (mein, dein)
                    │
                    └─── B1.1: Relativpronomen (der, die, das)
    </div>"""
    elif lesson_number == 3:
        return """<h2>🧩 Grammar Mind Map: How Everything Connects</h2>
    <div class="mind-map">
                    ┌─── A1: Aktiv (Ich öffne das Fenster)
                    │
PASSIV MIT MODAL ───┼─── A2: Einfaches Passiv (Das Fenster wird geöffnet)
                    │
                    └─── B1.1: Passiv mit Modalverben (Das Fenster muss geöffnet werden)

                    ┌─── A1: Possessivpronomen (mein, dein)
                    │
GENITIV ────────────┼─── A2: Possessivartikel (Peters Auto)
                    │
                    └─── B1.1: Genitiv (des Mannes, der Frau)

                    ┌─── A1: Grundzahlen (eins, zwei, drei)
                    │
BRUCHZAHLEN ────────┼─── A2: Prozente (50%, 25%)
                    │
                    └─── B1.1: Bruchzahlen (die Hälfte, ein Drittel)
    </div>"""
    elif lesson_number == 4:
        return """<h2>🧩 Grammar Mind Map: How Everything Connects</h2>
    <div class="mind-map">
                    ┌─── A1: Einfache Bedingungen (wenn + Präsens)
                    │
KONJUNKTIV II ──────┼─── A2: Höfliche Bitten (Könnten Sie...)
                    │
                    └─── B1.1: Irreale Bedingungen (Wenn ich... hätte/wäre/könnte)

                    ┌─── A1: Präpositionen mit Akkusativ/Dativ
                    │
WEGEN + GENITIV ────┼─── A2: Präpositionen mit festen Fällen
                    │
                    └─── B1.1: Wegen + Genitiv (wegen des Wetters)

                    ┌─── A1: Einfache Fragen (Wo? Wann?)
                    │
HÖFLICHE FRAGEN ────┼─── A2: Indirekte Fragen (Ich möchte wissen, ob...)
                    │
                    └─── B1.1: Höfliche Fragen (Könnten Sie mir sagen, ob...)
    </div>"""
    else:
        return ""

def enhance_content(content, lesson_number):
    """Enhance the markdown content with additional HTML elements."""
    # Extract the title
    title = extract_title(content)
    
    # Add mind map after the color coding section
    mind_map = create_mind_map(lesson_number)
    content = re.sub(r'(## 🎨 Farbkodierung.*?</ul>)', r'\1\n\n' + mind_map, content, flags=re.DOTALL)
    
    # Enhance examples with fun-examples box
    content = re.sub(r'(### 🔍 Beispiele.*?)(?=###|\n## |\Z)', 
                    r'<div class="fun-examples">\n\1\n</div>', 
                    content, flags=re.DOTALL)
    
    # Enhance memory aids with memory-trick box
    content = re.sub(r'(### 💡 Gedächtnisstützen.*?)(?=###|\n## |\Z)', 
                    r'<div class="memory-trick">\n\1\n</div>', 
                    content, flags=re.DOTALL)
    
    # Add grammar connection boxes
    grammar_sections = re.findall(r'## \d️⃣ (.*?)(?=## \d️⃣|\Z)', content, re.DOTALL)
    for section in grammar_sections:
        section_title = re.search(r'(.*?)(?=\n)', section).group(1)
        connection_box = f"""<div class="grammar-connection">
        <h3>👉 Grammar Connection</h3>
        <ul>
            <li><strong>A1 Connection</strong>: Basic concepts related to {section_title}</li>
            <li><strong>A2 Connection</strong>: Intermediate concepts building on {section_title}</li>
            <li><strong>Remember</strong>: Key points about {section_title}</li>
        </ul>
    </div>"""
        enhanced_section = section + connection_box
        content = content.replace(section, enhanced_section)
    
    # Add "What I can do now" box at the end
    can_do_box = """<div class="can-do-box">
        <h2>🎯 Was ich jetzt kann! (What I Can Do Now!)</h2>
        <p>Ich kann jetzt...</p>
        <ul>
            <li>...über irreale Bedingungen sprechen: <span class="example">"Wenn ich mehr Zeit hätte, würde ich mehr lesen."</span></li>
            <li>...Wichtigkeit ausdrücken und begründen: <span class="example">"Für mich ist es wichtig, dass ich jeden Tag Sport treibe."</span></li>
            <li>...höflich um Informationen bitten: <span class="example">"Könnten Sie mir bitte sagen, wo der Bahnhof ist?"</span></li>
            <li>...um Wiederholung bitten: <span class="example">"Entschuldigung, könnten Sie das bitte wiederholen?"</span></li>
            <li>...über Sprachen sprechen: <span class="example">"Meine Muttersprache ist Deutsch, aber ich lerne auch Englisch."</span></li>
        </ul>
    </div>"""
    
    if "# Zusammenfassung" in content:
        content = content.replace("# Zusammenfassung", can_do_box + "\n\n# Zusammenfassung")
    else:
        content += "\n\n" + can_do_box
    
    # Add quick reference at the end
    quick_reference = """<div class="memory-trick">
        <h3>💡 Super Quick Reference 📋</h3>
        <table>
            <thead>
                <tr>
                    <th>Grammar Point</th>
                    <th>Remember This!</th>
                    <th>Example</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Konjunktiv II</td>
                    <td>Für irreale Bedingungen und Wünsche</td>
                    <td>Wenn ich Zeit <span class="grammar">hätte</span>, <span class="grammar">würde</span> ich kommen.</td>
                </tr>
                <tr>
                    <td>Wegen + Genitiv</td>
                    <td>Für Gründe und Ursachen</td>
                    <td><span class="grammar">Wegen des</span> schlechten Wetters bleibe ich zu Hause.</td>
                </tr>
                <tr>
                    <td>Höfliche Fragen</td>
                    <td>Mit Modalverben und Konjunktiv II</td>
                    <td><span class="grammar">Könnten Sie mir</span> bitte helfen?</td>
                </tr>
            </tbody>
        </table>
    </div>"""
    
    content += "\n\n" + quick_reference
    
    return content

def convert_md_to_html(content):
    """Convert markdown content to HTML."""
    # This is a very simple conversion, for a real implementation you might want to use a library like markdown
    # Convert headers
    content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    
    # Convert paragraphs
    content = re.sub(r'(?<!\n\n)^(?!<h|<div|<p|<ul|<ol|<table|<pre|$)(.*?)$', r'<p>\1</p>', content, flags=re.MULTILINE)
    
    # Convert lists
    content = re.sub(r'^- (.*?)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'(<li>.*?</li>\n)+', r'<ul>\n\g<0></ul>', content, flags=re.DOTALL)
    
    # Convert code blocks
    content = re.sub(r'```(.*?)```', r'<pre>\1</pre>', content, flags=re.DOTALL)
    
    # Convert inline code
    content = re.sub(r'`(.*?)`', r'<code>\1</code>', content)
    
    # Convert bold text
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    
    # Convert italic text
    content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
    
    # Convert links
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
    
    # Convert horizontal rules
    content = re.sub(r'^---$', r'<hr>', content, flags=re.MULTILINE)
    
    return content

def process_file(input_file, output_file=None, lesson_number=None):
    """Process a markdown file and create an enhanced HTML file."""
    # Determine the lesson number if not provided
    if lesson_number is None:
        match = re.search(r'Lektion#(\d+)', input_file)
        if match:
            lesson_number = int(match.group(1))
        else:
            lesson_number = 1  # Default to lesson 1
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Enhance the content
    enhanced_content = enhance_content(content, lesson_number)
    
    # Convert to HTML
    html_content = convert_md_to_html(enhanced_content)
    
    # Determine the output file if not provided
    if output_file is None:
        output_file = input_file.replace('.md', '-Enhanced.html')
    
    # Create the HTML file
    title = extract_title(content)
    html = HTML_TEMPLATE.format(title=title, content=html_content)
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Enhanced HTML file created: {output_file}")

def main():
    """Main function to parse arguments and process files."""
    parser = argparse.ArgumentParser(description='Create enhanced grammar HTML files from markdown files.')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output HTML file')
    parser.add_argument('-l', '--lesson', type=int, help='Lesson number (1-4)')
    
    args = parser.parse_args()
    
    process_file(args.input_file, args.output, args.lesson)

if __name__ == '__main__':
    main()
