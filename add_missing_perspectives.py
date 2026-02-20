#!/usr/bin/env python3
"""
Script to add missing philosophical_perspective, psychological_perspective, 
and complete political_perspective to all 29 art movements in tijdsgeest.json
"""

import json

# Load the current file
with open('tijdsgeest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the new perspectives for each movement
# This is organized by movement name

perspectives_data = {
    "Abstract Expressionisme": {
        "philosophical_perspective": {
            "title": "Existentiële Angst en de Filosofie van het Sublieme",
            "sections": [
                {
                    "title": "Existentialisme en de Naoorlogse Crisis",
                    "content": "Het abstract expressionisme ontstond in een tijd van diepe filosofische crisis. De Tweede Wereldoorlog had de Verlichting-idealiteiten van rede, vooruitgang en humanisme ondermijnd. Hoe kon de mensheid, na Auschwitz en Hiroshima, nog geloven in rationele vooruitgang? Filosofen als Theodor Adorno stelden dat 'na Auschwitz geen gedichten meer kunnen worden geschreven' – een sentiment dat abstract expressionisten deelden in hun verwerping van figuratieve, narratieve kunst.\n\nJean-Paul Sartre's existentialisme bood het intellectuele kader. Zijn 'L'Être et le Néant' (1943) stelde dat 'existentie voorafgaat aan essentie': de mens werd zonder vooraf bepaalde aard geboren, en moest zijn eigen betekenis creëren in een betekenisloos universum. Deze filosofie vertaalde zich direct naar abstract expressionistische doeken waar geen herkenbare vormen, geen verhalen, geen 'essentie' was – alleen pure actie, puur bestaan. Mark Rothko verklaarde: 'Ik ben geen abstract kunstenaar. Ik ben geïnteresseerd in basis menselijke emoties – tragedie, extase, ondergang.' Zijn enorme kleurvelden werden visuele equivalenten van existentiële angst en sublieme transcendence.\n\nAlbert Camus' concept van het 'absurde' – de botsing tussen de menselijke zoektocht naar betekenis en het zwijgende universum – vond zijn visuele expressie in de enorme, lege ruimtes van abstract expressionistische doeken. Willem de Kooning's 'Woman' series, met hun vervormde, geagiteerde figuren, verbeeldden de absurditeit van menselijke existentie in een wereld zonder goddelijke garanties. Franz Kline's zwarte en witte composities, geïnspireerd op Japanse kalligrafie, weerspiegelden een Oosterse filosofie van leegte en contemplatie die als alternatief voor Westers rationalisme werd omarmd.\n\nDe invloed van Europese filosofen die naar de VS waren gevlucht – zoals Hannah Arendt, die in 'The Origins of Totalitarianism' (1951) de wortels van het kwaad analyseerde, en Theodor Adorno, die in 'Dialectic of Enlightenment' (1944) de zelfdestructieve tendenzen van moderne rationaliteit bekritiseerde – schiep een intellectueel klimaat van diepe scepsis. Abstract expressionisten deelden deze scepsis, maar vonden in abstractie een manier om te communiceren wat taal niet kon bevatten: de onuitsprekelijke trauma's van de moderne tijd."
                },
                {
                    "title": "Het Sublieme en de Transcendentie",
                    "content": "Het concept van het 'sublieme', ontwikkeld door Edmund Burke en Immanuel Kant in de 18e eeuw, werd herontdekt door abstract expressionisten. Het sublieme was de ervaring van ontzag en angst voor iets dat het begrip te boven ging – de oneindigheid van de oceaan, de grootsheid van bergen, de kracht van stormen. In de 20e eeuw werd het sublieme niet meer in de natuur gezocht, maar in het atoomtijdperk: de nucleaire explosie, de kosmische leegte, de existentiële angst.\n\nBarnett Newman's 'zip' paintings – enorme doeken met een verticale lijn die het vlak doorsneed – werden door de kunstenaar zelf verbonden met het sublieme. 'The sublime is now', verklaarde Newman in 1948, waarmee hij suggereerde dat moderne kunst niet langer het schoone moest nastreven, maar het overweldigende, het grenzeloze. Rothko's kleurvelden, waarin kleuren leken te zweven en te resoneren, creëerden een ruimte voor contemplatie die religieuze ervaring benaderde. Rothko, zelf van Joodse afkomst, weigerde zijn werk te verklaren, maar verklaarde: 'Als mensen alleen door emoties worden geraakt, mis ik het punt. Ik wil ze te pakken nemen en ze in een wereld van emotie en dramatiek sleuren.'\n\nDe nadruk op schaal – de enorme doeken die de kijker moesten omringen, verzwelgen – was een bewuste strategie om het sublieme op te roepen. Waar de Romantiek het sublieme in de natuur had gezocht, zochten abstract expressionisten het in de confrontatie tussen mens en kunstwerk, tussen individueel bewustzijn en grenzeloze ruimte. De 'all-over' compositie – waarbij het hele doek gelijkwaardig behandeld werd, zonder hiërarchie of centraal punt – schiep een visuele metafoor voor een universum zonder center, zonder zin, maar toch doordrenkt van menselijke aanwezigheid."
                },
                {
                    "title": "Stijlfiguren en Filosofische Thema's",
                    "content": "De filosofische stromingen van de tijd vertaalden zich direct naar formele elementen van het abstract expressionisme. De enorme schaal van de doeken weerspiegelde het existentiële besef van menselijke nietigheid tegenover een grenzeloos universum. De 'all-over' compositie, zonder hiërarchie of centraal punt, verbeeldde een wereld zonder inherente betekenis, zonder goddelijke ordening. De nadruk op proces – 'action painting' als 'arena in which to act' – benadrukte het existentialistische idee dat betekenis niet gevonden maar gemaakt werd, dat het schilderen zelf een daad van existentiële zelfbevestiging was.\n\nKleurenpaletten varieerden van monochromatisch (Rothko's diepe rood, Newman's rode 'zips', Ad Reinhardt's 'black' paintings) tot explosieve veelkleurigheid (Pollock's 'drip' paintings met hun web van gekleurde lijnen). Deze kleuren waren niet beschrijvend maar expressief: ze verwezen niet naar de buitenwereld maar naar innerlijke toestanden. De techniek van impasto – dikke verflagen die de hand van de kunstenaar zichtbaar maakten – benadrukte de subjectiviteit, de individuele expressie, die het existentialisme als enige authentieke basis van betekenis erkende.\n\nThematisch verkenden abstract expressionisten: de existentiële angst in een wereld zonder God; de zoektocht naar het sublieme in een gedesacraliseerde moderne tijd; de crisis van betekenis na de Holocaust en de atoombom; de mogelijkheid van authentieke expressie in een 'inauthentieke' consumptiemaatschappij. De kunst werd niet gezien als representatie maar als openbaring – niet als afbeelding van de werkelijkheid, maar als manifestatie van existentiële waarheid."
                }
            ]
        },
        "psychological_perspective": {
            "title": "Het Onbewuste, Trauma en de Psychologie van de Creatie",
            "sections": [
                {
                    "title": "Psychoanalyse en Automatisch Schilderen",
                    "content": "De invloed van Sigmund Freud en Carl Jung op het abstract expressionisme kan niet worden overschat. Freud's theorie van het onbewuste – dat verdrongen herinneringen, verlangens en trauma's bevatte die het bewuste gedrag stuurden – werd omarmd door kunstenaars die toegang zochten tot diepere lagen van de psyche. Surrealisten hadden al geëxperimenteerd met 'automatisch schrijven' en 'automatisch tekenen' – technieken waarbij de hand zonder bewuste controle bewoog, geleid door het onbewuste. Abstract expressionisten namen deze technieken over en ontwikkelden ze verder.\n\nJackson Pollock's 'drip painting' techniek – waarbij hij verf op liggende doeken liet druppen, gieten en slingeren – werd door critici als 'psychisch automatisme' beschreven. Pollock zelf verklaarde: 'When I am in my painting, I'm not aware of what I'm doing.' Deze staat van 'flow', van opgaan in het creatieve proces, was psychoanalytisch geïnspireerd: de kunstenaar moest de censuur van het bewuste ego doorbreken om de diepere lagen van de psyche te bereiken. De resultaten – chaotische webben van lijnen, vlekken en spatten – werden geïnterpreteerd als visuele representaties van het onbewuste zelf.\n\nCarl Jung's concept van het 'collectieve onbewuste' en de 'archetypen' beïnvloedde kunstenaars als Mark Rothko en Barnett Newman. Jung stelde dat alle mensen een gedeelde psychologische erfenis deelden, een reservoir van universele symbolen en patronen die in dromen, mythen en kunst naar boven kwamen. Rothko's abstracte kleurvelden, met hun zwevende, resonante vormen, werden door de kunstenaar zelf verbonden met 'mythische' en 'tragische' thema's die universeel menselijk waren. Newman's 'zip' paintings verwezen naar het scheppingsverhaal, de oorspronkelijke scheiding van licht en donker, een archetypisch motief dat terugging op Jung's theorie van de 'oerbeeld'."
                },
                {
                    "title": "Trauma, Oorlogsneurose en Artistieke Verwerking",
                    "content": "De Tweede Wereldoorlog had diepe psychologische littekens achtergelaten. Vele abstract expressionisten hadden direct of indirect te maken gehad met oorlogstrauma – Pollock was in therapie geweest voor alcoholisme en emotionele instabiliteit, Rothko's Joodse achtergrond maakte hem zich pijnlijk bewust van de Holocaust, De Kooning was als illegale immigrant in de VS kwetsbaar. De naoorlogse psychoanalyse ontwikkelde nieuwe concepten om deze trauma's te begrijpen: 'shell shock' (wat later PTSS zou worden genoemd), 'survivor's guilt', de 'concentration camp syndrome'.\n\nKunst werd een vorm van therapeutische verwerking. De Amerikaanse psychiater Carl Rogers ontwikkelde in de jaren 1940-50 de 'cliëntgerichte therapie', die nadruk legde op zelfexpressie en creativiteit als wegen naar genezing. Martha Graham, de moderne danseres die met abstract expressionisten verkeerde, verklaarde: 'Movement never lies.' Dezelfde overtuiging – dat het lichaam, de hand, de actie een waarheid konden uitdrukken die het bewuste denken verdrong – dreef abstract expressionisten.\n\nDe enorme energie, de fysieke inspanning die nodig was om deze grote doeken te beschilderen, werd een vorm van katharsis – van emotionele zuivering via artistieke expressie. Pollock's 'action painting' was letterlijk fysieke actie: hij bewoog zich om het liggende doek, liet zijn hele lichaam deelnemen aan het schilderen. Deze 'gestural' benadering verwees naar een psychologie van expressie die niet intellectueel maar lichamelijk was – de hand die sprak waar het hoofd zweeg."
                },
                {
                    "title": "Stijlfiguren en Psychologische Thema's",
                    "content": "De psychologische stromingen van de tijd vertaalden zich naar formele elementen van het abstract expressionisme. De 'drip' en 'action painting' technieken weerspiegelden het psychoanalytische idee van automatisme, van kunst als uiting van het onbewuste. De chaotische, niet-gecontroleerde composities verbeeldden de psychedische chaos van het onbewuste zelf – een interne wereld die niet rationeel geordend was, maar associatief, fragmentarisch, droomachtig.\n\nKleuren werden niet gekozen om de werkelijkheid weer te geven, maar om emotionele toestanden uit te drukken. Rothko's diepe rood en donkerpaard evoceren melancholie en tragedie; Newman's 'zip' in helder rood of geel suggereert een moment van doorbraak, van openbaring; Pollock's complexe web van kleuren weerspiegelt de verwarring en energie van het moderne bewustzijn. De schaal van de doeken – vaak groter dan de mens – creëerde een confrontatie die niet alleen visueel maar psychologisch was: de kijker werd verzwolgen door het kunstwerk, net zoals het bewuste ego verzwolgen kon worden door het onbewuste.\n\nThematisch verkenden abstract expressionisten: de diepten van het onbewuste; de verwerking van collectief en individueel trauma; de crisis van identiteit in een gefragmenteerde moderne wereld; de mogelijkheid van authentieke zelfexpressie. De kunst werd niet gezien als product maar als proces – niet als 'object' maar als 'actie', niet als 'representatie' maar als 'onthulling'."
                }
            ]
        }
    },
    # Continue with other movements...
    # Due to the size limit, I'll add them in batches
}

# Now I'll create the complete data structure for ALL movements
# This is a comprehensive update

print("Starting to add missing perspectives to tijdsgeest.json...")
print(f"Total movements to process: {len(data['art_movements'])}")

# Process each movement
movements_updated = []
for movement in data['art_movements']:
    name = movement['name']
    print(f"\nProcessing: {name}")
    
    # Track what was added
    updates = []
    
    # Check if political_perspective is None and needs to be added
    if movement.get('political_perspective') is None:
        print(f"  - political_perspective is NULL, needs to be added")
        updates.append("political_perspective")
    
    # Check for philosophical_perspective
    if 'philosophical_perspective' not in movement or movement.get('philosophical_perspective') is None:
        print(f"  - philosophical_perspective MISSING, will add")
        updates.append("philosophical_perspective")
    
    # Check for psychological_perspective  
    if 'psychological_perspective' not in movement or movement.get('psychological_perspective') is None:
        print(f"  - psychological_perspective MISSING, will add")
        updates.append("psychological_perspective")
    
    if updates:
        movements_updated.append(f"{name}: {', '.join(updates)}")

print(f"\n\nSummary:")
print(f"Total movements: {len(data['art_movements'])}")
print(f"Movements needing updates: {len(movements_updated)}")
for m in movements_updated:
    print(f"  - {m}")

print("\n\nNOTE: This script only analyzes what's missing.")
print("I'll now create the complete updated JSON with all perspectives.")
