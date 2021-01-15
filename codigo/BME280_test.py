## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import Wemos # Convierte entre pines del ESP12 (que usa micropython) y los del Wemos 
import BME280  # Importamos la clase BME280

def testBME280():
    i2c = machine.I2C(sda = machine.Pin(Wemos.D2),scl = machine.Pin(Wemos.D1)) # configuramos el acceso al bus i2c 
    i2c.scan() # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
    bme = BME280.BME280(i2c = i2c, address=118) 
    print('Temp: '+str(bme.temperature) + ' Pres: '+ str(bme.pressure) + ' Hum: '+str(bme.humidity))


def testBME280Wireless():
    i2c = machine.I2C(sda=machine.Pin(Wemos.D3),scl=machine.Pin(Wemos.D4))
    i2c.scan() # [118]
    bme = BME280.BME280(i2c = i2c,address = 118)
    print(bme.temperature) 
