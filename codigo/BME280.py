# Sensor atmosferico https://github.com/catdog2/mpy_bme280_esp8266

import machine
import bme280

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

print(bme.values) ## Muestra los datos en un formato legible ('22.54C', '938.81hPa', '36.46%') 

# temperature: the temperature in hundredths of a degree celsius. For example, the value 2534 indicates a temperature of 25.34 degrees.
#  pressure: the atmospheric pressure. This 32-bit value consists of 24 bits indicating the integer value, and 8 bits indicating the fractional value. To get a value in Pascals, divide the return value by 256. For example, a value of 24674867 indicates 96386.2Pa, or 963.862hPa.
#  humidity: the relative humidity. This 32-bit value consists of 22 bits indicating the integer value, and 10 bits indicating the fractional value. To get a value in %RH, divide the return value by 1024. For example, a value of 47445 indicates 46.333%RH.
