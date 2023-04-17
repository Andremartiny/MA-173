#### Avansert: Forklare og bruke begrepet uniform sannsynlighetsmodell,  Øveppgaver

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
