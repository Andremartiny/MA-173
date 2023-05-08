#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  Øveoppgaver

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

1. \
a. Vi ser at vi må trekke fra et kvadrattall, så vi må dermed bruke de to trekanttallene våre til å kunne trekke fra kvadratet. Dette kan vi for eksempel illustrere på følgende måte

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-25-12-58-11.png)>

Der gul og grønn illustrerer trekanttallene og røde sirkler er det som skal trekkes vekk. Eller følgende måte

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-25-12-58-27.png)

Der gul og grønn illustrerer trekanttallene, men at vi har tatt vekk et kvadrattall fra det ene trekanttallet.

b. Ved å stirre hard kan vi se i første figur at hvis vi ikke trekker vekk kvadratet, så får vi et rektangel med størrelse $n+2$ og $n+1$. Kvadratet vi trekker fra ser vi at har størrelse $(n-1)^2$, som gir uttrykket $(n+2)(n+1)-(n-1)^2$.

c. Her må vi bare regne
$$
\begin{aligned}
2T_{n+1} - K_{n-1}
& =
2\frac{(n+1)(n+2)}{2} - (n-1)^2
\\
& =
(n+2)(n+1)-(n-1)^2
\end{aligned}
$$

4. Vi utnytter at vi vet at $n^2 + 2n + 1 = (n+1)^2$. Vi kan derfor skrive om uttrykket som $n^2 + 3n + 1 = n^2 + 2n + 1 +n = (n+1)^2+n$. Nå kan vi enkelt se at tillegget fra figur til figur er $(2n+1) + 1$, der $2n+1$ er økninga av kvadratet $+1$ er økningen fra ledded $n$. Dette gir oss også en enkel oversettelse til en figur, dette overlates til leseren!

#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  08.05

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 8$, $F_3 = 16$, $F_4 = 26$ og $F_5 = 38$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

##### Vuderingskriterier

Vi begynner med å analysere utviklingen av tallrekka. Vi ser at økningen er \(6\) så \(8\), så \(10\) og så \(12\). Tilleggene øker altså med \(2\). Dermed kan vi skrive 
$$
\begin{aligned}
F_1 & = 2
\\
F_2 & = 2 + 2\cdot 2 + 2
\\
F_3 & = 2 + 2\cdot 2 + 2 + 2\cdot 3 + 2
\\
\vdots
\\
F_n & = 2 + (2\cdot 2 + 2) + (2\cdot 3 + 2) + \ldots + (2\cdot n + 2).
\end{aligned}
$$

Ved å justere første leddet i summen får vi
$$
F_n = -2 + (2\cdot 1 + 2) + (2\cdot 2 + 2) + (2\cdot 3 + 2) + \ldots + (2\cdot n + 2).
$$

Denne kan vi nå enkelt skrive om til
$$
\begin{aligned}
F_n  
& =  -2 + 2(1+2+\ldots + n) + 2n
\\
& = -2 + 2T_n + 2n
\\
& = -2 + n(n+1) + 2n.
\end{aligned}
$$

Vi kan nå bruke formelen til å trekke ut en måte å lage figuren. Vi ser at det er to trekanttall og to linjer med lengde \(n\), der det i tillegg er trukket vekk 2. (Figuren får man lage selv 😉).


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  28.04

Se øveoppgave 1 a-c.


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  24.04

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


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  31.03.23

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


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  17.02.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 6$, $F_3 = 11$, $F_4 = 17$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

#### Vurderingskriterier avansert:  17.02.23

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  13.02.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 1$, $F_2 = 6$, $F_3 = 14$, $F_4 = 25$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

#### Vurderingskriterier avansert:  13.02.23

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  10.02.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 2$, $F_2 = 8$, $F_3 = 16$, $F_4 = 26$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

#### Vurderingskriterier avansert:  10.02.23

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det
være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  03.02.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 6$, $F_2 = 12$, $F_3 = 20$, $F_4 = 30$ og $F_5 = 42$.

Lag en figur som følger mønsteret til $F_n$. Det er nok å illustrere $F_1$, $F_2$ og $F_3$, så lengde det får fram mønsteret.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  27.01.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 1$, $F_2 = 9$, $F_3 = 20$, $F_4 = 34$ og $F_5 = 51$.

Lag en figur som følger mønsteret til $F_n$.
Vis og forklar sammenhengen mellom tallrekken og figurene rekursivt.
Finn en eksplisitt formel på to forskjellige måter.

#### Vurderingskriterier avansert:  27.01.23

Her må illustrere figuren (nok med de tre første), men
strukturen må komme fram i hvordan figuren utvikler seg!

ii. Her må de peke på utviklingen i både figur og tallrekker for
så å forklare hvordan de utvikler seg

iii. Finn eksplisitt på to forskjellige måter: Typisk kan det være: Bryte ned figur geometrisk, sum av tillegg,
gauss-triks algebraisk, gauss-triks ved figur. Merk at å
bryte ned figuren på flere måter teller som forskjellige
måter


#### Avansert: Beskrive oppbygningen av figurtall (alle typer),  10.01.23

Du får vite at et figurtall $F_n$ øker på følgende måte. $F_1 = 3$, $F_2 = 8$, $F_3 = 15$, $F_4 = 24$ og $F_5 = 35$.

Lag en figur som følger mønsteret til $F_n$. Begrunn sammenhengen mellom figuren og tallfølgen.

