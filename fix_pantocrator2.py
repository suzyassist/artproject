#!/usr/bin/env python3
import requests
from pathlib import Path

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
filepath = Path('/root/.openclaw/workspace/kunstgeschiedenis/website/images/byzantijns/03_pantocrator.jpg')

# Try different sources
sources = [
    # Internet Archive
    ("Internet Archive", "https://archive.org/download/ChristPantocrator/Christ_Pantocrator.jpg"),
    # Wikimedia with different format
    ("Wikimedia direct", "https://upload.wikimedia.org/wikipedia/commons/1/15/Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg"),
    # Wikipedia file page image
    ("Wikipedia EN", "https://en.wikipedia.org/wiki/Special:FilePath/Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg"),
]

for name, url in sources:
    print(f"Trying {name}: {url[:60]}...")
    try:
        r = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 10000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✓ Downloaded: {len(r.content)//1024} KB")
            break
        else:
            print(f"✗ Failed: {r.status_code}, {len(r.content)} bytes")
    except Exception as e:
        print(f"✗ Error: {e}")

# Check result
if filepath.exists():
    size = filepath.stat().st_size
    if size > 10000:
        print(f"\n✅ Final size: {size//1024} KB")
    else:
        print(f"\n⚠️ File too small: {size} bytes")
else:
    print("\n❌ File not created")
