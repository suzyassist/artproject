#!/usr/bin/env python3
"""
Generate complete HTML pages with FULL WIDTH images
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

def generate_full_page(md_file, title, period, featured_img, featured_title, featured_artist, featured_year):
    """Generate complete HTML page with full-width images"""
    md_path = base_dir / md_file
    content = md_path.read_text(encoding='utf-8')
    
    # Extract sections
    sections = content.split('\n## ')
    intro_section = sections[0]
    
    # Build intro HTML
    intro_html = md_to_html(intro_section)
    
    # Build artworks HTML
    artworks_html = []
    for section in sections[1:]:
        if not section.strip():
            continue
        
        # Check if it's an artwork section (starts with ### number)
        if re.match(r'^### \d+\. "', section):
            # Extract artwork info
            match = re.match(r'^### (\d+)\. "([^"]+)" \(([^)]+)\) — ([^\n]+)', section)
            if match:
                number, artwork_title, year, artist = match.groups()
                
                # Determine image filename based on title
                img_file = get_image_filename(md_file, artwork_title)
                
                # Build artwork HTML with FULL WIDTH image
                artwork_html = f'''
<div class="artwork-fullwidth">
    <div class="artwork-header">
        <h3>{number}. "{artwork_title}" ({year}) — {artist}</h3>
    </div>
    <div class="artwork-image-full">
        <img src="images/{img_file}" alt="{artwork_title}" loading="lazy">
    </div>
    <div class="artwork-content">
        {md_to_html(section)}
    </div>
</div>
'''
                artworks_html.append(artwork_html)
        else:
            # Regular section (Context, Stijlfiguren, etc.)
            section_html = md_to_html('## ' + section)
            artworks_html.append(f'<section class="content-section">\n{section_html}\n</section>')
    
    # Build full HTML
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Kunstgeschiedenis</title>
    <link rel="stylesheet" href="style.css">
    <style>
        /* Full width image styles */
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
        @media (min-width: 768px) {{
            .artwork-fullwidth {{
                padding: 3rem;
            }}
            .artwork-image-full img {{
                max-height: 600px;
                object-fit: contain;
            }}
        }}
    </style>
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
        <section class="movement-header">
            <div class="featured-artwork">
                <h2>Meesterwerk: {featured_title}</h2>
                <p class="featured-artist">{featured_artist}, {featured_year}</p>
                <img src="images/{featured_img}" alt="{featured_title}" class="featured-image">
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
    
    output_file = website_dir / md_file.replace('.md', '.html')
    output_file.write_text(html, encoding='utf-8')
    print(f"✅ Generated: {output_file.name}")

def get_image_filename(md_file, title):
    """Map artwork title to image filename"""
    # Neoclassicisme mappings
    if 'Marat' in title:
        return 'david_marat.jpg'
    elif 'Horatii' in title or 'Eed' in title:
        return 'david_horatii.jpg'
    elif 'Recamier' in title or 'Récamier' in title:
        return 'david_recamier.jpg'
    elif 'Napoleon' in title or 'Napoleon' in title:
        if 'David' in title:
            return 'david_napoleon.jpg'
        else:
            return 'ingres_napoleon.jpg'
    elif 'Psyche' in title and 'Gérard' in title:
        return 'gerard_psyche.jpg'
    elif 'Psyche' in title and 'Canova' in title:
        return 'canova_psyche.jpg'
    elif 'Pauline' in title or 'Venus Victrix' in title:
        return 'canova_pauline.jpg'
    elif 'Village' in title or 'Corbeil' in title:
        return 'greuze_village.jpg'
    elif 'Tiepolo' in title or 'Apollo' in title:
        return 'tiepolo_apollo.jpg'
    elif 'Chardin' in title or 'Atelier' in title:
        return 'chardin_portrait.jpg'
    elif 'Brutus' in title:
        return 'david_brutus.jpg'
    
    # Postmodernisme mappings
    elif 'Soup' in title:
        return 'warhol_soup.jpg'
    elif 'Balloon' in title or 'Banksy' in title:
        return 'banksy_balloon.jpg'
    elif 'My Bed' in title or 'Emin' in title:
        return 'emin_tracey.jpg'
    elif 'Shark' in title or 'Hirst' in title:
        return 'hirst_shark.jpg'
    elif 'Clock' in title or 'Marclay' in title:
        return 'marclay_clock.jpg'
    elif 'Cloud' in title or 'Kapoor' in title:
        return 'kapoor_cloud.jpg'
    elif 'Kruger' in title:
        return 'kruger_untitled.jpg'
    elif 'González-Torres' in title or 'Candy' in title:
        return 'gonzalez_candy.jpg'
    elif 'Kusama' in title or 'Infinity' in title:
        return 'kusama_room.jpg'
    elif 'Eliasson' in title or 'Weather' in title:
        return 'eliasson_weather.jpg'
    
    return 'placeholder.jpg'

print("="*60)
print("GENERATING HTML WITH FULL-WIDTH IMAGES")
print("="*60)

generate_full_page(
    'neoclassicisme.md', 
    'Neoclassicisme', 
    '1750-1850',
    'david_horatii.jpg',
    'De Eed van de Horatii',
    'Jacques-Louis David',
    '1784'
)

generate_full_page(
    'postmodernisme.md', 
    'Postmodernisme', 
    '1960-heden',
    'warhol_soup.jpg',
    "Campbell's Soup Cans",
    'Andy Warhol',
    '1962'
)

print("\n" + "="*60)
print("PAGES GENERATED WITH FULL-WIDTH IMAGES!")
print("="*60)
