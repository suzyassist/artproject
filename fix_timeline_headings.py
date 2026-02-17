#!/usr/bin/env python3
"""
Fix timeline-box heading colors to white on all art movement pages.
"""

import glob
import re

# The CSS rule to add
HEADING_STYLE = ".timeline-box h2, .timeline-box h3, .timeline-box h4, .timeline-box h5 {color:white !important}"

def fix_page(filepath):
    """Add white color styling for timeline-box headings."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has the styling
    if re.search(r'\.timeline-box h[234].*color:\s*white', content):
        return False, "Already has white h3 styling"
    
    # Skip if no timeline-box
    if 'timeline-box' not in content:
        return False, "No timeline-box found"
    
    # Find the timeline-box CSS rule and add the heading style after it
    # Pattern: .timeline-box { ... }
    pattern = r'(\.timeline-box \{[^}]+\})'
    
    if re.search(pattern, content):
        # Add the heading style after the timeline-box rule
        new_content = re.sub(
            pattern,
            r'\1\n        ' + HEADING_STYLE,
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Added heading style"
    
    return False, "Could not find timeline-box CSS rule"

def main():
    html_files = sorted(glob.glob('*.html'))
    
    fixed = []
    skipped = []
    
    for filepath in html_files:
        if filepath == 'index.html':
            continue
        
        was_fixed, message = fix_page(filepath)
        
        if was_fixed:
            fixed.append(filepath)
            print(f"✅ {filepath}")
        else:
            skipped.append((filepath, message))
            if "Already" not in message:
                print(f"⏭️ {filepath}: {message}")
    
    print(f"\n{'='*50}")
    print(f"Fixed: {len(fixed)} pages")
    for f in fixed:
        print(f"  ✅ {f}")
    
    print(f"\nSkipped: {len(skipped)} pages")

if __name__ == '__main__':
    main()
