# Tutorial de micropython basado en Wemos

esptool.py --port /dev/ttyUSB0 erase_flash

esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect-fm dio 0 ~/Descargas/esp8266-20191121-v1.11-586-g1530fda9c.bin 

# configuramos weprepl

>>> import weprepl_setup
# respondemos y se resetea

# Configuramos la red (esta configuracion se mantendra tras un reset)
>>> wl = network.WLAN(network.STA_IF)
>>> wl.active(True)
>>> wl.scan()
>>> wl.connect("SSID","CLAVE_SSID")
>>> wl.ifconfig()
# ('192.168.1.55', '255.255.255.0', '192.168.1.1', '192.168.1.1') 


Subimos el fichero Wemos.py

# Led builtIn

```python
import machine
import wemos

led = machine.Pin(Wemos.D4,machine.Pin.OUT) # LED Builtin

led.off() # Esta invertido
led.on()

```

## Rele


```python
import machine
import wemos

rele = machine.Pin(Wemos.D1,machine.Pin.OUT)

rele.on() # Encendemos el rele

rele.off() # Apagamos el rele
```

# PWM sobre 

# TODO
```python
import machine
import time
import Wemos

pwm = machinePWM(machine.Pin(Wemos.D4))

pwm.duty(896)
time.sleep(1)
pwm.duty(512)
time.sleep(1)
pwm.duty(0)
```

# Neopixel

```python
import neopixel,machine
import Wemos

ledRGB = neopixel.NeoPixel(machine.Pin(Wemos.D2),1) 

# Rojo
ledRGB[0] = (50,0,0)
ledRGB.write()
# Verde
ledRGB[0] = (0,50,0)
ledRGB.write()
# Azul
ledRGB[0] = (0,0,50)
ledRGB.write() 
# Blanco
ledRGB[0] = (255,255,255)
ledRGB.write() 
# Negro
ledRGB[0] = (0,0,0)
ledRGB.write() 

```
# DHT11 - D4

```python
import dht,machine
import Wemos

dht11 = dht.DHT11(machine.Pin.D4)

dht11.measure()
dht11.temperature()
dht11.humidity()

```

# BMP180

# Subimos el fichero bmp180.py de https://github.com/micropython-IMU/micropython-bmp180


```python
import machine
import bmp180
import Wemos

i2c = machine.I2C(sda = machine.Pin(Wemos.D2),scl = machine.Pin(Wemos.D1))
i2c.scan() # [119] o 0x77

bmp = bmp180.BMP180(i2c)

bmp.temperature
bmp.pressure

bmp.baseline = 101234## Presion a nivel del mar
bmp.altitude

```


```python
import onewire, ds18x20 
ds = ds18x20.DS18X20(onewire.OneWire(machine.Pin(Wemos.D2)))
roms = ds.scan()
ds.convert_temp() 
ds.read_temp(roms[0]) # 27.1875
ds.convert_temp() 
ds.read_temp(roms[0]) # 30.625 

```


# Pantalla OLED 

# subimos el fichero [ssd1306.py](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)


```python
import ssd1306
import machine
import Wemos

i2c = machine.I2C(sda = machine.Pin(Wemos.D2), scl = machine.Pin(Wemos.D1))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
display.fill(0)
display.text("Hello", 0, 0)
display.text("world!", 0, 8)
display.pixel(20, 20, 1)
display.show()

```

```python


```

## Ficheros


import os
print(os.listdir())
You should see something like ['boot.py'] – that’s a list with just one file name in it. boot.py and later main.py are two special files that are executed when the board starts. boot.py is for configuration, and you can put your own code in main.py.

You can create, write to and read from files like you would with normal Python:

with open("myfile.txt", "w") as f:
    f.write("Hello world!")
print(os.listdir())
with open("myfile.txt", "r") as f:
    print(f.read())
    
    
## HTTP


HTTP Requests
Once you are connected to network, you can talk to servers and interact with web services. The easiest way is to just do a HTTP request – what your web browser does to get the content of web pages:

import urequests
r = urequests.get("http://duckduckgo.com/?q=micropython&format=json").json()
print(r)
print(r['AbstractText'])
You can use that to get information from websites, such as weather forecasts:

import json
import urequests
r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=Zurich&appid=XXX").json()
print(r["weather"][0]["description"])
print(r["main"]["temp"] - 273.15)
It’s also possible to make more advanced requests, adding special hea
