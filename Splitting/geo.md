<!-- 
PDF:
Kjør i terminal fra markdown mappa pandoc .\quizzer\geometri\geo.md -f markdown -t pdf --pdf-engine=xelatex --variable=block-headings --toc -o .\quizzer\geometri\geo.pdf
HTML:
pandoc .\quizzer\geometri\geo.md -f markdown -t html --mathjax --template=template.html --toc -s -H styling.css -o .\quizzer\geometri\geo.html
-->
# Måling og areal

## Øveoppgaver

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene *størrelse,
    måltall* og *måleenhet.* Besvarelsen må inneholde 1-, 2-dimensjonale
    eksempler.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

1. Vis grunnskoletilpasset (ved hjelp av ordforklaringer og
    illustrasjoner) hvordan man kan avgjøre

    a.  omkretsen av en mangekant, når man vet sidelengdene

    b.  omkretsen av en sirkel, når man vet radiusen

    c.  Arealet av et rektangel, når man kjenner til sidelengdene

    d.  Arealet av et parallellogram, når man kjenner til høyde og
        bredde

    e.  Arealet av et trapes, når man kjenner til lengden to parallelle
        sider og avstanden (høyden) mellom den

    f.  Arealet av en rettvinklet trekant, når man vet lengden på
        katetene

    g.  Arealet av en vilkårlig trekant, når man vet lengde og høyde.

Bruke forklaringene og illustrasjonene til å gi en generell formel (med
hjelp av algebraiske symboler).\
Forklaringene må få fram måleenheten som brukes og hvordan størrelsen
man avgjør er relatert til måleenheten.

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 3-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene *størrelse,
    måltall* og *måleenhet.* Besvarelsen må inneholde 3 dimensjonale
    eksempler.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler (med illustrasjoner) på hva som menes med
    begrepene *punkt, linje, plan, linjestykke,* *vinkel og parallelle
    linjer.*

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Argumentere for vinkelsum av de indre vinklene i en

    a.  trekant

    b.  mangekant

2. Hvis linje *f* og *g* er parallelle. Hva er vinkel *v*?\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image1.png)

##### Løsningsforslag

1. \
   a. Ta utgangspunkt i animasjonen under og kall, blå, rød og grønn vinkel for $x$, $y$ og $z$. Vi ser at spaserturen viser at vi har dreid $360^\circ$ (summen av de ytre vinklene, de gule). Ser vi på indre vinkel pluss ytre vinkel ser vi at denne også alltid er $180^\circ$. Noe som tilsier at summen av indre og yre vinkler er $3\cdot 180^\circ$. Trekker vi fra summen av de ytre vinklene får vi $3\cdot 180^\circ-360^\circ = 180^\circ$.
   b. Forsøk selv, ved å bruke samme argument.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/Visvinkler.mp4){width=75%}

2. Trekk en linje parallell med $f$ og $g$ gjennom vinkel $v$. Vi får da, ved å bruke parallellitetsegenskaper, at $v$ kan deles inn i to vinkler, en del som er $13^\circ$ og en del som er $35^\circ$. Vinkel $v$ er dermed $48^\circ$. *Merk*: Besvarelsen mangler en tegning. Gjør dette selv og forsøk å gjøre din egen besvarelse.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

1. En korde-tangent-vinkel har størrelse *v*. Hvor stor er sirkelbuen
    den skjærer av? (Merk: En tangent står vinkelrett på linjen fra
    sentrum av sirkelen til tangeringspunktet).\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image2.png)

##### Løsningsforslag

1. Vi merker oss først at grønn + rød vinkel er $90^\circ$. Rød vinkel kan beskrives ved hjelp av den grønne vinkelen slik: $\angle ACB = 90 - v$. Vi er på jakt etter den rosa vinkelen $\angle BAC$. Siden 2 røde vinkler + rosa utgjør indre vinkelsum av en trekant får vi
$$
\begin{aligned}
180
&  = 2\text{rød}+ \text{rosa}
\\
180 & = 2(90 - v) + \angle BAC
\\
180 &  = 180 - 2v + \angle BAC
\\
2v & = \angle BAC
\\
v & = \frac{\angle BAC}{2}.
\end{aligned}
$$
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-03-21-15-36.png)

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler (med illustrasjoner) på hva som menes med
    begrepene *mangekant, sirkel.*

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar ved å bruke definisjoner at

    a.  Kvadrat er rektangel,

    b.  rektangel er parallellogram,

    c.  parallellogram er trapes,

    d.  Rektangel er et trapes.

##### Løsningsforslag

1. \
   a. Et kvadrat kan defineres ved at alle indre vinkler er $90^\circ$ og *alle* sider er like lange. Et rektangel kan defineres ved at alle indre vinkler er $90^\circ$. Siden definisjonen av et kvadrat krever at alle vinklene er $90^\circ$, må altså et kvadrat være et rektangel.
   b. Et parallellogram kan defineres ved å si at motstående sider må være parallelle. Siden kravet om at alle indre vinkler i rektangler er $90^\circ$ impliserer at motstående sider må være parallelle, betyr det altså at et rektangel må også være et parallellogram.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler og prismer

1. Gjengi formelen for

    a.  Trekanter

    b.  Rektangler

    c.  Parallellogram

    d.  Prismer

    e.  Pyramider

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Hvis et trapes har areal $A$. Forklar ved hjelp av formelen til et trapes hvorfor arealet til trapeset blir $\frac{25}{4}A$ hvis vi forstørrer lengdene i trapeset med $\frac{5}{2}$.

##### Løsningsforslag

Vi vet at $A = \frac{(a+b)h}{2}$. Skalerer vi opp trapeset og bevarer formen får vi at trapeset har areal $\frac{(\frac{5}{2}a + \frac{5}{2}b)\frac{5}{2}h}{2} = \frac{25}{4}\frac{(a+b)h}{2}=\frac{25}{2}A$.

#### Avansert: Utforske og løse problemer knyttet til geometriske figurer

1. Arkene i A-formatet (A1, A2, A3, A4, A5, osv) har den egenskapen at
    når du halverer de ved å brette de på langsiden, så vil de bevare
    forholdet mellom sidelengdene. Det vil si at hvis sidelengdene i A4
    er *a* og *b,* så er sidelengdene i A5 *b/2* og *a* og forholdet
    mellom sidelengdene vil være like. Vis at dette forholdet, vil være $\sqrt 2$.

2. Hvor stor er summen av de små omkretsene i forhold til den store?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image3.png)

##### Løsningsforslag

1. Vi er ute etter å beskrive forholdet $\frac{b}{a}$. La oss kalle dette for $x$. Videre får vi vite at $\frac{b}{a}= \frac{a}{\frac{b}{2}}$. Nå kan vi regne videre at
$$
\begin{aligned}
\frac{b}{a}
& =
\frac{a}{\frac{b}{2}}
\\
x & = \frac{2a}{2\frac{b}{2}}
\\
& = \frac{2a}{b}
\\
& = \frac{2\frac{a}{a}}{\frac{b}{a}}
\\
& = \frac{2}{x}.
\end{aligned}
$$
Vi ser altså at $x^2 = 2$ eller at $x = \sqrt 2$.

### Bruke begrepet formlikhet av trekanter

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar, gjennom et eksempel, hva som menes med formlike
trekanter.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepet

Under ser du en figur av tre formlike trekanter. Avgjør lengden på de resterende sidene hvis du får vite at:

1. $a = 3$, $b = 6$, $i = 1$ og $g = 4$.
2. $a = 1$, $b = 4$, $i = 2$ og $g = 4$.
3. $a = 2$, $b = 1$, $i = 4$ og $g = 10$.
4. $a = 5$, $b = 2$, $i = 10$ og $g = 6$.
5. $a = 1$, $b = 2$, $f = 2$ og $e = 3$.
6. $a = \frac{1}{2}$, $b = \frac{1}{3}$, $f = \frac{3}{2}$ og $e = 3$.
7. $a = \frac{3}{5}$, $b = 4$, $f = \frac{9}{10}$ og $e = 3$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-14-23-27.png)

##### Løsningsforslag

1. Vi ser at $a$ samsvarer med $d$ og $g$, at $b$ samsvarer med $e$ og $h$ og at $c$ samsvarer med $f$ og $h$. For å skalere $a = 3$ til $g = 4$, må vi skalere med $\frac{4}{3}$. Dermed må $b = 6$ skaleres til $6\cdot \frac{4}{3} = 8 = h$. For å gå fra $i$ til $c$ må vi skalere ned med $\frac{3}{4}$. Det gir at $c = 1 \cdot \frac{3}{4} = \frac{3}{4}$.

### Argumentere visuelt for Pytagoras setning

#### Grunnleggende: Gjengi og forklar Pytagoras setning

Gjengi og forklar Pytagoras setning. Forklaringen må referere til en
figur.

##### Løsningsforslag

Pytagoras setning sier at for enhver rettvinklet trekant, så gjelder at $a^2+b^2= c^2$, der $a$ og $b$ er katetene og $c$ er hypotenusen. *Merk* at dere må legge ved en figur som dere referer til også!

#### Middels: Gi et visuelt argument for at Pytagoras setning gjelder

Gi et grunnskoletilpasset bevis for Pytagoras setning med et visuelt argument.

##### Løsningsforslag

Se for eksempel Alfa.

### Bruke Pytagoras setning

#### Grunnleggende: Bruke Pytagoras setning til å løse enkle problemer

1. Finn lengden på hypotenusen i en rettvinklet trekant når du vet at
    katetene har lengde:

    a.  3 og 4

    b.  6 og 8

    c.  9 og 12

    d.  8 og 15

    e.  1 og 1

    f.  2 og 4

    g.  1 og 5

    h.  2 og 5

    i.  $\sqrt{8}$ og $\sqrt{8}$

2. Gitt en rettvinklet trekant. Finn lengden på den resterende siden
    når du vet at hypotenus og katet har lengde

    a.  4 og 5

    b.  6 og 10

    c.  5 og $6$

    d.  5 og $\sqrt{41}$

    e.  $\sqrt{11}$ og $\sqrt{27}$

**Merk:** Utregningene skal ikke være avrundet og skal gis i eksakte
verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$,
så skal ikke dette rundes av til $2,236$

##### Løsningsforslag

1. \
   a. Vi får at $3^2 + 4^2 = 25 = c^2$. Dermed er $c = 5$
   b. Vi får at $6^2+8^2 = 100 = c^2$. Dermed er $c = 10$.
   c. Vi får at $9^2 + 12^2 = 225 = c^2$. Dermed er $c = 15$.
   d.  Vi får at $8^2 +15^2 = 64+225 = 289 = c^2$. Dermed er $c = \sqrt 289$.\
   $\vdots$

#### Middels: Bruke Pytagoras setning til å løse problemer

1. Under er det tegnet inn en rettvinklet trekant plassert. På katetene og hypotenusen er det også tegnet inn halvsirkler.

   a. Avgjør arealet av det hvite området.
   b. Hva er forholdet mellom arealet av det hvite området og arealet av trekanten?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image4.png)

2. Under er et rektangel der det er lagt inn en rettvinklet trekant der hypotenusen deles med grunnlinjen til rektangelet. Denne rettvinklede trekanten deler rektangelet inn i tre rettvinklede trekanter. Hvis den minste trekanten har sidelengder 25 og 60. Hva er de resterende sidelengdene i figuren?\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image5.png)\

**Bonus:** Figuren er konstruert med utgangspunkt i den Pytagoreiske trippelen $5^{2} + 12^{2} = 13^{2}$. Velg en annen Pytagoreisk trippel og lag en tilsvarende figur.

##### Løsningsforslag

1. La oss kalle sidene i den rettvinkla trekanten for $x$, $y$ og $z$, slik at $x^2 + y^2 = z^2$. Da vet vi at de tre halvsirklene har areal $\pi(\frac{x}{2})^2 = \pi \frac{x^2}{4}$, $\pi \frac{y^2}{4}$ and $\pi \frac{z^2}{4}$. I tillegg har trekanten areal $\frac{2x\cdot2y}{2} = 2xy$. Tar vi de to små halvsirklene i tillegg til trekanten får vi hele området. Dette har areal $\frac{\pi}{2}(x^2+y^2)+ 2ab$. Vi kan nå bruke Pytagoras setning til å si at dette arealet kan skrives som $\frac{\pi c^2}{4} + 2ab$.Nå gjenstår det bare å trekke fra den store halvsirkelen for å få arealet av det hvite området. Dette gir $\frac{\pi c^2}{4}+ 2ab - \frac{\pi c^2}{4} = 2ab$. Vi ser dermed at det hvite området har samme areal som trekanten. Dermed blir forholdet mellom det hvite området og arealet av trekanten $1$.

## 28.04.23

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 1- og 2-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f17g1}

Besvarelsen må gi eksempler i både en og to dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

Velg passende måleenheter. Vis med ordforklaringer og illustrasjoner, uten å begrunne ved hjelp av de kjente formlene, hvordan man kan avgjøre

a. arealet av et trekant, når man kjenner til høyde og bredde

b. arealet av en sirkel, når man vet radius.

Bruk forklaringene og illustrasjonene til å vise hva de generelle formlene må være.

##### Vurderingskriterier: Middels {#f17m1}

Besvarelsen må gi en forståelig forklaring (og illustrasjon) for hvordan man avgjør størrelsene. For omkrets må en få fram måleenheten en bruker (typisk et linjestykke. Ofte cm, meter og lignende). For areal må det komme tydelig fram hvordan arealet henger sammen med måleenheten kvadrat (noe som i de aller fleste tilfeller betyr at en må vise en omforming til et rektangel, et halvt rektangel eller liknende). Begrunnelsene trekke ut ideen fra forklaringen og gi en generell formel for de tre størrelsene.  

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter  i 3-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 3-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f17g2}

Besvarelsen må gi eksempler i både tre dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

##### Vurderingskriterier: Grunnleggende {#f13g3}

Studenten må gi en forklaring med en illustrasjon på de gitte begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Hvis linje *f* og *g* er parallelle. Hva er vinkel *v*?\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image1.png)

##### Vurderingskriterier: Middels {#f13m3}

Se øveoppgaver oppgave 2. 

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

En korde-tangent-vinkel har størrelse *v*. Hvor stor er sirkelbuen
    den skjærer av? (Merk: En tangent står vinkelrett på linjen fra
    sentrum av sirkelen til tangeringspunktet).\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image2.png)

##### Vurderingskriterier: Avansert {#f13a3}

Se øveoppgavene

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene sirkel, kvadrat og trapes.

##### Vurderingskriterier

Studenten må gi forklaringer og illustrasjoner til begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, et parallellogram er et trapes.
2. Se på følgende påstand "Hvis jeg vet alle vinklene i en trekant, og én av sidelengdene, så kan jeg konstruere trekanten". Avgjør om påstanden er sann eller ikke

##### Vurderingskriterier

1. Studenten må peke på at et parallellogram alltid er et trapes. Dette er fordi *begge* motstående sider i et parallellogram er parallelle. En firkant er et trapes dersom *minst* én par av motstående sider er parallelle. Dermed må alle parallellogram være trapes. (Hvis studenten følger Alfa sin utdaterte definisjon om at trapes har nøyaktig ett par parallelle sider, så vil påstanden være falsk og studenten kan også argumentere for dette med denne definisjonen)
2. Studenten kan argumentere for at dette stemmer ved å tegne en linje som er like lang som siden vi kjenner og deretter tegne på de to vinklene vi kjenner til. Drar vi ut strålene fra disse vinklene kan vi nå se at de krysser i ett punkt. Dette punktet er det manglende hjørnet, og vi har konstruert trekanten.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Trekanter

b. Trapes

c. Prismer

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

##### Vurderingskriterier: Grunnleggende {#f10g5}

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Du har en sirkel med radius $r$. Hvis radius økes med $x$. Vis algebraisk hvor mye lengre omkretsen til den nye sirkelen har blitt.

##### Vurderingskriterier: Middels {#f10m5}

Dette må gjøres algebraisk.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en figur som er laget av sirkelsektorer og trekanter. Figuren er lagd ved å dele sirkelen med sentrum i \(A\) inn i seks like deler \(B\), \(C\), \(D\), \(E\), \(F\) og \(G\).  Sirkelen har radius \(r\).

a. Avgjør og begrunn hva omkretsen av figuren er

I en likesidet trekant er høyden i trekanten alltid \(\frac{\sqrt 3}{2}\) ganger så liten som sidelengdene i trekanten.
b. Avgjør arealet av figuren er.


Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er \(\sqrt{1^{2} + 2^{2}} = \sqrt{5}\), så skal ikke dette rundes av til \(2,236\). Inneholder svaret \(\pi\) skal dette heller ikke avrundes til \(3.14\)!

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-25-13-59-55.png)

##### Vurderingskriterier: Avansert 

Studenten må løse begge oppgavene.
a. Her ser vi at vi har tre sirkelbuer som hver utgjør en seksdel av en sirkel. vi har altså en lengde på en halv sirkel med radius $r$. Det gir en $\frac{2\pi r}{2}= r\pi$. I tillegg har vi tre sidelengder som er like radiusen (siden det er likesidede trekanter). Dermed har vi en total omkrets på $3r + r\pi$. 
b. Vi får vite at høyden er $\frac{\sqrt 3}{2}r$. Fra a. har vi tre trekantener med høyde $\frac{\sqrt 3}{2}r$ og grunnlinje $r$. Det gir et areal på $\frac{1}{2}\frac{\sqrt 3}{2}r^2$. I tillegg har vi en halvsirkel (argumentert for på samme måte som i a), som har et areal på $\frac{\pi r^2}{2}$. Setter vi sammen disse arealene ser vi at det totale arealet avgrenset av figuren er $\frac{(2\pi + \sqrt 3)r^2}{4}$. 

### Bruke begrepet formlikhet av trekanter

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepet

*Merk* I oppgaven stod det opprinnelig feil med at $AF = \frac{12}{9}$. Dette er rettet opp i, men har studenten brukt dette i beregningene får de fortsatt godkjent så lenge de har regnet på en meningsfull måte.

På figuren under ser du en trekant $ABC$ med sidelengder $3$, $4$ og $5$. Inne i trekanten er det satt et kvadrat med sidelengde $\frac{12}{7}$, som gir $DC = \frac{16}{7}$ og $AF = \frac{9}{7}$. Kvadratet skaper også to nye trekanter $AFE$ og $EDC$. Alle trekantene er formlike. 

Bruk informasjonen til å avgjøre lengdene $AE$ og $EC$ (vink: Det kan være lurt å tegne trekantene hver for seg)

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-26-13-00-01.png)

##### Vurderingskriterier

1. Studenten må bruke formlikhet for å avgjøre lengdene. Ved å for eksempel tegne trekantene opp hver for seg kan vi se at for å skalere $ABC$ ned til $EDC$ så forminskes $4$ til $\frac{16}{7}$. Det vil si at forholdstallet må være $\frac{4}{7}$ fordi $4\cdot \frac{4}{7} = \frac{16}{7}$. Dermed må hypotenusen $5$ forminskes til $5\cdot \frac{4}{7} = \frac{20}{7}$. Tilsvarende kan studenten finne forholdstallet til $AFE$ ved å se at forholdstallet er $\frac{\frac{9}{7}}{3} = \frac{9}{7\cdot 3} = \frac{3}{7}$. Dermed blir hypotenusen i $AFE$ lik $5\cdot \frac{3}{7} = \frac{15}{7}$.

### Argumentere visuelt for Pytagoras setning

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar Pytagoras setning. Forklaringen må referere til en figur.

##### Vurderingskriterier

Studenten må gi en forklaring av Pytagoras setning ved å referere til en figur.

#### Middels: Gi et visuelt argument for at Pytagoras setning gjelder

Gi et grunnskoletilpasset argument for Pytagoras setning.

##### Vurderingskriterier

Studenten må gi et grunnskoletilpasset argument for at Pytagoras setning gjelder. Dette innebærer å tegne en eller flere figurer og bruke de til å argumentere for Pytagoras setning.

### Bruke Pytagoras setning

#### Grunnleggende: Bruke Pytagoras setning til å løse enkle problemer

Finn lengden på hypotenusen i en rettvinklet trekant når du vet at katetene har lengde:

a.  1 og 1
b.  3 og 4

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er \(\sqrt{1^{2} + 2^{2}} = \sqrt{5}\), så skal ikke dette rundes av til \(2,236\).

##### Vurderingskriterier

a. Studenten må bruke Pytagoras setninging. For eksempel kan de peke på at vi vet at $1^2 + 1^2 = h^2$, som betyr at $h = \sqrt{2}$.
b. Vi ser tilsvarende at $3^2+4^2 = 9+16 = 25 = h^2$, som betyr at $h = 5$. 

#### Middels: Bruke Pytagoras setning til å løse problemer

Øveoppgave oppgave 1.

##### Vurderingskriterier

Se øveoppgaver oppgave 1.

## 24.04.23

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

##### Vurderingskriterier: Grunnleggende {#f13g3}

Studenten må gi en forklaring med en illustrasjon på de gitte begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Argumenter for hvor stor vinkelsummen av de indre vinklene i en trekant er.

##### Vurderingskriterier: Middels {#f13m3}

Studentene må argumentere for hvor stor vinkelsummen av de indre vinklene i en trekant er.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en trekant $ABC$, der $\angle ACB$ er halvert og går gjennom punktet $E$ (det vil si at $a = c$). Linjen som går gjennom $BD$ er parallell med linjen gjennom $AC$.

1. Forklar at $a = b$ og $d = e$.

2. Forklar hvorfor $\triangle AEC$  er formlik med $\triangle EDB$ ved å begrunne at de indre vinklene i trekantene er de samme.

Når to trekanter er formlike gjelder det at de samsvarende sidene er har samme forhold. Det vil si $\frac{AC}{BD} = \frac{AE}{EB}$.

3. Forklar hvorfor $\frac{AC}{BC} = \frac{AE}{EB}$ (vink: trekanter med to like vinkler er likebeinte).

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-16-49.png)

##### Vurderingskriterier: Avansert {#f13a3}

Studentene må gjøre alle oppgavene.

1. Det må pekes på at $c = a$. Siden $BD$ er parallell med $AC$, så vil $c = b$ (dette kan pekes på ved å forlenge $BD$ og $CD$ og lage toppvinklene) som igjen betyr at $a = b$. At $d = e$ følger igjen av at linjene $BD$ og $AC$ er parallelle.
2. Her må studenten bare bruke informasjonen fra 1. sammen med at vinkelsummen i trekanter er $180$ grader.
3. Siden $a = b$ må $CB = BD$ (fordi det er en likebeint trekant fra 1.). Nå følger resultatet bare ved direkte bruk av formlikhet.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene likesidet trekant, sirkel, kvadrat og parallellogram.

##### Vurderingskriterier

Studenten må gi forklaringer og illustrasjoner til begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, et parallellogram er et kvadrat.
2. Avgjør og begrunn om følgende påstand er sann: Hvis en trekant er likebeint, så er den ene sidelengen lenger enn de to andre .

##### Vurderingskriterier

1. Studenten må peke på at et parallellogram ikke alltid er et kvadrat. Dette gjøres enklest ved å tegne et eksempel av et *skjevt* parallellogram eller et rektangel.
2. Studenten kan for eksempel tegne en likebeint trekant der den ene siden er mindre enn de to andre for å motbevise påstanden.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Trekanter

b. Trapes

c. Prismer

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

##### Vurderingskriterier: Grunnleggende {#f10g5}

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Du har en sirkel med radius $r$. Hvis radius økes med $x$. Vis algebraisk hvor mye lengre omkretsen til den nye sirkelen har blitt.

##### Vurderingskriterier: Middels {#f10m5}

Dette må gjøres algebraisk.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under er et rektangel med høyde $h$ som består av en blå rettvinklet trekant, en grønn rettvinklet trekant der lengden på grunnlinjen er $x$, og et trapes der de parallelle sidene har lengde $a$ og $b$ som markert på figuren.

1. Uttrykk lengden fra punkt $L$ til $I$ ved hjelp av $a$, $b$ og $x$.

2. Avgjør arealet $A$ av rektangelet.

3. Avgjør arealet $B$ til den blå trekanten og arealet $C$ til den grønne trekanten.

4. Begrunn at arealet av trapeset må være $\frac{(a+b)h}{2}$, ved å bruke arealene du fant i oppgave 2 og 3.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-22-14.png)

##### Vurderingskriterier: Avansert {#f10a5}

Studenten må gjøre alle oppgavene for å få godkjent.

1. Studenten må få fram at $LI = a+x-b$.
2. Studenten må peke på at $A = (a+x)h$.
3. Studenten må få fram at $B = \frac{(a+x-b)h}{2}$ og at $C = \frac{xh}{2}$.
4. Studenten må få fram arealet. Det vil være naturlig å regne seg fram ved å se på $A-B-C$.
$$
\begin{aligned}
A-B-C & = (a+x-b)h-\frac{(a+x-b)h}{2} - \frac{xh}{2}
\\
& = (a+x-b)h - \frac{(a-b+2x)h}{2} = \frac{(a+b) h}{2}.
\end{aligned}
$$

*Merk* at det bevisst er utelatt litt detaljer i regningen som bør være med.

### Bruke begrepet formlikhet av trekanter

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepet

Da det var jul hadde André kjøpt et høyt juletre som han fint hadde pyntet med en julestjerne på toppen. André mente det ville være morsomt for sin samboer å beregne høyden på treet ved å bruke formlikhet (men det syns ikke hun). Derfor ba han henne legge seg legge seg ned på gulvet slik at hun akkurat kunne se toppen av stjernen bak toppen av hodet til André . Da lå hun 3 meter unna André og 5 meter unna treet (se figur). André er $\frac{7}{4}$ meter høy. Bruk formlikhet til å avgjøre hvor høyt treet var, når en inkluderer stjernen på toppen.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/juletre.png)

##### Vurderingskriterier

1. Studenten må bruke formlikhet for å avgjøre høyden på treet. For eksempel kan de at den store trekanten er $\frac{5}{3}$ ganger så stor som den lille. Dermed må høyden til André skaleres opp med $\frac{5}{3}$. Det gir en høyde på $\frac{7}{4}\cdot \frac{5}{3} = \frac{35}{12}$. Dermed var treet $\frac{35}{12}$ meter eller $1/2$ meter unna å være tre meter høyt.

### Argumentere visuelt for Pytagoras setning

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar Pytagoras setning. Forklaringen må referere til en figur.

##### Vurderingskriterier

Studenten må gi en forklaring av Pytagoras setning ved å referere til en figur.

#### Middels: Gi et visuelt argument for at Pytagoras setning gjelder

Gi et grunnskoletilpasset argument for Pytagoras setning.

##### Vurderingskriterier

Studenten må gi et grunnskoletilpasset argument for at Pytagoras setning gjelder. Dette innebærer å tegne en eller flere figurer og bruke de til å argumentere for Pytagoras setning.

### Bruke Pytagoras setning

#### Grunnleggende: Bruke Pytagoras setning til å løse enkle problemer

Finn lengden på hypotenusen i en rettvinklet trekant når du vet at katetene har lengde:

a.  5 og 6
b.  3 og 11

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$, så skal ikke dette rundes av til $2,236$.

##### Vurderingskriterier

a. Studenten må bruke Pytagoras setninging. For eksempel kan de peke på at vi vet at $5^2 + 6^2 = h^2$, som betyr at $h = \sqrt{25+36} = \sqrt{61}$.
b. Vi ser tilsvarende at $3^2+11^2 = 9+121 = 130 = h^2$, som betyr at $h = \sqrt 130$.

#### Middels: Bruke Pytagoras setning til å løse problemer

På figuren under ser du et rektangel med sidelengder $\sqrt 2$ og $x$. Rektangelet er rotert $45^\circ$ og plassert i et kvadrat med sidelengde $DC = \sqrt 8 +1$. Avgjør hva $x$ er.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-15-21-11.png)

##### Vurderingskriterier

Studenten må løse for $x$. Siden rektangelet er rotert $45^\circ$ får vi en rettvinklet likebeint trekant med hypotenus lik $\sqrt 2$. Pytagoras gir nå at $a^2 + a^2 = 2$ eller at $a^2 = 1$ som betyr at $a = 1$, der $a$ er lengden $DG$. Det betyr at $GC = \sqrt 8$. Igjen er trekanten $GCF$ likebeint og rettvinklet som gir at $GC ^2 + CF^2 = x^2$ og siden $GC = CF$ får vi at $2(\sqrt 8) ^2 = x ^2$, eller at $16 = x^2$ som betyr at $x = 4$.  

## 17.04.23

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

##### Vurderingskriterier

Studenten må gi riktige forklaringer, med illsutrasjoner, av begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Argumenter for at vinkelsummen i sekskanter er $720^\circ$. Merk: hvis du bruker at vinkelsummen i trekanter er $180^\circ$ må du argumentere for dette også.

##### Vurderingskriterier

Studenten må argumentere for vinkelsummen. Dette kan for eksempel være *spasertur*argumentet eller ved å dele inn i mindre trekanter. Sistnevnte argument må da også inkludere et argument for hvorfor trekanter har vinkelsum $180^\circ$.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en firkant $ABCD$ der $\angle BAC$ er $90^\circ$, og $\angle BCD = 30^\circ$. Avgjør hva summen av de lilla vinklene er, det vil si, avgjør $\angle CBA + \angle ADC$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-12-15-47-28.png)

##### Vurderingskriterier

Studenten argumentere for summen av vinklene på en logisk og strukturert måte. Dette kan nok gjøres på flere måter. En mulighet kan være at studenten bruker at vinkelsummen i en fikant er $360^\circ$. Da kan man videre utnytte at siden $\angle BAC = 90^\circ$ så må $\angle DAB$ være $270^\circ$, siden vinklene utgjør en hel sirkel. Vi vet derfor at de indre vinklene i firkanten er $270^\circ + 30^\circ + \angle CBA + \angle ADC$. Det gir at summen av de lilla vinklene må være $60^\circ$.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene likesidet trekant, sirkel, kvadrat og parallellogram.

##### Vurderingskriterier

Studenten må gi forklaringer og illustrasjoner til begrepene.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, et parallellogram er et kvadrat.
2. Avgjør og begrunn om følgende påstand er sann: Hvis en trekant er likebeint, så er den ene sidelengen lenger enn de to andre .

##### Vurderingskriterier

1. Studenten må peke på at et parallellogram ikke alltid er et kvadrat. Dette gjøres enklest ved å tegne et eksempel av et *skjevt* parallellogram eller et rektangel.
2. Studenten kan for eksempel tegne en likebeint trekant der den ene siden er mindre enn de to andre for å motbevise påstanden.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Rektangler

b. Sirkler

c. Trapes

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Under ser du en illustrasjon av en iskrem som André spiste på fiskebrygga. Figuren er tegnet på et rutenett og består av en halvsirkel og en likebeint trekant. Enhetene i rutenettet måles i centimeter. Hvor stort areal fyller figuren på rutenettet?

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$, så skal ikke dette rundes av til $2,236$. Inneholder svaret $\pi$ skal dette heller ikke avrundes til $3.14$!

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-13-14-16-07.png)

##### Vurderingskriterier

Studenten må bruke at rutene i nettet er målt i centimeter. Halvsirkelen har derfor en radius på $2$cm (eventuelt $10$cm hvis de teller de små kvadratene som cm). Halvsirkelen har et areal på $\pi 2^2 = 4\pi$. Trekanten har også en grunnlinje på $4$cm og høyde på $5cm$. Det gir et areal på $\frac{4\cdot 5}{2} = 10$. Dermed fyller figuren $4\pi + 10$cm.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en løpebane konstruert ved hjelp av rutenett bestående av likesidede trekanter med sidelengde 10m. Selve banen er konstruert ved hjelp av kun halvsirkler.

1. Avgjør hvor lang banen er.
2. Avgjør hvor stort areal banen avgrenser.

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$, så skal ikke dette rundes av til $2,236$. Inneholder svaret $\pi$ skal dette heller ikke avrundes til $3.14$!

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-13-14-21-59.png)

##### Vurderingskriterier

1. Studenten må bryte ned figuren i relevante sirkelbuer. Det er to halvsirkler med lik radius, $20$m. Altså en sirkel med omkrets på $40\cdot \pi$. Videre er det to sirkelbuer som er en sjettedel av en sirkel ($60^\circ$), én med en radius på $20$m og én med radius $60$m. Disse buelengdene har dermed lenge $\frac{1}{6}(40\pi + 120\pi) = \frac{160\pi}{6}$. Totalt må løpebanen derfor være $40\pi + \frac{160\pi}{6}$.
2. Studenten må bryte ned figuren. Hvis de har brutt den ned som i forrige oppgave, kan dette brukes videre. De to halvsirklene avgrenser en del av området som banen avgrenser. Til sammen avgrenser de $\pi\cdot  20^2 = 400 \pi$. Videre avgrensenser den store sirkelbuen en sjettedel av en sirkel med radius $60$, dermed avgrensen den et areal på $\frac{1}{6}\pi 60^2 = 600 \pi$. Dette arealet inkluderer derimot et område utenfor banen. Dette kan vi løse ved å trekke vekk arealet den lille sirkelbuen avgrenser. Dermed ser vi at svaret bør være $400\pi + 600\pi - \frac{1}{6}\pi 20^2 = 1000 \pi- \frac{400 \pi}{6}$.

### Bruke begrepet formlikhet av trekanter

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepet

Under ser du to formlike trekanter. Avgjør lengden på de resterende sidene hvis du får vite at:

1. $c = 2$, $b = 5$, $f = 6$ og $d = 4$.
2. $a = \frac{1} {3}$, $b = 4$, $d= \frac{3}{2}$ og $f = 9$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-14-43-14.png)

##### Vurderingskriterier

1. Studenten må bruke at $c$ og $f$ samsvarer. Dermed ser vi at forholdet mellom trekantene er $3$. Dermed må $b = 5$ bety at $e = 3\cdot 5 = 15$. I tillegg må $d = 4$ bety at $a = \frac{4}{3}$.
2. Siden $a$ og $d$ samsvarer må forholdet være $\displaystyle\frac{\frac{1}{3}}{\frac{3}{2}} = \frac{\frac{1}{3}\frac{2}{3}}{\frac{3}{2}\frac{2}{3}} = \frac{2}{9}$. Dette forteller oss at $d$ må forstørres med $\frac{2}{9}$ for å få størrelsen $\frac{1}{3}$. Eller motsatt må $a$ skaleres med $\frac{9}{2}$ for å få $d$. Vi bruker dette til å innse at $b = 4$ betyr at $e = \frac{9}{2}\cdot 4 = 18$. Videre må $f = 9$ bety at $c = \frac{2}{9} = 2$.

### Argumentere visuelt for Pytagoras setning

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar Pytagoras setning. Forklaringen må referere til en figur.

##### Vurderingskriterier

Studenten må gi en forklaring av Pytagoras setning ved å referere til en figur.

#### Middels: Gi et visuelt argument for at Pytagoras setning gjelder

Gi et grunnskoletilpasset argument for Pytagoras setning.

##### Vurderingskriterier

Studenten må gi et grunnskoletilpasset argument for at Pytagoras setning gjelder. Dette innebærer å tegne en eller flere figurer og bruke de til å argumentere for Pytagoras setning.

### Bruke Pytagoras setning

#### Grunnleggende: Bruke Pytagoras setning til å løse enkle problemer

Finn lengden på den ukjente kateten i en rettvinklet trekant når du vet at:
a.  hypotenusen er 10 og en katet har lengde 8
b.  den ene kateten har lengde 5 og hypotenusen har lengde 10.

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$, så skal ikke dette rundes av til $2,236$.

##### Vurderingskriterier

    a. Studenten må bruke Pytagoras setninging. For eksempel kan de peke på at vi vet at $8^2 + k^2 = 10^2$. Trekker vi fra $8^2$ på begge sider, ser vi at $k^2 = 100-64 = 36$. Dermed må $k = 6$.
    b. På samme måte som i $a$ kan vi se at $5^2 + k^2 = 10^2$. Det gir dermed at $k^2 = 100-25$, så $k = \sqrt 75$ (som kan forenkles til $5\sqrt 3$, men dette er ikke nødvendig).

#### Middels: Bruke Pytagoras setning til å løse problemer

På figuren under ser du  et parallellogram med sidelengder $x$ og $y$. Trekanten $EFH$ er rettvinklet og har sidelengder $FH = a$ og $HE = b$.

1. Forklar hvorfor $GE^2 = (x+a)^2 + b^2$ og hvorfor $DF^2 = (x-a)^2 + b^2$.

2. Argumenter for hvorfor $GE^2 + DF^2 = 2x^2 + 2y^2$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-13-15-05-06.png)

##### Vurderingskriterier

1. Studenten trenger kun å peke på at $GH = x+a$ og så følger resultatet fra Pytagoras setning. Ved å trekke en normal ned fra $F$ til $DE$, kan en raskt innse at $DF^2 = (x-a)^2+b^2$ på samme måte som man gjorde med $GH$.
2. Studenten må regne seg frem og konkludere med påstanden på en forståelig måte. For eksempel kan de begynne med å peke på at $GE^2 = (x+a)^2 + b^2 =x^2+2xa +a^2+b^2$ og at $DF^2 = x^2 -2xa+a^2+b^2$. Legger vi nå sammen $GE^2+DF^2$ får vi $2x^2 +2(a^2+b^2)$. Skal påstanden stemme må $a^2+b^2 = y^2$, men dette ser vi at stemmer ved å bruke at $FHG$ er rettvinklet med sidelengder $a$, $b$ og $y$.

## 31.03.23

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 1- og 2-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f17g1}

Besvarelsen må gi eksempler i både en og to dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

Velg passende måleenheter. Vis med ordforklaringer og illustrasjoner, uten å begrunne ved hjelp av de kjente formlene, hvordan man kan avgjøre

a. arealet av et trekant, når man kjenner til høyde og bredde

b. arealet av en trapes, når man vet lengdene av to parallelle sider i trapeset.

Bruk forklaringene og illustrasjonene til å vise hva de generelle formlene må være.

##### Vurderingskriterier: Middels {#f17m1}

Besvarelsen må gi en forståelig forklaring (og illustrasjon) for hvordan man avgjør størrelsene. For omkrets må en få fram måleenheten en bruker (typisk et linjestykke. Ofte cm, meter og lignende). For areal må det komme tydelig fram hvordan arealet henger sammen med måleenheten kvadrat (noe som i de aller fleste tilfeller betyr at en må vise en omforming til et rektangel, et halvt rektangel eller liknende). Begrunnelsene trekke ut ideen fra forklaringen og gi en generell formel for de tre størrelsene.  

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter  i 3-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 3-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f17g2}

Besvarelsen må gi eksempler i både tre dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

 Argumenter for at vinkelsummen i firkanter er $360^\circ$. Merk: hvis du bruker at vinkelsummen i trekanter er $180^\circ$ må du argumentere for dette også.

##### Vurderingskriterier

Studenten må argumentere for vinkelsummen i en firkant. Dette kan for eksempel gjøres med teknikken der man "spaserer" rundt firkanten. Det går også å dele firkanten i to trekanter og peke på at det derfor må være $180\cdot 2$. I dette tilfellet *må* studenten videre argumentere for hvorfor vinkelsummen i trekanter er $180^\circ$.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en firkant der midtpunktene $E$, $F$, $G$ og $H$ er markert.

Under står det en sann påstand. Bruk påstanden til å vise at $EF$ er parallell med $HG$, og at linjen $EH$ er parallell med linjen $FG$.

Påstand: La $ABC$ være en vilkårlig trekant. Hvis $I$ og $M$ er midtpunktene på $AC$ og $BC$, så vil linjen $IM$ være parallell med $AB$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-14-26-10.png)

##### Vurderingskriterier

Studenten må gi en forståelig forklaring. Siden påstanden de skal bruke peker på trekanter er det naturlig at studenten trekker diagonalen i firkanten. Dermed kan de nå bruke at $E$, $F$, $G$, og $H$ alle er midtpunkter til å peke på at for eksempel $EF$ og $HG$ er parallell med samme diagonal, noe som betyr at de også må være parallelle. Tilsvarende kan de argumentere for $EH$ og $FG$.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene likesidet trekant, sirkel, rektangel og trapes.

##### Vurderingskriterier

Studenten må gi eksempler med illustrasjoner på begrepene som det best om.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, en likesidet trekant er en likebeint trekant.

2. Avgjør og begrunn om følgende påstand om en trekant stemmer: En firkant der diagonalene er like lange og skjærer hverandre på midten er et kvadrat.

##### Vurderingskriterier

1. Studenten må forklare hvorfor en likesidet trekant må være likebeint også. Dette må gjøres ved å peke på hva det vil si å være likesidet og hva det vil si å være likebeint.
2. Studenten må gi et moteksempel på argumentet for å vise at påstanden ikke stemmer.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Rektangler

b. Sirkler

c. Trapes

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

##### Vurderingskriterier

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Avgjør og begrunn om følgende påstand stemmer.

Et rektangel har sidelengder $x$ cm og $y$ cm og du øker begge lengdene med $3$ cm. Da blir det nye arealet $3\cdot 3$ cm$^2= 9$ cm$^2$ større.

##### Vurderingskriterier

Studenten gi et tilfedsstillenge argument for at påstanden ikke stemmer. Det kan for eksempel gjøres med et eksempel. Hvis rektangelet er $2\cdot 3$ blir arealet av nye rektangelet $5\cdot6 = 30$, som er mer enn $9$ cm$^2$.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Pytagoras setning sier at for rettvinklede trekanter så gjelder $a^2+b^2 = c^2$ der $a$ og $b$ er katetene i trekanten og $c$ er hypotenusen. Man kan derfor finne høyden i likebeinte trekanter hvis man vet sidelengdene, ved å halvere grunnlinjen og bruke Pytagoras setning.

I figuren er det skissert en åttekant inskribert i et kvardat der fire av sidelengdene har lengde $3$ og fire av sidelengdene har lengde $2$.

1. Bruk Pytagoras setning til å vise at sidelengdene til kvadratet åttekanten er inskribert i er  $3+2\sqrt 2$.

2. Forklar hvorfor høyden i trekantene med grunnlinje $3$ er $\frac{3}{2} + \sqrt 2$.

3. Avgjør arealet til åttekanten.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-14-31-10.png)

##### Vurderingskriterier

1. Studenten må argumentere for at lengen er $3 + 2 sqrt 2$. Dette kan for eksempel gjøres ved å kikke på hjørnet, der det blir oppgitt at det er en $45^\circ$ vinkel. Det betyr at trekanten i hjørnet er en likebein trekant med hypotenus lik $2$. Pytagoras gir dermed at lengden er
$$
\begin{aligned}
x^2 + x^2
& = 2^2
\\
2x^2
 & = 4
\\
x^2
& =
2
\\
x & = \sqrt 2.
\end{aligned}
$$
Dermed følger det nå at sidelengden er $3 + \sqrt 2$.
2. Studenten må argumentere for hva høyden er. Dette kan enkelt gjøres ved å argumentere for at den må være halve lengden av kvadratets sidelengde.
3. Studenten må avgjøre arealet. Det kan for eksempel avgjøres ved å ta arealet av kvadratet og trekke fra trekantene i hjørnet. Det gir
$$
\begin{aligned}
(3+2\sqrt 2)^2 - 4\frac{(\sqrt 2)^2}{2}
& =
3^2 + 2\cdot 6 \cdot \sqrt 2 + 4\cdot 2 - 2 \cdot 2
\\
& =
9 + 12\sqrt 2 + 8 - 4
\\
& = 13 + 12 \sqrt 2
\end{aligned}
$$

### Bruke begrepet formlikhet av trekanter

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar, gjennom et eksempel, hva som menes med formlike

trekanter.

##### Vurderingskriterier

Studenten må forklare gjennom et eksempel hva som menes med formlike trekanter. Forklaringen må inneholde en definisjon som enten peker til sammenhengen mellom vinklene i trekantene eller forholdet mellom samsvarende sider.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepet

Under ser du to formlike trekanter. Avgjør lengden på de resterende sidene hvis du får vite at:

1. $a = 3$, $b = 12$, $d = 1$ og $f = 4$.

2. $c = \frac{1} {2}$, $b = 4$, $f = \frac{3}{2}$ og $d = 9$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-14-43-14.png)

##### Vurderingskriterier

Studentene må aktivt bruke formlikhet til å avgjøre de resterende sidene.

1. Studenten kan peke på at siden $a$ og $d$ er de samsvarende sidene, så er skaleringsfaktoren mellom trekantene lik $3$. Dermed må $e$ være $3$ ganger så liten som $b = 12$, altså $e = 4$. Siden $f = 4$ må $c = 12$.
2. Studenten kan her peke på at $c$ og $f$ er de samsvarende sidene og at $f$ er tre ganger så stor som $c$. Dermed er skaleringsfaktoren den samme. Det gir på samme måte som i 1. at $a = 3$ og $e = 12$.

### Argumentere visuelt for Pytagoras setning

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepet

Gjengi og forklar Pytagoras setning. Forklaringen må referere til en figur.

##### Vurderingskriterier

Studenten må gi en forklaring av Pytagoras setning ved å referere til en figur.

#### Middels: Gi et visuelt argument for at Pytagoras setning gjelder

Gi et grunnskoletilpasset argument for Pytagoras setning.

##### Vurderingskriterier

Studenten må gi et grunnskoletilpasset argument for at Pytagoras setning gjelder. Dette innebærer å tegne en eller flere figurer og bruke de til å argumentere for Pytagoras setning.

### Bruke Pytagoras setning

#### Grunnleggende: Bruke Pytagoras setning til å løse enkle problemer

Finn lengden på hypotenusen i en rettvinklet trekant når du vet at katetene har lengde:

a. 3 og 4
b.  1 og 8

Utregningene skal ikke være avrundet og skal gis i eksakte verdier. Det vil si at hvis svaret er $\sqrt{1^{2} + 2^{2}} = \sqrt{5}$, så skal ikke dette rundes av til $2,236$.

##### Vurderingskriterier

Studenten må regne ut lengden på hypotenusen.
a. Vi har at $a^2 + b^2 = c^2$. Det gir at $3^2+4^2 = 25$. Dermed må hypotenusen være $\sqrt 25$.
b. Vi har at $1^2 + 8^2 = 65$ som gir at hypotenusen er $\sqrt 65$.

#### Middels: Bruke Pytagoras setning til å løse problemer

I figuren under ser dere et rektangel, med noen lengder ført på. Avgjør hva $x$, $y$ og $z$ må være.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-30-15-27-42.png)

##### Vurderingskriterier

Studenten må avgjøre lengdene $x$, $y$ og $z$. Dette kan gjøres ved å først se at $x = \sqrt{3^2 + 4^2} = 5$, ved å bruke nederste hjørnet til venstre i det store rektangelet. Trekanten nederst i venstre hjørne kan vi også løse ved å bruke at katetene er $8$ og $6$. Det gir at hypotenusen er $\sqrt{8^2+6^2}=10$.

Ved å studere flere trekanter kan studenten argumentere for at $z^2 + 10^2 = (10+y)^2$ og at $5^2 + y^2 = (z+3-8)^2$.
Dermed kan studentene regne ut og få at
$$
\begin{aligned}
z^2 + 10^2
& = (10+y)^2
\\
z^2 + 10^2
& =
10^2 + 20y + y^2
\\
z^2
& =
y^2 + 20y
\end{aligned}
$$
og
$$
\begin{aligned}
5^2 + y^2 & = (z+3-8)^2 = z^2 - 10z + 5^2
\\
y^2 & = z^2 - 10 z.
\end{aligned}
$$
Ved å bruke innsetning kan vi nå se at $z^2 = z^2 - 10 z + 20y$ eller at $10z = 20 y$ eller at $z = 2y$. Det gir videre at $y^2 = (2y)^2 - 20y$. Som nå gir at $3y^2 = 20y$ eller at $y = \frac{20}{3}$, som betyr at $z = \frac{40}{3}$.

## 17.02.23

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 1- og 2-dimensjonale eksempler.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

Velg passende måleenheter. Vis med ordforklaringer og illustrasjoner, uten å begrunne ved hjelp av de kjente formlene, hvordan man kan avgjøre

a. arealet av et trekant, når man kjenner til høyde og bredde

b. arealet av en sirkel, når man vet radius.

Bruk forklaringene og illustrasjonene til å vise hva de generelle formlene må være.

##### Vurderingskriterier: Grunnleggende {#f17g1}

Besvarelsen må gi eksempler i både en og to dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

##### Vurderingskriterier: Middels {#f17m1}

Besvarelsen må gi en forståelig forklaring (og illustrasjon) for hvordan man avgjør størrelsene. For omkrets må en få fram måleenheten en bruker (typisk et linjestykke. Ofte cm, meter og lignende). For areal må det komme tydelig fram hvordan arealet henger sammen med måleenheten kvadrat (noe som i de aller fleste tilfeller betyr at en må vise en omforming til et rektangel, et halvt rektangel eller liknende). Begrunnelsene trekke ut ideen fra forklaringen og gi en generell formel for de tre størrelsene.  

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter  i 3-dimensjonale figurer

Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 3-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f17g2}

Besvarelsen må gi eksempler i både tre dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Under ser du to parallelle linjer $f$ og $g$. Hva er vinkel $v$ når du får vite at $s = 35$ og $w = 13$?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-11-59.png)

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en sirkel med sentrum i $A$ og tre punkter på periferien, $C$, $D$ og $E$.  Punktene $C$ og $D$ skjærer av en sirkelbue og danner vinkelen $c = \angle DEC$. Hvis vinkel $c = 30^\circ$, hva er da vinkel $e = \angle DAC$?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-12-09.png)

##### Vurderingskriterier: Grunnleggende {#f173}

De må gi en forklaring med en illustrasjon på de gitte begrepene.

##### Vurderingskriterier: Middels {#f17m3}

Studentene må argumentere for hvor stor vinkelen $v$ er.

Dette gjøres gjerne ved å slå en parallell linje gjennom $v$. På denne måten kan en argumentere for at $v$ er summen av $s$ og $w$.

##### Vurderingskriterier: Avansert {#f17a3}

Studentene må på en forståelig måte få fram hvor stor $e$ er.

En naturlig framgangsmåte er benytte seg av diameteren på bildet og dele vinkel $c$ inn i $x$ og $y$, der $x = \angle AEC$ og $y = \angle DEA$. Deretter kan en bruke at $\triangle ADE$ og $\triangle ACE$ er likebeint for å argumentere for at $e = 60^\circ$.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene rettvinklet trekant, sirkel, parallellogram og trapes.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, en rettvinklet trekant er en likebeint trekant.

2. Avgjør og begrunn om følgende påstand om en trekant stemmer: En rettvinklet trekant har en indre vinkel som er $45^\circ$. Da må trekanten også være likebeint.

##### Vurderingskriterier: Grunnleggende {#f17g4}

Studentene må gi en forklaring med en illustrasjon på de gitte begrepene.

##### Vurderingskriterier: Middels {#f17m4}

Studentene må besvare begge oppgavene.

i. Dette kan motbevises ved å gi et eksempel der katetene ikke er like lange.

ii. Studenten må bruke at vinkelsummen i er $180^\circ$ til å argumentere for at trekanten må ha to $45^\circ$ vinkler. Dette gir da at trekanten må være likebeint.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Rektangler

b. Sirkler

c. Trapes

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Avgjør og begrunn om følgende påstand stemmer.

Et rektangel har sidelengder $x$ cm og $y$ cm og du øker begge lengdene med $3$ cm. Da blir det nye arealet $3\cdot 3$ cm$= 9$ cm større.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en vilkårlig trekant $ABC$. Punktene $F$, $E$ og $D$ er midtpunktene på sidene av trekanten. Trekker vi linjene fra hjørnene til motstående midtpunkt får vi et felles skjæringspunkt $G$ og trekanten deles opp i $6$ nye trekanter (markert i forskjellige farger under). Begrunn hvorfor arealet av alle de $6$ trekantene er det samme.  

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-13-42.png)

##### Vurderingskriterier: Grunnleggende {#f17g5}

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

##### Vurderingskriterier: Middels {#f17m5}

Dette må gjøres algebraisk. Her må det komme fram at $(x+3)\cdot (y+3) \neq xy + 9$.

##### Vurderingskriterier: Avansert {#f17a5}

Studenten må argumentere på en strukturert og forståelig måte.

En naturlig fremgangsmåte vil være å peke på at $\triangle DBA$ og $\triangle DCA$ har samme areal da de har lik grunnlinje og høyde (halve lengden av $BC$), og tilsvarende har $\triangle BDG$ og $\triangle DCG$ likt areal. Dermed kan det nå argumenteres for at trekantene $\triangle BGF$, $\triangle FGA$, $\triangle GEA$ og $\triangle GEC$ har samme areal. Gjentas dette argumentet nå kan studentene få fram at alle seks trekantene har samme areal.

## 13.02.23

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 1- og 2-dimensjonale eksempler.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

1. Velg passende måleenheter. Vis med ordforklaringer og illustrasjoner, uten å begrunne ved hjelp av de kjente formlene, hvordan man kan avgjøre

a. omkretsen av et trapes, når man vet sidelengdene

b. arealet av et parallellogram, når man kjenner til høyde og bredde

c. arealet av en sirkel, når man vet radius.

Bruk forklaringene og illustrasjonene til å vise hva de generelle formlene må være.

##### Vurderingskriterier: Grunnleggende {#f13g1}

Besvarelsen må gi eksempler i både en og to dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

##### Vurderingskriterier: Middels {#f13m1}

Besvarelsen må gi en forståelig forklaring (og illustrasjon) for hvordan man avgjør størrelsene. For omkrets må en få fram måleenheten en bruker (typisk et linjestykke. Ofte cm, meter og lignende). For areal må det komme tydelig fram hvordan arealet henger sammen med måleenheten kvadrat (noe som i de aller fleste tilfeller betyr at en må vise en omforming til et rektangel, et halvt rektangel eller liknende). Begrunnelsene trekke ut ideen fra forklaringen og gi en generell formel for de tre størrelsene.  

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter  i 3-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 3-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f13g2}

Besvarelsen må gi eksempler i både tre dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Argumenter for hvor stor vinkelsummen av de indre vinklene i en trekant er.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du en trekant $ABC$, der $\angle ACB$ er halvert og går gjennom punktet $E$ (det vil si at $a = c$. Linjen som går gjennom $BD$ er parallell med linjen gjennom $AC$.

Forklar at $a = b$ og $d = e$.

Forklar hvorfor $\triangle AEC$  er formlik med $\triangle EDB$ ved å begrunne at de indre vinklene i trekantene er de samme.

Når to trekanter er formlike gjelder det at de samsvarende sidene er har samme forhold. Det vil si $\frac{AC}{BD} = \frac{AE}{EB}$.

Forklar hvorfor $\frac{AC}{BC} = \frac{AE}{EB}$ (vink: trekanter med to like vinkler er likebeinte).

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-16-49.png)

##### Vurderingskriterier: Grunnleggende {#f13g3}

De må gi en forklaring med en illustrasjon på de gitte begrepene.

##### Vurderingskriterier: Middels {#f13m3}

Studentene må argumentere for hvor stor vinkelsummen av de indre vinklene i en trekant er.

##### Vurderingskriterier: Avansert {#f13a3}

Studentene må gjøre alle oppgavene.

1. Det må pekes på at $c = a$. Siden $BD$ er parallell med $AC$, så vil $c = b$ (dette kan pekes på ved å forlenge $BD$ og $CD$ og lage toppvinklene) som igjen betyr at $a = b$. At $d = e$ følger igjen av at linjene $BD$ og $AC$ er parallelle.
2. Her må studenten bare bruke informasjonen fra 1. sammen med at vinkelsummen i trekanter er $180$ grader.
3. Siden $a = b$ må $CB = BD$ (fordi det er en likebeint trekant fra 1.). Nå følger resultatet bare ved direkte bruk av formlikhet.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene kvadrat, trapes, likesidet trekant og sirkel.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, et trapes er et rektangel.

2. Avgjør og begrunn om følgende påstand om en firkant stemmer: Diagonalene i firkanten er like lange, og diagonalene står vinkelrett på hverandre. Derfor må firkanten være et kvadrat.

##### Vurderingskriterier: Grunnleggende {#f13g4}

Studentene må gi en forklaring med en illustrasjon på de gitte begrepene.

##### Vurderingskriterier: Middels {#f13m4}

Studentene må besvare begge oppgavene.

i. Dette kan motbevises ved å gi et eksempel på et trapes der to motstående sider ikke er parallelle. Et slikt trapes vil ikke oppfylle kravene for å være et rektangel.

ii. Studenten kan lage to diagonaler som er like lange og som står vinkelrett på hverandre som ikke skjærer hverandre på midten. Dette vil gi en drake, som ikke er et kvadrat.

#### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Rektangler

b. Sirkler

c. Trapes

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Et parallellogram har areal $A$. Vis at hvis du dobler høyden og tripler lengden i parallellogrammet så blir det nye arealet  $6A$.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Legger du inn en innsirkel i en rettvinklet trekant, vil tangeringspunktene dele trekantens sidelengder inn i lengdene $x+y$ og $y+z$ og $x+z$ (se figur). Argumenter ved å bruke egenskapene fra figuren at arealet av trekanten må være $(x+y+z)\cdot x$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-18-16.png)

##### Vurderingskriterier: Grunnleggende {#f13g5}

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

##### Vurderingskriterier: Middels {#f13m5}

Dette må gjøres algebraisk. For eksempel ved å peke på at $A = ah$ er arealet av et parallellogram med høyde $h$ og grunnlinje $a$. Tripler jeg grunnlinja får jeg $3a$ og dobler jeg høyden får jeg $2h$. Arealet av det nye parallellogrammet blir nå $3a\cdot 2h = 6 ah = 6A$. Som altså er $6$ ganger så stort som det originale arealet.

##### Vurderingskriterier: Avansert {#f13a5}

Studenten må gjøre argumentere på en strukturert og forståelig måte.

Studenten må få fram at radius til innsirkelen er $x$. Deretter følger resultatet ved å bryte trekanten inn i seks mindre trekanter og legge arealet av dem sammen.

## 10.02.23

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 1 og 2 dimensjoner

#### Grunnleggende: Gjengi, forklare og gi eksempler på begrepene størrelse, måltall og måleenheter i 1- og 2-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 1- og 2-dimensjonale eksempler.

#### Middels: Bruke begrepene til å forklare hvordan man kan avgjøre omkrets og areal av firkanter, trekanter og sirkler

1. Velg passende måleenheter. Vis med ordforklaringer og illustrasjoner, uten å begrunne ved hjelp av de kjente formlene, hvordan man kan avgjøre

a. omkretsen av et trapes, når man vet sidelengdene

b. arealet av et parallellogram, når man kjenner til høyde og bredde

c. arealet av en sirkel, når man vet radius.

Bruk forklaringene og illustrasjonene til å vise hva de generelle formlene må være.

##### Vurderingskriterier: Grunnleggende {#f10g1}

Besvarelsen må gi eksempler i både en og to dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

##### Vurderingskriterier: Middels {#f10m1}

Besvarelsen må gi en forståelig forklaring (og illustrasjon) for hvordan man avgjør størrelsene. For omkrets må en få fram måleenheten en bruker (typisk et linjestykke. Ofte cm, meter og lignende). For areal må det komme tydelig fram hvordan arealet henger sammen med måleenheten kvadrat (noe som i de aller fleste tilfeller betyr at en må vise en omforming til et rektangel, et halvt rektangel eller liknende). Begrunnelsene trekke ut ideen fra forklaringen og gi en generell formel for de tre størrelsene.  

### Bruke begrepene måltall, størrelse og måleenhet til å avgjøre størrelsen av grunnleggende figurer i 3 dimensjoner

#### Grunnleggende: Gjengi og forklare og gi eksempler på begrepene størrelse, måltall og måleenheter  i 3-dimensjonale figurer

1. Forklar og gi eksempler på hva som menes med begrepene størrelse, måltall og måleenhet. Besvarelsen må inneholde 3-dimensjonale eksempler.

##### Vurderingskriterier: Grunnleggende {#f10g2}

Besvarelsen må gi eksempler i både tre dimensjoner der måltall, måleenhet og størrelsen blir forklart forståelig.

### Bruke begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

1. Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene punkt, linje, plan, linjestykke, vinkel og parallelle linjer.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Argumenter for hvor stor vinkelsummen av de indre vinklene i en femkant er.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under ser du to parallelle linjer $f$ og $g$. Mellom linjene er det tre linjestykker som danner vinklene $a$, $b$, $c$ og $d$. Når $a = 50^\circ$ og $d = 70^\circ$, avgjør hvor stor $b+c$ er.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-21-01.png)

##### Vurderingskriterier: Grunnleggende {#f103}

De må gi en forklaring med en illustrasjon på de gitte begrepene.  

##### Vurderingskriterier: Middels {#f10m3}

Studentene må argumentere for hvor stor vinkelsummen av de indre vinklene i en femkant er.

##### Vurderingskriterier: Avansert {#f10a3}

Studentene må på en forståelig måte få fram hor stor summen av $b+c$ er.

En naturlig framgangsmåte er å trekke en linje parallell til $f$ og $g$ gjennom vinkel $d$ og $b$. På denne måten kan en splitte $d$ og $b$ inn i to vinkler. Disse kan nå brukes videre til å vise at $b = 50 + y$ og at $c = 70 - y$, der $y$ er ned *nedre* vinkelen i $b$.

### Bruke begrepene kvadrat, rektangel, parallellogram, trapes, likebeint trekant, likesidet trekant, rettvinklet trekant, mangekant, sirkel

#### Grunnleggende: Gjengi og forklare, gi eksempler og illustrasjoner til begrepene

Forklar og gi eksempler (med illustrasjoner) på hva som menes med begrepene kvadrat, trapes, likesidet trekant og sirkel.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

1. Forklar hvorfor, eller hvorfor ikke, et trapes er et rektangel.

2. Avgjør og begrunn om følgende påstand om en firkant stemmer: Diagonalene i firkanten er like lange, og diagonalene står vinkelrett på hverandre. Derfor må firkanten være et kvadrat.

##### Vurderingskriterier: Grunnleggende {#f10g4}

Studentene må gi en forklaring med en illustrasjon på de gitte begrepene.

##### Vurderingskriterier: Middels {#f10m4}

Studentene må besvare begge oppgavene.

i. Dette kan motbevises ved å gi et eksempel på et trapes der to motstående sider ikke er parallelle. Et slikt trapes vil ikke oppfylle kravene for å være et rektangel.

ii. Studenten kan lage to diagonaler som er like lange og som står vinkelrett på hverandre som ikke skjærer hverandre på midten. Dette vil gi en drake, som ikke er et kvadrat.

### Bruke formler for størrelser av figurer til å utforske geometriske sammenhenger

#### Grunnleggende: Gjengi og forklar formlene for trekanter, rektangler, parallellogram, trapes, sirkler, prismer, sylindre og pyramider

1. Gjengi formelen for å avgjøre arealet av

a. Trekanter

b. Trapes

c. Prismer

Besvarelsene må inneholde en illustrasjon der en peker på relevante lengder.

#### Middels: Argumentere for enkle sammenhenger knyttet til begrepene

Du har en sirkel med radius $r$. Hvis radius økes med $x$. Vis algebraisk hvor mye lengre omkretsen til den nye sirkelen har blitt.

#### Avansert: Utforske og løse ukjente problemet knyttet til begrepene

Under er et rektangel med høyde $h$ som består av en blå rettvinklet trekant, en grønn rettvinklet trekant der lengden på grunnlinjen er $x$, og et trapes der de parallelle sidene har lengde $a$ og $b$ som markert på figuren.

1. Uttrykk lengden fra punkt $L$ til $I$ ved hjelp av $a$, $b$ og $x$.

2. Avgjør arealet $A$ av rektangelet.

3. Avgjør arealet $B$ til den blå trekanten og arealet $C$ til den grønne trekanten.

4. Begrunn at arealet av trapeset må være $\frac{(a+b)h}{2}$, ved å bruke arealene du fant i oppgave 2 og 3.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-22-14.png)

##### Vurderingskriterier: Grunnleggende {#f10g5}

Studentene må gjengi formlene korrekt med en illustrasjon der det kommer fram hvilke lengder som brukes.

##### Vurderingskriterier: Middels {#f10m5}

Dette må gjøres algebraisk.

##### Vurderingskriterier: Avansert {#f10a5}

Studenten må gjøre alle oppgavene for å få godkjent.

1. Studenten må få fram at $LI = a+x-b$.
2. Studenten må peke på at $A = (a+x)h$.
3. Studenten må få fram at $B = \frac{(a+x-b)h}{2}$ og at $C = \frac{xh}{2}$.
4. Studenten må få fram arealet. Det vil være naturlig å regne seg fram ved å se på $A-B-C$.
$$
\begin{aligned}
A-B-C & = (a+x-b)h-\frac{(a+x-b)h}{2} - \frac{xh}{2}
\\
& = (a+x-b)h - \frac{(a-b+2x)h}{2} = \frac{(a+b) h}{2}.
\end{aligned}
$$

*Merk* at det bevisst er utelatt litt detaljer i regningen som bør være med.
