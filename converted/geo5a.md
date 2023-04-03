
#### Avansert:  Øveoppgaver

1. Arkene i A-formatet (A1, A2, A3, A4, A5, osv) har den egenskapen at
    når du halverer de ved å brette de på langsiden, så vil de bevare
    forholdet mellom sidelengdene. Det vil si at hvis sidelengdene i A4
    er *a* og *b,* så er sidelengdene i A5 *b/2* og *a* og forholdet
    mellom sidelengdene vil være like. Vis at dette forholdet, vil

2. Hvor stor er summen av de små omkretsene i forhold til den store?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image3.png)

#### Avansert:  31.03.23

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
(3+2\sqrt 2)^2 - 4(\sqrt 2)^2
& =
3^2 + 2\cdot 6 \cdot \sqrt 2 + 4\cdot 2 - 4 \cdot 2
\\
& =
9 + 12\sqrt 2 + 8 - 8
\\
& = 9 + 12 \sqrt 2
\end{aligned}
$$

#### Avansert:  17.02.23

Under ser du en vilkårlig trekant $ABC$. Punktene $F$, $E$ og $D$ er midtpunktene på sidene av trekanten. Trekker vi linjene fra hjørnene til motstående midtpunkt får vi et felles skjæringspunkt $G$ og trekanten deles opp i $6$ nye trekanter (markert i forskjellige farger under). Begrunn hvorfor arealet av alle de $6$ trekantene er det samme.  

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-13-42.png)

#### Vurderingskriterier avansert:  17.02.23

Studenten må argumentere på en strukturert og forståelig måte.

En naturlig fremgangsmåte vil være å peke på at $\triangle DBA$ og $\triangle DCA$ har samme areal da de har lik grunnlinje og høyde (halve lengden av $BC$), og tilsvarende har $\triangle BDG$ og $\triangle DCG$ likt areal. Dermed kan det nå argumenteres for at trekantene $\triangle BGF$, $\triangle FGA$, $\triangle GEA$ og $\triangle GEC$ har samme areal. Gjentas dette argumentet nå kan studentene få fram at alle seks trekantene har samme areal.


#### Avansert:  10.02.23 {#f10}

Under er et rektangel med høyde $h$ som består av en blå rettvinklet trekant, en grønn rettvinklet trekant der lengden på grunnlinjen er $x$, og et trapes der de parallelle sidene har lengde $a$ og $b$ som markert på figuren.

1. Uttrykk lengden fra punkt $L$ til $I$ ved hjelp av $a$, $b$ og $x$.

2. Avgjør arealet $A$ av rektangelet.

3. Avgjør arealet $B$ til den blå trekanten og arealet $C$ til den grønne trekanten.

4. Begrunn at arealet av trapeset må være $\frac{(a+b)h}{2}$, ved å bruke arealene du fant i oppgave 2 og 3.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-22-22-14.png)

#### Vurderingskriterier avansert:  10.02.23 {#f10}

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
