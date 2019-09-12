LarghezzaImg=1024
AltezzaImg=560
img=createImage(LarghezzaImg,AltezzaImg,RGB)
img.loadPixels()

def setup():
    global frog
    size(LarghezzaImg,AltezzaImg)
    frog=loadImage("frog2.jpg")
    noLoop()


def draw():
    input = createInput("DivinaCommedia");

    loadPixels()
    frog.loadPixels()
    #image(frog,0,0)
    car=0
    bit=15
    data = input.read()
    data = input.read()
    c=0
    while (data != -1 and c<(width*height)):
        r=red(frog.pixels[c])
        g=green(frog.pixels[c])
        b=blue(frog.pixels[c])
        #print(int(r))
        r=int(r)
        #print(chr(data))
        binario=binary(data,16)
        #binario=data
        #print(chr(data),binario, binario[bit])
        if (binario[bit]=="0" and (r%2)==1):
            r=r-1
        elif (binario[bit]=="1" and (r%2)==0):
            r=r+1
        bit=bit-1
        if bit==7:
            bit=15
            data= input.read();

        pixels[c]=color(r,g,b)
        c=c+1
    updatePixels()
    save("Frog_injected.tiff")
