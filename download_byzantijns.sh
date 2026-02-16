#!/bin/bash
# Download Byzantijns images

cd /root/.openclaw/workspace/kunstgeschiedenis/website/images

mkdir -p byzantijns
cd byzantijns

echo "Downloading Byzantijns images..."

# 1. Hagia Sophia (replace small placeholder)
wget -q --user-agent="Mozilla/5.0" -O 01_hagiasophia.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Hagia_Sophia_interior.jpg/800px-Hagia_Sophia_interior.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 01_hagiasophia.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8d/Hagia_Sophia_interior.jpg"

# 2. San Vitale (replace small placeholder)
wget -q --user-agent="Mozilla/5.0" -O 02_sanvitale.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/San_Vitale_Ravenna.jpg/800px-San_Vitale_Ravenna.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 02_sanvitale.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6f/San_Vitale_Ravenna.jpg"

# 3. Christus Pantocrator (replace small placeholder)
wget -q --user-agent="Mozilla/5.0" -O 03_pantocrator.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Christ_Pantocrator_Mosaic.jpg/800px-Christ_Pantocrator_Mosaic.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 03_pantocrator.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6c/Christ_Pantocrator_Mosaic.jpg"

# 4. Vladimir Icon (replace small placeholder)
wget -q --user-agent="Mozilla/5.0" -O 04_vladimir.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Our_Lady_of_Vladimir.jpg/800px-Our_Lady_of_Vladimir.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 04_vladimir.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/7/7c/Our_Lady_of_Vladimir.jpg"

# 5. Daphni Pantocrator
wget -q --user-agent="Mozilla/5.0" -O 05_daphni.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Daphni_Pantocrator.jpg/800px-Daphni_Pantocrator.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 05_daphni.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8a/Daphni_Pantocrator.jpg"

# 6. Rossano Gospels
wget -q --user-agent="Mozilla/5.0" -O 06_rossano.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Rossano_Gospels.jpg/800px-Rossano_Gospels.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 06_rossano.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8b/Rossano_Gospels.jpg"

# 7. David Plates (Byzantine silver)
wget -q --user-agent="Mozilla/5.0" -O 07_davidplates.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/David_Plate.jpg/800px-David_Plate.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 07_davidplates.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/6/6c/David_Plate.jpg"

# 8. Chludov Psalter
wget -q --user-agent="Mozilla/5.0" -O 08_chludov.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Chludov_Psalter.jpg/800px-Chludov_Psalter.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 08_chludov.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/7/7c/Chludov_Psalter.jpg"

# 9. Harbaville Triptych
wget -q --user-agent="Mozilla/5.0" -O 09_harbaville.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Harbaville_Triptych.jpg/800px-Harbaville_Triptych.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 09_harbaville.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8e/Harbaville_Triptych.jpg"

# 10. Paris Psalter
wget -q --user-agent="Mozilla/5.0" -O 10_parispsalter.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Paris_Psalter.jpg/800px-Paris_Psalter.jpg" || \
  wget -q --user-agent="Mozilla/5.0" -O 10_parispsalter.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/8/8c/Paris_Psalter.jpg"

ls -la *.jpg
cd ..

echo "Byzantijns done!"
