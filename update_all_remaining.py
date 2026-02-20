#!/usr/bin/env python3
"""
Complete update script for all remaining movements in tijdsgeest.json
Adds philosophical_perspective and psychological_perspective to all movements
and political_perspective to movements where it's null
"""

import json

# Load the current file
with open('tijdsgeest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper function to create consistent structure
def create_perspective(title, sections_data):
    """
    Create a perspective with title and sections
    sections_data is a list of tuples: [(section_title, section_content), ...]
    """
    return {
        "title": title,
        "sections": [
            {"title": sec_title, "content": sec_content}
            for sec_title, sec_content in sections_data
        ]
    }

# Define all perspectives by movement name
# This is a comprehensive dictionary with all content

all_perspectives = {
    "Art Nouveau": {
        "philosophical_perspective": create_perspective(
            "Symbolisme, Theosofie en de Zoektocht naar Spirituele Harmonie",
            [
                ("Symbolisme en de Ideale Wereld", 
                 "Art Nouveau ontstond in een tijd van filosofische herwaardering. Het symbolisme, met dichters als Charles Baudelaire, Paul Verlaine en Stéphane Mallarmé, had de kunst bevrijd van naturalistische weergave. De symbolisten zochten niet naar de werkelijkheid 'zoals die was', maar naar de 'ideale wereld' erachter, naar de 'absolute waarheden' die verborgen lagen achter de oppervlakte. Deze filosofie vertaalde zich direct naar Art Nouveau: de organische vormen, de vloeiende lijnen, de verfijnde motieven waren geen imitaties van de natuur, maar symbolen van een hogere, spirituele werkelijkheid.\n\nDe invloed van theosofie was enorm. Mme. Blavatsky's 'The Secret Doctrine' (1888) en later Rudolf Steiner's antroposofie stelden dat achter de materiële wereld een spirituele structuur lag, toegankelijk via intuïtie en contemplatie. Kunstenaars als Wassily Kandinsky, die later abstract zou schilderen, en vele Art Nouveau-ontwerpers deelden deze overtuiging: kunst was geen decoratie, maar een weg naar spirituele waarheid. De organische vormen van Art Nouveau – de slingerende lijnen, de spiraalvormige motieven, de asymmetrische composities – werden gezien als 'taal van de ziel', als expressie van een universele levenskracht die door alle dingen stroomde.\n\nDe synthese van kunst en leven, het 'Gesamtkunstwerk' dat Art Nouveau nastreefde, was filosofisch geworteld in een reactie tegen de fragmentatie van de moderne industriële maatschappij. Waar industrialisatie de wereld had opgesplitst in specialismen, zochten Art Nouveau-kunstenaars naar eenheid: architectuur, meubels, textiel, glas-in-lood moesten samensmelten tot één harmonieus geheel. Deze holistische benadering weerspiegelde een filosofisch verlangen naar integratie, naar heelheid, dat parallellen vertoonde met de theosofische en mystieke stromingen van de tijd."),
                ("Estheticisme en de Viering van het Kunstmatige",
                 "Het estheticisme van Oscar Wilde en Walter Pater stelde dat kunst geen morele of utilitaire functie hoefde te hebben – 'All art is quite useless', verklaarde Wilde. Deze 'art for art's sake'-doctrine bevrijdde kunstenaars van de verplichting om nuttig, edifyend of moraliserend te zijn. Art Nouveau omarmde deze filosofie: de weelderige ornamentiek, de verfijnde details, de pure decorativiteit werden gewaardeerd om hun eigen schoonheid, niet om wat ze 'betekenden' of 'leerden'.\n\nTegelijkertijd herontdekten kunstenaars de waarde van ambacht, van 'handwerk' in een tijd van massaproductie. De Arts and Crafts Movement van William Morris had al een terugkeer naar middeleeuwse gilden-tradities bepleit. Art Nouveau zette deze lijn voort: de kunstenaar als ambachtsman, als maker die elk detail zelf controleerde. Deze nadruk op het handgemaakte, het unieke, het niet-reproduceerbare was een filosofisch statement tegen de industrialisering, tegen de vervreemding van arbeider en product.\n\nDe 'femme fatale' – de verleidelijke maar gevaarlijke vrouw die centraal stond in zoveel Art Nouveau-ontwerpen – verwees naar een complexe filosofie van gender en seksualiteit. In een tijd waarin vrouwenrechten streden voor erkenning, verbeeldde Art Nouveau zowel de bevrijding als de angst die deze veranderingen opriepen. De vloeiende, organische vormen van vrouwenfiguren in Art Nouveau werden gevierd als expressie van natuurlijke sensualiteit, maar ook als waarschuwing voor de destructieve kracht van ongeremde passie."),
                ("Stijlfiguren en Filosofische Thema's",
                 "De filosofische stromingen van de tijd vertaalden zich naar formele elementen van Art Nouveau. De organische, vloeiende lijnen weerspiegelden een pantheïstische wereldvisie: de goddelijke kracht die door alle dingen stroomde, van plant tot mens tot kosmos. De asymmetrische composities verwierpen de klassieke harmonie van symmetrie en evenwicht, wat een filosofische breuk betekende met de Renaissance-traditie. De nadruk op ornamentiek en decoratie correspondeerde met het symbolistische ideaal van kunst als suggestie, als evocatie, niet als beschrijving.\n\nKleurenpaletten – gedempt groen, paars, goud en zilver – verwezen naar mystieke en spirituele sferen. De 'whiplash'-lijn, de 'geselende curve' die zo kenmerkend was voor Art Nouveau, werd gezien als visuele vertaling van ritme, van beweging, van de levensstroom zelf. Thematisch verkenden Art Nouveau-kunstenaars: de synthese van kunst en leven; de waarde van het kunstmatige en verfijnde boven het 'natuurlijke'; de zoektocht naar spirituele betekenis in een geseculariseerde wereld; de spanning tussen decadentie en vernieuwing.")
            ]
        ),
        "psychological_perspective": create_perspective(
            "Verlangens, Dromen en de Psychologie van de Decoratie",
            [
                ("Freudiaanse Symboliek en Onderdrukte Verlangens",
                 "De opkomst van de psychoanalyse van Sigmund Freud in de jaren 1890-1900 schiep een nieuw begrip van de menselijke psyche. Freud's theorie van het onbewuste, van verdrongen verlangens die zich via dromen, lapsussen en kunst manifesteerden, bood een kader om Art Nouveau's obsessie met organische vormen, sensuele lijnen en exotische motieven te begrijpen. De 'whiplash'-lijn – de slingerende, zweep-achtige curve – werd geïnterpreteerd als visuele expressie van libido, van levensdrift, van Eros.\n\nDe 'femme fatale' – de verleidelijke maar gevaarlijke vrouw die centraal stond in zoveel Art Nouveau-ontwerpen – verwees naar complexe psychologische dynamieken. In Freudiaanse termen vertegenwoordigde ze de angst voor castratie, de vrees voor vrouwelijke seksualiteit, maar ook het verlangen naar overgave, naar fusie met het andere. De slingerende lijnen, de verstrengelde plantenmotieven, de verfijnde ornamentiek werden gezien als sublimatie: de omzetting van seksuele energie in esthetische vorm.\n\nDe vlucht uit de moderne industriële werkelijkheid – het creëren van 'kunstmatige paradijzen' van verfijnde interieurs en exotische motieven – kon psychologisch worden begrepen als vlucht uit de realiteit, als 'regressie' naar een fantasiewereld. De Art Nouveau-interieur, waar elk detail harmonieus samensmolt tot een 'Gesamtkunstwerk', bood een veilige haven tegen de chaos en fragmentatie van de moderne stad. Deze psychologische functie van kunst – als toevluchtsoord, als droomwereld – was centraal voor de beweging."),
                ("Jungiaanse Archetypen en Collectieve Symbolen",
                 "Carl Jung's theorie van het 'collectieve onbewuste' en de 'archetypen' bood een ander perspectief op Art Nouveau's symboliek. Jung stelde dat alle mensen een gedeelde psychologische erfenis deelden, een reservoir van universele symbolen die in dromen, mythen en kunst naar boven kwamen. De organische vormen van Art Nouveau – de boom des levens, de spiraal, de cirkel, de slang – konden worden begrepen als archetypische symbolen die terugging op de diepste lagen van de menselijke psyche.\n\nDe nadruk op natuurmotieven – varens, lelies, libellen, bloemen – verwees naar een verlangen naar verbinding met de natuurlijke wereld, naar een tijd voor industrialisatie, naar een 'prelapsarian' staat van onschuld. Deze 'regressie' kon psychologisch worden begrepen als reactie op de vervreemding van de moderne tijd: de mens die zichzelf had losgemaakt van de natuurlijke ritmen, zocht via kunst terug te keren naar een organische, harmonieuze wereld.\n\nDe fantasierijke, soms groteske figuren van Art Nouveau – vrouwen met vleugels, hybride wezens van mens en plant, mythische creaturen – verwezen naar de droomwereld, naar het rijk van het onbewuste. Deze wezens waren geen realistische afbeeldingen maar psychologische projecties: manifestaties van diepe verlangens, angsten en aspiraties die het bewuste ik niet direct kon erkennen."),
                ("Stijlfiguren en Psychologische Thema's",
                 "De psychologische stromingen van de tijd vertaalden zich naar formele elementen van Art Nouveau. De vloeiende, organische lijnen weerspiegelden het Freudiaanse concept van libido, van levensenergie die door alle dingen stroomde. De asymmetrische composities verbeeldden een psyche die niet rationeel geordend was, maar associatief, droomachtig. De nadruk op decoratie en ornamentiek correspondeerde met een psychologie van oppervlakte versus diepte, van schijn versus werkelijkheid, van het bewuste versus het onbewuste.\n\nKleurenpaletten – de zachte groenen, paarsen, goudtinten – evoceren een sfeer van droom, van mystiek, van vlucht uit de harde realiteit. De 'whiplash'-lijn werd gezien als visuele vertaling van emotionele intensiteit, van passie, van beweging. Thematisch verkenden Art Nouveau-kunstenaars: de expressie van verdrongen verlangens; de vlucht in fantasie en droom; de zoektocht naar harmonie in een gefragmenteerde wereld; de spanning tussen Eros en Thanatos, tussen levensdrift en doodsdrift.")
            ]
        )
    },
    # Continue with more movements...
}

# I'll continue adding the remaining movements in batches
# For now, let's update Art Nouveau

print("Updating Art Nouveau...")
for i, movement in enumerate(data['art_movements']):
    if movement['name'] == 'Art Nouveau':
        data['art_movements'][i].update(all_perspectives['Art Nouveau'])
        print("  ✓ Added philosophical_perspective")
        print("  ✓ Added psychological_perspective")
        break

# Save progress
with open('tijdsgeest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nProgress saved. Continuing with remaining movements...")
print("Note: Due to the size of this task, I'll continue adding movements in batches.")
