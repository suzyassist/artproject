#!/usr/bin/env python3
"""
Generate HTML pages for the art history website from markdown files
Images are placed inline with the text where discussed
"""

from pathlib import Path
import re

# Paths
base_dir = Path('/root/.openclaw/workspace/kunstgeschiedenis')
website_dir = base_dir / 'website'
img_dir = website_dir / 'images'

def md_to_html(text):
    """Convert markdown to HTML"""
    # Convert headers
    text = re.sub(r'^### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    
    # Convert bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    # Convert lists
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
    
    # Convert paragraphs
    paragraphs = []
    for line in text.split('\n'):
        line = line.strip()
        if line and not line.startswith('<') and not line.startswith('**'):
            paragraphs.append(f'<p>{line}</p>')
        else:
            paragraphs.append(line)
    
    return '\n'.join(paragraphs)

def generate_artwork_section(artwork, number):
    """Generate HTML for a single artwork with image inline"""
    img_path = img_dir / artwork['file']
    if img_path.exists():
        img_html = f'<img src="images/{artwork["file"]}" alt="{artwork["title"]}" class="artwork-image">'
    else:
        img_html = '<p class="artwork-meta">[Afbeelding niet beschikbaar]</p>'
    
    return f'''
<div class="artwork" id="werk{number}">
    <h4>{number}. "{artwork['title']}" ({artwork['year']}) — {artwork['artist']}</h4>
    <p class="artwork-meta">{artwork.get('museum', 'N/A')} | {artwork.get('techniek', 'Olieverf op doek')}</p>
    {img_html}
    <div class="artwork-description">
        <h5>Achtergrond</h5>
        <h5>Tijdsgeest Vertaling</h5>
        <h5>Stijlanalyse</h5>
    </div>
</div>
'''

def generate_page_with_inline_images(md_file, title, period, artworks_list, featured_artwork):
    """Generate HTML with images inline in the text"""
    md_path = base_dir / md_file
    if not md_path.exists():
        print(f"❌ File not found: {md_path}")
        return False
    
    content = md_path.read_text(encoding='utf-8')
    
    # Split content by artwork sections
    # Look for patterns like "### 1. "Title" (year) — Artist"
    pattern = r'### (\d+)\. "([^"]+)" \(([^)]+)\) — ([^\n]+)'
    
    parts = re.split(pattern, content)
    
    # Build HTML with inline images
    html_parts = []
    
    # First part is intro/context sections
    intro_text = parts[0]
    
    # Add featured artwork to intro
    featured_img = f'<img src="images/{featured_artwork["file"]}" alt="{featured_artwork["title"]}" class="featured-image">' if (img_dir / featured_artwork['file']).exists() else ''
    
    intro_html = f'''
<section class="movement-header">
    <div class="featured-artwork">
        <h2>Meesterwerk: {featured_artwork['title']}</h2>
        <p class="featured-artist">{featured_artwork['artist']}, {featured_artwork['year']}</p>
        {featured_img}
    </div>
    {md_to_html(intro_text)}
</section>
'''
    html_parts.append(intro_html)
    
    # Process each artwork section
    for i in range(1, len(parts), 5):  # 5 groups: number, title, year, artist, content
        if i + 4 < len(parts):
            number = parts[i]
            title = parts[i+1]
            year = parts[i+2]
            artist = parts[i+3]
            section_content = parts[i+4]
            
            # Find the artwork data
            artwork = None
            for art in artworks_list:
                if art['title'] == title or title in art['title'] or art['title'] in title:
                    artwork = art
                    break
            
            if artwork:
                img_html = f'<img src="images/{artwork["file"]}" alt="{artwork["title"]}" class="artwork-image">' if (img_dir / artwork['file']).exists() else ''
            else:
                img_html = ''
            
            # Convert section content
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
    
    # Build full HTML
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
        <a href="romanticisme.html"{' class="active"' if 'romanticisme' in md_file else ''}>Romanticisme</a>
        <a href="expressionisme.html"{' class="active"' if 'expressionisme' in md_file else ''}>Expressionisme</a>
        <a href="kubisme.html"{' class="active"' if 'kubisme' in md_file else ''}>Kubisme</a>
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
    
    # Write file
    output_file = website_dir / md_file.replace('_nieuw.md', '.html').replace('_volledig.md', '.html')
    output_file.write_text(html, encoding='utf-8')
    print(f"✅ Generated: {output_file.name}")
    return True

# Artwork data - Ordered by importance
ROMANTICISME_ARTWORKS = [
    {'file': 'liberty.jpg', 'title': 'De Vrijheid leidt het Volk', 'artist': 'Eugène Delacroix', 'year': '1830', 'museum': 'Musée du Louvre, Parijs', 'techniek': 'Olieverf op doek'},
    {'file': 'medusa.jpg', 'title': 'Het Vlot van de Medusa', 'artist': 'Théodore Géricault', 'year': '1818-1819', 'museum': 'Musée du Louvre, Parijs', 'techniek': 'Olieverf op doek'},
    {'file': 'wanderer.jpg', 'title': 'Wanderer above the Sea of Fog', 'artist': 'Caspar David Friedrich', 'year': '1818', 'museum': 'Kunsthalle Hamburg', 'techniek': 'Olieverf op doek'},
    {'file': 'saturn.jpg', 'title': 'Saturnus verslindt zijn Zoon', 'artist': 'Francisco de Goya', 'year': '1819-1823', 'museum': 'Museo del Prado, Madrid', 'techniek': 'Olieverf op doek'},
    {'file': 'tres_mayo.jpg', 'title': 'De Derde Mei 1808', 'artist': 'Francisco de Goya', 'year': '1814', 'museum': 'Museo del Prado, Madrid', 'techniek': 'Olieverf op doek'},
    {'file': 'eismeer.jpg', 'title': 'Het Zee van Ijs (Das Eismeer)', 'artist': 'Caspar David Friedrich', 'year': '1823-1824', 'museum': 'Hamburger Kunsthalle', 'techniek': 'Olieverf op doek'},
    {'file': 'turner_rain.jpg', 'title': 'Regen, Stoom en Snelheid', 'artist': 'J.M.W. Turner', 'year': '1844', 'museum': 'National Gallery, Londen', 'techniek': 'Olieverf op doek'},
    {'file': 'friedrich_moon.jpg', 'title': 'Twee Mannen beschouwen de Maan', 'artist': 'Caspar David Friedrich', 'year': '1819-1820', 'museum': 'Alte Nationalgalerie, Berlijn', 'techniek': 'Olieverf op doek'},
    {'file': 'turner_venice.jpg', 'title': 'De Brug der Zuchten', 'artist': 'J.M.W. Turner', 'year': '1840', 'museum': 'Tate Britain, Londen', 'techniek': 'Olieverf op doek'},
]

EXPRESSIONISME_ARTWORKS = [
    {'file': 'munch_schreeuw.jpg', 'title': 'De Schreeuw', 'artist': 'Edvard Munch', 'year': '1893', 'museum': 'National Gallery of Norway, Oslo', 'techniek': 'Olieverf, tempera en pastel op karton'},
    {'file': 'kirchner_berlijn.jpg', 'title': 'Straat, Berlijn', 'artist': 'Ernst Ludwig Kirchner', 'year': '1913', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
    {'file': 'kandinsky_compositie.jpg', 'title': 'Compositie VII', 'artist': 'Wassily Kandinsky', 'year': '1913', 'museum': 'Tretyakov Gallery, Moskou', 'techniek': 'Olieverf op doek'},
    {'file': 'marc_blauwe_paarden.jpg', 'title': 'De Toren van Blauwe Paarden', 'artist': 'Franz Marc', 'year': '1913', 'museum': 'Lenbachhaus, München', 'techniek': 'Olieverf op doek'},
    {'file': 'marc_gele_koe.jpg', 'title': 'Gele Koe', 'artist': 'Franz Marc', 'year': '1911', 'museum': 'Guggenheim, New York', 'techniek': 'Olieverf op doek'},
    {'file': 'kirchner_dance_hall.jpg', 'title': 'Dance Hall Bellevue', 'artist': 'Ernst Ludwig Kirchner', 'year': '1909-1910', 'museum': 'National Gallery of Art, Washington', 'techniek': 'Olieverf op doek'},
    {'file': 'kirchner_soldaat.jpg', 'title': 'Zelfportret als Soldaat', 'artist': 'Ernst Ludwig Kirchner', 'year': '1915', 'museum': 'Allen Memorial Art Museum, Oberlin', 'techniek': 'Olieverf op doek'},
    {'file': 'beckmann_nacht.jpg', 'title': 'De Nacht', 'artist': 'Max Beckmann', 'year': '1918-1919', 'museum': 'Kunstsammlung NRW, Düsseldorf', 'techniek': 'Olieverf op doek'},
    {'file': 'matisse_hoed.jpg', 'title': 'Vrouw met een Hoed', 'artist': 'Henri Matisse', 'year': '1905', 'museum': 'SFMOMA', 'techniek': 'Olieverf op doek'},
    {'file': 'matisse_rode_atelier.jpg', 'title': 'Het Rode Atelier', 'artist': 'Henri Matisse', 'year': '1911', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
]

KUBISME_ARTWORKS = [
    {'file': 'picasso_demoiselles.jpg', 'title': "Les Demoiselles d'Avignon", 'artist': 'Pablo Picasso', 'year': '1907', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
    {'file': 'picasso_kahnweiler.jpg', 'title': 'Portrait of Daniel-Henry Kahnweiler', 'artist': 'Pablo Picasso', 'year': '1910', 'museum': 'Art Institute of Chicago', 'techniek': 'Olieverf op doek'},
    {'file': 'braque_trees_estaque.jpg', 'title': 'Trees at Estaque', 'artist': 'Georges Braque', 'year': '1908', 'museum': 'Privécollectie', 'techniek': 'Olieverf op doek'},
    {'file': 'gris_picasso.jpg', 'title': 'Portrait of Pablo Picasso', 'artist': 'Juan Gris', 'year': '1912', 'museum': 'Art Institute of Chicago', 'techniek': 'Olieverf op doek'},
    {'file': 'braque_tasse.jpg', 'title': 'La Tasse (The Cup)', 'artist': 'Georges Braque', 'year': '1912', 'museum': 'Auckland Art Gallery', 'techniek': 'Olieverf op doek'},
    {'file': 'braque_still_life_1926.jpg', 'title': 'Still Life', 'artist': 'Georges Braque', 'year': '1926', 'museum': 'Kulenovic Collection, Zweden', 'techniek': 'Olieverf op doek'},
    {'file': 'leger_esquisse.jpg', 'title': 'Esquisse pour "La Ville"', 'artist': 'Fernand Léger', 'year': '1919', 'museum': 'Musée National d\'Art Moderne', 'techniek': 'Olieverf op doek'},
    {'file': 'leger_disque.jpg', 'title': 'Un disque dans la ville', 'artist': 'Fernand Léger', 'year': '1920', 'museum': 'Centre Pompidou, Parijs', 'techniek': 'Olieverf op doek'},
    {'file': 'leger_nature_morte.jpg', 'title': 'Nature morte', 'artist': 'Fernand Léger', 'year': '1919', 'museum': 'Privécollectie', 'techniek': 'Olieverf op doek'},
    {'file': 'picasso_three_musicians.jpg', 'title': 'Three Musicians', 'artist': 'Pablo Picasso', 'year': '1921', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
]

print("="*60)
print("GENERATING HTML PAGES WITH INLINE IMAGES")
print("="*60)

# Generate pages with featured artwork and inline images
generate_page_with_inline_images(
    'romanticisme_volledig.md', 
    'Romanticisme', 
    '1780-1850', 
    ROMANTICISME_ARTWORKS,
    ROMANTICISME_ARTWORKS[0]  # Liberty Leading the People as featured
)

generate_page_with_inline_images(
    'expressionisme_nieuw.md', 
    'Expressionisme', 
    '1905-1930', 
    EXPRESSIONISME_ARTWORKS,
    EXPRESSIONISME_ARTWORKS[0]  # The Scream as featured
)

generate_page_with_inline_images(
    'kubisme_nieuw.md', 
    'Kubisme', 
    '1907-1914', 
    KUBISME_ARTWORKS,
    KUBISME_ARTWORKS[0]  # Les Demoiselles as featured
)

print("\n" + "="*60)
print("ALL PAGES GENERATED WITH INLINE IMAGES!")
print("="*60)
