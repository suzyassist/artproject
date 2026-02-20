#!/usr/bin/env python3
import json
import os

# Load art_movements.json to get all movement names
with open('art_movements.json', 'r', encoding='utf-8') as f:
    art_data = json.load(f)

# Load existing tijdsgeest.json
with open('tijdsgeest.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# Get all movement IDs from art_movements.json
art_movements = {m['id']: m for m in art_data['movements'] if 'id' in m}

# Update tijdsgeest.json with all movements from art_movements.json
existing_ids = {entry['name']: entry for entry in existing_data['art_movements']}

new_entries = []
for movement_id, movement_data in art_movements.items():
    movement_name = movement_data['name']

    if movement_name in existing_ids:
        # Update existing entry
        existing_ids[movement_name]['period'] = f"{movement_data['start']}-{movement_data['end']}"
        print(f"Updated: {movement_name}")
    else:
        # Add new entry with empty political_perspective
        new_entry = {
            "name": movement_name,
            "period": f"{movement_data['start']}-{movement_data['end']}",
            "political_perspective": None
        }
        new_entries.append(new_entry)
        print(f"Added: {movement_name}")

# Add new entries
existing_data['art_movements'].extend(new_entries)

# Sort by movement name
existing_data['art_movements'].sort(key=lambda x: x['name'])

# Save updated tijdsgeest.json
with open('tijdsgeest.json', 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, indent=2, ensure_ascii=False)

print(f"\n✅ tijdsgeest.json updated! Total: {len(existing_data['art_movements'])} movements")
