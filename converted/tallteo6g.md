#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  Øveoppgaver

1. Se figurtallene under.

    a.  Gi en så kort og presis verbal beskrivelse du kan av hvordan
        figurene vokser (rekursiv sammenheng).

    b.  Illustrer den rekursive sammenhengen i figurene.

    c.  Gi en beskrivelse av den eksplisitte sammenhengen mellom
        figurnummer og figurtall (presisjon er målet her også).

    d.  Vis den eksplisitte sammenhengen i figurene.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image2.png)

2. Samme ordlyd som oppgave 1.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/image3.png)

##### Løsningsforslag

1. \
   a. Dette kan gjøres på flere måter. For eksempel kan en se forrige figur i neste, og peke på hva som er lagt til for å bygge den nye figuren. Vi kan også peke på at figuren består av to deler. En trekant, som står på et rektangel. For å lage neste figur så skyv trekanten opp og legg til en bunn på størrelse $n+1$. Rektangelet skal øke én i høyde og én i bredde også. Dermed må vi legge til $n$ og $n-1$. Totalt legger vi altså til $3n$.
   b. Under er sammenhengen markert. De grønne er forrige figur, det røde er det som legges til i trekanten, det blå er bunnen som legges til i rektangelet, og det gule er siden som legges til i rektangelet. ![Rekursiv sammenheng](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/rekursiv.svg)
   c. Vi kan nå bruke dekomponeringen vi har brukt til å beskrive den rekursive sammenhengen. For figur $P_n$ har vi trekanttall $n+1$ minus toppen. Det gir $T_{n+1}-1 = \frac{(n+1)(n+2)}{2}-1$. Rektangelet er alltid $n(n-1)$, så vi får at den eksplisitte formelen er $\frac{(n+1)(n+2)}{2}-1+n(n-1)$.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  12.05

Under ser dere de første figurene i et figurtallsmønster.

Ved å illustrere figurene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom figur nummer $n$ og antall prikker i figuren.

2. en rekursiv sammenheng mellom to påfølgende figurer. 

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/figurtall1205.svg)


##### Vurderingskriterier

1. Studenten kan for eksempel markere og bryte ned figuren i tre komponenter. To trekanter som er like store og er én større enn figurtallsnummeret (figur 1 har trekanter med størrelse 2, figur 2 har trekanter med størrelse 3 osv). Den siste komponenten er et kvadrat i midten som mangler sidene (men ikke hjørnene), også kvadratet er én større enn figurtallsnummeret (se figurer under). 
2. Fra 1. kan vi peke på at hvis vi skal gå fra figurtallnumer $n$ til å lage neste figur så må øke de tre komponentene på følgende måte: vi legge på sidelenger med størrelse $n+2$ på de to trekantene. På kvadratet må vi fylle sidene og legge til "ytre hjørner" (eventuelt må vi bare flytte de fire hjørnene ut og legge til rammen). 

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/tallteo/figurtall1205.drawio%20copy.svg)

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  08.05

Under ser dere dere de tre første piltallene.

Ved å illustrere piltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i piltallet.

2. en rekursiv sammenheng mellom to påfølgende piltall.


![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-32-20.png)

##### Vurderingskriterier

1. Studenten kan for eksempel markere trekanten i figuren og peke på at det er et rektangel med størrelse $n$ og $2n$ og at trekanten har størrelse $3$ mer enn $n$ men at den kun er rammen. Rammen er tre linjer som er to lenger enn figurtallnummeret. Dermed kan vi regne ved å ta størrelsen av et rektangel med størrelse $n$ og $2n$ og tre linjer på størrelse $n+2$. 
2. Fra 1. kan vi peke på at hvis vi skal gå fra figurtallnumer $n$ til $n+1$, så vil rektangelet øke med én linje på toppen med lengde $n+1$ og en kolonne med høyde $2n$. Trekanten øker med en prikk på hver av de tre linjene, så den øker alltid med $3$. 

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  28.04

Øveoppgave oppgave 1 a. og b.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  24.04

Ved å illustrere figurtallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom figurtall nummer $n$ og antall prikker i figurtallet.

2. en rekursiv sammenheng mellom to påfølgende figurtall.

##### Vurderingskriterier

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\

For eksempel kan det fremheves at det er to trekanter som ligger i figuren som starter på samme nivå som figurtallsnummeret, markert i gult i figuren under. Flytter man trekantene sammen får man et rektangel av størrelse $n$ og $n+1$.  Videre kan en da utifra markeringene se hvis en flytter toppene ned i "hullet", markert i grønn, så vil en ha et rektangel med høyde $n$ og bredde $2$. Totalt sett får vi et rektangel med bredde $2 + (n+1)$ og høyde $n$. Som gir en eksplisitt formel $(n+3)\cdot n$.

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-13-28-48.png)

![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-04-21-13-26-27.png)

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  31.03.23

Ved å illustrere trappetallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom trappetall nummer $n$ og antall prikker i trappetallet.

2. en rekursiv sammenheng mellom to påfølgende trappetall.

##### Vurderingskriterier

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\

For eksempel kan det fremheves at det er to forskjøvede trekanter som ligger på hverandre. Trekantene deler også sitt andre ledd (det er første figur). Vi har altså to trekanttall, som mangler topp og deler en side som alltid har lengde $2$. Trekanttallet starter også "en før" som betyr at vi har $2T_{n+1}-2-2 = (n+2)(n+1)-4$. Denne måten å bryte ned problemet på gjør at studenten også kan innse at figuren øker med $2(n+1)$ hver gang. Dermed må den rekursive formelen være $F_n = F_{n-1}+2(n+1)$ der $F_1 = 2$.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  17.02.23

Ved å illustrere ambolttallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom ambolttall nummer $n$ og antall prikker i ambolttallet.

2. en rekursiv sammenheng mellom to påfølgende ambolttall.

#### Vurderingskriterier grunnleggende:  17.02.23

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  13.02.23

Ved å illustrere bokstallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom bokstall nummer $n$ og antall prikker i bokstallet.

2. en rekursiv sammenheng mellom to påfølgende bokstall.

#### Vurderingskriterier grunnleggende:  13.02.23

Her må alle spørsmålene besvares, og de må
illustrere figurer.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
For eksempel kan det pekes på at det er et kvadrat med oddetalls sidelengde. Generelt er sidelengden $2n+1$. I tillegg trekkes det fra fire trekanttall som *starter* en senere, altså trekkes det fra $4T_{n-1}$.\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  10.02.23

Ved å illustrere sommerfugltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i sommerfugltallet.

2. en rekursiv sammenheng mellom to påfølgende sommerfugltall.

#### Vurderingskriterier grunnleggende:  10.02.23

Her må alle spørsmålene besvares, og de må
illustrere figurer. *Merk* at figuren ikke øker på en naturlig måte da *stammen* ikke passer inn i et godt mønster.  

i.  Eksplisitt formel må utledes, og de må henvise til figuren.\
\
For eksempel kan det pekes på at det er fire kvadrater som
overlapper på 2 plasser, i tillegg til 2 trekanter og en
konstant stamme på 10.  
\
\
ii. Her må de henvise til illustrasjonen for å få fram hvordan
figuren utvikler seg rekursivt.\
\
Igjen kan de ta utgangspunkt i eksempelet gitt på (i) for å
peke på hvordan utviklingen skjer.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  03.02.23

Under ser dere dere de tre første piltallene.

Ved å illustrere piltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i piltallet.

2. en rekursiv sammenheng mellom to påfølgende piltall.


![](https://raw.githubusercontent.com/Andremartiny/MA-173/main/img/2023-03-24-14-32-20.png)

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  27.01.23

Ved å illustrere medaljetallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom medaljetall nummer $n$ og antall prikker i medaljetallet.

2. en rekursiv forklaring av sammenhengen mellom to påfølgende medaljetall.

#### Vurderingskriterier grunnleggende:  27.01.23

Her må alle spørsmålene besvares, og de må
illustrere figurer

i.  Eksplisitt formel må finnes, og de må henvise til figuren

ii. Her er ordlyden blitt litt dum. Her må de henvise til
illustrasjonen for å få fram hvordan figuren utvikler seg
rekursivt.

#### Grunnleggende: Beskrive oppbygningen av figurtall (alle typer),  10.01.23

Ved å illustrere båttallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplsitt sammenheng mellom båttall nummer $n$ og antall prikker i båttallet.

2. en rekursiv forklaring av sammenhengen mellom to påfølgende båttall.

