<!-- 
PDF:
Kjør i terminal fra markdown mappa pandoc .\quizzer\tallteori\tallteori.md -f markdown -t pdf --pdf-engine=xelatex --variable=block-headings --toc -o .\quizzer\tallteori\tallteori.pdf 
HTML:
pandoc .\quizzer\tallteori\tallteori.md -f markdown -t html --mathjax --template=template.html --toc -s -H styling.css -o .\quizzer\tallteori\tallteori.html
-->
# Tallteori

## Øveoppgaver

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler på hva som menes med begrepene *faktor* og *divisor.* Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
2. Forklar og gi eksempler på hva som menes med *felles faktor* og *største felles faktor* for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
3. Forklar og gi eksempler på hva som menes med begrepet *multiplum*. Besvarelsen må inneholde både formell definisjon og grunnskoletilpasset forklaring.

4. Forklar og gi eksempler på hva som menes med *felles multiplum* og *minste felles multiplum* for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor produktet av største felles faktor og minste felles
    multiplum for to tall er det samme som produktet av de to tallene.

2. Du skal lage gaveposer med to typer godteri. Den ene typen har du
    210 av, den andre 84. Hver pose skal ha likt innhold. Hvilke antall
    poser er det mulig å fylle, dersom alle godteriene skal brukes?

3. La $sff(a,b) = 12$, $mfm(a,b) = 5460$ og $a = 420$. Hva er $b$?
    Begrunn.

4. To tannhjul dreier med ulik hastighet. Det ene bruker 15 sekunder på
    én omdreining. Du ønsker at det andre skal holde en dreiehastighet
    slik at dersom de settes i gang på likt, vil de begge stå i
    utgangsposisjonen hvert 105. sekund. Hva må hastigheten til det
    andre tannhjulet være?

5. Undersøk og begrunn.

    a.  Har alle summer av tre påfølgende naturlige tall en felles faktor?
    b.  Hva med summer av fem, syv, ni og så videre påfølgende tall?
    c.  Gjelder det samme for summer av påfølgende tall der antallet ledd i summen er et partall?

##### Løsningsforslag

1. Den enkleste løsningen her er å bruke at $\text{sff}\cdot \text{mfm} = ab$. Vi vet altså at $12\cdot 5460 = 420 b$ Deler vi på $420$ får vi nå at $b = 156$.
2. Hvis vi primtallsfaktoriserer kan vi skrive $210$ som $2\cdot 2\cdot 5 \cdot 11$ og $84$ kan skrives som $2\cdot 2 \cdot 3\cdot 7$. Vi kan nå se at én pose fungerer med $210$ av den ene og 84 går. Siden begge inneholder faktoren $2$ kan vi også dele de i 2 og få to poser med $110$ og $42$ i hver. Vi ser at begge kan deles i to igjen, som gir fire poser med $55$ og $21$ i hver. Vi har nå ingen felles faktorer, så det kan heller ikke fordeles på andre måter. Det gir at vi kan dele i enten én, to eller fire poser.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

1. Hvis vi studerer summer av påfølgende tall, vil vi oppdage at
    summene i noen tilfeller er delelig med antallet ledd i summen. Vis
    algebraisk hvilke tilfeller det er slik, og hvilke tilfeller det
    ikke er slik.

2. Du får vite at minste felles multiplum for to tall er $1155$ og det
    ene tallet er $105$. Hva kan det andre tallet være?

3. Alle produkter av tre påfølgende naturlige tall har tre felles
    faktorer forskjellig fra $1$. Hvilke er det? Begrunn.

4. Velg to sifre mellom $1$ og $9$. Lag to ulike tall som begge inneholder begge sifrene (for eksempel $64$ og $46$). Del summen av tallene på summen av de to sifrene.
   a. Undersøk flere tilfeller -- hva ser ut til å være mønsteret?
   b. Begrunn mønsteret.

##### Løsningsforslag

3. La oss skrive tre vilkårlig påfølgende tall slik $n-1$, $n$ og $n+1$. Er for eksempel $n = 3$ er de tre påfølgende tallene her $2$, $3$ og $4$. Det viktige vi må legge merke til her er at vi vil alltid ha minst ett partall i rekken. Starter vi på et partall så har vi to. I tillegg vil vi alltid ha et tall i $3$-gangen. Det betyr at produktet vårt må inneholde faktoren $2$ og $3$. Dermed må prodkutet også faktoren $6$. Alle produkter av tre påfølgende tall har derfor felles faktorer $2$, $3$ og $6$, i tillegg til $1$.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler på hva et *naturlig tall* er.
2. Forklar og gi eksempler på hva *partall* og *oddetall* er.
    Besvarelsen må inneholde både algebraiske definisjoner,
    ordforklaringer og illustrasjoner.
3. Forklar og gi eksempler på hva *primtall* og *sammensatt tall* er.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Vis grunnskoletilpasset (ved hjelp av ordforklaringer og
    illustrasjoner) og formelt (med algebraiske symboler) at summen av
    ...

    a.  par og par er par,

    b.  odde og odde er par,

    c.  par og odde er odde.

2. Vis grunnskoletilpasset (ved hjelp av ordforklaringer og
    illustrasjoner) og formelt (med algebraiske symboler) at produktet
    av ...

    a.  par og par er par,

    b.  odde og odde er odd,

    c.  par og odde er par.

##### Løsningsforslag

2. \
   a. \
   Formelt: At et tall er et partall betyr at det kan deles på $2$ eller sagt med andre ord at det inneholder faktoren $2$. Det betyr derfor at vi kan skrive to vilkårlige partall som $2m$ og $2n$. Produktet av disse vil derfor være $2n\cdot 2m = 2(2nm)$. Dette er et tall som kan deles på to og er derfor også et partall. Dermed har vi vist at produktet av to partall alltid er et partall. \
   Grunnskoletilpasset: La oss begynne med å avklare en måte å tenke på partall. Siden partall betyr at noe kan deles på to, kan vi også si at partall kan stables eller visualiseres som tårn som kommer i par. For eksempel kan vi ta utgangspunkt i to partall $4$ og $6$. Stabler vi disse slik som forklart vil de se ut som på bildet under:
   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main//img/tallteo/pargpardel1.svg)
   Ved å tenke på multiplikasjon som gjentatt addisjon kan vi derfor gjenta partårnet som representerer $6$ fire ganger. Multiplikasjonen kan vi altså se for oss slik som figuren under:
   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main//img/tallteo/pargpardel2.svg)
   Siden vi nå har flere tårn (helt konkret fire tårn), som alle er to i bredden. Kan vi stable de fint oppå hverandre, noe som gir et nytt partårn.
   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main//img/tallteo/pargpardel3.svg)
   Siden sluttresultatet endte med et partårn var sluttresultatet også et partall, i dette tilfellet var $6\cdot 4 = 24$. Vi kan deretter peke på at det ikke var noe spesielt med hverken $4$ eller $6$. Det eneste spesielle var vi la sammen flere partårn (vi la sammen fire), det kunne vært hva som helst. Vi kunne for eksempel byttet ut $6$ med et hvilket som helst partall. Vi kunne også byttet ut $4$ med et hvilket som helst partall også. Hadde vi for eksempel tatt $6$ og $24$ ville strukturen i beviset fortsatt fungert, noe som må bety at partall multiplisert med partall må resultere i et partall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

1. Se for deg at du stiller opp tallene fra én til ti på en rekke. Kan
    du plassere $+$ og $–$ mellom dem slik at summen blir null? Hva med
    andre rekker fra én og opp? Finnes det et mønster?

2. Hvis vi ønsker å undersøke manuelt om et tall $n$ er prim eller
    sammensatt, er det ikke nødvendig å lete etter faktorer i $n$ som er
    høyere enn $\sqrt{n}$. Forklar hvorfor.

##### Løsningsforslag

1. Hvis vi fokuserer på antall oddetall i summen, ser vi at det er $1, 3, 5, 7$ og $9$. Vi kan enten legge de til eller trekke de fra i summen vår. Siden vi har et oddetall antall oddetall. Det betyr også at vi enten vil legge til et oddetall antall oddetall, eller trekke fra et oddetall antall oddetall. Vi kan anta at vi legger de til (for hvis summen ble 0 etter vi la til + og -, så ville vi fortsatt fått 0 i sum dersom vi byttet om alle +'ene med -'er og motsatt). Siden vi legger til et oddetall antall oddetall i tillegg til noen partall vil vi til slutt ende opp med å ha lagt til et oddetall. Ser vi på hva vi trekker fra, ser vi at vi trekker fra et partall antall oddetall i tillegg til noen partall. Det betyr at vi trekker fra et partall. Vi må altså ha at vi legger til et oddetall og trekker fra et partall. Dette kan åpenbart ikke bli 0. Uten å undersøke noen mønstre veldig nøye, kan vi allerede nå konkludere med at hvis vi har et oddetall antall oddetall og en tilsvarende situasjon, så vil vi aldri kunne lage en sum som blir 0. (Videre undersøking for flere mønstre får dere gjøre selv 😉)

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Begrunne delelighetsreglene

1. Begrunn delelighetsregelen for tall som er delelig med 2. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

2. Begrunn delelighetsregelen for tall som er delelig med 3. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

3. Begrunn delelighetsregelen for tall som er delelig med 4. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

4. Begrunn delelighetsregelen for tall som er delelig med 5. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

5. Begrunn delelighetsregelen for tall som er delelig med 6. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

6. Begrunn delelighetsregelen for tall som er delelig med 9. Du må gi
    både en formell og en grunnskoletilpasset begrunnelse.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

1. Utled det eksplisitte uttrykket for summen av de $n$ første
    naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av
    Gauss-trikset (doble summen):

    a.  ved hjelp av figur

    b.  algebraisk

2. Finn summen av de naturlige tallene fra 1 til 9 ved hjelp av
    Gauss-trikset.

3. Utled det eksplisitte uttrykket for rektangeltall $n$ ved hjelp av
    strategien *sum av tillegg.* Vis i en figur hvordan tilleggene
    danner et rektangel.

4. Utled det eksplisitte uttrykket for kvadrattall $n$ ved hjelp av
    strategien *sum av tillegg.* Vis i en figur hvordan tilleggene
    danner et kvadrat.

5. Finn summen av de naturlige tallene fra 5 til 16.

6. Finn summen av oddetallene fra 5 til 13.

7. Finn summen av partallene fra 6 til 16.

8. Undersøk summen av par av nabo-trekanttall.

    a.  Beskriv en antakelse du får,

    b.  begrunn den geometrisk

    c.  og algebraisk.

9. Alle gjestene i et selskap skal håndhilse med hverandre. Hvordan
    avhenger antall håndtrykk av antall gjester?

#### Middels: Ved hjelp av sum av tillegg for andre polygontall

1. Illustrer femkanttallene opp til $P_{4}$, og utled eksplisitt
    uttrykk for $P_{n}$ ved hjelp av strategien *sum av tillegg.*

2. Illustrer sekskanttallene opp til $H_{4}$, og utled eksplisitt
    uttrykk for $H_{n}$ ved hjelp av strategien *sum av tillegg.*

3. Illustrer syvkanttallene opp til $S_{4}$, og utled eksplisitt
    uttrykk for $S_{n}$ ved hjelp av strategien *sum av tillegg.*

4. Undersøk tilleggene for polygontallene (trekant- kvadrat-,
    femkanttallene og så videre). Forsøk å generalisere mønsteret du
    finner.

    a.  Argumenter for mønsteret ved å vise til figurene.

    b.  Lag et algebraisk uttrykk som beskriver mønsteret tilleggene
        følger. (Hvis $n$ står for figurnummer, kan du for eksempel la
        $m$ stå for antall kanter i polygonen.)

##### Løsningsforslag

1. For å bruke sum av tillegg er vi nødt til å fremheve tilleggene fra figur til figur. Gjør dette selv ved å tegne! Se også \
![Hentet fra Wikipedia](https://upload.wikimedia.org/wikipedia/commons/b/b5/Pentagonal_number.gif)

Vi ser altså at tillegget fra $P_1$ til $P_2$ er $4$, fra $P_2$ til $P_3$ er $7$. Generelt kan vi legge merke til at vi legger til $3$ sider med sidelengde $n$ for å lage $P_n$ fra $P_{n-1}$. Når vi legger til sidene får vi to hjørner som overtelles. Generelt må tillegget derfor være $3n-2$. Vi kan nå skrive figurene våre ved hjelp av tilleggene.
$$
\begin{aligned}
P_1 & = 1
\\
P_2 & = 1 + 4 = (3\cdot 1 - 2) + (3\cdot 2 - 2)
\\
P_3 & = 1 + 4 + 7 =  (3\cdot 1 - 2) + (3\cdot 2 - 2) = (3\cdot 3 - 2)
\\
P_4 & = 1 + 4 + 7+ 11 =(3\cdot 1 - 2) + (3\cdot 2 - 2) = (3\cdot 3 - 2) + (3\cdot 4 - 2)
\\
\vdots
\\
P_n & = (3\cdot 1-2) + (3\cdot 2 -2) + \ldots + (3\cdot n -2).
\end{aligned}
$$
Nå må vi bare gjøre litt manipulering for å komme oss i mål. Vi faktoriserer ut den felles faktoren $3$ og ser at i hvert ledd trekker fra $2$. Vi trekker altså fra $n\cdot 2$. Det gir \
$P_n = (3\cdot 1-2) + (3\cdot 2 -2) + \ldots + (3\cdot n -2) = 3(1+2+\ldots + n) - n\cdot 2$.
Siden vi vet at $T_n = 1+2+\ldots+n = \frac{n(n+1)}{2}$, kan vi erstatte dette i uttrykket vårt over og få \
$P_n = 3T_n -2n = \frac{3n(n+1)}{2}-2n$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

1. Under ser du figurtall én til fire.

    a.  Finn eksplisitt sammenheng ved hjelp av geometrisk
        betraktning/stirre-hardt-strategien. Dekomponer figuren på så
        mange måter du klarer.

    b.  Finn eksplisitt sammenheng ved hjelp av strategien *sum av
        tillegg*.

    c.  Vis at verdien av figurtall nummer $n$ er én mindre enn
        kvadrattall nummer $n + 1$, og bruk dette til å omarrangere
        figurene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image1.png)

1. Under ser du figurtall én til fire.

    a.  Finn eksplisitt sammenheng ved hjelp av geometrisk
        betraktning/stirre-hardt-strategien. Dekomponer figuren på så
        mange måter du klarer.

    b.  Finn eksplisitt sammenheng ved hjelp av strategien *sum av
        tillegg*.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image2.png)

##### Løsningsforslag

1. \
   a. Vi kan legge merke til at toppen av figuren består av et *skjevt* kvadrat, eller en diamant, altså er dette kvadrattallene. Denne vet vi at kan beskrives eksplisitt $n^2$. \
   Videre har figuren 2 bein. Benene øker lineært. Vi ar $2$ så $4$ så $6$ og så videre. Dermed kan siste del av figuren beskrives eksplisitt som $2n$. \
   Setter vi det sammen får vi at figuren kan beskrives slik: $P_n = n^2 + 2n$. \
   Let selv etter andre måter å bryte ned figuren!!
   b. Vi kan bruke nedbrytningen fra forrige oppgave til å beskrive tillegget. Det n'te kvadrattallet er alltid det forrige kvadrattallet pluss det n'te oddetallet. Altså $n^2 = (n-1)^2+2n-1$. Videre øker en lineær sammenheng alltid med det samme, så tillegget her er alltid $2$. Totalt kan tillegget beskrives ved $(2n-1)+2 = 2n+1$.
   Vi kan også undersøke selve tallrekka, som er $3, 8, 15, 24$. Vi ser at differansen mellom hvert ledd i rekka er $5, 7, 9$. Her ser vi at tillegget øker med 2 hver gang, noe som tilsier at tillegget vokser lineær med stigning $2$. Det må bety at formen på tillegget er $2n+b$, der $b$ fortsatt er ukjent. Vi kan derimot enkelt avgjøre $b$ ved å sjekke, for eksempel $P_2$. Da er tillegget $2\cdot 2 + b$, og $P_2$ er  $P_1 + 2\cdot2+b$. Siden $P_2 = 8$ og $P_1 = 3$, så må $2\cdot 2 + b = 5$ som betyr at $b=1$. Tillegget kan altså skrives på formen $2n+1$.
   Nå kan vi skrive figurtallene som summen av tilleggene:
   $$
   \begin{aligned}
   P_1 & = 3
   \\
   P_2 & = 3 + 2\cdot 2+1
   \\
   P_3 & = 3 + (2\cdot 2 + 1) +(2\cdot 3 + 1)
   \\
   \vdots
   \\
   P_n & = (2\cdot 1 + 1) + (2\cdot 2 + 1) + (2\cdot 3 + 1)+ \ldots + (2\cdot n + 1).
   \end{aligned}
   $$
   Vi får derfor at
   $$
   \begin{aligned}
   P_n & = (2\cdot 1 + 1) + (2\cdot 2 + 1) + (2\cdot 3 + 1)+ \ldots + (2\cdot n + 1)
   \\
   P_n & = 2(1+2+3+\ldots + n) + 1\cdot n
   \\
   & = 2T_n + n
   \\
   & = n(n+1)+n
   \\
   & =  n^2 + n + n = n^2 + 2n
   \end{aligned}
   $$
   c. Hvis vi skal vise at figurtallet $P_n$ er én mindre enn kvadrattall nummer $n+1$, kan vi bare se på differansen mellom de. $(n+1)^2 - P_n = (n^2+2n+1)-(n^2+2n) = n^2 +2n + 1 - n^2 -2n = 1$. Som viser første del av oppgaven. Vi må nå bare omarrangere figuren. Det kan for eksempel gjøres som i figuren nedenfor. Der ser de grønne ringene uten rød ring ikke flyttet. De grønne med rød ring rundt er de hvite ringene flyttet og den røde ringen er den *manglende* ringen for å fullføre kvadratet.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/stirrehardt.svg)

### Finne rekursivt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

1. Vis i en illustrasjon hvordan hver figur inneholder den forrige, og
    finn rekursivt uttrykk for trekanttall $n$

    a.  ved hjelp av strategien *form på tillegg*

    b.  ved hjelp av strategien *differanse mellom eksplisitte uttrykk*

2. Vis i en illustrasjon hvordan hver figur inneholder den forrige, og
    finn rekursivt uttrykk for kvadrattall $n$

    a.  ved hjelp av strategien *form på tillegg*

    b.  ved hjelp av strategien *differanse mellom eksplisitte uttrykk*

3. Vis i en illustrasjon hvordan hver figur inneholder den forrige, og
    finn rekursivt uttrykk for rektangeltall $n$

    a.  ved hjelp av strategien *form på tillegg*

    b.  ved hjelp av strategien *differanse mellom eksplisitte uttrykk*

##### Løsningsforslag

Se heftet for alle.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

1. Hva er sammenhengen mellom påfølgende figurer? Finn rekursivt
    uttrykk.

    a.  Vis i figuren.

    b.  Finn ved hjelp av *form på tillegg.*

    c.  Finn ved hjelp av *differanse mellom eksplisitte uttrykk.*

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image2.png)

2. Hva er sammenhengen mellom påfølgende figurer? Finn rekursivt
    uttrykk.

    a.  Vis i figuren.

    b.  Finn ved hjelp av *form på tillegg.*

    c.  Finn ved hjelp av *differanse mellom eksplisitte uttrykk.*

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image1.png)

##### Løsningsforslag

1. Ser vi på oppgave 1. i læringsmålet **Finne eksplisitt uttrykk for figurtall** på Avansert nivå, ser vi at mye av arbeidet allerede er forklart.

   a. Vi kan for eksempel tegne figurene på følgende måte (prøv selv og tegne neste med egne farger, der det forrige figur kommer tydelig fram i neste).
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/rekursivtall.svg)
   b. Fra tidligere har vi at formen på tillegget er $2n+1$ og dermed vet vi derfor at $F_n = F_{n-1} + 2n+1$
   c. Vi har også fra tidligere at det eksplisitte uttrykket er $P_n = n^2 + 2n$. Vi må derfor finne tillegget ved å se på $P_n - P_{n-1}$. Ved å regne får vi
   $$
   \begin{aligned}
   P_n - P_{n-1}
   & = n^2 + 2n - ((n-1)^2+2(n-1))
   \\
   & = n^2 + 2n - (n^2-2n+1+2n-2)
   \\
   & =
   n^2 + 2n - (n^2 -1)
   \\
   & =
   n^2 + 2n - n^2 +1 = 2n + 1.
   \end{aligned}
   $$

### Beskrive oppbygningen av figurtall (alle typer)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

1. Se figurtallene under.

    a.  Gi en så kort og presis verbal beskrivelse du kan av hvordan
        figurene vokser (rekursiv sammenheng).

    b.  Illustrer den rekursive sammenhengen i figurene.

    c.  Gi en beskrivelse av den eksplisitte sammenhengen mellom
        figurnummer og figurtall (presisjon er målet her også).

    d.  Vis den eksplisitte sammenhengen i figurene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image2.png)

2. Samme ordlyd som oppgave 1.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image3.png)

##### Løsningsforslag

1. \
   a. Dette kan gjøres på flere måter. For eksempel kan en se forrige figur i neste, og peke på hva som er lagt til for å bygge den nye figuren. Vi kan også peke på at figuren består av to deler. En trekant, som står på et rektangel. For å lage neste figur så skyv trekanten opp og legg til en bunn på størrelse $n+1$. Rektangelet skal øke én i høyde og én i bredde også. Dermed må vi legge til $n$ og $n-1$. Totalt legger vi altså til $3n$.
   b. Under er sammenhengen markert. De grønne er forrige figur, det røde er det som legges til i trekanten, det blå er bunnen som legges til i rektangelet, og det gule er siden som legges til i rektangelet. ![Rekursiv sammenheng](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/rekursiv.svg)
   c. Vi kan nå bruke dekomponeringen vi har brukt til å beskrive den rekursive sammenhengen. For figur $P_n$ har vi trekanttall $n+1$ minus toppen. Det gir $T_{n+1}-1 = \frac{(n+1)(n+2)}{2}-1$. Rektangelet er alltid $n(n-1)$, så vi får at den eksplisitte formelen er $\frac{(n+1)(n+2)}{2}-1+n(n-1)$.

#### Middels: Finne flere algebraiske uttrykk til samme figur

1. Dekomponer figuren på minst tre måter. Illustrer dekomponeringene i
    figurene, og beskriv dem algebraisk slik at det er en tydelig
    sammenheng mellom illustrasjon og uttrykk.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image2.png)

2. Under ser du trekantramme nummer fire, samt fem forslag til
    eksplisitt uttrykk for trekantramme nummer $n$.

a.  Hvordan ser de foregående rammene ut?

b.  Hvilke uttrykk stemmer? Argumenter ved hjelp av figuren og ved å
    omforme uttrykkene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-03-20-19-18.png)

   i. $3(n - 1) + 3$
   ii. $(n - 1) + n + (n + 1)$
   iii. $3n$
   iv. $\frac{(n + 1)(n + 2)}{2} - \frac{(n - 2)(n - 1)}{2}$
   v. $3(n + 1) - 3$

##### Løsningsforslag

2. \
   a. Vi kan se for oss at dette er slik trekantrammene utvikler seg
   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-03-20-23-57.png)
   b. Vi ser at med tolkningen i a. så øker figurene med $3$ hver gang. Dermed passer hvertfall iii.\
   Vi ser også at $3(n-1)+3 = 3n - 3 + 3 = 3n$, så dette må også stemme. I figuren kan vi tolke $3(n-1)$ som sideflatene uten hjørnene og $+3$ som hjørnene lagt til (tegn inn selv og let etter egen måte å se dette i figuren). \
   Vi kan tenke på $(n+1) + n + (n-1)$ som hele bunnen av figuren $n+1$ legg til hele venstre side uten nederste hjørne $n$ og legg til hele høyre side uten begge hjørnene $n-1$. Vi ser også algebraisk at dette tilsvarer $3n$ (tegn inn selv!). \
   Vi kan se for oss den siste som å telle alle sidene, inkludert hjørnene ($n+1$ per side). Da overteller vi hvert hjørne ($-3$). Dermed stemmer dette uttrykket også.\
   *Merk*: Det er viktig å tegne selv og forsikre seg om at man forstår sammenhengen mellom uttrykket og figuren. Tegn derfor selv!

#### Avansert: Lage figurer basert på algebraiske uttrykk

1. La $H_{n} = 2 \cdot T_{n + 1} - K_{n - 1}$.

    a.  Illustrer $H_{1}$ til $H_{4}$ ved hjelp av trekant- og kvadrattall.

    b.  Finn eksplisitt uttrykk for $H_{n}$ ved hjelp av *stirre-hardt*-*metoden*.

    c.  Bekreft uttrykket du fant i b. ved å regne ut $2 \cdot T_{n + 1} - K_{n - 1}$.

    d.  Bruk uttrykket fra b. og c. til å lage et nytt figurmønster som matcher formen på uttrykket (stirre-hardt-metoden bare baklengs, altså).

2. En figurtallfølge er gitt ved den rekursive sammenhengen $F_{n} = F_{n - 1} + 2n + 1$, der $F_{1} = 2$.

    a.  Illustrer figur 1-4 slik at det går tydelig frem hvordan figuren
        vokser.

    b.  Finn eksplisitt uttrykk.

3. Den $n$-te figuren i et figurtallmønster har eksplisitt uttrykk
    $G_{n} = 2n^{2} - (n - 2)^{2} + \frac{n(n + 1)}{2}$.
   a. Illustrer figur 1-4 slik at strukturen i det algebraiske uttrykket kommer tydelig frem.
   b. Finn rekursiv sammenheng.

4. Lag figurtall og finn rekursivt uttrykk til følgende eksplisitte sammenheng: $n^{2} + 3n + 1$. Tips: Forsøk å omforme uttrykket slik at du finner uttrykk du kjenner fra før, sånn som trekanttall, kvadrattall eller kvadratsetninga. Hvor mange figurtall klarer du å lage?

##### Løsningsforslag

4. Vi utnytter at vi vet at $n^2 + 2n + 1 = (n+1)^2$. Vi kan derfor skrive om uttrykket som $n^2 + 3n + 1 = n^2 + 2n + 1 +n = (n+1)^2+n$. Nå kan vi enkelt se at tillegget fra figur til figur er $(2n+1) + 1$, der $2n+1$ er økninga av kvadratet $+1$ er økningen fra ledded $n$. Dette gir oss også en enkel oversettelse til en figur, dette overlates til leseren!

### Vurdere arbeid med figurtall med hensyn til læreplanens kjerneelementer og didaktikk knyttet til algebraisk tenkning

#### Middels: Forklare hvordan arbeid med figurtall innebærer algebraisk tenkning og arbeid med kjerneelementene

1. Ta utgangspunkt i Alfas beskrivelse av *algebraisk tenkning* i
    delkapittel 3.1. Gi flere argumenter for at arbeid med figurtall i
    grunnskolen vil innebære algebraisk tenkning for elevene.

2. Les kjerneelementene for matematikk i læreplanen. For hvert
    kjerneelement, argumenter for om arbeid med figurtall innebærer
    arbeid med aktuelle kjerneelementet.

3. Finn kompetansemål i læreplanen som du mener man berører når man
    arbeider med figurtall i skolen. Begrunn.

#### Avansert: Lage og begrunne undervisningsaktiviteter med utgangspunkt i kjerneelementer, kompetansemål og litteratur om algebraisk tenkning

1. Ta utgangspunkt i aktuell litteratur om algebraisk tenkning, samt
    læreplanens kompetansemål og kjerneelementer.

    a.  Lag en undervisningsaktivitet med figurtall for *mellomtrinnet*.

    b.  Begrunn hvordan oppgaven innebærer arbeid med algebraisk
        tenkning og kompetansemålene og kjerneelementene du valgte.

2. Ta utgangspunkt i aktuell litteratur om algebraisk tenkning, samt
    læreplanens kompetansemål og kjerneelementer.

    a.  Lag en undervisningsaktivitet med figurtall for
        *ungdomstrinnet*.

    b.  Begrunn hvordan oppgaven innebærer arbeid med algebraisk
        tenkning og kompetansemålene og kjerneelementene du valgte.


## 24.04

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Gi en grunnskoletilpasset forklaring med eksempel på begrepene faktor og divisor.
2. Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

La $a$ og $b$ være to naturlige tall med største felles faktor $10$ og minste felles multiplum $1050$. Hvis $a = 30$ hva er da $b$? Begrunn.

##### Vurderingskriterier

Studentene må bevare oppgaven på en forståelig og riktig måte. For eksempel kan en bruke at $SFF\cdot MFM = a\cdot b$ og løse dette som en likning. Det gir at $10\cdot 1050 = 10500 = 30\cdot b$, eller at $1050 = 3\cdot b$ eller $b = 350$.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Under ser du en påstand. Undersøk den og begrunn at den stemmer. Du må begrunne  formelt.

Hvis et tall er faktor i to tall, så er det også faktor i differansen mellom de to tallene.

##### Vurderingskriterier

Studenten må besvare oppgaven på en forståelig og riktig måte. Hvis vi antar at $a$ er faktor i to tall kan vi si at disse tallene kan skrives som $an$ og $am$ (og vi kan anta at $n > m$). Ser vi nå på differansen mellom disse tallene ser vi på $an - am$, men siden vi kan faktorisere $a$ får vi at differansen er $a(n-m)$, og siden $n-m$ er et naturlig tall så ser vi at $a$ er en faktor i dette tallet.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva partall og oddetall er.
Forklar og gi eksempler på hva primtall og sammensatt tall er.
Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Gi et formelt argument for at sum av oddetall og oddetall er partall.

2. Gi et grunnskoletilpasset argument for at partall multiplisert med oddetall gir partall.

##### Vurderingskriterier

1. Studenten må gi et formelt argument. Det kan være å skrive to oddetall som $2n-1$ og $2m-1$. Summen er da $2n-1 + 2m-1 = 2n + 2m - 2 = 2(n+m-2)$. Vi ser at summen inneholder faktoren to og derfor er et partall.
2. Studenten må gi et grunnskoletilpasset argument. Her er det flere muligheter. De kan for eksempel gi et generisk eksempel og dra ut strukturen derfra. Ta for eksempel partallet $6$ og oddetallet $9$. Siden $6$ er et partall kan vi skrive det som $2$ ganger noe, i dette tilfellet $3$. Dermed er produktet $6\cdot 9$ også produktet $2\cdot 3 \cdot 9$. Men vi ser nå at vi har en faktor $2$ i produktet. Dermed må dette være et partall. Siden det ikke var noe spesielt med partallet $6$, så ser vi at vi alltid kan dra ut faktoren $2$, slik det ble gjort med $6$ og produktet mellom et partall og oddetall vil derfor alltid inneholde faktoren $2$, noe som gjør det til et partall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Hvis vi skal gange et tosifret tall med $11$, kan vi gjøre det på denne måten, dersom tverrsummen er mindre enn ti: Sett første siffer på hundrerplassen, tverrsummen på tierplassen og andre siffer på enerplassen. Eksempelvis er da $35\cdot 11=385$. Vis at dette er sant for alle tosifra tall med tverrsum lavere enn ti.

##### Vurderingskriterier

Studenten må vise at dette stemmer. En naturlig måte vil være å skrive tallet som $10a+b$ der $a$ og $b$ er siffer og $a+b < 10$. Tar vi tallet vårt ganger $11$ får vi $(10a+b)\cdot 11 = (10a+b)(10+1) = 100a + 10 b + 10 a + b$, eller $100a + 10(a+b) + b$. Dermed ser vi at siden $a$, $b$ og $a+b<10$ første siffer, $a$ være på hundrerplassen, tverrsummen, $a+b$, på tierplassen og andre siffer, $b$, vil være på enerplassen.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Gi en formell begrunnelse for delelighetsregelen for tall som er delelig med 5.
Gi en grunnskoletilpasset begrunnelse for delelighetsregelen for tall som er delelig med 9.

##### Vurderingskriterier

Studenten må besvare begge oppgavene.

Formelt: For eksempel kan de ta utgangspunkt i tre eller firesifra tall
($1000a + 100b + 10c + d$) og gjøre argumentene. Deretter *må* de
peke på hvorfor dette også fungerer for tall med flere siffer. Alternativt kan de skrive et tall som $10n + b$, der $b$ er et siffer og $n$ er et vilkårlig positivt tall. For tallet $2343403$ vil $n = 234340$ og $b = 3$. Dermed kan de nå peke direkte på at siden $10n$ inneholder faktoren $5$, så vil det være $b$, altås siste siffer, som avgjør om tallet er delelig på $5$ eller ikke.

Grunnskoletilpasset: Ta utgangspunkt i et konkret eksempel og
forklare strukturen. Igjen må det komme tydelig fram hvordan
resultatet gjelder for et hvilket som helst antall sifre.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer  $n$, ved hjelp av Gauss-trikset (doble summen) geometrisk.
Utled det eksplisitte uttrykket for kvadrattallene ved hjelp av sum av tillegg.

#### Middels: Ved hjelp av sum av tillegg for andre polygontall

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 5, 12, 22,  \ldots$.

##### Vurderingskriterier

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $3n-2$, som gir at figurtall nummer $n$ kan skrives som summen av tilleggene slik:
$$
P_n = 1 + 4 + 7 + 10 + \ldots + 3n - n.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 8$, $F_2 = 18$ og $F_3 = 32$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-12-10-31.png)

##### Vurderingskriterier

1. Studenten må betrakte figuren og finne en eksplisitt formel ved å referere til figuren. For eksempel kan man ved å betrakte figuren figuren geometrisk kan en se at hvis en flytter trekantene som "stikker ut" tilbake på plass, så får man et rektangel som alltid er dobbelt så høyt som langt og at lengden er én høyere enn figurtallsnummeret. Man ser dermed at $F_1 = 2\cdot 4$, $F_2 = 3\cdot 6$ og $F_3 = 4 \cdot 8$ og generelt at $F_n = (n+1)\cdot 2(n+1) = 2(n+1)^2$.
2. Studenten må bruke teknikken sum av tillegg. Først bør de finne formen på tillegget. Dette kan de for eksempel gjøre ved å bruke den eksplisitte formelen over og se på $F_n - F_{n-1} = 2(n+1)^2 - 2n^2 = 2(n+1+n)(n+1-n) = 2(2n+1)$ eller $4n + 2$. Nå gjenstår bare bruken av teknikken sum av tillegg. Siden vi nå har formen på tilleggene kan vi skrive $F_n = 8 + (4\cdot 2 + 2) + (4\cdot 3 + 2) + \ldots + (4n+2)$. Vi ser også at $8 = 4\cdot 1 + 2 +2$, som gir oss muligheten til å skrive
$$
\begin{aligned}
F_n
& = 2 + (4\cdot 1 + 2) + (4\cdot 2 + 2) + (4\cdot 3 + 2) + \ldots + (4n+2)
\\
&
= 2 + 4(1+2+\ldots + n) + 2\cdot n
\\
&
= 2 + 4T_n +2n
\\
&
2 + 2n(n+1)+2n.
\end{aligned}
$$
Her har vi et eksplisitt uttrykk for figurtall nummer $n$ og studenten trenger ikke omforme dette til å passe med 1., men vi kan se at det gjør det ved å fortsette
$$
\begin{aligned}
2 + 2n(n+1) + 2n
& =
2(1+2n(n+1)+n)
\\
&
=2(n(n+1) + (n+1))
\\
& =
2(n+1)(n+1) = 2(n+1)^2
\end{aligned}
$$

### Finne rekursiv uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk.

i.  Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg.

ii. Her *må* de ta differanse mellom $T_{n}$ og $T_{n - 1}$ og
gjøre regne seg fram til formen på tillegget

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for femkanttallene  $P_n$, der $P_1 =1$, $P_2 = 5$ og $P_3 = 12$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $P_n = {\frac{n}{2}(3n-1)}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med $3$, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning $3$.
Fra dette bør de komme seg til\
$$
P_{n} = P_{n - 1} + 3n-2
$$

ii. Finne uttrykket ved hjelp av å regne $P_{n}– P_{n - 1}$.

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de tre figurtallene $F_1$, $F_2$ og $F_3$

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-12-22-21.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere figurtallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom figurtall nummer $n$ og antall prikker i figurtallet.

2. en rekursiv sammenheng mellom to påfølgende figurtall.

##### Vurderingskriterier

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\

For eksempel kan det fremheves at det er to trekanter som ligger i figuren som starter på samme nivå som figurtallsnummeret, markert i gult i figuren under. Flytter man trekantene sammen får man et rektangel av størrelse $n$ og $n+1$.  Videre kan en da utifra markeringene se hvis en flytter toppene ned i "hullet", markert i grønn, så vil en ha et rektangel med høyde $n$ og bredde $2$. Totalt sett får vi et rektangel med bredde $2 + (n+1)$ og høyde $n$. Som gir en eksplisitt formel $(n+3)\cdot n$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-13-28-48.png)

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-13-26-27.png)

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte figurtallene ned på flere måter, utled to ulike, men likeverdige uttrykk for figurtallene.

##### Vurderingskriterier

De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren. For
eksempel kan de gjøre som i grunnleggende i tillegg til en annen
nedbrytning. Geometrisk kan dette være å peke på en alltid i "midten" har et rektangel med bredde $4$ og høyde $n$ (ved å flytte ned toppene), altså $4n$ prikker i rektangelet i midten. I tillegg stikker det ut to trekanter som for figurtallsnummer $n$ er av størrelse $T_{n-1}$. Disse trekantene kan altså eksplisitt utregnes ved å ta $2T_{n-1} = n(n-1)$. Totalt gir dette det eksplisitte uttrykket $4n + n(n-1)$.  

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 6$, $F_3 = 11$, $F_4 = 17$.

1. Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
2. Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
3. Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

1. Studenten står fritt til hvordan de vil gjøre dette. for eksempel kan de se at vi kan skrive følgen slik, $F_1 = 4+ 1$, $F_2 = 4+3$, $F_3 = 4+6$ og $F_4 = 4+10$. Vi kjenner igjen rekken $1$, $3$, $6$ og $10$ som trekanttallene. Dermed kan vi se at det kun er en trekant i tillegg til noe som konstant er $4$. Da kan en figur se slik ut

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-13-39-36.png)

2. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg. Har de tegnet som figuren over er det nok å peke på at det alltid legges en ny rad på toppen av figuren og at denne alltid inneholder $n$ prikker.

1. Studenten *må* finne formelen på to forskjellige måter. Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter. Siden figuren fra 1. er laget litt taktisk kan en nå se at en enkelt kan bryte den ned til å være $T_n + 4$ som gir formelen $\frac{n(n+1)}{2}+ +4$.


## 31.03.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Gi en grunnskoletilpasset forklaring med eksempel på begrepene faktor og divisor.
2. Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

To tannhjul dreier med ulik hastighet. Det ene bruker 21 sekunder på én omdreining. Du ønsker at det andre skal holde en dreiehastighet slik at dersom de settes i gang på likt, vil de begge kun stå samtidig i utgangsposisjonen hvert 147. sekund. Hva må hastigheten til det andre tannhjulet være, dersom det ikke bruker 147 sekunder per omdreining?

##### Vurderingskriterier

Studentene må bevare oppgaven på en forståelig og riktig måte. Det kan være å innse at $21 = 3\cdot 7$ og at $147 = 7\cdot 7 \cdot 7$. Siden tannhjulene ikke kan stå i samme posisjon før det har gått $147$ sekunder må det andre tannhjulet dreie med en faktor av $147$ eller $21$. Dermed må faktoren være $7\cdot 7$.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Uten å regne det ut, hvordan kan vi vite hvor mange 0'ere, det vil være på slutten av produktet av tallene 1, 2, 3, 4, 5, 6, 7, 8, 9 og 10?

##### Vurderingskriterier

Studenten må besvare oppgaven på en forståelig og riktig måte. Dette kan være ved å peke på at $2\cdot 5 \cdot 10 = 100$. Derfor må det minst være to 0'ere. Deretter kan de peke på at det ikke kan være flere 0'ere, fordi da måtte $1000$ vært en faktor i produktet, noe som ville krevd en ekstra faktor $5$ som ikke er der.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva partall og oddetall er.
Forklar og gi eksempler på hva primtall og sammensatt tall er.
Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Gi et grunnskoletilpasset argument for at sum av oddetall og partall er oddetall.

2. Gi et formelt argument for at oddetall multiplisert med oddetall gir oddetall.

##### Vurderingskriterier

1. Studenten må gi en forklaring som kan passe på grunnskolen. Dette kan innebære å lage illustrasjoner. For eksempel kan en illustrere et partall som noe som kommer i par og et oddetall som to rader der en er én høyere. Da kan en peke til figuren å si at når man legger sammen figurene på hverandre vil man fortsatt ha én som er en høyere. Dermed fortsatt ett oddetall.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-12-14-25.png)

2. Studenten bør få fram at to oddetall kan skrives som $2n+1$ og $2m+1$ der $m$ og $n$ er to vilkårlige naturlige tall. Dermed blir produktet $(2n-1)(2m-1) = 2mn-2n-2m+1 = 2(mn-n-m)+1$. Dette er altså noe én over et partall og må derfor fortsatt være et oddetall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Hvis vi ønsker å undersøke manuelt om et tall $n$ er prim eller sammensatt, er det ikke nødvendig å lete etter faktorer i $n$ som er høyere enn $\sqrt n$. Forklar hvorfor.

##### Vurderingskriterier

Studenten må gi en strukturert og logisk forklaring på hvorfor $\sqrt n$ er det høyeste tallet en trenger å sjekke.  

Dette handler i hovedsak om å peke på at faktorer (som ikke er $1$ eller tallet selv) kommer i par.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Gi en formell begrunnelse for delelighetsregelen for tall som er delelig med 4.
Gi en grunnskoletilpasset begrunnelse for delelighetsregelen for tall som er delelig med 9.

##### Vurderingskriterier

1. Studenten kan for eksempel peke på at alle tall kan skrives som $100a + b$, der $a$ er et vilkårlig naturlig tall og $b$ er et vilkårlig tosifret tall. For eksempel vil 26 tilsvare $a = 0 $ og $b = 26$, mens $152324$ kan deles opp i $a = 1523$ og $b = 24$. Siden $100a = 4\cdot 25 a$ som er delelig på fire, vil tallet $100a + b$ kun være delelig på fire når $b$ er det. Hvis $b$ ikke er delelig på fire vil heller ikke $100a + b$ være delelig på fire. Dermed ser vi at tall er delelig på fire hvis, og bare hvis, de to siste sifrene i tallet er delelig på fire.
2. Her må studenten gjøre et grunnskoletilpasset argument. Det kan være å peke på et konkret tall og dra ut strukturen derfra. For eksempel kan vi se på tallene $124$ og $621$. Tallene kan vi dele opp slik $124 = 1\cdot 100 + 2\cdot 10 + 4 = (99+1) + (9+1)\cdot 2 + 4 = (99+2\cdot 9) + 1 + 2 +4$ og $631 = 6\cdot 100 + 3 \cdot 10 + 1 = 6(99+1) + 2(9+1)+1 = (6\cdot 99 + 2\cdot 9) + 6+ 2 +1 $. I begge tilfellene ser vi at første del er delelig med 9 alltid og at vi har klart å skille ut tverrsummen fra tallene. Siden $1+2+4 = 7$ som ikke er delelig på 9 kan tallet $124$ ikke være delelig på 9, mens $6+2+1 = 9$ er delelig med 9 som gjør at tallet $621$ også må være delelig med 9. Videre må studenten trekke ut strukturen fra eksemplene. Dette kan gjøres ved å peke på at det vi har gjort ikke er unikt våre tresifrede tall. Det ville faktisk fungert for alle tall fordi $9, 99, 999, 9999, 99999, \ldots$ alltid er delelig på 9. Derfor kan vi alltid trekke ut tverrsummen slik vi har gjort, noe som gjør at det er tverrsummen som alltid vil avgjøre om tallet er delelig på 9 eller ei.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer  $n$, ved hjelp av Gauss-trikset (doble summen) geometrisk.
Utled det eksplisitte uttrykket for kvadrattallene ved hjelp av sum av tillegg.

##### Vurderingskriterier

Studentene må besvare begge spørsmålene med riktig teknikk (se heftet).

#### Middels: Ved hjelp av sum av tillegg for andre polygontall

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 6, 15, 28,  \ldots$.

##### Vurderingskriterier

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $4n-3$, som gir at figurtall nummer $n$ kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 5 + 9 + 13 + \ldots + 4n - 3.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 7$, $F_2 = 12$ og $F_3 = 18$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-12-43-49.png)

##### Vurderingskriterier

Ved å betrakte figuren bør studentene se at figuren kan skrives som $F_1 = 3+ 4$, $F_2 = 3 + 4 + 5$, $F_3 = 3+4+5+6$ og generelt $F_n = 3+4+5+\ldots + n+3$. Formen på tillegget er dermed $n+3$. Videre må de nå bare bruke riktig teknikk for å komme i mål. Her kan de se i heftet for mer info om teknikkene.

### Finne rekursiv uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk.

i.  Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg.

ii. Her *må* de ta differanse mellom $T_{n}$ og $T_{n - 1}$ og
gjøre regne seg fram til formen på tillegget

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene  $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $H_n = {n(2n-1)}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med $4$, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning $4$.
Fra dette bør de komme seg til\
$$
H_{n} = H_{n - 1} + 4n-3
$$

ii. Finne uttrykket ved hjelp av å regne $H_{n}– H_{n - 1}$.

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de fire første trappetallene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-12-48-55.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere trappetallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom trappetall nummer $n$ og antall prikker i trappetallet.

2. en rekursiv sammenheng mellom to påfølgende trappetall.

##### Vurderingskriterier

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\

For eksempel kan det fremheves at det er to forskjøvede trekanter som ligger på hverandre. Trekantene deler også sitt andre ledd (det er første figur). Vi har altså to trekanttall, som mangler topp og deler en side som alltid har lengde $2$. Trekanttallet starter også "en før" som betyr at vi har $2T_{n+1}-2-2 = (n+2)(n+1)-4$. Denne måten å bryte ned problemet på gjør at studenten også kan innse at figuren øker med $2(n+1)$ hver gang. Dermed må den rekursive formelen være $F_n = F_{n-1}+2(n+1)$ der $F_1 = 2$.

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte trappetallene ned på flere måter, utled to ulike, men likeverdige uttrykk for trappetallene.

##### Vurderingskriterier

De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren. For
eksempel kan de gjøre som i grunnleggende i tillegg til en annen
geometrisk nedbrytning. Eventuelt kan de bruke andre teknikker
(se heftet for teknikker). Blant annet kan de analysere
tallfølgen og finne eksplisitt uttrykk ved hjelp av sum av
tillegg.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 6$, $F_3 = 11$, $F_4 = 17$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter

## 17.02.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Gi en grunnskoletilpasset forklaring med eksempel på begrepene faktor og divisor.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

To tannhjul dreier med ulik hastighet. Det ene bruker 15 sekunder på én omdreining. Du ønsker at det andre skal holde en dreiehastighet slik at dersom de settes i gang på likt, vil de begge stå i utgangsposisjonen hvert 105. sekund. Hva må hastigheten til det andre tannhjulet være?

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

1. Hvis vi ønsker å undersøke manuelt om et tall $n$ er prim eller sammensatt, er det ikke nødvendig å lete etter faktorer i $n$ som er høyere enn $\sqrt n$. Forklar hvorfor.

##### Vurderingskriterier: Grunnleggende {#f17g1}

Studenten må besvare alle spørsmålene.  

Det skal gis *både* formell og uformell forklaring.  
Formelt: Algebraisk.
Grunnskoletilpasset: med ord og/eller illustrasjoner

##### Vurderingskriterier: Middels {#f17m1}

Studenten må besvare oppgaven på en forståelig og riktig måte.

##### Vurderingskriterier: Avansert {#f17a1}

Studenten må gi en strukturert og logisk forklaring på hvorfor $\sqrt n$ er det høyeste tallet en trenger å sjekke.  

Dette handler i hovedsak om å peke på at faktorer (som ikke er $1$ eller tallet selv) kommer i par.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene {#123}

Forklar og gi eksempler på hva partall og oddetall er.
Forklar og gi eksempler på hva primtall og sammensatt tall er.
Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#d21}

1. Gi et grunnskoletilpasset argument for at sum av oddetall og oddetall er partall.

2. Gi et formelt argument for at oddetall multiplisert med oddetall gir oddetall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene {#12asd}

Hvis vi finner alle faktorene i kvadrattallene ser vi at det er et odde antall faktorer. Forklar alle tall, bortsett fra kvadrtattallene, har et partall antall faktorer.

##### Vurderingskriterier: Grunnleggende {#f17g2}

Studenten må besvare alle spørsmålene.  

Besvarelsene må inneholde, forklaringer, eksempler, definisjoner og
illustrasjoner der dette påpekes i oppgaveteksten.

##### Vurderingskriterier: Middels {#f17m2}

Studenten må besvare alle oppgavene.

Formelt: Ved hjelp av algebra.

Grunnskoletilpasset: Kan gjøres ved hjelp av et talleksempel der
de drar ut strukturer/egenskaper som forklarer hvorfor det
gjelder generelt (generisk eksempel). Kan også gjøres
visuelt/ved hjelp av en figur; også da er det viktig at
illustrasjonen viser strukturer/egenskaper som får frem hvorfor
sammenhengen gjelder generelt (se heftet for eksempler).

##### Vurderingskriterier: Avansert {#f17a2}

Studenten må i besvarelsen få fram tydelig hvorfor dette alltid
gjelder.  

En naturlig besvarelse vil være å peke på at faktorene i et tall alltid kommer i par. På denne måten kan studenten få fram at kvadrattallene er (per definisjon) de tallene der to *like* faktorer er parret sammen. Det er denne egenskapen som må tas tak i.  

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#123s}

Gi en formell begrunnelse for delelighetsregelen for tall som er delelig med 5.
Gi en grunnskoletilpasset begrunnelse for delelighetsregelen for tall som er delelig med 3.

##### Vurderingskriterier: Middels

Studenten må besvare begge oppgavene.

Formelt: Ta utgangspunkt i tre eller firesifra tall
($1000a + 100b + 10c + d$) og gjøre argumentene. Deretter *må* de
peke på hvorfor dette også fungerer for tall med flere siffer.

Grunnskoletilpasset: Ta utgangspunkt i et konkret eksempel og
forklare strukturen. Igjen må det komme tydelig fram hvordan
resultatet gjelder for et hvilket som helst antall sifre.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen) geometrisk.
Utled det eksplisitte uttrykket for kvadrattallene ved hjelp av sum av tillegg.

#### Middels: Ved hjelp av sum av tillegg for andre polygontall

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 6, 15, 28,  \ldots$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 2$, $F_2 = 8$ og $F_3 = 16$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-40-43.png)

##### Vurderingskriterier: Grunnleggende {#f17g4}

Studentene må besvare begge spørsmålene med riktig teknikk (se heftet).

##### Vurderingskriterier: Middels {#f17m4}

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $4n-3$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 5 + 9 + 13 + \ldots + 4n - 3.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).

##### Vurderingskriterier: Avansert {#f17a4}

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel. For eksempel kan det pekes på at figuren nesten er to trekanter som starter *en før* (altså $T_{n+1}$) lagt opp på hverandre. Begge mangler bare toppen og deler rad 2. Dermed får vi $F_n = 2T_{n+1} - 2- 2 = (n+2)(n+1) - 4 $

ii. Her må de igjen bruke sum av tillegg som på middels.

### Finne rekursivt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene  $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $H_n = {n(2n-1)}$.

I begge oppgavene bes det om to teknikker. Se heftet for *differanse
mellom eksplisitte uttrykk* og *form på tillegg*.

##### Vurderingskriterier: Grunnleggende {#f17G5}

Studenten må besvare alle spørsmålene med riktig
teknikk.

i.  Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg.

ii. Her *må* de ta differanse mellom $T_{n}$ og $T_{n - 1}$ og
gjøre regne seg fram til formen på tillegget

##### Vurderingskriterier: Middels {#f17m5}

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med $4$, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning $4$.
Fra dette bør de komme seg til\
$$
H_{n} = H_{n - 1} + 4n-3
$$

ii. Finne uttrykket ved hjelp av å regne $H_{n}– H_{n - 1}$.

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de fire første ambolttallene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-41-25.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere ambolttallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom ambolttall nummer $n$ og antall prikker i ambolttallet.

2. en rekursiv sammenheng mellom to påfølgende ambolttall.

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte ambolttallene ned på flere måter, utled to ulike, men likeverdige uttrykk for ambolttallene.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 6$, $F_3 = 11$, $F_4 = 17$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier: Grunnleggende {#f17g6}

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

##### Vurderingskriterier: Middels {#f17m6}

De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren. For
eksempel kan de gjøre som i grunnleggende i tillegg til en annen
geometrisk nedbrytning. Eventuelt kan de bruke andre teknikker
(se heftet for teknikker). Blant annet kan de analysere
tallfølgen og finne eksplisitt uttrykk ved hjelp av sum av
tillegg.

##### Vurderingskriterier: Avansert {#f173a6}

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter

## 13.02.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum {#12edfasd}

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene {#12312e}

Gi en grunnskoletilpasset forklaring med eksempel på begrepene faktor og divisor.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#12dvsdv}

1. Forklar hvorfor ingen summer av fire påfølgende naturlige tall har felles faktor  $4$.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Du får vite at største felles faktor for to tall $A$ og $B$ er $210$ og at tallet $A$ er $1260$.

1. Hva er minste mulige verdi for $B$, hvis $B$ ikke er $210$?

##### Vurderingskriterier: Grunnleggende {#f13g1}

Studenten må besvare alle spørsmålene.  

Det skal gis *både* formell og uformell forklaring.  
Formelt: Algebraisk.
Grunnskoletilpasset: med ord og/eller illustrasjoner

##### Vurderingskriterier: Middels {#f13m1}

Studenten må gjøre følgende for å få godkjent.

Det må gis en forklaring på hvorfor dette alltid er
tilfellet.
For eksempel kan en peke på at
$0 + 1 + 2 + 3 = 6 = 1 \cdot 4 + 2$. Skal vi nå til «neste i
rekka», må vi legge til 1 på hvert tall i summen, dvs
$(0 + 1) + (1 + 1) + (2 + 1) + (3 + 1) + = (1\cdot 4 + 2) + 4 = 2 \cdot 4 + 2$.
Skal vi begynne på for eksempel 256, må vi legge til 256 på
alle. Det gir
$(0 + 256) + (1 + 256) + (2 + 256) + (3 + 256) =  (1\cdot 4 + 2) + 4 \cdot 256 = 256\cdot 4 + 2$.
Vi ser altså at dette alltid ligger to over noe i firegangen, uansett hvilket
naturlig tall vi starter på. Dermed kan ingen summer av fire
påfølgende naturlige tall ha faktor 4.

##### Vurderingskriterier: Avansert {#f13a1}

Studenten må gi en strukturert og logisk forklaring på hva
minste $B$ må være.  

For eksempel kan en først peke på at
$A = 6 \cdot 210$. Siden $B$ ikke skal være 210, må den
inneholde minst én faktor til (og nøyaktig én å være minst
mulig). Vi ser at $A$ inneholder 2 og 3 i tillegg til $210$, så
$B$ må inneholde faktoren $\ 5$. Dermed må $B = 5 \cdot 210$.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall {#123asdf}

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene {#asasd}

Forklar og gi eksempler på hva partall og oddetall er.
Forklar og gi eksempler på hva primtall og sammensatt tall er.
Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#123asd}

1. Gi et formelt argument for at sum av oddetall og partall er oddetall.

2. Gi et grunnskoletilpasset argument for at oddetall multiplisert med oddetall gir oddetall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene {#12dsdv}

Alle naturlige tall kan beskrives relativ til et tall i tre-gangen. Noen tall er i tre-gangen ($3, 6, 9, \ldots, 3n, \ldots$), noen er én mer enn et tall i tre-gangen ($1, 4, 7, \ldots, 3n +1, \ldots$), resten er to mer enn tall i tre-gangen ($2, 5, 8, \ldots, 3n+2, \ldots $). Forklar hvorfor alle kvadrattall enten er i tre-gangen eller én mer enn et tall i tre-gangen. (Merk: Kvadrattallene er alle tallene på formen $n^2$)

##### Vurderingskriterier: Grunnleggende {#f13g2}

Studenten må besvare alle spørsmålene.  

Besvarelsene må inneholde, forklaringer, eksempler, definisjoner og
illustrasjoner der dette påpekes i oppgaveteksten.

##### Vurderingskriterier: Middels {#f13m2}

Studenten må besvare alle oppgavene.

Formelt: Ved hjelp av algebra.

Grunnskoletilpasset: Kan gjøres ved hjelp av et talleksempel der
de drar ut strukturer/egenskaper som forklarer hvorfor det
gjelder generelt (generisk eksempel). Kan også gjøres
visuelt/ved hjelp av en figur; også da er det viktig at
illustrasjonen viser strukturer/egenskaper som får frem hvorfor
sammenhengen gjelder generelt (se heftet for eksempler).

##### Vurderingskriterier: Avansert {#f13a2}

Studenten må i besvarelsen få fram tydelig hvorfor dette alltid
gjelder.  

En naturlig løsning kan være å splitte i tre
tilfeller:

i. Alle tall som er i tre er på formen $3n$.
Kvadratttallene som har opphav fra disse tallene er derfor
$(3n)^{2} = 9n^{2} = 3\cdot (3n^{2})$, noe i tregangen

ii. Alle tall som er én over tregangen er på formen $3n + 1$.
Kvadrattallene som har opphav fra disse tallene er derfor
$(3n + 1)^{2} = 9n^{2} + 6n + 1 = 3\left( 3n^{2} + 2n \right) + 1$,
altså noe én over noe i tregangen.

iii. Alle tall som er to over noe i tregangen er på formen
$3n + 2$. Kvadrattallene som har oppgav fra disse tallene
er derfor
$(3n + 2)^{2} = 9n^{2} + 12n + 4 = 3\left( 3n^{2} + 4n + 1  \right) + 1$,
altså noe én over noe i tregangen.

Da dette dekker alle mulige kvadrattall har vi nå vist at de
enten er i tregangen eller er én over noe i tregangen.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9 {#12eassadd}

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#12esdfzxcv}

Gi en formell begrunnelse for delelighetsregelen for tall som er delelig med 4.
Gi en grunnskoletilpasset begrunnelse for delelighetsregelen for tall som er delelig med 3.

##### Vurderingskriterier: Middels

Studenten må besvare begge oppgavene.

Formelt: Ta utgangspunkt i tre eller firesifra tall
($1000a + 100b + 10c + d$) og gjøre argumentene. Deretter *må* de
peke på hvorfor dette også fungerer for tall med flere siffer.

Grunnskoletilpasset: Ta utgangspunkt i et konkret eksempel og
forklare strukturen. Igjen må det komme tydelig fram hvordan
resultatet gjelder for et hvilket som helst antall sifre.

### Finne eksplisitt uttrykk for figurtall {#1asddc}

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall {#12eqsdasc}

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen) geometrisk.
Utled det eksplisitte uttrykket for kvadrattallene ved hjelp av sum av tillegg.

#### Middels: Ved hjelp av sum av tillegg for andre polygontall {#d1dasca}

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 6, 15, 28,  \ldots$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall {#dascxc}

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 3$, $F_2 = 13$ og $F_3 = 31$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-37-18.png)

##### Vurderingskriterier: Grunnleggende {#f13g4}

Studentene må besvare begge spørsmålene med riktig teknikk (se heftet).

##### Vurderingskriterier: Middels {#f13m4}

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $4n-3$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 5 + 9 + 13 + \ldots + 4n - 3.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).

##### Vurderingskriterier: Avansert {#f13a4}

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel. For eksempel kan en innse at de to ytterste firkantene er $n^2$, mens det skrå kvadratet kan deles inn i to "lag" som gir $n^2$ for det ene og $(n-1)^2$ for det andre. Totalt blir dette $2n^2+n^2 + (n-1)^2 $.

ii. Her må de igjen bruke sum av tillegg som på middels.

### Finne rekursivt uttrykk for figurtall {#dzvxcb}

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall {#dasczxcad}

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall {#wdaxc}

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-37-44.png)

Over ser du de tre første figurene i bikubetallene. Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for bikubetallene $B_n$, der $B_1 =1$, $H_2 = 7$ og $H_3 = 19$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $B_n = {3n(n-1)}+1$.

I begge oppgavene bes det om to teknikker. Se heftet for *differanse
mellom eksplisitte uttrykk* og *form på tillegg*.

##### Vurderingskriterier: Grunnleggende {#f13G5}

Studenten må besvare alle spørsmålene med riktig
teknikk.

i.  Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg.

ii. Her *må* de ta differanse mellom $T_{n}$ og $T_{n - 1}\ $og
gjøre regne seg fram til formen på tillegget

##### Vurderingskriterier: Middels {#f13m5}

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med 6, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning 6.
Fra dette bør de komme seg til\
$$
B_{n} = B_{n - 1} + 6n
$$

ii. Finne uttrykket ved hjelp av å regne $B_{n}–\ B_{n - 1}\ $

### Beskrive oppbygningen av figurtall (alle typer) {#dzxcvsdv}

Under ser dere dere de tre første bokstallene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-38-06.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon {#wdac}

Ved å illustrere bokstallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom bokstall nummer $n$ og antall prikker i bokstallet.

2. en rekursiv sammenheng mellom to påfølgende bokstall.

#### Middels: Finne flere algebraiske uttrykk til samme figur {#dascsdvbq}

Ved å bryte bokstallene ned på flere måter, utled to ulike, men likeverdige uttrykk for bokstall.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger {#wdacdsasc}

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 1$, $F_2 = 6$, $F_3 = 14$, $F_4 = 25$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier: Grunnleggende {#f13g6}

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
For eksempel kan det pekes på at det er et kvadrat med oddetalls sidelengde. Generelt er sidelengden $2n+1$. I tillegg trekkes det fra fire trekanttall som *starter* en senere, altså trekkes det fra $4T_{n-1}$.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

##### Vurderingskriterier: Middels {#f13m6}

De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren. For
eksempel kan de gjøre som i grunnleggende i tillegg til en annen
geometrisk nedbrytning. Eventuelt kan de bruke andre teknikker
(se heftet for teknikker). Blant annet kan de analysere
tallfølgen og finne eksplisitt uttrykk ved hjelp av sum av
tillegg.

##### Vurderingskriterier: Avansert {#f13a6}

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter

## 10.02.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum {#wdasccc}

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene {#wdascd}

Forklar og gi eksempler på hva som menes med begrepene faktor og divisor. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#dascavqc}

1. Forklar hvorfor alle summer av fem påfølgende naturlige tall har felles faktor  $5$.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene {#wdascfqwc}

Du får vite at største felles faktor for to tall $A$ og $B$ er $210$ og at tallet $A$ er $1260$.

Hva er minste mulige verdi for $B$, hvis $B$ ikke er $210$?

##### Vurderingskriterier: Grunnleggende

Studenten må besvare alle spørsmålene.  

Det skal gis *både* formell og uformell forklaring.  
Formelt: Algebraisk.
Grunnskoletilpasset: med ord og/eller illustrasjoner

##### Vurderingskriterier: Middels

Studenten må gjøre følgende for å få godkjent.

Det må gis en forklaring på hvorfor dette alltid er
tilfellet.
For eksempel kan en peke på at
$0 + 1 + 2 + 3 + 4 = 10 = 2 \cdot 5$. Skal vi nå til «neste i
rekka», må vi legge til 1 på hvert tall i summen, dvs
$(0 + 1) + (1 + 1) + (2 + 1) + (3 + 1) + (4 + 1) = \ 10 + 5 = 2 \cdot 5 + 5$.
Skal vi begynne på for eksempel 256, må vi legge til 256 på
alle. Det gir
$(0 + 256) + (1 + 256) + (2 + 256) + (3 + 256) + (4 + 256) = 10 + 5 \cdot 256$.
Vi ser altså at dette alltid vil fungere, uansett hvilket
naturlig tall vi starter på. Dermed må alle summer av fem
påfølgende naturlige tall ha felles faktor 5.

##### Vurderingskriterier: Avansert

Studenten må gi en strukturert og logisk forklaring på hva
minste $B$ må være.  

For eksempel kan en først peke på at
$A = 6 \cdot 210$. Siden $B$ ikke skal være 210, må den
inneholde minst én faktor til (og nøyaktig én å være minst
mulig). Vi ser at $A$ inneholder 2 og 3 i tillegg til $210$, så
$B$ må inneholde faktoren $\ 5$. Dermed må $B = 5 \cdot 210$.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall {#wdqwd}

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene {#wdasdq}

Forklar og gi eksempler på hva partall og oddetall er.
Forklar og gi eksempler på hva primtall og sammensatt tall er.
Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#qwe15ref}

1. Gi et grunnskoletilpasset argument for at sum av oddetall og oddetall er partall.

2. Gi et formelt argument for at oddetall multiplisert med oddetall gir oddetall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene {#1232tgsdv}

Alle naturlige tall kan beskrives relativ til et tall i fire-gangen. Noen tall er i fire-gangen ($4, 8, 12, \ldots, 4n, \ldots$), noen er én mer enn et tall i fire-gangen ($1, 5, 9, \ldots, 4n +1, \ldots$), noen er to mer enn tall i fire-gangen, og noen er tre mer enn tall i firegangen. Forklar hvorfor alle kvadrattall enten er i firegangen eller én mer enn et tall i fire-gangen. (Merk: Kvadrattallene er alle tallene på formen $n^2$)

##### Vurderingskriterier: Grunnleggende {#g2}

Studenten må besvare alle spørsmålene.  

Besvarelsene må inneholde, forklaringer, eksempler, definisjoner og
illustrasjoner der dette påpekes i oppgaveteksten.

##### Vurderingskriterier: Middels {#m2}

Studenten må besvare alle oppgavene.

Formelt: Ved hjelp av algebra.

Grunnskoletilpasset: Kan gjøres ved hjelp av et talleksempel der
de drar ut strukturer/egenskaper som forklarer hvorfor det
gjelder generelt (generisk eksempel). Kan også gjøres
visuelt/ved hjelp av en figur; også da er det viktig at
illustrasjonen viser strukturer/egenskaper som får frem hvorfor
sammenhengen gjelder generelt (se heftet for eksempler).

##### Vurderingskriterier: Avansert {#a2}

Studenten må i besvarelsen få fram tydelig hvorfor dette alltid
gjelder.  

En naturlig løsning kan være å splitte i fire
tilfeller:

i. Alle tall som er i firegangen er på formen $4n$.
Kvadratttallene som har opphav fra disse tallene er derfor
$(4n)^{2} = 16n^{2} = 4 \cdot (4n^{2})$, noe i firegangen

ii. Alle tall som er én over firegangen er på formen $4n + 1$.
Kvadrattallene som har opphav fra disse tallene er derfor
$(4n + 1)^{2} = 16n^{2} + 8n + 1 = 4\left( 4n^{2} + 2n \right) + 1$,
altså noe én over noe i firegangen.

iii. Alle tall som er to over noe i firegangen er på formen
$4n + 2$. Kvadrattallene som har oppgav fra disse tallene
er derfor
$(4n + 2)^{2} = 16n^{2} + 16n + 4 = 4\left( 6n^{2} + 4n + 1 \right)$,
altså noe i firegangen

iv. Alle tall som er tre over noe i firegangen er på formen
$4n + 3$. Kvadrattallene som har opphav fra disse tallene er
derfor
$(4n + 3)^{2} = 16n^{2} + 24n + 8 + 1 = \ 4\left( 4n^{2} + 6n + 2 \right) + 1$,
altså noe én over noe i firegangen.

Da dette dekker alle mulige kvadrattall har vi nå vist at de
enten er i firegangen eller er én over noe i firegangen.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9 {#12esdvczxc}

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene {#12easczxvb}

Begrunn delelighetsregelen for tall som er delelig med 4. Du må gi en formell  begrunnelse.
Begrunn delelighetsregelen for tall som er delelig med 9. Du må gi en grunnskoletilpasset begrunnelse.

##### Vurderingskriterier: Middels

Studenten må besvare begge oppgavene.

Formelt: Ta utgangspunkt i tre eller firesifra tall
($1000a + 100b + 10c + d$) og gjøre argumentene. Deretter *må* de
peke på hvorfor dette også fungerer for tall med flere siffer.

Grunnskoletilpasset: Ta utgangspunkt i et konkret eksempel og
forklare strukturen. Igjen må det komme tydelig fram hvordan
resultatet gjelder for et hvilket som helst antall sifre.

### Finne eksplisitt uttrykk for figurtall {#213gxc}

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall {#124df14}

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen) geometrisk.
Utled det eksplisitte uttrykket for kvadrattallene ved hjelp av sum av tillegg.

#### Middels: Ved hjelp av sum av tillegg for andre polygontall {#12eaf132r}

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 5, 12, 22, \ldots$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall {#123easczxc}

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 12$, $F_2 = 26$ og $F_3 = 44$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-34-41.png)

##### Vurderingskriterier: Grunnleggende {#g4}

Studentene må besvare begge spørsmålene med riktig teknikk (se heftet).

##### Vurderingskriterier: Middels {#m4}

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $3n-2$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 4 + 7 + 10 + \ldots + 3n - 2.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).

##### Vurderingskriterier: Avansert {#a4}

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel.

ii. Her må de igjen bruke sum av tillegg som på middels.

### Finne rekursivt uttrykk for figurtall {#d12ddasd}

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall {#123easczxc}

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall {#12easczxc}

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for sekskanttallene er $H_n = {n(2n-1)}$.

I begge oppgavene bes det om to teknikker. Se heftet for *differanse
mellom eksplisitte uttrykk* og *form på tillegg*.

##### Vurderingskriterier: Grunnleggende {#G5}

Studenten må besvare alle spørsmålene med riktig
teknikk.

i.  Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg.

ii. Her *må* de ta differanse mellom $T_{n}$ og $T_{n - 1}\ $og
gjøre regne seg fram til formen på tillegget

##### Vurderingskriterier: Middels {#m5}

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med 4, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning 4.
Fra dette bør de komme seg til\
$$
H_{n} = H_{n - 1} + 4n - 3
$$

ii. Finne uttrykket ved hjelp av å regne $H_{n}–\ H_{n - 1}\ $

### Beskrive oppbygningen av figurtall (alle typer) {#123asc}

Under ser dere dere de tre første sommerfugltallene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-35-28.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere sommerfugltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i sommerfugltallet.

2. en rekursiv sammenheng mellom to påfølgende sommerfugltall.

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte sommerfugltallene ned på flere måter, utled to ulike, men likeverdige uttrykk for sommerfugltallene.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 8$, $F_3 = 16$, $F_4 = 26$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier: Grunnleggende {#g6}

Her må alle spørsmålene besvares, og de må
illustrere figurer. *Merk* at figuren ikke øker på en naturlig måte da *stammen* ikke passer inn i et godt mønster.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
For eksempel kan det pekes på at det er fire kvadrater som
overlapper på 2 plasser, i tillegg til 2 trekanter og en
konstant stamme på 10.  
\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

##### Vurderingskriterier: Middels {#m6}

*Merk* at figuren ikke øker på en naturlig måte da *stammen* ikke passer inn i et godt mønster. \
\
De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren. For
eksempel kan de gjøre som i grunnleggende i tillegg til en annen
geometrisk nedbrytning. Eventuelt kan de bruke andre teknikker
(se heftet for teknikker). Blant annet kan de analysere
tallfølgen og finne eksplisitt uttrykk ved hjelp av sum av
tillegg.

##### Vurderingskriterier: Avansert {#a6}

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter

## 03.02.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva som menes med begrepene faktor og divisor. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med felles faktor og største felles faktor for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med begrepet multiplum. Besvarelsen må inneholde både formell definisjon og grunnskoletilpasset forklaring.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor summen av tre påfølgende naturlige tall har en felles faktor.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Undersøk og begrunn følgende påstand.

Når vi deler et tall på et annet, får vi en rest som er mellom 0 og tallet vi deler på. Enhver felles faktor for de to tallene i divisjonen er også en faktor i resten.

##### Vurderingskriterier: Grunnleggende {#f123g1}

Her må alle spørsmålene besvares. Det skal gis
*både* formell og uformell forklaring. Formelt: Algebraisk.
Grunnskoletilpasset: med ord og/eller illustrasjoner

##### Vurderingskriterier: Middels {#f123m1}

Her må strukturen komme fram. Dette kan gjøres
algebraisk eller med et konkret talleksempel, men det er viktig
at de peker på den generelle strukturen som gjør at påstanden
stemmer.

##### Vurderingskriterier: Avansert {#f13as1}

Enten gjøre algebra ved å skrive tallene som *ca* og *cb* og
forklare påstanden derifra. Eller med et talleksempel som får
fram hvorfor det alltid gjelder!

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva et naturlig tall er.
Forklar og gi eksempler på hva partall og oddetall er. Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.
Forklar og gi eksempler på hva primtall og sammensatt tall er.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Gi et formelt og et grunnskoletilpasset argument for at sum av oddetall og oddetall er partall.

2. Gi et formelt og et grunnskoletilpasset argument for at oddetall multiplisert med oddetall gir oddetall.

##### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Alle naturlige tall kan beskrives relativ til et tall i fire-gangen. Noen tall er i fire-gangen, noen er én mer enn et tall i fire-gangen, noen er to mer enn tall i fire-gangen, osv. Forklar hvorfor alle primtall bortsett fra 2 er enten én mer eller én mindre enn et tall i fire-gangen.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Begrunn delelighetsregelen for tall som er delelig med 5. Du må gi både en formell og en grunnskoletilpasset begrunnelse.
Begrunn delelighetsregelen for tall som er delelig med 3. Du må gi både en formell og en grunnskoletilpasset begrunnelse.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen):
geometrisk
algebraisk

#### Middels: Ved hjelp av sum av tillegg for andre polygontall

Illustrer syvkanttallene opp til $H_3$, og utled eksplisitt uttrykk for $H_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 7, 18, 34, \ldots$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 4$, $F_2 = 10$ og $F_3 = 19$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-31-42.png)

### Finne rekursivt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for trekanttall er $\frac{n\cdot(n+1)}{2}$.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for sekskanttallene er $H_n = {n(2n-1)}$.

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de tre første piltallene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-32-20.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere piltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i piltallet.

2. en rekursiv sammenheng mellom to påfølgende piltall.

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte piltallene ned på flere måter, utled to ulike, men likeverdige uttrykk for piltallene.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 6$, $F_2 = 12$, $F_3 = 20$, $F_4 = 30$ og $F_5 = 42$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

## 27.01.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva som menes med begrepene faktor og divisor. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med felles faktor og største felles faktor for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med begrepet multiplum. Besvarelsen må inneholde både formell definisjon og grunnskoletilpasset forklaring.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor produktet av største felles faktor og minste feles multiplum for to tall er det samme som produktet av de to tallene.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Hvis vi skal gange et tosifret tall med $11$, kan vi gjøre det på denne måten, dersom tverrsummen er mindre enn ti: Sett første siffer på hundrerplassen, tverrsummen på tierplassen og andre siffer på enerplassen. Eksempelvis er da $35\cdot 11=385$. Vis at dette er sant for alle tosifra tall med tverrsum lavere enn ti.

##### Vurderingskriterier: Grunnleggende {#f123gs1}

Grunnleggende: Her må alle spørsmålene besvares. Det skal gis
*både* formell og uformell forklaring. Formelt: Algebraisk.
Grunnskoletilpasset: med ord og/eller illustrasjoner.

##### Vurderingskriterier: Middels {#f1s23m1}

Her må strukturen komme fram. Dette gjøres gjerne ved
et konkret talleksempel, men det er viktig at de peker på den
generelle strukturen som gjør at sff\*mfm = a\*b

##### Vurderingskriterier: Avansert {#f1s3as1}

Her må de skrive tosifra tall som a\*10 + b og deretter gjøre
noe algebra.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler på hva et naturlig tall er.
Forklar og gi eksempler på hva partall og oddetall er. Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.
Forklar og gi eksempler på hva primtall og sammensatt tall er.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Gi et formelt og et grunnskoletilpasset argument for at sum av oddetall og oddetall er partall.

2. Gi et formelt og et grunnskoletilpasset argument for at partall multiplisert med partall gir partall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene

Tar du $6\cdot 6 = 36$, slutter verdien på $6$. Tar du $36\cdot 6 = 216$, slutter verdien på $6$. Forklar hvorfor, hvis en fortsetter å gange med $6$, at produktene man får alltid ender på $6$. Forklaringen skal være mulig for en elev å forstå.

##### Vurderingskriterier: Grunnleggende {#f1s3sg2}

Her må alle spørsmålene besvares. Besvarelsene må
inneholde, forklaringer, eksempler, definisjoner og
illustrasjoner der dette påpekes i oppgaveteksten.

##### Vurderingskriterier: Middels {#f13ssm2}

Alle oppgavene må besvares: Formelt: Algebra,
Grunnskoletilpasset: Kan gjøres ved hjelp av et talleksempel der
de drar ut strukturer/egenskaper som forklarer hvorfor det
gjelder generelt (generisk eksempel). Kan også gjøres
visuelt/ved hjelp av en figur; også da er det viktig at
illustrasjonen viser strukturer/egenskaper som får frem hvorfor
sammenhengen gjelder generelt.

##### Vurderingskriterier: Avansert {#f1ss3a2}

Her må man får frem struktur på en forståelig måte. For eksempel
dele opp tallene slik:
$6 \cdot 36 = 6 \cdot (30 + 6) = 6 \cdot 30 + 36$. Når vi
skiller ut de 6 enerne ser vi at vi i hvert tilfelle får
$6 \cdot$ *et antall tiere* $+ \ 36$. Med andre ord ender tallet
på 6.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Begrunn delelighetsregelen for tall som er delelig med 5. Du må gi både en formell og en grunnskoletilpasset begrunnelse.
Begrunn delelighetsregelen for tall som er delelig med 3. Du må gi både en formell og en grunnskoletilpasset begrunnelse.

##### Vurdereingskriterier: Middels

Formelt: Ta utgangspunkt i tre eller firesifra tall
($1000a + 100b + 10c + d$) og gjøre argumentene. Deretter *må* de
peke på hvorfor dette også fungerer for tall med flere siffer.
Grunnskoletilpasset: Ta utgangspunkt i et konkret eksempel og
forklare strukturen. Igjen må det komme tydelig fram hvordan
resultatet gjelder for et hvilket som helst antall sifre.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen):
geometrisk
algebraisk

##### Middels: Ved hjelp av sum av tillegg for andre polygontall

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 5, 12, 22, \ldots$.

#### Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 10$, $F_2 = 22$ og $F_3 = 42$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-06-04.png)

##### Vurderingskriterier: Grunnleggende {#f1d3sg4}

Studentene må besvare begge spørsmålene med riktig teknikk (se heftet).

##### Vurderingskriterier: Middels {#f1s3sm4}

Her må det være med en illustrasjon. I tillegg *må* den
eksplisitte formelen utledes ved å bruke sum av tillegg: Det vil
si jobbe seg fra $1+4+7+\ldots + 3n-2$ til $n^2+\frac{n(n-1)}{2}$ ved hjelp av
algebra og (mest sannsynlig) formelen for trekanttall.

##### Vurderingskriterier: Avansert {#f1s3sa4}

MERK: Her står det feil i oppgavetekst. Det skal være F_2 = 24

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel

ii. Her må de igjen bruke sum av tillegg sånn som på middels

### Finne rekursivt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for rektangeltall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk eksplisitt uttrykk for rektangeltall er $n\cdot(n+1)$.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for syvkanttallene $H_n$, der $H_1 =1$, $H_2 = 7$ og $H_3 = 18$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for syvkanttallene er $H_n = \frac{n(5n-3)}{2}$.

I begge oppgavene bes det om to teknikker. Se heftet for *differanse
mellom eksplisitte uttrykk* og *form på tillegg*.

##### Vurderingskriterier: Grunnleggende {#f1ss3G5}

Her må alle spørsmålene besvares med riktig
teknikk.

i. Her må de peke på formen på tillegget. Enten ved å peke på
figuren og vise hvordan den utvikler seg generelt. Eller ved
å peke på tilleggene i tallfølgen og forklare hvordan den
utvikler seg

ii. Her *må* de ta $R_n - R_{n-1}$ og gjøre algebra for å komme
fram til formen på tillegget.

##### Vurderingskriterier: Middels {#f13ssm5}

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i)

ii. Finne uttrykket ved hjelp av å regne $H_n-H_{n-1}$

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de tre første medaljetallene

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-07-13.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon

Ved å illustrere medaljetallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom medaljetall nummer $n$ og antall prikker i medaljetallet.

2. en rekursiv forklaring av sammenhengen mellom to påfølgende medaljetall.

#### Middels: Finne flere algebraiske uttrykk til samme figur

Ved å bryte medaljetallene ned på flere måter, utled to ulike, men likeverdige uttrykk for medaljetallene.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 1$, $F_2 = 9$, $F_3 = 20$, $F_4 = 34$ og $F_5 = 51$.

Lag en figur som følger mønsteret til $F_n$.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vurderingskriterier: Grunnleggende {#f1ss3g6}

Her må alle spørsmålene besvares, og de må
illustrere figurer

i.  Eksplisitt formel må finnes, og de må henvise til figuren

ii. Her er ordlyden blitt litt dum. Her må de henvise til
illustrasjonen for å få fram hvordan figuren utvikler seg
rekursivt.

##### Vurderingskriterier: Middels {#f1s3sm6}

De må finne minst to eksplisitte uttrykk og det må gis
en god nok forklaring på hvordan de har brutt ned figuren.

##### Vurderingskriterier: Avansert {#fs1d3a6}

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter

## 10.01.23

### Bruke begrepene faktor (divisor), felles faktor og største felles faktor, multiplum, felles multiplum og minste felles multiplum

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene 20.01

Forklar og gi eksempler på hva som menes med begrepene faktor og divisor. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med felles faktor og største felles faktor for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.
Forklar og gi eksempler på hva som menes med begrepet multiplum. Besvarelsen må inneholde både formell definisjon og grunnskoletilpasset forklaring.
Forklar og gi eksempler på hva som menes med felles multiplum og minste felles multiplum for to tall. Besvarelsen må inneholde både formelle definisjoner og grunnskoletilpassete forklaringer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene 20.01

La $a$ og $b$ være to naturlige tall med største felles faktor $10$ og minste felles multiplum $105$. Hvis $a = 30$ hva er da $b$? Begrunn.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene 20.01

Under ser du en påstand. Undersøk den og begrunn at den stemmer. Du må begrunne både uformelt og formelt.

Hvis et tall er faktor i to tall, så er det også faktor i differansen mellom de to tallene.

### Bruke begrepene naturlig tall, partall og oddetall, primtall og sammensatt tall

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene 20.01 {#123123}

Forklar og gi eksempler på hva et naturlig tall er.
Forklar og gi eksempler på hva partall og oddetall er. Besvarelsen må inneholde både algebraiske definisjoner, ordforklaringer og illustrasjoner.
Forklar og gi eksempler på hva primtall og sammensatt tall er.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene 20.01{#121233123}

1. Gi et formelt og grunnskoletilpasset argument for at sum av oddetall og partall er oddetall.

2. Gi et formelt og grunnskoletilpasset argument for at oddetall multiplisert med partall gir partall.

#### Avansert: Løse (også ukjente) problemer knyttet til begrepene 20.01 {#123123123}

Ved å multiplisere primtallene to primtall $a$ og $b$ og legge til $1$ får vi tallet $a\cdot b + 1$. Begrunn hvorfor dette tallet aldri er delelig på $a$ eller $b$.

### Begrunne delelighetsreglene for tall som er delelig med 2, 3, 4, 5, 6 og 9

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene 20.01 {#1232}

Begrunn delelighetsregelen for tall som er delelig med 4. Du må gi både en formell og en grunnskoletilpasset begrunnelse.
Begrunn delelighetsregelen for tall som er delelig med 9. Du må gi både en formell og en grunnskoletilpasset begrunnelse.

### Finne eksplisitt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av Gauss-trikset/doble summen for trekanttall, og ved hjelp av sum av tillegg for kvadrat- og rektangeltall 20.01

Utled det eksplisitte uttrykket for summen av de $n$ første naturlige tallene, det vil si trekanttall nummer $n$, ved hjelp av Gauss-trikset (doble summen):
geometrisk
algebraisk

#### Middels: Ved hjelp av sum av tillegg for andre polygontall 20.01

Illustrer sekskanttallene opp til $H_4$, og utled eksplisitt uttrykk for $H_n$ ved hjelp av strategien sum av tillegg.
Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall.
På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 12$, $F_2 = 22$ og $F_3 = 34$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-13-53-34.png)

### Finne rekursivt uttrykk for figurtall

#### Grunnleggende: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for trekant-, kvadrat- og rektangeltall 20.01

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for trekanttall $n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk.

#### Middels: Ved hjelp av form på tillegg, og differanse mellom eksplisitte uttrykk for andre polygontall og sammensatte figurtall 20.01

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene $H_n$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for sekskanttallene er $H_n = 2n^2-n$.

### Beskrive oppbygningen av figurtall (alle typer)

Under ser dere dere de tre første båttallene $B_1$, $B_2$ og $B_3$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-13-55-27.png)

#### Grunnleggende: Beskrive eksplisitt og rekursiv sammenheng verbalt og ved hjelp av illustrasjon 20.01

Ved å illustrere båttallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplsitt sammenheng mellom båttall nummer $n$ og antall prikker i båttallet.

2. en rekursiv forklaring av sammenhengen mellom to påfølgende båttall.

#### Middels: Finne flere algebraiske uttrykk til samme figur 20.01

Ved å bryte båttallene ned på flere måter, utled to ulike, men likeverdige uttrykk for båttallene.

#### Avansert: Lage figurer basert på algebraiske uttrykk og tallfølger 20.01

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 3$, $F_2 = 8$, $F_3 = 15$, $F_4 = 24$ og $F_5 = 35$.

Lag en figur som følger mønsteret til $F_n$. Begrunn sammenhengen mellom figuren og tallfølgen.

### Vurdere arbeid med figurtall med hensyn til læreplanens kjerneelementer og didaktikk knyttet til algebraisk tenkning

#### Middels: Forklar hvordan arbeid med figurtall innebærer algebraisk tenkning og arbeid med kjerneelementene

Gi en forklaring hvordan arbeidet med figurtall innebærer algebraisk tenkning og pek på hvilke kjerneelementer som er relevante i arbeid med figurtall.

#### Avansert: Lag en undervisningsaktivitet med utgangspunkt i kjerneelementer, kompetansemål og litteratur om algebraisk tenkning. Forklar hvordan undervisnignsaktiviteten samsvarer med kjerneelementer, kompetansemål og litteratur om algebraisk tenkning

Lag en figur som vokser i et tydelig mønster. Lag en kort undervisningsaktivitet med utgangspunkt i kjerneelementer, kompetansemål, litteratur om algebraisk tenkning og figuren du har laget. Gi en begrunnelse for valgene du har gjort.
