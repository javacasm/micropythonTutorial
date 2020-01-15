import machine,neopixel

# Led compatible neopixel https://a.pololu-files.com/picture/0J5433.631.jpg 
# Using GRB format

v = '1.2.1'

Red = b'Red'
Black = b'Black'
Blue = b'Blue'
Green =b'Green'
White = b'White'

def colorByName(msg):
    col = (0,0,0)
    if msg == Red:
        col = (0,150,0)
    elif msg == Black:
        col = (0,0,0)
    elif msg == Blue:
        col = (0,0,150)
    elif msg == Green:
        col = (150,0,0)
    elif msg == White:
        col = (255,255,255)
    elif msg == b'TinyBlue':
        col = (0,0,10)
    elif msg == b'Yellow':
        col = (244,252,3)
    elif msg == b'Orange':
        col = (140,252,3)
    elif msg == b'Gray':
        col = (10,10,10)
    elif msg == b'TinyGreen':
        col = (10,0,0)
    elif msg == b'TinyRed':
        col = (0,10,0)
    elif msg == b'Pink':
        col = (0,70,30)
    elif msg == b'Purple':
        col = (0,30,70)
    return col

def test(pin = 2):
    import time
    np = neopixel.NeoPixel(machine.Pin(pin),1) # Led RGB through the Hole en pin D4 (GPIO2) by default
    ciclo = {b'Blue', b'Green', b'Red', b'White', b'Black'}
    for color in ciclo:
        np[0] = colorByName(color)
        np.write()
        time.sleep(0.5)

