# https://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver

from machine import Pin
from neopixel import NeoPixel

Height = 8
Width = 32
Num_Pixels = Height * Width

RowsXColor = 6

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, Num_Pixels) 

NumSteps = Height * RowsXColor 

for i in range(0 , NumSteps):
     np[i] = (i,0,0)
     np[i + NumSteps ] = (i,i,0)
     np[i + 2 * NumSteps ] = (0,i,0)
     np[i + 3 * NumSteps ] = (0,i,i)
     np[i + 4 * NumSteps ] = (0,0,i)

np.write()
