# Meteo Salon

# SDA       D4 (GPIO02)
# SCL       D3 (GPIO00)
# LED RGB   D2 (GPIO04)

import neopixel,machine,NeoPixelTHO,time


ledRGB = neopixel.NeoPixel(machine.Pin(4),1) # Led RGB through the Hole en pin D2 (GPIO4)
led = machine.Pin(2,machine.Pin.OUT)  

def testColor():
    for color in NeoPixelTHO.ciclo:
        ledRGB[0] = color
        ledRGB.write()

## Encendemos todo
def encendemosTodo():
    testColor()
    led.off()

## Apagamos todo
def apagamosTodo():
    led.on()
    ledRGB[0]=NeoPixelTHO.black
    ledRGB.write()

def start():
    encendemosTodo()
    time.sleep(1000)
    apagamosTodo()
    





