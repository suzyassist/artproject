#!/usr/bin/env python3
"""
Fix minimalisme.html and postmodernisme.html to match Gotisch structure
"""
import re

def fix_page(filepath):
    """Fix a page to have Gotisch timeline structure"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if page has TIJDSGEEST content section
    if 'TIJDSGEEST CONTEXT' not in content:
        # This page doesn't have a proper timeline section
        # We need to add one
        # Find the end of first artwork section and insert before it
        art_section_match = re.search(r'<div class="artwork-fullwidth">.*?</div>', content, re.DOTALL)
        
        if art_section_match:
            # Insert Gotisch-style timeline section before artwork
            timeline_section = f'''
        <section class="content-section">
            <h2>📚 TIJDSGEEST CONTEXT (1960-1975)</h2>
            
            <div class="timeline-box">
                <h3>🌍 POLITIEK PERSPECTIEF</h3>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    <li><strong>Vietnamoorlog:</strong> Sociale protesten maken emotionele kunst politiek beladen</li>
                    <li><strong>Space Age:</strong> NASA's cleanroom design, functioneel en gestroomlijnd</li>
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
                    <li><strong>Het object als object:</strong> Geen metafoor, geen symboliek, alleen materiële aanwezigheid</li>
                    <li><strong>Merleau-Ponty:</strong> Lichaamsfenomenologie - ervaring als fundamenteel</li>
                    <li><strong>Wittgenstein:</strong> Terug naar het letterlijke, het zichtbare</li>
                </ul>
            </div>
        </section>
{artwork_fullwidth}
'''
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Converted to Gotisch structure"

def main():
    pages = ['minimalisme.html', 'postmodernisme.html']
    
    for page in pages:
        print(f"Fixing {page}...")
        was_fixed, msg = fix_page(page)
        
        if was_fixed:
            print(f"✅ {page} - {msg}")
        else:
            print(f"⏭️ {page} - {msg}")

if __name__ == '__main__':
    main()
