#!/usr/bin/env python3
"""
Convert minimalisme.html and postmodernisme.html to Gotisch structure.
"""

import re

# Gotisch-style timeline section for minimalisme
MINIMALISME_SECTION = '''
        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1960-1975)</h2>
            
            <div class="timeline-box">
                <h3>🌍 POLITIEK PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Vietnamoorlog:</strong> Sociale protesten maken emotionele kunst politiek beladen</li>
                    <li><strong>Space Age:</strong> NASA's cleanroom design - functioneel en gestroomlijnd</li>
                    <li><strong>Koude Oorlog:</strong> Weigering van ideologisch narratief in kunst</li>
                    <li><strong>Democratisering:</strong> Geen ingewikkelde interpretatie nodig</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>📖 LITERAIR PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Minimal poetry:</strong> Woorden als objecten, taal als materiaal</li>
                    <li><strong>Anti-narratief:</strong> Geen verhaal, geen betekenis achter de tekst</li>
                    <li><strong>Concrete poëzie:</strong> De vorm is de inhoud</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🧠 PSYCHOLOGISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Reactie tegen Abstract Expressionisme:</strong> Behoefte aan orde en kalmte</li>
                    <li><strong>Mechanische perfectie:</strong> Troost in een tijd van sociale onrust</li>
                    <li><strong>Fenomenologische ervaring:</strong> Het lichaam in de ruimte</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>⚙️ HISTORISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Massaproductie:</strong> Objecten die identiek reproduceerbaar zijn</li>
                    <li><strong>Modulaire architectuur:</strong> Systeemdenken en standaardisatie</li>
                    <li><strong>Digitale revolutie:</strong> Informatie als binaire code</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🎭 FILOSOFISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>"What you see is what you see":</strong> Het einde van diepere betekenis</li>
                    <li><strong>Het object als object:</strong> Geen metafoor, geen symboliek</li>
                    <li><strong>Wittgenstein:</strong> Terug naar het letterlijke, het zichtbare</li>
                </ul>
            </div>
        </section>
'''

# Gotisch-style timeline section for postmodernisme
POSTMODERNISME_SECTION = '''
        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1970-2000)</h2>
            
            <div class="timeline-box">
                <h3>🌍 POLITIEK PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Val van communisme (1989-1991):</strong> Einde van de Koude Oorlog</li>
                    <li><strong>Protestbewegingen:</strong> Vietnamoorlog, burgerrechten, studentenopstanden</li>
                    <li><strong>Post-koloniale theorie:</strong> Grenzen van het Westen worden problematisch</li>
                    <li><strong>Globalisering:</strong> Economische ongelijkheid wordt versterkt</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>📖 LITERAIR PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Metafictie:</strong> Thomas Pynchon, Don DeLillo, Umberto Eco</li>
                    <li><strong>"Death of the author":</strong> Roland Barthes - geen stabiele betekenis</li>
                    <li><strong>Deconstructie:</strong> Jacques Derrida - teksten zonder oorsprong</li>
                    <li><strong>Pastiche:</strong> Combineren van eerdere stijlen</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🧠 PSYCHOLOGISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Gefragmenteerd subject:</strong> Identiteit als performance</li>
                    <li><strong>Judith Butler:</strong> Gender Trouble - gender als constructie</li>
                    <li><strong>Hyperrealiteit:</strong> Baudrillard - simulatie realer dan origineel</li>
                    <li><strong>Keuzestress:</strong> Nostalgie naar verloren authenticiteit</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>⚙️ HISTORISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Postindustriële samenleving:</strong> Informatie als hoofdbron van rijkdom</li>
                    <li><strong>Computerrevolutie:</strong> Internet transformeert ervaring</li>
                    <li><strong>Ecologische crisis:</strong> Einde van modernistisch geloof in vooruitgang</li>
                    <li><strong>Sociale media:</strong> Het zelf in de digitale spiegelwereld</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🎭 FILOSOFISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Poststructuralisme:</strong> Foucault, Derrida, Deleuze, Baudrillard</li>
                    <li><strong>Discours en macht:</strong> Kennis is nooit neutraal</li>
                    <li><strong>Rizoom:</strong> Kennis als netwerk zonder hiërarchie</li>
                    <li><strong>Einde van "grote verhalen":</strong> Vooruitgang en universalisme afgewezen</li>
                </ul>
            </div>
        </section>
'''

# CSS to add for timeline-box styling
TIMELINE_CSS = '''
        .timeline-box {background:linear-gradient(135deg,#2c1810 0%,#1a0f08 100%);color:white;padding:1.5rem;margin:1rem 0;border-radius:8px}
        .timeline-box h2, .timeline-box h3, .timeline-box h4, .timeline-box h5 {color:white !important}
'''

def fix_minimalisme():
    """Fix minimalisme.html to Gotisch structure"""
    with open('minimalisme.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS if not present
    if '.timeline-box {' not in content:
        content = content.replace('</style>', TIMELINE_CSS + '</style>')
    
    # Remove old tijdsgeest-link sections
    content = re.sub(r"<div class='tijdsgeest-link'>.*?</div>", '', content, flags=re.DOTALL)
    
    # Remove old timeline-box with h4 (the old TIJDSGEEST section)
    content = re.sub(r"<div class='timeline-box'[^>]*>.*?<h4>🔗 TIJDSGEEST.*?</div>", '', content, flags=re.DOTALL)
    
    # Find where to insert the new section (before the first artwork-fullwidth)
    insert_pos = content.find('<div class="artwork-fullwidth">')
    if insert_pos > 0:
        content = content[:insert_pos] + MINIMALISME_SECTION + '\n' + content[insert_pos:]
    
    with open('minimalisme.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ minimalisme.html converted to Gotisch structure")

def fix_postmodernisme():
    """Fix postmodernisme.html to Gotisch structure"""
    with open('postmodernisme.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS if not present
    if '.timeline-box {' not in content:
        content = content.replace('</style>', TIMELINE_CSS + '</style>')
    
    # Remove old tijdsgeest-link sections
    content = re.sub(r'<div class="tijdsgeest-link">.*?</div>', '', content, flags=re.DOTALL)
    
    # Find where to insert the new section (before first artwork section or content-section)
    insert_pos = content.find('<section class="content-section">')
    if insert_pos > 0:
        # Insert before the first content-section
        content = content[:insert_pos] + POSTMODERNISME_SECTION + '\n        ' + content[insert_pos:]
    
    with open('postmodernisme.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ postmodernisme.html converted to Gotisch structure")

def main():
    print("Converting pages to Gotisch structure...\n")
    fix_minimalisme()
    fix_postmodernisme()
    print("\n✅ Done! Both pages now have Gotisch TIJDSGEEST structure")

if __name__ == '__main__':
    main()
