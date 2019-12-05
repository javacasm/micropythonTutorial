# https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver


# DHT11 can be called no more than once per second and the DHT22 once every two seconds for most accurate results.

# Wemos DHT11 Shield  uses D4

import dht
import machine
d11 = dht.DHT11(machine.Pin(4))

d22 = dht.DHT22(machine.Pin(5))
d11.measure()
d11.temperature()
d11.humidity()
