#!/usr/bin/env python3
"""
Generate HTML pages for the art history website from markdown files
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
    
    # Convert paragraphs (lines that aren't tags)
    paragraphs = []
    for line in text.split('\n'):
        line = line.strip()
        if line and not line.startswith('<') and not line.startswith('**'):
            paragraphs.append(f'<p>{line}</p>')
        else:
            paragraphs.append(line)
    
    return '\n'.join(paragraphs)

def generate_page(md_file, title, period, artworks_map):
    """Generate a complete HTML page from markdown"""
    md_path = base_dir / md_file
    if not md_path.exists():
        print(f"❌ File not found: {md_path}")
        return False
    
    content = md_path.read_text(encoding='utf-8')
    
    # Split into sections
    sections = content.split('\n## ')
    
    # First section is the intro/header
    header_html = md_to_html(sections[0])
    
    # Build sections HTML
    sections_html = []
    for section in sections[1:]:
        if not section.strip():
            continue
        section_html = md_to_html('## ' + section)
        sections_html.append(f'<section class="content-section">\n{section_html}\n</section>')
    
    # Generate artwork sections with images
    artworks_html = []
    for key, artwork in artworks_map.items():
        img_path = img_dir / artwork['file']
        if img_path.exists():
            img_tag = f'<img src="images/{artwork["file"]}" alt="{artwork["title"]}" class="artwork-image">'
        else:
            img_tag = '<p class="artwork-meta">[Afbeelding niet beschikbaar]</p>'
        
        artwork_html = f'''
<div class="artwork">
    <h4>{artwork['title']} ({artwork['year']}) — {artwork['artist']}</h4>
    <p class="artwork-meta">Museum: {artwork.get('museum', 'N/A')} | Techniek: {artwork.get('techniek', 'Olieverf op doek')}</p>
    {img_tag}
</div>
'''
        artworks_html.append(artwork_html)
    
    # Build full HTML
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
        <a href="romanticisme.html">Romanticisme</a>
        <a href="expressionisme.html"{' class="active"' if 'expressionisme' in md_file else ''}>Expressionisme</a>
        <a href="kubisme.html"{' class="active"' if 'kubisme' in md_file else ''}>Kubisme</a>
        <a href="modernisme.html"{' class="active"' if 'modernisme' in md_file else ''}>Modernisme</a>
    </nav>

    <main>
        <section class="movement-header">
            {header_html}
        </section>

        {''.join(sections_html[:3])}  <!-- Context, Stijlfiguren, Thema's -->

        <section class="content-section">
            <h3>De Tien Meest Invloedrijke Werken</h3>
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
    output_file = website_dir / md_file.replace('_nieuw.md', '.html').replace('_volledig.md', '.html')
    output_file.write_text(html, encoding='utf-8')
    print(f"✅ Generated: {output_file.name}")
    return True

# Artwork data
ROMANTICISME_ARTWORKS = {
    'medusa': {'file': 'medusa.jpg', 'title': 'Het Vlot van de Medusa', 'artist': 'Théodore Géricault', 'year': '1818-1819', 'museum': 'Musée du Louvre, Parijs', 'techniek': 'Olieverf op doek'},
    'liberty': {'file': 'liberty.jpg', 'title': 'De Vrijheid leidt het Volk', 'artist': 'Eugène Delacroix', 'year': '1830', 'museum': 'Musée du Louvre, Parijs', 'techniek': 'Olieverf op doek'},
    'wanderer': {'file': 'wanderer.jpg', 'title': 'Wanderer above the Sea of Fog', 'artist': 'Caspar David Friedrich', 'year': '1818', 'museum': 'Kunsthalle Hamburg', 'techniek': 'Olieverf op doek'},
    'eismeer': {'file': 'eismeer.jpg', 'title': 'Het Zee van Ijs (Das Eismeer)', 'artist': 'Caspar David Friedrich', 'year': '1823-1824', 'museum': 'Hamburger Kunsthalle', 'techniek': 'Olieverf op doek'},
    'saturn': {'file': 'saturn.jpg', 'title': 'Saturnus verslindt zijn Zoon', 'artist': 'Francisco de Goya', 'year': '1819-1823', 'museum': 'Museo del Prado, Madrid', 'techniek': 'Olieverf op doek'},
    'tres_mayo': {'file': 'tres_mayo.jpg', 'title': 'De Derde Mei 1808', 'artist': 'Francisco de Goya', 'year': '1814', 'museum': 'Museo del Prado, Madrid', 'techniek': 'Olieverf op doek'},
    'turner_rain': {'file': 'turner_rain.jpg', 'title': 'Regen, Stoom en Snelheid', 'artist': 'J.M.W. Turner', 'year': '1844', 'museum': 'National Gallery, Londen', 'techniek': 'Olieverf op doek'},
    'friedrich_moon': {'file': 'friedrich_moon.jpg', 'title': 'Twee Mannen beschouwen de Maan', 'artist': 'Caspar David Friedrich', 'year': '1819-1820', 'museum': 'Alte Nationalgalerie, Berlijn', 'techniek': 'Olieverf op doek'},
    'turner_venice': {'file': 'turner_venice.jpg', 'title': 'De Brug der Zuchten', 'artist': 'J.M.W. Turner', 'year': '1840', 'museum': 'Tate Britain, Londen', 'techniek': 'Olieverf op doek'},
}

EXPRESSIONISME_ARTWORKS = {
    'munch': {'file': 'munch_schreeuw.jpg', 'title': 'De Schreeuw', 'artist': 'Edvard Munch', 'year': '1893', 'museum': 'National Gallery of Norway, Oslo', 'techniek': 'Olieverf, tempera en pastel op karton'},
    'kirchner_berlijn': {'file': 'kirchner_berlijn.jpg', 'title': 'Straat, Berlijn', 'artist': 'Ernst Ludwig Kirchner', 'year': '1913', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
    'kandinsky': {'file': 'kandinsky_compositie.jpg', 'title': 'Compositie VII', 'artist': 'Wassily Kandinsky', 'year': '1913', 'museum': 'Tretyakov Gallery, Moskou', 'techniek': 'Olieverf op doek'},
    'marc_blauw': {'file': 'marc_blauwe_paarden.jpg', 'title': 'De Toren van Blauwe Paarden', 'artist': 'Franz Marc', 'year': '1913', 'museum': 'Lenbachhaus, München', 'techniek': 'Olieverf op doek'},
    'marc_koe': {'file': 'marc_gele_koe.jpg', 'title': 'Gele Koe', 'artist': 'Franz Marc', 'year': '1911', 'museum': 'Guggenheim, New York', 'techniek': 'Olieverf op doek'},
    'kirchner_dance': {'file': 'kirchner_dance_hall.jpg', 'title': 'Dance Hall Bellevue', 'artist': 'Ernst Ludwig Kirchner', 'year': '1909-1910', 'museum': 'National Gallery of Art, Washington', 'techniek': 'Olieverf op doek'},
    'kirchner_soldaat': {'file': 'kirchner_soldaat.jpg', 'title': 'Zelfportret als Soldaat', 'artist': 'Ernst Ludwig Kirchner', 'year': '1915', 'museum': 'Allen Memorial Art Museum, Oberlin', 'techniek': 'Olieverf op doek'},
    'beckmann': {'file': 'beckmann_nacht.jpg', 'title': 'De Nacht', 'artist': 'Max Beckmann', 'year': '1918-1919', 'museum': 'Kunstsammlung NRW, Düsseldorf', 'techniek': 'Olieverf op doek'},
    'matisse_hoed': {'file': 'matisse_hoed.jpg', 'title': 'Vrouw met een Hoed', 'artist': 'Henri Matisse', 'year': '1905', 'museum': 'SFMOMA', 'techniek': 'Olieverf op doek'},
    'matisse_atelier': {'file': 'matisse_rode_atelier.jpg', 'title': 'Het Rode Atelier', 'artist': 'Henri Matisse', 'year': '1911', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
}

KUBISME_ARTWORKS = {
    'picasso_demoiselles': {'file': 'picasso_demoiselles.jpg', 'title': "Les Demoiselles d'Avignon", 'artist': 'Pablo Picasso', 'year': '1907', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
    'braque_trees': {'file': 'braque_trees_estaque.jpg', 'title': 'Trees at Estaque', 'artist': 'Georges Braque', 'year': '1908', 'museum': 'Privécollectie', 'techniek': 'Olieverf op doek'},
    'picasso_kahnweiler': {'file': 'picasso_kahnweiler.jpg', 'title': 'Portrait of Daniel-Henry Kahnweiler', 'artist': 'Pablo Picasso', 'year': '1910', 'museum': 'Art Institute of Chicago', 'techniek': 'Olieverf op doek'},
    'braque_still_life': {'file': 'braque_still_life_1926.jpg', 'title': 'Still Life', 'artist': 'Georges Braque', 'year': '1926', 'museum': 'Kulenovic Collection, Zweden', 'techniek': 'Olieverf op doek'},
    'braque_tasse': {'file': 'braque_tasse.jpg', 'title': 'La Tasse (The Cup)', 'artist': 'Georges Braque', 'year': '1912', 'museum': 'Auckland Art Gallery', 'techniek': 'Olieverf op doek'},
    'leger_disque': {'file': 'leger_disque.jpg', 'title': 'Un disque dans la ville', 'artist': 'Fernand Léger', 'year': '1920', 'museum': 'Centre Pompidou, Parijs', 'techniek': 'Olieverf op doek'},
    'leger_nature': {'file': 'leger_nature_morte.jpg', 'title': 'Nature morte', 'artist': 'Fernand Léger', 'year': '1919', 'museum': 'Privécollectie', 'techniek': 'Olieverf op doek'},
    'gris_picasso': {'file': 'gris_picasso.jpg', 'title': 'Portrait of Pablo Picasso', 'artist': 'Juan Gris', 'year': '1912', 'museum': 'Art Institute of Chicago', 'techniek': 'Olieverf op doek'},
    'leger_esquisse': {'file': 'leger_esquisse.jpg', 'title': 'Esquisse pour "La Ville"', 'artist': 'Fernand Léger', 'year': '1919', 'museum': 'Musée National d\'Art Moderne', 'techniek': 'Olieverf op doek'},
    'picasso_three_musicians': {'file': 'picasso_three_musicians.jpg', 'title': 'Three Musicians', 'artist': 'Pablo Picasso', 'year': '1921', 'museum': 'MoMA, New York', 'techniek': 'Olieverf op doek'},
}

print("="*60)
print("GENERATING HTML PAGES")
print("="*60)

# Generate pages
generate_page('romanticisme_volledig.md', 'Romanticisme', '1780-1850', ROMANTICISME_ARTWORKS)
generate_page('expressionisme_nieuw.md', 'Expressionisme', '1905-1930', EXPRESSIONISME_ARTWORKS)
generate_page('kubisme_nieuw.md', 'Kubisme', '1907-1914', KUBISME_ARTWORKS)

print("\n" + "="*60)
print("ALL PAGES GENERATED!")
print("="*60)
