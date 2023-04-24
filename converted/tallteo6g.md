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

Ved å illustrere piltallene og markere i illustrasjonen, gi en ordforklaring av

1. en eksplisitt sammenheng mellom piltall nummer $n$ og antall prikker i piltallet.

2. en rekursiv sammenheng mellom to påfølgende piltall.

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

