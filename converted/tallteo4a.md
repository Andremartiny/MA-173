#### Avansert:  Øveoppgaver

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
   P_1 & = 1
   \\
   P_2 & = 1 + 2\cdot 2+1
   \\
   P_3 & = 1 + (2\cdot 2 + 1) +(2\cdot 3 + 1)
   \\
   \vdots
   \\
   P_n & = 1 + (2\cdot 2 + 1) + (2\cdot 3 + 1)+ \ldots + (2\cdot n + 1).
   \end{aligned}
   $$
   Fra erfaring, ser vi at vi ønsker å ha et ledd $(2\cdot 1 + 1)$ for å enkelt kunne bruke at $T_n = 1+2+3+\ldots+n = \frac{n(n+1)}{2}$. Dette løser vi enkelt ved å legge til og trekke fra. Vi får derfor at
   $$
   \begin{aligned}
   P_n & = 1 + (2\cdot 2 + 1) + (2\cdot 3 + 1)+ \ldots + (2\cdot n + 1)
   \\
   P_n & = 1 - (2\cdot 1 + 1) +(2\cdot 1 + 1) + (2\cdot 2 + 1) + (2\cdot 3 + 1)+ \ldots + (2\cdot n + 1)
   \\
   P_n & = 1 - 2 - 1 + 2(1+2+3+\ldots + n) + 2\cdot n = -3 + 2T_n + 2n = -3 + n(n+1)+2n = -3 + n^2 + n + 2n
   \end{aligned}
   $$

#### Avansert:  Tallteori

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 7$, $F_2 = 12$ og $F_3 = 18$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-12-43-49.png)

##### Vurderingskriterier

Ved å betrakte figuren bør studentene se at figuren kan skrives som $F_1 = 3+ 4$, $F_2 = 3 + 4 + 5$, $F_3 = 3+4+5+6$ og generelt $F_n = 3+4+5+\ldots + n+3$. Formen på tillegget er dermed $n+3$. Videre må de nå bare bruke riktig teknikk for å komme i mål. Her kan de se i heftet for mer info om teknikkene.

#### Avansert:  17.02.23

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 2$, $F_2 = 8$ og $F_3 = 16$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-40-43.png)

#### Vurderingskriterier avansert:  17.02.23

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel. For eksempel kan det pekes på at figuren nesten er to trekanter som starter *en før* (altså $T_{n+1}$) lagt opp på hverandre. Begge mangler bare toppen og deler rad 2. Dermed får vi $F_n = 2T_{n+1} - 2- 2 = (n+2)(n+1) - 4 $

ii. Her må de igjen bruke sum av tillegg som på middels.

#### Avansert:  13.02.23

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 3$, $F_2 = 13$ og $F_3 = 31$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-37-18.png)

#### Vurderingskriterier avansert:  13.02.23

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel. For eksempel kan en innse at de to ytterste firkantene er $n^2$, mens det skrå kvadratet kan deles inn i to "lag" som gir $n^2$ for det ene og $(n-1)^2$ for det andre. Totalt blir dette $2n^2+n^2 + (n-1)^2 $.

ii. Her må de igjen bruke sum av tillegg som på middels.

#### Avansert:  10.02.23

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 12$, $F_2 = 26$ og $F_3 = 44$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-34-41.png)

#### Vurderingskriterier avansert:  10.02.23

Studenten må besvare begge oppgavene.

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel.

ii. Her må de igjen bruke sum av tillegg som på middels.

#### Avansert:  03.02.23

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 4$, $F_2 = 10$ og $F_3 = 19$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-31-42.png)

#### Avansert:  27.01.23

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 10$, $F_2 = 22$ og $F_3 = 42$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-06-04.png)

#### Vurderingskriterier avansert:  27.01.23

MERK: Her står det feil i oppgavetekst. Det skal være F_2 = 24

i.  Her må de henvise til figuren (gjerne ved å ha tegnet den
inn selv) og forklare hvordan den er brutt ned for å finne
en eksplisitt formel

ii. Her må de igjen bruke sum av tillegg sånn som på middels

