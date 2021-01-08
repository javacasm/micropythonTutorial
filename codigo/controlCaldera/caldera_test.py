import machine, neopixel
import Wemos

v = '1.8'
moduleName = 'caldera_test'
from Utils import identifyModule, myLog
identifyModule(moduleName,  v)

# Using a wemos https://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png

# Led compatible neopixel https://a.pololu-files.com/picture/0J5433.631.jpg 

np = neopixel.NeoPixel(machine.Pin(Wemos.D4),1) # Led RGB through the Hole en pin D4 (GPIO2)

blue = (0,0,10)
green = (10,0,0) 
red = (0,10,0) 
black = (0,0,0) 
white = (255,255,255)

rele = machine.Pin(Wemos.D1,machine.Pin.OUT)  # Rele shield en D1 (GPIO5)


def enciendeCaldera():
    rele.on()
    np[0] = red
    np.write()
    myLog('Caldera ON',saveToFile=True)

def apagaCaldera():
    rele.off()
    np[0] = blue
    np.write()
    myLog('Caldera OFF',saveToFile=True)


def checkCaldera():
    msg = 'Unknown'
    if rele.value()==1:
        np[0] = red
        msg = 'On'
    else:
        np[0] = blue
        msg = 'Off'
    np.write()
    return msg
