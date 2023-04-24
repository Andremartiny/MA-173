
#### Avansert: Bruke begrepene i temaet til å løse sammensatte problemet,  Øveppgaver

1. Anta at sannsynligheten for å få en gutt alltid er 1/2. I en familie
    som har to barn er det tre muligheter, to gutter, to jenter eller
    ett av hvert kjønn.
    1. Eleven Per sier at hvis en velger en tilfeldig
    tobarnsfamilie er det 1/3 sjans for at de har to gutter. Avgjør om Per tenker rett. Pek på eventuelle misforståelser eller riktige oppfatninger. Hvis det er noen misforståelser må disse rettes opp slik at Per forstår hva som er feil.
    André og Kristin planlegger å få fem barn.
    2. Hva er sannsynligheten for at de får bare gutter?
    3. Hva er sannsynligheten for at de får to jenter og tre gutter?
    4. Hva er sannsynligheten for at de får minst 2 jenter?
2. I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter,
    ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10
    i tillegg til en knekt, en dame og en konge. Når man spiller bridge
    får man en hånd bestående av 13 tilfeldige kort.
    - Hvor mange av alle de mulige bridgehendene består av nøyaktig åtte
        kløver?
    - Hvor mange ulike bridgehender med nøyaktige fem spar er det
        mulig å dele ut?
    - Hvor mange bridgehender med seks kort i en og samme farge finnes
        det?
    - Hva er sannsynligheten for å få ei slik hånd?
3. Vi trekker ut seks kort av en kortstokk på 52 kort.
    - Hva er sannsynligheten for at det er nøyaktig to spar blant de
        fem?
    - Hva er sannsynligheten for at alle dem fem kortene er kløver?
    - Hva er sannsynligheten for at ruter knekt er med?
    - Hvor stor sannsynlighet er det for at det er to kort med samme
        verdi hånden som deles ut?
4. Vi har et rutenett med $2 \times 5$ ruter. Vi skal først fargelegge
    fire ruter røde og så to gule.
    1. Hvor mange måter kan vi gjøre det på?
    2. Hvordan ville det blitt om vi først velger de to som skal være
        gule, og så de fire som skal være røde?
    3. Hva om vi velger rutene som ikke skal fargelegges, så de fire
        som skal være røde?

##### Løsningsforslag

1. Anta at sannsynligheten for å få en gutt alltid er 1/2. I en familie som har to barn er det tre muligheter, to gutter, to jenter eller ett av hvert kjønn.
   1. Eleven Per sier at hvis en velger en tilfeldig
   tobarnsfamilie er det 1/3 sjans for at de har to gutter. Avgjør om Per tenker rett. Pek på eventuelle misforståelser eller riktige oppfatninger. Hvis det er noen misforståelser må disse rettes opp slik at Per forstår hva som er feil.
   \
   - Problemet med utsagnet til Per er mest sannsynlig at han tenker at alle de tre utfallene han lister opp i er like sannsynlige. Hvis vi tegner et utfallstre vil vi se at vi får grenene $\{gg, gj, jg, jj\}$, altså fire utfall. Siden det er lik sannsynlighet for at hver gren skal "skje" så er de fire utfallene like sannsynlige. Vi kan nå vise Per at det derfor er $\frac{1}{4}$ av tilfellene som gir bare gutter og $\frac{1}{4}$ som gir bare jenter, og at i $50\%$ av tilfellene så får vi gutt og jente.
   \
   André og Kristin planlegger å få fem barn.
   2. Hva er sannsynligheten for at de får bare gutter?
   \
   - Vi kan tenke likt som over og se at det er $2^5$ mulige utfall. Det er kun ett av disse som gir kun gutter, så sannsynligheten blir derfor $\frac{1}{32}$.
   \
   3. Hva er sannsynligheten for at de får to jenter og tre gutter?
   \
   - Siden vi vet at det er kun $32$ mulige utfall, kan vi enten telle antallet som inneholder to gutter og tre jenter. Vi kan også tenke slik. Av de fem barnene så skal jeg velge to av dem som skal være gutter. Det er derfor $\frac{5\cdot 4}{2}$ mulige måter å velge ut to gutter av fem barn. Vi har derfor at det er $10$ muligheter for å få nøyaktig to gutter og tre jenter, som gir en sannsynlighet på $\frac{10}{32}$.
   \
   1. Hva er sannsynligheten for at de får minst 2 jenter?
   \
   Vi vet at det er én måte å få ingen jenter (kun gutter), i tillegg er det mulig å få nøyaktig én jente (førstefødte er jente resten gutter, andrefødte er jente resten gutter osv). Dermed er det $6$ utfall som gir mindre enn $2$ jenter. De gjenværende utfallene må derfor være minst to jenter og sannsynligheten blir derfor $\frac{26}{32}$.
   \
2. I en vanlig kortstokk med 52 kort finnes det fire sorter, hjerter, ruter, kløver og spar. I hver sort er det 13 kort, kortene 1 til 10 i tillegg til en knekt, en dame og en konge. Når man spiller bridge får man en hånd bestående av 13 tilfeldige kort.

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

4. Vi har et rutenett med $2 \times 5$ ruter. Vi skal først fargelegge
    fire ruter røde og så to gule.
   1. Hvor mange måter kan vi gjøre det på?
   - Vi har 10 ruter å velge mellom. Begynner vi med fire ruter i rødt får vi $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}$. Her deler vi på $4\cdot 3\cdot 2\cdot 1$ fordi dette er et uordnet utvalg uten tilbakelegg. Det gjenstår nå 6 ruter vi kan velge til gulfargene. Det gir $\frac{6\cdot 5}{2}$. Multiplikasjonsprinsippet forteller oss nå at det er $\frac{10\cdot 9\cdot 8 \cdot 7}{4\cdot 3\cdot 2\cdot 1}\cdot \frac{6\cdot 5}{2}$ forskjellige måter å fargelegge 4 av de ti rutene røde og så 2 av rutene gule.
   2. Hvordan ville det blitt om vi først velger de to som skal være gule, og så de fire som skal være røde?
   - Logikken blir lik som over, men fremgangen er noe ulik. Altså først $\frac{10\cdot 9}{2}$ og deretter $\frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ og igjen får vi totalt $\frac{10\cdot 9}{2}\cdot \frac{8\cdot 7\cdot 6\cdot 5}{4\cdot 3 \cdot 2 \cdot 1}$ muligheter.
   3. Hva om vi velger rutene som ikke skal fargelegges, så de fire
        som skal være røde?
   - Her får dere regne selv, men egg merke til at dette gir samme svar som de to oppgavene over.


