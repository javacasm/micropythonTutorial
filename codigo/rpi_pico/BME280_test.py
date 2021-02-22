## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import rpi_pico # Convierte entre pines del ESP12 (que usa micropython) y los del RPI Pico
import BME280  # Importamos la clase BME280

v = '0.3'

i2c = None

def initI2C():
    global i2c
    i2c = machine.I2C(0, sda = machine.Pin(rpi_pico.I2C0_SDA), scl = machine.Pin(rpi_pico.I2C0_SCL))
    i2c.scan()    

def testBME280():
    if i2c == None:
        initI2C()
    bme = BME280.BME280(i2c = i2c, address=BME280.BME280_I2CADDR) 
    print('Temp: '+str(bme.temperature) + ' Pres: '+ str(bme.pressure) + ' Hum: '+str(bme.humidity))
