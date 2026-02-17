#!/usr/bin/env python3
"""
Fix timeline-box headings to white on all art movement pages.
"""

import os
import glob

# CSS rule to add
HEADING_STYLE = "        .timeline-box h2, .timeline-box h3, .timeline-box h4, .timeline-box h5 {color:white !important}"

def fix_page(filepath):
    """Fix a page's timeline-box headings to have white color"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if page has timeline-box
    if '<div class="timeline-box"' not in content:
        # Page doesn't have timeline-box at all - skip
        return False, "No timeline-box found"
    
    # Check if heading style already exists
    if '.timeline-box h2' in content or '.timeline-box h3, .timeline-box h4, .timeline-box h5' in content:
        # Already has styling - skip
        return False, "Already has white h3"
    
    # Find all timeline-box occurrences and add heading style before each one
    import re
    pattern = r'<div class="timeline-box"[^>]*?\s*(?:?![^>]*)'
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        return False, "No timeline-box divs found"
    
    # Add the heading style before each timeline-box div
    for i, match in enumerate(matches):
        # Insert the CSS rule before the timeline-box div
        fixed_content = content[:match.start()] + HEADING_STYLE + '\n            <div class="' + match.group(0) + '>'
        
        # Insert it before the h3 heading inside the div
        h3_pattern = r'(<h3>📚 TIJDSGEEST CONTEXT[^<]*)'
        h3_match = re.search(h3_pattern, match.group(0))
        if h3_match:
            # Insert before the h3
            fixed_content = content[:h3_match.start()] + HEADING_STYLE + '\n' + h3_match.group(0) + '>\n            '
        
        # Apply the style directly to the h3 element itself
            h3_with_style = h3_match.group(0).replace('>', f' style="{HEADING_STYLE}">')
            fixed_content = fixed_content.replace(h3_match.group(0), h3_with_style)
        
        # Update the content
        content = fixed_content.replace(match.group(0), h3_with_style)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, f"Fixed {os.path.basename(filepath)}"

def main():
    html_files = sorted(glob.glob('*.html'))
    
    fixed = []
    skipped = []
    
    for filepath in html_files:
        if filepath == 'index.html':
            continue
        
        was_fixed, msg = fix_page(filepath)
        
        if was_fixed:
            fixed.append(filepath)
            print(f"✅ {filepath}")
        else:
            skipped.append((filepath, msg))
            if "No timeline-box" not in msg:
                print(f"⏭️ {filepath}: {msg}")
            print()
    
    print(f"\n{'='*50}")
    print(f"Fixed: {len(fixed)} pages")
    print(f"\nSkipped: {len(skipped)} pages")
    for f in fixed:
        print(f"   ✅ {f}")
    for s in skipped:
        print(f"   ⏭️ {s[0]}: {s[1]}")

if __name__ == '__main__':
    main()
