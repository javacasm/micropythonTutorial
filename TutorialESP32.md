# Tutorial de micropython con ESP32


## Flashear micropython

```
esptool.py --port /dev/ttyUSB0 erase_flash
```

[Descargamos el firmware](http://micropython.org/download#esp32)

Hay d'ia de hoy hay 3 diferentes

GENERIC
GENERIC-SPIRAM
TinyPICO 


[Diferencia SRAM/SPIRAM](https://forum.micropython.org/viewtopic.php?t=5519)


```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
```

Conectamos al REPL

```
screen /dev/ttyUSB0 115200
```

## Builtin led

>>> import machine
>>> led = machine.Pin(5,machine.Pin.OUT))
>>> led.on() # Esta invertido
>>> led.off()

## configuramos wifi

## Modificamos el fichero **boot.py**

```python
import webrepl
import network
iw = network.WLAN(network.STA_IF)
iw.active(True)
iw.connect('OpenWrt','qazxcvbgtrewsdf')
webrepl.start()
iw.ifconfig()
print('esp32 Lolin32.34')
```

## Modelos

### Lolin32

![Front](https://wiki.wemos.cc/_media/products:lolin32:lolon32_v1.0.0_2_16x9.jpg)

![Back](https://wiki.wemos.cc/_media/products:lolin32:lolon32_v1.0.0_3_16x9.jpg)

![Pinout](./images/lolon32_v1.0.1_pinout.png)

[Esquematico de Lolin32 ESP32](https://wiki.wemos.cc/_media/products:lolin32:sch_lolin32_v1.0.0.pdf)

## Referencia

[Quick Reference](https://docs.micropython.org/en/latest/esp32/quickref.html)

