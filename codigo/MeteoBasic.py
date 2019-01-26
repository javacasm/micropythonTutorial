# Meteo basic

import machine,bme280 

from machine import I2C
from esp8266_i2c_lcd import I2cLcd 

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)) 
i2c.scan() ## [63, 118] 
bme = bme280.BME280(i2c=i2c) 

lcd = I2cLcd(i2c, 63, 2, 16) 

lcd.move_to(0, 0) 
lcd.putstr(bme.values[0])
lcd.move_to(0, 1) 
lcd.putstr(bme.values[1])
lcd.move_to(10, 0)
lcd.putstr(bme.values[2]) 
