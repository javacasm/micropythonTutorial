import machine,neopixel

# Led compatible neopixel https://a.pololu-files.com/picture/0J5433.631.jpg 

blue = (0,0,150)
tinyBlue = (0,0,10)
green = (150,0,0) 
tinyGreen = (10,0,0)
red = (0,150,0)
tinyRed = (0,10,0)
yellow = (120,100,0)
orange = (100,120,0)
black = (0,0,0)
white = (255,255,255)
gray = (10,10,10)
pink = (0,70,30)
purple = (0,30,70)

def colorByName(msg):
    col = black
    if msg == b'Red':
        col = red
    elif msg == b'Black':
        col = black
    elif msg == b'Blue':
        col = blue
    elif msg == b'TinyBlue':
        col = tinyBlue
    elif msg == b'Green':
        col = green
    elif msg == b'White':
        col = white
    elif msg == b'Yellow':
        col = yellow
    elif msg == b'Orange':
        col = orange
    elif msg == b'Gray':
        col = gray
    elif msg == b'TinyGreen':
        col = tinyGreen
    elif msg == b'TinyRed':
        col = tinyRed
    elif msg == b'Pink':
        col = pink
    elif msg == b'Purple':
        col = purple
    return col

def test(pin = 2):
    import time
    np = neopixel.NeoPixel(machine.Pin(pin),1) # Led RGB through the Hole en pin D4 (GPIO2) by default
    ciclo = {blue, green, red, white, black}
    for color in ciclo:
        np[0] = color
        np.write()
        time.sleep(0.5)

