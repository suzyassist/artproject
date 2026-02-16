#!/usr/bin/env python3
"""
Download Romaans images via Wikimedia Commons API
"""

import requests
import json
import time
from pathlib import Path

IMG_DIR = Path('/root/.openclaw/workspace/kunstgeschiedenis/website/images/romaans')
IMG_DIR.mkdir(exist_ok=True, parents=True)

# Search for images on Wikimedia Commons
def search_commons(title):
    """Search Wikimedia Commons for an image"""
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": title,
        "srnamespace": 6,  # File namespace
        "srlimit": 5
    }
    
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        results = data.get('query', {}).get('search', [])
        return [r['title'] for r in results]
    except Exception as e:
        print(f"❌ Commons search error: {e}")
        return []

def get_image_url(filename):
    """Get direct image URL from Commons"""
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": filename,
        "prop": "imageinfo",
        "iiprop": "url|size",
        "iiurlwidth": 800
    }
    
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        pages = data.get('query', {}).get('pages', {})
        
        for page_id, page_data in pages.items():
            if 'imageinfo' in page_data:
                info = page_data['imageinfo'][0]
                # Try thumbnail first, then full
                return info.get('thumburl') or info.get('url')
    except Exception as e:
        print(f"❌ Commons URL error: {e}")
    
    return None

def download_image(url, filename):
    """Download image with proper headers"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (ArtHistoryBot/1.0)',
        'Referer': 'https://commons.wikimedia.org/'
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200 and len(r.content) > 10000:
            filepath = IMG_DIR / filename
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return len(r.content)
    except Exception as e:
        print(f"❌ Download error: {e}")
    
    return 0

# Artworks to find
artworks = [
    {"search": "Speyer Cathedral", "filename": "01_speyer.jpg"},
    {"search": "Conques Abbey Church", "filename": "02_conques.jpg"},
    {"search": "Bayeux Tapestry", "filename": "03_bayeux.jpg"},
    {"search": "Durham Cathedral", "filename": "04_durham.jpg"},
    {"search": "Pisa Cathedral facade", "filename": "05_pisa.jpg"},
    {"search": "Saint-Sernin Toulouse", "filename": "06_stsernin.jpg"},
    {"search": "Vézelay Basilica", "filename": "07_vezelay.jpg"},
    {"search": "Cluny Abbey", "filename": "08_cluny.jpg"},
    {"search": "Autun Cathedral tympanum", "filename": "09_autun.jpg"},
    {"search": "Moissac Abbey portal", "filename": "10_moissac.jpg"},
]

print("🌐 Downloading Romaans images from Wikimedia Commons...")

downloaded = 0

for art in artworks:
    print(f"🔍 Searching: {art['search']}")
    
    # Search Commons
    files = search_commons(art['search'])
    
    if not files:
        print(f"  ❌ No results")
        continue
    
    print(f"  ✅ Found {len(files)} files")
    
    # Try each file
    for file in files[:3]:
        img_url = get_image_url(file)
        
        if img_url:
            size = download_image(img_url, art['filename'])
            
            if size:
                print(f"  ✅ Downloaded: {art['filename']} ({size//1024} KB)")
                downloaded += 1
                break
            else:
                print(f"  ❌ Download failed for {file}")
        else:
            print(f"  ❌ No URL for {file}")
    
    time.sleep(0.5)

print(f"\n🖼️ Complete: {downloaded}/10 Romaans images downloaded")
