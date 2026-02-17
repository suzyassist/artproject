#!/usr/bin/env python3
"""
Fix minimalisme.html and postmodernisme.html to have Gotisch TIJDSGEEST structure.
"""

import re

# Minimalisme content extracted from the page
MINIMALISME_SECTION = '''
        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1960-1975)</h2>
            
            <div class="timeline-box">
                <h3>🌍 POLITIEK PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Vietnamoorlog:</strong> Sociale protesten maken emotionele kunst politiek beladen</li>
                    <li><strong>Space Age:</strong> NASA's cleanroom design - functioneel en gestroomlijnd</li>
                    <li><strong>Koude Oorlog:</strong> Weigering van ideologisch narratief in kunst</li>
                    <li><strong>Democratisering:</strong> Geen ingewikkelde interpretatie nodig - kunst voor iedereen</li>
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
                    <li><strong>Reactie tegen Abstract Expressionisme:</strong> Behoefte aan orde en kalmte na emotionele overbelasting</li>
                    <li><strong>Mechanische perfectie:</strong> Troost in een tijd van sociale onrust</li>
                    <li><strong>Fenomenologische ervaring:</strong> Het lichaam in de ruimte, niet alleen het oog</li>
                    <li><strong>Behoefte aan helderheid:</strong> Tegen informatie-overload en propaganda</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>⚙️ HISTORISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Massaproductie:</strong> Objecten die identiek reproduceerbaar zijn</li>
                    <li><strong>Modulaire architectuur:</strong> Systeemdenken en standaardisatie</li>
                    <li><strong>Cybernetica:</strong> Objecten die resoneren met hun omgeving</li>
                    <li><strong>Digitale revolutie:</strong> Informatie als binaire, letterlijke code</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🎭 FILOSOFISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>"What you see is what you see":</strong> Het einde van diepere betekenis</li>
                    <li><strong>Het object als object:</strong> Geen metafoor, geen symboliek</li>
                    <li><strong>Merleau-Ponty:</strong> Lichaamsfenomenologie - ervaring als fundamenteel</li>
                    <li><strong>Wittgenstein:</strong> Terug naar het letterlijke, het zichtbare</li>
                </ul>
            </div>
        </section>'''

# Postmodernisme content 
POSTMODERNISME_SECTION = '''
        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1970-2000)</h2>
            
            <div class="timeline-box">
                <h3>🌍 POLITIEK PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Val van communisme (1989-1991):</strong> Einde van de Koude Oorlog</li>
                    <li><strong>Protestbewegingen:</strong> Vietnamoorlog, burgerrechten, studentenopstanden 1968</li>
                    <li><strong>Post-koloniale theorie:</strong> De grenzen van het Westen worden problematisch</li>
                    <li><strong>Globalisering:</strong> Economische ongelijkheid wordt versterkt</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>📖 LITERAIR PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Metafictie:</strong> Thomas Pynchon, Don DeLillo, Umberto Eco</li>
                    <li><strong>"Death of the author":</strong> Roland Barthes - geen enkele stabiele betekenis</li>
                    <li><strong>Deconstructie:</strong> Jacques Derrida - teksten zonder oorsprong</li>
                    <li><strong>Pastiche:</strong> Combineren van eerdere stijlen zonder ironische afstand</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>🧠 PSYCHOLOGISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Gefragmenteerd subject:</strong> Identiteit als performance</li>
                    <li><strong>Judith Butler:</strong> Gender Trouble - gender als constructie</li>
                    <li><strong>Hyperrealiteit:</strong> Baudrillard - simulatie realer dan origineel</li>
                    <li><strong>Keuzestress:</strong> Overvloed aan mogelijkheden, nostalgie naar authenticiteit</li>
                </ul>
            </div>

            <div class="timeline-box">
                <h3>⚙️ HISTORISCH PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Postindustriële samenleving:</strong> Informatie als hoofdbron van rijkdom</li>
                    <li><strong>Computerrevolutie:</strong> Internet transformeert menselijke ervaring</li>
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
                    <li><strong>Einde van "grote verhalen":</strong> Vooruitgang, emancipatie, universalisme afgewezen</li>
                </ul>
            </div>
        </section>'''

def fix_minimalisme():
    """Add TIJDSGEEST section to minimalisme.html."""
    with open('minimalisme.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has h2 TIJDSGEEST
    if '<h2>📚 TIJDSGEEST CONTEXT' in content:
        return False, "Already has correct structure"
    
    # Find the end of the style-grid section and add before closing </section>
    # Look for the last </div></section> before the artwork section
    pattern = r"(</div>\s*</div>\s*</section>)(\s*<section[^>]*>.*?TIEN MEESTERWERKEN)"
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(
            pattern,
            r"\1\n" + MINIMALISME_SECTION + r"\n\2",
            content,
            flags=re.DOTALL
        )
        with open('minimalisme.html', 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Added TIJDSGEEST section"
    
    return False, "Could not find insertion point"

def fix_postmodernisme():
    """Add TIJDSGEEST section to postmodernisme.html."""
    with open('postmodernisme.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has h2 TIJDSGEEST
    if '<h2>📚 TIJDSGEEST CONTEXT' in content:
        return False, "Already has correct structure"
    
    # Find insertion point - before artwork section or at end of main content
    pattern = r"(</section>\s*<section[^>]*class=\"content-section\"[^>]*>\s*<h2[^>]*>.*?TIEN MEESTERWERKEN|</main>)"
    
    if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
        content = re.sub(
            pattern,
            POSTMODERNISME_SECTION + r"\n\1",
            content,
            flags=re.DOTALL
        )
        with open('postmodernisme.html', 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Added TIJDSGEEST section"
    
    return False, "Could not find insertion point"

def main():
    print("=== Fixing minimalisme.html ===")
    ok, msg = fix_minimalisme()
    print(f"{'✅' if ok else '⏭️'} minimalisme.html: {msg}")
    
    print("\n=== Fixing postmodernisme.html ===")
    ok, msg = fix_postmodernisme()
    print(f"{'✅' if ok else '⏭️'} postmodernisme.html: {msg}")

if __name__ == '__main__':
    main()
