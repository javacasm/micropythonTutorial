# Dev Board 

# http://forum.hobbycomponents.com/viewtopic.php?f=110&t=2056
# http://hobbycomponents.com/images/forum/HCDVBD0027_Features.png
# RGB 12 (green), 13 (blue), and 15 (red)
# Leds Ordered 2 0 4 5 14 16 (All inverted) 

from machine import Pin, PWM

led1 = Pin(2,Pin.OUT)
led2 = Pin(0,Pin.OUT)
led3 = Pin(4,Pin.OUT)
led4 = Pin(5,Pin.OUT)
led5 = Pin(14,Pin.OUT)
led6 = Pin(16,Pin.OUT)

pinGreen = Pin(12, Pin.OUT)
pinBlue = Pin(13, Pin.OUT)
pinRed = Pin(15, Pin.OUT)

frequency = 750

Green = PWM(pinGreen, freq = frecuency)
Blue = PWM(pinBlue, freq = frecuency)
Red = PWM(pinRed, freq = frecuency)  
