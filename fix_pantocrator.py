#!/usr/bin/env python3
import requests
from pathlib import Path

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
filepath = Path('/root/.openclaw/workspace/kunstgeschiedenis/website/images/byzantijns/03_pantocrator.jpg')

# Direct URLs for Christ Pantocrator
urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg/800px-Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg/600px-Christ_Pantocrator_mosaic_from_Hagia_Sophia_2744_x_2900_pixels_3.1_MB.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Christ_Pantocrator_Dehici.jpg/800px-Christ_Pantocrator_Dehici.jpg",
]

for url in urls:
    print(f"Trying: {url[:80]}...")
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200 and len(r.content) > 10000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✓ Downloaded: {len(r.content)//1024} KB")
            break
        else:
            print(f"✗ Failed: {r.status_code}, {len(r.content)} bytes")
    except Exception as e:
        print(f"✗ Error: {e}")

print("Done!")
