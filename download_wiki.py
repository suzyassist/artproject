#!/usr/bin/env python3
"""
Download images directly from Wikipedia page scraping
"""

import requests
import re
import time
from pathlib import Path

IMG_DIR = Path('/root/.openclaw/workspace/kunstgeschiedenis/website/images')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_wiki_image_url(page_title, lang='en'):
    """Get image URL from Wikipedia page"""
    try:
        # Try to get from Wikipedia API
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
            if 'pageimage' in page:
                # Get full image URL
                img_name = page['pageimage']
                return f"https://upload.wikimedia.org/wikipedia/commons/thumb/{img_name[0]}/{img_name[:2]}/{img_name}/800px-{img_name}"
    except Exception as e:
        print(f"  Error: {e}")
    
    return None

def download_image(url, filepath):
    """Download image"""
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200 and len(r.content) > 5000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return len(r.content)
    except Exception as e:
        print(f"  Download error: {e}")
    return 0

# Define images to download
romaans = [
    ("Speyer Cathedral", "01_speyer.jpg"),
    ("Conques Abbey", "02_conques.jpg"),
    ("Bayeux Tapestry", "03_bayeux.jpg"),
    ("Durham Cathedral", "04_durham.jpg"),
    ("Pisa Cathedral", "05_pisa.jpg"),
    ("Basilica of Saint-Sernin, Toulouse", "06_stsernin.jpg"),
    ("Vézelay Abbey", "07_vezelay.jpg"),
    ("Cluny Abbey", "08_cluny.jpg"),
    ("Autun Cathedral", "09_autun.jpg"),
    ("Moissac Abbey", "10_moissac.jpg"),
]

gotisch = [
    ("Notre-Dame de Paris", "01_notredame.jpg"),
    ("Chartres Cathedral", "02_chartres.jpg"),
    ("Sainte-Chapelle", "03_saintechapelle.jpg"),
    ("Reims Cathedral", "04_reims.jpg"),
    ("Amiens Cathedral", "05_amiens.jpg"),
    ("Cologne Cathedral", "06_cologne.jpg"),
    ("Ghent Altarpiece", "07_ghent.jpg"),
    ("Très Riches Heures du Duc de Berry", "08_tresriches.jpg"),
    ("Westminster Abbey", "09_westminster.jpg"),
    ("Milan Cathedral", "10_milan.jpg"),
]

byzantijns = [
    ("Hagia Sophia", "01_hagiasophia.jpg"),
    ("Basilica of San Vitale", "02_sanvitale.jpg"),
    ("Christ Pantocrator (Sinai)", "03_pantocrator.jpg"),
    ("Our Lady of Vladimir", "04_vladimir.jpg"),
    ("Daphni Monastery", "05_daphni.jpg"),
    ("Rossano Gospels", "06_rossano.jpg"),
    ("David Plates", "07_davidplates.jpg"),
    ("Chludov Psalter", "08_chludov.jpg"),
    ("Harbaville Triptych", "09_harbaville.jpg"),
    ("Paris Psalter", "10_parispsalter.jpg"),
]

# Download function
def download_batch(images, folder_name):
    folder = IMG_DIR / folder_name
    folder.mkdir(exist_ok=True, parents=True)
    
    print(f"\n📥 Downloading {folder_name} images...")
    downloaded = 0
    
    for search_term, filename in images:
        filepath = folder / filename
        if filepath.exists() and filepath.stat().st_size > 10000:
            print(f"  ⏭️  {filename} already exists ({filepath.stat().st_size//1024} KB)")
            downloaded += 1
            continue
            
        print(f"  🔍 {search_term}...", end=' ')
        url = get_wiki_image_url(search_term)
        
        if url:
            size = download_image(url, filepath)
            if size:
                print(f"✓ {size//1024} KB")
                downloaded += 1
            else:
                print("✗ download failed")
        else:
            print("✗ not found")
        
        time.sleep(0.5)
    
    print(f"  📊 {downloaded}/{len(images)} downloaded")
    return downloaded

# Download all
romaans_count = download_batch(romaans, "romaans")
gotisch_count = download_batch(gotisch, "gotisch")
byzantijns_count = download_batch(byzantijns, "byzantijns")

print(f"\n🎨 Complete!")
print(f"  Romaans: {romaans_count}/10")
print(f"  Gotisch: {gotisch_count}/10")
print(f"  Byzantijns: {byzantijns_count}/10")
