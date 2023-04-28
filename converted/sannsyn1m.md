#### Middels: Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell,  Øveppgaver

1. Alfa 7.10
2. Alfa 7.11

##### Løsningsforslag

Siden $P\left( u_{1} \right) = 0.2$, og $P\left( u_{2} \right) = 0.3$ og
i tillegg
$P(\left\{ u_{1},u_{2},u_{3}\} \right) = 1 = P\left( u_{1} \right) + P\left( u_{2} \right) + P\left( u_{3} \right) = P(u_{3})+0.5$
får vi at $P\left( u_{3} \right) = 0.5$.\

#### Middels: Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell,  28.04.23

1. Hva er galt med denne sannsynlighetsmodellen? \(U = \{u_1, u_2, u_3\} \), \(P(u_1) = 0,5\), \(P(u_2) = 0,4\) og \(P(u_3) = 0.2\)?
2. La et forsøk ha et utfallsrom \(U = { u_1, u_2, u_3, u_4, u_5} \). Forklar at \(P(\{u_3\})\) må være større enn \(0.2\) hvis \(P(\{u_1,u_3\}) = 0.8\) og \(P(\{u_2, u_3\}) = 0.4\).  

##### Vurderingskriterier

1. Studenten må begrunne påstanden. Ved å peke på at summen av sannsynlighetene for enkeltutfallene er større enn $1$, ser vi at vi at det ikke kan være en sannsynlighetsmodell.
2. Siden $1.2 = 0.4+0.8 = P(\{u_1,u_3\}) + P(\{u_2,u_3\}) = P(u_1)+P(u_2)+2P(u_3)$, ser vi at hvis $P(u_3)$ er mindre enn $0.2$ så vil $1.2-P(u_3)$ være større enn $1$ samtidig som det vil være lik sannsynligheten for tre enkelutufall i utfallsrommet. Noe som gir en motsigelse.

#### Middels: Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell,  24.04.23

1. La et forsøk ha utfallsrommet $U = { u_1, u_2, u_3, u_4, u_5}$. Hvis $P(\{u_1, u_2, u_3\}) = 0.6$, gi et eksempel på hva $P(\{u_4, u_5\})$ og $P(u_6)$ kan være. Besvarelsen må være begrunnet.

2. La et forsøk ha et utfallsrom $U = { u_1, u_2, u_3, u_4, u_5}$. Forklar at $P(\{u_3\})$ må være større enn $0.4$ hvis $P(\{u_1,u_3\}) = 0.7$ og $P(\{u_2, u,3\}) = 0.7$.  

**Merk** Det var en feil i teksten over der det stod ''Forklar at $P(\{u_3\})$ _ikke kan være_ større enn...''. Dette er rettet i teksten over.

##### Vurderingskriterier

1. Studenten må begrunne påstanden. Her kan de for eksempel bare peke på at $P(U) = 1$ og dermed kan en enkelt bare si at $P(\{u_4, u_5\})$ kan være lik $0.2$, hvis $P(u_6)$ også er lik $0.2$. Dette er fordi en ikke bryter med noen av aksiomene til sannsynlighetsmodeller.
2. Siden $1.4 = 0.7+0.7 = P(\{u_1,u_3\}) + P(\{u_2,u_3\}) = P(u_1)+P(u_2)+2P(u_3)$, ser vi at hvis $P(u_3)$ ikke er større enn $0.4$ så vil $1.4-P(u_3)$ være større enn $1$ samtidig som det vil være lik sannsynligheten for tre enkelutufall i utfallsrommet. Noe som gir en motsigelse.

#### Middels: Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell,  17.04.23

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


#### Middels: Forklare og bruke begrepene utfallsrom, utfall og hendelse og sannsynlighetsmodell,  31.03.23

1. La et forsøk ha utfallsrommet $U = \{ u_1, u_2, u_3\}$. La $P(u_1) = 0.2$, $P(u_2) = 0.2$ og $P(u_3) = 0.5$. Gjør rede for om dette kan være en sannsynlighetsmodell.

2. La et forsøk ha utfallsrommet $U = \{ u_1, u_2, u_3\}$. La $P(u_1) = 0.2$, $P(u_2) = 0.3$. Begrunn hva $P(\{u_1, u_3\})$ må være for at dette skal være en sannsynlighetsmodell.

##### Vurderingskriterier

1. Studenten må bruke at $P(U) = 1$ og at $P(\{u_1,u_2,u_3\}= P(u_1)+P(u_2)+P(u3)$ noe som ikke stemmer.
2. Studenten kan angripe oppgaven på flere måter. For eksempel kan de først vise at $P(u_3) = 0.5$ og deretter bruke at $P(\{u_1,u_3\}) = P(u_1)+P(u_3) = 0.7$.

