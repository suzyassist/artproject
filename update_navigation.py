#!/usr/bin/env python3
"""Update navigation on all art history pages"""

import os
import re
from pathlib import Path

# Define all movements in order with icons
MOVEMENTS = [
    ("index.html", "🏠", "Home"),
    ("byzantijns.html", "☦️", "Byzantijnse Kunst"),
    ("romaans.html", "🏰", "Romaanse Kunst"),
    ("gotisch.html", "⛪", "Gotische Kunst"),
    ("renaissance.html", "🏛️", "Renaissance"),
    ("manierisme.html", "🎭", "Maniërisme"),
    ("barok.html", "🎪", "Barok"),
    ("rococo.html", "🎀", "Rococo"),
    ("neoclassicisme.html", "⚱️", "Neoclassicisme"),
    ("romanticisme.html", "🌊", "Romantiek"),
    ("realisme.html", "🌾", "Realisme"),
    ("impressionisme.html", "☀️", "Impressionisme"),
    ("postimpressionisme.html", "🌻", "Post-Impressionisme"),
    ("symbolisme.html", "🌙", "Symbolisme"),
    ("artnouveau.html", "🌿", "Art Nouveau"),
    ("fauvisme.html", "🦁", "Fauvisme"),
    ("expressionisme.html", "😱", "Expressionisme"),
    ("kubisme.html", "🔲", "Kubisme"),
    ("futurisme.html", "⚡", "Futurisme"),
    ("dadaisme.html", "🎲", "Dadaïsme"),
    ("destijl.html", "⬜", "De Stijl"),
    ("surrealisme.html", "🦋", "Surrealisme"),
    ("abstract.html", "🔥", "Abstract Expressionisme"),
    ("popart.html", "🍿", "Pop Art"),
    ("minimalisme.html", "⬛", "Minimalisme"),
    ("conceptueel.html", "💡", "Conceptuele Kunst"),
    ("postmodernisme.html", "🌀", "Postmodernisme"),
    ("hedendaags.html", "🌐", "Hedendaagse Kunst"),
    ("digitaal.html", "💻", "Digitale Kunst"),
]

def get_prev_next(current_file):
    """Get previous and next movement"""
    for i, (file, icon, name) in enumerate(MOVEMENTS):
        if file == current_file:
            prev = MOVEMENTS[i-1] if i > 0 else None
            next = MOVEMENTS[i+1] if i < len(MOVEMENTS)-1 else None
            return prev, next
    return None, None

def generate_side_nav(current_file):
    """Generate side navigation HTML"""
    lines = ['<div class="side-nav-content">']
    for file, icon, name in MOVEMENTS:
        active = ' active' if file == current_file else ''
        lines.append(f'            <a href="{file}" class="side-nav-link{active}"><span class="nav-icon">{icon}</span><span class="nav-text">{name}</span></a>')
    lines.append('        </div>')
    return '\n'.join(lines)

def generate_bottom_nav(current_file):
    """Generate bottom navigation HTML"""
    prev, next = get_prev_next(current_file)
    lines = ['<nav class="bottom-nav">']
    
    if prev and prev[0] != "index.html":
        lines.append(f'    <a href="{prev[0]}" class="nav-prev">← {prev[1]} {prev[2]}</a>')
    else:
        lines.append('    <span></span>')
    
    lines.append('    <a href="index.html" class="nav-home">🏠 Home</a>')
    
    if next:
        lines.append(f'    <a href="{next[0]}" class="nav-next">{next[1]} {next[2]} →</a>')
    else:
        lines.append('    <span></span>')
    
    lines.append('</nav>')
    return '\n'.join(lines)

def update_page(filepath, current_file):
    """Update a single HTML page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update side-nav-content
    pattern = r'<div class="side-nav-content">.*?</div>\s*</nav>'
    new_nav = generate_side_nav(current_file) + '\n    </nav>'
    content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
    
    # Check if bottom-nav exists
    has_bottom_nav = 'class="bottom-nav"' in content
    
    if not has_bottom_nav:
        # Add bottom-nav before footer
        bottom_nav = generate_bottom_nav(current_file)
        
        # Find footer and insert before it
        if '</footer>' in content:
            # Insert before the closing </footer>
            content = content.replace('</footer>', f'\n    {bottom_nav}\n\n    </footer>')
        elif '<footer>' in content:
            # Insert after footer opening
            content = content.replace('<footer>', f'<footer>\n    {bottom_nav}\n\n')
    
    # Ensure bottom-nav is inside footer, not after
    # Move bottom-nav inside footer if it's outside
    if '</footer>' in content and 'bottom-nav' in content:
        # Check if bottom-nav is after </footer>
        if re.search(r'</footer>\s*<nav class="bottom-nav">', content):
            # Move it inside
            content = re.sub(
                r'</footer>\s*(<nav class="bottom-nav">.*?</nav>)',
                r'\1\n\n    </footer>',
                content,
                flags=re.DOTALL
            )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    website_dir = Path(__file__).parent
    
    updated = []
    for file, icon, name in MOVEMENTS:
        filepath = website_dir / file
        if filepath.exists():
            if update_page(filepath, file):
                updated.append(file)
                print(f"✓ Updated {file}")
        else:
            print(f"✗ Missing {file}")
    
    print(f"\n✅ Updated {len(updated)} pages")

if __name__ == "__main__":
    main()
