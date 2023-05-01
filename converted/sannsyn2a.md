#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  Øveppgaver

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

#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  28.04.23

André har en firesidet terning på kontoret sitt, der det er like sannsynlig å slå 1, 2, 3 og 4. André kaster to ganger og multipliserer verdiene han fikk.

1. Sett opp en modell som gir opphav til en uniform sannsynlighetsmodell.
2. Avgjør ved hjelp av modellen hva sannsynligheten er for at André får mer enn 7 når han har slått begge terningene.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan de tegne et trediagram som dette

![](../../img/sannsyn/utfallstre.png)

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

#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  24.04.23

Henrik og André spiller et spill der de først kaster en vanlig seksidet terning og deretter en mynt. Vi anter at det er like sannsynlig å få kron og mynt, og at alle seks sidene på terningen er like sannsynlig. Spillet fungerer slik: Når man har kastet en verdi, $n$, på terningen så kaster man mynten. Hvis den lander på mynt, får man dobbler man verdien man fikk på terningen. Kaster man kron får man kun verdien man hadde på terningen.

For eksempel vil et terningkast på 4 og så et kast som gir mynt gi 8 poeng, mens et terningkast på 6 og så en kron vil gi 6 poeng.

1. Sett opp et utfallsrom som gir opphav til en uniform sannsynlighetsmodell.
2. Bruk modellen til å avgjøre hva sannsynligheten er for å få 6 eller flere poeng når man spiller spillet.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan dette gjøres ved å sette opp utfallsrommet $\{1m, 2m, 3m, 4m, 5m, 6m, 1k, 2k, 3k, 4k, 5k, 6k\}$, der siffrene er tallene fra terningskastet og $m$ står får mynt og $k$ står for kron. Studenten kan også tegne opp et utfallstre og peke på at greiene tilsvarer hvert utfall. Studenten må deretter begrunne at modellen er uniform. Det kan de gjøre ved å enkelt peke på at første delforsøk er uniform, slik som det andre delforsøket (myntkastet). Dermed må det være like sannsynlig å få $3m$ som $6k$, siden $3$ og $6$ er like sannsynlig og $m$ og $k$ er like sannsnylig.
2. Studenten kan nå bare telle opp fra utfallsrommet fra forrige oppgave. $3m$, $4m$, $5m$ og $6m$ vil tilsvare en poengverdi på $6, 8, 10$ og $12$. I tillegg vil $6k$ tilsvare en poengverdi på $6$. Det er altså 5 gunstige utfall, noe som gir en sannsynlighet på $\frac{5}{12}$.

#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  17.04.23

Henrik skal skyte straffespark og har alltid 50% sannsynlighet for å score. Henrik sykter tre ganger.

1. Sett opp et utfallsrom som gir en uniform sannsynlighetsmodell.

2. Avgjør hva sannsynligheten er for at Henrik scorer på nøyaktig to av tre av skuddene.

##### Vurderingskriterier

1. Studenten *må* sette opp en uniform sannsynlighetsmodell. For eksempel kan dette gjøres ved å sette opp utfallsrommet $\{BBB, BBM, BMB, BMM, MBB, MBM, MMB, MMM\}$, der $B$ står for *bom* og $M$ står for *mål*. Vi ser dermed at det er åtte utfall og siden det er lik sannsynlighet for både mål og bom, så er alle utfallene like sannsynlig.
2. Studenten kan nå bare telle opp fra utfallsrommet fra forrige oppgave. For eksempel ser vi fra 1. at det er utfallene $\{BMM, MBM, MMB\}$ som tilsvarer nøyaktig to mål på tre skudd. Det gir at $P(\text{Henrik scorer på nøyaktig to av tre skudd}) = \frac{3}{8}$.

#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  31.03.23

Det er 15 personer i en klasse. Det skal velges ut to elever som skal være i elevrådet og begge to skal trekkes tilfeldig. Henrik vil veldig gjerne være med i elevrådet. Sett opp en uniform sannsynlighetsmodell som får fram at det er $\frac{2}{15}$ sannsynlighet for at Henrik får være med i elevrådet.

##### Vurderingskriterier

Studenten må sette opp et utfallsrom som gir opphav til en uniform sannsynlighetsmodell som viser at sannsynligheten er $\frac{2}{15}$. E naturlig måte å gjøre dette på er for eksempel ved å si at klassen settes opp i en tilfeldig rekkefølge (for eksempel ved loddtrekning). Det gjør at alle elvene har like stor sannsynlighet for å havne på hver av de femten plassene. Hvis det er de to første i rekken som får være med i elevrådet tilsvarer denne måten å trekke ut elevrådsmedlemmene den samme situasjonen som beskrevet i oppgaven. Dermed er det lik sannsynlighet for å havne på en av $15$ plasser, en uniform sannsynlighetsmodell der utfallsrommet er {Henrik havner på første plass, Henrik havner på andre plass, Henrik havner på tredje plass,..., Henrik havner på femtende plass}. Det er kun to av plassene som får han med i elevrådet, dermed $\frac{2}{15}$ sannsynlighet for dette.
