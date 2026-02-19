#!/usr/bin/env python3
"""
Image download helper - saves URLs for manual download if automated fails
"""

from pathlib import Path

IMG_DIR = Path('/root/.openclaw/workspace/kunstgeschiedenis/images')

# Manual download URLs for artworks
MANUAL_DOWNLOADS = {
    'wanderer': {
        'title': 'Wanderer above the Sea of Fog',
        'artist': 'Caspar David Friedrich',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_Sea_of_Fog_-_Google_Art_Project.jpg',
        'instructions': 'Rechtermuisklik → Afbeelding opslaan als → wanderer.jpg'
    },
    'eismeer': {
        'title': 'The Sea of Ice (Das Eismeer)',
        'artist': 'Caspar David Friedrich',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/0/06/Caspar_David_Friedrich_-_Das_Eismeer_-_Google_Art_Project.jpg',
        'instructions': 'Rechtermuisklik → Afbeelding opslaan als → eismeer.jpg'
    },
    'saturn': {
        'title': 'Saturn Devouring His Son',
        'artist': 'Francisco Goya',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/6/62/Francisco_de_Goya%2C_Saturno_devorando_a_un_hijo.jpg',
        'instructions': 'Rechtermuisklik → Afbeelding opslaan als → saturn.jpg'
    },
    'turner_rain': {
        'title': 'Rain, Steam and Speed',
        'artist': 'J.M.W. Turner',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/4/46/Turner_-_Rain%2C_Steam_and_Speed_-_The_Great_Western_Railway.jpg',
        'instructions': 'Rechtermuisklik → Afbeelding opslaan als → turner_rain.jpg'
    }
}

print("="*70)
print("🖼️  HANDMATIGE DOWNLOAD INSTRUCTIES")
print("="*70)
print("\nWikimedia Commons blokkeert geautomatiseerde downloads.")
print("Download deze afbeeldingen handmatig en plaats ze in:")
print(f"📁 {IMG_DIR}\n")

for key, data in MANUAL_DOWNLOADS.items():
    print(f"\n{'─'*70}")
    print(f"🎨 {data['title']}")
    print(f"   Door: {data['artist']}")
    print(f"\n   URL: {data['url']}")
    print(f"\n   📥 {data['instructions']}")
    print(f"   💾 Bestandsnaam: {key}.jpg")

print(f"\n{'='*70}")
print("✅ REEDS GEDOWNLOAD:")
print("="*70)

existing = list(IMG_DIR.glob('*.jpg'))
if existing:
    for f in sorted(existing):
        size_kb = f.stat().st_size // 1024
        print(f"  ✓ {f.name} ({size_kb} KB)")
else:
    print("  (nog geen afbeeldingen)")

print(f"\n{'='*70}")
print("📝 OF: Gebruik deze eenmalige download links:")
print("="*70)

# Create download script
script_path = IMG_DIR / 'download.sh'
with open(script_path, 'w') as f:
    f.write("#!/bin/bash\n# Download images with proper headers\n\ncd \"$(dirname \"$0\")\"\n\n")
    for key, data in MANUAL_DOWNLOADS.items():
        f.write(f"# {data['title']}\n")
        f.write(f"echo 'Downloading {key}...'\n")
        f.write(f"curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \\\n")
        artist_slug = data['artist'].replace(' ', '_')
        f.write(f"  -H 'Referer: https://en.wikipedia.org/wiki/{artist_slug}' \\\n")
        f.write(f"  -o {key}.jpg \\\n")
        f.write(f"  '{data['url']}'\n")
        f.write(f"sleep 2\n\n")
    f.write("echo 'Done!'\n")

script_path.chmod(0o755)
print(f"\n💻 Script aangemaakt: {script_path}")
print("   Voer uit met: bash images/download.sh")
