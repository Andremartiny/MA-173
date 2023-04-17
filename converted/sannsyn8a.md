#### Avansert: Forklare, illustrere og bruke addisjonssetningen (for sannsynlighet *og* kombinatorikk),  Øveppgaver

1. Henrik har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder en toer (minst), men er ikke et partall. Avgjør hvor mange gjenværende muligheter det er
2. André har en tresifret kombinasjon på sykkellåsen sin. Du får vite at koden inneholder minst én ener og minst én toer. Du regner deg fram til at det er 271 koder som inneholder minst én ener, og 271 koder som inneholder minst én toer. I tillegg er det 512 av de totalt 1000 mulighetene som hverken inneholder enere eller toere. Hvor mange forskjellige koder kan André ha på sin lås?


##### Løsninsgforslag

1. Siden tallet ikke kan være et partall, så kan toer(ne) kun være på første og andre posisjon og på tredje posisjon kan vi velge fritt mellom oddetallene (5 muligheter). Vi begynner med å splitte i tre disjunkte tilfeller:
   1. Enten er det en toer på første posisjon, men ikke på andre. Vi kan altså ha kombinasjonene $2x$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). For hver av de $9$ sifrene kan vi kombintere det med et av fem oddetall. Altså totalt $9\cdot 5 = 45$ muligheter i dette tilfellet.
   2. Eller så er det ikke en toer på første posisjon, men på andre $x2$, der $x$ er et siffer som ikke er $2$ (altså 9 muligheter). Tilsvarende som over får vi $45$ muligheter. 
   3. Eller $22$. Her er det kun siste siffer som kan endre på seg, og vi har derfor 5 muligheter.
   Siden vi nå har delt mulighetene våre i tre tilfeller som dekker alle mulighetene, og i tillegg ikke overteller noe (er disjunkt), så sier addisjonsprinsippet at antallet er $45+45+5 = 95$.

