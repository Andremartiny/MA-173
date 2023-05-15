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
får vi at $P\left( u_{3} \right) = 0.5$.

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
mulig utfall parene, (1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6) og (5,6). Det er rimelig å anta at alle parene er like sannsynlige siden vi trekker tilfeldig. Alle parene som inneholder enten $1$, $2$ eller $3$ eller to defekte betyr at André tar med seg en defekt pære. Teller vi opp får vi at sannsynligheten er $\frac{12}{15}$.

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

Dette læringsmålet gjøres og godkjennes som en gruppeoppgave (på maks tre personer).

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

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk)

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
2. Studenten kan tegne opp et Venn-diagram som under og argumentere ved hjelp av dette. Vi ser at å inneholde enten minst én ener eller minst én toer (eller begge) er $1000-512 = 488$. Vi ser også at hvis vi tar $271+271$, så vil vi overtelle snittet mellom de to mengdene tegnet på. Siden addisjonsprinsippet tilsier at $271+271 - \text{ snittet }$ gir oss antall mengder i unionen og at dette skal bli $488$, så må snittet være $542-488 = 52$. Siden det er denne mengden vi er ute etter har vi nå svaret.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/%C3%B8vingl%C3%A5ser.svg)

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

### Bruke begrepene i temaet til å løse sammensatte problemer

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
3. Vi trekker ut fem kort av en kortstokk på 52 kort.
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

3. Vi trekker ut fem kort av en kortstokk på 52 kort.

- Hva er sannsynligheten for at det er nøyaktig to spar blant de fem?
  - Vi kan for eksempel tenke oss at det ikke er viktig hvilken rekkefølge vi trekker ut i (det går også å tenke at rekkefølgen betyr noe). Dermed får vi $\frac{52 \cdot 51 \cdot 50\cdot 49\cdot 48}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ mulige hender vi kan trekke. Videre er det $\frac{13\cdot 12}{2} = 78$ måter å velge to kort som er spar. For hver av de to kortene som er spar, så er det $\frac{39\cdot 38\cdot 37}{3\cdot 2\cdot 1}$ mulige måter å trekke tre kort som ikke inneholder noen spar. Dermed må det, ved multiplikasjonsprinsippet være $78\cdot \frac{39\cdot 38\cdot 37}{3\cdot 2\cdot 1}$ mulige hender som inneholder nøyaktig to spar.
- Hva er sannsynligheten for at alle dem fem kortene er kløver?
  - Vi vet allerede antall mulige hender vi kan trekke. Siden det er $13$ kløver er det $\frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2\cdot 1}$. Dermed er sannsynligheten
$$
\frac{\frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2\cdot 1}}{\frac{52 \cdot 51 \cdot 50\cdot 49\cdot 48}{5\cdot 4\cdot 3\cdot 2\cdot 1}} = \frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{52 \cdot 51 \cdot 50\cdot 49\cdot 48} .
$$
- Hva er sannsynligheten for at ruter knekt er med?
  - En naturlig måte å beregne sannsynligheten er å finne antall hender som ikke inneholder ruter knekt og bruke komplementærsetningen. Det gir $1- \frac{51 \cdot 50\cdot 49\cdot 48\cdot 47}{52 \cdot 51 \cdot 50\cdot 49\cdot 48} = 1- \frac{47}{52}$.
- Hvor stor sannsynlighet er det for at det er to kort med samme verdi hånden som deles ut?
  - På samme måte som i forrige oppgave kan det være naturlig å se på hender som *ikke* inneholder det vi er ute etter. Vi skal trekke ett kort først. Det kan være hva som helst, vi har altså $52$ muligheter. Neste gang vi trekker ønsker vi ikke å trekke verdien vi har fått på første kort. Dermed er det $48$ gunstige kort. Hvis vi sitter med to ulike kort, vil det nå være $44$ gunstige kort vi kan trekke og så videre. Det gir derfor $\frac{52\cdot 48\cdot 44\cdot 40\cdot 36}{5 \cdot 4\cdot 3\cdot 2} = 4\cdot \frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2} =4\cdot 13\cdot 11\cdot 9$. Det gir en sannsynlighet på $1- \frac{4\cdot 13\cdot 11\cdot 9}{52 \cdot 51 \cdot 50\cdot 49\cdot 48}$

1. Vi har et rutenett med $2 \times 5$ ruter. Vi skal først fargelegge
    fire ruter røde og så to gule.
   1. Hvor mange måter kan vi gjøre det på?
   - Vi har 10 ruter å velge mellom. Begynner vi med fire ruter i rødt får vi $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}$. Her deler vi på $4\cdot 3\cdot 2\cdot 1$ fordi dette er et uordnet utvalg uten tilbakelegg. Det gjenstår nå 6 ruter vi kan velge til gulfargene. Det gir $\frac{6\cdot 5}{2}$. Multiplikasjonsprinsippet forteller oss nå at det er $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}\cdot \frac{6\cdot 5}{2}$ forskjellige måter å fargelegge 4 av de ti rutene røde og så 2 av rutene gule.
   1. Hvordan ville det blitt om vi først velger de to som skal være gule, og så de fire som skal være røde?
   - Logikken blir lik som over, men fremgangen er noe ulik. Altså først $\frac{10\cdot 9}{2}$ og deretter $\frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ og igjen får vi totalt $\frac{10\cdot 9}{2}\cdot \frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ muligheter.
   1. Hva om vi velger rutene som ikke skal fargelegges, så de fire
        som skal være røde?
   - Her får dere regne selv, men egg merke til at dette gir samme svar som de to oppgavene over.

## 12.05

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. Hva er galt med denne sannsynlighetsmodellen? $U = \{u_1, u_2, u_3\}$, $P(u_1) = 0,2$, $P(u_2) = 0,3$ og $P(\{u_3\}) = 0.4$?

2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4}$, slik at $P(\{u_1,u_3\}) = 0.6$ og $P(\{u_2, u_3\}) = 0.7$. Kan $P(u_3) =  0.5$?

##### Vurderingskriterier

1. Studenten må peke på at det kun er en sannsynlighetsmodell hvis $1 = P(\{u_1, u_2, u_3\}) = P(u_1) + P(u_2) + P(u_3) = 0.2+0.3+0.4 = 0.9$, men $1$ er jo ikke lik $0.9$.
2. Studenten må undersøke og begrunne (for eksempel ved å gi et konkret tilfelle) at det er mulig at $P(u_3) = 0.5$.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en riktig forklaring, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

Henrik kaster en sekssidet terning og trekker deretter et kort fra en vanlig kortstokk. En vanlig kortstokk inneholder 16 bildekort (knekt, dame, konge og ess) og 36 vanlige kort (kort fra 2 til 10). Henrik setter opp et utfallstre, slik du kan se på bildet under. På utfallstreet har han market at i første omgang kan han få 1 til 6. I neste omgang kan han få enten bildekort eller et kort fra 2 til 10. Det gir totalt $6\cdot 2 = 12$ grener i treet. Forklar hvorfor disse 12 utfallene ikke vil gi opphav til en uniform sannsynlighetsmodell.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/uniform1205sannsyn.svg)

##### Vurderingskriterier

Studenten må peke på problemet med modellen, nemlig at i andre del av utvelgingen, så er det flere kort som ikke er bildekort enn de som er bildekort. Hvis vi antar at alle kortene er like sannsynlige å trekke vil det dermed være mer sannsynlig å slå en ener på terningen og deretter trekke et kort som ikke er bildekort, sammenlignet med å slå en ener på terningen og deretter trekke et bildekort.

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

Følgende oppgave ble gitt på middels:
*Henrik kaster en sekssidet terning og trekker deretter et kort fra en vanlig  kortstokk. En vanlig kortstokk inneholder 16 bildekort (knekt, dame, konge og ess) og 36 vanlige kort (kort fra 2 til 10). Henrik setter opp et utfallstre, slik du kan se på bildet under. På utfallstreet har han market at i første omgang kan han få 1 til 6. I neste omgang kan han få enten bildekort eller et kort fra 2 til 10. Det gir totalt $6\cdot 2 = 12$ grener i treet. Forklar hvorfor disse 12 utfallene ikke vil gi opphav til en uniform sannsynlighetsmodell.*

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/uniform1205sannsyn.svg)

I oppgaven over er det gitt et utfallstre som ikke gir opphav til en uniform sannsynlighetsmodell. Gjør nødvendige endringer for å lage en uniform sannsynlighetsmodell som viser hva sannsynligheten er for å slå en treer eller sekser og samtidig få et bildekort.

##### Vurderingskriterier

Studenten må gjøre endringer som gir opphav til en uniform sannsynlighetsmodell som hjelper de å beregne sannsynligheten. Dette kan for eksempel gjøres ved å peke på at i andre del av utvelgelsen så er det 13 mulige verdier man kan få (som alle er like sannsynlige), men at det kun er fire av de som er bildekort. Dermed er det $6$ mulige utfall ved terningkastet og så $13$ muligheter ved korttrekningen. Det gir totalt $6\cdot 13$ muligheter som har lik sannsynlighet for å skje. Det er derimot kun 2 gunstige i første omgang og for hver av de to mulige utfallene (kaste 3'er eller 6'er), så er det 4 gunstige utfall (trekke bildekort). Det gir dermed $2\cdot 4 = 8$ gunstige muligheter. Sannsynligheten blir dermed $\frac{8}{78}$.

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklar med bakgrunn i et eksempel på hva som menes med et sammensatt valg.

##### Vurderingskriterier

Studenten må bruke et eksempel til å forklare hva som menes med et sammensatt valg.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer frem at produktregelen må gjelde.

##### Vurderingskriterier

Studenten må forklare og illustrere produktregelen (Alfa 7.24). Det viktige er å få fram hvorfor vi får multiplikasjon ved flere valg. Typisk innebærer det å peke på noe sånn som *for hver av de n... får vi m... derfor får vi n m ganger* eller noe liknende.

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Se øveoppgaver

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Se øveoppgaver

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels: Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg med eller uten tilbakelegg

Se øveoppgaver

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk)

#### Grunnleggende: Forklare hva union og snitt er

Forklar begrepene union og snitt ved hjelp av et eksempel.

#### Middels: Forklare og illustrere addisjonssetningen for to mengder (Setning 7.53)

Forklar og illustrere addisjonssetningen for to mengder (Setning 7.53) ved hjelp av et eksempel.

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

André har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder minst én ener og minst én toer. Du regner deg fram til at det er 271 koder som inneholder minst én ener, og 271 koder som inneholder minst én toer. I tillegg er det 512 av de totalt 1000 mulighetene som hverken inneholder enere eller toere. Hvor mange forskjellige koder kan André ha på sin lås?

##### Vurderingskriterier

Se øveoppgaver.

### Forklare, illustrere og bruke komplementsetningen

#### Grunnleggende: Forklare begrepet komplement

Forklar begrepet komplement ved hjelp av et eksempel.

#### Middels: Forklare og illustrere komplementsetningen i sannsynlighet

Du skal spiller et kortspill og er interessert i sannsynligheten for hendelse $A$. Du får vite at $P(A^C) = 0.9$. Hva er $P(A)$?

##### Vurderingskriterier

Studenten må bare bruke komplementsetningen til å peke på at $P(A) + P(A^C) = 1$, noe som gir at $P(A) = 0.1$.

#### Avansert: Forklare, illustrere og bruke komplementsetningen i sannsynlighet

Da Henrik var student gikk han i en klasse med 18 studenter. Hver undervisningsøkt deltes de inn i grupper på tre. Henrik hadde fire venner han gjerne ønsket å komme på gruppe med. Hva var synligheten for at Henrik kom på gruppe med minst en av dine venner, når gruppene ble valgt tilfeldig?

##### Vurderingskriterier

Studenten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan en peke på hvilke to som havner på gruppe med Henrik er like sannsynlig. Det er $\frac{17\cdot 16}{2} = 136$ forskjellige mulige klassekammerater som han kan havne på. For å avgjøre hvor mange av de som inneholder minst én, er det naturlig å se på hvor mange som ikke inneholder noen. Av de 17 resterende klassekammeratene er det 12 som ikke er av de fire vennene Henrik ønsker å komme på gruppe med. Derfor er det $\frac{12\cdot 11}{2} = 66$ grupper som ikke inneholder noen av Henriks venner. Derfor må det være $136 - 66 = 70$ mulige grupper der Henrik er på gruppe med minst én av sine venner. Sannsynligheten er derfor $\frac{70}{136}$.

### Bruke begrepene i temaet til å løse sammensatte problemer

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

Vi trekker ut fem kort av en kortstokk på 52 kort.

- Hva er sannsynligheten for at det er nøyaktig to spar blant de
  fem?
- Hva er sannsynligheten for at alle dem fem kortene er kløver?
- Hvor stor sannsynlighet er det for at det er to kort med samme
  verdi i hånden som deles ut?

##### Vurderingskriterier

Se øveoppgaver.

## 08.05

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. Hva er galt med denne sannsynlighetsmodellen? $U = \{u_1, u_2, u_3\}$, $P(u_1) = 0,5$, $P(u_2) = 0,4$ og $P(\{u_1, u_2\}) = 0.2$?

2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4}$, slik at $P(\{u_1,u_3\}) = 0.6$ og $P(\{u_2, u_3\}) = 0.7$. Kan $P(u_3) =  0.1$?

##### Vurderingskriterier

1. Studenten må peke på at det kun er en sannsynlighetsmodell hvis $0. 2 = P(\{u_1, u_2\}) = P(u_1) + P(u_2) = 0.5+0.4$, men $0.2$ er jo ikke lik $0.9$.
2. Siden $1.3 = 0.6+0.7 = P(\{u_1,u_3\}) + P(\{u_2,u_3\}) = P(u_1)+P(u_2)+2P(u_3)$, ser vi at hvis $P(u_3) = 0.1$ så vil $1.1 = 1.2-P(u_3) = P(u_1)+P(u_2)+2P(u_3)$. Dette gir ingen mening siden $P(u_1)+P(u_2)+2P(u_3)$ ikke kan være større enn $1$ samtidig som det vil være lik sannsynligheten for tre enkelutufall i utfallsrommet. Noe som gir en motsigelse.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en riktig forklaring, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

Se 31.03

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

Det er 18 personer i en klasse. Det skal velges ut tre elever som skal være i elevrådet og alle tre skal trekkes tilfeldig. Henrik vil veldig gjerne være med i elevrådet. Sett opp en uniform sannsynlighetsmodell som får fram at det er $\frac{3}{18}$ sannsynlighet for at Henrik får være med i elevrådet.

##### Vurderingskriterier

Studenten må sette opp et utfallsrom som gir opphav til en uniform sannsynlighetsmodell som viser at sannsynligheten er $\frac{3}{18}$. En naturlig måte å gjøre dette på er for eksempel ved å si at klassen settes opp i en tilfeldig rekkefølge (for eksempel ved loddtrekning), se figur under. Det gjør at alle elvene har like stor sannsynlighet for å havne på hver av de atten plassene. Hvis det er de tre første i rekken som får være med i elevrådet tilsvarer denne måten å trekke ut elevrådsmedlemmene den samme situasjonen som beskrevet i oppgaven. Dermed er det lik sannsynlighet for å havne på en av $18$ plasser, en uniform sannsynlighetsmodell der utfallsrommet er {Henrik havner på første plass, Henrik havner på andre plass, Henrik havner på tredje plass,..., Henrik havner på attende plass}. Det er kun to av plassene som får han med i elevrådet, dermed $\frac{3}{15}$ sannsynlighet for dette.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/08.05.sannsynuniform.svg)

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklar med bakgrunn i et eksempel på hva som menes med et sammensatt valg.

##### Vurderingskriterier

Studenten må bruke et eksempel til å forklare hva som menes med et sammensatt valg.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer frem at produktregelen må gjelde.

##### Vurderingskriterier

Studenten må forklare og illustrere produktregelen (Alfa 7.24). Det viktige er å få fram hvorfor vi får multiplikasjon ved flere valg. Typisk innebærer det å peke på noe sånn som *for hver av de n... får vi m... derfor får vi n m ganger* eller noe liknende.

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til:

- et ordnet utvalg med tilbakelegg
- et ordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er ordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget.

- Du er i en vennegjeng på 5 venner. Dere snakker om å gå på kino å se den nye storfilmen "Henrik og André på nye eventyr". Det er ikke sikkert at alle velger å gå på kino, noen velger kanskje at de ikke vil være med. Hvor mange forskjellige grupper fra vennegjengen kan man lage?

2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget.

- I et hesteløp skal er det 8 hester som deltar.  Hvor mange forskjellige kombinasjoner av seierspaller kan man få (seierspallen er de tre første plassene i en konkurranse)?

##### Vurderingskriterier

Studenten må gi en forståelig og riktig begrunnelse i begge oppgavene. I tillegg må de finne antall muligheter i utvalget.

1. Studenten kan peke på at vi kan rangere vennene fra 1-5. Deretter kan vi da avgjøre hvem som skal gå ved å sette opp en 5-tuppel $a_1, a_2, a_3, a_4, a_5$, der de forskjellige a'ene kan være 0 eller 1, hvor 0 betyr at de ikke blir med og 1 betyr at de blir med. For eksempel betyr $0,1,1,0,0$ at venn 1, 4 og 5 ikke blir med, mens venn 2 og 3 blir med. Nå kan en tydelig se at en har fem posisjoner der en kan trekke 0 eller 1 i hvert utvalg (med tilbakelegg) og at rekkefølgen betyr noe siden de ulike posisjonene forteller hvilken venn det er snakk om. Vi ser derfor at vi har $2$ valg fem ganger. Multiplikasjonsprinsippet gir dermed at det er $2^5$ mulige utvalg.
2. Studenten må peke på at én hest ikke kan komme på flere plasser, dermed er det uten tilbakelegg. Det er også forskjell på om hest nummer 8 kommer på 4 eller 1 eller 2 plass, dermed er det ordnet. Vi har dermed $8$ muligheter for første, så $7$, så $6$. Det gir totalt $8\cdot 7\cdot 6$ muligheter.

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til

- et uordnet utvalg med tilbakelegg
- et uordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er uordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som uordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget

- André skal på ferie med familien. For å gjøre seg klar til turen pakker André ned tre av de seks barnebøkene de har lånt fra biblioteket. Hvor mange forskjellige kombinasjoner av tre barnebøker kan André ta med seg?

2. Begrunn at følgende utvalg er uordnet utvalg med tilbakelegg og finn antall muligheter i utvalget

- Du skal lage en enkel dessert til sommeravslutningen. Du har bestemt deg for å bare kjøpe sørlandsis boksis, og kan velge mellom sjokolade, vanilje og pistasj. Hvis du skal ha fire bokser is, hvor mange forskjellige kombinasjoner av bokser kan du kjøpe med deg til avslutningen?

##### Vurderingskriterier

Studenten må gi en forståelig og riktig begrunnelse i begge oppgavene. I tillegg må de finne antall muligheter i utvalget.

1. Studenten bør peke på at en ikke kan velge samme bok flere ganger (uten tilbakelegg), og at rekkefølgen han velger ut i ikke er av betydning (uordna). Dermed får vi $6\cdot 5\cdot 4$ muligheter, men siden vi ikke bryr oss om rekkefølge så teller vi hvert utvalg $3\cdot 2\cdot 1$ ganger. Vi kan derfor dele på $6$ og se at det er $20$ muligheter.
2. Studenten må begrunne at vi kan velge samme is flere ganger (med tilbakelegg), men at det ikke er viktig hvilken rekkefølge vi velger isen i (uordna). Deretter må de finne utvalget. En naturlig måte vil være å telle på en strukturert måte, for eksempel ved hjelp av en tabell, slik som under. Teller vi over ser vi at det er $15$ mulige utvalg.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/iskrem.svg)

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels: Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg med eller uten tilbakelegg

Avgjør og begrunn om situasjonene under kan tenkes som ordnede eller uordnede utvalg og om utvalgene er med eller uten tilbakelegg:

1. Du skal kjøpe tre kuler is på iskiosken på fiskebrygga. Der har de 12 forskjellige smaker man kan velge mellom.
2. Du skal låne nye bøker på biblioteket. Du ønsker å låne tre nye bøker i temaet "matematikkens historie". På biblioteket har de femten bøker i denne kategorien.
3. André, Henrik og Anders spiller kortspillet *President* på jobben, og har laget en tabell der de holder oversikt over antall seiere per person. Etter å ha spilt seks runder, hvor mange forskjellige stillinger kan oppstå?
4. I underveisvurderingen i MA-173 kan du velge mellom 58 læringsmål. Hvis du svarer på én oppgave på seks forskjellige læringsmål. Hvor mange forskjellige kombinasjoner av seks læringsmål kan du velge?

##### Vurderingskriterier

Studenten må argumentere og begrunne sitt valg. Det *må* ikke nødvendigvis stemme med forslaget under, men er det annerledes må begrunnelsen hvertfall være meningsfull!

1. Studenten kan peke på nesten hvilken tolkning som helst. For eksempel kan de peke på at en selvfølgelig kan velge samme smak flere ganger og at rekkefølgen ikke betyr noe. Dermed blir det uordna utvalg uten tilbakelegg.S
2. En naturlig tolkning kan være å tolke dette som at man har 15 bøker å velge mellom, men man kan ikke velge samme bok flere ganger (uten tilbakelegg). I tillegg er det ikke viktig hvilken rekkefølge man velger i, dermed uordna.
3. En naturlig tolkning kan være å tenke på dette som seks runder der vi kan trekke en vinner mellom de samme tre personene hver gang (med tilbakelegg). Når vi er ferdig er vi ikke interessert i rekkefølgen på resultatet, kun antall ganger noen har vunnet, noe som gjør at vi ikke bryr oss om rekkefølgen (uordna).
4. En naturlig tolkning kan være å argumentere for at vi ikke kan velge samme læringsmål flere ganger (noe som blir pekt på i teksten). I tillegg er det ikke viktig hvolken rekkefølge vi besvarer spørsmålene, altså uordna.

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk)

#### Grunnleggende: Forklare hva union og snitt er

Forklar begrepene union og snitt ved hjelp av et eksempel.

#### Middels: Forklare og illustrere addisjonssetningen for to mengder (Setning 7.53)

Forklar og illustrere addisjonssetningen for to mengder (Setning 7.53) ved hjelp av et eksempel.

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder en toer (minst), men er ikke et partall.

- Avgjør hvor mange gjenværende muligheter det er. Besvarelsen må peke til en illustrasjon som viser hvordan du bruker addisjonssetningen.

##### Vurderingskriterier

Se oppgave 1 øveoppgaver. Merk at oppgaven *må* også inneholde en illustrasjon!

### Forklare, illustrere og bruke komplementsetningen

#### Grunnleggende: Forklare begrepet komplement

Forklar begrepet komplement ved hjelp av et eksempel.

#### Middels: Forklare og illustrere komplementsetningen i sannsynlighet

Du skal spille et kortspill og er interessert i sannsynligheten for hendelse $A$. Du får vite at $P(A^C) = 0.4$. Hva er $P(A)$?

##### Vurderingskriterier

Studenten må bare bruke komplementsetningen til å peke på at $P(A) + P(A^C) = 1$, noe som gir at $P(A) = 0.6$.

#### Avansert: Forklare, illustrere og bruke komplementsetningen i sannsynlighet

Det er 13 gutter og 12 jenter i en klasse. Det skal trekkes en tilfeldig gruppe på tre fra klassen. Hva er sannsynligheten for at man trekker minst én jente?

##### Vurderingskriterier

Studenten må regne ut sannsynligheten på en forståelig måte. Det kan for eksempel gjøres ved å tenke at alle mulige utvalg er like sannsynlige og at det er et uordnet utvalg uten tilbakelegg. Det gir en uniform sannsynlighetsmodell med $\frac{25\cdot 24\cdot 23}{3\cdot 2\cdot 1} = 25\cdot 4\cdot 23 = 2300$ mulige utfall. Vi er nå interessert i hendelsen *minst én jente*. Finner vi sannsynligheten for å velge ut *kun* gutter kan vi bruke at dette er komplementærhendelsen til hendelsen vi er ute etter. Siden det er $\frac{12\cdot 11\cdot 10}{3\cdot 2\cdot 1} ={2\cdot 11\cdot 10} = 220$ mulge utvalg som inneholder kun gutter må sannsynligheten for å trekke minst én jente være $1 - \frac{220}{2300}$.

### Bruke begrepene i temaet til å løse sammensatte problemer

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

Studentene i MA-173 holder på med aktiviteter for å undersøke sannsynlighetsmodeller. I en oppgave kastet de to terninger og ganget tallene de fikk, med hverandre. De brukte vanlige spillterninger med tallene 1–6. Henrik kastet terningene flere ganger, og syntes han fikk mistenkelig mange svar som var partall. Han spurte læreren hva grunnen kunne være.

1. Hva ville du som lærer ha svart Henrik?
2. Hva er sannsynligheten for å få partall som svar når vi ganger tallene vi får på terningene, med hverandre?
3. Hvis vi kaster terningene fire ganger, hva er sannsynligheten for å få partall som svar på gangestykket alle gangene?
4. Hva er sannsynligheten for å få partall som svar to ganger og oddetall to ganger?

##### Vurderingskriterier

Studenten må besvare *alle* spørsmålene på en rimelig måte.

1. Her finnes ingen eksakt fasit, men en besvarelse bør inneholder noe som peker på og *begrunner* hvorfor dette er tilfellet. Det kan for eksempel være ved å lage en tabell som viser de ulike mulige utfallene, som under.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/terningkast0805.svg)
I tabellen kan man se at det er 27 av de 36 mulige utfallene som gir et partall. Dette kan også forklares ved at en kun får oddetall ved at begge terningene slår oddetall. Det er kun 3 mulige utfall i begge terningkastene, altså totalt $9$ forskjellige utfall som gir oddetall.
2. Svaret bør allerede være argumenter for i oppgave 1. Sannsynligheten er $\frac{27}{36}= \frac{3}{4}$.
3. Her kan studenten ty til multiplikasjonsprinsippet. Det er $27$ mulige gunstige utfall i hvert av de fire kastene, dermed $27^4$ mulige gunstige utfall. Totalt er det $36^4$ mulige utfall (36 utfall i hvert enkeltkast). Siden alle mulige utfall er like sannsynlige får vi en sannsynlighet på $\frac{27^4}{36^4}$.
4. Studenten kan for eksempel bruke at dette kan skje på følgende måter $OOPP$, $OPOP$, $OPPO$, $POOP$, $POPO$ og $PPOO$, der $P$ er partall og $O$ er oddetall. Hver av disse seks mulige rekkefølgene er like sannsynlige, så vi må bare finne sannsynligheten for hver av de. Vi kan for eksempel ta for oss $OOPP$ og se at vi er på utkikk etter antall muligheter som gir oddetall, så oddetall, så partall så partall. Vi vet nå at dette betyr at det er $9$ muligheter, så $9$, så $27$ så $27$. Totalt gir multiplikasjonsprinsippet at det er $9\cdot 9 \cdot 27\cdot 27$ mulige måter for å først få oddetall, så oddetall så partall så partall. Sannsynligheten for $OOPP$ blir da $\frac{9^2\cdot 27^2}{36^4}$. Siden dette også er sannsynligheten for alle mulige utfallene får vi en sannsynlighet for å få nøyaktig to oddetall og to partall ved fire kast lik $6\cdot \frac{9^2\cdot 27^2}{36^4}$.

## 28.04.23

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. Hva er galt med denne sannsynlighetsmodellen? $U = \{u_1, u_2, u_3\}$, $P(u_1) = 0,5$, $P(u_2) = 0,4$ og $P(u_3) = 0.2$?
2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4, u_5}$. Forklar at $P(\{u_3\})$ må være større enn $0.2$ hvis $P(\{u_1,u_3\}) = 0.8$ og $P(\{u_2, u_3\}) = 0.4$.  

##### Vurderingskriterier

1. Studenten må begrunne påstanden. Ved å peke på at summen av sannsynlighetene for enkeltutfallene er større enn $1$, ser vi at vi at det ikke kan være en sannsynlighetsmodell.
2. Siden $1.2 = 0.4+0.8 = P(\{u_1,u_3\}) + P(\{u_2,u_3\}) = P(u_1)+P(u_2)+2P(u_3)$, ser vi at hvis $P(u_3)$ er mindre enn $0.2$ så vil $1.2-P(u_3)$ være større enn $1$ samtidig som det vil være lik sannsynligheten for tre enkelutufall i utfallsrommet. Noe som gir en motsigelse.

### Forklare og bruke begrepet uniform sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepet

Forklar hva en uniform sannsynlighetsmodell er og gi et eksempel på en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en riktig forklaring, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en uniform sannsynlighetsmodell

Et forsøk skal utføres ved å kaste en mynt tre ganger og registrere om det blir kron eller mynt. Henrik setter opp utfallsrommet {tre kron,to kron og en mynt,en kron og to mynt,tre mynt}. Avgjør om dette gir opphav til en uniform sannsynlighetsmodell.

##### Vurderingskriterier

Se øveoppgave 3.

#### Avansert: Sette opp uniforme sannsynlighetsmodeller fra en gitt situasjon

André har en firesidet terning på kontoret sitt, der det er like sannsynlig å slå 1, 2, 3 og 4. André kaster to ganger og multipliserer verdiene han fikk.

1. Sett opp en modell som gir opphav til en uniform sannsynlighetsmodell.
2. Avgjør ved hjelp av modellen hva sannsynligheten er for at André får mer enn 7 når han har slått begge terningene.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan de tegne et trediagram som dette

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/utfallstre.png)

Dette kan de bruke til å peke på at grenene helt nederst viser utfallene. Studenten kan også lage en tabell
$$
\begin{array} {|r|r|r|r|r|r|}\hline  & \text{Første kast} & 1 & 2 & 3 & 4
\\
\hline
\text{Andre kast}
\\ \hline  
1 & & 1,1 & 2,1 & 3,1 & 4,1
\\ \hline  
2 & & 1,2& 2,2 & 3,2 & 4,2
\\ \hline
3 & & 1,3 & 2,3 & 3,3 & 4,3
\\ \hline
4 & & 1,4 & 2,4 & 3,4 & 4,4
\\ \hline
\end{array}
$$

Uansett, så ser vi at siden alle utfallene fra hver terning er like sannsynlig er det også naturlig at alle 16 utfallene i treet/tabellen er like sannsynlig. Dermed er dette en uniform annsynlighetsmodell.
b. De kan nå telle over utfallene som gir mer enn $7$ og se for eksempel se at i tabellen så er det alle som ligger nedenfor den ene diagonalen. Det er altså $6$ utfall som gir mer enn $7$, så dermed er det $\frac{6}{16}$  sannsynlighet for å få mer enn $7$ når en tar produktet av begge terningkastene.

### Forklare, illustrere og bruke produktregelen

#### Grunnleggende: Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere trinn

Forklar med bakgrunn i et eksempel på hva som menes med et sammensatt valg.

##### Vurderingskriterier

Studenten må bruke et eksempel til å forklare hva som menes med et sammensatt valg.

#### Middels: Forklare og illustrere produktregelen

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer frem at produktregelen må gjelde.

##### Vurderingskriterier

Studenten må forklare og illustrere produktregelen (Alfa 7.24). Det viktige er å få fram hvorfor vi får multiplikasjon ved flere valg. Typisk innebærer det å peke på noe sånn som *for hver av de n... får vi m... derfor får vi n m ganger* eller noe liknende.

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til:

- et ordnet utvalg med tilbakelegg
- et ordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er ordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som ordnet utvalg med tilbakelegg og finn antall muligheter i utvalget.\ Du skal gjøre en flervalgsprøve med fem spørsmål. Hvert spørsmål har fire alternativer. Hvor mange forskjellige besvarelser kan man gjøre på prøven?
2. Begrunn at følgende utvalg er ordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget. \
Til årsmøtet i et lag møter det ti personer. På hvor mange måter kan det velges formann, nestformann og kasserer?

##### Vurderingskriterier

1. Studenten må få fram at siden vi for hvert spørsmål kan velge to alternativer, vi kan tenke på dette som å velge mellom 1 og 2. Dette gjør vi fem ganger og rekkefølgen på besvarelsene er åpenbart viktig. Dermed har vi et ordnet utvalg med tilbakelegg. Vi får derfor $2^5 = 32$ mulige besvarelser.
2. Studenten må peke på at det er forskjellige roller, dermed er det naturlig å tenke på dette som et ordnet utvalg (førstemann er forman, neste er nestformann og tredje er kasserer). Siden vi skal ha tre forskjellige personer er det uten tilbakelegg. Vi får dermed $10\cdot 9 \cdot 8 = 720$ muligheter.

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi et eksempel til

- et uordnet utvalg med tilbakelegg
- et uordnet utvalg uten tilbakelegg

##### Vurderingskriterier

Studenten må gi eksempler som de blir bedt om, og de må forklare hva et ordnet utvalg med og uten tilbakelegg er.

#### Middels: Begrunne at et utvalg er uordnet og om det er med eller uten tilbakelegg, samt finne antall muligheter i utvalget

1. Begrunn at følgende situasjoner kan tenkes på som uordnet utvalg uten tilbakelegg og finn antall muligheter i utvalget
   - I en klasse på 20 elever skal det velges ut en gruppe på 6. På hvor mange måter kan det gjøres på?
2. Begrunn at følgende utvalg er uordnet utvalg med tilbakelegg og finn antall muligheter i utvalget
   - Du og tre venner spiller yatzee på hytta. Dere spiller to runder og holder oversikt over hvor mange runder hver person vinner. Hvor mange forskjellige kombinasjoner av vinnere kan vi ha?

##### Vurderingskriterier

1. Studenten må forklare at det er uordnet utvalg uten tilbakelegg ved å peke på at en trekker lag og at det ikke er noe rolle innad i laget. Dermed er det uordnet. Vi må også ha forskjellige elever på laget, som gir et utvalg uten tilbakelegg. For å finne antallet kan en først tenke at det er 3 valg, først 20 muligheter, så 19 og så 18. Altså $20 \cdot 19 \cdot 18$. Deretter må de ta hensyn til overtellingen. Ved å tenke på for eksempel en gruppe på Arne, Bjarne og Dan, så ser vi at denne kan stokkes om på $3\cdot 2\cdot 1$ mulige måter. Vi overteller altså alle grupper med $6$. Det gir at det er $\frac{20\cdot 19\cdot 18}{6}=3\cdot 20\cdot 19 = 3\cdot 380 = 1140$ mulige utvalg.
2. Studenten kan peke på at vi trekker mellom de fire vennene. Siden de kan vinne mer enn en gang, har vi like mange valg hver gang, altså utvalg med tilbakelegg. Vi bryr oss derimot ikke når vi vinner, bare hvor mange ganger vi vinner (uordna). Vi kan telle oss fram til mulighetene. La oss nummerere vennene fra 1 til 4. Det gir mulighetene $11$, $12$, $13$, $14$, $22$, $23$, $24$, $33$, $34$, $44$, altså 10 muligheter.

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels: Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg med eller uten tilbakelegg

Avgjør og begrunn om situasjonene under kan tenkes som ordnede eller uordnede utvalg og om utvalgene er med eller uten tilbakelegg:

1. Du blir bedt om å lage et passord med lengde på $8$ symboler. Du kan velge mellom bokstavene i alfabetet og sifrene fra $0$ til $9$.
2. Du har 8 bøker som skal sette i hylla. På hvor mange måter kan du gjøre det?
3. I et hesteløp skal er det 8 hester som deltar. Du vedder på å treffe på både første-, andre- og tredjeplass. Hvor mange forskjellige kombinasjoner av pallplasser kan man få?
4. I et spill med poker har man en hånd med 2 kort som du kan se og stokke på. Hvor mange forskjellige hender kan du ha?

##### Vurderingskriterier

Studenten må argumentere og begrunne sitt valg. Det *må* ikke nødvendigvis stemme med forslaget under, men er det annerledes må begrunnelsen hvertfall være meningsfull!

1. Siden man alltid kan velge mellom de samme bokstavene og sifrene er det med tilbakelegg. Rekkefølgen man skriver inn et passord har noe å si, så det er ordnet. Vi har altså et ordnet utvalg med tilbakelegg.
2. Du kan plassere bøkene i en bestemt rekkefølge for hver gang, altså ordnet. Siden vi heller ikke kan plassere samme bok flere ganger får vi et ordnet utvalg uten tilbakelegg.
3. Rekkefølgen har noe å si (ordnet) og hestene kan ikke komme på mer enn én plass. Dermed er det ordnet uten tilbakelegg.
4. Siden vi kan stokke om på kortene blir det uordnet. Vi kan heller ikke ha samme kort to ganger. Dermed blir det uordnet utvalg uten tilbakelegg.

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk)

#### Grunnleggende: Forklare hva union og snitt er

Forklar begrepene union og snitt ved hjelp av et eksempel.

#### Middels: Forklare og illustrere addisjonssetningen for to mengder (Setning 7.53)

Forklar og illustrere addisjonssetningen for to mengder (Setning 7.53) ved hjelp av et eksempel.

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

Det er $30$ tall under $121$ som er delelig på 4 fordi ${121 \over 4} = 30+ \text{én i rest}$.

1. Hvor mange tall under 121 er delelig på enten 4, 11 eller 59? Besvarelsen må inneholde en illustrasjon som får fram hvordan du har løst problemet.

2. Du velger et tilfeldig tall under $121$. Hva er sannsynligheten for at tallet er delelig på 4, 11 eller 59?

##### Vurderingskriterier

1. Ved å illustrere kan vi se se på mengdene som er delelig på 4, 11 og 59. Siden $59$ er et primtall er minste felles multiplum etter $121$. Tallene $11$ og $4$ har derimot minste felles multiplum lik $44$. Derfor vil alt i 44 gangen overtelles når vi tar antall tall i 4 gangen og tall i 11 gangen. Vi ser at $44$, $88$ og $132$ er de tre første verdiene i 44-gangen. Dermed overteller vi bare 2 tall. Snittet mellom de andre mengdene er tomme. Vi får altså at det er $30$ tall delelig på 4, og 10 tall delelig på 11 (eventuelt 11 hvis en leser feil og ikke ser at der er *under* 121) og 2 tall delelig på 59 under 121. Totalt får vi dermed $30+10-2+2 = 40$ tall delelig på enten 4, 11 eller 59.
2. Vi kan nå se at vi har 40 av 120 mulige som gir $\frac{40}{120}=\frac{4}{12}= \frac{1}{3}$ sjans for å velge et tall under 121 som er delelig på enten 4, 11 eller 59.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/sannsyn28.04.svg)

### Forklare, illustrere og bruke komplementsetningen

#### Grunnleggende: Forklare begrepet komplement

Forklar begrepet komplement ved hjelp av et eksempel.

#### Middels: Forklare og illustrere komplementsetningen i sannsynlighet

Sannsynligheten for hendelsen $A$ er $0.4$. Forklar, ved hjelp av en illustrasjon, hva $P(A^C)$ er.

##### Vurderingskriterier

Studenten trenger bare å bruke at $P(A) + P(A^C) = 1$ for å konkludere at $P(A^C) = 0.6$.

#### Avansert: Forklare, illustrere og bruke komplementsetningen i sannsynlighet

Poker er et kortspill der man har 52 kort. Det er tretten kort i hver sort (kløver, ruter, spar og hjerter), inkludert ett ess i hver sort. Hva er sannsynligheten for å *ikke* få et par i ess (to ess) på blant de to kortene du trekker?

##### Vurderingskriterier

Studenten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan de peke på at det er $\frac{52\cdot 51}{2}$ mulige hender man kan starte med og alle hendene er like sannsylige. Dermed kan vi finne antall muligheter for å få et par i ess og bruke komplementsetningen. Det kan vi gjøre ved å finne antall hender som inneholder et par i ess. Det kan vi for eksempel løse bare ved å telle. Vi kan ha hjerter-kløver, hjerter-ruter, hjerter-spar, kløver-ruter, kløver-spar, ruter-spar. Dermed er det $26\cdot 51 - 6$ mulige hender som ikke er et par i ess av totalt $26\cdot 51$ mulige hender. Siden alle hendene er like sannsynlige kan vi konkludere med at det er $\frac{26\cdot 51-6}{26\cdot 51} = 1 - \frac{6}{26\cdot 51}$ i sannsynlighet for å ikke få par i ess.

### Bruke begrepene i temaet til å løse sammensatte problemer

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

Ved kast med to terninger noteres differensen mellom antall øyne på terningene (det største tallet minus det minste tallet). Hvis terningene viser samme antall øyne, er differensen lik 0.

1. List opp eller lag tabell som viser alle mulighetene der differensen blir 0, 1, 2, 3, 4 eller 5.
2. Hva er sannsynligheten for at differensen blir 0? Hva er sannsynligheten
for at differensen blir 1? Forklar.
3. To terninger kastes to ganger. Hva er sannsynligheten for den
sammensatte hendelsen at differensen blir 0 i første kast og at
differansen blir 1 i andre kast? Forklar.
4. To terninger kastes to ganger. Hva er sannsynligheten for at differensen
ikke blir 0 i noen av kastene?

*Vink:* $36\cdot 36 = 1296$.

##### Vurderingskriterier

1.

$$
\begin{array} {|r|r|r|r|r|r|}\hline  & \text{Første terning} & 1 & 2 & 3 & 4 & 5 & 6
\\
\hline
\text{Andre terning}
\\ \hline  
1 & & 1-1 = 0 & 2-1 = 1 & 3-1 = 2 & 4-1 = 3 & 5-1 =4 & 6-1 = 5
\\ \hline  
2 & & 2-1 = 1& 2-2 = 0 & 3-2 = 1 & 4-2 = 2 & 5-2 = 3 & 6-2 = 4
\\ \hline
3 & & 3-1 =2& 3-2 =1 & 3-3 = 0 & 4-3 = 1 & 5-3 = 2 & 6-3 = 3
\\ \hline
4 & & 4-1 =3 & 4-2 =2 &  4-3 = 1 & 4-4 = 0& 5-4 = 1 & 6-4 = 2
\\ \hline
5 & & 5-1 =4& 5-2 = 3 &  5-3 = 2 & 5-4 =1 & 5-5 = 0 & 6-5 = 1
\\ \hline
6 & & 6-1 =5& 6-2 = 4 &  6-3 =3 & 6-4 =2 & 6-5 =1 & 6-6 = 0
\\ \hline
\end{array}
$$

2. Vi ser at 6 av de 36 mulige utfallene gir 0, så sannsynligheten er $\frac{6}{36} = \frac{1}{6}$. Vi ser videre at det er 10 mulige utfall som gir $1$, eller $\frac{10}{36}$ i sannsynlighet for å få 1.
3. Vi kan bruke multiplikasjonsprinsippet til å innse at vi har 36 utfall i første kast av to terninger og så 36 i neste. Derfor får vi totalt $1296$ mulige utfall. Vi vet at det i seks av de første kastene så kan vi få 0 i differanse. For hver av de seks mulighetene har vi 10 muligheter for å få 1 i differanse på andre kast. Igjen gir multiplikasjonsprinsippet oss at det må være $6\cdot 10 = 60$ mulige utfall av de $1296$ utfallene som gir 0 på første kast av to terninger og 1 på andre kast av to terninger. Sannsynligheten blir derfor $\frac{60}{1296}$.
4. Det vil være 30 muligheter for å ikke få 0 i første og tilsvarende 30 for å ikke få noen i neste. Dermed får vi en sannsynlighet på $\frac{900}{1296}$.

## 24.04.23

### Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell

#### Grunnleggende: Gjengi og gi eksempler til begrepene

1. Forklar hva en sannsynlighetsmodell er ved hjelp av begrepene utfall, utfallsrom og hendelse. Gi et eksempel på en sannsynlighetsmodell.

##### Vurderingskriterier

Studenten må gi en forklaring som bruker begrepene, samt gi et eksempel.

#### Middels: Avgjøre og begrunne om situasjoner er en sannsynlighetsmodell

1. La et forsøk ha utfallsrommet $U = { u_1, u_2, u_3, u_4, u_5}$. Hvis $P(\{u_1, u_2, u_3\}) = 0.6$, gi et eksempel på hva $P(\{u_4, u_5\})$ og $P(u_6)$ kan være. Besvarelsen må være begrunnet.

2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4, u_5}$. Forklar at $P(\{u_3\})$ må være større enn $0.4$ hvis $P(\{u_1,u_3\}) = 0.7$ og $P(\{u_2, u,3\}) = 0.7$.  

**Merk** Det var en feil i teksten over der det stod ''Forklar at $P(\{u_3\})$ *ikke kan være* større enn...''. Dette er rettet i teksten over.

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

Studenten trenger bare å bruke at $P(A) + P(A^C) = 1$ for å konkludere at $P(A^C) = 0.6$.

#### Avansert: Forklare, illustrere og bruke komplementsetningen i sannsynlighet

Da Henrik var student gikk han i en klasse med 21 studenter. Hver undervisningsøkt deltes de inn i grupper på tre. Henrik hadde fire venner han gjerne ønsket å komme på gruppe med. Hva var synligheten for at Henrik kom på gruppe med minst en av dine venner, når gruppene ble valgt tilfeldig?

##### Vurderingskriterier

Studenten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan en peke på hvilke to som havner på gruppe med Henrik er like sannsynlig. Det er $\frac{20\cdot 19}{2} = 190$ forskjellige mulige klassekammerater som han kan havne på. For å avgjøre hvor mange av de som inneholder minst én, er det naturlig å se på hvor mange som ikke inneholder noen. Av de 20 resterende klassekammeratene er det 16 som ikke er av de fire vennene Henrik ønsker å komme på gruppe med. Derfor er det $\frac{16\cdot 15}{2} = 8\cdot 15 = 120$ grupper som ikke inneholder noen av Henriks venner. Derfor må det være $180 - 120 = 60$ mulige grupper der Henrik er på gruppe med minst én av sine venner. Sannsynligheten er derfor $\frac{60}{190}=\frac{6}{19}$.

### Bruke begrepene i temaet til å løse sammensatte problemer

#### Avansert

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

1. Studenten må bruke at $P(U) = 1$ og at $P(\{u_1,u_2,u_3\})= P(u_1)+P(u_2)+P(u3)$ noe som ikke stemmer.
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
