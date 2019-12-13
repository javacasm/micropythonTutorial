import machine
import BME280

# v1.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

def initSensor():
    i2c = machine.I2C(sda = machine.Pin(5),scl = machine.Pin(4))
    i2cDevices = i2c.scan()
    if len(i2cDevices) > 0:
        bme = BME280.BME280(i2c = i2c,address = 118)
        print(bme.temperature)
        return bme
    else:
        print('No BME280 device found')
        return None
