# micropython en ESP32

## [Especificaciones técnicas ESP32](https://docs.micropython.org/en/latest/esp32/general.html#technical-specifications-and-soc-datasheets)

* Architecture: Xtensa Dual-Core 32-bit LX6
* CPU frequency: up to 240MHz
* Total RAM available: 528KB (part of it reserved for system
* BootROM: 448KB
* Internal FlashROM: none
* External FlashROM: code and data, via SPI Flash; usual size 4MB
* GPIO: 34 (GPIOs are multiplexed with other functions, including external FlashROM, UART, etc.)
* UART: 3 RX/TX UART (no hardware handshaking), one TX-only UART
* SPI: 4 SPI interfaces (one used for FlashROM)
* I2C: 2 I2C (bitbang implementation available on any pins)
* I2S: 2
* ADC: 12-bit SAR ADC up to 18 channels
* DAC: 2 8-bit DACs
* Programming: using BootROM bootloader from UART - due to external FlashROM and always-available BootROM bootloader, the ESP32 is not brickable

## Micropython

```
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```

Descargamos el firmware de micropython para ESP32 desde la pagina de [micropython.org](http://micropython.org/download#esp32)

```
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ~/Descargas/esp32-idf3-20191211-v1.11-633-gb310930db.bin
```

```
screen /dev/ttyUSB0 115200

```

## GPIO

https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio


## ADC

* pines ADC entre 32-39
* 12 bits: 0-4095 pero podemos reducir la resolución 
|ADC.Width|bits
|---|---
|ADC.WIDTH_9BIT|9
|ADC.WIDTH_10BIT|10
|ADC.WIDTH_11BIT|11
|ADC.WIDTH_12BIT|12 (default)

* Lectura entre 0 y 1.0v, aunque se puede atenuar la señal con adc.atten(machine.ADC.ATTN_11DB)
|ATTN|max V|
|---|---|
|ADC.ATTN_0DB|  1.00v
|ADC.ATTN_2_5DB | 1.34v
|ADC.ATTN_6DB|2.00v
|ADC.ATTN_11DB|3.6v 

```python
import machine

adc = machine.ADC(machine.Pin(32))
print(adc.read())



[Referencia](https://docs.micropython.org/en/latest/esp32/quickref.html#adc-analog-to-digital-conversion)


## Sensores internos

```python
import esp32

esp32.hall_sensor()     # read the internal hall sensor
tF = esp32.raw_temperature() # read the internal temperature of the MCU, in Farenheit
tC = (tF - 32)*5/9

```

## PWM

1Hz - 40MHz

todos los pines lo permite

## Touch pad


```python
import machine
import time

t = machine.TouchPad(machine.Pin(14))
while True:
    print(t.read()) # 1046 si no se toca 100 o menos si te toca 
    time.sleep(100)
```

[Referencia](https://docs.micropython.org/en/latest/esp32/quickref.html#capacitive-touch)


### Weakup

Podemos usar un touch pad para despertar

```python
import machine
import esp32

t = machine.TouchPad(machine.Pin(14))
t.config(500)               # Valor a partir del cual se despertara
esp32.wake_on_touch(True)
machine.lightsleep()        # ponemos a dormir
```

# ESP32 lipo

[Producto](https://es.aliexpress.com/item/33021934361.html)
