
#### Middels: Finne eksplisitt uttrykk for figurtall,  Øveoppgaver

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


#### Middels: Finne eksplisitt uttrykk for figurtall,  24.04

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


#### Middels: Finne eksplisitt uttrykk for figurtall,  31.03.23

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


#### Middels: Finne eksplisitt uttrykk for figurtall,  17.02.23

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 6, 15, 28,  \ldots$.

#### Vurderingskriterier middels:  17.02.23

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $4n-3$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 5 + 9 + 13 + \ldots + 4n - 3.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).


#### Middels: Finne eksplisitt uttrykk for figurtall,  13.02.23

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører sekskanttallene er $1, 6, 15, 28,  \ldots$.

#### Vurderingskriterier middels:  13.02.23

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $4n-3$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 5 + 9 + 13 + \ldots + 4n - 3.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).


#### Middels: Finne eksplisitt uttrykk for figurtall,  10.02.23

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 5, 12, 22, \ldots$.

#### Vurderingskriterier middels:  10.02.23

Studenten må illustrere figurene og finne eksplisitt uttrykk med riktig teknikk.

Studenten må derfor utlede at formen på tillegget er $3n-2$, som gir at figurtall nummer $n$kan skrives som summen av tilleggene slik:
$$
F_n = 1 + 4 + 7 + 10 + \ldots + 3n - 2.
$$
Deretter må de jobbe med summen av tilleggene og bruke den eksplisitte formelen ved å
bruke formelen for trekanttall (se heftet for teknikken om sum
av tillegg).


#### Middels: Finne eksplisitt uttrykk for figurtall,  03.02.23

Illustrer syvkanttallene opp til $H_3$, og utled eksplisitt uttrykk for $H_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 7, 18, 34, \ldots$.


#### Middels: Finne eksplisitt uttrykk for figurtall,  27.01.23

Illustrer femkanttallene opp til $P_3$, og utled eksplisitt uttrykk for $P_n$ ved hjelp av strategien sum av tillegg. Merk at tallrekken som tilhører femkanttallene er $1, 5, 12, 22, \ldots$.

#### Vurderingskriterier middels:  27.01.23

Her må det være med en illustrasjon. I tillegg *må* den
eksplisitte formelen utledes ved å bruke sum av tillegg: Det vil
si jobbe seg fra $1+4+7+\ldots + 3n-2$ til $n^2+\frac{n(n-1)}{2}$ ved hjelp av
algebra og (mest sannsynlig) formelen for trekanttall.


#### Middels: Finne eksplisitt uttrykk for figurtall,  10.01.23

Illustrer sekskanttallene opp til $H_4$, og utled eksplisitt uttrykk for $H_n$ ved hjelp av strategien sum av tillegg.
Avansert: Ved hjelp av geometrisk betraktning/stirre hardt og sum av tillegg for sammensatte figurtall.
På figuren under ser du de tre første figurene i en sammensatt figur, der $F_1 = 12$, $F_2 = 22$ og $F_3 = 34$.

1. Finn en eksplsitt formel for $F_n$ ved å betrakte figuren geometrisk.

2. Finn en eksplisitt formel ved hjelp av sum av tillegg.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-13-53-34.png)

