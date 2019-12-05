

```python

import Wemos
import machine

rele = machine.Pin(Wemos.D1)

rele.on()

rele.off()

```python
import dht
import Wemos
dht11 = dht.DHT
DHTBase DHT11DHT22 
dht11 = dht.DHT11(machine.Pin(Wemos.D4))
dht11.measure()
print(dht11.temperature())
print(dht11.humidity())

```python
import onewire
import ds18x20
ds = ds18x20.DS18X20(onewire.OneWire(machine.Pin(Wemos.D2)))
roms = ds.scan()
print(roms)
ds.read_temp(roms[0]) 




```python
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c.scan()

# subimos el fichero bmp180.py
 
```python
import bmp180 
bmp = bmp180. 
__class____name__I2C Pin
mathtimeunp BMP180
bmp = bmp180.BMP180(i2c)
Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
File "bmp180.py", line 48, in __init__
OSError: [Errno 19] ENODEV
bmp = bmp180.BMP180(i2c)
bmp.temperature
26.2409
bmp.pressure
