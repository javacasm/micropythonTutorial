import machine,neopixel

# Using a wemos https://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png

np = neopixel.NeoPixel(machine.Pin(2),1) # Led RGB through the Hole en pin D4 (GPIO2)

blue = (0,0,150)
green = (150,0,0) 
red = (0,150,0) 
black = (0,0,0) 
white = (255,255,255)

ciclo = {blue, green, red, white, black}
for color in ciclo:
    np[0] = color
    np.write()

