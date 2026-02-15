#!/usr/bin/env python3
"""
Generate complete HTML for Postmodernisme with ALL images
"""

from pathlib import Path
import re

base_dir = Path('/root/.openclaw/workspace/kunstgeschiedenis')
website_dir = base_dir / 'website'
img_dir = website_dir / 'images'

# Read the markdown file
md_path = base_dir / 'postmodernisme.md'
content = md_path.read_text(encoding='utf-8')

# Find all artworks using regex
artwork_pattern = r'### (\d+)\. "([^"]+)" \(([^)]+)\) — ([^\n]+)\n\n\*\*Museum:\*\* ([^\n]+)\n\*\*Techniek:\*\* ([^\n]+)(.+?)(?=### \d+\. |$)'

matches = list(re.finditer(artwork_pattern, content, re.DOTALL))

print(f"Found {len(matches)} artworks")

# Build HTML for each artwork
artworks_html = []

for i, match in enumerate(matches, 1):
    number = match.group(1)
    title = match.group(2)
    year = match.group(3)
    artist = match.group(4)
    museum = match.group(5)
    technique = match.group(6)
    body = match.group(7)
    
    # Map to image
    image_map = {
        1: 'warhol_soup.jpg',
        2: None,  # Kruger - no image
        3: 'hirst_shark.jpg',
        4: 'gonzalez_candy.jpg',
        5: 'emin_tracey.jpg',
        6: None,  # Marclay - no image
        7: 'kapoor_cloud.jpg',
        8: 'banksy_balloon.jpg',
        9: 'kusama_room.jpg',
        10: 'eliasson_weather.jpg',
    }
    
    img_file = image_map.get(i)
    
    if img_file and (img_dir / img_file).exists():
        img_html = f'<div class="artwork-image-full"><img src="images/{img_file}" alt="{title}" loading="lazy"></div>'
    else:
        img_html = f'<div class="artwork-image-full" style="background:#f5f5f5; padding:4rem; text-align:center; color:#666; border:2px dashed #ddd;"><p style="margin:0; font-size:1.2rem;">🖼️ Afbeelding niet beschikbaar op Wikimedia Commons</p><p style="margin:0.5rem 0 0 0; font-size:0.9rem;">{title} ({year}) — {artist}</p></div>'
    
    # Process body text
    body = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', body)
    body = re.sub(r'^\n+', '', body)
    body = body.replace('\n\n', '</p><p>')
    body = '<p>' + body + '</p>'
    
    artwork_html = f'''
<div class="artwork-fullwidth">
    <div class="artwork-header">
        <h3>{number}. "{title}" ({year}) — {artist}</h3>
        <p style="margin:0.5rem 0 0 0; color:#666; font-style:italic;">{museum} | {technique}</p>
    </div>
    {img_html}
    <div class="artwork-content">
        {body}
    </div>
</div>
'''
    artworks_html.append(artwork_html)

print(f"Generated HTML for {len(artworks_html)} artworks")

# Now build the full page
intro_match = re.match(r'(.+?)## De Tien Meest Invloedrijke Werken', content, re.DOTALL)
if intro_match:
    intro = intro_match.group(1)
else:
    intro = content

# Process intro
intro = re.sub(r'### (.+?)\n', r'<h3>\1</h3>', intro)
intro = re.sub(r'## (.+?)\n', r'<h2>\1</h2>', intro)
intro = re.sub(r'# (.+?)\n', r'<h1>\1</h1>', intro)
intro = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', intro)
intro = re.sub(r'^- ', r'<li>', intro, flags=re.MULTILINE)
intro = intro.replace('\n\n', '</p><p>')
intro = '<p>' + intro + '</p>'

# Build full HTML
html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Postmodernisme - Kunstgeschiedenis</title>
    <link rel="stylesheet" href="style.css">
    <style>
        .featured-artwork {{
            background: linear-gradient(135deg, #f8f4e8 0%, #fff9e6 100%);
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 8px;
            text-align: center;
        }}
        .featured-artwork h2 {{
            color: #1a1a1a;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }}
        .featured-artist {{
            color: #666;
            font-style: italic;
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }}
        .featured-image {{
            width: 100%;
            max-width: 900px;
            border-radius: 8px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        }}
        .artwork-fullwidth {{
            background: #fff;
            margin: 3rem 0;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
        }}
        .artwork-header {{
            border-bottom: 3px solid #c9a227;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
        }}
        .artwork-header h3 {{
            color: #1a1a1a;
            font-size: 1.6rem;
            margin: 0;
        }}
        .artwork-image-full {{
            width: 100%;
            margin: 2rem 0;
            text-align: center;
        }}
        .artwork-image-full img {{
            width: 100%;
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }}
        .artwork-content {{
            padding: 0 1rem;
        }}
        .artwork-content p {{
            text-align: justify;
            line-height: 1.7;
            margin-bottom: 1rem;
        }}
    </style>
</head>
<body>
    <header>
        <h1>🎨 Postmodernisme</h1>
        <p class="subtitle">1960-heden</p>
    </header>

    <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="neoclassicisme.html">Neoclassicisme</a>
        <a href="romanticisme.html">Romanticisme</a>
        <a href="expressionisme.html">Expressionisme</a>
        <a href="kubisme.html">Kubisme</a>
        <a href="postmodernisme.html" class="active">Postmodernisme</a>
    </nav>

    <main>
        <section class="movement-header">
            <div class="featured-artwork">
                <h2>Meesterwerk: Campbell's Soup Cans</h2>
                <p class="featured-artist">Andy Warhol, 1962</p>
                <img src="images/warhol_soup.jpg" alt="Campbell's Soup Cans" class="featured-image">
            </div>
            {intro}
        </section>

        <section class="content-section">
            <h2>De Tien Meest Invloedrijke Werken</h2>
            {''.join(artworks_html)}
        </section>
    </main>

    <footer>
        <p>Kunstgeschiedenis Project | matthiasr.com/art</p>
    </footer>
</body>
</html>
'''

# Write file
output_file = website_dir / 'postmodernisme.html'
output_file.write_text(html, encoding='utf-8')
print(f"✅ Generated: {output_file.name}")
print(f"✅ Total artworks with content: {len(artworks_html)}")
