#### Avansert: Finne eksplisitt uttrykk for figurtall,  Øveoppgaver

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

#### Avansert: Finne eksplisitt uttrykk for figurtall,  28.04

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 4$, $F_2 = 10$ og $F_3 = 19$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-31-42.png)

##### Vurderingskriterier

1. Studenten må betrakte figuren og finne en eksplisitt formel ved å referere til figuren. For eksempel kan man ved å betrakte figuren figuren geometrisk kan en se at det er en trekant og et kvadrat. Kvadratet har størrelse som figurtallsnummeret (figurtall 3 har bredde 3, figurtall 4 har bredde 4, figurtall $n$ må da ha bredde $n$). Trekanten har alltid lengde én mer enn figurtallsnummeret, for figur $n$ er trekanten trekanttall $n+1$. Dermed får vi $n^2 + T_{n+1} = n^2 + \frac{(n+1)(n+2)}{2}$.
2. Studenten kan bruke tolkningen fra 1. til å peke på at trekanten øker med $n+1$ og at kvadratet øker med det n'te oddetallet $2n-1$. Dermed er formen på tillegget $n+1 + 2n-1 = 3n$. Dermed kan vi nå bruke teknikken sum av tilleg ved å skrive ut figurtallene som en sum av tillegg:
$$
\begin{aligned}
F_n
& = 4 + (3\cdot 2) + (3\cdot 3) + (3\cdot 4 ) + \ldots + 3n
\\
&
= (1 + 3\cdot 1) + (3\cdot 3 ) + (3\cdot 4 ) + \ldots + 3n
\\
&
= 1 + 3(1+2+3+\ldots + n)
\\
&
1+3\frac{n(n+1)}{2}
\end{aligned}
$$
Her har vi et eksplisitt uttrykk for figurtall nummer $n$ og studenten trenger ikke omforme dette til å passe med 1.
La oss bare gjøre det slik at vi kan se at det gjør det ved å gange ut begge uttrykkene (studenten trenger ikke gjøre dette):
$$
\begin{aligned}
1+3\frac{n(n+1)}{2}
& =
\frac{2 + 3n(n+1)}{2}
\\
&
= \frac{2 + 3n^2 +3n}{2},
\end{aligned}
$$
Videre ser vi at svaret fra forrige oppgave kan skrives som
$$
\begin{aligned}
n^2 + \frac{(n+1)(n+2)}{2}
& =
\frac{2n^2 + n^2+3n+2}{2}
\\
&
= \frac{3n^2 +2n+2}{2}.
\end{aligned}
$$

#### Avansert: Finne eksplisitt uttrykk for figurtall,  24.04

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

#### Avansert: Finne eksplisitt uttrykk for figurtall,  31.03.23

På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 7$, $F_2 = 12$ og $F_3 = 18$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-12-43-49.png)

##### Vurderingskriterier

Ved å betrakte figuren bør studentene se at figuren kan skrives som $F_1 = 3+ 4$, $F_2 = 3 + 4 + 5$, $F_3 = 3+4+5+6$ og generelt $F_n = 3+4+5+\ldots + n+3$. Formen på tillegget er dermed $n+3$. Videre må de nå bare bruke riktig teknikk for å komme i mål. Her kan de se i heftet for mer info om teknikkene.

#### Avansert: Finne eksplisitt uttrykk for figurtall,  17.02.23

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

#### Avansert: Finne eksplisitt uttrykk for figurtall,  13.02.23

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

#### Avansert: Finne eksplisitt uttrykk for figurtall,  10.02.23

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

#### Avansert: Finne eksplisitt uttrykk for figurtall,  03.02.23

På figuren under ser du de fire første figurene i en sammensatt figur, der $F_1 = 4$, $F_2 = 10$ og $F_3 = 19$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-31-42.png)

#### Avansert: Finne eksplisitt uttrykk for figurtall,  27.01.23

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

