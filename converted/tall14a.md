
#### Avansert: Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall,  Øveoppgaver

1. Alle brøkene som svarer til endelige desimaltall, har en felles
   egenskap. Forklar hvilken det er, og gi en begrunnelse for at det er
   slik.

2. Brøkene som ikke svarer til endelige desimaltall, gir periodiske
   desimaltall. Begrunn hvorfor det er slik.

##### Løsningsforslag

1. Alle brøkene som svarer til endelige desimaltall, har en felles
    egenskap. Forklar hvilken det er, og gi en begrunnelse for at det er
    slik. De har til felles at når maksimalt forkorta, er 2 og 5 eneste primfaktorer i nevneren. For at en brøk skal være et endelig desimaltall, må den kunne utvides til 10-, 100- eller 1000- deler og så videre, altså til en brøk med tierpotens til nevner (fordi det er det desimaltall er). Siden 2 og 5 er de eneste primfaktorene i $10^{n}$, kan vi ikke ha andre faktorer i nevner om brøken skal være endelig.

2. Brøkene som ikke svarer til endelige desimaltall, gir periodiske
    desimaltall. Begrunn hvorfor det er slik. Skal vi gjøre om brøker til desimaltall, kan vi dele. For eksempel finner vi 3/7 som desimaltall ved å dele 3 på 7. Når vi gjør dette ved hjelp av divisjonsalgoritmen, deler vi ut så mye vi kan, gjør om resten til neste posisjon (3 enere til 30 tideler for eksempel), og «trekker ned» sifferet som angir hvor mye vi har fra før av den posisjonen. \
    \
    Når vi deler på for eksempel syv, er det bare syv mulige rester vi kan få, nemlig 0, 1, 2, ... og 6. Det betyr at vi før eller siden (innen seks steg, for divisjonen vil jo ikke gå opp på noe tidspunkt) vil få en rest vi har hatt tidligere når vi utfører divisjonsalgoritmen. Og da vil vi nødvendigvis få en gjentakelse av stegene fra første gang vi fikk den resten; vi havner i en «periode-loop».


#### Avansert: Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall,  24.04

1. Begrunn påstanden: En brøk svarer til et endelig desimaltall bare dersom den maksimalt forkorta kun har primfaktorene 2 og 5 i nevner.

2. Begrunn hvorfor resten av brøkene gir periodiske desimaltall.

##### Vurderingskriterier

a.  Må vise til at desimaltall er brøker med tierpotenser til nevner. Siden eneste primfaktorer i 10 er 2 og 5, må den maksimalt forkorta brøken ha nevner uten andre primfaktorer enn disse.
b. Begrunnes ved hjelp av eksempel: Tolke for eksempel 3/7 som divisjonen 3 : 7, og utføre den vanlige algoritmen. Divisjon med 7 kan bare gi restene 0, 1, ..., 6 (i vårt tilfelle ikke 0, for divisjonen går ikke opp). Det gir at høyeste antall mulige steg i divisjonsalgoritmen før vi får en rest vi har hatt tidligere, er seks. Dermed havner vi i en  «periode-loop».

