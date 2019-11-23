import machine,neopixel

# Led compatible neopixel https://a.pololu-files.com/picture/0J5433.631.jpg 

blue = (0,0,150)
green = (150,0,0) 
red = (0,150,0) 
black = (0,0,0) 
white = (255,255,255)


def test(pin = 2):
    np = neopixel.NeoPixel(machine.Pin(pin),1) # Led RGB through the Hole en pin D4 (GPIO2) by default
    ciclo = {blue, green, red, white, black}
    for color in ciclo:
        np[0] = color
        np.write()

