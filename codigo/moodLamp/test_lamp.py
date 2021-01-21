import machine
from neopixel import NeoPixel
import Wemos
import BME280_test
import time

v = '0.2'

N_Led = 16

def testBME():
    BME280_test.testBME280Wireless()

np = NeoPixel(machine.Pin(Wemos.D2), N_Led)

def testRGBWhite():
    for i in range(0, N_Led):
        np[i]=(255, 255, 255)
    np.write()

def testFadeOutRGB():
    for t in range(0,10):
        for i in range(0, N_Led):
            np[i]=(155-15*t, 155-15*t, 155-15*t)
        np.write()
        time.sleep(0.1)
    RGBoff()

def RGBoff():
    for i in range(0, N_Led):
        np[i]=(0, 0, 0)
    np.write()


testBME()
testRGBWhite()
time.sleep(1)
testFadeOutRGB()
