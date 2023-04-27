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
   b. Det er syv mulige personer som kan få førsteplassen. Når førsteplassen er valgt vil det være 6 mulige personer som kan komme på andre plass, og da 5 personer som kan komme på tredje. Dermed har vi for hver av de syv førsteplassene 6 mulige valg for andreplassen, altså $6$ syv ganger $7\cdot 6$. For hver av de $7\cdot 6$ mulighetene for første *og* andreplasser er det $5$ mulige valg for tredje, altså totalt $7\cdot 6 \cdot 5$ mulige 1.-, 2. og 3. plasser.

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
   a. Vi kan velge samme pizza flere ganger, så det er med
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

##### Løsningsforslag

1. Alfa 7.72
   Hvis vi kaster en mynt fem ganger kan vi for hvert kast få enten kron eller mynt. Dermed vil vi ha $2^5$ forskjellige utfall i forsøket vårt (vi bryr oss om rekkefølge).
   a. Det er kun én måte å få bare kron på. Dermed blir sannsynligheten også $\frac{1}{32}$, siden alle mulige utfall er like sannsynlig og det er $32$ mulige utfall.
   b. Siden det å ikke bare få kron dekker alle andre utfall enn å bare få kron, så må det være $32-1$ mulige utfall som ikke bare gir ikke bare kron. Sannsynligheten blir derfor $\frac{31}{32}$.
   c. Det er på samme måte kun ett utfall som gir bare mynt. Dermed av de totalt $32$ mulighetene så er det $32-2$ som hverken inneholder bare kron eller bare mynt. Sannsynligheten blir derfor $\frac{30}{32}$.

### Bruke begrepene i temaet til å løse sammensatte problemet

#### Avansert

1. Anta at sannsynligheten for å få en gutt alltid er 1/2. I en familie
    som har to barn er det tre muligheter, to gutter, to jenter eller
    ett av hvert kjønn.
    1. Eleven Per sier at hvis en velger en tilfeldig
    tobarnsfamilie er det 1/3 sjans for at de har to gutter. Avgjør om Per tenker rett. Pek på eventuelle misforståelser eller riktige oppfatninger. Hvis det er noen misforståelser må disse rettes opp slik at Per forstår hva som er feil.
    André og Kristin planlegger å få fem barn.
    2. Hva er sannsynligheten for at de får bare gutter?
    3. Hva er sannsynligheten for at de får to jenter og tre gutter?
    4. Hva er sannsynligheten for at de får minst 2 jenter?
2. I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter,
    ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10
    i tillegg til en knekt, en dame og en konge. Når man spiller bridge
    får man en hånd bestående av 13 tilfeldige kort.
    - Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte
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

##### Løsningsforslag

1. Anta at sannsynligheten for å få en gutt alltid er 1/2. I en familie som har to barn er det tre muligheter, to gutter, to jenter eller ett av hvert kjønn.
   1. Eleven Per sier at hvis en velger en tilfeldig
   tobarnsfamilie er det 1/3 sjans for at de har to gutter. Avgjør om Per tenker rett. Pek på eventuelle misforståelser eller riktige oppfatninger. Hvis det er noen misforståelser må disse rettes opp slik at Per forstår hva som er feil.
   \
   - Problemet med utsagnet til Per er mest sannsynlig at han tenker at alle de tre utfallene han lister opp i er like sannsynlige. Hvis vi tegner et utfallstre vil vi se at vi får grenene $\{gg, gj, jg, jj\}$, altså fire utfall. Siden det er lik sannsynlighet for at hver gren skal "skje" så er de fire utfallene like sannsynlige. Vi kan nå vise Per at det derfor er $\frac{1}{4}$ av tilfellene som gir bare gutter og $\frac{1}{4}$ som gir bare jenter, og at i $50\%$ av tilfellene så får vi gutt og jente.
   \
   André og Kristin planlegger å få fem barn.
   2. Hva er sannsynligheten for at de får bare gutter?
   \
   - Vi kan tenke likt som over og se at det er $2^5$ mulige utfall. Det er kun ett av disse som gir kun gutter, så sannsynligheten blir derfor $\frac{1}{32}$.
   \
   3. Hva er sannsynligheten for at de får to jenter og tre gutter?
   \
   - Siden vi vet at det er kun $32$ mulige utfall, kan vi enten telle antallet som inneholder to gutter og tre jenter. Vi kan også tenke slik. Av de fem barnene så skal jeg velge to av dem som skal være gutter. Det er derfor $\frac{5\cdot 4}{2}$ mulige måter å velge ut to gutter av fem barn. Vi har derfor at det er $10$ muligheter for å få nøyaktig to gutter og tre jenter, som gir en sannsynlighet på $\frac{10}{32}$.
   \
   1. Hva er sannsynligheten for at de får minst 2 jenter?
   \
   Vi vet at det er én måte å få ingen jenter (kun gutter), i tillegg er det mulig å få nøyaktig én jente (førstefødte er jente resten gutter, andrefødte er jente resten gutter osv). Dermed er det $6$ utfall som gir mindre enn $2$ jenter. De gjenværende utfallene må derfor være minst to jenter og sannsynligheten blir derfor $\frac{26}{32}$.
   \
2. I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

Vi merker oss først at det er $\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}$ mulige brigdehender man kan ha (vi tenker på dette som et uordnet utvalg uten tilbakelegg, da vi ikke kan ha samme kort på hånden og vi ikke bryr oss om rekkefølgen).

- Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte kløver?
  - Vi ønsker å trekke ut åtte av de tretten kløverne. Dette kan gjøres på $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter. Vi deler på $8\cdot 7 \cdot 6\cdots 3\cdot 2\cdot 1$ fordi vi ikke bryr oss om overtelling, og vi deler derfor dette vekk. Videre må vi nå se på hvor mange måter vi kan trekke ut nøyaktig de fem resterende kortene uten at dette er kløver. Siden det er 13 kort som er kløver er det $39$ kort som ikke er det. Dermed har vi $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$. Vi kan altså for hvert unike utvalg av åtte kløver kombinere dette med $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ andre utvalg som ikke er kløver. Totalt får vi altså (fra multiplikasjonsprinsippet) $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig åtte kløver.
- Hvor mange ulike bridgehender med nøyaktige fem spar er det mulig å dele ut?
  - Tanken her er den samme som i oppgaven over, vi får derfor $\frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36 \cdot 35\cdot 34\cdot 33\cdot 32}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig fem spar.
- Hvor mange bridgehender med nøyaktig seks kort i en og samme farge finnes det?
  - Vi kan først finne antall muligheter for å få seks av samme sort (men allerede nå kan vi merke oss at vi da også teller hender som inneholder for eksempel 6 spar *og* seks ruter). For å få seks hjerter er det $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}$ mulige hender. Siden hjerter ikke var spesielt her, er det generelt $4$ ganger så mange måter å velge ut en sort og få nøyaktig seks av den sorten i en hånd. Problemet nå er at vi overteller noe. Vi overteller alle måter å trekke ut nøyaktig seks av i to sorter. Dette kan gjøres på $6$ måter (hjerter-spar, herter-kløver, hjerter-ruter, spar-kløver, spar-ruter og kløver-ruter). Hver av disse kombinasjonene har $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26$ ulike hender (vi ganger med $26$ fordi det er 26 gjenværende kort som ikke er i de to sortene vi har valgt). Dermed kan vi ved å bruke addisjonssetningen nå si at det er
  $$
  \begin{aligned}
   4\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   \\
   -6\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26
  \end{aligned}
  $$
  mulige hender som inneholder nøyaktig seks av en sort.
- Hva er sannsynligheten for å få ei slik hånd?
  - Sannsynligheten blir dermed gunstige over mulige eller
  $$
  \frac{4\cdot
   \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   -6\cdot\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26}{\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}}
  $$

4. Vi har et rutenett med $2 \times 5$ ruter. Vi skal først fargelegge
    fire ruter røde og så to gule.
   1. Hvor mange måter kan vi gjøre det på?
   - Vi har 10 ruter å velge mellom. Begynner vi med fire ruter i rødt får vi $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}$. Her deler vi på $4\cdot 3\cdot 2\cdot 1$ fordi dette er et uordnet utvalg uten tilbakelegg. Det gjenstår nå 6 ruter vi kan velge til gulfargene. Det gir $\frac{6\cdot 5}{2}$. Multiplikasjonsprinsippet forteller oss nå at det er $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}\cdot \frac{6\cdot 5}{2}$ forskjellige måter å fargelegge 4 av de ti rutene røde og så 2 av rutene gule.
   2. Hvordan ville det blitt om vi først velger de to som skal være gule, og så de fire som skal være røde?
   - Logikken blir lik som over, men fremgangen er noe ulik. Altså først $\frac{10\cdot 9}{2}$ og deretter $\frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ og igjen får vi totalt $\frac{10\cdot 9}{2}\cdot \frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ muligheter.
   3. Hva om vi velger rutene som ikke skal fargelegges, så de fire
        som skal være røde?
   - Her får dere regne selv, men egg merke til at dette gir samme svar som de to oppgavene over.

## 24.04.23

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. La et forsøk ha utfallsrommet $U = { u_1, u_2, u_3, u_4, u_5}$. Hvis $P(\{u_1, u_2, u_3\}) = 0.6$, gi et eksempel på hva $P(\{u_4, u_5\})$ og $P(u_6)$ kan være. Besvarelsen må være begrunnet.

2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4, u_5}$. Forklar at $P(\{u_3\})$ må være større enn $0.4$ hvis $P(\{u_1,u_3\}) = 0.7$ og $P(\{u_2, u,3\}) = 0.7$.  

**Merk** Det var en feil i teksten over der det stod ''Forklar at $P(\{u_3\})$ _ikke kan være_ større enn...''. Dette er rettet i teksten over.

##### Vurderingskriterier

1. Studenten må begrunne påstanden. Her kan de for eksempel bare peke på at $P(U) = 1$ og dermed kan en enkelt bare si at $P(\{u_4, u_5\})$ kan være lik $0.2$, hvis $P(u_6)$ også er lik $0.2$. Dette er fordi en ikke bryter med noen av aksiomene til sannsynlighetsmodeller.
2. Siden $1.4 = 0.7+0.7 = P(\{u_1,u_3\}) + P(\{u_2,u_3\}) = P(u_1)+P(u_2)+2P(u_3)$, ser vi at hvis $P(u_3)$ ikke er større enn $0.4$ så vil $1.4-P(u_3)$ være større enn $1$ samtidig som det vil være lik sannsynligheten for tre enkelutufall i utfallsrommet. Noe som gir en motsigelse.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en riktig forklaring, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

Det er 21 studenter i klassen og de skal deles opp i 7 grupper som alle inneholder 3 studenter. Du trekker kort først og havner på gruppe 1. Neste som trekker er bestevennen din. Det er 20 mulige kort igjen å trekke og to mulige plasser på din gruppe. Bestevennen din sier. Det er to mulige utfall, enten så trekker jeg gruppen din, eller så gjør jeg ikke det. I 10% av tilfellene kommer vi på gruppe, og i 90% av tilfellene gjør vi ikke det. Avgjør og begrunn om modellen som er satt opp er en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må konkludere med at modellen ikke er en uniform sannsynlighetsmodell. Dette kan de enkelt gjøre ved å peke på at hvis det kun er to utfall i utfallsrommet, må det være $50\%$ sjans for hver av utfallene. Dette er det ikke i modellen som er satt opp.

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

Henrik og André spiller et spill der de først kaster en vanlig seksidet terning og deretter en mynt. Vi anter at det er like sannsynlig å få kron og mynt, og at alle seks sidene på terningen er like sannsynlig. Spillet fungerer slik: Når man har kastet en verdi, $n$, på terningen så kaster man mynten. Hvis den lander på mynt, får man dobbler man verdien man fikk på terningen. Kaster man kron får man kun verdien man hadde på terningen.

For eksempel vil et terningkast på 4 og så et kast som gir mynt gi 8 poeng, mens et terningkast på 6 og så en kron vil gi 6 poeng.

1. Sett opp et utfallsrom som gir opphav til en uniform sannsynlighetsmodell.
2. Bruk modellen til å avgjøre hva sannsynligheten er for å få 6 eller flere poeng når man spiller spillet.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan dette gjøres ved å sette opp utfallsrommet $\{1m, 2m, 3m, 4m, 5m, 6m, 1k, 2k, 3k, 4k, 5k, 6k\}$, der siffrene er tallene fra terningskastet og $m$ står får mynt og $k$ står for kron. Studenten kan også tegne opp et utfallstre og peke på at greiene tilsvarer hvert utfall. Studenten må deretter begrunne at modellen er uniform. Det kan de gjøre ved å enkelt peke på at første delforsøk er uniform, slik som det andre delforsøket (myntkastet). Dermed må det være like sannsynlig å få $3m$ som $6k$, siden $3$ og $6$ er like sannsynlig og $m$ og $k$ er like sannsnylig.
2. Studenten kan nå bare telle opp fra utfallsrommet fra forrige oppgave. $3m$, $4m$, $5m$ og $6m$ vil tilsvare en poengverdi på $6, 8, 10$ og $12$. I tillegg vil $6k$ tilsvare en poengverdi på $6$. Det er altså 5 gunstige utfall, noe som gir en sannsynlighet på $\frac{5}{12}$.

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklar med bakgrunn i et eksempel på hva som menes med et sammensatt valg.

##### Vurderingskriterier

Studenten må bruke et eksempel til å forklare hva som menes med et sammensatt valg.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer frem at produktregelen må gjelde.

##### Vurderingskriterier

Studenten må forklare og illustrere produktregelen (Alfa 7.24).

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til:

- et ordnet utvalg med tilbakelegg
- et ordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er ordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget. Du har en krukke med 8 kuler nummerert 1 til 8 og du trekker en kule to ganger for å lage et tall.\
Hver gang du trekker en kule legger du den tilbake og skriver ned sifferet du trakk.
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget. \
Henrik har en kasse med 16 defekte lys og 1 fungerende lys. Han skal skifte lys i stua og satser på at han er heldig og tar med seg 3 lyspærer fra kassa.

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hvert trekk kan trekke mellom de 8 kulene, så vil en ha et utvalg med tilbakelegg. I tillegg skriver man ned siffrene man trekker hver gang for å lage et tall. Dermed er det natulig å tenke at utvalget er ordnet. Siden vi derfor har 8 valg på første trekk og så 8 valg på neste, må det være $8\cdot 8 = 64$ mulige utfall.
2. Studenten må få frem at at en har 17 lys, men ikke kan trekke samme pæren to ganger. For å forklare at det kan tenkes på som ordnet må en peke på at vi bryr oss om rekkefølgen på utvalget, for eksempel fordi Henrik tester pærene han har valgt ut i rekkefølgen han trakk de med seg. *Merk at det er noe kunstig å tolke denne situasjonen som ordnet, da det er mer naturlig å tenke seg at den er uordnet (at man ikke bryr seg om rekkefølgen)*. Siden vi nå tolker dette som et ordnet utvalg uten tilbakelegg så har vi 17 muligheter på første trekk, så 16, så 15. Multiplikasjonsprinsippet forteller oss derfor at det er $17\cdot 16\cdot 15$ mulige utvalg. 

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til

- et uordnet utvalg med tilbakelegg
- et uordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er uordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som uordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget
   - Du har gjester på besøk og har dekket på til seks. Når du skal skjenke Cola innser du at du kun har nok til tre glass. På hvor mange måter kan du velge ut tre av de seks glassene du har dekket på?
2. Begrunn at følgende utvalg er uordnet utvalg med tilbakelegg og finn antall muligheter i utvalget
   - Du og dine venner har dratt til dyreparken og dere rekker tre turer med attraksjoner før dere må dra hjem. Dere kan velge mellom tømmerrenna, jungelboben og fyrtårnet. Hvor mange forskjellige turer.

##### Vurderingskriterier

1. Studenten må forklare at det er uordnet utvalg uten tilbakelegg ved å peke på at vi har seks glass og kun tre av dem skal fylles. Rekkefølgen på når vi fyller glassene er ikke betydelig da det er personene som ikke får Cola som blir opprørt. I tillegg kan man ikke fylle ett glass flere ganger som gir uordna uten tilbakelegg. Hvis det var ordnet ville vi hatt $6\cdot 5\cdot4$ muligheter (siden vi har 6 valg, så 5 valg, så 4 valg). Siden dette er uordnet må vi ta hensyn til overtelling. Siden hvert utvalg kan stokkes om på $3\cdot 2\cdot 1$ måter kan vi dele på $6$ og få $20$ muligheter. 
2. Studenten kan peke på at det går å tenke på dette som tre valg, der en skal velge mellom en av de tre attraksjonene hver gang, altså med tilbakelegg. Når vi velger en attraksjon, men det er ikke noen forskjell på rekkefølgen vi gjør de i. Vi kan systematisere ved å kalle attraksjonene for $0$, $1$ og $2$. Da har vi mulighetene:\
000, 001, 002, 011, 012, 022, 111, 112, 122, 222, altså $10$ muligheter.

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels: Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg med eller uten tilbakelegg

Avgjør om situasjonene under kan tenkes som ordnede eller uordnede utvalg og om utvalgene er med eller uten tilbakelegg:

1. I bedriftsidrettslaget er det 20 medlemmer som spiller basket. På hvor mange måter kan det velges to personer som skal sitte i styret av basketballavdelingen?
2. I en klasse på 18 elever skal det velges ut en elevrådsleder og en vara. På hvor mange måter kan det gjøres på?
3. I en klasse er det 12 gutter og 10 jenter. På hvor mange måter kan man velge ut 4 gutter?
4. En student ved lærerutdanninga har møtt opp på alle obligatoriske undervisninger. Nå gjenstår det fire obligatoriske seminarer, og studenten vil komme over fraværsgrensa på 70% selv om de ikke møter på noen av seminarene. Studenten har derfor konkludert med at de står fritt til å velge om de vil møte opp eller ikke for hver av de fire seminarene. På hvor mange utvalg av seminarer kan de velge å gå på? 

##### Vurderingskriterier

Studenten må argumentere og begrunne sitt valg. Det *må* ikke nødvendigvis stemme med forslaget under, men er det annerledes må begrunnelsen hvertfall være meningsfull!

1. Studenten kan peke på at det ikke sies noe om rollene i styret. Dermed er det naturlig å tenke at dette er et uordna utvalg. Det er heller ikke tilbakelegg siden vi trekker mellom personene og vi ikke kan velge samme person to ganger.
2. Studenten kan peke på at det skal velges roller (ordna), men det skal være forskjellige personer (uten tilbakelegg). 
3. Studenten kan peke på at vi har 12 gutter å velge mellom, men kan ikke velge samme (uten tilbakelegg). Siden det kun er en gruppe er det naturlig å tolke at rekkefølgen ikke har noe å si (uordna)
4. Studenten kan peke på at det skal gjøres fire valg, der de i hvert valg velger mellom å delta og å ikke delta (to muligheter). De trekker mellom disse mulighetene hver gang, så det er med tilbakelegg. I tillegg er rekkefølgen betydelig fordi det avgjør hva slags innhold studenten får (eller ikke får) i seminarene, altså ordna utvalg med tilbakelegg.

### Forklare, illustrere og bruke komplementsetningen

#### Grunnleggende: Forklare begrepet komplement

Forklar begrepet komplement ved hjelp av et eksempel.

#### Middels: Forklare og illustrere komplementsetningen i sannsynlighet

Sannsynligheten for hendelsen $A$ er $0.4$. Forklar, ved hjelp av en illustrasjon, hva $P(A^C)$ er.

##### Vurderingskriterier

Studetnen trenger bare å bruke at $P(A) + P(A^C) = 1$ for å konkludere at $P(A^C) = 0.6$.

#### Avansert: Forklare, illustrere og bruke komplementsetningen i sannsynlighet

Da Henrik var student gikk han i en klasse med 21 studenter. Hver undervisningsøkt deltes de inn i grupper på tre. Henrik hadde fire venner han gjerne ønsket å komme på gruppe med. Hva var synligheten for at Henrik kom på gruppe med minst en av dine venner, når gruppene ble valgt tilfeldig?

##### Vurderingskriterier

Studeten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan en peke på hvilke to som havner på gruppe med Henrik er like sannsynlig. Det er $\frac{20\cdot 19}{2} = 190$ forskjellige mulige klassekammerater som han kan havne på. For å avgjøre hvor mange av de som inneholder minst én, er det naturlig å se på hvor mange som ikke inneholder noen. Av de 20 resterende klassekammeratene er det 16 som ikke er av de fire vennene Henrik ønsker å komme på gruppe med. Derfor er det $\frac{16\cdot 15}{2} = 8\cdot 15 = 120$ grupper som ikke inneholder noen av Henriks venner. Derfor må det være $180 - 120 = 60$ mulige grupper der Henrik er på gruppe med minst én av sine venner. Sannsynligheten er derfor $\frac{60}{190}=\frac{6}{19}$.

### Bruke begrepene i temaet til å løse sammensatte problemer

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 (ess) til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

- Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte kløver?
- Hvor mange ulike bridgehender med nøyaktige fem spar er det mulig å dele ut?
- Hvor mange bridgehender med seks kort i en og samme farge finnes det?
  - Hva er sannsynligheten for å få ei slik hånd?

Du trenger ikke regne ut verdiene. For eksempel holder det å skrive at et antall er $30\cdot 29\cdot 28$.

##### Vurderingskriterier

**Merk** Det stod opprinnelig ikke *nøyaktig* åtte kløver i oppgaveteksten. Derfor godtas flere tolkninger av første deloppgave. I tillegg er det også presisert *nøyaktig* i tredje deloppgave, men denne kunne også tolkes på flere måter. Det er uansett fremgangsmåten og logikken som tas tak i og utgjør om studenten får godkjent eller ikke.

I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

Vi merker oss først at det er $\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}$ mulige brigdehender man kan ha (vi tenker på dette som et uordnet utvalg uten tilbakelegg, da vi ikke kan ha samme kort på hånden og vi ikke bryr oss om rekkefølgen).

- Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte kløver?
  - Vi ønsker å trekke ut åtte av de tretten kløverne. Dette kan gjøres på $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter. Vi deler på $8\cdot 7 \cdot 6\cdots 3\cdot 2\cdot 1$ fordi vi ikke bryr oss om overtelling, og vi deler derfor dette vekk. Videre må vi nå se på hvor mange måter vi kan trekke ut nøyaktig de fem resterende kortene uten at dette er kløver. Siden det er 13 kort som er kløver er det $39$ kort som ikke er det. Dermed har vi $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$. Vi kan altså for hvert unike utvalg av åtte kløver kombinere dette med $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ andre utvalg som ikke er kløver. Totalt får vi altså (fra multiplikasjonsprinsippet) $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig åtte kløver.
- Hvor mange ulike bridgehender med nøyaktige fem spar er det mulig å dele ut?
  - Tanken her er den samme som i oppgaven over, vi får derfor $\frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36 \cdot 35\cdot 34\cdot 33\cdot 32}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig fem spar.
- Hvor mange bridgehender med nøyaktig seks kort i en og samme farge finnes det?
  - Vi kan først finne antall muligheter for å få seks av samme sort (men allerede nå kan vi merke oss at vi da også teller hender som inneholder for eksempel 6 spar *og* seks ruter). For å få seks hjerter er det $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}$ mulige hender. Siden hjerter ikke var spesielt her, er det generelt $4$ ganger så mange måter å velge ut en sort og få nøyaktig seks av den sorten i en hånd. Problemet nå er at vi overteller noe. Vi overteller alle måter å trekke ut nøyaktig seks av i to sorter. Dette kan gjøres på $6$ måter (hjerter-spar, herter-kløver, hjerter-ruter, spar-kløver, spar-ruter og kløver-ruter). Hver av disse kombinasjonene har $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26$ ulike hender (vi ganger med $26$ fordi det er 26 gjenværende kort som ikke er i de to sortene vi har valgt). Dermed kan vi ved å bruke addisjonssetningen nå si at det er
  $$
  \begin{aligned}
   4\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   \\
   -6\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26
  \end{aligned}
  $$
  mulige hender som inneholder nøyaktig seks av en sort.
- Hva er sannsynligheten for å få ei slik hånd?
  - Sannsynligheten blir dermed gunstige over mulige eller
  $$
  \frac{4\cdot
   \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   -6\cdot\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26}{\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}}
  $$

## 17.04.23

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. La et forsøk ha utfallsrommet $U = { u_1, u_2, u_3, u_4, u_5}$. Hvis $P(\{u_1, u_2, u_3\}) = 0.6$, begrunn at $P(\{u_3, u_4, u_5\}) = 0.7$ må bety at $P(u_3) = 0.3$.

2. Henrik var ute på parkeringsplassen på UiA på mandag, tirsdag og onsdag. På mandag registrerte han $50\%$ av bilene som en Tesla. På tirsdag var $40\%$ av de parkerte bilene en Skoda. På onsdagen var $40\%$ Volvo. Henrik konkluderer med at det er $50\%$ sannsynlig at en bil som parkerer på er Tesla, $40\%$ at det er en Skoda og $40\%$ at det er en Volvo. Avgjør om dette kan være en sannsynlighetsmodell.

##### Vurderingskriterier

1. Studenten må begrunne påstanden. Dette kan for eksempel gjøres ved å peke på at
$$
\begin{aligned}
0.6 + 0.7
& = P(\{u_1, u_2, u_3\}) + P(\{u_3, u_4, u_5\})
\\
& = P(\{u_1\})+P(\{u_2\}) + P(\{u_3\}) + P(\{u_3\})+ P(\{u_4\}) + P(\{u_5\})
\\
& = P(\{u_1\})+P(\{u_2\}) + P(\{u_3\})+ P(\{u_4\}) + P(\{u_5\})+ P(\{u_3\})
\\
& =
P(\{u_1, u_2, u_3, u_4, u_5\}) + P(\{u_3\})
\\
& = 1 + P(\{u_3\}).
\end{aligned}
$$
Det betyr at $1.3 = 1 + P(\{u_3\})$, eller at $P(\{u_3\}) = 0.3$
2. Studenten må forklare at dette ikke er en meningsfull sannsynlighetsmodell da summen av sannsynligheten for de forskjellige utfallene blir mer enn $100\%$.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en riktig forklaring, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

1. André skal kaste en sekssidet terning. Han skal kaste terningen en gang og setter opp utfallsrommet $\{1, 2, 3, 4, 5, 6\}$. Avgjør om dette gir en uniform sannsynlighetsmodell.

2. Avgjør og begrunn om det finnes noen sannsynlighetsmodell der $P(u_3) = 0.15$.

##### Vurderingskriterier

1. Studenten må forklare at dette gir opphav til en uniform sannsynlighetsmodell ved å peke på at alle utfallene i utfallsrommet er like sannsynlige.
2. Studenten må konkludere med at dette ikke går an. Dette kan man innse ved å se at siden $0.15 = \frac{3}{20}$, og $3$ ikke går opp i $20$, så vil det ikke finnes et heltall antall utfall som gjør at summen av sannsynlighetene blir $1$.

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

Henrik skal skyte straffespark og har alltid 50% sannsynlighet for å score. Henrik sykter tre ganger.

1. Sett opp et utfallsrom som gir en uniform sannsynlighetsmodell.

2. Avgjør hva sannsynligheten er for at Henrik scorer på nøyaktig to av tre av skuddene.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan dette gjøres ved å sette opp utfallsrommet $\{BBB, BBM, BMB, BMM, MBB, MBM, MMB, MMM\}$, der $B$ står for *bom* og $M$ står for *mål*. Vi ser dermed at det er åtte utfall og siden det er lik sannsynlighet for både mål og bom, så er alle utfallene like sannsynlig.
2. Studenten kan nå bare telle opp fra utfallsrommet fra forrige oppgave. For eksempel ser vi fra 1. at det er utfallene $\{BMM, MBM, MMB\}$ som tilsvarer nøyaktig to mål på tre skudd. Det gir at $P(\text{Henrik scorer på nøyaktig to av tre skudd}) = \frac{3}{8}$.

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklar med bakgrunn i et eksempel på hva som menes med et sammensatt valg.

##### Vurderingskriterier

Studenten må bruke et eksempel til å forklare hva som menes med et sammensatt valg.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer frem at produktregelen må gjelde.

##### Vurderingskriterier

Studenten må forklare og illustrere produktregelen (Alfa 7.24).

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til:

- et ordnet utvalg med tilbakelegg
- et ordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er ordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget
   - Du skal velge en tresifret kode der du kan ha sifrene 1-7 på hver posisjon.
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget
   - En klasse på 15 elever skal sende tre elever på en turnering der én elev skal løpe 200 m, én elev skal hoppe lenge og én elev skal løpe 3000 m. Siden ingen fra klassen har lyst til å delta trekker de lodd om hvem som må gjøre hva.

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hver posisjon kan velge mellom siffrene 1-7 så vil det være med tilbakelegg. Rekkefølgen på en kode er også opplagt viktig, som betyr at utvalget er ordna. Altså et ordna utvalg med tilbakelegg. For å finne antallet kan man bruke produktregelen og se at man har tre valg med 7 muligheter i hvert valg. Det gir $7\cdot 7\cdot 7$ muligheter.
2. Studenten må få frem at elevene kan trekkes ut til forskjellige roller er det er ordnet utvalg, men siden én elev kun skal gjøre en aktivitet er det uten tilbakelegg. For å finne antall muligheter kan man bruke at man skal gjøre tre valg, med $15$ muligheter i første trekk, $14$ i neste og så $13$ i siste valg. Dermed får man $15\cdot 14\cdot 13$ muligheter.

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til

- et uordnet utvalg med tilbakelegg
- et uordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er uordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som uordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget
   - I en klasse på 12 elever skal dere ha innebandyturnering i kroppsøvingen. Du velger ut tre og tre elever. Hvor mange forskjellige lag bestående av tre elever kan man lage?
2. Begrunn at følgende utvalg er uordnet utvalg med tilbakelegg og finn antall muligheter i utvalget
   - Du skal fordele 5 kjeks på to gutter, men begge guttene må ikke få kjeks. På hvor mange måter kan du fordele kjeksene?

##### Vurderingskriterier

1. Studenten må forklare at det er uordnet utvalg uten tilbakelegg ved å peke på at en trekker lag og at det ikke er noe rolle innad i laget. Dermed er det uordnet. Vi må også ha forskjellige elever på laget, som gir et utvalg uten tilbakelegg. For å finne antallet kan en først tenke at det er 3 valg, først 12 muligheter, så 11 og så 10. Altså $12\cdot 11\cdot 10$. Deretter må de ta hensyn til overtellingen. Ved å tenke på for eksempel en gruppe på Arne, Bjarne og Dan, så ser vi at denne kan stokkes om på $3\cdot 2\cdot 1$ mulige måter. Vi overteller altså alle grupper med $6$. Det gir at det er $\frac{12\cdot11\cdot10}{6}=2\cdot 11\cdot 10 = 220$ mulige utvalg.
2. Studenten kan peke på at det går å tenke på dette som fem valg, der en skal velge mellom en av de to guttene hver gang, altså med tilbakelegg. Når vi velger en gutt får han kjeks, men det er ikke noen forskjell på kjeksene, så det er derfor uordnet. Vi kan systematisere ved å kalle guttene for $0$ og $1$. Da har vi mulighetene:\
00000, 00001, 00011, 00111, 01111, 11111, altså $6$ muligheter.

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels: Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg med eller uten tilbakelegg

Avgjør om situasjonene under kan tenkes som ordnede eller uordnede utvalg og om utvalgene er med eller uten tilbakelegg:

1. Til årsmøtet i et lag møter det ti personer. På hvor mange måter kan det velges formann, nestformann og kasserer?
2. I en klasse på 20 elever skal det velges ut en gruppe på 6. På hvor mange måter kan det gjøres på?
3. På hvor mange måter kan forskjellige tresifrede tall lages med sifrene 1, 2, 3, 4 og 6, der en kan gjenta gjenta sifre?
4. På en flervalgsprøve med åtte spørsmål er det tre alternativer på hvert spørsmål, der kun ett alternativ er rett. Hvor mange mulige forskjellige besvarelser kan man gi på prøven?

##### Vurderingskriterier

Studenten må argumentere og begrunne sitt valg. Det *må* ikke nødvendigvis stemme med forslaget under, men er det annerledes må begrunnelsen hvertfall være meningsfull!

1. Studenten må peke på at siden det er forskjellige roller, så vil det være et ordnet utvalg, men siden det ikke er noen som kan være samme rolle så er det uten tilbakelegg.
2. De skal velge en gruppe på $6$ elever. Én elev kan såklart ikke være med flere ganger i gruppen, så det blir uten tilbakelegg. Det er heller ikke påpekt at gruppen inneholder noen roller som gjør det naturlig å tenke på dette som et uordnet utvalg.
3. Det blir påpekt at en kan gjenta sifrene, dermed må det tenkes på som et utvalg med tiblakelegg. Rekkefølgen har noe å si siden vi skal lage tresifrede tall, som gjør det til et ordnet utvalg med tilbakelegg.
4. Siden det er tre muligheter på hvert spørsmål kan en tenke at en på de åtte spørsmålene kan velge mellom 1, 2 og 3, noe som gir et utvalg med tilbakelegg. I tillegg bryr vi oss om rekkefølgen fordi vi ser et mulige besvarelser som kan gis på prøven. Dermed blir dette et ordnet utvalg med tilbakelegg.

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
