<!-- 
PDF:
Kjør i terminal fra markdown mappa pandoc .\quizzer\funksjoner\funk.md -f markdown -t pdf --pdf-engine=xelatex --variable=block-headings --toc -o .\quizzer\funksjoner\funk.pdf
HTML:
pandoc .\quizzer\funksjoner\funk.md -f markdown -t html --mathjax --template=template.html --toc -s -H styling.css -o .\quizzer\funksjoner\funk.html
-->
# Funksjoner

## Øveoppgaver

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med
    utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær
    funksjon.

2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med
    utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk
    funksjon.

3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart
    kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en
    omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. Avgjør og begrunn hva slags funksjon det er snakk om i hvert
    tilfelle. Begrunnelsen må vise til både en graf og et
    funksjonsuttrykk.

    a.  Sammenhengen mellom sidene i et rektangel med fast areal.

    b.  Sammenhengen radius og areal i en sirkel.

    c.  Sammenhengen mellom tid og avstand hjemmefra for en person som
        holder jevn fart.

##### Løsningsforslag

1. \
   a. Hvis vi kaller sidelengene i rektangelet for $x$ og $y$ så vet vi at med et fast areal $A$ så er $xy = A$. Dermed er $y = \frac{A}{x}$. Siden omvendtproporsjonale funksjoner alltid er på formen $y = \frac{a}{x}$ eller tilsvarende $xy = a$ så ser vi at dette gir en omvendt proporsjonal funksjon, men vi merker oss at negative verdier ikke gir mening i denne situasjonen. Lar vi arealet være $1$ i dette tilfellet vil grafen se slik ut

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-11-41-05.png)

   b. Vi vet at arealet av en sirkel er $\pi r^2$. Vi kan derfor skrive arealet som en funksjon av radiusen ved å si $A(r) = \pi r^2$. Vi ser at dette er en andregradsfunksjon og hvis vi skisserer den vil grafen se slik ut.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-11-42-05.png)

   c. Vi kan tenke oss at en person holder farten $a$ kilometer i timen og at personen går i en rett linje fra hjemmet sitt. Da vil personen i utgangspunktet, ved tid $0$ være $0$ km fra hjemmet sitt. Avstanden vil nå vokse lineært siden personen holder jevn fart og vi kan uttrykke sammenhengen som $f(x) = ax$ der $f$ er avstanden hjemmefra målt i kilometer og $x$ er antall timer som personen har gått i. Grafen vil, hvis $a$ er $6$ kilometer i timen se slik ut:

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-11-46-49.png)

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Lineære funksjoner.

    a.  Angi en situasjon som svarer til en lineær funksjon.

    b.  Skisser grafen, og sett opp funksjonsuttrykk.

    c.  Begrunn kort hvordan grafen og funksjonsuttrykket svarer til
        situasjonseksemplet.

2. Kvadratiske funksjoner.

    a.  Angi en situasjon som svarer til en kvadratisk funksjon.

    b.  Skisser grafen, og sett opp funksjonsuttrykk.

    c.  Begrunn kort hvordan grafen og funksjonsuttrykket svarer til
        situasjonseksemplet.

3. Omvendt proporsjonale funksjoner.

    a.  Angi en situasjon som svarer til en omvendt proporsjonal
        funksjon.

    b.  Skisser grafen, og sett opp funksjonsuttrykk.

    c.  Begrunn kort hvordan grafen og funksjonsuttrykket svarer til
        situasjonseksemplet.

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

1. Alfa s. 346--347.

    a.  4.9

    b.  4.12

    c.  4.13

    d.  4.14

    e.  4.16 (du behøver ikke argumentere på grunnleggende
        kompleksitetsnivå)

2. En lineær funksjon er en funksjon på formen $f(x) = ax + b.$ Forklar
    og vis i et koordinatsystem hva som skjer når

    a.  stigningstallet $a$ endres

    b.  konstantleddet $b$ endres

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

1. Alfa s. 346--347.

    a.  4.10 (Det sentrale her er å *forstå* hvordan man finner likninga
        så godt at man kort og presist kan *forklare* både hvordan og
        hvorfor. Prioriter derfor å gjøre *noen oppgaver grundig* og med
        forklaring, ikke *mange oppgaver kjapt*.)

    b.  4.11

    c.  4.15

    d.  4.16 (med argumentasjon)

    e.  4.17

    f.  **Bonus** (ut over læringsmålet): 4.18 og 4.19

##### Løsningsforslag

4.10. \

   a. Vi har punktene $(0, 0)$, altså origo og $(2,-3)$. Vi ser altså at hvis $x$ øker med to, fra $0$ til $2$, så synker $y$-verdien fra $0$ til $-3$, altså med $-3$. For å finne hvor mye den synker per $x$ deler vi stigningen på avstanden vi har forflyttet oss i $x$-retning. Det gir en stigning på $\frac{-3}{2}$. Siden vi kan se at linjen går gjennom origo vil det lineære uttrykket ha konstantledd lik $0$. Det gir dermed $y = \frac{-3}{2}x$. \
   b. Vi har punktene $(0, 3)$ og $(4, 3)$. Vi ser at linjen ikke stiger noe, altså at stigningen er lik $0$. Dermed må skjæringen med andreaksen være der $y = 3$. Det gir dermed likningen $y = 3$. \
   c. Vi har punktene $(-3, 1)$ og $(1,4)$. Endring i $x$-retning er her $1- 3 = 4$ og endring i $y$-retning er $4-1 = 3$. For å finne endring per $x$ ser vi på forholdet mellom stigningen og endring i $x$-retning. Det gir en stigning per $x$ lik $\frac{4}{3}$. En lineær funksjon med denne stigningen vil være $y = \frac{4}{3} x + b$. Det gjenstår å finne verdien for $b$, altså skjæring med andreaksen. Dette gjør vi nå ved å se at når $y = 4$ så er $x = 1$. Setter vi det inn i likningen $y = \frac{4}{3}x + b$ får vi $4 = \frac{4}{3}1 + b$. Vi kan nå løse for $b$ slik:
   $$
   \begin{aligned}
   4
   & =
   \frac{4}{3} + b
   \\
   4 - \frac{4}{3}  
   & =
   \frac{4}{3} - \frac{4}{3}  + b
   \\
   \frac{12-4}{3}  
   & =
   b
   \\
   \frac{8}{3}  
   & = b.
   \end{aligned}
   $$
   Likningen som går gjennom punktene er derfor $y = \frac{4}{3}x + \frac{8}{3}$.

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

1. Skisser grafen $y = x^{2}$ i et koordinatsystem. Skisser deretter i
    samme koordinatsystem:

    a.  $y = 2x^{2}$

    b.  $\frac{1}{2}x^{2}$

    c.  $2x^{2} - 3$

2. Gjengi med ord hvilken påvirkning endringer i $a$ (tallet foran
    $x^{2}$) og $c$ (konstantleddet) har på grafen til en
    andregradsfunksjon.

3. Skisser grafene $y = \frac{9}{x}$ og $y = - \frac{9}{x}$ i samme
    koordinatsystem.

4. I hvilke punkter skjærer $y = x$ og $y = \frac{a}{x}$?

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

1. En kvadratisk funksjon ser generelt slik ut:
    $f(x) = ax^{2} + bx + c$. Forklar kort (slik at det fremstår
    meningsfullt for noen som ikke kan det) og vis i et koordinatsystem
    hva som skjer med grafen når

    a.  parameteren $a$ endres

    b.  parameteren $c$ endres

2. En omvendt proporsjonal funksjon ser generelt slik ut:
    $f(x) = \frac{a}{x}$. Forklar kort (slik at det fremstår
    meningsfullt for noen som ikke kan det) og vis i et koordinatsystem
    hvordan grafen må se ut når

    a.  parameteren $a$ er større enn $0$

    b.  parameteren $a$ er mindre enn $0$

3. Forklar kort (slik at det fremstår meningsfullt for noen som ikke
    kan det) og vis i et koordinatsystem hvor grafene $y = x$ og
    $y = \frac{a}{x}$ skjærer hverandre.

##### Løsningsforslag

Se vurderingskriteriene fra ett av vurderingssettene.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

1. Gitt $4x - 7 = - 5x + 3$.

    a.  Løs likningen.

    b.  Forklar hva det vil si at tallet du fant er løsning av
        likningen.

    c.  Tolk VS og HS som funksjonsuttrykk, og skisser grafene.

    d.  Forklar sammenhengen mellom b. og c.

2. Gitt $3(x - 7) = - \frac{1}{2}x + 3$.

    a.  Løs likningen.

    b.  Forklar hva det vil si at tallet du fant er løsning av
        likningen.

    c.  Tolk VS og HS som funksjonsuttrykk, og skisser grafene.

    d.  Forklar sammenhengen mellom b. og c.

3. Forklar ved hjelp av et eget eksempel, hva som menes med løsningen
    av en lineær likning. Forklar både algebraisk og grafisk, og pek på
    sammenhengen mellom dem.

##### Løsnningsforslag

1. \
   a. Vi kan løse likningen slik
   $$
   \begin{aligned}
   4x-7
   & =
   -5x + 3
   \\
   4x - 7 + 7 + 5x
   & =
   -5x + 3 + 7 + 5x
   \\
   9 x
   & =
   10
   \\
   \frac{9x}{9} = x
    & =
   \frac{10}{9}.
   \end{aligned}
   $$
   b. Tallet $\frac{10}{9}$ vi fant sier oss at når  $x = \frac{10}{9}$ så vil venstre side være lik høyre side i likningen når vi bytter ut $x$ med tallet.
   c.  Tolker vi VS og HS som funksjoner får vi funksjonene $f(x) = 4x-7$ og $g(x) = -5x + 3$. En skisse vil se slik ut

   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-12-06-48.png)

   d. Vi ser at grafene krysser i punktet $\frac{10}{9}$. At de krysser betyr at for den samme $x$-verdi så er funksjonenverdien også lik. Siden vi tolket HS og VS som funksjoner, så betyr krysningspunktet at for $x$-verdien $\frac{10}{9}$ så vil funksjonsverdiene være like. Dette er nøyaktig det som vi sa i b.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Du løper sammen med en av de fjernstyrte bilene dine langs en rett
    strekning. Bilen holder seks meter i sekundet, mens du klarer $3,5$.
    Fjernkontrollens rekkevidde er $200$ meter.

    a.  Hvor langt kommer du før bilen er utenfor rekkevidde?

    b.  Illustrer turen grafisk.

    c.  Hvis du starter med $150$ meters forsprang, når og hvor tar
        bilen deg igjen?

    d.  Lag et uttrykk som viser avstanden mellom deg og bilen som
        funksjon av tiden.

    e.  Du er ute på samme strekning med den andre fjernstyrte bilen
        din. Du starter med $150$ meters forsprang. Etter å ha løpt
        $140$ meter, tar bilen deg igjen. Hva er bilens fart?

2. La $f(x) = - 15x + \frac{1}{2}$.

    a.  Hvor skjærer $f$ andreaksen, og hvorfor? (forklar)

    b.  Hvor skjærer $f$ førsteaksen, og hvorfor? (forklar)

3. Lag tekstoppgaver/finn passende kontekster til likningene. Tolk og
    vis i koordinatsystem.

    a.  $170x + 900 = 230x + 200$

    b.  $3 - \frac{1}{2}t = 1$

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

1. La $f(x) = \frac{12}{x}$ og $g(x) = 3x - \frac{1}{2}$.

    a.  Skisser grafene.

    b.  Finn eventuelle skjæringspunkt ved regning.

2. La $f(x) = - 6x + b$ og $g(x) = x^{2} - 4x$.

    a.  Bestem $b$ slik at $f$ og $g$ skjærer hverandre i $x = 1$ og
        $x = - 3$.

    b.  Skisser grafene.

3. En fjernstyrt bli som kjører 12 m/s bruker 3/2 sekunder på å nå
    topphastigheten. Frem til det er strekningen den tilbakelegger gitt
    ved $s(t) = 4t^{2}$, der $t$ er tiden målt i sekunder. Fra og med
    3/2 sek., holder bilen 12 m/s.

    a.  Skisser situasjonen i et koordinatsystem.

    b.  Finn funksjonsuttrykket som beskriver tilbakelagt strekning fra
        og med 3/2 sek.

##### Løsningsforslag

2. \
   a. Vi vil at $-6x + b = x^2 -4x$ når $x = 1$ og når $x = -3$. Setter vi for eksempel inn $x=1$ får vi
   $$
   -6 + b = 1-4 = -3.
   $$
   Ved å legge til $6$ på begge sider ser vi at $b = 3$. Vi kan nå også teste å se at dette stemmer for $x= -3$ ved å sette inn:
   $$
   \begin{aligned}
    -6\cdot -3 + 3
    & = (-3)^2 -4\cdot -3
    \\
    18 + 3 = 21
    & =
    9 + 12 = 21.
   \end{aligned}
   $$
   b. Skisserer vi grafene ser det slik ut

   ![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-12-15-21.png)

### Bruke begrepene funksjon, variabel, uavhengig variabel (innverdi), avhengig variabel (utverdi), funksjonsverdi, definisjonsmengde og verdimengde

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene

1. Ta utgangspunkt i en funksjonssammenheng (velg selv), og bruk den
    til å forklare begrepene.

2. Sammenhengen mellom sidelengden og arealet av et kvadrat er en
    funksjonssammenheng. Bruk eksemplet til å forklare begrepene.

3. Sammenhengen mellom grader målt i Fahrenheit og grader målt i
    Celsius er en funksjonssammenheng. Bruk eksemplet til å forklare
    begrepene.

#### Middels: Avgjøre og begrunne (ved hjelp av begrepene) om en gitt sammenheng er en funksjonssammenheng

1. Sammenhengen mellom sidelengden og arealet av et kvadrat er en
    funksjonssammenheng.

    a.  Bruk eksemplet til å forklare begrepene.

    b.  Arealfunksjonen er her uttrykt som en situasjonsbeskrivelse.
        Uttrykk den også som tabell, funksjonsuttrykk og graf.

2. Sammenhengen mellom grader målt i Fahrenheit og grader målt i
    Celsius er en funksjonssammenheng.

    a.  Bruk eksemplet til å forklare begrepene.

    b.  Sammenhengen mellom temperaturskalaene er her uttrykt som en
        situasjonsbeskrivelse. Uttrykk den også som tabell,
        funksjonsuttrykk og graf.

> (Her må du enten google eller, hvis du er tøff (og det er du jo),
> bruke dette: Sammenhengen er lineær, og $(32,\ 0)$ og $(41,\ 5)$ er to
> punkter på grafen, der førstekoordinat er temperaturen i Fahrenheit,
> andrekoordinat tilhørende Celsius-verdi.)

3. Under ser du noen par av variabler. Avgjør og begrunn i hvert
    tilfelle om den ene er funksjon av den andre. Begrunnelsen må vise
    til en definisjon av funksjon og en algebraisk eller grafisk
    fremstilling av situasjonen.

    a.  Temperaturen der du bor og tiden gjennom ett døgn.

    b.  Omkretsen av et rektangel og arealet av rektanglet.

    c.  Omkretsen av en sirkel og arealet av sirkelen.

    d.  En balls høyde over bakken og tiden målt fra da du slapp den.

4. Oppgavene 4.1--4.5, s. 335 i Alfa er også ok oppgaver av typen «er y
    funksjon av x i *dette* tilfellet?»

##### Løsningsforslag

2. \
   a. Vi vet (enten ved å Google, eller ved tidligere kunnskap) at det er en lineær sammenheng mellom Fahrenheit og Celcius. Ved å løse for punktene $(32,0)$ og $(41, 5)$ (se tidligere læringsmål for å gjøre dette) ser vi at sammenhengen er $F(C) = 32 + \frac{9}{5}C$, der $F$ er Fahrenheit og $C$ er Celcius. Her vil $C$ være den uavhengige variabelen (innverdien) og $F$ vil være funksjonsverdien (utverdi). Vi vet også at det finnes et absolutt minimum $0$ Kelvin, som tilsvarer $-273.15$ Celcius. Det finnes ingen øvre grense på varme og definisjonsområdet for denne sammenhengen blir derfor $[-273.15, \infty]$. Setter vi inn nedre grense ser vi at funksjonsverdiene vi kan få går fra $F(-273.15) = -459.67$ til uendelig. Det gir en verdimengde lik $[-459.67, \infty]$.
   b. Funksjonsuttrykket har vi allerede fra a. Vi kan lage en enkel tabell slik:

+-------+--------+
| C     |   F    |
+:=====:+:======:+
| -10   |   14   |
+-------+--------+
| -5    |   23   |
+-------+--------+
| 0     |   32   |
+-------+--------+
| 5     |   41   |
+-------+--------+
| 10    |   50   |
+-------+--------+

   Skisserer vi grafen vil den se sirka slik ut:

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-12-33-04.png)

### Gjøre om mellom ulike representasjonsformer for funksjonssammenhenger

#### Middels: Gjøre om mellom de fire representasjonene av funksjoner (Janviers tabell, Alfa 4.1), og vurdere elevers arbeid med overganger mellom representasjonene

1. Alfa s. 335--336: oppgavene 4.6--4.8

2. Overgang mellom graf og situasjon.

    a.  Gi en passende situasjonsbeskrivelse til grafen under.

    b.  Hvordan vil grafen til samme situasjon se ut dersom andreaksen
        heller måler tilbakelagt avstand?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/Picture2.jpg)

3. Tabellen viser en forenklet trinnskattemodell. Dersom man tjener
    $60\ 000$ eller mer, betaler man skatt på hele beløpet, ikke bare
    den delen som overstiger frikortgrensa. Skattesatsene slår inn ved
    $60\ 000$, $300\ 000$ og så videre. Tegn en graf som viser
    sammenhengen mellom brutto- og nettoinntekt.

+-------------------------------------------+--------------------------+
| **Bruttolønn**                            | **Skattetrekk**          |
+===========================================+==========================+
| $$000\ 000 - 60\ 0000$$                   | $$0\ \%$$                |
+-------------------------------------------+--------------------------+
| $$060\ 000 - 300\ 000$$                   | $$20\ \%$$               |
+-------------------------------------------+--------------------------+
| $$300\ 000 - 450\ 000$$                   | $$24\ \%$$               |
+-------------------------------------------+--------------------------+
| $$450\ 000 - 600\ 000$$                   | $$28\ \%$$               |
+-------------------------------------------+--------------------------+
| $$600\ 000 - 800\ 000$$                   | $$>30\ \%$$              |
+-------------------------------------------+--------------------------+

4. Se figuren under. Skisser en graf over sammenhengen mellom krukkas
    høyde og volum, der førsteaksen angir høyden og andreaksen volumet.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/Picture1.jpg)

1. Klassen din får oppgaven under. Mange av elevene velger den øverste
    grafen med begrunnelser av typen «her ser vi tydelig hvordan bakken
    blir brattere».

    a.  Hva er misforståelsen disse elevene har?

    b.  Forklar hvorfor den nederste grafen er den som passer til
        situasjonen.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/funk/image3.png)

##### Løsningsforslag

4. Fyllingen kan deles inn i to *faser*. Den første er fylling før vannet har nådd krukkas tykkeste punkt. Siden krukken øker i diameter vil høyden øke saktere og saktere fram til den kommer til krukkast tykkeste. Da vil høyden begynne å øke fortere og fortere og vil nå en høyere hastighet enn da vi begynte å fylle (siden tuppen er tynnere enn bunnen). Hvis vi prøver å få alt dette med i en skisse kan det se noe slik ut:

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-27-12-47-38.png)

## 31.03.23


### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.
2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.
3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. Et kvadrat i grønt ligger over et rektangel i lilla og  firkantene vokser i takt, slik som vist under. Rektangelets grunnlinje er alltid tre ganger så lang som sidelengen i kvadratet, og høyden til rektangelet er to ganger så langt som kvadratets sidelengde. Hva er sammenhengen mellom sidelengden i kvadratet og det synlige lilla området?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-31-09-23-39.gif)

2. "En skole skal holde en fest og har fått en pris for lokalet. Ikke alle vil delta på festen og det er bestemt at alle som deltar skal betale like mye. Siden prisen per elev, $x$, avtar når antallet gjester, $y$, øker, er sammenhengen mellom $x$ og $y$ omvendt proporsjonal." Avgjør og begrunn om påstanden stemmer.

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Tabellen under viser en funksjonssammenheng.

a. Avgjør om den er lineær, kvadratisk eller omvendt proporsjonal.

b. Lag en passende situasjon som kan høre til funksjonssammenhengen.

c. Finn funksjonsuttrykk, og skisser grafen.

| x   | -2  | -1  | 1  |  2  |
|-----|-----|-----|----|-----|
| y   | -4  | -8  | 8  | 4   |

1. Under ser du grafen til en funksjon.

a. Avgjør hva slags funksjon det er snakk om.

b. Finn funksjonsuttrykket.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-31-09-26-46.png)

#### Vurderingskriterier: Grunnleggende {#170211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.  

#### Vurderingskriterier: Middels {#170212}

1. Studenten *må* lage en sammenheng mellom arealet mellom området og sidelengden. Her bør de bruke at hvis sidelengden er $s$ så er lengdene i rektangelet $2s$ og $3s$. Dermed er arealet av det synlige lilla området $2s\cdot 3s - s^2 = 5s^2$. Studenten kan dermed peke på at sammenhengen må være $A(s) = 5s^2$, der $A$ er arealet av det synlige lilla området og $s$ er sidelengden i det grønne kvadratet.
2. Studenten må få fram at siden prisen, som vi kan kalle $P$ alltid skal deles likt på antall elever som vi kaller $x$, så må elevene betale $\frac{P}{x}$. Det betyr at summen elevene må betale er $f(x) = \frac{P}{x}$, altså omvendtproporsjonale.

#### Vurderingskriterier: Avansert {#170213}

Studentene *må* peke på hvilken funksjon det er. I første eksempel bør studenten få fram at det må være en omvendt proporsjonal funksjon og begrunne dette. Det gir funksjonen $f(x)  = \frac{8}{x}$. I det andre eksempelet ser vi at $x = 2$ er toppunkt og at funksjonen er en parabel. Dermed er det en andregradsfunksjon. Deretter må finne funksjonsuttrykket (for eksempel ved regning). Dette kan de gjøre ved å først innse at koeffisienten $a$ i $ax^2+bx+c$ må være $-1$. Deretter kan de se at når $x = 2$ så er $f(2) = 6$ og $x=1$ så er $f(1) = 5$. Ved hjelp av dette kan de sette opp et likningssett og løse det.

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Grafen til en lineær funksjon går gjennom punktene $(-3, 0)$ og $(6, 3)$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

#### Vurderingskriterier: Grunnleggende {#170221}

Peke på hva parameterne gjør for førstegradsfunksjoner
Middels:
Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En omvendt proporsjonal funksjon kan skrives på formen $\frac{a}{x}$. Vis i et koordinatsystem hvordan grafen ser ut dersom $a>0$ og dersom $a<0$.

Skisser grafen til $f$ og $g$ der $f(x)=x(x-5)$ og  $g(x)=x(x-5) + 2$

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#170231}

1. Peke på hva parameterne gjør for andregradsfunksjoner
2. Skissere de to omvendt proporsjonale grafene.  

#### Vurderingskriterier: Middels {#170232}

1. Omvendt proporsjonale:  
Grafen må skisseres for $a>0$ og $a<0$. Det må komme fram hvorfor formen på grafen er som den er. For eksempel $a>0$ kan en gi et konkret eksempel på en om omvendt prop. funk. og framheve sammenhengen (skaleres $x$ opp med noe skaleres $y$ ned med det samme, derav navnet omvendt prop) $\rightarrow$  større og større $x$ gir $y$ som kryper mot $0$, mindre og mindre $x$ gir større og større $y$. Det bør komme fram noen symmetrier med grafen. Når $a<0$ kan en bare peke på at $a< 0$ gir bare samme graf flippet over $x$-aksen.  
Kvadratiske funksjoner:  
Her må det kort komme fram at a avgjør hvor bratt funksjonen stiger (hvis $a>0$) eller synker ($a<0$), og at $c$ flytter grafen oppover eller nedover og tilsier hvor funksjonen skjærer andreaksen.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

Gitt likningen $6(4x-2) = 12$.

Løs likningen
Tolk venstre side og høyre side som funksjonsuttrykk, og skisser grafene i samme koordinatsystem.
Forklar algebraisk og grafisk hva det vil si at tallet du fant i 1. er en løsning på likningen.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Gi en situasjon som passer til funksjonen $f(x)=50 - 5x$. Hva svarer likninga $50 - 5x=10$ til i situasjonsbeskrivelsen din? Tolk og løs likningen grafisk i et koordinatsystem.

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

La $f(x)=2x^2+12x-x$  og  $g(x)=-6x-6$.

Bestem eventuelle skjæringspunkt (begge koordinater) mellom grafene til $f$ og $g$ ved regning.

Skisser grafene i et koordinatsystem.

#### Vurderingskriterier: Grunnleggende {#170241}

Alle oppgaver må besvares.  

1. Likningen må løses.
2. Her må de tolke og skissere begge grafene i samme koordinatsystem.
3. Gi en forklaring som viser sammenhengen mellom at løsning gir likhet av venstre og høyre side i likningen og at det tilsvarer skjæringspunktet mellom grafene.  

#### Vurderingskriterier: Middels {#170242}

De må lage en situasjon som gir likningen. Deretter må de illustrere likningen grafisk og vise løsningen i koordinatsystemet.

#### Vurderingskriterier: Avansert {#170243}

Alle oppgavene må besvares

1. Studenten må regne ut skjæringspunktene.
2. Studenten må skissere grafene i et koordinatsystem.

### Bruke begrepene funksjon, variabel, uavhengig variabel (innverdi), avhengig variabel (utverdi), funksjonsverdi, definisjonsmengde og verdimengde

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene

Sammenhengen mellom sidelengden og arealet av et kvadrat er en funksjonssammenheng. Bruk eksemplet til å forklare begrepene funksjon, innverdi og funksjonsverdi.

#### Middels: Avgjøre og begrunne (ved hjelp av begrepene) om en gitt sammenheng er en funksjonssammenheng

Til hvert av punktene A) og B), er to variabler beskrevet. Avgjør i hvert tilfelle om én av variablene er funksjon av den andre, begge variabler er funksjon av hverandre, eller ingen av dem er funksjon av den andre. Besvarelsen må inneholde ordene innverdi og funksjonsverdi, definisjons- og verdimengde.

A) En persons personnummer og personens høyde.

B) En persons navn og personens utdanning.

#### Vurderingskriterier: Grunnleggende {#170251}

Her må de peke på at arealet av en kvadrat med sidelengde $r$ er $r^2$ (altså at $A(r) = r^2$). Arealet er derfor en funksjon av $r$ (innverdi) fordi hver sidelengde $r$ gir et entydig areal (som her er funksjonsverdien).

#### Vurderingskriterier: Middels {#170252}

Besvarelsene *må* inneholde ordene innverdi, funksjonsverdi, definisjons- og verdimengde.
A. Studenten må begrunne sammenhengen personens personnummer og høyde. Siden personnummer er unikt for personer og alle personer kun har en høyde, vil det for hvert personnummer (innverdi) finnes nøyaktig én høyde (funksjonsverdi) som hører til det personnummeret. Dette betyr at høyden er en funksjon av personnummeret. Studenten må også gi en meningsfull forklaring på hva definisjons- og verdimengden er til denne funksjonen.
B. Studenten bør få fram at det kan finnes flere personer med samme navn. Dermed kan ikke en personens navn være nok til å avgjøre utdanning. Tilsvarende kan en utdanning ikke være nok til å avgjøre hvem personers navn.

### Gjøre om mellom ulike representasjonsformer for funksjonssammenhenger

#### Middels: Gjøre om mellom de fire representasjonene av funksjoner (Janviers tabell, Alfa 4.1), og vurdere elevers arbeid med overganger mellom representasjonene

Under ser du en skisse av Henriks reisevei til jobb dersom han kjører bil. Fartsgrensene gjelder hver av de rette strekkene.

1. Lag en passende tabell som viser avstand hjemmefra som funksjon av tid på Henriks kjøretur til jobb.
2. Skisser en graf til samme situasjon.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-31-09-44-03.png)

#### Vurderingskriterier: Middels {#170262}

1. Studentene må lage en passende tabell som viser avstand hjemmefra som funksjon av tid. Funksjonen bør (men må ikke) bruke overgangene mellom fartsgrensene, slik at skisseringen i neste oppgave tydelig henger sammen med tabellen.
2. Studentene må skissere en graf som får fram sammenhengen på en riktig måte, den må også samsvare med tabellen som er beskrevet i 1.. \
Siden strekningen inneholder ulike soner med ulike hastigheter *må* dette være gjenspeilet i grafen.

## 17.02.23

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.

Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.

Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. Den store sirkelen har radius $10$, den lille har radius $r$. Hva er sammenhengen mellom den lille radien og arealet mellom den store og den lille sirkelen?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-27-49.png)

2. "I et selskap deles det ut lodd. Fra de $1000$ loddene, deles tre lodd ut til hver gjest. Siden antallet gjenværende lodd, $y$, avtar når antallet gjester, $x$, øker, er sammenhengen mellom $x$ og $y$ omvendt proporsjonal." Avgjør og begrunn om påstanden stemmer.

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Tabellen under viser en funksjonssammenheng.

a. Avgjør om den er lineær, kvadratisk eller omvendt proporsjonal.

b. Lag en passende situasjon som kan høre til funksjonssammenhengen.

c. Finn funksjonsuttrykk, og skisser grafen.

| x  | 1    | 3    | 4   | -2   |
|:---|:-----|:-----|:----|:-----|
| y  | 150  | 100  | 75  | 225  |

2. Under ser du grafen til en funksjon.

a. Avgjør hva slags funksjon det er snakk om.

b. Finn funksjonsuttrykket.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-34-15.png)

#### Vurderingskriterier: Grunnleggende {#170211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.  

#### Vurderingskriterier: Middels {#170212}

1. Studenten *må* lage en sammenheng mellom arealet mellom stor og liten sirkel og radiusen. Det naturlige er å sette opp differansen mellom stor og liten sirkel $\pi\cdot 10^2 - \pi\cdot r^2 = \pi(10^2-r^2)$.
2. Studenten må få fram at dette ikke gir en omvendt proporsjonal sammenhenge. Dette kan de for eksempel gjøre ved å forklare at $y$ må være $1000-3x$, der $x$ er anntall gjester og peke på at dette ikke gir sammenhengen $y\cdot x = a$ der $a$ er en konstant.  

#### Vurderingskriterier: Avansert {#170213}

Studentene *må* peke på hvilken funksjon det er. I første eksempel kan de se at økningen er lineær, med $25$ per $x$.  Det gir funksjonen $f(x)  = 175 - 25x$. I det andre eksempelet ser vi at $x = 2$ er toppunkt og at funksjonen er en parabel. Dermed er det en andregradsfunksjon. Deretter må finne funksjonsuttrykket (for eksempel ved regning).

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Grafen til en lineær funksjon går gjennom punktene $(-3, 0)$ og $(6, 3)$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

#### Vurderingskriterier: Grunnleggende {#170221}

Peke på hva parameterne gjør for førstegradsfunksjoner
Middels:
Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En omvendt proporsjonal funksjon kan skrives på formen $\frac{a}{x}$. Vis i et koordinatsystem hvordan grafen ser ut dersom $a>0$ og dersom $a<0$.

Skisser grafen til $f$ og $g$ der $f(x)=x(x-5)$ og  $g(x)=x(x-5) + 2$

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#170231}

1. Peke på hva parameterne gjør for andregradsfunksjoner
2. Skissere de to omvendt proporsjonale grafene.  

#### Vurderingskriterier: Middels {#170232}

1. Omvendt proporsjonale:  
Grafen må skisseres for $a>0$ og $a<0$. Det må komme fram hvorfor formen på grafen er som den er. For eksempel $a>0$ kan en gi et konkret eksempel på en om omvendt prop. funk. og framheve sammenhengen (skaleres $x$ opp med noe skaleres $y$ ned med det samme, derav navnet omvendt prop) $\rightarrow$  større og større $x$ gir $y$ som kryper mot $0$, mindre og mindre $x$ gir større og større $y$. Det bør komme fram noen symmetrier med grafen. Når $a<0$ kan en bare peke på at $a< 0$ gir bare samme graf flippet over $x$-aksen.  
Kvadratiske funksjoner:  
Her må det kort komme fram at a avgjør hvor bratt funksjonen stiger (hvis $a>0$) eller synker ($a<0$), og at $c$ flytter grafen oppover eller nedover og tilsier hvor funksjonen skjærer andreaksen.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

Gitt likningen $2(3x-1) = 3x+1$.

Løs likningen
Tolk venstre side og høyre side som funksjonsuttrykk, og skisser grafene i samme koordinatsystem.
Forklar algebraisk og grafisk hva det vil si at tallet du fant i 1. er en løsning på likningen.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Gi en situasjon som passer til funksjonen $f(x)=5-\frac{1}{2}x$. Hva svarer likninga $5-\frac{1}{2}x=2$ til i situasjonsbeskrivelsen din? Tolk og løs likningen grafisk i et koordinatsystem.

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

La $f(x)=\frac{1}{2}x^2+6x-1$  og  $g(x)=\frac{3}{2}x+4$.

Bestem eventuelle skjæringspunkt (begge koordinater) mellom grafene til $f$ og $g$ ved regning.

Skisser grafene i et koordinatsystem.

#### Vurderingskriterier: Grunnleggende {#170241}

Alle oppgaver må besvares.  

1. Likningen må løses.
2. Her må de tolke og skissere begge grafene i samme koordinatsystem.
3. Gi en forklaring som viser sammenhengen mellom at løsning gir likhet av venstre og høyre side i likningen og at det tilsvarer skjæringspunktet mellom grafene.  

#### Vurderingskriterier: Middels {#170242}

De må lage en situasjon som gir likningen. Deretter må de illustrere likningen grafisk og vise løsningen i koordinatsystemet.

#### Vurderingskriterier: Avansert {#170243}

Alle oppgavene må besvares

1. Studenten må regne ut skjæringspunktene.
2. Studenten må skissere grafene i et koordinatsystem.

### Bruke begrepene funksjon, variabel, uavhengig variabel (innverdi), avhengig variabel (utverdi), funksjonsverdi, definisjonsmengde og verdimengde

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene

Sammenhengen mellom sidelengden og arealet av et kvadrat er en funksjonssammenheng. Bruk eksemplet til å forklare begrepene funksjon, innverdi og funksjonsverdi.

#### Middels: Avgjøre og begrunne (ved hjelp av begrepene) om en gitt sammenheng er en funksjonssammenheng

Til hvert av punktene A) og B), er to variabler beskrevet. Avgjør i hvert tilfelle om én av variablene er funksjon av den andre, begge variabler er funksjon av hverandre, eller ingen av dem er funksjon av den andre. Besvarelsen må inneholde ordene innverdi og funksjonsverdi, definisjons- og verdimengde.

A) En pakkes vekt og prisen man betaler for å sende den.

B) Temperatur målt utenfor stuevinduet og tidspunktene for målingene.

#### Vurderingskriterier: Grunnleggende {#170251}

Her må de peke på at arealet av en kvadrat med sidelengde $r$ er $r^2$ (altså at $A(r) = r^2$). Arealet er derfor en funksjon av $r$ (innverdi) fordi hver sidelengde $r$ gir et entydig areal (som her er funksjonsverdien).

#### Vurderingskriterier: Middels {#170252}

Besvarelsene *må* inneholde ordene innverdi, funksjonsverdi, definisjons- og verdimengde.
A. Studenten må begrunne sammenhengen vekt og pris. Som oftes er prisen avhengig av både størrelse og vekt. På denne måten kan en argumentere for at prisen ikke er entydig bestemt av vekten alene. Derfor er pris ikke en funksjon av vekt. Tilsvarende kan en ikke *hente tilbake* vekten ved å se på prisen, da disse ofte settes i intervaller. På den andre side kan en tolke oppgaven som at pakken er i en fiksert størrelse. Dermed vil vekten entydig bestemme prisen. I dette tilfellet vil vekten være innverdi og prisen være funksjonsverdien. Siden vekten kan være alle positive tall må er det naturlig å tenke at definisjonsmengden er alle positive verdier. Verdimengden i dette tilfellet blir de prisene en er nødt til å betale, som i dette tilfelle nok blir en diskrete verdier.  
B. Studenten må begrunne sammenhengen tid og temperatur.Det vil for hvert tidspunkt være en målt temperatur utenfor stuevinduet. Dermed kan temperaturen utenfor stuevinduet ses på som en funksjon av tiden. Da det ved flere tidspunkt kan være samme temperatur utenfor, kan en ikke finne tilbake til et tidspunkt ved å se på temperaturen. Derfor vil ikke tiden være en funksjon av temperaturen.

### Gjøre om mellom ulike representasjonsformer for funksjonssammenhenger

#### Middels: Gjøre om mellom de fire representasjonene av funksjoner (Janviers tabell, Alfa 4.1), og vurdere elevers arbeid med overganger mellom representasjonene

André "sykler" (el-sykkel) og Henrik sykler (skikkelig sykkel) til jobb. De har lik reisevei ($8$ km) og bruker like lang tid ($25$ min.). André, med "sykkelen" sin, holder jevn fart hele veien. Henriks fart varierer avhengig om det er strake veier eller bakker. På Henriks reisestrekning er det to oppoverbakker - den første lang og slak, den andre en del kortere og bratt. Det er også én lang nedoverbakke. Det resterende av strekningen er flat. Den første oppoverbakken er ved $2,5$ km, den andre ved $4$ km. Nedoverbakken er ved $7,2$ km.

Skisser to grafer i samme koordinatsystem. Den ene skal være en fremstilling av Andrés reise til jobb, den andre Henriks reise til jobb. La det gå klart frem hvilke variabler som inngår i den grafiske fremstillingen din.

#### Vurderingskriterier: Middels {#170262}

Studentene må skissere en graf som får fram sammenhengen på en riktig måte, som også inneholder all informasjonen som er gitt. André sin graf bør være en lineær graf mens Henrik sin bør variere i tråd med beskrivelsen.

## Funksjoner 13.02.23

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.
2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.
3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. I hagen ligger det et barnebasseng som rommer $1$ m$^3$. Bassenget skal fylles med vann. Du har en vannslage som fyller $0,05$ m$^3$ vann i bassenget per minutt. I tillegg fyller du bøtter med varmt vann innefra og klarer å fylle $0,01$ m$^3$ varmt vann per minutt.  Hva er sammenhengen mellom tiden og mengden vann i bassenget?

2. I koordinatsystemet under ser du to grafer. Begrunn hvilken av dem som er grafen til en omvendt proporsjonal funksjon. Begrunnelsen må vise til et funksjonsuttrykk. (Å si at grafen ser ut sånn og sånn, er altså ikke en begrunnelse ;))

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-48-58.png)

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Tabellen under viser en funksjonssammenheng.

a. Avgjør om den er lineær, kvadratisk eller omvendt proporsjonal.

b. Lag en passende situasjon som kan høre til funksjonssammenhengen.

c. Finn funksjonsuttrykk, og skisser grafen.

| x  | 2    | 3    | 4   | 6   | 12  |
|--- |----- |----- |---- |----- | ----- |
| y  | 150  | 100  | 75  | 50  | 25 |

1. Under ser du grafen til en funksjon.

a. Avgjør hva slags funksjon det er snakk om.

b. Finn funksjonsuttrykket.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-49-07.png)

#### Vurderingskriterier: Grunnleggende {#130211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.  

#### Vurderingskriterier: Middels {#130212}

1. Studenten *må* lage en sammenheng mellom mengde vann og tid. Det naturlige er at å koble mengde vann som fylles per minutt, som er $0,\!05 + 0,\!01 = 0,\!06$. Siden vi skal fylle et basseng kan vi anta et det er tomt, som gir $f(x) =0,\!06x$, der $x$ er antall minutter og $f$ er antall $m^3$ som vannet fyller i bassenget.  
2. Studenten må peke på egenskaper ved omvendtproporsjonale funksjoner for å begrunne. For eksempel kan en peke på at den grønne funksjonen oppfyller dobling av $x$ gir halvering av $y$. Altså at $x= 4$ gir $y=16$ og $x=8$ gir $y = 8$. De bør også pekes på at den blå grafen ikke oppfyller denne egenskapen for eksempel ved å peke på at de krysser i $x= 8$, men ikke i $x= 4$.  

#### Vurderingskriterier: Avansert {#130213}

Studentene *må* peke på hvilken funksjon det er. I første eksempel kan de se at dobling av $x$ gir halvering av $y$. Det gir funksjonen $f(x)  = \frac{300}{x}$. I det andre eksempelet ser vi at $x = 2$ er bunnpunkt og at funksjonen er en parabel. Dermed er det en andregradsfunksjon. Deretter må finne funksjonsuttrykket (for eksempel ved regning).

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Under ser du en lineær funksjon som går gjennom punktene $A$ og $B$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-50-16.png)

#### Vurderingskriterier: Grunnleggende {#130221}

Peke på hva parameterne gjør for førstegradsfunksjoner

#### Vurderingskriterier: Middels {#130222}

Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En andregradsfunksjon kan skrives på formen $ax^2 + b x + c$. Gjengi med ord hvilken påvirkning endringer i $a$ (tallet foran $x^2$) og $c$ (konstantleddet) har på grafen til en andregradsfunksjon.

Skisser grafene $y = \frac{24}{x}$ og $y = \frac{-24}{x}$ i samme koordinatsystem.

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#130231}

1. Peke på hva parameterne gjør for andregradsfunksjoner
2. Skissere de to omvendt proporsjonale grafene.  

#### Vurderingskriterier: Middels {#130232}

1. Omvendt proporsjonale:  
Grafen må skisseres for $a>0$ og $a<0$. Det må komme fram hvorfor formen på grafen er som den er. For eksempel $a>0$ kan en gi et konkret eksempel på en om omvendt prop. funk. og framheve sammenhengen (skaleres $x$ opp med noe skaleres $y$ ned med det samme, derav navnet omvendt prop) $\rightarrow$  større og større $x$ gir $y$ som kryper mot $0$, mindre og mindre $x$ gir større og større $y$. Det bør komme fram noen symmetrier med grafen. Når $a<0$ kan en bare peke på at $a< 0$ gir bare samme graf flippet over $x$-aksen.  
Kvadratiske funksjoner:  
Her må det kort komme fram at a avgjør hvor bratt funksjonen stiger (hvis $a>0$) eller synker ($a<0$), og at $c$ flytter grafen oppover eller nedover og tilsier hvor funksjonen skjærer andreaksen.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

Gitt likningen $12-5x = \frac{1}{3}(x+4)$.

Løs likningen
Tolk venstre side og høyre side som funksjonsuttrykk, og skisser grafene i samme koordinatsystem.
Forklar algebraisk og grafisk hva det vil si at tallet du fant i 1. er en løsning på likningen.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Gi en situasjon som passer til funksjonen $f(x)=5+3x$. Hva svarer likninga $5+3x=0$ til i situasjonsbeskrivelsen din? Tolk og løs likningen grafisk i et koordinatsystem.

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

To fjellklatrere, Henrik og André, skal overnatte på et fjell. De skal overnatte på en høyde på 2200 meter og bestemmer seg for å vedde om hvem som kommer seg ned til basen på 300 meter først.

Henrik er gammel og rutinert og holder en jevn fart fra han begynner turen nedover. Turen hans kan beskrives med funksjonen $p(x) = 100(22-2x)$, der $p$ er meter over havet, og $x$ er antall timer etter Henrik starter turen.

André er innbiller seg at han er ung og sprek og velger å sove lenge og starter turen nedover noen timer etter Henrik. André starter i en voldsom fart, men blir fort sliten og må senke farten. André sin tur nedover kan beskrives med funksjonen $h(x) = (\frac{100\cdot 36}{x})$, der $h$ viser meter over havet og $x$ er timer etter Henrik startet turen.

Under ser du en grafisk representasjon av funksjonene $p$ og $h$.

1. Forklar hva skjæringspunktene mellom grafene til $p$ og $h$ betyr.

I figuren under er også linjen $q = 300$ lagt inn.

2. Forklar hva skjæring mellom $h$ og $q$ betyr og skjæring mellom $p$ og $q$ betyr.

3. Finn skjæringsunktene mellom $p$ og $h$ med regning  (Merk: Både $x$- og $y$-verdi må oppgis for skjæringspunktene).

4. Finn skjæringsunktene mellom $q$ og $h$ med regning  (Merk: Både $x$- og $y$-verdi må oppgis for skjæringspunktene).

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-57-45.png)

#### Vurderingskriterier: Grunnleggende {#130241}

Alle oppgaver må besvares.  

1. Likningen må løses.
2. Her må de tolke og skissere begge grafene i samme koordinatsystem.
3. Gi en forklaring som viser sammenhengen mellom at løsning gir likhet av venstre og høyre side i likningen og at det tilsvarer skjæringspunktet mellom grafene.  

#### Vurderingskriterier: Middels

De må lage en situasjon som gir likningen. Deretter må de illustrere likningen grafisk og vise løsningen i koordinatsystemet.

#### Vurderingskriterier Avansert

Alle oppgavene må besvares

1. Studenten må forklare at siden $p$ og $h$ begge forteller høyden til André og Henrik, så må skjæringen være tidspunktene de samtidig er like høyt oppe.  
2. Tilsvarende må skjæringen mellom $h$ og $p$ med $q$ være når de er kommet seg ned.
3. Her må de sette opp og løse $p = h$.
4. Her må de sette opp og løse $q = h$.

### Bruke begrepene funksjon, variabel, uavhengig variabel (innverdi), avhengig variabel (utverdi), funksjonsverdi, definisjonsmengde og verdimengde

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene

Sammenhengen mellom sidelengden og arealet av et kvadrat er en funksjonssammenheng. Bruk eksemplet til å forklare begrepene funksjon, innverdi og funksjonsverdi.

#### Middels: Avgjøre og begrunne (ved hjelp av begrepene) om en gitt sammenheng er en funksjonssammenheng

Én av følgende sammenhenger er en funksjonssammenheng: A) Sammenhengen mellom omkrets og bredden i et rektangel. B) Sammenhengen mellom omkrets og areal av en sirkel.  

Avgjør og begrunn ved hjelp av en definisjon av funksjon hvilken av de to sammenhengene som er en funksjonssammenheng.
Bruk funksjonssammenhengen til å forklare begrepene uavhengig og avhengig variabel og definisjons- og verdimengde.

#### Vurderingskriterier: Grunnleggende {#130251}

Her må de peke på at arealet av en kvadrat med sidelengde $r$ er $r^2$ (altså at $A(r) = r^2$). Arealet er derfor en funksjon av $r$ (innverdi) fordi hver sidelengde $r$ gir et entydig areal (som her er funksjonsverdien).

#### Vurderingskriterier: Middels

Her må studenten peke på og begrunne hvorfor det er sammenhengen mellom omkrets og kvadrat som gir en funksjonssammenheng. Begrunnelsen må referere til en riktig definisjon av en funksjon. Deretter må de bruke eksempelet til å forklare begrepene det bes om.

### Gjøre om mellom ulike representasjonsformer for funksjonssammenhenger

#### Middels: Gjøre om mellom de fire representasjonene av funksjoner (Janviers tabell, Alfa 4.1), og vurdere elevers arbeid med overganger mellom representasjonene

Illustrasjonen til venstre viser en (litt forstørret) klinkekule som slippes ned en liten bakke. Skisser en en graf som viser sammenhengen mellom hastigheten til kulen og hvor mange meter kulen har bevegd seg i horisontal retning.
Beskriv en situasjon som passer til grafen til høyre. (Andreaksen viser kroner målt i 1000, førsteaksen viser tid)

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-58-35.png)
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-20-58-43.png)

#### Vurderingskriterier: Middels {#130262}

1. Studentene må skissere en graf som får fram sammenhengen på en riktig måte
2. Studentene må her peke på en (mulig) situasjon som kan beskrive grafen som er gitt. (Timelønn kan være en naturlig situasjon her).

## Funksjoner 10.02.23

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.
2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.
3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. På hyttetaket ligger det $70$ m$^3$ snø som skal spas bort. Hvert spadetak rommer $0,8$ m$^3$, og du greier $8$ spadetak i minuttet. Hva er sammenhengen mellom tiden og mengden snø igjen på taket?

2. I koordinatsystemet under ser du to grafer. Begrunn hvilken av dem som er grafen til en omvendt proporsjonal funksjon. Begrunnelsen må vise til et funksjonsuttrykk. (Å si at grafen ser ut sånn og sånn, er altså ikke en begrunnelse ;))

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-21-04-39.png)

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Tabellen under viser en funksjonssammenheng.

a. Avgjør om den er lineær, kvadratisk eller omvendt proporsjonal.

b. Lag en passende situasjon som kan høre til funksjonssammenhengen.

c. Finn funksjonsuttrykk, og skisser grafen.

| x  | 1    | 2    | 3   | 6   | 10 |
|--- |----- |----- |----- |----- |-----|
| y  | $\frac{1}{2}$ | 2  | $\frac{9}{2}$  | 18  | 50 |

1. Under ser du grafen til en funksjon.

a. Avgjør hva slags funksjon det er snakk om.

b. Finn funksjonsuttrykket.

c. Beskriv en situasjon som kan passe til funksjonen.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-21-04-54.png)

#### Vurderingskriterier: Grunnleggende {#100211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.  

#### Vurderingskriterier: Middels {#100212}

1. Studenten *må* lage en sammenheng mellom mengde snø og tid. Det naturlige er at å koble mengde snø fjernet per minutt, som er $8\cdot 0,\!8 = 6,\!4$. Siden vi begynne på $70$ må dette gi $f(x) = 70- 6,\!4x$, det $x$ er antall minutter.
2. Studenten må peke på egenskaper ved omvendtproporsjonale funksjoner for å begrunne. For eksempel kan en peke på at den grønne funksjonen oppfyller dobling av $x$ gir halvering av $y$. Altså at $x= 1$ gir $y=36$ og $x=2$ gir $y = 18$. De bør også pekes på at den blå grafen ikke oppfyller denne egenskapen da $x = 1$ gir $y$ over $30$ og $x= 2$ gir $y$ under $15$.

#### Vurderingskriterier: Avansert {#10213}

Studentene *må* peke på hvilken funksjon det er. I første eksempel kan de set at vi alltid har halvparten av et kvadrattall. Det gir funksjonen $f(x)  = x^2/2$. I det andre eksempelet ser vi at $x = 1$ gir $y= 25$ og $x= 5$ gir $y = 5$, altså en femdobling av $x$ gir at $y$ blir en femtedel.  
Deretter *må* studentene omforme funksjonene til de andre representasjonene det bes om.

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Anta at en lineær funksjon $f$ går gjennom punktene $(-3, -3)$ og $(6, 0)$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

#### Vurderingskriterier: Grunnleggende {#100221}

Peke på hva parameterne gjør for førstegradsfunksjoner

#### Vurderingskriterier: Middels {#100222}

Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En andregradsfunksjon kan skrives på formen $ax^2 + b x + c$. Gjengi med ord hvilken påvirkning endringer i $a$ (tallet foran $x^2$) og $c$ (konstantleddet) har på grafen til en andregradsfunksjon.

Skisser grafene $y = \frac{5}{x}$ og $y = \frac{-5}{x}$ i samme koordinatsystem.

### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#100231}

1. Peke på hva parameterne gjør for andregradsfunksjoner
2. Skissere de to omvendt proporsjonale grafene.  

#### Vurderingskriterier: Middels {#100232}

1. Omvendt proporsjonale:
Grafen må skisseres for $a>0$ og $a<0$. Det må komme fram hvorfor formen på grafen er som den er. For eksempel $a>0$ kan en gi et konkret eksempel på en om omvendt prop. funk. og framheve sammenhengen (skaleres $x$ opp med noe skaleres $y$ ned med det samme, derav navnet omvendt prop) $\rightarrow$  større og større $x$ gir $y$ som kryper mot $0$, mindre og mindre $x$ gir større og større $y$. Det bør komme fram noen symmetrier med grafen. Når $a<0$ kan en bare peke på at $a< 0$ gir bare samme graf flippet over $x$-aksen.  
Kvadratiske funksjoner:
Her må det kort komme fram at a avgjør hvor bratt funksjonen stiger (hvis $a>0$) eller synker ($a<0$), og at $c$ flytter grafen oppover eller nedover og tilsier hvor funksjonen skjærer andreaksen.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

Gitt likningen $20-5x = \frac{1}{2}(x+10)$.

Løs likningen
Tolk venstre side og høyre side som funksjonsuttrykk, og skisser grafene i samme koordinatsystem.
Forklar algebraisk og grafisk hva det vil si at tallet du fant i 1. er en løsning på likningen.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Gi en situasjon som passer til funksjonen $f(x)=20-\frac{1}{2}x$. Hva svarer likninga $20-\frac{1}{2}x=0$ til i situasjonsbeskrivelsen din? Tolk og løs likningen grafisk i et koordinatsystem.

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

La $f(x) = \frac{4}{x}$ og $g(x) = 1+3x$.

Skisser grafene.
Finn skjæringspunktene ved regning (Merk: Både $x$- og $y$-verdi må oppgis for skjæringspunktene).

#### Vurderingskriterier: Grunnleggende {#100241}

Alle oppgaver må besvares

1. Likningen må løses.
2. Her må de tolke og skissere begge grafene i samme koordinatsystem.
3. Gi en forklaring som viser sammenhengen mellom at løsning gir likhet av venstre og høyre side i likningen og at det tilsvarer skjæringspunktet mellom grafene.  

#### Vurderingskriterier: Middels {#100242}

De må lage en situasjon som gir likningen. Deretter må de illustrere likningen grafisk og vise løsningen i koordinatsystemet.\

#### Vurderingskriterier: Avansert {#100243}

Begge oppgavene må besvares

1. De må skissere grafene slik at på en god måte (skissa må ikke være utrolig nøyaktig, men bør heller ikke være voldsomt slurvete).
2. De må sette opp likninga og finne skjæringspunktene ved regning.

### Bruke begrepene funksjon, variabel, uavhengig variabel (innverdi), avhengig variabel (utverdi), funksjonsverdi, definisjonsmengde og verdimengde

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene

Sammenhengen mellom radien og arealet av en sirkel er en funksjonssammenheng. Bruk eksemplet til å forklare begrepene funksjon, innverdi og funksjonsverdi.

#### Middels: Avgjøre og begrunne (ved hjelp av begrepene) om en gitt sammenheng er en funksjonssammenheng

Én av følgende sammenhenger er en funksjonssammenheng: A) Sammenhengen mellom omkrets og areal i et rektangel. B) Sammenhengen mellom omkrets og areal i et kvadrat.  

Avgjør og begrunn ved hjelp av en definisjon av funksjon hvilken av de to sammenhengene som er en funksjonssammenheng.
Bruk funksjonssammenhengen til å forklare begrepene uavhengig og avhengig variabel og definisjons- og verdimengde.

#### Vurderingskriterier: Grunnleggende {#100251}

Her må de peke på at arealet av en sirkel med radius $r$ er $\pi$ multiplisert med $r^2$ (altså at $A(r) = \pi r^2$). Arealet er derfor en funksjon av $r$ (innverdi) fordi hver radius gir et entydig areal (som her er funksjonsverdien).\

#### Vurderingskriterier: Middels {#100252}

Her må studenten peke på og begrunne hvorfor det er sammenhengen mellom omkrets og kvadrat som gir en funksjonssammenheng. Begrunnelsen må referere til en riktig definisjon av en funksjon. Deretter må de bruke eksempelet til å forklare begrepene det bes om.

### Gjøre om mellom ulike representasjonsformer for funksjonssammenhenger

#### Middels: Gjøre om mellom de fire representasjonene av funksjoner (Janviers tabell, Alfa 4.1), og vurdere elevers arbeid med overganger mellom representasjonene

Illustrasjonen til venstre viser havdybden målt i ei linje 100 meter utover fra strandkanten. Skisser en en graf som viser sammenhengen mellom avstanden fra land og havdybden.
Beskriv en situasjon som passer til grafen til høyre. (Andreaksen viser meter over bakken, førsteaksen viser tid.)

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-21-09-27.png)
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-21-09-32.png)

#### Vurderingskriterier: Middels {#100262}

1. Studentene må skissere en graf som får fram sammenhengen på en riktig måte
2. Studentene må her peke på en (mulig) situasjon som kan beskrive grafen som er gitt.

## Funksjoner 3.02.23

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.
2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.
3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. Under ser du tre situasjoner. Avgjør og begrunn hva slags funksjon det er snakk om i hvert tilfelle. Begrunnelsen må vise til både en graf og et funksjonsuttrykk.

a. Du skal lage en rektangulær innhegning til hønene dine på $121$m$^2$. Hva er sammenhengen mellom bredden og lengden i innhegningen?

b. Du skal lage en sirkulær figur med radius $r$. Hva er sammenhengen mellom radius og arealet arealet på figuren?

c. Du kjører med bil fra Skien til Kristiansand. Du bruker $0.5$ liter bensin per mil. Du starter i Skien med 50 liter bensin. Hva er sammenhengen mellom liter igjen på tanken og mil du har kjørt?

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Avgjør om funksjonssammenhengen fra tabellen under er lineær, kvadratisk eller omvendt proporsjonal. Lag en passende situasjon som kan høre ti funksjonssammenhengen, og en tilhørende graf og funksjonsuttrykk.

| x  | 16   | 8    | 4   | 2   | 1 |
|--- |--- |--- |--- |--- |---|
| y  | 16 | 32  | 64 | 128  | 256 |

2. Avgjør og begrunn hva slags funksjon følgende situasjon beskriver. Begrunnelse må vise til både en graf, tabell og et funksjonsuttrykk.

Du skal lage en sirkulær figur med radius $r$. Hva er sammenhengen mellom radius og arealet arealet på figuren?
3. Under ser du en graf. Beskriv deretter en situasjon som kan passe til grafen og gi et funksjonsuttrykk til grafen og lag en tabell til funksjonen.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-21-13-57.png)

#### Vurderingskriterier: Grunnleggende {#130s211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.

#### Vurderingskriterier: Middels {#130s212}

De må avgjøre, med begrunnelse (for eksempel ved å peke på definisjon og funksjonsuttrykket de har gitt), hvilken type funksjon som hører til alle tre situasjonene. Det skal også gis et funksjonsuttrykk og en grafisk representasjon av situasjonen.

#### Vurderingskriterier: Avansert {#13s0213}

Her må de gjøre det samme som på middels bare at de nå starter med ulike representasjoner og må gjøre om til de andre representasjonsformene (representasjonsformene er: situasjon, funksjonsuttrykk, tabell og graf)!

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Anta at en lineær funksjon $f$ går gjennom punktene $(\frac{9}{3}, 7)$ og $(\frac{18}{3}, 10)$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

#### Vurderingskriterier: Grunnleggende {#130s221}

Peke på hva parameterne gjør for førstegradsfunksjoner

#### Vurderingskriterier: Middels {#13022s2}

Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En andregradsfunksjon kan skrives på formen $ax^2 + b x + c$. Gjengi med ord hvilken påvirkning endringer i $a$ (tallet foran $x^2$) og $c$ (konstantleddet) har på grafen til en andregradsfunksjon.

Skisser grafene $y = \frac{5}{x}$ og $y = \frac{-5}{x}$ i samme koordinatsystem.

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#1302s31}

i. Peke på hva parameterne gjør for andregradsfunksjoner
ii. Skissere de to omvendt proporsjonale grafene

#### Vurderingskriterier: Middels {#13s0232}

i. Omvendt proporsjonale: Grafen må skisseres for a>0 og a<0. Det må komme fram hvorfor formen på grafen er som den er. For eksempel a> 0 kan en gi et konkret eksempel på en om omvendt prop. funk. og framheve sammenhengen (skaleres x opp med noe skaleres y ned med det samme, derav navnet omvendt prop)  større og større x gir y som kryper mot 0, mindre og mindre x gir større og større y. Det bør komme fram noen symmetrier med grafen. Når a>0 er forklar kan en bare peke på at a<0 gir bare samme graf flippet over x-aksen
ii. Kvadratiske funksjoner: Her må det kort komme fram at a avgjør hvor bratt funksjonen stiger (hvis a>0) eller synker (a<0), og at c flytter grafen oppover eller nedover og tilsier hvor funksjonen skjærer andreaksen.

### Løse likninger fra funksjonsperspektiv

#### Grunnleggende: Forklare algebraisk og grafisk hva som menes med løsningen av en lineær likning

Gitt likningen $3x + 6 = -2x + 3$.

Løs likningen
Tolk venstre side og høyre side som funksjonsuttrykk, og skisser grafene i samme koordinatsystem.
Forklar algebraisk og grafisk hva det vil si at tallet du fant i 1. er en løsning på likningen.

#### Middels: Tolke lineære likninger grafisk, og finne skjæringspunkt mellom lineære grafer og mellom lineære grafer og aksene

1. Lag en realistisk situasjon som gir opphav til likningen $20x + 30 =10x + 80$. Tolk likningen grafisk og vis løsningen i et koordinatsystem.

#### Avansert: Tolke likninger grafisk, og finne skjæringspunkt mellom grafer til ulike typer funksjoner og mellom grafer og aksene

La $f(x) = \frac{30}{x}$ og $g(x) = 2x+4$.

Skisser grafene.
Finn skjæringspunktene ved regning.

#### Vurderingskriterier: Grunnleggende {#1302s41}

Alle oppgaver må besvares
i. Likningen må løses.
ii. Her må de tolke og skissere begge grafene i samme koordinatsystem.
iii. Gi en forklaring som viser sammenhengen mellom at løsning gir likhet av venstre og høyre side i likningen og at det tilsvarer skjæringspunktet mellom grafene.

#### Vurderingskriterier: Middels {#1s30242}

De må lage en situasjon som gir likningen. Deretter må de illustrere likningen grafisk og vise løsningen i koordinatsystemet.

#### Vurderingskriterier: Avansert {#asdsf1}

Begge oppgavene må besvares
i. De må skissere grafene slik at på en god måte (skissa må ikke være utrolig nøyaktig, men bør heller ikke være voldsomt slurvete).
ii. De må sette opp likninga og finne skjæringspunktene ved regning.

## Funksjoner 27.01.23

### Bruke begrepene lineær funksjon, andregradsfunksjon og omvendt proporsjonal funksjon

#### Grunnleggende: Forklare kjennetegn ved og gi eksempler på funksjonstypene

1. Gi et eksempel på en lineær funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en lineær funksjon.
2. Gi et eksempel på en kvadratisk funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en kvadratisk funksjon.
3. Gi et eksempel på en omvendt proporsjonal funksjon, og forklart kort, med utgangspunkt i eksemplet ditt, hva som kjennetegner en omvendt proporsjonal funksjon.

#### Middels: Bestemme og begrunne funksjonstype basert på beskrivelse av situasjon, uttrykk, graf og tabell

1. Under ser du tre situasjoner. Avgjør og begrunn hva slags funksjon det er snakk om i hvert tilfelle. Begrunnelsen må vise til både en graf og et funksjonsuttrykk.

a. Du skal kjøre $120$km. Hva er sammenhengen mellom hastigheten du kjører i (du kjører i konstant hastighet) og tiden det tar før du kommer frem?

b. Du skal male en rektangulær vegg der høyden er 2 meter lengre enn bredden. Hva er sammenhengen mellom bredden og arealet du må male?

c. Du skal utføre et arbeid og får 1000 kr i grunnhonorar for å ta på deg oppdraget. I tillegg får du en timelønn på 250 kroner. Hva er sammenhengen mellom antall timer du utfører på arbeidet og inntekten du får for arbeidet?

#### Avansert: Gjøre om mellom ulike representasjonsformer for de tre funksjonstypene, og begrunne omgjøringen

1. Lineære funksjoner.

a. Angi en situasjon som svarer til en lineær funksjon (som er ulik situasjonene fra oppgaven over).

b. Skisser grafen, og sett opp funksjonsuttrykk.

c. Begrunn kort hvordan grafen og funksjonsuttrykket svarer til situasjonseksemplet.

1. Kvadratiske funksjoner.

a. Angi en situasjon som svarer til en kvadratisk funksjon (som er ulik situasjonene fra oppgaven over).

b. Skisser grafen, og sett opp funksjonsuttrykk.

c. Begrunn kort hvordan grafen og funksjonsuttrykket svarer til situasjonseksemplet.  

1. Omvendt proporsjonale funksjoner.

a. Angi en situasjon som svarer til en omvendt proporsjonal funksjon (som er ulik situasjonene fra oppgaven over).

b. Skisser grafen, og sett opp funksjonsuttrykk.

c. Begrunn kort hvordan grafen og funksjonsuttrykket svarer til situasjonseksemplet.

#### Vurderingskriterier: Grunnleggende {#13sdfs211}

Her må de gi et eksempel og forklare kjennetegnene, slik oppgaven ber om.

#### Vurderingskriterier: Middels {#130sasd212}

De må avgjøre, med begrunnelse (for eksempel ved å peke på definisjon og funksjonsuttrykket de har gitt), hvilken type funksjon som hører til alle tre situasjonene. Det skal også gis et funksjonsuttrykk og en grafisk representasjon av situasjonen

#### Vurderingskriterier: Avansert {#13asds0213}

Her må de gjøre det samme som på middels bare at de må på egen hånd gi en situasjon!

### Forklare sammenhenger mellom parameterne i funksjonsuttrykket og grafen til lineære funksjoner

#### Grunnleggende: Forklare hvordan endringer i stigningstall og konstantledd påvirker grafen til en lineær funksjon

Gitt en lineær funksjon $ax+b$, der $a = 1$ og $b=0$. Illustrer i et koordinatsystem hvordan endringer av $a$ påvirker grafen og hvordan endringer av $b$ påvirker grafen.

#### Middels: Forklare hvordan man kan finne likninga til en lineær funksjon når to punkter på grafen er kjent uten bruk av topunktsformelen

Anta at en lineær funksjon $f$ går gjennom punktene $(\frac{5}{2}, 7)$ og $(\frac{11}{2}, 4)$. Forklar hvordan vi kan finne likninga til den lineære funksjonen.

#### Vurderingskriterier: Grunnleggende {#130asds221}

Peke på hva parameterne gjør for førstegradsfunksjoner

#### Vurderingskriterier: Middels {#13asd022s2}

Finne likninga og forklare hvordan på en slik måte at man klart forstår det generelle i fremgangsmåten (kunne åpenbart blitt brukt for hvilke som helst punkt-par).

### Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

#### Grunnleggende: Gjengi hvilke roller parameterne i funksjonsuttrykkene til andregrads- og omvendt proporsjonale funksjoner spiller med hensyn til grafene

En andregradsfunksjon kan skrives på formen $ax^2 + b x + c$. Gjengi med ord hvilken påvirkning endringer i $a$ (tallet foran $x^2$) og $c$ (konstantleddet) har på grafen til en andregradsfunksjon.

Skisser grafene $y = \frac{15}{x}$ og $y = \frac{-15}{x}$ i samme koordinatsystem.

#### Middels: Forklare hvordan endringer i parameterne i funksjonsuttrykket påvirker grafene til andregrads- og omvendt proporsjonale funksjoner

En omvendt proporsjonal funksjon ser generelt slik ut: $f(x)=\frac{a}{x}$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hvordan grafen må se ut når
parameteren $a$ er større enn 0.
parameteren $a$ er mindre enn 0

En kvadratisk funksjon ser generelt slik ut: $f(x)=ax^2+bx+c$. Forklar kort (slik at det fremstår meningsfullt for noen som ikke kan det) og vis i et koordinatsystem hva som skjer med grafen når
parameteren $a$ endres.
parameteren $c$ endres.

#### Vurderingskriterier: Grunnleggende {#1asd302s31}

i. Peke på hva parameterne gjør for andregradsfunksjoner
ii. Skissere de to omvendt proporsjonale grafene

#### Vurderingskriterier: Middels {#13s0sdf232}

Gjøre begge oppdragene som står i kulepunktene på en tilfredsstillende måte.
