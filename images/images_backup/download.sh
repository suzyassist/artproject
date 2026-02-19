#!/bin/bash
# Download images with proper headers

cd "$(dirname "$0")"

# Wanderer above the Sea of Fog
echo 'Downloading wanderer...'
curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  -H 'Referer: https://en.wikipedia.org/wiki/Caspar_David_Friedrich' \
  -o wanderer.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_Sea_of_Fog_-_Google_Art_Project.jpg'
sleep 2

# The Sea of Ice (Das Eismeer)
echo 'Downloading eismeer...'
curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  -H 'Referer: https://en.wikipedia.org/wiki/Caspar_David_Friedrich' \
  -o eismeer.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/0/06/Caspar_David_Friedrich_-_Das_Eismeer_-_Google_Art_Project.jpg'
sleep 2

# Saturn Devouring His Son
echo 'Downloading saturn...'
curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  -H 'Referer: https://en.wikipedia.org/wiki/Francisco_Goya' \
  -o saturn.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/6/62/Francisco_de_Goya%2C_Saturno_devorando_a_un_hijo.jpg'
sleep 2

# Rain, Steam and Speed
echo 'Downloading turner_rain...'
curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  -H 'Referer: https://en.wikipedia.org/wiki/J.M.W._Turner' \
  -o turner_rain.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/4/46/Turner_-_Rain%2C_Steam_and_Speed_-_The_Great_Western_Railway.jpg'
sleep 2

echo 'Done!'
