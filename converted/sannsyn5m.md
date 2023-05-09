
#### Middels: Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg,  Øveppgaver

1. Begrunn at følgende situasjoner kan tenkes på som ordnede utvalg med tilbakelegg og finn antall muligheter i utvalgene\
   a. Du skal velge en firesifret kode der du kan ha sifrene 0-9 på hver posisjon.
   b. Du skal kaste en terning tre ganger og skriver opp antall øyne på terningen for hvert kast i kronologisk rekkefølge.
2. Begrunn at følgende situasjoner kan tenkes på som ordnede utvalg uten tilbakelegg og finn antall muligheter i utvalgene\
   a. Du skal stokke om bokstavene i navnet André.
   b. I et skirenn deltar det 7 personer. Du ønsker å skrive opp mulige 1.- 2.- og 3.plasser som kan oppstå.

##### Løsningsforslag

1. Begrunn at følgende situasjoner kan tenkes på som ordnede utvalg med tilbakelegg og finn antall muligheter i utvalgene\
   a. Siden vi skal velge fire posisjoner og vi kan velge hvilket siffer vi vil på hver posisjon har vi alltid 10 sifre og velge mellom. En kan derfor tenke at en mulig kode kan finnes ved å trekke et siffer fire ganger. Skal du låse opp en kode, må vi så klart ta hensyn til rekkefølgen. Derfor får vi et ordnet (fordi rekkefølgen betyr noe) utvalg med tilbakelegg (fordi vi kan velge samme siffer flere ganger). Vi har derfor $10 \cdot 10 \cdot 10 \cdot 10 = 10000$ mulige kombinasjoner vi kan velge.
   b. Vi skal skrive opp antall øyne for hvert kast. Et eksempel kan være (1,3, 6) som betyr 1 på første, 3 på andre og 6 på tredje. Vi ser at rekkefølgen betyr noe, siden (3, 1, 6) betyr 3 på første og 1 på andre. Siden vi hver gang kan slå et tall fra 1 til 6 blir dette også et ordnet utvalg med tilbakelegg, som gir $6 \cdot 6 \cdot 6 = 216$ mulige utfall.
2. Begrunn at følgende utvalg er ordnede utvalg uten tilbakelegg og finn antall muligheter i utvalgene\
   a. Siden vi har fem bokstaver (A, n, d, r, e) som jeg skal stokke om, så kan jeg ikke bruke de flere ganger (uten tilbakelegg). Likevel så bryr jeg meg om rekkefølgen, så det er et ordnet utvalg. Det gir derfor først fem valg, så 4 valg (siden jeg har brukt opp en bokstav), så 3 valg og så videre, altså $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$.
   b. Det er syv mulige personer som kan få førsteplassen. Når førsteplassen er valgt vil det være 6 mulige personer som kan komme på andre plass, og da 5 personer som kan komme på tredje. Dermed har vi for hver av de syv førsteplassene 6 mulige valg for andreplassen, altså $6$ syv ganger $7\cdot 6$. For hver av de $7\cdot 6$ mulighetene for første *og* andreplasser er det $5$ mulige valg for tredje, altså totalt $7\cdot 6 \cdot 5$ mulige 1.-, 2. og 3. plasser.


#### Middels: Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg,  08.05

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget.

- Du er i en vennegjeng på 5 venner. Dere snakker om å gå på kino å se den nye storfilmen "Henrik og André på nye eventyr". Det er ikke sikkert at alle velger å gå på kino, noen velger kanskje at de ikke vil være med. Hvor mange forskjellige grupper fra vennegjengen kan man lage?

2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget.

- I et hesteløp skal er det 8 hester som deltar.  Hvor mange forskjellige kombinasjoner av seierspaller kan man få (seierspallen er de tre første plassene i en konkurranse)?

##### Vurderingskriterier

Studenten må gi en forståelig og riktig begrunnelse i begge oppgavene. I tillegg må de finne antall muligheter i utvalget.

1. Studenten kan peke på at vi kan rangere vennene fra 1-5. Deretter kan vi da avgjøre hvem som skal gå ved å sette opp en 5-tuppel $a_1, a_2, a_3, a_4, a_5$, der de forskjellige a'ene kan være 0 eller 1, hvor 0 betyr at de ikke blir med og 1 betyr at de blir med. For eksempel betyr $0,1,1,0,0$ at venn 1, 4 og 5 ikke blir med, mens venn 2 og 3 blir med. Nå kan en tydelig se at en har fem posisjoner der en kan trekke 0 eller 1 i hvert utvalg (med tilbakelegg) og at rekkefølgen betyr noe siden de ulike posisjonene forteller hvilken venn det er snakk om. Vi ser derfor at vi har $2$ valg fem ganger. Multiplikasjonsprinsippet gir dermed at det er $2^5$ mulige utvalg.
2. Studenten må peke på at én hest ikke kan komme på flere plasser, dermed er det uten tilbakelegg. Det er også forskjell på om hest nummer 8 kommer på 4 eller 1 eller 2 plass, dermed er det ordnet. Vi har dermed $8$ muligheter for første, så $7$, så $6$. Det gir totalt $8\cdot 7\cdot 6$ muligheter.


#### Middels: Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg,  28.04.23

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget.\ Du skal gjøre en flervalgsprøve med fem spørsmål. Hvert spørsmål har fire alternativer. Hvor mange forskjellige besvarelser kan man gjøre på prøven?
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget. \
Til årsmøtet i et lag møter det ti personer. På hvor mange måter kan det velges formann, nestformann og kasserer?

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hvert spørsmål kan velge to alternativer, vi kan tenke på dette som å velge mellom 1 og 2. Dette gjør vi fem ganger og rekkefølgen på besvarelsene er åpenbart viktig. Dermed har vi et ordnet utvalg med tilbakelegg. Vi får derfor $2^5 = 32$ mulige besvarelser.
2. Studenten må peke på at det er forskjellige roller, dermed er det naturlig å tenke på dette som et ordnet utvalg (førstemann er forman, neste er nestformann og tredje er kasserer). Siden vi skal ha tre forskjellige personer er det uten tilbakelegg. Vi får dermed $10\cdot 9 \cdot 8 = 720$ muligheter.


#### Middels: Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg,  24.04.23

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget. Du har en krukke med 8 kuler nummerert 1 til 8 og du trekker en kule to ganger for å lage et tall.\
Hver gang du trekker en kule legger du den tilbake og skriver ned sifferet du trakk.
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget. \
Henrik har en kasse med 16 defekte lys og 1 fungerende lys. Han skal skifte lys i stua og satser på at han er heldig og tar med seg 3 lyspærer fra kassa.

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hvert trekk kan trekke mellom de 8 kulene, så vil en ha et utvalg med tilbakelegg. I tillegg skriver man ned siffrene man trekker hver gang for å lage et tall. Dermed er det natulig å tenke at utvalget er ordnet. Siden vi derfor har 8 valg på første trekk og så 8 valg på neste, må det være $8\cdot 8 = 64$ mulige utfall.
2. Studenten må få frem at at en har 17 lys, men ikke kan trekke samme pæren to ganger. For å forklare at det kan tenkes på som ordnet må en peke på at vi bryr oss om rekkefølgen på utvalget, for eksempel fordi Henrik tester pærene han har valgt ut i rekkefølgen han trakk de med seg. *Merk at det er noe kunstig å tolke denne situasjonen som ordnet, da det er mer naturlig å tenke seg at den er uordnet (at man ikke bryr seg om rekkefølgen)*. Siden vi nå tolker dette som et ordnet utvalg uten tilbakelegg så har vi 17 muligheter på første trekk, så 16, så 15. Multiplikasjonsprinsippet forteller oss derfor at det er $17\cdot 16\cdot 15$ mulige utvalg.


#### Middels: Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg,  17.04.23

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget
   - Du skal velge en tresifret kode der du kan ha sifrene 1-7 på hver posisjon.
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget
   - En klasse på 15 elever skal sende tre elever på en turnering der én elev skal løpe 200 m, én elev skal hoppe lenge og én elev skal løpe 3000 m. Siden ingen fra klassen har lyst til å delta trekker de lodd om hvem som må gjøre hva.

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hver posisjon kan velge mellom siffrene 1-7 så vil det være med tilbakelegg. Rekkefølgen på en kode er også opplagt viktig, som betyr at utvalget er ordna. Altså et ordna utvalg med tilbakelegg. For å finne antallet kan man bruke produktregelen og se at man har tre valg med 7 muligheter i hvert valg. Det gir $7\cdot 7\cdot 7$ muligheter.
2. Studenten må få frem at elevene kan trekkes ut til forskjellige roller er det er ordnet utvalg, men siden én elev kun skal gjøre en aktivitet er det uten tilbakelegg. For å finne antall muligheter kan man bruke at man skal gjøre tre valg, med $15$ muligheter i første trekk, $14$ i neste og så $13$ i siste valg. Dermed får man $15\cdot 14\cdot 13$ muligheter.

