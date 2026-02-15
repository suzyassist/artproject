#!/usr/bin/env python3
"""
Generate complete HTML pages for Neoclassicisme and Postmodernisme
"""

from pathlib import Path
import re

base_dir = Path('/root/.openclaw/workspace/kunstgeschiedenis')
website_dir = base_dir / 'website'

def md_to_html(text):
    """Convert markdown to HTML"""
    text = re.sub(r'^### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    lines = text.split('\n')
    result = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            content = line.strip()[2:]
            result.append(f'<li>{content}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    
    if in_list:
        result.append('</ul>')
    
    text = '\n'.join(result)
    
    paragraphs = []
    for line in text.split('\n'):
        line = line.strip()
        if line and not line.startswith('<') and not line.startswith('**'):
            paragraphs.append(f'<p>{line}</p>')
        else:
            paragraphs.append(line)
    
    return '\n'.join(paragraphs)

def generate_full_page(md_file, title, period, artworks_list):
    """Generate complete HTML page with inline images"""
    md_path = base_dir / md_file
    content = md_path.read_text(encoding='utf-8')
    
    # Split by artwork sections
    pattern = r'### (\d+)\. "([^"]+)" \(([^)]+)\) — ([^\n]+)'
    parts = re.split(pattern, content)
    
    html_parts = []
    intro_text = parts[0]
    
    # Get featured artwork (first in list)
    featured = artworks_list[0]
    featured_img = f'<img src="images/{featured["file"]}" alt="{featured["title"]}" class="featured-image">'
    
    intro_html = f'''
<section class="movement-header">
    <div class="featured-artwork">
        <h2>Meesterwerk: {featured['title']}</h2>
        <p class="featured-artist">{featured['artist']}, {featured['year']}</p>
        {featured_img}
    </div>
    {md_to_html(intro_text)}
</section>
'''
    html_parts.append(intro_html)
    
    # Process each artwork
    for i in range(1, len(parts), 5):
        if i + 4 < len(parts):
            number = parts[i]
            title = parts[i+1]
            year = parts[i+2]
            artist = parts[i+3]
            section_content = parts[i+4]
            
            artwork = None
            for art in artworks_list:
                if art['title'] in title or title in art['title']:
                    artwork = art
                    break
            
            img_html = ''
            if artwork:
                img_html = f'<img src="images/{artwork["file"]}" alt="{artwork["title"]}" class="artwork-image">'
            
            section_html = md_to_html(section_content)
            
            artwork_section = f'''
<div class="artwork" id="werk{number}">
    <h4>{number}. "{title}" ({year}) — {artist}</h4>
    {img_html}
    <div class="artwork-text">
        {section_html}
    </div>
</div>
'''
            html_parts.append(artwork_section)
    
    content_html = '\n'.join(html_parts)
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Kunstgeschiedenis</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>🎨 {title}</h1>
        <p class="subtitle">{period}</p>
    </header>

    <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="neoclassicisme.html"{' class="active"' if 'neoclassicisme' in md_file else ''}>Neoclassicisme</a>
        <a href="romanticisme.html">Romanticisme</a>
        <a href="expressionisme.html">Expressionisme</a>
        <a href="kubisme.html">Kubisme</a>
        <a href="postmodernisme.html"{' class="active"' if 'postmodernisme' in md_file else ''}>Postmodernisme</a>
    </nav>

    <main>
        {content_html}
    </main>

    <footer>
        <p>Kunstgeschiedenis Project | matthiasr.com/art</p>
    </footer>
</body>
</html>
'''
    
    output_file = website_dir / md_file.replace('.md', '.html')
    output_file.write_text(html, encoding='utf-8')
    print(f"✅ Generated: {output_file.name}")

# Artwork data
NEOCLASSICISME_ARTWORKS = [
    {'file': 'david_horatii.jpg', 'title': 'De Eed van de Horatii', 'artist': 'Jacques-Louis David', 'year': '1784'},
    {'file': 'david_napoleon.jpg', 'title': 'Napoleon bij de Sint-Bernardpas', 'artist': 'Jacques-Louis David', 'year': '1801'},
    {'file': 'canova_psyche.jpg', 'title': 'Cupid and Psyche', 'artist': 'Antonio Canova', 'year': '1787-1793'},
    {'file': 'canova_pauline.jpg', 'title': 'Pauline Bonaparte als Venus Victrix', 'artist': 'Antonio Canova', 'year': '1805-1808'},
]

POSTMODERNISME_ARTWORKS = [
    {'file': 'warhol_soup.jpg', 'title': "Campbell's Soup Cans", 'artist': 'Andy Warhol', 'year': '1962'},
    {'file': 'banksy_balloon.jpg', 'title': 'Girl with a Balloon', 'artist': 'Banksy', 'year': '2002'},
]

print("="*60)
print("GENERATING FULL HTML PAGES")
print("="*60)

generate_full_page('neoclassicisme.md', 'Neoclassicisme', '1750-1850', NEOCLASSICISME_ARTWORKS)
generate_full_page('postmodernisme.md', 'Postmodernisme', '1960-heden', POSTMODERNISME_ARTWORKS)

print("\n" + "="*60)
print("PAGES GENERATED!")
print("="*60)
