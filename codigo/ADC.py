# https://docs.micropython.org/en/latest/esp8266/quickref.html#adc-analog-to-digital-conversion

#  input voltages on the ADC pin must be between 0v and 1.0v.

from machine import ADC

adc = ADC(0)            # create ADC object on ADC pin
adc.read()              # read value, 0-1024
