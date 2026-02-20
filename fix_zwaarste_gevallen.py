#!/usr/bin/env python3
"""
Fix kubisme.html en destijl.html met alle perspectief secties
"""

import json
import shutil

# Template met sidebar en timeline-box CSS
TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Kunstgeschiedenis</title>
    <link rel="stylesheet" href="style.css">
    <style>
        .featured-artwork {{background:linear-gradient(135deg,{gradient});padding:2rem;margin-bottom:2rem;border-radius:8px;text-align:center}}
        .featured-artwork img {{width:100%;max-width:800px;height:auto;border-radius:4px;margin-top:1rem}}
        .artwork-fullwidth {{background:#fff;margin:3rem 0;padding:2rem;border-radius:8px;box-shadow:0 2px 15px rgba(0,0,0,0.1)}}
        .artwork-header {{border-bottom:3px solid {color};margin-bottom:1.5rem;padding-bottom:1rem}}
        .style-analysis-box {{background:#f9f9f9;border-left:4px solid {color};padding:1rem;margin:1rem 0}}
        .style-grid {{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin:1rem 0}}
        .style-item {{background:{light_bg};padding:1rem;border-radius:4px}}
        .timeline-box {{background:linear-gradient(135deg,#2c1810 0%,#1a0f08 100%);color:white;padding:1.5rem;margin:1rem 0;border-radius:8px}}
        .timeline-box h2, .timeline-box h3, .timeline-box h4, .timeline-box h5 {{color:white !important}}
    </style>
</head>
<body>
    <header><h1>{emoji} {name}</h1><p class="subtitle">{period}</p></header>
    <nav class="top-nav">
        <a href="{prev_link}" class="nav-prev">← {prev_name}</a>
        <a href="index.html" class="nav-home">🏠 Home</a>
        <a href="{next_link}" class="nav-next">{next_name} →</a>
    </nav>
    <button id="menu-btn" class="menu-button" aria-label="Menu openen">☰</button>
    <nav id="sidebar" class="side-nav">
        <div class="side-nav-header"><h3>🎨 Kunststromingen</h3><button id="close-btn" class="close-button" aria-label="Menu sluiten">×</button></div>
        <div class="side-nav-content">
            <a href="index.html" class="side-nav-link"><span class="nav-icon">🏠</span><span class="nav-text">Home</span></a>
            <a href="byzantijns.html" class="side-nav-link"><span class="nav-icon">☦️</span><span class="nav-text">Byzantijnse Kunst</span></a>
            <a href="romaans.html" class="side-nav-link"><span class="nav-icon">🏰</span><span class="nav-text">Romaanse Kunst</span></a>
            <a href="gotisch.html" class="side-nav-link"><span class="nav-icon">⛪</span><span class="nav-text">Gotische Kunst</span></a>
            <a href="renaissance.html" class="side-nav-link"><span class="nav-icon">🏛️</span><span class="nav-text">Renaissance</span></a>
            <a href="manierisme.html" class="side-nav-link"><span class="nav-icon">🎭</span><span class="nav-text">Maniërisme</span></a>
            <a href="barok.html" class="side-nav-link"><span class="nav-icon">🎪</span><span class="nav-text">Barok</span></a>
            <a href="rococo.html" class="side-nav-link"><span class="nav-icon">🎀</span><span class="nav-text">Rococo</span></a>
            <a href="neoclassicisme.html" class="side-nav-link"><span class="nav-icon">⚱️</span><span class="nav-text">Neoclassicisme</span></a>
            <a href="romanticisme.html" class="side-nav-link"><span class="nav-icon">🌊</span><span class="nav-text">Romantiek</span></a>
            <a href="realisme.html" class="side-nav-link"><span class="nav-icon">🌾</span><span class="nav-text">Realisme</span></a>
            <a href="impressionisme.html" class="side-nav-link"><span class="nav-icon">☀️</span><span class="nav-text">Impressionisme</span></a>
            <a href="postimpressionisme.html" class="side-nav-link"><span class="nav-icon">🌻</span><span class="nav-text">Post-Impressionisme</span></a>
            <a href="symbolisme.html" class="side-nav-link"><span class="nav-icon">🌙</span><span class="nav-text">Symbolisme</span></a>
            <a href="artnouveau.html" class="side-nav-link"><span class="nav-icon">🌿</span><span class="nav-text">Art Nouveau</span></a>
            <a href="fauvisme.html" class="side-nav-link"><span class="nav-icon">🦁</span><span class="nav-text">Fauvisme</span></a>
            <a href="expressionisme.html" class="side-nav-link"><span class="nav-icon">😱</span><span class="nav-text">Expressionisme</span></a>
            <a href="{active_link}" class="side-nav-link active"><span class="nav-icon">{emoji}</span><span class="nav-text">{name}</span></a>
            <a href="futurisme.html" class="side-nav-link"><span class="nav-icon">⚡</span><span class="nav-text">Futurisme</span></a>
            <a href="dadaisme.html" class="side-nav-link"><span class="nav-icon">🎲</span><span class="nav-text">Dadaïsme</span></a>
            <a href="destijl.html" class="side-nav-link"><span class="nav-icon">⬜</span><span class="nav-text">De Stijl</span></a>
            <a href="surrealisme.html" class="side-nav-link"><span class="nav-icon">🦋</span><span class="nav-text">Surrealisme</span></a>
            <a href="abstract.html" class="side-nav-link"><span class="nav-icon">🔥</span><span class="nav-text">Abstract Expressionisme</span></a>
            <a href="popart.html" class="side-nav-link"><span class="nav-icon">🍿</span><span class="nav-text">Pop Art</span></a>
            <a href="minimalisme.html" class="side-nav-link"><span class="nav-icon">⬛</span><span class="nav-text">Minimalisme</span></a>
            <a href="conceptueel.html" class="side-nav-link"><span class="nav-icon">💡</span><span class="nav-text">Conceptuele Kunst</span></a>
            <a href="postmodernisme.html" class="side-nav-link"><span class="nav-icon">🌀</span><span class="nav-text">Postmodernisme</span></a>
            <a href="hedendaags.html" class="side-nav-link"><span class="nav-icon">🌐</span><span class="nav-text">Hedendaagse Kunst</span></a>
            <a href="digitaal.html" class="side-nav-link"><span class="nav-icon">💻</span><span class="nav-text">Digitale Kunst</span></a>
        </div>
    </nav>
    <div id="overlay" class="nav-overlay"></div>
    <script>
        document.getElementById('menu-btn').addEventListener('click', function() {{
            document.getElementById('sidebar').classList.add('open');
            document.getElementById('overlay').classList.add('show');
            document.body.style.overflow = 'hidden';
        }});
        document.getElementById('close-btn').addEventListener('click', function() {{
            document.getElementById('sidebar').classList.remove('open');
            document.getElementById('overlay').classList.remove('show');
            document.body.style.overflow = '';
        }});
        document.getElementById('overlay').addEventListener('click', function() {{
            document.getElementById('sidebar').classList.remove('open');
            document.getElementById('overlay').classList.remove('show');
            document.body.style.overflow = '';
        }});
    </script>

    <main>
        <section class="movement-header">
            <div class="featured-artwork">
                <h2>🏆 Meesterwerk: {featured_title}</h2>
                <p>{featured_artist}</p>
                <img src="{featured_image}" alt="{featured_alt}" style="width:100%;max-width:800px;height:auto;border-radius:4px;margin-top:1rem;box-shadow:0 4px 15px rgba(0,0,0,0.3);">
            </div>
        </section>

        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT ({years})</h2>"""

TIMELINE_BOX = """            <div class="timeline-box">
                <h3>{emoji} {heading}</h3>
                <div style="margin:1rem 0;line-height:1.7">
                    {content}
                </div>
            </div>"""

# Load extracted content
with open('extracted_content.json') as f:
    extracted = json.load(f)

# Load literary content
with open('literary_content.json') as f:
    literary = json.load(f)

# Merge content
all_content = {}
for mv in ['kubisme', 'de_stijl']:
    all_content[mv] = {
        'politiek': extracted[mv]['politiek'],
        'filosofisch': extracted[mv]['filosofisch'],
        'psychologisch': extracted[mv]['psychologisch'],
        'literair': literary[mv]
    }

# Config for each movement
config = {
    'kubisme': {
        'file': 'kubisme.html',
        'title': 'Kubisme',
        'name': 'Kubisme',
        'emoji': '🔲',
        'period': '1907-1914 · Fragmentatie en Meerdere Perspectieven',
        'years': '1907-1914',
        'gradient': '#4A4A4A 0%,#2C2C2C 100%',
        'color': '#4A4A4A',
        'light_bg': '#f0f0f0',
        'prev_link': 'expressionisme.html',
        'prev_name': 'Expressionisme 😱',
        'next_link': 'futurisme.html',
        'next_name': 'Futurisme ⚡',
        'active_link': 'kubisme.html',
        'featured_title': 'Les Demoiselles d\'Avignon',
        'featured_artist': 'Pablo Picasso, 1907',
        'featured_image': 'images/kubisme/picasso_demoiselles.jpg',
        'featured_alt': 'Pablo Picasso - Les Demoiselles d\'Avignon'
    },
    'de_stijl': {
        'file': 'destijl.html',
        'title': 'De Stijl',
        'name': 'De Stijl',
        'emoji': '⬜',
        'period': '1917-1931 · Pure Abstractie en Harmonie',
        'years': '1917-1931',
        'gradient': '#FFFFFF 0%,#F0F0F0 100%',
        'color': '#000000',
        'light_bg': '#f5f5f5',
        'prev_link': 'dadaisme.html',
        'prev_name': 'Dadaïsme 🎲',
        'next_link': 'surrealisme.html',
        'next_name': 'Surrealisme 🦋',
        'active_link': 'destijl.html',
        'featured_title': 'Compositie met Rood, Geel en Blauw',
        'featured_artist': 'Piet Mondrian, 1930',
        'featured_image': 'images/destijl/mondrian_compositie.jpg',
        'featured_alt': 'Piet Mondrian - Compositie met Rood, Geel en Blauw'
    }
}

# Process each movement
for mv_key, mv_config in config.items():
    print(f"\n=== Processing {mv_config['name']} ===")
    
    # Build new HTML
    html = TEMPLATE.format(**mv_config)
    
    # Add timeline boxes
    perspectives = [
        ('politiek', '🌍', 'POLITIEK PERSPECTIEF'),
        ('filosofisch', '💭', 'FILOSOFISCH PERSPECTIEF'),
        ('psychologisch', '🧠', 'PSYCHOLOGISCH PERSPECTIEF'),
        ('literair', '📖', 'LITERAIR PERSPECTIEF')
    ]
    
    for ptype, emoji, heading in perspectives:
        content = all_content[mv_key][ptype]
        if content:
            # Format content with proper paragraph tags
            paragraphs = content.split('\n\n')
            formatted = '\n                    '.join([f'<p>{p}</p>' for p in paragraphs if p.strip()])
            html += TIMELINE_BOX.format(emoji=emoji, heading=heading, content=formatted)
            print(f"  ✓ {ptype}: {len(content.split())} woorden")
        else:
            print(f"  ❌ {ptype}: NIET GEVONDEN")
    
    # Close content section and main
    html += """
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 Kunstgeschiedenis - Matthias R</p>
    </footer>
</body>
</html>"""
    
    # Backup original
    shutil.copy(mv_config['file'], f"{mv_config['file']}.backup")
    print(f"  ✓ Backup: {mv_config['file']}.backup")
    
    # Write new file
    with open(mv_config['file'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Written: {mv_config['file']}")
    
    # Check result
    with open(mv_config['file']) as f:
        new_content = f.read()
        boxes = new_content.count('timeline-box')
        print(f"  ✓ Timeline-boxes: {boxes}")

print("\n✅ Alle zwaarste gevallen gefixed!")
print("Run: git add -A && git commit -m 'fix: kubisme.html en destijl.html naar timeline-box structuur'")
