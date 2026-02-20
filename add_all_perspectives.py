#!/usr/bin/env python3
"""
Script to add missing philosophical, psychological, and political perspectives
to all art movements in tijdsgeest.json
"""

import json

# Read current file
with open('/root/.openclaw/workspace/kunstgeschiedenis/tijdsgeest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Content for each movement (specific to each art movement)
# Format: (political, philosophical, psychological) - only used if missing

movement_content = {
    "Abstract Expressionisme": {
        "philosophical_perspective": {
            "title": "Existentiële Filosofie en het Sublieme: De Intellectuele Grondslag",
            "sections": [{
                "title": "Existentiële Filosofie en het Sublieme",
                "content": "Het abstract expressionisme werd diep beïnvloed door de existentieel-filosofische stromingen die Europa in de naoorlogse jaren domineerden. Jean-Paul Sartre's 'L'Être et le Néant' (1943) en Albert Camus' 'L'Étranger' (1942) stelden dat het leven geen inherente betekenis had – de mens moest zijn eigen essentie creëren. Deze filosofie vertaalde zich direct naar abstract expressionistische doeken waar geen herkenbare voorstellingen waren, alleen pure actie en emotie. Mark Rothko's kleurvelden werden de visuele equivalent van Camus' 'absurde' universum: enorm, leeg, en toch doordrenkt van menselijke aanwezigheid.\n\nDe kunstenaars zochten naar wat zij het 'sublieme' noemden – een ervaring die het normale esthetische begrip te boven ging, die ontzag en angst opriep. Dit concept, dat terugging op Edmund Burke en Immanuel Kant, werd hernomen in een moderne context: het atoomtijdperk, de Holocaust, de Koude Oorlog hadden een nieuw soort sublieme ervaring gecreëerd – niet het sublieme van de natuur, maar het sublieme van menselijke vernietiging. Barnett Newman's 'Vir Heroicus Sublimis' (1950-1951) belichaamde deze zoektocht: een enorm doek met een verticale lijn ('zip') die de oneindigheid suggereerde.\n\nDe Amerikaanse pragmatistische traditie, met figuren als John Dewey en William James, bood een alternatief perspectief. Kunst was volgens Dewey niet een gescheiden domein van 'schoonheid', maar een ervaring die continu was met het dagelijks leven. Deze filosofie ondersteunde de abstract expressionistische afwijzing van traditionele schoonheidscriteria: als kunst een ervaring was, dan kon elke ervaring – chaos, angst, vernietiging – artistiek materiaal zijn. Jackson Pollock's 'drip paintings' werden niet beoordeeld op hun representatie, maar op hun vermogen om een ervaring te creëren.\n\nStijlfiguren die deze filosofische achtergrond weerspiegelden: de nadruk op het proces boven het product ('action painting' als existentieel handelen); de afwezigheid van herkenbare figuren (weerspiegeling van de 'dood van God' en de afwezigheid van universele betekenis); de enorme schaal (het sublieme, het oneindige, het onvatbare); de asymmetrie (verwerping van traditionele harmonie en evenwicht). De abstractie was niet een esthetische keuze, maar een filosofische positie: in een wereld waar alle zekerheden waren weggevallen, kon kunst niet langer de werkelijkheid 'afbeelden' – het moest de ervaring van het bestaan zelf worden."
            }]
        },
        "psychological_perspective": {
            "title": "Het Onderbewuste en de Psychische Littekens van de Oorlog",
            "sections": [{
                "title": "Het Onderbewuste en de Psychische Littekens van de Oorlog",
                "content": "Het abstract expressionisme ontwikkelde zich in de nasleep van de Tweede Wereldoorlog, een periode waarin de collectieve psyche van Europa en Amerika diep getraumatiseerd was. De Holocaust, de atoombommen op Hiroshima en Nagasaki, de gruwelen van de concentratiekampen – deze gebeurtenissen hadden een collectieve PTSD gecreëerd die de kunstenaars probeerden te verwerken. Jackson Pollock, die in 1943 in dienst was van de WPA Federal Art Project, gebruikte zijn kunst als een vorm van psychologische verwerking. Zijn 'drip technique', die hij rond 1947 ontwikkelde, werd door critici als een uiting van 'action painting' bestempeld – een proces dat de kunstenaar in een staat van trance bracht, een directe verbinding met het onbewuste.\n\nDe invloed van het surrealisme, met zijn technieken van 'automatisme' en 'écriture automatique', was direct zichtbaar. Surrealisten als André Breton en Max Ernst, die naar New York waren gevlucht, hadden de nadruk gelegd op het onderbewuste als bron van artistieke creatie. Pollock's 'drip paintings' werden gezien als een Amerikaanse variant van dit automatisme: de kunstenaar stond boven het doek, liet de verf uit een blik of penseel vallen, en volgde een intuïtieve, bijna meditatieve beweging. Dit proces weerspiegelde de psychoanalytische idee dat creativiteit voortkwam uit de diepere lagen van de psyche, niet uit rationele planning.\n\nMark Rothko's 'color field paintings' boden een ander psychologisch perspectief. Rothko sprak over zijn schilderijen als 'dramas' en 'tragedies', als expressies van 'basic human emotions – tragedy, ecstasy, doom'. De enorme kleurvelden, vaak in donkere tinten (zwart, grijs, bordeaux), creëerden een sfeer van contemplatie en existentiële angst. Rothko, die zelf kampte met depressies en uiteindelijk in 1970 zelfmoord zou plegen, zag zijn kunst als een poging om de kijker te confronteren met de fundamentele eenzaamheid van het menselijk bestaan. Zijn latere werken voor de Rothko Chapel in Houston werden ontworpen als een spirituele ruimte, een plek voor meditatie en introspectie.\n\nStijlfiguren die deze psychologische focus weerspiegelden: de 'all-over' compositie (zonder centrum, zonder hiërarchie – weerspiegeling van een gefragmenteerd bewustzijn); de zichtbare sporen van de kunstenaarshand (penseelstreken, gedruppelde verf – directe verbinding met het lichaam en de psyche); de enorme schaal (confrontatie, overweldiging, het 'opslorpen' van de kijker); de donkere kleurpaletten (rouw, angst, depressie, het 'zwarte gat' van de traumatische ervaring). De abstractie was niet slechts esthetisch, maar therapeutisch: een poging om de onuitsprekelijke trauma's van de oorlog in beeld te brengen, te verwerken, te transcenderen."
            }]
        }
    },
    # Add more movements here...
}

# Count what needs to be done
changes_made = []

for movement in data['art_movements']:
    name = movement['name']
    
    # Check if this movement has specific content defined
    if name in movement_content:
        content = movement_content[name]
        
        # Add philosophical_perspective if missing
        if 'philosophical_perspective' not in movement or movement['philosophical_perspective'] is None:
            movement['philosophical_perspective'] = content['philosophical_perspective']
            changes_made.append(f"{name}: philosophical_perspective added")
        
        # Add psychological_perspective if missing
        if 'psychological_perspective' not in movement or movement['psychological_perspective'] is None:
            movement['psychological_perspective'] = content['psychological_perspective']
            changes_made.append(f"{name}: psychological_perspective added")
        
        # Add political_perspective if missing
        if 'political_perspective' not in movement or movement['political_perspective'] is None:
            if 'political_perspective' in content:
                movement['political_perspective'] = content['political_perspective']
                changes_made.append(f"{name}: political_perspective added")

# Save changes
with open('/root/.openclaw/workspace/kunstgeschiedenis/tijdsgeest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Print summary
print(f"✅ Changes made: {len(changes_made)}")
for change in changes_made:
    print(f"  - {change}")

# Verify final status
has_all_count = 0
for movement in data['art_movements']:
    has_all = (
        movement.get('political_perspective') is not None and
        movement.get('philosophical_perspective') is not None and
        movement.get('psychological_perspective') is not None and
        movement.get('literary_context') is not None
    )
    if has_all:
        has_all_count += 1

print(f"\n📊 Final status: {has_all_count}/29 movements have all 4 sections")
