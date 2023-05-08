
#### Avansert: Bruke begrepene i temaet til å løse sammensatte problemer,  08.05

Studentene i MA-173 holder på med aktiviteter for å undersøke sannsynlighetsmodeller. I en oppgave kastet de to terninger og ganget tallene de fikk, med hverandre. De brukte vanlige spillterninger med tallene 1–6. Henrik kastet terningene flere ganger, og syntes han fikk mistenkelig mange svar som var partall. Han spurte læreren hva grunnen kunne være.

1. Hva ville du som lærer ha svart Henrik?
2. Hva er sannsynligheten for å få partall som svar når vi ganger tallene vi får på terningene, med hverandre?
3. Hvis vi kaster terningene fire ganger, hva er sannsynligheten for å få partall som svar på gangestykket alle gangene?
4. Hva er sannsynligheten for å få partall som svar to ganger og oddetall to ganger?

##### Vurderingskriterier


Studenten må besvare *alle* spørsmålene på en rimelig måte. 

1. Her finnes ingen eksakt fasit, men en besvarelse bør inneholder noe som peker på og *begrunner* hvorfor dette er tilfellet. Det kan for eksempel være ved å lage en tabell som viser de ulike mulige utfallene, som under. 
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/sannsyn/terningkast0805.svg)
I tabellen kan man se at det er 27 av de 36 mulige utfallene som gir et partall. Dette kan også forklares ved at en kun får oddetall ved at begge terningene slår oddetall. Det er kun 3 mulige utfall i begge terningkastene, altså totalt \(9\) forskjellige utfall som gir oddetall. 
2. Svaret bør allerede være argumenter for i oppgave 1. Sannsynligheten er \(\frac{27}{36}= \frac{3}{4}\).
3. Her kan studenten ty til multiplikasjonsprinsippet. Det er \(27\) mulige gunstige utfall i hvert av de fire kastene, dermed \(27^4\) mulige gunstige utfall. Totalt er det \(36^4\) mulige utfall (36 utfall i hvert enkeltkast). Siden alle mulige utfall er like sannsynlige får vi en sannsynlighet på \(\frac{27^4}{36^4}\).
4. Studenten kan for eksempel bruke at dette kan skje på følgende måter \(OOPP\), \(OPOP\), \(OPPO\), \(POOP\), \(POPO\) og \(PPOO\), der \(P\) er partall og \(O\) er oddetall. Hver av disse seks mulige rekkefølgene er like sannsynlige, så vi må bare finne sannsynligheten for hver av de. Vi kan for eksempel ta for oss \(OOPP\) og se at vi er på utkikk etter antall muligheter som gir oddetall, så oddetall, så partall så partall. Vi vet nå at dette betyr at det er \(9\) muligheter, så \(9\), så \(27\) så \(27\). Totalt gir multiplikasjonsprinsippet at det er \(9\cdot 9 \cdot 27\cdot 27\) mulige måter for å først få oddetall, så oddetall så partall så partall. Sannsynligheten for \(OOPP\) blir da \(\frac{9^2\cdot 27^2}{36^4}\). Siden dette også er sannsynligheten for alle mulige utfallene får vi en sannsynlighet for å få nøyaktig to oddetall og to partall ved fire kast lik \(6\cdot \frac{9^2\cdot 27^2}{36^4}\).



#### Avansert: Bruke begrepene i temaet til å løse sammensatte problemer,  28.04.23

Ved kast med to terninger noteres differensen mellom antall øyne på terningene (det største tallet minus det minste tallet). Hvis terningene viser samme antall øyne, er differensen lik 0.

1. List opp eller lag tabell som viser alle mulighetene der differensen blir 0, 1, 2, 3, 4 eller 5.
2. Hva er sannsynligheten for at differensen blir 0? Hva er sannsynligheten
for at differensen blir 1? Forklar.
3. To terninger kastes to ganger. Hva er sannsynligheten for den
sammensatte hendelsen at differensen blir 0 i første kast og at
differansen blir 1 i andre kast? Forklar.
4. To terninger kastes to ganger. Hva er sannsynligheten for at differensen
ikke blir 0 i noen av kastene?

*Vink:* $36\cdot 36 = 1296$.

##### Vurderingskriterier

1. 
$$
\begin{array} {|r|r|r|r|r|r|}\hline  & \text{Første terning} & 1 & 2 & 3 & 4 & 5 & 6
\\
\hline
\text{Andre terning}
\\ \hline  
1 & & 1-1 = 0 & 2-1 = 1 & 3-1 = 2 & 4-1 = 3 & 5-1 =4 & 6-1 = 5
\\ \hline  
2 & & 2-1 = 1& 2-2 = 0 & 3-2 = 1 & 4-2 = 2 & 5-2 = 3 & 6-2 = 4
\\ \hline
3 & & 3-1 =2& 3-2 =1 & 3-3 = 0 & 4-3 = 1 & 5-3 = 2 & 6-3 = 3
\\ \hline
4 & & 4-1 =3 & 4-2 =2 &  4-3 = 1 & 4-4 = 0& 5-4 = 1 & 6-4 = 2
\\ \hline
5 & & 5-1 =4& 5-2 = 3 &  5-3 = 2 & 5-4 =1 & 5-5 = 0 & 6-5 = 1
\\ \hline
6 & & 6-1 =5& 6-2 = 4 &  6-3 =3 & 6-4 =2 & 6-5 =1 & 6-6 = 0
\\ \hline
\end{array}
$$
2. Vi ser at 6 av de 36 mulige utfallene gir 0, så sannsynligheten er $\frac{6}{36} = \frac{1}{6}$. Vi ser videre at det er 10 mulige utfall som gir $1$, eller $\frac{10}{36}$ i sannsynlighet for å få 1. 
3. Vi kan bruke multiplikasjonsprinsippet til å innse at vi har 36 utfall i første kast av to terninger og så 36 i neste. Derfor får vi totalt $1296$ mulige utfall. Vi vet at det i seks av de første kastene så kan vi få 0 i differanse. For hver av de seks mulighetene har vi 10 muligheter for å få 1 i differanse på andre kast. Igjen gir multiplikasjonsprinsippet oss at det må være $6\cdot 10 = 60$ mulige utfall av de $1296$ utfallene som gir 0 på første kast av to terninger og 1 på andre kast av to terninger. Sannsynligheten blir derfor $\frac{60}{1296}$.
4. Det vil være 30 muligheter for å ikke få 0 i første og tilsvarende 30 for å ikke få noen i neste. Dermed får vi en sannsynlighet på $\frac{900}{1296}$.



#### Avansert: Bruke begrepene i temaet til å løse sammensatte problemer,  24.04.23

I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 (ess) til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

- Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte kløver?
- Hvor mange ulike bridgehender med nøyaktige fem spar er det mulig å dele ut?
- Hvor mange bridgehender med seks kort i en og samme farge finnes det?
  - Hva er sannsynligheten for å få ei slik hånd?

Du trenger ikke regne ut verdiene. For eksempel holder det å skrive at et antall er $30\cdot 29\cdot 28$.

##### Vurderingskriterier

**Merk** Det stod opprinnelig ikke *nøyaktig* åtte kløver i oppgaveteksten. Derfor godtas flere tolkninger av første deloppgave. I tillegg er det også presisert *nøyaktig* i tredje deloppgave, men denne kunne også tolkes på flere måter. Det er uansett fremgangsmåten og logikken som tas tak i og utgjør om studenten får godkjent eller ikke.

I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

Vi merker oss først at det er $\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}$ mulige brigdehender man kan ha (vi tenker på dette som et uordnet utvalg uten tilbakelegg, da vi ikke kan ha samme kort på hånden og vi ikke bryr oss om rekkefølgen).

- Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte kløver?
  - Vi ønsker å trekke ut åtte av de tretten kløverne. Dette kan gjøres på $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter. Vi deler på $8\cdot 7 \cdot 6\cdots 3\cdot 2\cdot 1$ fordi vi ikke bryr oss om overtelling, og vi deler derfor dette vekk. Videre må vi nå se på hvor mange måter vi kan trekke ut nøyaktig de fem resterende kortene uten at dette er kløver. Siden det er 13 kort som er kløver er det $39$ kort som ikke er det. Dermed har vi $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$. Vi kan altså for hvert unike utvalg av åtte kløver kombinere dette med $\frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ andre utvalg som ikke er kløver. Totalt får vi altså (fra multiplikasjonsprinsippet) $\frac{13\cdot 12\cdot 11\cdot 10 \cdots 7\cdot 6}{8\cdot 7 \cdots 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36\cdot 35}{5\cdot 4\cdot 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig åtte kløver.
- Hvor mange ulike bridgehender med nøyaktige fem spar er det mulig å dele ut?
  - Tanken her er den samme som i oppgaven over, vi får derfor $\frac{13\cdot 12\cdot 11\cdot 10\cdot 9}{5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdot 37\cdot 36 \cdot 35\cdot 34\cdot 33\cdot 32}{8\cdot 7 \cdots 3\cdot 2\cdot 1}$ mulige måter å trekke ut nøyaktig fem spar.
- Hvor mange bridgehender med nøyaktig seks kort i en og samme farge finnes det?
  - Vi kan først finne antall muligheter for å få seks av samme sort (men allerede nå kan vi merke oss at vi da også teller hender som inneholder for eksempel 6 spar *og* seks ruter). For å få seks hjerter er det $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}$ mulige hender. Siden hjerter ikke var spesielt her, er det generelt $4$ ganger så mange måter å velge ut en sort og få nøyaktig seks av den sorten i en hånd. Problemet nå er at vi overteller noe. Vi overteller alle måter å trekke ut nøyaktig seks av i to sorter. Dette kan gjøres på $6$ måter (hjerter-spar, herter-kløver, hjerter-ruter, spar-kløver, spar-ruter og kløver-ruter). Hver av disse kombinasjonene har $\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26$ ulike hender (vi ganger med $26$ fordi det er 26 gjenværende kort som ikke er i de to sortene vi har valgt). Dermed kan vi ved å bruke addisjonssetningen nå si at det er
  $$
  \begin{aligned}
   4\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   \\
   -6\cdot
   & \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26
  \end{aligned}
  $$
  mulige hender som inneholder nøyaktig seks av en sort.
- Hva er sannsynligheten for å få ei slik hånd?
  - Sannsynligheten blir dermed gunstige over mulige eller
  $$
  \frac{4\cdot
   \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{39\cdot 38\cdots 35\cdot 34\cdot 33}{7\cdot 6\cdot 5\cdot 4\cdot 3 \cdot 2\cdot 1}
   -6\cdot\frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}\cdot \frac{13\cdot 12\cdot 11\cdot 10 \cdot 9 \cdot 8}{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1} \cdot 26}{\frac{52\cdot 51\cdot 50\cdots 42\cdot 41\cdot 40}{13\cdot 12\cdots 3\cdot 2\cdot 1}}
  $$


