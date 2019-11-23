# Meteo Salon

# SDA       D4 (GPIO02)
# SCL       D3 (GPIO00)
# LED RGB   D2 (GPIO04)

import neopixel,machine,NeoPixelTHO,time,Wemos


ledRGB = neopixel.NeoPixel(machine.Pin(Wemos.D2),1) # Led RGB through the Hole en pin D4 (GPIO4)
led = machine.Pin(Wemos.BUILTIN_LED,machine.Pin.OUT)
led.on()  # It's inverted

def testColor():
    for color in NeoPixelTHO.ciclo:
        ledRGB[0] = color
        ledRGB.write()

## Encendemos todo
def encendemosTodo():
    testColor()
    time.sleep(1)
    led.off()

## Apagamos todo
def apagamosTodo():
    led.on()
    ledRGB[0]=NeoPixelTHO.black
    ledRGB.write()

def start():
    encendemosTodo()
    time.sleep(1)
    apagamosTodo()

def color(c):
    ledRGB[0]=c
    ledRGB.write()






