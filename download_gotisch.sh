#!/bin/bash
# Download Gotisch images

cd /root/.openclaw/workspace/kunstgeschiedenis/website/images

mkdir -p gotisch
cd gotisch

echo "Downloading Gotisch images..."

# 1. Notre-Dame de Paris
wget -q --user-agent="Mozilla/5.0" -O 01_notredame.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Notre-Dame_de_Paris_2013-07-24.jpg/800px-Notre-Dame_de_Paris_2013-07-24.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 01_notredame.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/5/50/Notre-Dame_de_Paris_2013-07-24.jpg"

# 2. Chartres Cathedral
wget -q --user-agent="Mozilla/5.0" -O 02_chartres.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Cath%C3%A9drale_Notre-Dame_de_Chartres.jpg/800px-Cath%C3%A9drale_Notre-Dame_de_Chartres.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 02_chartres.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/1/16/Cath%C3%A9drale_Notre-Dame_de_Chartres.jpg"

# 3. Sainte-Chapelle
wget -q --user-agent="Mozilla/5.0" -O 03_saintechapelle.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Ste_chapelle_panorama.jpg/800px-Ste_chapelle_panorama.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 03_saintechapelle.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8e/Ste_chapelle_panorama.jpg"

# 4. Reims Cathedral
wget -q --user-agent="Mozilla/5.0" -O 04_reims.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Cath%C3%A9drale_Notre-Dame_de_Reims.jpg/800px-Cath%C3%A9drale_Notre-Dame_de_Reims.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 04_reims.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6c/Cath%C3%A9drale_Notre-Dame_de_Reims.jpg"

# 5. Amiens Cathedral
wget -q --user-agent="Mozilla/5.0" -O 05_amiens.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Amiens_Cathedral.jpg/800px-Amiens_Cathedral.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 05_amiens.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6a/Amiens_Cathedral.jpg"

# 6. Cologne Cathedral
wget -q --user-agent="Mozilla/5.0" -O 06_cologne.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/K%C3%B6lner_Dom.jpg/800px-K%C3%B6lner_Dom.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 06_cologne.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6e/K%C3%B6lner_Dom.jpg"

# 7. Ghent Altarpiece (van Eyck)
wget -q --user-agent="Mozilla/5.0" -O 07_ghent.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Ghent_Altarpiece_%28Jan_van_Eyck%29.jpg/800px-Ghent_Altarpiece_%28Jan_van_Eyck%29.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 07_ghent.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/2/2f/Ghent_Altarpiece_%28Jan_van_Eyck%29.jpg"

# 8. Tres Riches Heures
wget -q --user-agent="Mozilla/5.0" -O 08_tresriches.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Les_Tr%C3%A8s_Riches_Heures_du_duc_de_Berry_janvier.jpg/800px-Les_Tr%C3%A8s_Riches_Heures_du_duc_de_Berry_janvier.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 08_tresriches.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/e/e2/Les_Tr%C3%A8s_Riches_Heures_du_duc_de_Berry_janvier.jpg"

# 9. Westminster Abbey
wget -q --user-agent="Mozilla/5.0" -O 09_westminster.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Westminster_Abbey.jpg/800px-Westminster_Abbey.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 09_westminster.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/5/54/Westminster_Abbey.jpg"

# 10. Milan Cathedral
wget -q --user-agent="Mozilla/5.0" -O 10_milan.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Milan_Cathedral.jpg/800px-Milan_Cathedral.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 10_milan.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/7/7c/Milan_Cathedral.jpg"

ls -la *.jpg
cd ..

echo "Gotisch done!"
