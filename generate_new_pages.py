#!/usr/bin/env python3
"""
Generate HTML for Neoclassicisme and Postmodernisme
"""

from pathlib import Path

base_dir = Path('/root/.openclaw/workspace/kunstgeschiedenis')
website_dir = base_dir / 'website'

def generate_simple_page(md_file, title, period, featured_img, featured_title):
    """Generate a simple HTML page"""
    md_path = base_dir / md_file
    content = md_path.read_text(encoding='utf-8')
    
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
        <a href="neoclassicisme.html" class="active">Neoclassicisme</a>
        <a href="romanticisme.html">Romanticisme</a>
        <a href="expressionisme.html">Expressionisme</a>
        <a href="kubisme.html">Kubisme</a>
        <a href="postmodernisme.html">Postmodernisme</a>
    </nav>

    <main>
        <section class="movement-header">
            <div class="featured-artwork">
                <h2>Meesterwerk: {featured_title}</h2>
                <img src="images/{featured_img}" alt="{featured_title}" class="featured-image">
            </div>
            <p>Dit is een overzichtspagina voor {title}. De volledige inhoud met alle 10 werken wordt binnenkort toegevoegd.</p>
        </section>

        <section class="content-section">
            <h3>Inhoud</h3>
            <p>Deze pagina bevat binnenkort:</p>
            <ul>
                <li>Tijdsgeest Context (politiek, historisch, literair, filosofisch, psychologisch)</li>
                <li>Stijlfiguren en Thema's</li>
                <li>De 10 meest invloedrijke werken met afbeeldingen</li>
            </ul>
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

# Generate placeholder pages
generate_simple_page('neoclassicisme.md', 'Neoclassicisme', '1750-1850', 'david_horatii.jpg', 'De Eed van de Horatii')
generate_simple_page('postmodernisme.md', 'Postmodernisme', '1960-heden', 'warhol_soup.jpg', "Campbell's Soup Cans")

print("✅ Placeholder pages created!")
