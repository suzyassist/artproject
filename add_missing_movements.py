#!/usr/bin/env python3
import json
import copy

# Load the current art_movements.json
with open('art_movements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Movements that need to be added (based on user's list)
new_movements = {
    "dadaisme": {
        "name": "Dadaisme",
        "type": "canon",
        "start": 1916,
        "end": 1924,
        "visual": {
            "kenmerken": [
                "antikunst",
                "chaos",
                "onbedoeld",
                "absurde humor"
            ],
            "stijlfiguren": [
                "collage",
                "ready-mades",
                "zufällige assemblage"
            ],
            "palet": [
                "concurrerend",
                "contrast"
            ],
            "technieken": [
                "montage",
                "collage",
                "fotomontage"
            ],
            "motieven": [
                "anti-art",
                "anti-logica",
                "ironie",
                "pessimisme"
            ]
        },
        "works": [
            {
                "title": "Fontein (Fountain)",
                "creator": "Marcel Duchamp",
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
                "title": "Die Tante",
                "creator": "Hans Arp",
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
    "popart": {
        "name": "Pop Art",
        "type": "canon",
        "start": 1950,
        "end": 1970,
        "visual": {
            "kenmerken": [
                "hergebruik van dagelijks objecten",
                "massaproductie esthetiek",
                "harde randen",
                "simpele vormen"
            ],
            "stijlfiguren": [
                "appropriatie",
                "serigraphie",
                "mega-afmetingen"
            ],
            "palet": [
                "donker en fel",
                "contrastrijk"
            ],
            "technieken": [
                "lithografie",
                "acryl",
                "aquarel"
            ],
            "motieven": [
                "consumentencultuur",
                "media",
                "reclame",
                "melk, eieren, pittenzakken"
            ]
        },
        "works": [
            {
                "title": "Campbell's Soup Cans",
                "creator": "Andy Warhol",
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
                "title": "Marilyn Monroe",
                "creator": "Andy Warhol",
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
    "postmodern": {
        "name": "Postmodern",
        "type": "canon",
        "start": 1970,
        "end": 1990,
        "visual": {
            "kenmerken": [
                "plaatsing van kleurrijkheid",
                "groeiend zelfbewustzijn",
                "relationele 3D",
                "hergebruik en collages"
            ],
            "stijlfiguren": [
                "metafictie",
                "appropriatie",
                "bricolage"
            ],
            "palet": [
                "donker en somber",
                "harde randen"
            ],
            "technieken": [
                "serigraphie",
                "aquarel"
            ],
            "motieven": [
                "referentie naar kunstgeschiedenis",
                "skepticisme"
            ]
        },
        "works": [
            {
                "title": "Campbell's Soup Cans II",
                "creator": "Andy Warhol",
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
                "title": "The Gold of the Americas",
                "creator": "Rebecca Morgan",
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
    "hedendaags": {
        "name": "Hedendaags",
        "type": "canon",
        "start": None,
        "end": None,
        "visual": {
            "kenmerken": [
                "divers",
                "non-lineair",
                "experimenteel"
            ],
            "stijlfiguren": [
                "melange",
                "einde van de geschiedenis van de kunst"
            ],
            "palet": [
                "divers"
            ],
            "technieken": [
                "meerdere technieken"
            ],
            "motieven": [
                "kunst in de samenleving",
                "cross-disciplinair"
            ]
        },
        "works": [
            {
                "title": "Tilted Arc",
                "creator": "Richard Serra",
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
                "title": "Tether",
                "creator": "El Anatsui",
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
    "digitaal": {
        "name": "Digitaal",
        "type": "canon",
        "start": 2000,
        "end": None,
        "visual": {
            "kenmerken": [
                "digitale technieken",
                "vector graphics",
                "photo manipulation"
            ],
            "stijlfiguren": [
                "pixel art",
                "generative art",
                "3D render"
            ],
            "palet": [
                "digitale kleurenpaletten"
            ],
            "technieken": [
                "software",
                "compositie",
                "rendering"
            ],
            "motieven": [
                "technologie en kunst",
                "digitalisering"
            ]
        },
        "works": [
            {
                "title": "Fluid Fields",
                "creator": "Julian Opie",
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
    "byzantijns": {
        "name": "Byzantijns",
        "type": "canon",
        "start": 330,
        "end": 1453,
        "visual": {
            "kenmerken": [
                "abstracte sfumbatid",
                "geometrische stijl",
                "rechte lijnen",
                "gold leaf"
            ],
            "stijlfiguren": [
                "middeleeuwse afbeelding"
            ],
            "palet": [
                "rood, groen, blauw, goud"
            ],
            "technieken": [
                "mosaïeken",
                "muurschilderkunst",
                "miniatuur"
            ],
            "motieven": [
                "christelijke thema's",
                "geestelijk leven"
            ]
        },
        "works": [
            {
                "title": "Mosaïek van de Hoogste Koning",
                "creator": "Justinianus I",
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
                "title": "St. Sophia",
                "creator": "Anthemius van Tralles en Isidorus van Miletus",
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
    "conceptueel": {
        "name": "Conceptueel",
        "type": "canon",
        "start": 1960,
        "end": None,
        "visual": {
            "kenmerken": [
                "idee boven vorm",
                "kunst als idee",
                "conceptuele vooruitgang"
            ],
            "stijlfiguren": [
                "process art",
                "land art",
                "performance art"
            ],
            "palet": [
                "geen specifiek palet"
            ],
            "technieken": [
                "tekst",
                "documentatie",
                "installatie"
            ],
            "motieven": [
                "intellectuele vooruitgang",
                "kunst als methode"
            ]
        },
        "works": [
            {
                "title": "One and Three Chairs",
                "creator": "Joseph Kosuth",
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
                "title": "Mona Lisa with an Eyepatch",
                "creator": "John Baldessari",
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

# Add new movements to the data
for movement_id, movement_data in new_movements.items():
    # Check if movement already exists
    exists = any(m.get("id") == movement_id for m in data["movements"])
    if not exists:
        data["movements"].append(movement_data)
        print(f"Added: {movement_id}")
    else:
        print(f"Skipped (already exists): {movement_id}")

# Save the updated JSON
with open('art_movements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ art_movements.json updated successfully!")
print(f"Total movements: {len(data['movements'])}")
