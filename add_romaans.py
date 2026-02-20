#!/usr/bin/env python3
import json

# Add romaans
romaans_data = {
    "name": "Romaans",
    "type": "canon",
    "start": 1000,
    "end": 1400,
    "visual": {
        "kenmerken": [
            "enorme kerk",
            "kleinere kerk",
            "abten en kloosters",
            "heidens monumenten"
        ],
        "stijlfiguren": [
            "waterval",
            "romane sculptuur",
            "bronzen deuren"
        ],
        "palet": [
            "bibiellisch rood en groen",
            "goudaccenten"
        ],
        "technieken": [
            "glacis",
            "mosaïeken",
            "muurschilderkunst"
        ],
        "motieven": [
            "kruisweg",
            "steden en markten",
            "transformatie van de menselijke vorm",
            "gerichte en nepotistische religieuze thema's"
        ]
    },
    "works": [
        {
            "title": "Grote Kathedraal van Cluny III",
            "creator": "N/A",
            "image": {"url": None, "page": None, "source": None, "license": None, "attribution": None},
            "identifiers": {"wikidata_qid": None, "commons_file": None, "iiif_manifest": None},
            "copyright": {
                "status": None, "license": None, "rights_holder": None,
                "jurisdiction": None, "expiry_year_estimate": None,
                "source_confidence": None, "publish_ok": None, "notes": None
            },
            "links": {"direct_image": None, "info_page": None, "source": None}
        },
        {
            "title": "De Madonna van Reims",
            "creator": "Giles de Corbie",
            "image": {"url": None, "page": None, "source": None, "license": None, "attribution": None},
            "identifiers": {"wikidata_qid": None, "commons_file": None, "iiif_manifest": None},
            "copyright": {
                "status": None, "license": None, "rights_holder": None,
                "jurisdiction": None, "expiry_year_estimate": None,
                "source_confidence": None, "publish_ok": None, "notes": None
            },
            "links": {"direct_image": None, "info_page": None, "source": None}
        }
    ],
    "needs_research": False
}

# Load the current JSON
with open('art_movements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check if it exists
exists = any(m.get("id") == "romaans" for m in data["movements"])
if not exists:
    data["movements"].append(romaans_data)
    print(f"Added: romaans")
else:
    print(f"Skipped (already exists): romaans")

# Save
with open('art_movements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ art_movements.json updated! Total: {len(data['movements'])} movements")
