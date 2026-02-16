import requests
import time
import os

# Set up session with proper headers
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://commons.wikimedia.org/'
})

# Romaans images
romaans_images = [
    ("01_speyer.jpg", "https://upload.wikimedia.org/wikipedia/commons/6/6a/Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg"),
    ("02_conques.jpg", "https://upload.wikimedia.org/wikipedia/commons/7/7e/Conques_Abbatiale_Sainte-Foy.jpg"),
    ("03_bayeux.jpg", "https://upload.wikimedia.org/wikipedia/commons/2/2b/Bayeux_Tapestry_William.jpg"),
    ("04_durham.jpg", "https://upload.wikimedia.org/wikipedia/commons/a/a6/Durham_Cathedral_External.jpg"),
    ("05_pisa.jpg", "https://upload.wikimedia.org/wikipedia/commons/5/56/Pisa_Cathedral_Facade.jpg"),
    ("06_stsernin.jpg", "https://upload.wikimedia.org/wikipedia/commons/8/8a/Basilique_Saint-Sernin_Toulouse.jpg"),
    ("07_vezelay.jpg", "https://upload.wikimedia.org/wikipedia/commons/1/1f/Basilique_de_V%C3%A9zelay.jpg"),
    ("08_cluny.jpg", "https://upload.wikimedia.org/wikipedia/commons/d/d4/Cluny_Abbey.jpg"),
    ("09_autun.jpg", "https://upload.wikimedia.org/wikipedia/commons/a/a8/Autun_Cath%C3%A9drale_Tympan.jpg"),
    ("10_moissac.jpg", "https://upload.wikimedia.org/wikipedia/commons/9/9b/Moissac_Portal.jpg"),
]

os.chdir('/root/.openclaw/workspace/kunstgeschiedenis/website/images/romaans')

for filename, url in romaans_images:
    try:
        print(f"Downloading {filename}...")
        response = session.get(url, timeout=30)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"  ✓ {filename}: {len(response.content)} bytes")
        else:
            print(f"  ✗ {filename}: HTTP {response.status_code}, {len(response.content)} bytes")
    except Exception as e:
        print(f"  ✗ {filename}: {e}")
    time.sleep(1)

print("\nRomaans download complete!")
