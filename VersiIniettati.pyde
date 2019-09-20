LarghezzaImg=1024
AltezzaImg=560

#Creo una immaggine vuota in codifica RGB
img=createImage(LarghezzaImg,AltezzaImg,RGB)

#Carico la struttura dell'immagine
img.loadPixels()

def setup():
    global frog
    size(LarghezzaImg,AltezzaImg)
    frog=loadImage("frog2.jpg")
    disegna()
    #noLoop()


def disegna():
    input = createInput("Paradiso_1-12"); #Apro il file con il testo da iniettare

    loadPixels()

    #Carico l'immagine contenitore
    frog.loadPixels()

    #inizializzo il puntatore al bit da iniettare
    bit=15

    # Salto il primmo carattere in input
    # e leggo carattere da iniettare
    data = input.read()
    data = input.read()
    carattereCorrente=1
    #Contatore carattere da iniettare
    pixelCorrente=0

    while (data != -1 and pixelCorrente<(width*height)):
        #Estraggo le componenti RGB
        r=red(frog.pixels[pixelCorrente])
        g=green(frog.pixels[pixelCorrente])
        b=blue(frog.pixels[pixelCorrente])

        #trasformo la componente rossa in intero
        r=int(r)

        #trasformo in binario, la Codifica ASCII è negli 8 bit più significativi:
        binario=binary(data,16)

        if (binario[bit]=="0" and (r%2)==1):
            #bit da esaminare zero e  componente rossa dispari -> decremento la componente
            r=r-1
        elif (binario[bit]=="1" and (r%2)==0):
            #bit da esaminare uno e la componente rossa pari -> incremento la componente
            r=r+1

        #scorro i bit
        bit=bit-1
        if bit==7:
            #teminati gli 8 bit più significativi, passo al carattere successivo da iniettare e riparto da bit 15
            bit=15
            #Leggo il carattere successivo
            data= input.read()
            carattereCorrente+=1

        pixels[pixelCorrente]=color(r,g,b) #inietto la componente rossa nell'pixel corrente dell'immagine risultato
        pixelCorrente=pixelCorrente+1

    print("Ho iniettato %s caratteri. Copio il resto dell'immagine" %(carattereCorrente))

    while (pixelCorrente<(width*height)):
        #Copio il resto dell'immagine se il testo è finito prima
        r=red(frog.pixels[pixelCorrente])  #Estraggo le componenti RGB
        g=green(frog.pixels[pixelCorrente])
        b=blue(frog.pixels[pixelCorrente])
        pixels[pixelCorrente]=color(r,g,b) #inietto la componente rossa nell'pixel corrente dell'immagine risultato
        pixelCorrente=pixelCorrente+1


    #Aggiorno l'immagine
    updatePixels()

    #Scrivo il file finale
    save("Frog_injected.tiff")
