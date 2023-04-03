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

- Alfa 7.14
- 7.15. Besvarelsen skal begrunnes ved å peke på definisjonen av en
    uniform sannsynlighetsmodell.
- Et forsøk skal utføres ved å kaste en mynt tre ganger og registrere om det blir kron eller mynt. Henrik setter opp utfallsrommet {tre kron,to kron og en mynt,en kron og to mynt,tre mynt}. Avgjør om dette gir opphav til en uniform sannsynlighetsmodell.

##### Løsningsforslag

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

- Du er på hytta og kaster fire femmere på første kast. Med to kast
    igjen bestemmer du deg for å gå for yatzy. Sett opp et utfallsrom
    som gir en uniform sannsynlighetsmodell og finn sannsynligheten for
    at du får yatzy ved hjelp av modellen.

##### Løsningsforslag

Vi kan tenke oss at vi uansett kaster to kast, selv om vi får en femmer på første kast. Dette betyr bare at vi har fått yatzy og at det siste kastet ikke har noe å si. Vi kan skrive opp de ulike mulighetne slik:
$$\left\{ \begin{array}{r}
11,12,13,14,15,16, \\
21,22,23,24,25,26, \\
31,32,33,34,35,36, \\
41,42,43,44,45,46, \\
51,52,53,54,55,56, \\
61,62,63,64,65,66 \\
\end{array} \right\}$$

Vi ser her at det er $11$ av de $36$ mulighetene som inneholder en femmer. Dermed er sannsynligheten $\frac{11}{36}$.

- André har kjøpt inn 6 lyspærer som han legger i en ekse slik at han
    slipper å måtte kjøpe nye hver gang en pære går. Uten å tenke seg om
    byttet André tre lyspærer, men puttet de gamle defekte lyspærene
    sammen med de nye. Neste gang skal han bytte to pærer og tar han
    bare to tilfeldige pærer ut fra esken. Sett opp et utfallsrom som
    gir en uniform sannsynlighetsmodell og avgjør, ved hjelp av
    modellen, hva sannsynligheten er for at André tar med seg en defekt
    pære.

##### Løsningsforslag

Anta at pærene er nummerert 1 til 6 og la 1 og 2 være defekte. Da er
mulig utfall parene, (1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4),
(2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6) og (5,6). Det er
rimelig å anta at alle parene er like sannsynlige siden vi trekker tilfeldig. Alle parene som inneholder enten $1$ eller $2$ eller begge betyr at André tar med seg en defekt pære. Teller vi opp får vi at sannsynligheten er $\frac{9}{15}$.

### Forklare og bruke store talls lov (Alfa 7.3)

Dette læringsmålet gjøres og godkjennes som en gruppeoppgave (på maks
tre personer).

Læringsmålet tar utgangspunkt i aktiviteten fra timen tirsdag 28.03.

*Aktivitet*: Henrik og André gamblet i pauserommet i J-bygget med en mynt de hadde liggende. Henrik hadde valgt kron og André mynt. De bestemte seg at det var førstemann som fikk 5 poeng som vant. Da de kom til stillingen 2-4 ble de «busta» av Ingvald som tok mynten og sa at de må avslutte. Problemet er at det ble lagt inn 3000 kroner i potten. Hvordan skal de fordele pengene?

#### Grunnleggende: Forklare store talls lov

1. Forklar store talls lov ved hjelp av et eksempel.

#### Middels: Undersøke og estimere sannsynligheter ved å bruke store talls lov

1. Forklar store talls lov ved hjelp av et eksempel
2. Ta utgangspunkt i aktiviteten beskrevet over.
   a. Bruk et verktøy (programmering eller excel eller lignende) til å simulere aktiviteten. Dere skal simulere minst 1000 forsøk. Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringen (I Excel betyr dette å få hvordan dette er strukturer og hvilke formler som er brukt og hvorfor dette simulerer den faktiske situasjonen. Hvis det er gjort ved hjelp av programmering det komme fram et skjermutklipp som viser koden).
   b. Bruk resultatene fra forsøkene til å estimere sannsynligheten for at Henrik vinner. Besvarelsen må inneholde et skjermutklipp og en forklaring som får fram hvordan du har gjennomført simuleringen
   c. Anta nå at Henrik og André spilte førstemann til 10 poeng og at de ble avbrutt på stillingen 2-4. Brukt et verktøy til å simulere 1000 forsøk og bruk dette til å estimere sannsynligheten for at Henrik vinner, på samme måte som i a. og b.
       - Hvis Excel brukes så kan "TILFELDIGMELLOM()", "ANTALL.HVIS()" være nyttige funksjoner. Google er også alltid et nyttig verktøy 😉
       - Besvarelsen må ikke bare gjøre et godt estimat av sannsynlighetene. Besvarelsen også må være skrevet og strukturert på en slik måte at leseren kan gjenta simuleringen og få tilsvarende resultater.

#### Avansert: Undersøke, estimere og bruke store talls lov i undervisning

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
frem at produktregelen må gjelde (Setning 7.53).

### Forklare og bruke begrepene ordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene

Forklar og gi eksempler til begrepene

#### Middels: Begrunne at et utvalg er ordnet med og uten tilbakelegg, og finne antall muligheter i utvalget

- Begrunn at følgende situasjoner kan tenkes på som ordnede utvalg med
    tilbakelegg og finn antall muligheter i utvalgene
  - Du skal velge en firesifret kode der du kan ha sifrene 0-9 på
        hver posisjon.
  - Du skal kaste en terning tre ganger og skriver opp antall øyne
        på terningen for hvert kast i kronologisk rekkefølge.
- Begrunn at følgende situasjoner kan tenkes på som ordnede utvalg
    uten tilbakelegg og finn antall muligheter i utvalgene
  - Du skal stokke om bokstavene i navnet André.
  - I et skirenn deltar det 7 personer. Du ønsker å skrive opp
        mulige 1.- 2.- og 3.plasser som kan oppstå.

### Forklare og bruke begrepene uordnet utvalg med og uten tilbakelegg

#### Grunnleggende: Forklare og gi eksempler til begrepene uordnet utvalg med og uten tilbakelegg

Forklar og gi eksempler til begrepene

#### Middels: Begrunne at et utvalg er uordnet m/u tilbakelegg, og finne antall muligheter i utvalget

- Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg
    uten tilbakelegg og finn antall muligheter i utvalgene
  - Du har en twistpose med 7 forskjellige twist igjen. Du tar
        hånden ned i poser og får med deg tre twist.
  - Det skal trekkes tre heldige ansatte blant 15 ansatte som får et
        gavekort på 1000 kr hver.
- Begrunn at følgende situasjoner kan tenkes på som uordnede utvalg
    med tilbakelegg og finn antall muligheter i utvalgene
  - Du skal bestille 3 pizza fra Dolly dimples til deg og
        vennegjengen på en fredag. Dolly dimples har 5 mulige typer dere
        kan velge mellom.
  - Du bestemmer deg for å spise fem frukter hver dag. Du har alltid
        5 bananer, 5 pærer, 5 epler og 5 appelsiner liggende.

### Avgjøre om utvalg er ordnet eller uordnet og om det er med eller uten tilbakelegg

#### Middels

Avgjør om situasjonene under kan tenkes som (u)ordnede utvalg m/u
tilbakelegg

1. Du skal velge ut en komité fra en 20 lærerstudenter. Komitéen skal
    bestå av 4 studenter.
2. En klasse med 25 elever skal velge tillitsvalgt. De skal ta ut
    første, andre tillitsperson. Første elev skal være
    hovedtillitsvalgt, neste skal være stedfortreder.
3. Hver uke i tre uker har 6 lærere et ukentlig bruslotteri der de
    vinner en sekspakning Cola hvis de vinner. Det trekkes en vinner
    blant de 6 lærerne hver uke.
4. Til et lag i $4 \times 100$m stafett er det tatt ut fire sprintere,
    A, B, C og D. Hvor mange rekkefølger kan de stille opp stafettlaget
    på?
5. Du har et bord med seks plasser og du skal dekke på til fire. Hvor
    mange mulige kombinasjoner kan lage?
6. Du skal kjøpe en firepakning med donuts fra Donutsjappa ved
    Aquarama. De har tre typer donuts du kan velge mellom. Hvor
    forskjellige firepakninger kan du lage?
7. Du skal trekke ut fire gutter fra en klasse på 16 gutter og 17
    jenter. Hvor mange måter kan du gjøre det på?
8. Syv studenter bor i et kollektiv sammen. Den første uke trakker de
    lodd om hvem som skal lage mat, gjøre rent fellesarealet og vaske
    badet. Ingen får mer enn én jobb. Hvor mange mulige utfall kan
    trekningen ha?

### Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet *og* kombinatorikk)

#### Grunnleggende: Forklare hva union og snitt er

Forklare og illustrere et sammensatt valg/et forsøk sammensatt av flere
trinn.

#### Middels: Forklare og illustrere addisjonssetningen for to mengder (Setning 7.53)

Forklare og illustrere produktregelen. Pek tydelig på hvorfor det kommer
frem at produktregelen må gjelde (Setning 7.53).

#### Avansert: Bruke addisjonssetningen for å undersøke problemer

1. Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite
    at koden inneholder en toer (minst), men er ikke et partall. Avgjør
    hvor mange gjenværende muligheter det er
2. André har en tresifret kombinasjon på sykkellåsen sin. Du får vite
    at koden inneholder minst én ener og minst én toer. Du regner deg
    fram til at det er 271 koder som inneholder minst én ener, og 271
    koder som inneholder minst én toer. I tillegg er det 512 av de
    totalt 1000 mulighetene som hverken inneholder enere eller toere.
    Hvor mange forskjellige koder kan André ha på sin lås?

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
