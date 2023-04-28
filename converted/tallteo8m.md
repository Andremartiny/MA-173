#### Middels: Finne rekursiv uttrykk for figurtall,  28.04

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for sekskanttallene er $H_n = {n(2n-1)}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig teknikk, samt illustrere sekskanttallene, se for eksempel ![](https://upload.wikimedia.org/wikipedia/commons/f/f0/Hexagonal_numbers.svg)

i.  Ved å se på utviklingen ser vi at tillegget øker med fire hver gang, fra $5$ til $9$ til $13$ osv.  Dermed øker tillegget lineært med stigning fire. Fra $1$ til $6$ ser vi at økningen er $4\cdot 2 - 3$, noe som også stemmer med figuren. Vi lekker til fire sider, og har tre hjørner vi teller to ganger, altså $4\cdot 2 - 3$, eller generelt $4\cdot n - 3$.

ii. Her *må* de ta differanse mellom $H_n$ og $H_{n-1}$ eller $H_{n+1}$ og $H_n$. Førstnevnte gir
$$
\begin{aligned}
n(2n-1) - (n-1)(2(n-1)-1)
& =
2n^2 - n - (n-1)(2(n-1)-1)
\\
& =
2n^2 - n - (n-1)(2n-3)
\\
& =
2n^2 - n - (n(2n-3) - (2n-3))
\\
& =
2n^2 - n - n(2n-3) + (2n-3)
\\
& =
2n^2 - n - 2n^2+3n + 2n-3
= 4n -3
\end{aligned}
$$

#### Middels: Finne rekursiv uttrykk for figurtall,  24.04

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for femkanttallene  $P_n$, der $P_1 =1$, $P_2 = 5$ og $P_3 = 12$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $P_n = {\frac{n}{2}(3n-1)}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med $3$, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning $3$.
Fra dette bør de komme seg til\
$$
P_{n} = P_{n - 1} + 3n-2
$$

ii. Finne uttrykket ved hjelp av å regne $P_{n}– P_{n - 1}$.

#### Middels: Finne rekursiv uttrykk for figurtall,  31.03.23

Vis i en illustrasjon hvordan hver figur inneholder den forrige, og finn rekursivt uttrykk for sekskanttallene  $H_n$, der $H_1 =1$, $H_2 = 6$ og $H_3 = 15$:
ved hjelp av strategien form på tillegg.
ved hjelp av strategien differanse mellom eksplisitte uttrykk. Merk: Det eksplisitte uttrykket for bikubetallene er $H_n = {n(2n-1)}$.

##### Vurderingskriterier

Studenten må besvare alle spørsmålene med riktig
teknikk. Her *må* det være med en illustrasjon.

i.  Finne ved å peke på form på tillegg (se grunnleggende i).
De må altså se at tilleggene øker med $4$, noe som tilsier at
formen på tillegget må være en lineær faktor med stigning $4$.
Fra dette bør de komme seg til\
$$
H_{n} = H_{n - 1} + 4n-3
$$

ii. Finne uttrykket ved hjelp av å regne $H_{n}– H_{n - 1}$.

