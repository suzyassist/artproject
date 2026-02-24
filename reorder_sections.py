#!/usr/bin/env python3
"""
Reorder HTML sections: move TIJDSGEEST CONTEXT after MEESTERWERKEN
Safe approach with backup and single-file testing
"""
import os
import glob
import shutil

def find_closing_tag(content, start_pos, open_tag='<section', close_tag='</section>'):
    """Find the matching closing tag by counting nesting"""
    depth = 1
    pos = start_pos
    open_len = len(open_tag)
    close_len = len(close_tag)
    
    while depth > 0:
        next_open = content.find(open_tag, pos)
        next_close = content.find(close_tag, pos)
        
        if next_close == -1:
            return -1
        
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + open_len
        else:
            depth -= 1
            if depth == 0:
                return next_close + close_len
            pos = next_close + close_len
    
    return -1

def extract_section(content, marker):
    """Extract a section containing the marker"""
    marker_pos = content.find(marker)
    if marker_pos == -1:
        return None, None, None
    
    # Find opening <section before marker
    section_start = content.rfind('<section', 0, marker_pos)
    if section_start == -1:
        return None, None, None
    
    # Find closing </section>
    section_end = find_closing_tag(content, section_start + len('<section'))
    if section_end == -1:
        return None, None, None
    
    return section_start, section_end, content[section_start:section_end]

def reorder_html_file(filepath, dry_run=False):
    """Read HTML file, reorder sections, optionally write back"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find both sections
    t_start, t_end, t_section = extract_section(content, '📚 TIJDSGEEST')
    m_start, m_end, m_section = extract_section(content, 'MEESTERWERKEN')
    
    if not t_section:
        return 'no_tijdsgeest'
    if not m_section:
        return 'no_meesterwerken'
    
    # Check order
    if m_start < t_start:
        return 'already_correct'
    
    # Swap: put MEESTERWERKEN first, then TIJDSGEEST
    # Content between the two sections
    between = content[t_end:m_start]
    # Content after the second section
    after = content[m_end:]
    # Content before the first section
    before = content[:t_start]
    
    new_content = before + m_section + between + t_section + after
    
    if dry_run:
        print(f"  WOULD reorder: {os.path.basename(filepath)}")
        return 'dry_run'
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 'reordered'

def main():
    import sys
    
    website_dir = '/root/.openclaw/workspace/kunstgeschiedenis/website'
    
    # Check for single file mode
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if not os.path.isabs(filepath):
            filepath = os.path.join(website_dir, filepath)
        
        print(f"Testing on: {filepath}\n")
        result = reorder_html_file(filepath, dry_run=False)
        print(f"Result: {result}")
        return
    
    # Process all files
    html_files = sorted(glob.glob(os.path.join(website_dir, '*.html')))
    html_files = [f for f in html_files if os.path.basename(f) != 'index.html']
    
    print(f"Processing {len(html_files)} files\n")
    
    # Create backup
    backup_dir = os.path.join(website_dir, 'backup_before_reorder')
    os.makedirs(backup_dir, exist_ok=True)
    for f in html_files:
        shutil.copy(f, backup_dir)
    print(f"✅ Backup created in {backup_dir}\n")
    
    stats = {'reordered': 0, 'already_correct': 0, 'no_tijdsgeest': 0, 'no_meesterwerken': 0}
    
    for filepath in html_files:
        result = reorder_html_file(filepath)
        stats[result] = stats.get(result, 0) + 1
        
        name = os.path.basename(filepath)
        if result == 'reordered':
            print(f"  ✅ {name}")
        elif result == 'already_correct':
            print(f"  ✓  {name} (already correct)")
        elif result == 'no_tijdsgeest':
            print(f"  ⏭️  {name} (no tijdsgeest)")
        elif result == 'no_meesterwerken':
            print(f"  ⏭️  {name} (no meesterwerken)")
    
    print(f"\n📊 Results:")
    print(f"   Reordered: {stats['reordered']}")
    print(f"   Already correct: {stats['already_correct']}")
    print(f"   No tijdsgeest: {stats['no_tijdsgeest']}")
    print(f"   No meesterwerken: {stats['no_meesterwerken']}")

if __name__ == '__main__':
    main()
