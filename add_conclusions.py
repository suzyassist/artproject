#!/usr/bin/env python3
"""
Add conclusion sections to all pages that don't have one
"""
import re

conclusions = {
    'conceptueel.html': {
        'title': 'CONCLUSIE: IDEE BOVEN OBJECT',
        'points': [
            'Dat kunst denken is: Het concept is het kunstwerk, niet het object',
            'Dat taal een medium is: Tekst, instructies, documentatie - woorden worden kunst',
            'Dat de kunstenaar kan verdwijnen: Sommige werken bestaan zonder maker',
            'Dat de kijker mede-schepper is: Zonder participatie is er geen kunst',
            'Dat vraagtekens belangrijker zijn dan uitroeptekens: Twijfel als artistieke strategie'
        ],
        'summary': 'Conceptuele kunst bevrijdde kunst van het object - en stelde de vraag: wat is kunst eigenlijk?'
    },
    'digitaal.html': {
        'title': 'CONCLUSIE: PIXELS ALS PIGMENT',
        'points': [
            'Dat code kunst is: Algoritmes, software, blockchain - technologie als artistiek medium',
            'Dat AI mede-schepper is: Mens en machine creëren samen nieuwe werelden',
            'Dat virtualiteit realiteit is: Digitale ervaringen zijn net zo echt als fysieke',
            'Dat eigendom kan veranderen: NFT\'s herdefiniëren wat "bezitten" betekent',
            'Dat de toekomst nu is: Kunst evolueert sneller dan ooit tevoren'
        ],
        'summary': 'Digitale kunst is de 21e-eeuwse revolutie - waar technologie en creativiteit samensmelten.'
    },
    'expressionisme.html': {
        'title': 'CONCLUSIE: DE KLEUR VAN ANGST',
        'points': [
            'Dat emotie belangrijker is dan realisme: De binnenwereld boven de buitenwereld',
            'Dat kleur kan schreeuwen: Fel, dissonant, pijnlijk - verf als expressie van de ziel',
            'Dat het lichaam kan breken: Vervorming, hoekigheid, maskers - het moderne zelf is gefragmenteerd',
            'Dat oorlog kunst vernietigt: Een generatie kunstenaars ging ten onder in WOI',
            'Dat de stad een nachtmerrie is: Berlijn, Parijs, Wenen - de moderne metropool als angstaanjagend'
        ],
        'summary': 'Het expressionisme was de schreeuw van een wereld die aan stukken ging.'
    },
    'fauvisme.html': {
        'title': 'CONCLUSIE: KLEUR ALS VRIJHEID',
        'points': [
            'Dat kleur autonoom is: Groene bomen? Waarom niet rood! Kleur volgt geen regels',
            'Dat schilderen emotie is: Niet wat je ziet, maar wat je voelt',
            'Dat eenvoud kracht is: Weinig detail, maximum impact',
            'Dat regels er zijn om gebroken te worden: Het Salon des Indépendants was nooit meer hetzelfde',
            'Dat "wilde beesten" complimenten kunnen zijn: Fauves werd een eretitel'
        ],
        'summary': 'Het fauvisme was de korte, explosieve bevrijding van de kleur.'
    },
    'futurisme.html': {
        'title': 'CONCLUSIE: SNELHEID ALS GOD',
        'points': [
            'Dat de toekomst het heden verslindt: Oude kunst, oude steden, oude waarden - allemaal vernietigen',
            'Dat oorlog "de enige hygiëne van de wereld" is: Een gevaarlijke ideologie die fataal afliep',
            'Dat beweging stilstand doodt: Auto\'s, treinen, vliegtuigen - de machine esthetiek',
            'Dat manifesten kunst zijn: Woorden als wapens, pamfletten als schilderijen',
            'Dat kunst politiek kan zijn: Met fatale gevolgen - Marinetti omarmde het fascisme'
        ],
        'summary': 'Het futurisme vierde de moderne tijd - en toont de gevaren van kunst in dienst van ideologie.'
    },
    'hedendaags.html': {
        'title': 'CONCLUSIE: ALLES IS MOGELIJK',
        'points': [
            'Dat er geen regels meer zijn: Globalisering, digitalisering, diversiteit - kunst is alles en overal',
            'Dat identiteit kunst is: Gender, ras, seksualiteit - wie ben ik in de 21e eeuw?',
            'Dat shock waarde heeft: Hirst, Emin, Koons - het schandaal als strategie',
            'Dat de markt meebeslist: Veilinghuizen, beurzen, investeerders - kunst als commodity',
            'Dat kunstenaars activisten zijn: Ai Weiwei, Banksy, Kara Walker - kunst als politiek wapen'
        ],
        'summary': 'Hedendaagse kunst is de kunst van het nu - divers, complex, en onmogelijk in één hokje te vangen.'
    },
    'minimalisme.html': {
        'title': 'CONCLUSIE: WAT JE ZIET IS WAT ER IS',
        'points': [
            'Dat minder meer is: Reductie tot de essentie, geen illusie, geen expressie',
            'Dat het object spreekt: Geen metafoor, geen symboliek - het werk is wat het is',
            'Dat de kijker deelneemt: Ruimte, licht, schaal - de ervaring is het kunstwerk',
            'Dat industriële productie geldt: Geen hand van de meester, wel het oog van de kunstenaar',
            'Dat serialiteit compositie vervangt: Herhaling, systeem, orde - geen romantische genialiteit'
        ],
        'summary': 'Minimalisme was de ultieme reductie - kunst die alles wegliet behalve wat echt essentieel is.'
    },
    'popart.html': {
        'title': 'CONCLUSIE: CAMPBELL\'S SOUP ALS KUNST',
        'points': [
            'Dat consumentencultuur kunst is: Reclame, strips, sterren - de massa als muse',
            'Dat ironie en liefde samengaan: Warhol hield echt van Campbell\'s soup',
            'Dat reproduktie origineel is: Schermprint, serie, kopie - uniek door veelvoud',
            'Dat hoge en lage cultuur samensmelten: MoMA en supermarkt zijn gelijkwaardig',
            'Dat beroemd zijn kunst is: Warhol was zijn eigen kunstwerk'
        ],
        'summary': 'Pop Art vierde en bekritiseerde de consumptiemaatschappij - in felle kleuren en oneindige reeksen.'
    },
    'postmodernisme.html': {
        'title': 'CONCLUSIE: ALLES IS EEN CITAT',
        'points': [
            'Dat er geen grote verhalen meer zijn: Geen vooruitgang, geen waarheid, geen absoluut',
            'Dat ironie de nieuwe ernst is: Speels, skeptisch, zelfbewust - niets is heilig',
            'Dat alles samenstelt: Collage, pastiche, remix - origineel is een mythe',
            'Dat hoge en lage cultuur gelijk zijn: Opera en soap zijn equivalent',
            'Dat de kunstenaar dood is: De auteur is verdwenen, de kijker bepaalt de betekenis'
        ],
        'summary': 'Postmodernisme was het einde van de zekerheden - en het begin van eindeloze mogelijkheden.'
    },
    'rococo.html': {
        'title': 'CONCLUSIE: HET EINDE VAN DE ZON',
        'points': [
            'Dat plezier politiek is: De aristocratie vierde feest terwijl de revolutie naderde',
            'Dat intimiteit majesteit vervangt: Kleine salons, geen grote paleizen',
            'Dat asymmetrie harmonie is: S-vormen, schelpen, natuurlijke curved - de rocaille',
            'Dat pastel kracht is: Roze, blauw, goud - zachtheid als esthetiek',
            'Dat frivoliteit diepgang heeft: Onder de oppervlakte ligt angst voor de toekomst'
        ],
        'summary': 'Rococo was de laatste dans van het ancien régime - mooi, breekbaar, gedoemd.'
    },
    'symbolisme.html': {
        'title': 'CONCLUSIE: HET ONZICHTBARE ZICHTBAAR MAKEN',
        'points': [
            'Dat dromen realiteit zijn: Het onderbewuste, het mystieke, het irrationele',
            'Dat symbolen meer zeggen dan woorden: Een rode roos is liefde, dood, en passie tegelijk',
            'Dat decadentie schoonheid is: Moreau, Redon, Klimt - de schoonheid van het verwordene',
            'Dat kunst ontsnapping is: Weg van de moderne wereld, naar een tijdloze sfeer',
            'Dat mythes eeuwig zijn: Orpheus, Salomé, de dood - archetype als inspiratie'
        ],
        'summary': 'Het symbolisme zocht het goddelijke in het alledaagse - en vond het in droom en mythe.'
    }
}

def add_conclusion(filepath, conclusion_data):
    """Add a conclusion section to an HTML file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if conclusion already exists
    if 'CONCLUSIE' in content:
        return 'already_exists'
    
    # Build conclusion HTML
    points_html = '\n                    '.join([f'<li><strong>{point}</strong></li>' for point in conclusion_data['points']])
    
    conclusion_html = f'''
        <section class="content-section">
            <h2>📚 {conclusion_data['title']}</h2>
            <div class="timeline-box">
                <p>De {conclusion_data['title'].split(':')[1].strip().lower()} leert ons:</p>
                <ul style="margin:1rem 0;padding-left:1.5rem">
                    {points_html}
                </ul>
                <p>{conclusion_data['summary']}</p>
            </div>
        </section>
'''
    
    # Find insertion point: before </main>
    if '</main>' not in content:
        return 'no_main_tag'
    
    # Insert before </main>
    content = content.replace('</main>', conclusion_html + '    </main>')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return 'added'

# Process files
website_dir = '/root/.openclaw/workspace/kunstgeschiedenis/website'

for filename, data in conclusions.items():
    filepath = f'{website_dir}/{filename}'
    result = add_conclusion(filepath, data)
    print(f"  {'✅' if result == 'added' else '⏭️' if result == 'already_exists' else '❌'} {filename}: {result}")

print("\n✅ Done!")
