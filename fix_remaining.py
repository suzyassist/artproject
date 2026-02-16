#!/usr/bin/env python3
import requests
import time
from pathlib import Path

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def get_wiki_image_url(page_title, lang='en'):
    try:
        api_url = f"https://{lang}.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'titles': page_title,
            'prop': 'pageimages',
            'format': 'json',
            'pithumbsize': 800
        }
        r = requests.get(api_url, params=params, headers=headers, timeout=15)
        data = r.json()
        pages = data.get('query', {}).get('pages', {})
        for page_id, page in pages.items():
            if 'thumbnail' in page:
                return page['thumbnail']['source']
    except Exception as e:
        print(f"  Error: {e}")
    return None

def download_image(url, filepath):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200 and len(r.content) > 5000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return len(r.content)
    except Exception as e:
        print(f"  Download error: {e}")
    return 0

# Try alternative search terms
alternatives = [
    # Romaans
    ("/root/.openclaw/workspace/kunstgeschiedenis/website/images/romaans/02_conques.jpg", [
        "Sainte-Foy de Conques",
        "Conques", 
        "Abbatiale Sainte-Foy"
    ]),
    # Byzantijns
    ("/root/.openclaw/workspace/kunstgeschiedenis/website/images/byzantijns/03_pantocrator.jpg", [
        "Christ Pantocrator",
        "Pantocrator",
        "Sinai Pantocrator"
    ]),
    ("/root/.openclaw/workspace/kunstgeschiedenis/website/images/byzantijns/04_vladimir.jpg", [
        "Vladimir Mother of God",
        "Vladimir icon",
        "Virgin of Vladimir"
    ]),
    ("/root/.openclaw/workspace/kunstgeschiedenis/website/images/byzantijns/07_davidplates.jpg", [
        "David Plates",
        "Byzantine silver",
        "David plate"
    ]),
]

for filepath, search_terms in alternatives:
    for term in search_terms:
        print(f"🔍 {term}...", end=' ')
        url = get_wiki_image_url(term)
        if url:
            size = download_image(url, filepath)
            if size:
                print(f"✓ {size//1024} KB")
                break
            else:
                print("✗ failed")
        else:
            print("✗ not found")
        time.sleep(0.5)
    else:
        print(f"  ⚠️ All alternatives failed for {filepath}")

print("\nDone!")
