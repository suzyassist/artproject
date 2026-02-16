#!/usr/bin/env python3
import requests
import time
from pathlib import Path

IMG_DIR = Path('/root/.openclaw/workspace/kunstgeschiedenis/website/images/romaans')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Fix missing Romaans image
images = [
    ("Abbey Church of Saint Foy", "02_conques.jpg"),
]

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

for search_term, filename in images:
    filepath = IMG_DIR / filename
    print(f"🔍 {search_term}...", end=' ')
    url = get_wiki_image_url(search_term)
    if url:
        size = download_image(url, filepath)
        if size:
            print(f"✓ {size//1024} KB")
        else:
            print("✗ failed")
    else:
        print("✗ not found")

print("Done!")
