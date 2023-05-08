#### Avansert: Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk),  Øveppgaver

1. Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder en toer (minst), men er ikke et partall. Avgjør hvor mange gjenværende muligheter det er
2. André har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder minst én ener og minst én toer. Du regner deg fram til at det er 271 koder som inneholder minst én ener, og 271 koder som inneholder minst én toer. I tillegg er det 512 av de totalt 1000 mulighetene som hverken inneholder enere eller toere. Hvor mange forskjellige koder kan André ha på sin lås?

##### Løsninsgforslag

1. Siden tallet ikke kan være et partall, så kan toer(ne) kun være på første og andre posisjon og på tredje posisjon kan vi velge fritt mellom oddetallene (5 muligheter). Vi begynner med å splitte i tre disjunkte tilfeller:
   1. Enten er det en toer på første posisjon, men ikke på andre. Vi kan altså ha kombinasjonene $2x$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). For hver av de $9$ sifrene kan vi kombintere det med et av fem oddetall. Altså totalt $9\cdot 5 = 45$ muligheter i dette tilfellet.
   2. Eller så er det ikke en toer på første posisjon, men på andre $x2$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). Tilsvarende som over får vi $45$ muligheter.
   3. Eller $22$. Her er det kun siste siffer som kan endre på seg, og vi har derfor 5 muligheter.
   Siden vi nå har delt mulighetene våre i tre tilfeller som dekker alle mulighetene, og i tillegg ikke overteller noe (er disjunkt), så sier addisjonsprinsippet at antallet er $45+45+5 = 95$.

#### Avansert: Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk),  08.05

Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder en toer (minst), men er ikke et partall.

- Avgjør hvor mange gjenværende muligheter det er. Besvarelsen må peke til en illustrasjon som viser hvordan du bruker addisjonssetningen.

##### Vurderingskriterier

Se oppgave 1 øveoppgaver. Merk at oppgaven *må* også inneholde en illustrasjon!

#### Avansert: Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet og kombinatorikk),  28.04.23

Det er \(30\) tall under \(121\) som er delelig på 4 fordi \({121 \over 4} = 30+ \text{én i rest}\).

1. Hvor mange tall under 121 er delelig på enten 4, 11 eller 59? Besvarelsen må inneholde en illustrasjon som får fram hvordan du har løst problemet.

2. Du velger et tilfeldig tall under \(121\). Hva er sannsynligheten for at tallet er delelig på 4, 11 eller 59?

##### Vurderingskriterier

1. Ved å illustrere kan vi se se på mengdene som er delelig på 4, 11 og 59. Siden $59$ er et primtall er minste felles multiplum etter $121$. Tallene $11$ og $4$ har derimot minste felles multiplum lik $44$. Derfor vil alt i 44 gangen overtelles når vi tar antall tall i 4 gangen og tall i 11 gangen. Vi ser at $44$, $88$ og $132$ er de tre første verdiene i 44-gangen. Dermed overteller vi bare 2 tall. Snittet mellom de andre mengdene er tomme. Vi får altså at det er $30$ tall delelig på 4, og 10 tall delelig på 11 (eventuelt 11 hvis en leser feil og ikke ser at der er *under* 121) og 2 tall delelig på 59 under 121. Totalt får vi dermed $30+10-2+2 = 40$ tall delelig på enten 4, 11 eller 59.
2. Vi kan nå se at vi har 40 av 120 mulige som gir $\frac{40}{120}=\frac{4}{12}= \frac{1}{3}$ sjans for å velge et tall under 121 som er delelig på enten 4, 11 eller 59.

![](/img/sannsyn/sannsyn28.04.svg)

