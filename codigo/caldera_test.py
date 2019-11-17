import machine,neopixel

# Using a wemos https://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png

# Led compatible neopixel https://a.pololu-files.com/picture/0J5433.631.jpg 

np = neopixel.NeoPixel(machine.Pin(2),1) # Led RGB through the Hole en pin D4 (GPIO2)

blue = (0,0,50)
green = (50,0,0) 
red = (0,50,0) 
black = (0,0,0) 
white = (255,255,255)

rele = machine.Pin(5,machine.Pin.OUT)  # Rele shield en D1 (GPIO5)


def enciendeCaldera():
    rele.on()
    np[0] = red
    np.write()

def apagaCaldera():
    rele.off()
    np[0] = blue
    np.write()


def checkCaldera():
    if rele.value()==1:
        np[0] = red
    else:
        np[0] = blue
    np.write()
