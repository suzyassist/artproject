#!/usr/bin/env python3
"""
Script to add missing philosophical_perspective and psychological_perspective
to all 29 art movements in tijdsgeest.json
"""

import json

# Load the JSON file
with open('/root/.openclaw/workspace/kunstgeschiedenis/tijdsgeest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the new content for each movement
movements_content = {
    "Abstract Expressionisme": {
        "philosophical_perspective": {
            "title": "Existentieel Absolutisme en de Filosofie van het Sublime",
            "sections": [{
                "title": "Existentiële Angst en de Zoektocht naar Betekenis",
                "content": "Het abstract expressionisme ontstond in een tijd van diepe filosofische crisis. De Tweede Wereldoorlog had de verlichtingsidealen van vooruitgang en rationaliteit fundamenteel ondermijnd. Existentialistische filosofen als Jean-Paul Sartre en Martin Heidegger stelden dat het bestaan voorafgaat aan de essentie – de mens moest zijn eigen betekenis creëren in een universum zonder inherente doel. Deze filosofie vertaalde zich direct naar de abstract expressionistische doeken: geen herkenbare voorstellingen, geen duidelijke verhalen, alleen de pure aanwezigheid van verf en handeling. Jackson Pollock's 'drip paintings' werden de visuele equivalent van Sartre's 'existence precedes essence' – het schilderen zelf, de actie, was belangrijker dan het eindresultaat.\n\nDe invloed van Friedrich Nietzsche's concept van het 'sublime' was onmiskenbaar. Waar het pittoreske comfortabel en aangenaam was, confronteerde het sublime de kijker met het oneindige, het onmeetbare, dat wat rede te boven ging. Mark Rothko's enorme kleurvelden – soms drie, vier meter hoog – dwongen de kijker tot een ervaring van het oneindige, van wat Kant het 'mathematisch sublime' noemde. De kijker voelde zich klein, onbeduidend, maar juist in die kleinheid ervoer hij een soort transcendentie. Deze filosofische dimensie maakte abstract expressionisme meer dan decoratie: het was een spirituele oefening, een confrontatie met het absolute.\n\nDe theosofische en mystieke stromingen die via Wassily Kandinsky en Piet Mondrian naar Amerika waren gekomen, beïnvloedden kunstenaars als Rothko, Barnett Newman en Adolph Gottlieb. Newman's 'zips' – verticale lijnen die enorme kleurvelden doorsneden – werden 'totems', 'heilige' symbolen die verwezen naar een pre-linguïstische, pre-culturele spiritualiteit. Deze kunstenaars lazen Mircea Eliade's werken over het 'heilige en het profane', Martin Buber's 'Ich und Du', en de geschriften van de vroege kerkvaders. Hun abstractie was niet leeg, maar geladen met een zoektocht naar het numineuze – dat wat Rudolf Otto had gedefinieerd als 'tremendum et fascinans', het ontzagwekkende én het aantrekkelijke.\n\nDe fenomenologische traditie, ontwikkeld door Edmund Husserl en Maurice Merleau-Ponty, bood een theoretisch kader voor de abstract expressionistische nadruk op directe ervaring. Merleau-Ponty's 'Phénoménologie de la perception' (1945) stelde dat het lichaam, niet het intellect, het primaire medium van kennis was. Deze filosofie rechtvaardigde de fysieke, bijna dansende schildermethode van Pollock, die letterlijk in het doek stapte, verf slingerde, zijn hele lichaam gebruikte. De kunstenaar was geen distant observer, maar een 'being-in-the-world', een term die Heidegger populair had gemaakt.\n\nStijlfiguren die deze filosofische dimensie uitdrukten: de monochromatische vlakken van Rothko en Newman verwezen naar het 'Ene' van Plotinus, de neoplatonische filosoof die stelde dat alle werkelijkheid uit één enkele bron voortkwam; de 'all-over' composities zonder centrum weerspiegelden het existentialistische inzicht dat er geen vaststaande orde bestond, geen hiërarchie, alleen het vlakke, het democratische, het gelijke; de enorme schaal van de doeken dwong de kijker tot een existentiële confrontatie – je kon niet 'kijken naar' het schilderij, je werd erdoor omringd, opgeslokt. Thematisch: de leegte als niet-leegte; het absurde als uitdaging; de vrijheid als verantwoordelijkheid; de dood als confrontatie; het ik als project, niet als gegeven."
            }]
        },
        "psychological_perspective": {
            "title": "Het Onbewuste, Trauma en de Psychologie van de Daad",
            "sections": [{
                "title": "Psychoanalyse, Automatisme en de Verwerking van Oorlog",
                "content": "De psychologische grondslag van het abstract expressionisme lag in de psychoanalytische theorieën van Sigmund Freud en Carl Jung. De Europese surrealisten die naar New York waren gevlucht – André Breton, Max Ernst, Yves Tanguy – hadden de technieken van het 'automatische schrijven' en 'automatische schilderen' meegebracht, direct ontleend aan Freud's concept van 'vrije associatie'. De kunstenaar moest de censuur van het bewuste brein omzeilen, het onbewuste direct laten spreken. Jackson Pollock's 'drip technique' was een variant van deze methode: door de verf niet bewust te plaatsen maar te slingeren, te druppelen, te laten vallen, gaf hij het toeval, het onbewuste, de vrije hand. 'When I am in my painting, I'm not aware of what I'm doing', verklaarde Pollock – een uitspraak die rechtstreeks uit de psychoanalytische traditie kwam.\n\nCarl Jung's concept van het 'collectief onbewuste' en de 'archetypen' beïnvloedde kunstenaars als Rothko, Gottlieb en Newman. Jung stelde dat achter het persoonlijke onbewuste een diepere laag lag, gemeenschappelijk voor alle mensen, bevolkt door universele symbolen – de schaduw, de anima/animus, het zelf. Rothko's geometrische vormen, Newman's 'zips', Gottlieb's 'pictographs' konden worden gelezen als moderne manifestaties van deze archetypen. De kunstenaars lazen Jung's 'Psychology of the Unconscious' (1912) en 'Archetypes and the Collective Unconscious' (1959), en zagen hun werk als visuele talen die toegang gaven tot het universele, niet slechts het persoonlijke.\n\nDe Traumatheorie, die na de Tweede Wereldoorlog enorm in belang toenam, bood een kader voor het begrijpen van abstract expressionisme als verwerkingsmechanisme. Kunstenaars als Arshile Gorky, die de Armeense genocide had overleefd, en Mark Rothko, wiens Joodse familie uit Rusland was gevlucht, droegen collectieve trauma's met zich mee. De abstractie bood een manier om het onuitsprekelijke uit te drukken zonder het te moeten benoemen. Waar realistische kunst de verschrikking zou moeten 'tonen', kon abstracte kunst de emotionele realiteit van trauma overbrengen – de angst, de leegte, de dissociatie – zonder explicititeit. Deze psychologische functie maakte abstract expressionisme tot een vorm van collectieve therapie, niet alleen voor de kunstenaars maar voor de hele naoorlogse samenleving.\n\nDe 'action painting' theorie van Harold Rosenberg, die in 1952 stelde dat het doek een 'arena' was waarin de kunstenaar handelde, benadrukte de psychologische dimensie van het schilderen als daad. Rosenberg, beïnvloed door existentialistische en pragmatistische filosofen als John Dewey, zag het schilderen niet als productie van een object, maar als existentiële handeling. De kunstenaar 'was' wat hij deed – een concept dat rechtstreeks verbonden was met de behavioristische psychologie van B.F. Skinner en de 'self-actualization' theorie van Abraham Maslow. De mens werd gedefinieerd door zijn acties, niet door zijn essentie.\n\nStijlfiguren die deze psychologische dimensie uitdrukten: de zichtbare penseelstreken, de druppels, de spatten maakten het proces van creatie zichtbaar, wat de kijker herinnerde aan de psychologische daad van het schilderen; de lagen verf, soms over elkaar heen geschilderd, suggereerden de lagen van het onbewuste, de herinneringen, de trauma's die onder de oppervlakte lagen; de organische vormen in het werk van Gorky en Willem de Kooning verwezen naar het lichaam, de primal urges, het id van Freud; de geometrische abstractie van Rothko en Newman verwees naar het superego, de behoefte aan orde, aan transcendentie, aan het 'zelf' van Jung. Thematisch: angst als fundamentele toestand; het trauma als onuitwisbaar; het onbewuste als bron; de daad als identiteit; de creatie als catharsis."
            }]
        }
    }
}

# Add content for Abstract Expressionisme (first movement)
for movement in data['art_movements']:
    if movement['name'] == 'Abstract Expressionisme':
        movement['philosophical_perspective'] = movements_content['Abstract Expressionisme']['philosophical_perspective']
        movement['psychological_perspective'] = movements_content['Abstract Expressionisme']['psychological_perspective']
        break

# Save the updated JSON
with open('/root/.openclaw/workspace/kunstgeschiedenis/tijdsgeest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Added philosophical_perspective and psychological_perspective to Abstract Expressionisme")
print("Next: Continue with remaining 28 movements...")
