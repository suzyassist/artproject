#!/usr/bin/env python3
"""
Generate complete HTML for Postmodernisme with ALL images
"""

from pathlib import Path
import re

base_dir = Path('/root/.openclaw/workspace/kunstgeschiedenis')
website_dir = base_dir / 'website'
img_dir = website_dir / 'images'

def md_to_html(text):
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

def get_image_for_artwork(number, title, artist):
    """Map artwork to image file"""
    mappings = {
        1: ('warhol_soup.jpg', "Campbell's Soup Cans"),
        2: ('kruger_untitled.jpg', 'Untitled (I shop therefore I am)'),
        3: ('hirst_shark.jpg', 'The Physical Impossibility of Death'),
        4: ('gonzalez_candy.jpg', 'Untitled (Portrait of Ross in L.A.)'),
        5: ('emin_tracey.jpg', 'My Bed'),
        6: ('marclay_clock.jpg', 'The Clock'),
        7: ('kapoor_cloud.jpg', 'Cloud Gate'),
        8: ('banksy_balloon.jpg', 'Girl with a Balloon'),
        9: ('kusama_room.jpg', 'Infinity Mirror Rooms'),
        10: ('eliasson_weather.jpg', 'The Weather Project'),
    }
    
    if number in mappings:
        img_file, img_title = mappings[number]
        img_path = img_dir / img_file
        if img_path.exists():
            return img_file
    return None

# Read the markdown file
md_path = base_dir / 'postmodernisme.md'
content = md_path.read_text(encoding='utf-8')

# Split into sections
sections = content.split('\n## ')
intro_section = sections[0]

# Build intro HTML
intro_html = md_to_html(intro_section)

# Build artworks HTML
artworks_html = []

for section in sections[1:]:
    if not section.strip():
        continue
    
    # Check if it's an artwork section
    match = re.match(r'^(\d+)\. "([^"]+)" \(([^)]+)\) — ([^\n]+)', section)
    if match:
        number, title, year, artist = match.groups()
        number = int(number)
        
        # Get image
        img_file = get_image_for_artwork(number, title, artist)
        
        if img_file:
            img_html = f'<div class="artwork-image-full"><img src="images/{img_file}" alt="{title}" loading="lazy"></div>'
        else:
            img_html = '<div class="artwork-image-full" style="background:#f0f0f0; padding:3rem; text-align:center; color:#999;">[Afbeelding niet beschikbaar op Wikimedia Commons]</div>'
        
        # Process section content
        section_content = section[section.find('\n'):]
        section_html = md_to_html(section_content)
        
        artwork_html = f'''
<div class="artwork-fullwidth">
    <div class="artwork-header">
        <h3>{number}. "{title}" ({year}) — {artist}</h3>
    </div>
    {img_html}
    <div class="artwork-content">
        {section_html}
    </div>
</div>
'''
        artworks_html.append(artwork_html)
    else:
        # Regular section
        section_html = md_to_html('## ' + section)
        artworks_html.append(f'<section class="content-section">\n{section_html}\n</section>')

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
        .artwork-content h4 {{
            color: #333;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }}
        .artwork-content p {{
            text-align: justify;
            line-height: 1.7;
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
            {intro_html}
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
print(f"   Total artworks: {len([a for a in artworks_html if 'artwork-fullwidth' in a])}")
