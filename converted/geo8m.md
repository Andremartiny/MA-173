
#### Middels: Bruke Pytagoras setning,  Øveoppgaver

1. Under er det tegnet inn en rettvinklet trekant plassert. På katetene og hypotenusen er det også tegnet inn halvsirkler.

   a. Avgjør arealet av det hvite området.
   b. Hva er forholdet mellom arealet av det hvite området og arealet av trekanten?

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image4.png)

2. Under er et rektangel der det er lagt inn en rettvinklet trekant der hypotenusen deles med grunnlinjen til rektangelet. Denne rettvinklede trekanten deler rektangelet inn i tre rettvinklede trekanter. Hvis den minste trekanten har sidelengder 25 og 60. Hva er de resterende sidelengdene i figuren?\

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/geo/image5.png)\

**Bonus:** Figuren er konstruert med utgangspunkt i den Pytagoreiske trippelen $5^{2} + 12^{2} = 13^{2}$. Velg en annen Pytagoreisk trippel og lag en tilsvarende figur.

##### Løsningsforslag

1. La oss kalle sidene i den rettvinkla trekanten for $x$, $y$ og $z$, slik at $x^2 + y^2 = z^2$. Da vet vi at de tre halvsirklene har areal $\pi(\frac{x}{2})^2 = \pi \frac{x^2}{4}$, $\pi \frac{y^2}{4}$ and $\pi \frac{z^2}{4}$. I tillegg har trekanten areal $\frac{2x\cdot2y}{2} = 2xy$. Tar vi de to små halvsirklene i tillegg til trekanten får vi hele området. Dette har areal $\frac{\pi}{2}(x^2+y^2)+ 2ab$. Vi kan nå bruke Pytagoras setning til å si at dette arealet kan skrives som $\frac{\pi c^2}{4} + 2ab$.Nå gjenstår det bare å trekke fra den store halvsirkelen for å få arealet av det hvite området. Dette gir $\frac{\pi c^2}{4}+ 2ab - \frac{\pi c^2}{4} = 2ab$. Vi ser dermed at det hvite området har samme areal som trekanten. Dermed blir forholdet mellom det hvite området og arealet av trekanten $1$.




#### Middels: Bruke Pytagoras setning,  31.03.23

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



