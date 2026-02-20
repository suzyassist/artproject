#!/usr/bin/env python3
import json

# Movements that need to be added
new_movements = {
    "gotisch": {
        "name": "Gotisch",
        "type": "canon",
        "start": 1140,
        "end": 1500,
        "visual": {
            "kenmerken": [
                "spiraalvormige, asymmetrische vormen",
                "natuurlijke vormen",
                "inconsistente details",
                "naakte menselijke vormen"
            ],
            "stijlfiguren": [
                "criticism of classical rules",
                "sheer modeling",
                "giants",
                "sphinxes"
            ],
            "palet": [
                "biblical red and green",
                "gilded accents"
            ],
            "technieken": [
                "glacis",
                "stained glass",
                "gilding"
            ],
            "motieven": [
                "St. Luke painting",
                "monks",
                "pilgrims",
                "holy figures"
            ]
        },
        "works": [
            {
                "title": "Grote Kathedraal van Reims",
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
    },
    "renaissance": {
        "name": "Renaissance",
        "type": "canon",
        "start": 1400,
        "end": 1600,
        "visual": {
            "kenmerken": [
                "perspectief",
                "nieuw denken",
                "verzorgd uitgevoerd"
            ],
            "stijlfiguren": [
                "figuratief",
                "herhaalde wereldbeeld"
            ],
            "palet": [
                "hoog contrast"
            ],
            "technieken": [
                "olieverf",
                "tempera"
            ],
            "motieven": [
                "Heraderster"
            ]
        },
        "works": [
            {
                "title": "Laest",
                "creator": "Botticelli",
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
                "title": "De Davidschilderijen",
                "creator": "Donatello, Verrocchio, Michelangelo",
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
    },
    "art nouveau": {
        "name": "Art Nouveau",
        "type": "canon",
        "start": 1890,
        "end": 1910,
        "visual": {
            "kenmerken": [
                "naturalistische ornamenten",
                "ingewikkelde regels",
                "geleidelijk verdwijnen"
            ],
            "stijlfiguren": [
                "apropriatie",
                "beïnvloedingen",
                "karakteristieke stylische kenmerken",
                "organisch",
                "georganiseerde chaoticiteit"
            ],
            "palet": [
                "geen specifiek palet"
            ],
            "technieken": [
                "Illustratie",
                "stencil"
            ],
            "motieven": [
                "infinitesimal afdruk"
            ]
        },
        "works": [
            {
                "title": "Wisteria",
                "creator": "Hector Guimard",
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
                "title": "Vrouw met een Hoed",
                "creator": "Matisse",
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
}

# Load the current JSON
with open('art_movements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new movements
for movement_id, movement_data in new_movements.items():
    exists = any(m.get("id") == movement_id for m in data["movements"])
    if not exists:
        data["movements"].append(movement_data)
        print(f"Added: {movement_id}")
    else:
        print(f"Skipped (already exists): {movement_id}")

# Save
with open('art_movements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ art_movements.json updated! Total: {len(data['movements'])} movements")
