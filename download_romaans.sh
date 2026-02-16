#!/bin/bash
# Download images for art movements

cd /root/.openclaw/workspace/kunstgeschiedenis/website/images

# ROMAANS
mkdir -p romaans
cd romaans

echo "Downloading Romaans images..."

# 1. Speyer Cathedral
wget -q --user-agent="Mozilla/5.0" -O 01_speyer.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg/800px-Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 01_speyer.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6a/Speyer_Cathedral_%28UNESCO_World_Heritage_Site%29.jpg"

# 2. Sainte-Foy de Conques
wget -q --user-agent="Mozilla/5.0" -O 02_conques.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Conques_Abbatiale_Sainte-Foy.jpg/800px-Conques_Abbatiale_Sainte-Foy.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 02_conques.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/7/7e/Conques_Abbatiale_Sainte-Foy.jpg"

# 3. Bayeux Tapestry
wget -q --user-agent="Mozilla/5.0" -O 03_bayeux.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bayeux_Tapestry_William.jpg/800px-Bayeux_Tapestry_William.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 03_bayeux.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/2/2b/Bayeux_Tapestry_William.jpg"

# 4. Durham Cathedral
wget -q --user-agent="Mozilla/5.0" -O 04_durham.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Durham_Cathedral_External.jpg/800px-Durham_Cathedral_External.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 04_durham.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/a/a6/Durham_Cathedral_External.jpg"

# 5. Pisa Cathedral
wget -q --user-agent="Mozilla/5.0" -O 05_pisa.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Pisa_Cathedral_Facade.jpg/800px-Pisa_Cathedral_Facade.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 05_pisa.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/5/56/Pisa_Cathedral_Facade.jpg"

# 6. Saint-Sernin Toulouse
wget -q --user-agent="Mozilla/5.0" -O 06_stsernin.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Basilique_Saint-Sernin_Toulouse.jpg/800px-Basilique_Saint-Sernin_Toulouse.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 06_stsernin.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8a/Basilique_Saint-Sernin_Toulouse.jpg"

# 7. Vezelay
wget -q --user-agent="Mozilla/5.0" -O 07_vezelay.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Basilique_de_V%C3%A9zelay.jpg/800px-Basilique_de_V%C3%A9zelay.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 07_vezelay.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/1/1f/Basilique_de_V%C3%A9zelay.jpg"

# 8. Cluny Abbey
wget -q --user-agent="Mozilla/5.0" -O 08_cluny.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Cluny_Abbey.jpg/800px-Cluny_Abbey.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 08_cluny.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/d/d4/Cluny_Abbey.jpg"

# 9. Autun Cathedral Tympanum
wget -q --user-agent="Mozilla/5.0" -O 09_autun.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Autun_Cath%C3%A9drale_Tympan.jpg/800px-Autun_Cath%C3%A9drale_Tympan.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 09_autun.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/a/a8/Autun_Cath%C3%A9drale_Tympan.jpg"

# 10. Moissac Portal
wget -q --user-agent="Mozilla/5.0" -O 10_moissac.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Moissac_Portal.jpg/800px-Moissac_Portal.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 10_moissac.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/9/9b/Moissac_Portal.jpg"

ls -la *.jpg
cd ..

echo "Romaans done!"
