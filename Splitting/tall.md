<!--
PDF:
Kjør i terminal fra markdown mappa pandoc .\quizzer\tall\tall.md -f markdown -t pdf --pdf-engine=xelatex --variable=block-headings --toc -o .\quizzer\tall\tall.pdf
HTML:
pandoc .\quizzer\tall\tall.md -f markdown -t html --mathjax --template=template.html --toc -s -H styling.css -o .\quizzer\tall\tall.html
-->

# Tall

## Øveoppgaver

### Forklare hva et posisjonssystem er

#### Grunnleggende

Forklare hva et posisjonssystem er, og regne med tall uttrykt i
posisjonssystem med ulike baser.

1. Forklar hvordan et posisjonssystem er bygd opp. Gi eksempler med
   ulike baser.

2. Hvilke siffer trengs i et posisjonssystem med base syv? Forklar.

3. Hvilke siffer treng i et posisjonssystem med base tolv? Forklar.

4. Skriv de første tjuefem tallene (eller mer) i base ...

   a. To

   b. Tre

   c. Fem

   d. Tolv

5. Vis hva tallene «betyr» ved å skrive dem på utvidet form.

   a. $234_{fem}$

   b. $307_{åtte}$

   c. $93A_{elleve}$

##### Løsningsforslag

1. Ideen med posisjonssystem er å gruppere (i for eksempel tiere), og indikere ved hjelp av posisjon hvilken verdi et gitt siffer står for. Når basen, eller grunntallet, er ti, grupperer vi i tiere. På den måten trenger vi bare ti unike siffer, 0–9. I stedet for et eget symbol for ti, skriver vi 10, som betyr én tier, ingen enere. Vi kan la et hvilket som helst tall danne basen. I base seks, for eksempel, grupperer vi i seksere. Vi trenger da seks unike siffer: 0–5. Fra høyre mot venstre har vi posisjonene 1, 6, 36, 216 og så videre, altså potenser av seks: $6^0,6^1,6^2,6^3$ og så videre.
2. Vi trenger like mange siffer som basens verdi. Når basen, eller grunntallet, er syv, trenger vi syv siffer: 0, 1, 2, 3, 4, 5 og 6. Vi trenger ikke et eget symbol for syv, for det er én syver og ingen enere, altså 10.
3. Som over. Siden basen er høyere enn ti, må vi «finne opp» nye symboler for ti og elleve. Enkleste løsning er A og B. Vi har da 0, 1, 2, 3, 4, 5, 6. 7, 8, 9, A, B. Tolv er 10.
4. \

| Ti  | To     | Tre | Fem | Tolv |
| --- | ------ | --- | --- | ---- |
| 1   | 1      | 1   | 1   | 1    |
| 2   | 10     | 2   | 2   | 2    |
| 3   | 11     | 10  | 3   | 3    |
| 4   | 100    | 11  | 4   | 4    |
| 5   | 101    | 12  | 10  | 5    |
| 6   | 110    | 20  | 11  | 6    |
| 7   | 111    | 21  | 12  | 7    |
| 8   | 1 000  | 22  | 13  | 8    |
| 9   | 1 001  | 100 | 14  | 9    |
| 10  | 1 010  | 101 | 20  | A    |
| 11  | 1 011  | 102 | 21  | B    |
| 12  | 1 100  | 110 | 22  | 10   |
| 13  | 1 101  | 111 | 23  | 11   |
| 14  | 1 110  | 112 | 24  | 12   |
| 15  | 1 111  | 120 | 30  | 13   |
| 16  | 10 000 | 121 | 31  | 14   |
| 17  | 10 001 | 122 | 32  | 15   |
| 18  | 10 010 | 200 | 33  | 16   |
| 19  | 10 011 | 201 | 34  | 17   |
| 20  | 10 100 | 202 | 40  | 18   |
| 21  | 10 101 | 210 | 41  | 19   |
| 22  | 10 110 | 211 | 42  | 1A   |
| 23  | 10 111 | 212 | 43  | 1B   |
| 24  | 11 000 | 220 | 44  | 20   |
| 25  | 11 001 | 221 | 100 | 21   |

5. \
   1. $234_{\text{fem}}=2⋅5^2+3⋅5^1+4⋅5^0=2⋅25+3⋅5+4$
   2. $307_{\text{åtte}}=3⋅8^2+0⋅8^1+7⋅8^0=3⋅64+0⋅8+7$
   3. $93A_{\text{elleve}}=9⋅11^2+3⋅11^1+A⋅11^0=2⋅12 +3⋅11 10$

#### Middels: Forklare hva et posisjonssystem er, og gjøre om tall mellom ulike baser

1. Gjør om til base ti.

   a. $4321_{fem}$

   b. $666_{syv}$

   c. $305_{åtte}$

   d. $A0B3_{tolv}$

2. Gjør om ...

   a. $224_{ti}$ til base tre

   b. $144_{ti}$ til base tolv

   c. $777_{ti}$ til base syv

3. Gjør om til base to.

   a. $17_{ti}$

   b. $17_{tolv}$

   c. $72_{åtte}$

4. Gjør om ...

   a. $224_{fem}$ til base tre

   b. $10010_{to}$ til base fire

   c. ${20B}_{tolv}$ til base fem

##### Løsningsforslag

1. Gjør om til base ti.

   a. $4321_{\text{fem}} = 4 \cdot 5^{3} + 3 \cdot 5^{2} + 2 \cdot 5^{1} + 1 \cdot 5^{0} = 4 \cdot 125 + 3 \cdot 25 + 2 \cdot 5 + 1 = 586_{ti}$

   b. $666_{\text{syv}} = 6 \cdot 7^{2} + 6 \cdot 7^{1} + 6 \cdot 7^{0} = 6 \cdot 49 + 6 \cdot 7 + 6 = 192_{ti}$

   c. $305_{\text{åtte}} = 3 \cdot 8^{2} + 0 \cdot 8^{1} + 5 \cdot 8^{0} = 3 \cdot 64 + 0 \cdot 8 + 5 = 197_{ti}$

   d. $A0B3_{\text{tolv}} = A \cdot 12^{3} + 0 \cdot 12^{2} + B \cdot 12^{1} + 3 \cdot 12^{0} = 10 \cdot 1\ 728 + 0 \cdot 144 + 11 \cdot 12 + 3 = {17\ 415}_{ti}$

2. Gjør om ...
   a. $224_{ti}$ til base tre: Posisjonene i base tre: 243 ($3^{5}$), 81 ($3^{4}$), 27 ($3^{3}$), 9 ($3^{2}$), 3 ($3^{1}$), 1 ($3^{0}$). 243 er høyere enn 224, så høyeste aktuelle posisjon er 81. Det går **[to]{.underline}** 81-ere på 224, med 62 i rest. Det går **[to]{.underline}** 27-ere på 62, med 8 i rest. 8 er **[ingen]{.underline}** 9-ere, **[to]{.underline}** 3-ere og **[to]{.underline}** 1-ere. $224_{ti} = 22022_{tre}$
   b. $144_{ti}$ til base tolv $100_{tolv}$
   c. $777_{ti}$ til base syv $2160_{syv}$

3. Gjør om til base to.
   a. $17_{ti} = 16 + 1$,\ så\ $10001_{to}$
   b. $17_{tolv} = 12 + 7 = 16 + 2+1$,\ så\ $10011_{to}$
   c. $72_{åtte} = 56 + 2 = 32+24+2 = 32+16+8+2$,\ så\ $111010_{to}$
4. Gjør om ...
   a. $224_{fem}$ til base tre: $224_{fem} = 2 \cdot 25 + 2 \cdot 5 + 4 = 2 \cdot 27 + 1 \cdot 9 + 0 \cdot 3 + 1 = 2101_{tre}$
   b. $10010_{to}$ til base fire: $10010_{to} = 1 \cdot 16 + 1 \cdot 4 = 110_{fire}$
   c. ${20B}_{tolv}$ til base fem: ${20B}_{tolv} = 2 \cdot 144 + 11 = 2 \cdot 125 + 38 + 10 + 1 = 2 \cdot 125 + 49 = 2 \cdot 125 + 1 \cdot 25 + 4 \cdot 5 + 4 \cdot 1 = 2144_{fem}$

#### Avansert: Utføre beregninger med tall uttrykt i andre baser enn ti

1. Gjør beregningene i den aktuelle basen (uten å oversette til base
   ti, altså).

   a. $123_{fem} + 321_{fem}$

   b. $321_{fire} - 123_{fire}$

   c. $32_{åtte} \cdot 24_{åtte}$

   d. $4A3_{tolv}\ :3_{tolv}$

   e. Lag egne regnestykker.

2. Finn basen $b$ uten gjett og sjekk.

   a. $143_{b} = 48_{ti}$

   b. $153_{b} = 69_{ti}$

   c. $313_{b} = 55_{ti}$

3. Forklar hvordan man enkelt kan finne basen $b$ til tall på formen
   $121_{b}$ dersom man kjenner tallets verdi i base ti.

4. Finn sifrene $A$ og $B$ når $AB_{fem} = 17_{ti}$ og
   $AB_{syv} = 23_{ti}$.

5. Når vi uttrykker tall i titallsystemet er et tall delelig med to
   bare dersom siste siffer er delelig med to. Uttrykt i
   femtallsystemet, derimot, er et tall delelig med to bare dersom
   tverrsummen er delelig med to. Begrunn dette. Forsøk også å
   generalisere: I hvilke baser gjelder siste-siffer-regelen, og i
   hvilke gjelder tverrsum-regelen?

##### Løsningsforslag

1. Gjør beregningene i den aktuelle basen (uten å oversette til base
   ti, altså).

   a. $123_{fem} + 321_{fem}$

   b. $321_{fire} - 123_{fire}$

   c. $32_{åtte} \cdot 24_{åtte}$

   d. $4A3_{tolv}\ :3_{tolv}$

   e. Lag egne regnestykker.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/Picture1.jpg)

2. Finn basen $b$ uten gjett og sjekk.

   a. $143_{b} = 48_{ti}$ \
   Dette gir likninga $b^{2} + 4b + 3 = 48$. Får da $b^{2} + 2 \cdot 2b + 4 = 49 \rightarrow (b + 2)^{2} = 7^{2} \rightarrow b = 5$.

   b. ${153}_{b} = 69_{ti}$

Gir likninga

$$
\begin{aligned}
b^{2} + 5b + 3
& = 69
\\
b^{2} + 2 \cdot \frac{5}{2}b + \left( \frac{5}{2} \right)^{2}
& = \frac{4 \cdot 66}{4} + \frac{25}{4}
\\
\left( b + \frac{5}{2} \right)^{2}
& = \frac{289}{4}
\\
b
& = \frac{17 - 5}{2}
\end{aligned}
$$

Basen er seks.

c. $313_{b} = 55_{ti}$

$$
\begin{aligned}
3b^{2} + b + 3
&  = 55
\\
b^{2} + \frac{1}{3}b
& = \frac{52}{3}
\\
b^{2} + 2 \cdot \frac{1}{6}b + \left( \frac{1}{6} \right)^{2}
&  = \frac{1}{36} + \frac{52 \cdot 12}{36}
\\
\left( b + \left( \frac{1}{6} \right) \right)^{2}
&  = \frac{625}{36}
\\
b
& = 4
\end{aligned}
$$

1. Forklar hvordan man enkelt kan finne basen $b$ til tall på formen
   $121_{b}$ dersom man kjenner tallets verdi i base ti.

$121_{b} = b^{2} + 2b + 1 = (b + 1)^{2}$. Kjenner man verdien $n$ i base
ti, er det bare å løse likningen $(b + 1)^{2} = n$. Med andre ord, basen
er roten av verdien i base ti minus én.

4. Finn sifrene $A$ og $B$ når $AB_{fem} = 17_{ti}$ og
   $AB_{syv} = 23_{ti}$.

Første info gir $5A + B = 17$. Andre info gir $7A + B = 23$. Nå er det
bare å løse likningssettet. Trekker siste fra første:
$2A = 6 \rightarrow A = 3$. Da er $B = 2$.

5. Når vi uttrykker tall i titallsystemet er et tall delelig med to
   bare dersom siste siffer er delelig med to. Uttrykt i
   femtallsystemet, derimot, er et tall delelig med to bare dersom
   tverrsummen er delelig med to. Begrunn dette. Forsøk også å
   generalisere: I hvilke baser gjelder siste-siffer-regelen, og i
   hvilke gjelder tverrsum-regelen?

Hint: I partallsbaser er det bare enerposisjonen som kan være oddetall.
Når basen $b$ er et oddetall, er også $b^{n}$ et oddetall. Da er
$b^{n} - 1$ alltid par.

### Beskrive situasjoner med hensyn til additive strukturer

#### Grunnleggende: Gjengi med eksempler de ulike additive strukturene for både addisjon og subtraksjon

1. Gi et eksempel på hver av strukturene med _addisjon_ som modell:
   _økning, forening, additiv sammenlikning, komplettering_ og
   _oppheving av minskning_.

2. Gi et eksempel på hver av strukturene med _subtraksjon_ som modell:
   _minskning, oppdeling, additiv sammenlikning, mangel_ og _oppheving
   av økning_.

##### Løsningsforslag

1. Gi et eksempel på hver av strukturene med _addisjon_ som modell:
   _økning, forening, additiv sammenlikning, komplettering_ og
   _oppheving av minskning_. Alfa.

2. Gi et eksempel på hver av strukturene med _subtraksjon_ som modell:
   _minskning, oppdeling, additiv sammenlikning, mangel_ og _oppheving
   av økning_. Alfa.

#### Middels: Avgjøre og begrunne hvilken struktur en gitt situasjon svarer til

1. Avgjør hvilken additiv struktur situasjonene svarer til. Spesifiser
   også hva som er ukjent der det er relevant. Merk at én og samme
   situasjon kan tolkes både som addisjon og subtraksjon.

   a. Arne hadde litt penger i lommeboka. Han samler og panter flasker
   for 167 kroner. Nå har han 527 kroner. Hvor mye hadde han fra
   før?

   b. I bilen på vei til butikken for å pante, satte Arne opp farta
   med 12 km/t til 73 km/t. Hvor høy fart holdt han før
   fartsøkninga?

   c. Forrige gang Arne pantet, fikk han 234 kroner. Hvor mye mer var
   det enn denne gang?

   d. For å få råd til egen pantemaskin, mangler Arne 12 364 kroner.
   Hvor mye koster en pantemaskin?

   e. Arne innser at prosjekt «egen pantemaskin» ikke lar seg
   gjennomføre uten hjelp. Han slår seg sammen med Anne. De har til
   sammen 9 530. Hvor mange penger har Anne?

   f. Etter en tids hardt innsamlingsarbeid, kjøper Arne og Anne
   omsider en pantemaskin. De sitter da igjen med 421 kroner. Hvor
   mye penger hadde før de kjøpte maskinen?

##### Løsningsforslag

1. Avgjør hvilken additiv struktur situasjonene svarer til. Spesifiser
   også hva som er ukjent der det er relevant. Merk at én og samme
   situasjon kan tolkes både som addisjon og subtraksjon.
   a. Arne hadde litt penger i lommeboka. Han samler og panter flasker for 167 kroner. Nå har han 527 kroner. Hvor mye hadde han fra før? Økning, ukjent utgangspunkt. $\_\_ + 167 = 527$ eller $527 - 167 = \_\_$. **Eller** forening, total kjent: slår sammen mengde 1: penger i lommeboka med mengde 2: pantepenger.
   b. I bilen på vei til butikken for å pante, satte Arne opp farta med 12 km/t til 73 km/t. Hvor høy fart holdt han før fartsøkninga? Samme som over.
   c. Forrige gang Arne pantet, fikk han 234 kroner. Hvor mye mer var det
   enn denne gang? Sammenlikning, ukjent differanse. $167 + \_\_ = 234$
   eller $234 - 167 = \_\_$.

   d. For å få råd til egen pantemaskin, mangler Arne 12 364 kroner. Hvor mye koster en pantemaskin? Komplettering/mangel, ukjent total: $har + mangler = ?$ eller $? - mangler = har$, eller $? - har = mangler$.

   e. Arne innser at prosjekt «egen pantemaskin» ikke lar seg gjennomføre uten hjelp. Han slår seg sammen med Anne. De har til sammen 9 530. Hvor mange penger har Anne? Sammenslåing, total kjent.

   f. Etter en tids hardt innsamlingsarbeid, kjøper Arne og Anne omsider en pantemaskin. De sitter da igjen med 421 kroner. Hvor mye penger hadde før de kjøpte maskinen? Oppheving av minskning.

### Beskrive situasjoner med hensyn til multiplikative strukturer

#### Grunnleggende: Gjengi med eksempler de ulike multiplikative strukturene for både multiplikasjon og divisjon

1. Gi et eksempel på hver av strukturene med _multiplikasjon_ som modell: _like grupper, multiplikativ sammenlikning, rate, kombinatorisk situasjon_ og _rektangulært arrangement_.
2. Gi et eksempel på hver av strukturene med _divisjon_ som modell, både målings- og delingsdivisjon i de tre første: _like grupper, multiplikativ sammenlikning, rate, kombinatorisk situasjon_ og _rektangulært arrangement_.

#### Middels: Avgjøre og begrunne hvilken struktur en gitt situasjon svarer til

1. Avgjør hvilken multiplikativ struktur situasjonene svarer til.
   Spesifiser også hva som er ukjent der det er relevant. Merk at én og
   samme situasjon kan tolkes både som multiplikasjon og divisjon.

   a. Arne rydder i flaskesamlinga si for lettere å kunne telle over
   hvor mange panteflasker han har. Han fyller 12 bæreposer, alle
   med 13 flasker. Hvor mange flasker har Arne?

   b. Anne, som konsekvent bidrar betydelig mer enn Arne i deres
   felles prosjekter, har 624 flasker. Hvor mange flere har hun i
   forhold til Arne?

   c. Med 3 kroner i pant per flaske, hvor mye hanker de inn når de
   panter flaskene sine?

   d. Hensikten med pantingen denne gangen, er å kjøpe garn for å
   strikke et rektangulært teppe. (Teppet skal ligge foran den nye
   panteautomaten deres for å hindre søl på gulvet.) Teppet skal ha
   et areal på 3,2 m^2^ og være to meter den ene veien. Hvor langt
   skal det være den andre veien?

   e. Arne og Anne er estetisk bevisste og ønsker å lage et
   dekorativt, stripet teppe i to farger. I garnbutikken selger de
   garn i fem ulike farger. Hvor mange tepper kan de velge å
   strikke?

   f. Etter å ha betalt for garnet, hadde Arne og Anne 164 kroner
   igjen som de fordeler likt mellom seg. Hvor mye får hver?

   g. Hver fargestripe måler fem centimeter nedover den lengste sida.
   Hvor mange striper har teppet?

##### Løsningsforslag

1. Avgjør hvilken multiplikativ struktur situasjonene svarer til.
   Spesifiser også hva som er ukjent der det er relevant. Merk at én og
   samme situasjon kan tolkes både som multiplikasjon og divisjon.

   a. Like grupper.

   b. Sammenlikning.

   c. Rate.

   d. Rektangulært arrangement.

   e. Kombinatorisk situasjon.

   f. Like grupper: delingsdivisjon.

   g. Like grupper: målingsdivisjon.

### Bruke regnestrategier og egenskaper ved regneoperasjonene

#### Grunnleggende: Gjengi kommutativ, assosiativ og distributiv egenskap for addisjon og multiplikasjon

1. Forklart kort med eksempler de tre egenskapene.

#### Middels: Bruke regnestrategier, også ved hjelp av egenskapene over

1. Gjør beregningene ved hjelp av strategier (som ikke er oppstilt
   regning).

   a. $126 - 31$

   b. $126 + 37$

   c. $136\ :8$

   d. $461\ :20$

   e. $\frac{3}{4} \cdot 160$

   f. $17 \cdot 19$

2. Vis hvordan én eller flere av de tre egenskapene kan brukes som
   regnestrategier.

   a. $13 \cdot 26$

   b. $376 + 39$

   c. $14 \cdot 7$

   d. $113 \cdot 6$

   e. $15 \cdot 8 + 30$

   f. $\frac{5}{4} \cdot 120$

##### Løsningsforslag

1. Gjør beregningene ved hjelp av strategier (som ikke er oppstilt
   regning).

   a. $126 - 31$ Eks fast differanse: $125 - 30$

   b. $126 + 37$ Eks opp/ned: $123 + 40$

   c. $136\ :8$ Eks forkorte: $68\ :4 = 34\ :2$

   d. $461\ :20$ Eks dele på ti, dele på to: $46,1\ :2$

   e. $\frac{3}{4} \cdot 160$ Eks: $\frac{1}{4} \cdot 16 = 4$,
   $3 \cdot 4 = 12$, $10 \cdot 12 = 120$

   f. $17 \cdot 19$ Eks distributiv og assosiativ:
   $17 \cdot 2 \cdot 10 = 340$, $340 - 17 = 323$

2. Vis hvordan én eller flere av de tre egenskapene kan brukes som
   regnestrategier.
   a. $13 \cdot 26$ $= (10 + 3) \cdot 26$
   b. $376 + 39$ $= (375 + 1) + 39 = 375 + (1 + 39)$
   c. $14 \cdot 7$ $= (2 \cdot 7) \cdot 7 = 2 \cdot (7 \cdot 7)$
   d. $113 \cdot 6$ $= 6 \cdot 113 = 6 \cdot (110 + 6)$
   e. $15 \cdot 8 + 30$ $= 8 \cdot 15 + 2 \cdot 15 = (8 + 2) \cdot 15$
   f. $\frac{5}{4} \cdot 120$ $= 5 \cdot (\frac{1}{4} \cdot 120)$

#### Avansert: Bruke, illustrere og begrunne regnestrategier og egenskapene

1. Gjør oppgavene fra middels. Begrunn, og dersom hensiktsmessig,
   illustrer strategien slik at det går tydelig frem at den alltid
   funker.

2. Fra Nasjonal deleksamen 30.11.22.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image1.png)

##### Løsningsforslag

1. Gjør oppgavene fra middels. Begrunn, og dersom hensiktsmessig, illustrer strategien slik at det går tydelig frem at den alltid funker.

1 c) Se for deg en illustrasjon av 136 fordelt i 8 like bunker. Da vil
_halvparten_ av 136 ligge i _halvparten_ av de 8 bunkene. Tilsvarende om
vi for eksempel deler på 6 og forkorter med 3. Av det som er fordelt
likt på seks bunker, finner vi en tredel i en tredel av bunkene (i to
bunker, altså).

Ellers: Heftet.

2. Fra Nasjonal deleksamen 30.11.22.

a) er strategien «doble/halvere», illustrert i Heftet. Algebraisk:
$\frac{1}{2}a \cdot 2b = \frac{1}{2} \cdot 2 \cdot ab = 1 \cdot ab = ab$.
b) er et spesialtilfelle av tredje kvadratsetning. Algebraisk:
$(10a + b)(10a - b) = (10a)^{2} - b^{2}$ ved tredje kvadratsetning.
Eventuelt kan man vise mellomregning.

### Forklare og gi eksempler på de ulike betydningene av brøk: del av hel/enhet, del av antall, tall og forhold

#### Grunnleggende: Forklare og gi eksempler på de ulike betydningene av brøk

1. Forklar og gi eksempler på hva som menes med brøk som

   a. del av en hel eller del av en enhet

   b. del av et antall

   c. tall

   d. forhold

#### Middels: Lage oppgaver og identifisere situasjoner med de ulike betydningene av brøk

1. Lag oppgaver der brøk opptrer i betydningen

   a. del av en hel eller del av en enhet

   b. del av et antall

   c. tall

   d. forhold

2. Under ser du noen situasjoner som involverer brøkbegrepet. Avgjør og
   begrunn i hvert tilfelle hvilke(n) betydning av brøk det er snakk
   om.

   a. To femdeler av Norges befolkning spiser taco hver fredag.

   b. Prisen på en vare har gått ned med én tredel.

   c. To femdeler av Norges landareal er beiteområder for rein.

   d. En gressklipper bruker $0,3$ liter bensin på $20$ minutter. Hvor
   lenge kan man klippe gress på en halv liter?

   e. Fem personer deler syv boller likt mellom seg.

   f. Hvor mange glass på én tredels liter kan man fylle med
   $2\frac{1}{2}$ liter vann?

##### Løsningsforslag

2. \
a. Del av antall. (Bak brøkene er det antall, nemlig (deler av) Norges befolkning.)
bTall. (Opprinnelig pris er p. Da er ny pris $\frac{2}{3}p$ og avslaget $\frac{1}{3}p$.) (Man kan selvsagt krangle og si dette er del av antall, der prisen er et antall kroner, men det er en litt rar tolkning.)
c. Del av helhet. (Landareal som helhet.) Kan også tenke at arealet er tallfestet; da er vi samme situasjon som over.
d. Forhold. ($0.3 = \frac{3}{20}=\frac{?}{30}$. Altså 0,3 liter per 20 min angir et forhold; og forhold er brøk.)
e. Tall (7∶5) eller del av hel (syv boller som hel, eller hver bolle som helhet – har syv slike).
f. Tall. (2 1/2 ∶1/3.)

### Forklare hvordan de reelle tallene er bygd opp

#### Grunnleggende: Forklare hva hele, rasjonale og irrasjonale tall er

1. Forklar hva hele, rasjonale og irrasjonale tall er. (Husk at målet
   med forklaringsoppgaver er 1) at _du_ skal forstå, og 2) at du skal
   forstå slik at du kan _hjelpe andre å forstå_.)

#### Middels: Forklare hvordan de reelle tallene er bygd opp av naturlige, hele, rasjonale og irrasjonale tall

1. Forklar hva naturlige, hele, rasjonale og irrasjonale tall er.
   Forklar og illustrer deretter hvordan disse til sammen utgjør de
   reelle tallene.

##### Løsningsforslag

**Naturlige tall**: $\mathbb{N} = \{ 1,\ 2,\ 3,\ \ldots\}$.
Telletallene.

**Hele** **tall** (eller heltall):
$\mathbb{Z} = \{\ldots,\  - 2,\  - 1,\ 0,\ 1,\ 2,\ \ldots\}$.
Telletallene, null og de negative telletallene.

**Rasjonale tall**: $\mathbb{Q =}$ alle $\frac{a}{b}$, der $a$ og $b$ er
i ℤ. Brøkene, som inkluderer heltallene.

**Irrasjonale tall**: Tallene som _ikke_ er brøker.

**Reelle tall**: Hele tallinja. Det vil si samlinga av alle mengdene
over.

Figuren viser hvordan de reelle tallene (hele figuren) er satt sammen de
øvrige tallmengdene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/err.png)

### Utvide og forkorte brøker

#### Grunnleggende: Utvide og forkorte brøker

1. Alfa s. 105

#### Middels: Utvide og forkorte brøker, og forklare og illustrere hvorfor dette gir brøker av lik verdi

1. Alfa s. 105

2. Vis ved hjelp av illustrasjon og ordforklaring hvorfor utviding og
   forkorting gir likeverdige brøker.

##### Løsningsforslag

Figuren til venstre viser $\frac{2}{3}$ (kvadratet er $1$). Ved å dele
hver tredel i fire, får vi $3 \cdot 4$ små deler. De to skraverte
tredelene utgjør da $2 \cdot 4$ tolvdeler. Altså:
$\frac{2}{3} = \frac{2 \cdot 4}{3 \cdot 4} = \frac{8}{12}$. Det samme
gjelder opplagt andre vei, altså forkorting. At teller og nevner har
felles faktor, betyr bare at det finnes et mindre antall kakestykker
kvadratkaka kan deles i, som fortsatt gir akkurat like stor dele av hele
kaka.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image4.png){width="5.2659722222222225in"
height="2.2843307086614173in"}

### Utføre addisjon og subtraksjon med brøk

#### Grunnleggende: Utføre addisjon og subtraksjon med brøk

1. Alfa s. 108. Bare beregningene, ikke lage regnefortellinger og
   konkretiseringer.

#### Middels: Utføre addisjon og subtraksjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

1. Alfa s. 108.

2. Velg en addisjon og en subtraksjon av brøker med ulike nevnere.
   Forklar og illustrer løsningen. Pass på at forklaring og
   illustrasjon viser _hvorfor,_ ikke bare _hva_ du gjør.

##### Løsingsforslag

Problemet er at ulike deler ikke uten videre kan adderes, for eksempel
for $\frac{1}{4} + \frac{2}{3}$. Vi må finne en mindre inndeling som lar
oss telle _både_ 4- og 3-deler. Hvis vi deler firedelene i tre (eller
tredelene i fire), får vi til dette. Vi _utvider_ altså til det som (av
ganske åpenbare årsaker) heter _fellesnevner._ Vi kan da støtte oss i en
figur som den over, med kvadratene, eller vi kan illustrere ved hjelp av
tallinjer. Se under. Vi deler firedelene i tre, og ser at
$\frac{1}{4} = \frac{3}{12}$, og $\frac{2}{3} = \frac{8}{12}$. Tolvdeler
er glade i hverandre, så nå er det bare å dure i vei:
$\frac{3}{12} + \frac{8}{12} = \frac{11}{12}$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image5.png)

### Utføre multiplikasjon med brøk

#### Grunnleggende: Utføre multiplikasjon med brøk

1. Alfa s. 119. Kun beregningene på grunnleggende.

   a. 1.41 a, b, c og d

   b. 1.42

   c. 1.45

#### Middels: Utføre multiplikasjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

1. Alfa s. 119

   a. 1.41 a, b, c og d

   b. 1.42

2. Ta utgangspunkt i de tre multiplikasjonene $7 \cdot \frac{4}{5}$,
   $\frac{2}{3} \cdot 12$ og $\frac{2}{3} \cdot \frac{4}{5}$.

   a. Forklar i hvert tilfelle hvordan vi kan forstå eller tolke
   multiplikasjonen.

   b. Gi en passende kontekst til hver multiplikasjon. (Lag gjerne
   flere kontekster slik at flere av betydningene av brøk dekkes.)

   c. Vis ved illustrasjon og ordforklaring _hvorfor_ vi regner som vi
   gjør. Forsøk å knytte forklaringene til kontekstene.

3. Vis ved hjelp av ordforklaring og illustrasjon at brøkmultiplikasjon
   er kommutativ.

##### Løsningsforslag

2. \
a. Syv kopier av 4/5. to tredeler av tolv. To tredeler av 4/5.
b. Syv flasker, hver med 4/5 liter vann i. 2/3 av en strekning på 12 meter. Drikker 2/3 av ei av flaskene med 4/5 liter vann i.
c. Heftet.

### Utføre divisjon med brøk

#### Grunnleggende: Utføre divisjon med brøk

1. Alfa s. 119. Kun beregningene på grunnleggende.

   a. 1.41 e, f og g

   b. 1.46

#### Middels: Vise ved hjelp av generisk eksempel hvorfor regneregelen for divisjon med brøk er som den er

1. Forklar ved hjelp av et generisk eksempel hvorfor divisjon med en
   brøk svarer til å gange med den omvendte brøken.

##### Løsningsforslag

Heftet.

#### Avansert: Forklare ved hjelp av kontekst (både målings- og delingsdivisjon) hvorfor regneregelen for divisjon med brøk gir mening

1. Velg en divisjon med brøk.

   a. Lag en passende kontekst som gir _målingsdivisjon_. Bruk
   konteksten til å forklare og illustrere hvorfor delingsregelen
   er som den er.

   b. Lag en passende kontekst som gir _delingsdivisjon_. Bruk
   konteksten til å forklare og illustrere hvorfor delingsregelen
   er som den er.

##### Løsningsforslag

Heftet.

### Utføre formell omforming av brøk

#### Avansert: Utføre formell omforming av brøk

1. Regn ut.

   a. $\frac{3}{2}\left( 7 + \frac{3\  + \ \frac{1}{5}}{\frac{2}{3}} \right) - 1$

   b. $\frac{\left( \frac{4}{7}\  \cdot \ 2\ \frac{3}{5} \right)\  - \ 3}{\frac{2}{3}} + 8$

   c. $\frac{\frac{4}{3}\  + \ 5}{\frac{3}{4}\  + \ \frac{3}{5}} + \frac{7}{2}\left( 1 - \frac{8}{3} \right)$

   d. $\left( \frac{\left( 2\ \ :\ \frac{2}{3} \right)\  \cdot \ \frac{3}{2}}{1\  + \ \frac{3}{2}} - \frac{4}{5} \right) \cdot (\frac{4}{5} - 2)$

##### Løsningsforslag

1. \
a.
$$
\begin{aligned}
\frac{3}{2}\left( 7 + \frac{16}{5} \cdot \frac{3}{2} \right) - 1
& = \frac{3}{2} \cdot \frac{35 + 24}{5} - 1
\\
& = \frac{177}{10} - \frac{10}{10}
\\
& = \frac{167}{10}
\end{aligned}
$$
b.
$$
\begin{aligned}
\frac{4 \cdot 13-105}{7 \cdot 5} \cdot \frac{3}{2} + 8
&
= {\frac{53}{7 \cdot 5} \cdot \frac{3}{2} + 8}
\\
&
= {\frac{-159\cdot 3}{7\cdot 5\cdot 2} + \frac{560}{7\cdot 5\cdot 2}}
\\
& = \frac{401}{70}
\end{aligned}
$$
c.
$$
\begin{aligned}
\frac{19}{3} \cdot \frac{20}{27} + \frac{7}{2} \cdot \left( - \frac{5}{3} \right)
 &
 =\frac{380}{81} - \frac{35}{6}
\\
&= \frac{760}{162} - \frac{945}{162}
\\
& = - \frac{185}{162}
\end{aligned}
$$
d.
$$
\begin{aligned}
{\left( \left( 2 \cdot \frac{3}{2} \cdot \frac{3}{2} \right) \cdot \frac{2}{5} - \frac{4}{5} \right) \cdot \left( - \frac{6}{5} \right)
}
&
= {\left( \frac{9}{5} - \frac{4}{5} \right) \cdot \left( - \frac{6}{5} \right)
}
\\
& = {- \frac{6}{5}}
\end{aligned}
$$

### Forklare begrepet og regne med desimaltall

#### Grunnleggende: Beskrive desimaltall med hensyn til posisjonssystemet og brøkbegrepet

1. Utdyp og forklar: _desimaltall er en skrivemåte for brøker der
   nevneren er en potens av ti._

2. Forklar hva $257,1208$ betyr ved å vise til hvordan
   posisjonssystemet er bygd opp, og å skrive tallet på utvidet form.

3. Alfa s. 139

   a. 1.65

   b. 1.66

   c. 1.67

##### Løsningsforslag

3. s. 139
a. 165: Tideler er (ti ganger) større enn hundredeler. 0,1 er én tidel. 0,17 er én tidel og syv hundredeler (altså mer enn én tidel). 0,2 er to tideler (altså mer enn det igjen).
b.  1.66: \
1,20 \| 2,05 \| 1,008 \| 0,65 \| 3,204
c.  1.67
   1. $1\frac{7}{10} = 1,7$
   2. $\frac{4}{10} = 0,4$
   3. $\frac{2}{10} + \frac{3}{100} = 0,23$
   4. $5\frac{6}{100} = 5,06$
   5. $\frac{4}{100} = 0,04$
   6. $\frac{23}{10} = 1,3$
   7. $\frac{80}{10\ 000} = 0,008$

#### Middels: Forklare hvordan man kan regne med desimaltall med hensyn til posisjonssystemet og brøkbegrepet

1. Alfa s. 140

   a. 1.68

   b. 1.69

   c. 1.70

##### Løsningsforslag

1. Alfa s. 140

    a.  1.68

$2 \cdot 0,4$ er to kopier av $0,4$.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image6.png)
$0,4 \cdot 3$ er fire tideler av tre.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image7.png)
$0,7 \cdot 0,4$ er syv tideler av fire tideler.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image8.png)
b.  1.69
$$
3 \cdot 0,2 = 3 \cdot \frac{2}{10} = \frac{6}{10} = 0,6
$$
$$
40 \cdot 0,006 = 40 \cdot \frac{6}{1000} = \frac{24 \cdot 10}{100 \cdot 10} = \frac{24}{100} = 0,24
$$
$$
21,72 \cdot 0,3 = \left( 2172 \cdot \frac{1}{100} \right) \cdot \left( 3 \cdot \frac{1}{10} \right) = (2172 \cdot 3) \cdot \left( \frac{1}{10} \cdot \frac{1}{100} \right) = \frac{2172 \cdot 3}{1000}$$
$$
0,000943\ :0,0023 = \frac{943 \cdot 10^{6}}{23 \cdot 10^{4}} = \frac{943}{23} \cdot \frac{1}{100} = \frac{41}{100} = 0,41
$$

### Gjøre om mellom brøk og desimaltall

#### Grunnleggende: Forklare og gi eksempler på de tre typene desimaltall, og gjengi hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

1. Forklar og gi eksempler på endelig, periodisk og uendelig
   ikke-periodisk desimaltall.

2. Hvilke brøker svarer til endelige og hvilke svarer til periodiske
   desimaltall?

#### Middels: Gjøre om mellom brøk og desimaltall med endelig desimalutvikling

1. Gjør om til desimaltall. Fremgangsmåte, strategi eller begrunnelse
   for omgjøringen må komme tydelig frem.

+----------------------+-----------------------+-----------------------+
| a\. $\frac{6}{5}$    | b\. $\frac{4}{15}$    | c\. $\frac{7}{2}$     |
+----------------------+-----------------------+-----------------------+
| d\. $\frac{12}{30}$  | e\.  $\frac{14}{450}$ | f\. $\frac{3}{40}$    |
+----------------------+-----------------------+-----------------------+

1. Gjør om til brøk maksimalt forkortet brøk. Fremgangsmåte, strategi
   eller begrunnelse for omgjøringen må komme tydelig frem.

   a. $0,21$

   b. $0,0202$

   c. $3,333$

   d. $0,8$

#### Avansert: Gjøre om mellom brøk og desimaltall med periodisk desimalutvikling

1. Alfa s. 140.

   a. 1.73

   b. 1.74

2. Gjør om til brøk.

   a. $0,\overline{45}$

   b. $0,0\overline{45}$

   c. $0,\overline{123}$

   d. $0,123\overline{45}$

   e. $1,001001001\ldots$

3. Gjør om til brøk.

   a. $0,111\ldots$

   b. $0,222\ldots$

   c. $0,333\ldots$

   d. Og så videre.

##### Løsningsforslag

2. Gjør om til brøk.
a.  $0,\overline{45}$
$$
\begin{aligned}
100x
& = 45,\overline{45}
\\
-x
&  =
-0,\overline{45}
\\
\Rightarrow 99x
& = 45
\\
x & = \frac{45}{99}
= \frac{5}{11}
\end{aligned}
$$

b.  $0,0\overline{45}$

$$
\begin{aligned}
1000x
&= 45,\overline{45}
\\
10x
&= 0,\overline{45}
\\
\Rightarrow 990x
& = 45
\\
x
& = \frac{45}{990} = \frac{1}{22}
\end{aligned}$$

c.  $0,\overline{123}$

$$
1000x - x = 999x = 123 \Rightarrow x = \frac{123}{999} = \frac{41}{333}
$$

d.  $0,123\overline{45}$

$$
\begin{aligned}
100\ 000x
& = 12\ 345,\overline{345}
\\
100x
& = 12,\overline{345}
\\
\Rightarrow 99\ 900x
& = 12\ 333
\\
x
& = \frac{12\ 333}{99\ 900} = \frac{4\ 111}{33\ 300}
\end{aligned}$$

e.  $1,001001001\ldots$

$$
\begin{aligned}
100\ 000x
& = 100\ 100,\overline{100}
\\
100x
& = 100,\overline{100}
\\
99\ 900x
& = 100\ 000
\\
x
& = \frac{100\ 000}{99\ 900} = \frac{1000}{999}
\end{aligned}$$

Alternativt kunne vi sett bort fra eneren, gjort trikset på
$0,00\overline{100}$, og lagt til $1$ etterpå.

3. Gjør om til brøk.

    a.  $0,111\ldots$ $= \frac{1}{9}$

    b.  $0,222\ldots = \frac{2}{9}$

    c.  $0,333\ldots = \frac{3}{9}$

    d.  Og så videre. $0,aaa\ldots = \frac{a}{9}$ for
        $a \in \{ 0,\ 1,\ \ldots,\ 9\}$. Det betyr spesielt at
        $0,999\ldots = \frac{9}{9} = 1.$

### Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

#### Middels: Avgjøre og begrunne (uten å utføre divisjon) om en gitt brøk er endelig eller periodisk

1. Alfa s. 140:

   a. 1.71

   b. 1.73 (avgjør uten å regne hva slags desimaltall brøken svarer
   til)

2. Hvis mulig, utvid eller forkort brøken slik at det klart fremgår at
den svarer til et endelig desimaltall. Begrunn ellers hvorfor dette ikke lar seg gjøre.
   1. $\frac{14}{35}$
   2. $\frac{12}{36}$
   3. $\frac{12}{36}$
   4. $\frac{3}{16}$
   5. $\frac{18}{45}$
   6. $\frac{6}{18}$

##### Løsningsforslag

2. \
   1. $\frac{14}{35}  = \frac{2}{5} = \frac{4}{\mathbf{10}}$
   2. $\frac{12}{36} = \frac{1}{\mathbf{3}}$
   3. $\frac{7}{150} = \frac{7}{\mathbf{3} \cdot 50}$
   4. $\frac{3}{16} = \frac{3 \cdot 5^{4}}{2^{4} \cdot 5^{4}} = \frac{3 \cdot 5^{4}}{\mathbf{10\ 000}}$
   5. $\frac{18}{45}= \frac{2}{5} = \frac{4}{\mathbf{10}}$
   6. $\frac{6}{18} = \frac{1}{\mathbf{3}}$
Det er valgt litt dumme eksempler her, da 3 ser ut til å være
eneste faktor i nevner som gjør at brøker ikke er endelige. Slik er det
ikke: Det er hvis, og bare hvis, 2 og 5 er de eneste primfaktorene i den
maksimalt forkorta nevneren, at brøken svarer til et endelig
desimaltall. _Alle andre faktorer_ i den maksimalt forkorta nevneren,
gir _ikke_ endelig desimaltall.

#### Avansert: Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

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

### Utføre og begrunne prosentregning

#### Grunnleggende: Finne prosentdel av et tall, uttrykke tall som prosentdel av et hele, og finne det hele når del og prosentdel er gitt

1. Alfa s. 143

   a. 1.77

   b. 1.78

   c. 1.79

   d. 1.80

   e. 1.81

   f. 1.82

   g. 1.83

   h. 1.84

   i. 1.85

2. Alfa s. 144

   a. 1.87

   b. 1.88

   c. 1.89

   d. 1.90

#### Middels: Utføre og begrunne beregningene over

1. Alfa s. 143--144:

   a. 1.77

   b. 1.91

2. Velg egne tall. Finn, ved hjelp av flere strategier, og begrunn dem
   i hvert tilfelle

   a. en prosentdel av et tall (hva er $x$ prosent av $y$?)

   b. en del av et tall uttrykt som prosent del (hvor stor prosentdel
   utgjør $x$ av $y$?)

   c. det hele når del og prosentdel er kjent (hvis $x$ utgjør $y$
   prosent, hva er da $100$ %?)

### Løse (ukjente) problemer knyttet til brøk, prosent (og desimaltall)

#### Avansert: Løse (ukjente) problemer knyttet til brøk, prosent (og desimaltall)

1. Alfa s. 143: 1.86

2. To butikker selger i utgangspunktet en vare til samme pris. Den ene
   butikken setter opp varen med 10 % for siden å sette den ned med 10
   %. Den andre butikken gjør motsatt: først ned 10 %, siden opp 10 %.

   a. Hvor lønner det seg å handle?

   b. Generaliser problemstillingen og løs den.

3. Blant en gruppe mennesker er 60 % gutter. Når det kommer 5 nye
   jenter, andelen 50/50. Hvor mange var de i utgangspunktet?

4. To kraner står over ei bøtte. Den ene krana fyller halve bøtta på en
   time. Den andre fyller en firedel på samme tid. Hvor lang tid tar
   før bøtta er full om begge kranene åpnes på likt?

5. I testamentet gir tante Beate halvparten av formuen sin til Røde
   Kors. Hennes tre nevøer skal dele resten. Per skal bare få to
   tredeler av det hver av de to andre nevøene skal få, etter som han
   ikke besøkte henne den siste tiden. Hvor stor andel av formuen skal
   Per ha?

6. Her er et snedig triks for å finne en brøk som ligger mellom to
   andre brøker: Lag brøken der teller er summen av de to brøkenes
   tellere, og nevneren summen av de to brøkenes nevnere. Eksempel:
   Brøken $\frac{2\  + \ 4}{3\  + \ 5}$ ligger mellom $\frac{2}{3}$ og
   $\frac{4}{5}$. Vis at trikset alltid funker. (Hint: Det kan lønne
   seg å bruke at dersom $\frac{2}{3} < \frac{4}{5}$, så er
   $2 \cdot 5 < 3 \cdot 4$.)

### Utføre addisjon og subtraksjon med negative tall

#### Grunnleggende: Utføre addisjon og subtraksjon med negative tall

1. Regn ut.

   a. $12 - ( - 3)$

   b. $- 12 + ( - 3)$

   c. $- ( - 12 + ( - 3))$

   d. $1 - ( - 12 + ( - 3))$

   e. $(5 - 7) - ( - 3 + 2)$

   f. $- 20 - ( - 13)$

   g. $- \left( ( - 23) - ( - 3) \right) - (( - 81) - ( - 19))$

   h. $\left( ( - 23) - 3 \right) - (( - 81) + ( - 19))$

#### Middels: Vise hvorfor regnereglene for negative tall gir mening

1. Lag regnetabeller som med utgangspunkt i de naturlige tallene, viser
   hvordan addisjon og subtraksjon må oppføre seg for å gi en
   meningsfull utvidelse til negative tall.

2. Forklar med ord hvordan addisjon og subtraksjon av negative tall må
   oppføre seg med utgangspunkt i beskrivelsen av (hele) negative tall
   som _motsatte av de positive (hele) tallene_.

3. Illustrer forklaringa fra forrige oppgave på tallinjer.

### Utføre multiplikasjon og divisjon med negative tall

#### Grunnleggende: Utføre multiplikasjon og divisjon med negative tall

1. Regn ut.

   a. $- 3 \cdot 5$

   b. $- 3 \cdot (5 - 1)$

   c. $- 3 \cdot \left( - (5 - 1) \right)$

   d. $2 \cdot \frac{12 - 15}{- 2}$

   e. $- \frac{3}{2} \cdot \left( 5 - \frac{4}{- 9} \right)$

   f. $\left( ( - 18) \cdot ( - 2) \cdot \left( - \frac{1}{3} \right) \right)\ :( - 12)$

#### Middels: Vise hvorfor regnereglene for multiplikasjon og divisjon med negative tall gir mening

1. Lag en multiplikasjonstabell for $0$--$10$. Utvid tabellen til
   $- 10$ i begge retninger, og forklar kort hvordan mønsteret må
   fortsette for å gi en meningsfull utvidelse.

2. Ta utgangspunkt i beskrivelse av negative tall som _motsatte av de
   positive tallene,_ og tolkninga av multiplikasjonen $a \cdot b$ som
   $b$ gjentatt (eller kopiert) $a$ ganger. Beskriv med ord hva som da
   er fornuftige tolkninger av $a \cdot ( - b)$, $( - a) \cdot b$ og
   $( - a) \cdot ( - b)$. Du må gjerne bruke generiske talleksempler i
   stedet for bokstaver.

3. Illustrer forklaringa fra oppgaven over på tallinjer.

4. Siden et tall ganger null er null, og et tall minus seg selv er
   null, må for eksempel $3 \cdot (2 - 2)$ være $0$. Bruk dette til å
   vise at

   a. $a \cdot (b - b)$ gir at produktet av et positivt og et negativt
   tall må være negativt, og at

   b. $- a \cdot (b - b)$ gir at produktet av to negative tall må være
   positivt. Du kan godt bruke generiske talleksempler.

### Gjengi betydningen av potensuttrykk, og regne med potenser

#### Grunnleggende: Gjengi hva potensuttrykk betyr når eksponenten er et naturlig tall (tre tilfeller: _eksponent_ $> 1$, _eksponent_ $= 1$ og _eksponent_ $= 0$), når den er et negativt tall og når den er en brøk

1. Hva betyr potensuttrykkene? Der det er nødvendig, angi også hvilke
   tall $a$, $n$ og $m$ betydningen gjelder for.

+----------------------+-----------------------+-----------------------+
| a\. $a^{n}$          | b\. $a^{1}$           | c\. $a^{0}$           |
+----------------------+-----------------------+-----------------------+
| d\. $a^{- n}$        | e\.$a^{\frac{n}{m}}$  |                       |
+----------------------+-----------------------+-----------------------+

1. Alfa s. 239

   a. 3.24

#### Middels: Regne med potenser med heltallige (som inkluderer naturlige) eksponenter, og begrunne beregningene ved hjelp av potensreglene

1. Alfa s. 239--241 (Det er ikke meningen å gjøre alt! Øv på det du
   trenger å øve på.)

   a. 3.23

   b. 3.25

   c. 3.26

   d. 3.27

   e. 3.29

   f. 3.32

   g. 3.38

2. Begrunn avgjørelsene deres for _hvert_ alternativ i oppgavene under.
   (Ikke for vår, men for din egen lærings skyld.)

   a. Hvilke(t) alternativ er $4^{7} \cdot 2^{4}$ lik?

+-------+-----------+
| A     | $4^{11}$  |
+-------+-----------+
| B     | $8^{6}$   |
+-------+-----------+
| C     | $8^{11}$  |
+-------+-----------+
| D     | $4^{9}$   |
+-------+-----------+
| E     | $2^{18}$  |
+-------+-----------+

b. Hvilke(t) alternativ er $2^{16} + 2^{16} + 2^{16} + \ldots + 2^{16}$
(16 ledd) lik?

+-------+-----------------------+
| A     | $4^{10}$              |
+-------+-----------------------+
| B     | $2^{19}$              |
+-------+-----------------------+
| C     | $16^{2}$              |
+-------+-----------------------+
| D     | $2^{5} \cdot 8^{5}$   |
+-------+-----------------------+
| E     | $2^{32}$              |
+-------+-----------------------+

c. Hvilke(t) alternativ er $10^{12}\ :20^{6}$ lik?

+-------+-----------------------------------+
| A     | $\frac{10^{12}}{2 \cdot 10^{6}}$  |
+-------+-----------------------------------+
| B     | $1$                               |
+-------+-----------------------------------+
| C     | $5^{6}$                           |
+-------+-----------------------------------+
| D     | $10^{(12 - 6)}\ :2^{6}$           |
+-------+-----------------------------------+
| E     | $25^{3}$                          |
+-------+-----------------------------------+

d. Hvilke(t) alternativ er $9^{- 6} \cdot 3^{12}$ lik?

+-------+-----------------------------------+
| A     | $9^{4}$                           |
+-------+-----------------------------------+
| B     | $1$                               |
+-------+-----------------------------------+
| C     | $81^{- 3} \cdot 81^{3}$           |
+-------+-----------------------------------+
| D     | $9^{- 6 + 6}$                     |
+-------+-----------------------------------+
| E     | $\frac{1}{6^{9}} \cdot 3^{12}$    |
+-------+-----------------------------------+

#### Avansert: Regne med potenser med rasjonale (som inkluderer heltallige) eksponenter, og begrunne beregningene ved hjelp av potensreglene

1. Alfa s. 239--341

   a. 3.28

   b. 3.37

2. Regn ut ved hjelp av potensregler.

   a. $2 \cdot \sqrt{100} \cdot 5^{- 1} \cdot 8^{- \frac{2}{3}}$

   b. ${\sqrt[13]{5^{\frac{2}{3}} \cdot 5^{\frac{3}{2}}}}^{\ 6}$

   c. $\frac{\left( \frac{2}{5}\  \cdot {\ 125}^{\frac{2}{5}} \right)^{5}}{2}$

3. Begrunn ved hjelp av potensregler at
   $\sqrt[m]{a^{n}} = {\sqrt[m]{a}}^{n}$.

4. Gjør om til et rotuttrykk.

$\frac{a^{3 + n} \cdot b^{\frac{2}{3}}}{(ab)^{\frac{n}{3}}}$

5. Avgjør og begrunn om uttrykkene har lik verdi.

   a. $\sqrt{3} \cdot 2^{4}$ og $\sqrt{6} \cdot {\sqrt{2}}^{7}$

   b. $81^{\frac{2}{4}}$ og
   $\left( \frac{18}{4} \cdot 2 \right)^{\frac{1}{2}}$

   c. $2^{3} \cdot 12^{- \frac{3}{2}}$ og
   $\left( {\sqrt[3]{3}}^{2} \right)^{- 1}$

   d. $\sqrt{3} \cdot 2^{4}$ og
   $\frac{3\  \cdot {\ \sqrt{2}}^{9}}{\sqrt{6}}$

   e. $\frac{4^{10}\  \cdot {\ 10}^{2}}{32^{\frac{10}{4}}}$ og
   $2^{10} \cdot 10^{2}$

### Utlede potensreglene

#### Middels: Utlede potensreglene for heltallige eksponenter

1. Utled potenssammenhengene under med utgangspunkt i at
   $a^{n} = a \cdot a \cdot \ldots \cdot a$ for $n$ $a$-er. Det er ok å
   gjøre utledningene ved hjelp av talleksempler, så lenge disse
   fungerer som _generiske_ eksempler. Du bør likevel tilstrebe
   fortrolighet med bokstaver (i matte 2 er det ingen bønn 😉).

+---+------------------------------------------+
| A | $a^{n} \cdot a^{m} = a^{n + m}$          |
+---+------------------------------------------+
| B | $a^{n} \cdot b^{n} = (ab)^{n}$           |
+---+------------------------------------------+
| C | $a^{n \cdot m} = \left(a^{n}\right)^{m}$ |
+---+------------------------------------------+
| D | $\frac{a^{n}}{a^{m}} = a^{n - m}$        |
+---+------------------------------------------+
| E | $a^{0} = 1$                              |
+---+------------------------------------------+
| F | $a^{-n} = \frac{1}{a^{n}}$               |
+---+------------------------------------------+

#### Avansert: Utlede potensreglene for rasjonale (som inkluderer heltallige) eksponenter

1. Utled potenssammenhengene under med utgangspunkt i at
   $a^{n} = a \cdot a \cdot \ldots \cdot a$ for $n$ $a$-er. Det er ok å
   gjøre utledningene ved hjelp av talleksempler, så lenge disse
   fungerer som _generiske_ eksempler. Du bør likevel tilstrebe
   fortrolighet med bokstaver (i matte 2 er det ingen bønn 😉).

+---+-------------------------------------------+
| A | $a^{n} \cdot a^{m} = a^{n + m}$           |
+---+-------------------------------------------+
| B | $a^{n} \cdot b^{n} = (ab)^{n}$            |
+---+-------------------------------------------+
| C | $a^{n \cdot m} = \left(a^{n}\right)^{m}$  |
+---+-------------------------------------------+
| D | $\frac{a^{n}}{a^{m}} = a^{n - m}$         |
+---+-------------------------------------------+
| E | $a^{0} = 1$                               |
+---+-------------------------------------------+
| F | $a^{-n} = \frac{1}{a^{n}}$                |
+---+-------------------------------------------+
| G | $a^{\frac{1}{m}} = \sqrt[m]{a}$           |
+---+-------------------------------------------+
| H | $a^{\frac{n}{m}} = \sqrt[m]{a^{n}}$       |
+---+-------------------------------------------+
| I | $\sqrt[m]{a^{n}} = {\sqrt[m]{a}}^{\ n}$   |
+---+-------------------------------------------+

## 24.04

### Forklare hva et posisjonssystem er

#### Grunnleggende

Forklar kort hva et posisjonssystem er. Gi eksempler fra base ti, tre, to og elleve.

##### Vurderingskriterier

Må få frem ideen om at sifrenes posisjon avgjør verdien de står for, og at denne verdien avhenger av hvilken gruppering vi velger -- hvilken base eller grunntall vi har. Må også ha med eksempler.

#### Middels

1. Forklar kort hva et posisjonssystem er.

2. Gjør om $289_{ti}$ til base tre,
3. $222_{fire}$ til base åtte uten å regne ut i base ti først.

##### Vurderingskriterier

Som grunnleggende + omgjøringene. Det må gå frem hvordan omgjøringene er gjort.

### Avansert

1. Gjør om  $212{tre}$ til base seks uten å først regne ut i base ti.
2. Regn ut i den aktuelle basen:
a.  $1001001{to} - 100110_{to}$  

b.  $43_{syv} \cdot 23_{syv}$

##### Vurderingskriterier

Som middels + beregninger. Disse må være ført i den aktuelle basen.

### Beskrive situasjoner med hensyn til additive strukturer

#### Grunnleggende

1. Beskriv tre situasjoner som har addisjon som modell med henholdsvis økning, forening og additiv sammenlikning som struktur.

2. Velg én av situasjonene over. Omformuler den slik at det er rimelig å si at den har samme struktur, men med subtraksjon som modell.

##### Vurderingskriterier

Additive strukturer s. 52 i Alfa.

### Middels

Avgjør og begrunn hvilken additiv struktur situasjonene har. Angi både addisjons- og subtraksjonsstykket som passer i hvert tilfelle.

1. I hver situasjon under, argumenter for to additive strukturer det er rimelig å si at situasjonen er et eksempel på. Oppgi i hvert tilfelle både addisjons- og subtraksjonsstykket som passer.
a. Henrik hiver to dartpiler. Første pil treffer $18$, andre pil $17$. Hvor mange poeng fikk han?  
b. André samler enhjørning-klistremerker. En pakke klistremerker koster $349$, men stakkars André har bare $200$ kroner. Hvor mye mer trenger han for å få råd?
a. På en uke har en solsikke inntil husveggen vokst til 212 cm. Hvor mange centimeter må den vokse før den når husveggen på 240 cm?
b. André fant 12 kroner i bukselomma. I jakkelomma fant han 50. Hvor mye mer fant han i jakka?  
2. Lag en oppgave til $150 + {\_\_} =225$ med additiv sammenlikning som struktur.

##### Vurderingskriterier

1. To struktur må angis med rimelig begrunnelse. Begge mulige regnestykker må med.
a. kan være forening, økning eller komplettering: 18 + 17 = \_\_ eller \_\_ -- 17 = 18.
b. kan være komplettering, økning eller sammenlikning: 200 + \_\_ = 349 eller 349 -- 200 = \_\_.
2. Oppgaven må rimelig kunne sies å være et eksempel på sammenlikning.

### Beskrive situasjoner med hensyn til multiplikative strukturer

#### Grunnleggende

1. Gjengi kort med et eksempel til hver, hva som menes med de to multiplikative strukturene rate og kombinatorisk situasjon.

2. Gjengi kort med et eksempel til hver, hva som menes med de to typene divisjon delingsdivisjon og målingsdivisjon.

##### Vurderingskriterier

Multiplikative strukturer s. 58 i Alfa.

#### Middels

1. Avgjør og begrunn hvilken multiplikativ struktur situasjonene svarer til.

a.  Antall Twist André spiser på $6,5$ minutter når han spiser $12$ Twist i minuttet.
b.  Arealet av en rektangulær terrasse med sider $2,3$ og $4,7$ meter.
c.  En strekning på $12 \ \text{km}$ er delt opp i $4$ etapper.  
2. Ta utgangspunkt i situasjon c. Legg til nødvendig informasjon, og omformuler på to måter: slik at du lager én divisjonsoppgave med målingsdivisjon og én med delingsdivisjon. Begrunn hvilken som er hva.  

##### Vurderingskriterier

Avgjørelsene må begrunnes kort.

1. \
a. er rate.
b. er rektangulært arrangement.
c. er like grupper.
2. \

- Målingsdivisjon: hvor mange 3 km etapper på 12 km?
- Delingsdivisjon: hvor lange etapper når 12 km deles i fire etapper?

### Bruke regnestrategier og egenskaper ved regneoperasjonene

#### Grunnleggende

Gjengi kommutativ, assosiativ og distributiv egenskap for addisjon og multiplikasjon.

##### Vurderingskriterier

Gjengi egenskapene.

#### Middels

1. Bruk minst én av egenskapene (kommutativ, assosiativ, distributiv) til å regne $23 \cdot 11$. Vis tydelig hvordan du tenker.

2. Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.
a.  $352 + 61$
b.  $240 : 2,5$
c.  $180 \cdot \frac{4}{3}$

##### Vurderingskriterier

Trengs et par setninger som tydelig får frem hvordan man har tenkt.

1. Nærliggende å distribuere: $23 \cdot 11 + 46 = 23 \cdot (11 + 2) = 23 \cdot (10 + 3)$
2. \
a. Eks. gå via hele 100-ere: $352 + 61 = 352 + 50 + 11$
b. Eks. dele på ti, gange med fire: $240\ :2,5 = (240\ :10) \cdot 4$
c. Eks. finne tredel av 18, gange opp med 4, og deretter med 10.

#### Avansert

1. Velg to passende multiplikasjoner, og illustrer og gi en kort forklaring av distributiv egenskap og kommutativ egenskap.

2. Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.

3. Velg én av strategiene fra 2., og gi en illustrasjon og kort forklaring som viser at strategien alltid funker.

a.  $240 : 2,5$
b.  $180 \cdot \frac{4}{3}$

##### Vurderingskriterier

Få tydelig frem hva man har tenkt.

1. Må velge eksempler som fungerer generisk, det vil si at de får frem at egenskapene gjelder generelt (for positive i alle fall).
2. \
a. Som 2b. og 2c. fra middels
3. Må få frem at strategien er generell (heller ikke her trengs nødvendigvis noe algebra)

### Forklare og gi eksempler på de ulike betydningen av brøk: del av hel/enhet, del av antall, tall og forhold

#### Grunnleggende

Forklar og gi eksempler på hva som menes med brøk som
a. del av en hel eller del av en enhet
b. del av et antall
c. tall
d. forhold

##### Vurderingskriterier

Må gi en kort forklaring. Alfa s. 96-101 og s. 109.

#### Middels

1. Avgjør og begrunn kort hvilken ene betydning av brøk det er naturlig å knytte til situasjonen under.

- André og Henrik skal dele en pose Twist som inneholder $45$ biter. Henrik er en grådig j***l, så i et øyeblikk der André snur seg, rasker han med seg $\frac{2}{3}$ av innholdet og løper.

2. Avgjør og begrunn hvilke to betydninger av brøk det er naturlig å knytte til situasjonen under.

- En rektangulær terrasse måler tre meter den ene veien og to og en halv meter den andre. Arealet av terrassen er da $3 \cdot 2\frac{1}{2}$ kvadratmeter.

3. Lag to oppgaver, og begrunn kort hvorfor de involverer den aktuelle betydningen av brøk.

a. Én oppgave med brøk som del av hel/enhet.
b. Én oppgave med brøk som forhold.

##### Vurderingskriterier

1. Må avgjøre med en kort, fornuftig begrunnelse. _Del av antall_ er rimelig.
2. Må avgjøre med en kort, fornuftig begrunnelse. _Tall_ og _del av enhet (kvadratmeter)_ er rimelig.
3. Må fornuftig kunne sies å involvere de angitte betydningene.

### Forklare hvordan de reelle tallene er bygd opp

#### Grunnleggende: Forklare hva hele, rasjonale og irrasjonale tall er

Gjengi kort hva som menes hele, rasjonale og irrasjonale tall.

##### Vurderingskriterier

Gjengi korrekt. Hele tall: ... -2, -1, 0, 1, 2,.... Rasjonale: brøk med heltallig teller og nevner. Irrasjonale: de som ikke er heltallige brøker.

#### Middels: Forklare hvordan de reelle tallene er bygd opp av naturlige, hele, rasjonale og irrasjonale tall

Forklar kort hva naturlige, hele, rasjonale og irrasjonale tall er, og vis med en illustrasjon hvordan disse til sammen utgjør de reelle tallene.

##### Vurderingskriterier

Som grunnleggende, men med presisering av naturlige også, samt et diagram eller liknende som får frem hvilke mengder som er delmengder av hvilke.

### Utvide og forkorte brøker

#### Grunnleggende: Utvide og forkorte brøker

Finn i hvert tilfelle den likeverdige brøken med lavest mulig heltallig teller og nevner.
a. $\frac{14}{12}$
b. $\frac{2,2}{11}$
c. $\frac{\frac{6}{5}}{2}$

##### Vurderingskriterier

7/6, 1/5, 3/5

#### Middels: Utvide og forkorte brøker, og forklare og illustrere hvorfor dette gir brøker av lik verdi  

1. Hvilke brøker er likeverdige med $\frac{2}{5}$?
a. $\frac{7,5}{9}$
b. $\frac{25}{36}$
c. $\frac{\frac{5}{3}}{2}$
d. $\frac{20}{24}$

2. Lag en illustrasjon som viser tydelig at $\frac{3}{4}$ og $\frac{9}{12}$ er likeverdige.  

##### Vurderingskriterier

1. a, c og d (må ha begrunnelse, det vil si passende utvidelse/forkorting av brøk).
2. Eks. dele kvadrat i firedeler den ene veien, og tredeler den
andre.

### Utføre addisjon og subtraksjon med brøk

#### Grunnleggende: Utføre addisjon og subtraksjon med brøk

Regn ut.
a. $\frac{2}{5} + \frac{7}{3}$
b. $\frac{7}{3} - \frac{3}{4}$

##### Vurderingskriterier

41/15, 19/12

#### Middels: Utføre addisjon og subtraksjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

Regn ut, og gi en forklaring med illustrasjon som viser at beregningen må være riktig.

a. $\frac{2}{5} + \frac{1}{4}$
b. $\frac{5}{6} - \frac{1}{3}$

##### Vurderingskriterier

13/20, 1/2. Illustrasjonen må vise utviding til felles nevner på en forståelig måte.

### Utføre multiplikasjon med brøk

#### Grunnleggende: Utføre multiplikasjon med brøk

Regn ut.
a. $\frac{7}{5} \cdot \frac{4}{5}$
b. $3 \frac{2}{3} \cdot \frac{3}{2}$

##### Vurderingskriterier

28/25, 11/2

#### Middels: Utføre multiplikasjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

1. Forklar ved hjelp av en passende illustrasjon at $5 \cdot \frac{3}{4} = \frac{3}{4} \cdot 5$.

2. Forklar kort ved hjelp av en passende illustrasjon hvorfor vi multipliserer teller med teller og nevner med nevner for å finne produktet av to brøker.  

##### Vurderingskriterier

1. Må vise til struktur, ikke bare at «svarene» er like, slik som i
eks under (feil tall, bare). Kvadratene er 1, grønn del 2/5. Figuren
kan leses som _2/5 gjentatt tre ganger,_ altså 3 ⋅ 2/5. Den kan også
leses som _2/5 av tre,_ altså 2/5 ⋅ 3.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img//tal/24.04media/media/image1.png)

1. Må vise til en figur som for eksempel den under (2/3 ⋅ 4/5):

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img//tal/24.04media/media/image2.png)

### Utføre divisjon med brøk

#### Grunnleggende: Utføre divisjon med brøk

Regn ut.
a. $2\frac{1}{3} : \frac{14}{6}$
b. $\frac{3}{4} : \frac{6}{5}$

##### Vurderingskriterier

1, 5/8

#### Middels: Vise ved hjelp av generisk eksempel hvorfor regneregelen for divisjon med brøk er som den er

Vis ved hjelp av et generisk eksempel hvorfor divisjon med en brøk svarer til multiplikasjon med den omvendte brøken.

##### Vurderingskriterier

Må tolke en brøkdivisjon som brøk over brøk, og utvide. Oppgaven ber om _generisk eksempel._ Poenget er at strukturen må komme frem (som i algebraen under). Å dele på en stambrøk er ikke godt nok. Velger noen algebra, er det ok.
$$\frac{a}{b}\ :\frac{c}{d} = \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{\frac{a}{b} \cdot d/c}{\frac{c}{d} \cdot d/c} = \frac{a}{b} \cdot \frac{d}{c}$$

#### Avansert: Forklare ved hjelp av kontekst (både målings- og delingsdivisjon) hvorfor regneregelen for divisjon med brøk gir mening

Ta utgangspunkt i divisjonen $9 : \frac{2}{3}$. Lag to passende kontekster, og bruk dem til å vise at $9 : \frac{2}{3} = 9 \cdot \frac{3}{2}$.

a. Den ene konteksten skal gi delingsdivisjon.

b. Den andre konteksten skal gi målingsdivisjon.

##### Vurderingskriterier

a. Delingsdivisjon: 9 liter maling rekker til 2/3 vegg (like vegger), hvor mye maling trengs per vegg? Fordeler de 9 literne likt på de to tredelene, som gir 9/2 liter per tredel. Ganger dette opp med tre for å få en hel vegg, altså $9\ :\frac{2}{3} = \frac{9}{2} \cdot 3 = 9 \cdot \frac{3}{2}$.
b. Målingsdivisjon: Hvor mange to-tredels-litere går det på ni liter? Det går tre tredelslitere på én liter, så $9 \cdot 3$ tredeler på ni liter. 2/3 liter er dobbelt så mye, så det går halvparten så mange, altså $9\ :\frac{2}{3} = \frac{9\  \cdot \ 3}{2} = 9 \cdot \frac{3}{2}$.

### Utføre formell omforming av brøk

#### Avansert: Utføre formell omforming av brøk

Regn ut.

a. $((\frac{4}{5} + \frac{1}{\frac{7}{3}}) \frac{1}{43})) \cdot 7 + \frac{4}{5}$
b. $\frac{1}{2} - \frac{\frac{4}{11}((\frac{8}{6} : \frac{1}{3}) + \frac{2}{5})}{\frac{4}{2,5}}$

##### Vurderingskriterier

1, -1/2

### Forklare begrepet og regne med desimaltall

#### Grunnleggende: Beskrive desimaltall med hensyn til posisjonssystemet og brøkbegrepet

Forklar hva $21,203$ betyr. Forklaringa må støtte seg på brøkbegrepet og hvordan posisjonssystemet er bygd opp.

##### Vurderingskriterier

Må peke på posisjonssystemet: \*10 til venstre,
        :10 til høyre. Gir tideler, hundredeler og så videre. Dette
        siste gir at desimaltall er brøker der nevner er tierpotenser.

#### Middels: Forklare hvordan man kan regne med desimaltall med hensyn til posisjonssystemet og brøkbegrepet

1. Det er fort gjort å gjøre denne feilen når man regner med desimaltall: $0,3 \cdot 0,2 = 0,6$. Forklar ved hjelp av posisjonssystemet og/eller brøkbegrepet hvorfor dette er feil.

2. Divisjonen $3,6 : 0,12$ kan gjøres ved å regne $36 : 12$, for deretter å flytte desimalkommaet til riktig plass. Forklar hvordan og hvorfor.

##### Vurderingskriterier

1. Siden vi kan brøkregning, ser vi at $0,3 \cdot 0,2 = \frac{3}{10} \cdot \frac{2}{10} = \frac{3 \cdot 2}{10 \cdot 10} = \frac{6}{100}$. Og seks hundredeler er 0,06.

2. Justeringen fra 3,6 : 0,12 til 36 : 12 er $\frac{3,6}{0,12} \rightarrow \frac{3,6 \cdot 10}{0,12 \cdot 100} = \frac{3,6}{0,12} \cdot \frac{1}{10}$. Svaret vi får er altså en tidel av det vi skal ha, så vi må gange opp med ti (flytte desimaltegnet én plass til høyre).

### Gjøre om mellom brøk og desimaltall

#### Grunnleggende: Forklare og gi eksempler på de tre typene desimaltall, og gjengi hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

Forklar og gi eksempler på hva som menes med endelig desimaltall, periodisk desimaltall og uendelig ikke-periodisk desimaltall.

##### Vurderingskriterier

Må gi passende eksempler og kort, riktig forklaring. _Endelige_ desimaltall har en endelig desimalutvikling; de er et endelig antall ti-, hundre-, tusendeler og så videre. (Eventuelt, er brøkene der nevner kan utvides til tierpotens). _Periodiske_ er uendelige, med siffersekvenser som gjentas i det uendelige (brøkene som maksimalt forkorta har nevner med andre primfaktorer enn to og fem). _Ikke_-_periodiske_, uendelige desimaltall er de irrasjonale tallene (kan ha uendelig med desimaler uten mønster, eller med mønster, bare ikke periodisk, for eksempel 0,01001000100001 ...).

#### Middels: Gjøre om mellom brøk og desimaltall med endelig desimalutvikling

1. Gjør om til brøk.
a. $0,23$
b. $0,2003$
c. $0,0203$

2. Gjør om til desimaltall.

a. $\frac{3}{15}$
b. $\frac{35}{14}$
c. $\frac{3}{20}$

##### Vurderingskriterier

1. \
a.23/100,
b. 2003/10 000,
c. 203/10 000

2. \
a.  0,2;
b. 2,5;
c. 0,15

#### Avansert: Gjøre om mellom brøk og desimaltall med periodisk desimalutvikling

1. Gjør om til brøk.
a. $0,\overline{23}$
b. $0,2\overline{003}$
2. Gjør om til desimaltall.
a. $\frac{3}{7}$
b. $\frac{17}{6}$

##### Vurderingskriterier

1. \
a.
$$
\begin{aligned}
100x &
= 23,232323\ldots
\\
-x
& = 0,232323\ldots
\\
\Rightarrow 99x
& = 23
\\
x
&= 23/99
\end{aligned}$$

b.
$$
\begin{aligned}
10\ 000x &
= 2003,003003\ldots
\\
-10x &
= 2,003003\ldots
\\
9990x
& = 2\ 001
\\
x
& = \frac{2\ 001}{9\ 990}
\end{aligned}
$$
2. Må vise utregning.

a.  $0,\overline{428571}$

b. $2,8\overline{3}$

### Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

#### Middels: Avgjøre og begrunne (uten å utføre divisjon) om en gitt brøk er endelig eller periodisk

Avgjør og begrunn om brøkene er endelige eller periodiske, uten å utføre divisjon.
a. $\frac{18}{24}$
b. $\frac{18}{25}$
c. $\frac{12}{35}$
d. $\frac{12}{30}$

##### Vurderingskriterier

a. $\frac{18}{24} = \frac{9}{8}$. Siden 2 er eneste primfaktor i 8, så brøken er endelig.
b. 25 er faktor i hundre; brøken er endelig.
c. 35 har faktoren 7; siden teller ikke har det, er brøken periodisk.
d. $\frac{12}{30} = \frac{4}{10}$ som er endelig.

#### Avansert: Begrunne hvilke brøker som svarer til endelige og hvilke som svarer til periodiske desimaltall

1. Begrunn påstanden: En brøk svarer til et endelig desimaltall bare dersom den maksimalt forkorta kun har primfaktorene 2 og 5 i nevner.

2. Begrunn hvorfor resten av brøkene gir periodiske desimaltall.

##### Vurderingskriterier

a.  Må vise til at desimaltall er brøker med tierpotenser til nevner. Siden eneste primfaktorer i 10 er 2 og 5, må den maksimalt forkorta brøken ha nevner uten andre primfaktorer enn disse.
b. Begrunnes ved hjelp av eksempel: Tolke for eksempel 3/7 som divisjonen 3 : 7, og utføre den vanlige algoritmen. Divisjon med 7 kan bare gi restene 0, 1, ..., 6 (i vårt tilfelle ikke 0, for divisjonen går ikke opp). Det gir at høyeste antall mulige steg i divisjonsalgoritmen før vi får en rest vi har hatt tidligere, er seks. Dermed havner vi i en  «periode-loop».

### Utføre og begrunne prosentregning

#### Grunnleggende: Finne prosentdel av et tall, uttrykke tall som prosentdel av et hele, og finne det hele når del og prosentdel er gitt

1. Finn $20 \ \%$ av $250$ på to måter.

2. Hva er $100 \ \%$ dersom $18$ er $12 \ \%$?

3. Hvis du har kjørt $36 \  \text{km}$ av en $108 \ \text{km}$ roadtrip, hvor stor prosentdel av turen er unnagjort?

##### Vurderingskriterier

1. Dele på fem, veien om 1 (prosent) ...
2. 18/12 \* 100
3. 36/108

#### Middels: Utføre og begrunne beregningene over

1. Forklar kort to strategier for å finne $20 \ \%$ av $250$. Forklaringene må vise tydelig at strategiene er riktige.

2. Hvis vi skal uttrykke $65$ som prosentdel av $260$, kan vi regne på de to måtene du ser under. Forklar hvorfor de to strategiene funker.

a. Dele $260$ på $100$, for så å dele $65$ på tallet vi fikk.
b. Dele $100$ på $260$, for så å gange $65$ med tallet vi fikk.

##### Vurderingskriterier

1. Som grunnleggende, bare med god forklaring.
2. \
a. 260/100 gir én prosent av 260. Vi lurer på hvor mange slike
1-prosentere som går på 65, så 65 : 260/100.
b. 100/260 gir antall prosent per 1-er. Vi har 65 1-ere, så ganger opp med 65.

### Løse (ukjente) problemer knyttet til brøk, prosent (og desimaltall)

#### Avansert: Løse (ukjente) problemer knyttet til brøk, prosent (og desimaltall)

Hvis noe øker fra f.eks. $20 \ \%$ til $25 \ \%$ sier vi at økningen var på $5$ prosentpoeng. Fra en en meningsmåling til den neste, økte et politisk parti sin oppslutning med $2$ prosentpoeng. Det tilsvarte en økning på $12,5 \ \%$. Hvor stor oppslutning hadde partiet ved første måling?  

##### Vurderingskriterier

Si partiet hadde $p/100$ i oppslutning. Økte med 2 poeng til $(p + 2)/100$. Dette svarer til en 12,5 % økning, altså er

$$
\begin{aligned}
\frac{p + 2}{100}
& = 1,125 \cdot \frac{p}{100}
\\
p + 2
& = 1,125 \cdot p
\\
0,125 \cdot p
& = 2
\\
p & = 16.
\end{aligned}
$$
Partiet hadde altså 16 % prosent oppslutning før økningen.

## 17.04.23

### Forklare hva et posisjonssystem er

#### Grunnleggende

Forklar kort hva et posisjonssystem er. Gi eksempler fra base ti, tre, to og elleve.

##### Vurderingskriterier

Må få frem ideen om at sifrenes posisjon avgjør verdien de står for, og at denne verdien avhenger av hvilken gruppering vi velger -- hvilken base eller grunntall vi har. Må også ha med eksempler.

#### Middels

1. Forklar kort hva et posisjonssystem er.

2. Gjør om $121_{ti}$ til base tre, $101101_{to}$ til base ti, og $112_{fire}$ til base fem.

##### Vurderingskriterier

Som grunnleggende + omgjøringene. Det må gå frem hvordan omgjøringene er gjort.

#### Avansert

1. Gjør om  $112_{tre}$ til base seks.
2. Regn ut i den aktuelle basen:
a.  $1101001_{to} - 110010_{to}$  

b.  $43_{seks} \cdot 23_{seks}$

##### Vurderingskriterier

Som middels + beregninger. Disse må være ført i den aktuelle basen.

### Beskrive situasjoner med hensyn til additive strukturer

#### Grunnleggende

1. Beskriv tre situasjoner som har addisjon som modell med henholdsvis økning, forening og additiv sammenlikning som struktur.

2. Velg én av situasjonene over. Omformuler den slik at det er rimelig å si at den har samme struktur, men med subtraksjon som modell.

##### Vurderingskriterier

Additive strukturer s. 52 i Alfa.

#### Middels

Avgjør og begrunn hvilken additiv struktur situasjonene har. Angi både addisjons- og subtraksjonsstykket som passer i hvert tilfelle.

a. På en uke har en solsikke inntil husveggen vokst til 212 cm. Hvor mange centimeter må den vokse før den når husveggen på 240 cm?
b. André fant 12 kroner i bukselomma. I jakkelomma fant han 50. Hvor mye mer fant han i jakka?  
c. Studentene må lese to pensumbøker med til sammen 643 sider. Den ene boka er på 425 sider. Hvor mange sider har den andre?

##### Vurderingskriterier

En struktur må angis med rimelig begrunnelse. Begge mulige regnestykker må med.
a. er komplettering: 212 + \_\_ = 240 eller 240 -- 212 = \_\_.
b. er sammenlikning: 12 + \_\_ = 50 eller 50 -- 12 = \_\_.
c. er forening/sammenslåing: 425 + \_\_ = 643 eller 643 -- 425 = \_\_.

### Beskrive situasjoner med hensyn til multiplikative strukturer

#### Grunnleggende

1. Gjengi kort med et eksempel til hver, hva som menes med de to multiplikative strukturene rate og kombinatorisk situasjon.

2. Gjengi kort med et eksempel til hver, hva som menes med de to typene divisjon delingsdivisjon og målingsdivisjon.

##### Vurderingskriterier

Multiplikative strukturer s. 58 i Alfa.

#### Middels

1. Avgjør og begrunn hvilken multiplikativ struktur situasjonene svarer til.

a. En bils tilbakelagte strekning når den har kjørt 60 km/t i 20 minutter.
b. Antall tyggegummi i tre pakker med åtte i hver.  
c. Antall seter i en kinosal med 23 rader, hver med 14 seter.

2. Ta utgangspunkt i situasjon b. Legg til nødvendig informasjon, og omformuler på to måter: slik at du lager én divisjonsoppgave med målingsdivisjon og én med delingsdivisjon. Begrunn hvilken som er hva.

##### Vurderingskriterier

Avgjørelsene må begrunnes kort.

1. \
a. er rate.
b. er like grupper.
c. er rektangulært arrangement (eller like grupper).
2. \

- Målingsdivisjon: 24 tyggegummi fordelt i pakker på 8, hvor mange  pakker?
- Delingsdivisjon: 24 tyggegummi i tre pakker, hvor mange i hver?

### Bruke regnestrategier og egenskaper ved regneoperasjonene

#### Grunnleggende

Gjengi kommutativ, assosiativ og distributiv egenskap for addisjon og multiplikasjon.

##### Vurderingskriterier

Gjengi egenskapene.

#### Middels

1. Bruk minst én av egenskapene (kommutativ, assosiativ, distributiv) til å regne $23 \cdot 11$. Vis tydelig hvordan du tenker.

2. Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.

a. $352 - 61$
b. $240 : 20$
c. $160 \cdot \frac{3}{4}$

##### Vurderingskriterier

Trengs et par setninger som tydelig får frem hvordan man har tenkt.
    i.  Nærliggende å distribuere: $23 \cdot 11 = 23 \cdot (10 + 1)$
    ii. Eks. dele opp: $352 - 61 = 352 - 60 - 1$
    iii. Eks. dele på ti, så to: $240\ :20 = (240\ :10):2$
    iv. Eks. finne firedel av 16, gange med 3, gange med 10.

#### Avansert

1. Bruk multiplikasjonen $5 \cdot 8$ til å illustrere og gi en kort forklaring av distributiv egenskap.

2. Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.

3. Velg én av strategiene fra 2., og gi en illustrasjon og kort forklaring som viser at strategien alltid funker.
a. $240 : 20$
b. $160 \cdot \frac{3}{4}$

##### Vurderingskriterier

Få tydelig frem hva man har tenkt.
    i.  Må bruke gitt multiplikasjon, og få frem at egenskapen er generell (generisk eksempel)
    ii. Som iii. og iv. fra middels
    iii. Må få frem at strategien er generell (heller ikke her trengs nødvendigvis noe algebra)

### Forklare og gi eksempler på de ulike betydningene av brøk: del av hel/enhet, del av antall, tall og forhold

#### Grunnleggende

Forklar og gi eksempler på hva som menes med brøk som
a. del av en hel eller del av en enhet
b. del av et antall
c. tall
d. forhold

##### Vurderingskriterier

Må gi en kort forklaring. Alfa s. 96-101 og s. 109.

#### Middels

1. Avgjør og begrunn kort hvilke(n) betydning av brøk det er naturlig å knytte til situasjonene.
a. Etter en viss tid har du løpt $\frac{3}{4}$ av strekningen for dagens joggetur.
b. André føler seg spenstig, og maler $\frac{2}{3}$ av stueveggen grønn, den siste tredelen rosa.

2. Lag to oppgaver, og begrunn kort hvorfor de involverer den aktuelle betydningen av brøk.
a. Én oppgave med brøk som del av antall.
b. Én oppgave med brøk som forhold.

##### Vurderingskriterier

1. Må avgjøre med en kort, fornuftig begrunnelse.
a. er rimelig å tolke som _tall_ (en måling).
b. er rimelig å tolke som _del av helhet_ (vegg som helhet).
2. Oppgavene må rimelig kunne sies å involvere den aktuelle tolkningen, og besvarelsen må inneholde en kort begrunnelse.

### Forklare hvordan de reelle tallene er bygd opp

#### Grunnleggende: Forklare hva hele, rasjonale og irrasjonale tall er

Gjengi kort hva som menes hele, rasjonale og irrasjonale tall.

##### Vurderingskriterier

Gjengi korrekt. Hele tall: ... -2, -1, 0, 1, 2,.... Rasjonale: brøk med heltallig teller og nevner. Irrasjonale: de som ikke er heltallige brøker.

#### Middels: Forklare hvordan de reelle tallene er bygd opp av naturlige, hele, rasjonale og irrasjonale tall

Forklar kort hva naturlige, hele, rasjonale og irrasjonale tall er, og vis med en illustrasjon hvordan disse til sammen utgjør de reelle tallene.

##### Vurderingskriterier

Som grunnleggende, men med presisering av naturlige også, samt et diagram eller liknende som får frem hvilke mengder som er delmengder av hvilke.

### Utvide og forkorte brøker

#### Grunnleggende: Utvide og forkorte brøker

Finn i hvert tilfelle den likeverdige brøken med lavest mulig heltallig teller og nevner.
a. $\frac{12}{14}$
b. $\frac{1,5}{6}$
c. $\frac{\frac{2}{3}}{4}$

##### Vurderingskriterier

6/7, 1/4, 1/6

#### Middels: Utvide og forkorte brøker, og forklare og illustrere hvorfor dette gir brøker av lik verdi  

1. Hvilke brøker er likeverdige med $\frac{2}{5}$?
a. $\frac{4}{15}$
b. $\frac{1}{2,5}$
c. $\frac{\frac{2}{3}}{\frac{5}{3}}$
d. $\frac{10}{25}$

2. Lag en illustrasjon som tydelig viser at $\frac{2}{3}$ og $\frac{8}{12}$ er likeverdige.  

##### Vurderingskriterier

1. b, c og d
2. Eks. dele kvadrat i tredeler den ene veien, og firedeler den
andre.

### Utføre addisjon og subtraksjon med brøk

#### Grunnleggende: Utføre addisjon og subtraksjon med brøk

Regn ut.
a. $\frac{5}{2} + \frac{2}{3}$
b. $\frac{7}{3} - \frac{1}{2}$

##### Vurderingskriterier

19/6, 11/6

#### Middels: Utføre addisjon og subtraksjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

Regn ut, og gi en forklaring med illustrasjon som viser at beregningen må være riktig.

a. $\frac{5}{2} + \frac{2}{3}$
b. $\frac{2}{3} - \frac{1}{2}$

##### Vurderingskriterier

19/6, 1/6. Illustrasjonen må vise utviding til felles nevner på en forståelig måte.

### Utføre multiplikasjon med brøk

#### Grunnleggende: Utføre multiplikasjon med brøk

Regn ut.
a. $\frac{3}{2} \cdot \frac{4}{5}$
b. $2 \frac{2}{5} \cdot \frac{2}{3}$

##### Vurderingskriterier

6/5, 8/5

#### Middels: Utføre multiplikasjon med brøk, og forklare og illustrere hvorfor regnereglene gir mening

1. Forklar ved hjelp av en passende illustrasjon at $3 \cdot \frac{2}{5} = \frac{2}{5} \cdot 3$.

2. Forklar kort ved hjelp av en passende illustrasjon hvorfor vi multipliserer teller med teller og nevner med nevner for å finne produktet av to brøker.  

##### Vurderingskriterier

1. Må vise til struktur, ikke bare at «svarene» er like. Eks under.
Kvadratene er 1, grønn del 2/5. Figuren kan leses som *2/5 gjentatt
tre ganger,* altså 3 ⋅ 2/5. Den kan også leses som _2/5 av tre,_ altså
2/5 ⋅ 3.
![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image13.png)

1. Må vise til en figur som for eksempel den under (2/3 ⋅ 4/5):

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tall/image2.png)

### Utføre divisjon med brøk

#### Grunnleggende: Utføre divisjon med brøk

Regn ut.
a. $\frac{4}{5} : \frac{5}{4}$
b. $\frac{4}{3} : \frac{2}{5}$

##### Vurderingskriterier

 16/25, 10/3

#### Middels: Vise ved hjelp av generisk eksempel hvorfor regneregelen for divisjon med brøk er som den er

Vis ved hjelp av et generisk eksempel hvorfor divisjon med en brøk svarer til multiplikasjon med den omvendte brøken.

##### Vurderingskriterier

Må tolke en brøkdivisjon som brøk over brøk, og utvide. Oppgaven ber om _generisk eksempel._ Poenget er at strukturen må komme frem (som i algebraen under). Å dele på en stambrøk er ikke godt nok. Velger noen algebra, er det ok.
$$\frac{a}{b}\ :\frac{c}{d} = \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{\frac{a}{b} \cdot d/c}{\frac{c}{d} \cdot d/c} = \frac{a}{b} \cdot \frac{d}{c}$$

#### Avansert: Forklare ved hjelp av kontekst (både målings- og delingsdivisjon) hvorfor regneregelen for divisjon med brøk gir mening

Ta utgangspunkt i divisjonen $9 : \frac{3}{2}$. Lag to passende kontekster, og bruk dem til å vise at $9 : \frac{3}{2} = 9 \cdot \frac{2}{3}$.

a. Den ene konteksten skal gi delingsdivisjon.

b. Den andre konteksten skal gi målingsdivisjon.

##### Vurderingskriterier

a. Delingsdivisjon: 9 liter maling rekker til 3/2 vegg (like vegger), hvor mye maling trengs per vegg? Fordeler de 9 literne likt på de tre todelene, som gir 9/3 liter per todel. Ganger dette opp med to for å få en hel vegg, altså $9\ :\frac{3}{2} = \frac{9}{3} \cdot 2 = 9 \cdot \frac{3}{2}$.
b. Målingsdivisjon: Hvor mange en-og-en-halv-litere går det på ni liter? Det går to halvlitere på én liter, så $9 \cdot 2$ halvlitere på ni liter. 3/2 liter er tre ganger så mye, så det går en tredel så mange, altså $9\ :\frac{3}{2} = \frac{9 \cdot 2}{3} = 9 \cdot \frac{3}{2}$.

### Utføre formell omforming av brøk

#### Avansert: Utføre formell omforming av brøk

Regn ut.

a. $\frac{3}{2}(2 + \frac{2}{3} - \frac{3 + \frac{1}{5}}{\frac{3}{2}}) -1$
b. $\frac{(\frac{4}{7} \cdot (2 + \frac{4}{5})) - \frac{3}{5}}{\frac{2}{3}} + \frac{1}{2}$

##### Vurderingskriterier

-1/5 og 2.

## 31.03.23

### Forklare hva et posisjonssystem er, og regne med tall uttrykt i posisjonssystem med ulike baser

#### Grunnleggende: Forklare hva et posisjonssystem er, og gi eksempler på tall uttrykt i posisjonssystem med ulike baser

Forklar kort hva et posisjonssystem er. Gi eksempler fra base ti, fem, to og tolv.

##### Vurderingskriterier

Må få frem ideen om at sifrenes posisjon avgjør verdien de står for, og at denne verdien avhenger av hvilken gruppering vi velger – hvilken base eller grunntall vi har. Må også ha med eksempler.

#### Middels: Forklare hva et posisjonssystem er, og gjøre om tall mellom ulike baser

1. Forklar kort hva et posisjonssystem er.

2. Gjør om $112_{ti}$ til base tre, $1001010_{to}$ til base ti, og $112_{tre}$ til base fem.

##### Vurderingskriterier

Som over + omgjøringene. Det må gå frem hvordan omgjøringene er gjort.

#### Avansert: Utføre beregninger med tall uttrykt i andre baser enn ti

1. Gjør om $112_{fire}$ til base fem.

2. Regn ut i den aktuelle basen:

   a. $2212_{tre} : 21_{tre}$

   b. $43_{fem} \cdot 23_{fem}$

##### Vurderingskriterier

Som over + beregninger. Disse må være ført i den aktuelle basen.

### Beskrive situasjoner med hensyn til additive strukturer

#### Grunnleggende: Gjengi med eksempler de ulike additive strukturene for både addisjon og subtraksjon

Beskriv tre situasjoner som har addisjon som modell med henholdsvis økning, forening og additiv sammenlikning som struktur.
Velg én av situasjonene over. Omformuler den slik at det er rimelig å si at den har samme struktur, men med subtraksjon som modell.

##### Vurderingskriterier

Additive strukturer s. 52 i Alfa.

#### Middels: Avgjøre og begrunne hvilken struktur en gitt situasjon svarer til

Avgjør og begrunn hvilken additiv struktur situasjonene har. Tolk både med addisjon og subtraksjon som modell.

1. På en uke har en plante vokst seg 21 cm lengre til 93 cm. Hvor lang var den for en uke siden?
2. André hadde 12 kroner i lomma. Da han fant noen penger bakken, hadde han 19 kroner. Hvor mye fant han?
3. Henrik har to samlinger med Pokémon-kort, én med sjeldne og én med vanlige kort. Han har totalt 497 kort, hvorav de vanlige utgjør 354. Hvor mange sjeldne kort har Henrik?

##### Vurderingskriterier

Det er nok om bare navnet på strukturen for addisjon som modell er oppgitt, men begge mulige regnestykker må med. Avgjørelsene må begrunnes kort.

1. er sammenlikning, kjent differanse: $\_+21=93 eller 93-21=\_$.
2. er økning/oppheving av økning, ukjent økning: $12+\_=19 eller 19-12=\_$.
3. er forening/oppdeling, totalen kjent: $354+\_=497 eller 497-354=\_$.

### Beskrive situasjoner med hensyn til multiplikative strukturer

#### Grunnleggende: Gjengi med eksempler de ulike multiplikative strukturene for både multiplikasjon og divisjon

Forklart kort med et eksempel til hver av de to multiplikative strukturene multiplikativ sammenlikning og kombinatorisk situasjon.
Forklar kort med et eksempel til hver av de to typene divisjon delingsdivisjon og målingsdivisjon.

##### Vurderingskriterier

Multiplikative strukturer s. 58 i Alfa.

#### Middels: Avgjøre og begrunne hvilken struktur en gitt situasjon svarer til

1. Avgjør og begrunn hvilken multiplikativ struktur situasjonene svarer til.

   a. En flaske ligger opp ned i sekken og lekker 4 ml i minuttet.

   b. Antall gir på en sykkel med tre tannhjul fremme og åtte bak.

   c. Solas diameter er 109 ganger jordas.

2. Ta utgangspunkt i situasjon 1. Legg til nødvendig informasjon, og omformuler på to måter: slik at du lager én divisjonsoppgave med målingsdivisjon og én med delingsdivisjon. Begrunn hvilken som er hva.

##### Vurderingskriterier

Avgjørelsene må begrunnes kort.

1. \
   - er rate.
   - er kombinatorisk eller like grupper.
   - er sammenlikning.
2. \
   Målingsdivisjon: 12 ml har lekket fra en flaske som lekker 4 ml i minuttet. Hvor lenge har den lekket?
   Delingsdivisjon: 12 ml har lekket jevnt ut av en flaske i tre minutter. Hvor mye lekker flaska per minutt?

### Bruke regnestrategier og egenskaper ved regneoperasjonene

#### Grunnleggende: Gjengi kommutativ, assosiativ og distributiv egenskap for addisjon og multiplikasjon

Gjengi kommutativ, assosiativ og distributiv egenskap for addisjon og multiplikasjon.

##### Vurderingskriterier

Gjengi egenskapene.

#### Middels: Bruke regnestrategier, også ved hjelp av egenskapene over

Bruk minst én av egenskapene over (kommutativ, assosiativ, distributiv) til å regne $12 \cdot 17$. Vis tydelig hvordan du tenker.
Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.

a. $127 - 38$

b. $125 : 15$

c. $160 \cdot \frac{3}{4}$

##### Vurderingskriterier

Trengs et par setninger som tydelig får frem hvordan man har tenkt.

1. Nærliggende å distribuere: 12⋅17=(10+2)⋅17
2. Eks. fast differanse: 127-38=129-40
3. Eks. forkorte: 125∶15=25∶3=8 1/3
4. Eks. finne firedel av 16, gange med 3, gange med 10.

#### Avansert: Bruke, illustrere og begrunne regnestrategier og egenskapene

Velg en multiplikasjon som passer til å illustrere distributiv egenskap sammen med en kort ordforklaring.  
Gjør beregningene under ved hjelp av regnestrategier som ikke innebærer oppstilt regning. Vis tydelig hvordan du tenker.
Velg én av strategiene fra 2., og gi en illustrasjon og kort ordforklaring som viser at strategien alltid funker.
a. $127 - 38$

b. $125 : 15$

c. $160 \cdot \frac{3}{4}$

##### Vurderingskriterier

Få tydelig frem hva man har tenkt.

1. Må få frem at egenskapen er generell (men kan være gjort ved hjelp av talleksempel)
2. Som over
3. Må få frem at strategien er generell (heller ikke her trengs nødvendigvis noe algebra)
