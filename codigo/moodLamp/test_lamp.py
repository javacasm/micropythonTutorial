import machine
from neopixel import NeoPixel
import Wemos
import BME280_test

BME280_test.testBME280Wireless()

np = NeoPixel(machine.Pin(Wemos.D7),17)

for i in range(0,17):
    np[i]=(255,255,255,)
    
np.write()