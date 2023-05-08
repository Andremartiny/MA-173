
#### Avansert: Forklare, illustrere og bruke komplementsetningen,  Øveppgaver

- Alfa 7.72, 7.74.

##### Løsningsforslag

1. Alfa 7.72
   Hvis vi kaster en mynt fem ganger kan vi for hvert kast få enten kron eller mynt. Dermed vil vi ha $2^5$ forskjellige utfall i forsøket vårt (vi bryr oss om rekkefølge).
   a. Det er kun én måte å få bare kron på. Dermed blir sannsynligheten også $\frac{1}{32}$, siden alle mulige utfall er like sannsynlig og det er $32$ mulige utfall.
   b. Siden det å ikke bare få kron dekker alle andre utfall enn å bare få kron, så må det være $32-1$ mulige utfall som ikke bare gir ikke bare kron. Sannsynligheten blir derfor $\frac{31}{32}$.
   c. Det er på samme måte kun ett utfall som gir bare mynt. Dermed av de totalt $32$ mulighetene så er det $32-2$ som hverken inneholder bare kron eller bare mynt. Sannsynligheten blir derfor $\frac{30}{32}$.


#### Avansert: Forklare, illustrere og bruke komplementsetningen,  08.05

Det er 13 gutter og 12 jenter i en klasse. Det skal trekkes en tilfeldig gruppe på tre fra klassen. Hva er sannsynligheten for at man trekker minst én jente?

##### Vurderingskriterier

Studenten må regne ut sannsynligheten på en forståelig måte. Det kan for eksempel gjøres ved å tenke at alle mulige utvalg er like sannsynlige og at det er et uordnet utvalg uten tilbakelegg. Det gir en uniform sannsynlighetsmodell med \(\frac{25\cdot 24\cdot 23}{3\cdot 2\cdot 1} = 25\cdot 4\cdot 23 = 2300\) mulige utfall. Vi er nå interessert i hendelsen *minst én jente*. Finner vi sannsynligheten for å velge ut *kun* gutter kan vi bruke at dette er komplementærhendelsen til hendelsen vi er ute etter. Siden det er \(\frac{12\cdot 11\cdot 10}{3\cdot 2\cdot 1} ={2\cdot 11\cdot 10} = 220\) mulge utvalg som inneholder kun gutter må sannsynligheten for å trekke minst én jente være \(1 - \frac{220}{2300}\).


#### Avansert: Forklare, illustrere og bruke komplementsetningen,  28.04.23

Poker er et kortspill der man har 52 kort. Det er tretten kort i hver sort (kløver, ruter, spar og hjerter), inkludert ett ess i hver sort. Hva er sannsynligheten for å *ikke* få et par i ess (to ess) på blant de to kortene du trekker?

##### Vurderingskriterier

Studenten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan de peke på at det er $\frac{52\cdot 51}{2}$ mulige hender man kan starte med og alle hendene er like sannsylige. Dermed kan vi finne antall muligheter for å få et par i ess og bruke komplementsetningen. Det kan vi gjøre ved å finne antall hender som inneholder et par i ess. Det kan vi for eksempel løse bare ved å telle. Vi kan ha hjerter-kløver, hjerter-ruter, hjerter-spar, kløver-ruter, kløver-spar, ruter-spar. Dermed er det $26\cdot 51 - 6$ mulige hender som ikke er et par i ess av totalt $26\cdot 51$ mulige hender. Siden alle hendene er like sannsynlige kan vi konkludere med at det er $\frac{26\cdot 51-6}{26\cdot 51} = 1 - \frac{6}{26\cdot 51}$ i sannsynlighet for å ikke få par i ess.

#### Avansert: Forklare, illustrere og bruke komplementsetningen,  24.04.23

Da Henrik var student gikk han i en klasse med 21 studenter. Hver undervisningsøkt deltes de inn i grupper på tre. Henrik hadde fire venner han gjerne ønsket å komme på gruppe med. Hva var synligheten for at Henrik kom på gruppe med minst en av dine venner, når gruppene ble valgt tilfeldig?

##### Vurderingskriterier

Studenten må løse på en måte slik at leseren kan forstå hva som er gjort. For eksempel kan en peke på hvilke to som havner på gruppe med Henrik er like sannsynlig. Det er $\frac{20\cdot 19}{2} = 190$ forskjellige mulige klassekammerater som han kan havne på. For å avgjøre hvor mange av de som inneholder minst én, er det naturlig å se på hvor mange som ikke inneholder noen. Av de 20 resterende klassekammeratene er det 16 som ikke er av de fire vennene Henrik ønsker å komme på gruppe med. Derfor er det $\frac{16\cdot 15}{2} = 8\cdot 15 = 120$ grupper som ikke inneholder noen av Henriks venner. Derfor må det være $180 - 120 = 60$ mulige grupper der Henrik er på gruppe med minst én av sine venner. Sannsynligheten er derfor $\frac{60}{190}=\frac{6}{19}$.

