#!/bin/bash
# Download images using curl with proper headers

cd /root/.openclaw/workspace/kunstgeschiedenis/website/images/romaans

echo "Downloading Romaans images with curl..."

# 1. Speyer Cathedral
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg/800px-Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg" \
  -o 01_speyer.jpg --max-time 30
sleep 1

# 2. Sainte-Foy de Conques
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Conques_Abbatiale_Sainte-Foy.jpg/800px-Conques_Abbatiale_Sainte-Foy.jpg" \
  -o 02_conques.jpg --max-time 30
sleep 1

# 3. Bayeux Tapestry
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bayeux_Tapestry_William.jpg/800px-Bayeux_Tapestry_William.jpg" \
  -o 03_bayeux.jpg --max-time 30
sleep 1

# 4. Durham Cathedral
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Durham_Cathedral_External.jpg/800px-Durham_Cathedral_External.jpg" \
  -o 04_durham.jpg --max-time 30
sleep 1

# 5. Pisa Cathedral
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Pisa_Cathedral_Facade.jpg/800px-Pisa_Cathedral_Facade.jpg" \
  -o 05_pisa.jpg --max-time 30
sleep 1

ls -la *.jpg
