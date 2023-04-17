<!-- 
PDF:
Kjør i terminal fra markdown mappa pandoc .\quizzer\sannsyn\sannsyn.md -f markdown -t pdf --pdf-engine=xelatex --variable=block-headings --toc -o .\quizzer\sannsyn\sannsyn.pdf
HTML:
pandoc .\quizzer\sannsyn\sannsyn.md -f markdown -t html --mathjax --template=template.html --toc -s -H styling.css -o .\quizzer\sannsyn\sannsyn.html
-->

# Sannsynlighet og kombinatorikk

## Øveppgaver

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall,
utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. Alfa 7.10
2. Alfa 7.11

##### Løsningsforslag

Siden $P\left( u_{1} \right) = 0.2$, og $P\left( u_{2} \right) = 0.3$ og
i tillegg
$P(\left\{ u_{1},u_{2},u_{3}\} \right) = 1 = P\left( u_{1} \right) + P\left( u_{2} \right) + P\left( u_{3} \right) = P(u_{3})+0.5$
får vi at $P\left( u_{3} \right) = 0.5$.\

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en
uniform sannsynlighetsmodell.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

1. Alfa 7.14
2. 7.15. Besvarelsen skal begrunnes ved å peke på definisjonen av en
    uniform sannsynlighetsmodell.
3. Et forsøk skal utføres ved å kaste en mynt tre ganger og registrere om det blir kron eller mynt. Henrik setter opp utfallsrommet {tre kron,to kron og en mynt,en kron og to mynt,tre mynt}. Avgjør om dette gir opphav til en uniform sannsynlighetsmodell.

##### Løsningsforslag

3. \
Ved tre kast kan vi registrere hvert kast i rekkefølge. Det gir
mulighetene

- Kron, kron, kron

- Kron, kron, mynt

- Kron, mynt, kron

- Kron, mynt, mynt

- Mynt, kron, kron

- Mynt, kron, mynt

- Mynt, mynt, kron

- Mynt, mynt, mynt,

Totalt 8 mulige utfall. Siden hvert kast gir lik sannsynlighet for kron
og mynt er dette utfallsrommet uniformt. Vi ser her at det er kun ett av de åtte tilfellene som gir kun tre kron, mens det er flere som gir nøyaktig to kron. Dermed kan ikke det opprinnelige utfallsrommet gitt i teksten gi opphav til en uniform

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

1. Du er på hytta og kaster fire femmere på første kast. Med to kast
    igjen bestemmer du deg for å gå for yatzy. Sett opp et utfallsrom
    som gir en uniform sannsynlighetsmodell og finn sannsynligheten for
    at du får yatzy ved hjelp av modellen.

2. André har kjøpt inn 6 lyspærer som han legger i en ekse slik at han slipper å måtte kjøpe nye hver gang en pære går. Uten å tenke seg om byttet André tre lyspærer, men puttet de gamle defekte lyspærene sammen med de nye. Neste gang skal han bytte to pærer og tar han bare to tilfeldige pærer ut fra esken. Sett opp et utfallsrom som gir en uniform sannsynlighetsmodell og avgjør, ved hjelp av modellen, hva sannsynligheten er for at André tar med seg en defekt pære.

##### Løsningsforslag

1. Anta at pærene er nummerert 1 til 6 og la 1, 2 og 3 være defekte. Da er
mulig utfall parene, (1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4),
(2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6) og (5,6). Det er
rimelig å anta at alle parene er like sannsynlige siden vi trekker tilfeldig. Alle parene som inneholder enten $1$, $2$ eller $3$ eller to defekte betyr at André tar med seg en defekt pære. Teller vi opp får vi at sannsynligheten er $\frac{12}{15}$.

2. Vi kan tenke oss at vi uansett kaster to kast, selv om vi får en femmer på første kast. Dette betyr bare at vi har fått yatzy og at det siste kastet ikke har noe å si. Vi kan skrive opp de ulike mulighetene slik:
$$\left\{ \begin{array}{r}
11,12,13,14,15,16, \\
21,22,23,24,25,26, \\
31,32,33,34,35,36, \\
41,42,43,44,45,46, \\
51,52,53,54,55,56, \\
61,62,63,64,65,66 \\
\end{array} \right\}$$

Vi ser her at det er $11$ av de $36$ mulighetene som inneholder en femmer. Dermed er sannsynligheten $\frac{11}{36}$.

### Forklare og bruke store talls lov (Alfa 7.3)

#### Grunnleggende: Forklare store talls lov

Dette læringsmålet gjøres og godkjennes som en gruppeoppgave (på maks
tre personer).

Læringsmålet tar utgangspunkt i aktiviteten fra timen tirsdag 28.03.

*Aktivitet*: Henrik og André gamblet i pauserommet i J-bygget med en mynt de hadde liggende. Henrik hadde valgt kron og André mynt. De bestemte seg at det var førstemann som fikk 5 poeng som vant. Da de kom til stillingen 2-4 ble de «busta» av Ingvald som tok mynten og sa at de må avslutte. Problemet er at det ble lagt inn 3000 kroner i potten. Hvordan skal de fordele pengene?

1. Forklar store talls lov ved hjelp av et eksempel.

#### Middels: Undersøke og estimere sannsynligheter ved å bruke store talls lov

Dette læringsmålet gjøres og godkjennes som en gruppeoppgave (på maks
tre personer).

Læringsmålet tar utgangspunkt i aktiviteten fra timen tirsdag 28.03.

*Aktivitet*: Henrik og André gamblet i pauserommet i J-bygget med en mynt de hadde liggende. Henrik hadde valgt kron og André mynt. De bestemte seg at det var førstemann som fikk 5 poeng som vant. Da de kom til stillingen 2-4 ble de «busta» av Ingvald som tok mynten og sa at de må avslutte. Problemet er at det ble lagt inn 3000 kroner i potten. Hvordan skal de fordele pengene?

1. Forklar store talls lov ved hjelp av et eksempel
2. Ta utgangspunkt i aktiviteten beskrevet over.
   a. Bruk et verktøy (programmering eller excel eller lignende) til å simulere aktiviteten. Dere skal simulere minst 1000 forsøk. Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringen (I Excel betyr dette å få hvordan dette er strukturer og hvilke formler som er brukt og hvorfor dette simulerer den faktiske situasjonen. Hvis det er gjort ved hjelp av programmering det komme fram et skjermutklipp som viser koden).
   b. Bruk resultatene fra forsøkene til å estimere sannsynligheten for at Henrik vinner. Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringen
   c. Anta nå at Henrik og André spilte førstemann til 10 poeng og at de ble avbrutt på stillingen 2-4. Brukt et verktøy til å simulere 1000 forsøk og bruk dette til å estimere sannsynligheten for at Henrik vinner, på samme måte som i a. og b.
       - Hvis Excel brukes så kan "TILFELDIGMELLOM()", "ANTALL.HVIS()" være nyttige funksjoner. Google er også alltid et nyttig verktøy 😉
       - Besvarelsen må ikke bare gjøre et godt estimat av sannsynlighetene. Besvarelsen også må være skrevet og strukturert på en slik måte at leseren kan gjenta simuleringen og få tilsvarende resultater.

#### Avansert: Undersøke, estimere og bruke store talls lov i undervisning

Dette læringsmålet gjøres og godkjennes som en gruppeoppgave (på maks
tre personer).

Læringsmålet tar utgangspunkt i aktiviteten fra timen tirsdag 28.03.

*Aktivitet*: Henrik og André gamblet i pauserommet i J-bygget med en mynt de hadde liggende. Henrik hadde valgt kron og André mynt. De bestemte seg at det var førstemann som fikk 5 poeng som vant. Da de kom til stillingen 2-4 ble de «busta» av Ingvald som tok mynten og sa at de må avslutte. Problemet er at det ble lagt inn 3000 kroner i potten. Hvordan skal de fordele pengene?

1. Forklar store talls lov ved hjelp av et eksempel
2. Ta utgangspunkt i aktiviteten beskrevet over.
   a. Bruk et verktøy (programmering eller excel eller lignende) til å simulere aktiviteten. Dere skal simulere minst 1000 forsøk. Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringen (I Excel betyr dette å få hvordan dette er strukturer og hvilke formler som er brukt og hvorfor dette simulerer den faktiske situasjonen. Hvis det er gjort ved hjelp av programmering det komme fram et skjermutklipp som viser koden).
   b. Bruk resultatene fra forsøkene til å estimere sannsynligheten for at Henrik vinner.Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringe.
   c. Anta nå at Henrik og André spilte førstemann til 10 poeng og at de ble avbrutt på stillingen 2-4. Brukt et verktøy til å simulere 1000 forsøk og bruk dette til å estimere sannsynligheten for at Henrik vinner, på samme måte som i a. og b.
       - Hvis Excel brukes så kan "TILFELDIGMELLOM()", "ANTALL.HVIS()" være nyttige funksjoner. Google er også alltid et nyttig verktøy 😉
        - Besvarelsen må ikke bare gi et godt estimat av sannsynlighetene. Besvarelsen også må være skrevet og strukturert på en slik måte at leseren kan gjenta simuleringen og få tilsvarende resultater.
   d. Gå tilbkae til det originale problemet med først til 5. Undersøk andre utgangsposisjoner enn 2-4 og estimer sannsynligehtene for å vinne ved disse utgangsposisjonene. Presenter sannsynlighetene i på en passende måte.
   e. Vurder arbeidet som er gjort med utgangspunkt i kjerneelementer og
    kompetansemål for niende trinn.

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere
trinn.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer
frem at produktregelen må gjelde (Setning 7.24).

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi eksempler til begrepene

#### Middels: Begrunne at et utvalg er ordnet med og uten tilbakelegg, og finne antall muligheter i utvalget

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

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene uordnet utvalg med og uten tilbakelegg

Forklar og gi eksempler til begrepene

#### Middels: Begrunne at et utvalg er uordnet m/u tilbakelegg, og finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg uten tilbakelegg og finn antall muligheter i utvalgene\
   a. Du har en twistpose med 7 forskjellige twist igjen. Du tar hånden ned i poser og får med deg tre twist.
   b. Det skal trekkes tre heldige ansatte blant 15 ansatte som får et gavekort på 1000 kr hver.
2. Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg med tilbakelegg og finn antall muligheter i utvalgene\
   a.Du skal bestille 3 pizza fra Dolly dimples til deg og vennegjengen på en fredag. Dolly dimples har 5 mulige typer dere kan velge mellom.
   b. Du bestemmer deg for å spise fem frukter hver dag. Du har alltid 5 bananer, 5 pærer, 5 epler og 5 appelsiner liggende.

##### Løsningsforslag

1. Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg uten tilbakelegg og finn antall muligheter i utvalgene
   a. Siden twistene er forskjellige og vi kan trekke en av hver type er dette et utvalg uten tilbakelegg. I tillegg ønsker er det ikke viktig hvilken rekkefølge vi plukker twistene opp i. Det er altså et uordna utvalg. Det gir derfor $7 \cdot 6 \cdot 5$ muligheter for å sette opp et ordna utvalg, men nå overteller vi alle omstokkingene av tre twist. Vi har altså telt alle utvalg $3 \cdot 2 \cdot 1 = 6$ ganger for mye. Totalt gir dette $\frac{7 \cdot 6 \cdot 5}{3 \cdot 2 \cdot 1} = 35$ muligheter.
2. Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg med tilbakelegg og finn antall muligheter i utvalgene
   a.Vi kan velge samme pizza flere ganger, så det er med
   tilbakelegg. I tillegg er rekkefølgen ikke nøye, så det
   er uordnet. Siden det er uordnet kan vi tenke oss at vi
   alltid skriver utvalgene i «stigende» rekkefølge. Dermed
   vi systematisere slik:\
   (1,1,1), (1,1,2), (1,1,3), (1,1,4), (1,1,5),\
   (1,2,2), (1,2,3), (1,2,4), (1,2,5)\
   (1,3,3), (1,3,4), (1,3,5),\
   (1,4,4), (1,4,5),\
   (1,5,5),\
   (2,2,2), (2,2,3), (2,2,4), (2,2,5)\
   (2,3,3), (2,3,4), (2,3,5),\
   (2,4,4), (2,4,5),\
   (2,5,5),\
   (3,3,3), (3,3,4), (3,3,5),\
   (3,4,4), (3,4,5),\
   (3,5,5),\
   (4,4,4), (4,4,5),\
   (4,5,5),\
   (5,5,5).\
   Vi ser altså at det er
   $1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + (1 + 2 + 3 + 4 + 5) = 35$
   muligheter.

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels

Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg m/u
tilbakelegg

1. Du skal velge ut en komité fra en 20 lærerstudenter. Komitéen skal
    bestå av 4 studenter.
2. En klasse med 25 elever skal velge tillitsvalgt. De skal velge to tillitsvalgte. Første elev skal være hovedtillitsvalgt, neste skal være stedfortreder.
3. Hver uke i tre uker har 6 lærere et ukentlig bruslotteri der de vinner en sekspakning Cola hvis de vinner. Det trekkes en vinner blant de 6 lærerne hver uke.
4. Til et lag i $4 \times 100$m stafett er det tatt ut fire sprintere, A, B, C og D. Hvor mange rekkefølger kan de stille opp stafettlaget på?
5. Du har et bord med seks plasser og du skal dekke på til fire. Hvor mange mulige kombinasjoner kan lage?
6. Du skal kjøpe en firepakning med donuts fra Donutsjappa ved Aquarama. De har tre typer donuts du kan velge mellom. Hvor forskjellige firepakninger kan du lage?
7. Du skal trekke ut fire gutter fra en klasse på 16 gutter og 17 jenter. Hvor mange måter kan du gjøre det på?
8. Syv studenter bor i et kollektiv sammen. Den første uke trakker de lodd om hvem som skal lage mat, gjøre rent fellesarealet og vaske badet. Ingen får mer enn én jobb. Hvor mange mulige utfall kan trekningen ha?

##### Løsningsforslag

1. Siden vi ikke kan trekke en student flere ganger, er dette utvalget uten tilbakelegg. I tillegg er det ingen opplysning som impliserer at de skal være distinkte roller i komitéen. Dermed må dette være uordnet (rekkefølge betyr ikke noe)
2. Her ser vi at rollen på personene som trekkes ut har noe å si, og det er dermed et ordnet utvalg. Det er også tydelig at vi ikke kan velge samme elev, og dermed er det et ordnet utvalg uten tilbakelegg.
4. Vi skal velge tre lærere. Det står at det alltids trekkes blant de 6 lærerne, og det er derfor et utvalg med tilbakelegg. Siden det er snakk om en uke mellom utvalgene, så er det naturlig å tolke dette som at rekkefølgen betyr noe. Dermed er dette et ordnet utvalg med tilbakelegg. *Alternativt kan en også argumentere for at rekkefølgen ikke har noe å si siden premien er den samme og vinnerne ikke bryr seg om når de får premien*.
5. Vi kan nummerere setene fra $1$ til $6$, og vi ønsker å velge ut fire av de seks sifrene. Vi kan ikke velge samme siffer to ganger, da dette betyr at vi skal dekke på samme plass to ganger. Dermed er det et utvalg uten tilbakelegg. Siden det å dekke på ikke har noen betydning i forhold til rekkefølgen vi gjør det i, så vil dette være et uordnet utvalg uten tilbakelegg.
6. $\vdots$

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet *og* kombinatorikk)

#### Grunnleggende: Forklare hva union og snitt er

Forklare og illustrere hva union og snitt er.

#### Middels: Forklare og illustrere addisjonssetningen for to mengder 

Forklare og illustrere addisjonssetningen. Pek tydelig på hvorfor det kommer
frem at addisjonsregelen må gjelde (Setning 7.53).

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

1. Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder en toer (minst), men er ikke et partall. Avgjør hvor mange gjenværende muligheter det er
2. André har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder minst én ener og minst én toer. Du regner deg fram til at det er 271 koder som inneholder minst én ener, og 271 koder som inneholder minst én toer. I tillegg er det 512 av de totalt 1000 mulighetene som hverken inneholder enere eller toere. Hvor mange forskjellige koder kan André ha på sin lås?


##### Løsninsgforslag

1. Siden tallet ikke kan være et partall, så kan toer(ne) kun være på første og andre posisjon og på tredje posisjon kan vi velge fritt mellom oddetallene (5 muligheter). Vi begynner med å splitte i tre disjunkte tilfeller:
   1. Enten er det en toer på første posisjon, men ikke på andre. Vi kan altså ha kombinasjonene $2x$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). For hver av de $9$ sifrene kan vi kombintere det med et av fem oddetall. Altså totalt $9\cdot 5 = 45$ muligheter i dette tilfellet.
   2. Eller så er det ikke en toer på første posisjon, men på andre $x2$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). Tilsvarende som over får vi $45$ muligheter. 
   3. Eller $22$. Her er det kun siste siffer som kan endre på seg, og vi har derfor 5 muligheter.
   Siden vi nå har delt mulighetene våre i tre tilfeller som dekker alle mulighetene, og i tillegg ikke overteller noe (er disjunkt), så sier addisjonsprinsippet at antallet er $45+45+5 = 95$.

### Forklare, illustrere og bruke komplementsetningen

#### Grunnleggende: Forklare begrepet komplement

Forklare begrepet komplement gjennom et eksempel

#### Middels: Forklare og illustrere komplementsetningen i sannsynlighet

- Forklare begrepet komplementsetningen ved å illustrere et eksempel
    (setning 7.59)
- Alfa 7.70

#### Avansert: Bruke komplementsetningen for å undersøke problemer

- Alfa 7.72, 7.74.

### Bruke begrepene i temaet til å løse sammensatte problemet

#### Avansert

1. Anta at sannsynligheten for å få en gutt alltid er 1/2. I en familie
    som har to barn er det tre muligheter, to gutter, to jenter eller
    ett av hvert kjønn. Eleven per sier at hvis en velger en tilfeldig
    tobarnsfamilie er det 1/3 sjans for at de har to gutter. André og
    Kristin planlegger å få fem barn.
    1. Hva er sannsynligheten for at de får bare gutter?
    2. Hva er sannsynligheten for at de får to jenter og tre gutter?
    3. Hva er sannsynligheten for at de får minst 2 jenter?
2. I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter,
    ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10
    i tillegg til en knekt, en dame og en konge. Når man spiller bridge
    får man en hånd bestående av 13 tilfeldige kort.
    - Hvor mange av alle de mulige bridgehendene består av åtte
        kløver?
    - Hvor mange ulike bridgehender med nøyaktige fem spar er det
        mulig å dele ut?
    - Hvor mange bridgehender med seks kort i en og samme farge finnes
        det?
    - Hva er sannsynligheten for å få ei slik hånd?
3. Vi trekker ut seks kort av en kortstokk på 52 kort.
    - Hva er sannsynligheten for at det er nøyaktig to spar blant de
        fem?
    - Hva er sannsynligheten for at alle dem fem kortene er kløver?
    - Hva er sannsynligheten for at ruter knekt er med?
    - Hvor stor sannsynlighet er det for at det er to kort med samme
        verdi hånden som deles ut?
4. Vi har et rutenett med $2 \times 5$ ruter. Vi skal først fargelegge
    fire ruter røde og så to gule.
    1. Hvor mange måter kan vi gjøre det på?
    2. Hvordan ville det blitt om vi først velger de to som skal være
        gule, og så de fire som skal være røde?
    3. Hva om vi velger rutene som ikke skal fargelegges, så de fire
        som skal være røde?

## 31.03.23


### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må forklare hva en sannsynlighetsmodell er ved hjelp av begrepene. Besvarelsen må også gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. La et forsøk ha utfallsrommet $U = \{ u_1, u_2, u_3\}$. La $P(u_1) = 0.2$, $P(u_2) = 0.2$ og $P(u_3) = 0.5$. Gjør rede for om dette kan være en sannsynlighetsmodell.

2. La et forsøk ha utfallsrommet $U = \{ u_1, u_2, u_3\}$. La $P(u_1) = 0.2$, $P(u_2) = 0.3$. Begrunn hva $P(\{u_1, u_3\})$ må være for at dette skal være en sannsynlighetsmodell.

##### Vurderingskriterier

1. Studenten må bruke at $P(U) = 1$ og at $P(\{u_1,u_2,u_3\}= P(u_1)+P(u_2)+P(u3)$ noe som ikke stemmer.
2. Studenten kan angripe oppgaven på flere måter. For eksempel kan de først vise at $P(u_3) = 0.5$ og deretter bruke at $P(\{u_1,u_3\}) = P(u_1)+P(u_3) = 0.7$.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må forklare begrepene og gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

André skal kaste en firesidet terning, nummerert 1 til 4. Han skal kaste terningen tre ganger og ønsker å få flest enere. og setter opp utfallsrommet {tre enere, to enere , en ener, ingen enere}. Avgjør om dette gir opphav til en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må begrunne at dette ikke gir opphav til en uniform sannsynlighetsmodell. For eksempel kan studenten peke på at for hvert kast er det mer sannsynlig å noe annet enn en ener. Sluttresultatet må derfor være at det er mindre sannsynlig å få tre enere enn å få ingen enere. Dette betyr at det ikke er en uniform sannsynlighetsmodell.

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

Det er 15 personer i en klasse. Det skal velges ut to elever som skal være i elevrådet og begge to skal trekkes tilfeldig. Henrik vil veldig gjerne være med i elevrådet. Sett opp en uniform sannsynlighetsmodell som får fram at det er $\frac{2}{15}$ sannsynlighet for at Henrik får være med i elevrådet.

##### Vurderingskriterier

Studenten må sette opp et utfallsrom som gir opphav til en uniform sannsynlighetsmodell som viser at sannsynligheten er $\frac{2}{15}$. E naturlig måte å gjøre dette på er for eksempel ved å si at klassen settes opp i en tilfeldig rekkefølge (for eksempel ved loddtrekning). Det gjør at alle elvene har like stor sannsynlighet for å havne på hver av de femten plassene. Hvis det er de to første i rekken som får være med i elevrådet tilsvarer denne måten å trekke ut elevrådsmedlemmene den samme situasjonen som beskrevet i oppgaven. Dermed er det lik sannsynlighet for å havne på en av $15$ plasser, en uniform sannsynlighetsmodell der utfallsrommet er {Henrik havner på første plass, Henrik havner på andre plass, Henrik havner på tredje plass,..., Henrik havner på femtende plass}. Det er kun to av plassene som får han med i elevrådet, dermed $\frac{2}{15}$ sannsynlighet for dette.
