# Meteo Salon

# SDA       D3 (GPIO00)
# SCL       D4 (GPIO02)
# LED RGB   D2 (GPIO04)

import neopixel, machine, NeoPixelTHO, time, Wemos, BME280

# LedRGBN
ledRGB = neopixel.NeoPixel(machine.Pin(Wemos.D2),1) # Led RGB through the Hole en pin D4 (GPIO4)

# Builtin Led
led = machine.Pin(Wemos.BUILTIN_LED,machine.Pin.OUT)
led.on()  # It's inverted

# BME280 via I2C 
i2c = machine.I2C(sda = machine.Pin(Wemos.D3),scl = machine.Pin(Wemos.D4))
bme = BME280.BME280(i2c = i2c, address = 118)


def testColor():
    NeoPixelTHO.test()

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







