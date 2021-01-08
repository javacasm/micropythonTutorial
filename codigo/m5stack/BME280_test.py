## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import BME280  # Importamos la clase BME280

from m5stack import *
from m5ui import *

v = 0.7

def testBME280():
    i2c = machine.I2C(sda = machine.Pin(21),scl = machine.Pin(22)) # configuramos el acceso al bus i2c 
    i2c.scan() # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
    bme = BME280.BME280(i2c = i2c, address=118) 
    print('Temp: '+str(bme.temperature) + ' Pres: '+ str(bme.pressure) + ' Hum: '+str(bme.humidity))


def testBME280Wireless():
    i2c = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
    i2c.scan() # [118]
    bme = BME280.BME280(i2c = i2c,address = 118)
    print(bme.temperature) 


def uiTemp():
    i2c = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
    i2c.scan() # [118]
    bme = BME280.BME280(i2c = i2c,address = 118)
    lcd.clear()
    label0 = M5TextBox(0, 0, "T: " + str(bme.temperature), lcd.FONT_DejaVu40, 0x88FFFF, rotate=0)
    label1 = M5TextBox(0, 55, "P: " + str(bme.pressure), lcd.FONT_DejaVu40, 0x88FF88, rotate=0)
    label2 = M5TextBox(0, 110, "H: " + str(bme.humidity), lcd.FONT_DejaVu40, 0xFF55FF, rotate=0)
    

while True:
    if btnC.wasPressed():
        uiTemp()
    if btnB.wasPressed():
        break
    
    