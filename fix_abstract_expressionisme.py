#!/usr/bin/env python3
"""
Fix abstract_expressionisme.html naar timeline-box structuur
"""

import re

# Template header met sidebar en timeline-box CSS
TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abstract Expressionisme - Kunstgeschiedenis</title>
    <link rel="stylesheet" href="style.css">
    <style>
        .featured-artwork {background:linear-gradient(135deg,#8B0000 0%,#DC143C 50%,#FF6347 100%);padding:2rem;margin-bottom:2rem;border-radius:8px;text-align:center}
        .featured-artwork img {width:100%;max-width:800px;height:auto;border-radius:4px;margin-top:1rem}
        .artwork-fullwidth {background:#fff;margin:3rem 0;padding:2rem;border-radius:8px;box-shadow:0 2px 15px rgba(0,0,0,0.1)}
        .artwork-header {border-bottom:3px solid #8B0000;margin-bottom:1.5rem;padding-bottom:1rem}
        .style-analysis-box {background:#f9f9f9;border-left:4px solid #8B0000;padding:1rem;margin:1rem 0}
        .style-grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin:1rem 0}
        .style-item {background:#fff5f5;padding:1rem;border-radius:4px}
        .timeline-box {background:linear-gradient(135deg,#2c1810 0%,#1a0f08 100%);color:white;padding:1.5rem;margin:1rem 0;border-radius:8px}
        .timeline-box h2, .timeline-box h3, .timeline-box h4, .timeline-box h5 {color:white !important}
    </style>
</head>
<body>
    <header><h1>🔥 Abstract Expressionisme</h1><p class="subtitle">1940-1950 · Angst en Vrijheid</p></header>
    <nav class="top-nav">
        <a href="romanticisme.html" class="nav-prev">← 🌊 Romantiek</a>
        <a href="index.html" class="nav-home">🏠 Home</a>
        <a href="kubisme.html" class="nav-next">Kubisme 🔲 →</a>
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
            <a href="kubisme.html" class="side-nav-link"><span class="nav-icon">🔲</span><span class="nav-text">Kubisme</span></a>
            <a href="futurisme.html" class="side-nav-link"><span class="nav-icon">⚡</span><span class="nav-text">Futurisme</span></a>
            <a href="dadaisme.html" class="side-nav-link"><span class="nav-icon">🎲</span><span class="nav-text">Dadaïsme</span></a>
            <a href="destijl.html" class="side-nav-link"><span class="nav-icon">⬜</span><span class="nav-text">De Stijl</span></a>
            <a href="surrealisme.html" class="side-nav-link"><span class="nav-icon">🦋</span><span class="nav-text">Surrealisme</span></a>
            <a href="abstract.html" class="side-nav-link active"><span class="nav-icon">🔥</span><span class="nav-text">Abstract Expressionisme</span></a>
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
        document.getElementById('menu-btn').addEventListener('click', function() {
            document.getElementById('sidebar').classList.add('open');
            document.getElementById('overlay').classList.add('show');
            document.body.style.overflow = 'hidden';
        });
        document.getElementById('close-btn').addEventListener('click', function() {
            document.getElementById('sidebar').classList.remove('open');
            document.getElementById('overlay').classList.remove('show');
            document.body.style.overflow = '';
        });
        document.getElementById('overlay').addEventListener('click', function() {
            document.getElementById('sidebar').classList.remove('open');
            document.getElementById('overlay').classList.remove('show');
            document.body.style.overflow = '';
        });
    </script>

    <main>
        <section class="movement-header">
            <div class="featured-artwork">
                <h2>🏆 Meesterwerk: Men in the City</h2>
                <p>Willem de Kooning, 1949</p>
                <img src="images/abstract/kooning_man_in_city.jpg" alt="Willem de Kooning - Men in the City" style="width:100%;max-width:800px;height:auto;border-radius:4px;margin-top:1rem;box-shadow:0 4px 15px rgba(0,0,0,0.3);">
            </div>
        </section>

        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1940-1950)</h2>"""

# Timeline-box template
TIMELINE_BOX = """            <div class="timeline-box">
                <h3>{emoji} {heading}</h3>
                <div style="margin:1rem 0;line-height:1.7">
{content}
                </div>
            </div>"""

# De content lezen
with open('abstract_expressionisme.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Zoek de Politieke Context section (de eerste h2)
pattern = r'<h2>📚 TIJDSGEEST CONTEXT.*?</h2>'
match = re.search(pattern, content, re.DOTALL)

if match:
    start = match.end()

    # Zoek de eerste section met .political-section of .style-element
    # of de Stijlfiguren sectie
    next_section = re.search(r'<section class="[^"]*"[^"]*">\s*<h2>', content[start:])
    stijl_section = re.search(r'<h3>Stijlfiguren', content[start:])

    if next_section:
        end = start + next_section.start()
    elif stijl_section:
        end = start + stijl_section.start()
    else:
        end = len(content)

    context_section = content[start:end]
    print(f"Gevonden TIJDSGEEST CONTEXT sectie: {len(context_section)} tekens")

    # Parse de secties
    sections = []
    current_section = None
    current_content = []

    for line in context_section.split('\n'):
        if '<h2>' in line or '<h3>' in line:
            if current_section:
                sections.append({
                    'heading': current_section,
                    'content': '\n'.join(current_content)
                })
            if '<h2>🌍 POLITIEKE CONTEXT' in line:
                current_section = 'Politieke Context'
            elif '<h3>Stijlfiguren' in line:
                sections.append({
                    'heading': current_section,
                    'content': '\n'.join(current_content)
                })
                current_section = None
                current_content = []
            elif current_section:
                current_content.append(line)
        elif current_section:
            current_content.append(line)

    if current_section:
        sections.append({
            'heading': current_section,
            'content': '\n'.join(current_content)
        })

    print(f"Vond {len(sections)} secties")

    # Bouw nieuwe content
    new_content = TEMPLATE

    # Politieke Context
    politiiek_match = next((s for s in sections if s['heading'] == 'Politieke Context'), None)
    if politiiek_match:
        new_content += TIMELINE_BOX.format(
            emoji='🌍',
            heading='POLITIEK PERSPECTIEF',
            content=politiiek_match['content']
        )

    # De Stijlfiguren sectie (zoals in origineel)
    stijl_match = re.search(r'<h3>Stijlfiguren.*?</h3>', content, re.DOTALL)
    if stijl_match:
        new_content += '\n' + stijl_match.group(0)

    # Nu de kunstwerken sectie toevoegen (alles na Stijlfiguren)
    kunstwerk_match = re.search(r'<h3>De Tien Meest Invloedrijke Werken</h3>.*$', content, re.DOTALL)
    if kunstwerk_match:
        new_content += '\n' + kunstwerk_match.group(0)

    # Close content-section
    new_content += '\n        </section>\n\n    </main>\n\n    <footer>\n        <p>&copy; 2026 Kunstgeschiedenis - Matthias R</p>\n    </footer>\n\n</body>\n</html>'

    # Schrijf naar nieuw bestand
    with open('abstract_expressionismus_fixed.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✓ abstract_expressionismus_fixed.html aangemaakt")

    # Vervang origineel
    import shutil
    shutil.copy('abstract_expressionismus_fixed.html', 'abstract_expressionisme.html')
    print("✓ abstract_expressionisme.html geüpdatet")

    # Commit
    import subprocess
    subprocess.run(['git', 'add', 'abstract_expressionisme.html'], cwd='..')
    subprocess.run(['git', 'commit', '-m', 'fix: abstract_expressionisme.html naar timeline-box structuur'], cwd='..')
    print("✓ Git commit gedaan")

else:
    print("❌ TIJDSGEEST CONTEXT sectie niet gevonden")
