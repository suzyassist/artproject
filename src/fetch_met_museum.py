#!/usr/bin/env python3
"""
Download missing Romanticism images using Met Museum API
"""

import requests
from pathlib import Path

IMG_DIR = Path('/root/.openclaw/workspace/kunstgeschiedenis/images')

def search_met_museum(query):
    """Search Met Museum collection"""
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}&isPublicDomain=true"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get('objectIDs', [])
    except Exception as e:
        print(f"   Error: {e}")
    return []

def get_object_details(object_id):
    """Get object details from Met Museum"""
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"   Error: {e}")
    return None

print("🔍 Searching Met Museum API for Romanticism artworks...\n")

# Works we're looking for
works = [
    ("Caspar David Friedrich", ["Wanderer", "Sea of Fog", "Eismeer"]),
    ("Francisco Goya", ["Saturn", "3rd May", "Tres de Mayo"]),
    ("J.M.W. Turner", ["Rain Steam Speed", "Trafalgar"]),
]

found_images = []

for artist, keywords in works:
    for keyword in keywords:
        print(f"Searching: {artist} - {keyword}")
        ids = search_met_museum(f"{artist} {keyword}")
        if ids:
            print(f"   ✓ Found {len(ids)} objects")
            # Get first object details
            details = get_object_details(ids[0])
            if details and details.get('primaryImage'):
                title = details.get('title', 'Unknown')
                image_url = details.get('primaryImage')
                found_images.append({
                    'title': title,
                    'artist': artist,
                    'url': image_url
                })
                print(f"   📷 {title[:50]}")
        else:
            print(f"   ✗ Not found in Met Museum")

print(f"\n{'='*60}")
print(f"Found {len(found_images)} images in Met Museum collection")
for img in found_images:
    print(f"  - {img['title'][:40]}... ({img['artist']})")

print("\n⚠️  NOTE: Some artworks are not in Met Museum:")
print("   - Wanderer above the Sea of Fog → Kunsthalle Hamburg")
print("   - Saturn Devouring His Son → Museo del Prado")
print("   - Das Eismeer → Hamburger Kunsthalle")
print("\n💡 Suggestion: Use alternative images from Met Museum collection")
