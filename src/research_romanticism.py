#!/usr/bin/env python3
"""
Research script for Romanticism artworks
Fetches data from Wikipedia/Wikidata to verify and enrich artwork information
"""

import json
import subprocess
import re
from pathlib import Path

# Load the JSON
with open('/root/.openclaw/workspace/kunstgeschiedenis/art_movements.json') as f:
    data = json.load(f)

# Find Romanticism
romanticism = None
for m in data['movements']:
    if m['id'] == 'romanticisme':
        romanticism = m
        break

print("=== ROMANTICISME WERKEN ===\n")
for i, work in enumerate(romanticism['works'], 1):
    print(f"{i}. {work['title']}")
    print(f"   Artist: {work['creator']}")
    print(f"   Status: {'✓' if work['creator'] else '?'} Creator known")
    print()

# Save list for processing
works_list = []
for work in romanticism['works']:
    works_list.append({
        'title': work['title'],
        'creator': work['creator'],
        'verified': False
    })

print(f"\nTotal: {len(works_list)} works to research")
