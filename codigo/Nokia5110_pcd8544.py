# Nokia 5110 - pcd8544


## Conexión

WeMos|Nokia 5110| Descripción
--- |--- |---
D0 (GPIO16)| 0 RST|Reset display
D1 (GPIO05)| 1 CE/CS|chip select/enable
D8 (GPIO15)| 2 DC|data/command
D7 (GPIO13)| 3 Din|SPI MOSI to display data input
D5 (GPIO14)| 4 Clk|SPI clock
3V3|5 Vcc| 3.3V 
D6 (GPIO12)| 6 BL| 3.3V backlight o PWM
G|7 Gnd| Ground

Test the display:

```python
>>> from machine import Pin, SPI
>>> import time
>>> import pcd8544

>>> spi = SPI(1, baudrate=80000000, polarity=0, phase=0)

>>> cs = Pin(5)
>>> dc = Pin(15)
>>> rst = Pin(16)

>>> bl = Pin(12, Pin.OUT, value=1)
>>> lcd = pcd8544.PCD8544(spi, cs, dc, rst)
```

Switch off the backlight:

```python
>>> bl.value(0)
```

Switch on the backlight:

```python
>>> bl.value(1)
```


>>> import framebuf
>>> buffer = bytearray((lcd.height // 8) * lcd.width)
>>> framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)
Light every pixel:

>>> framebuf.fill(1)
>>> lcd.data(buffer)
Clear screen:

>>> framebuf.fill(0)
>>> lcd.data(buffer)
Print Hello, World! using the 8x8 font:

>>> framebuf.text("Hello,", 0, 0, 1)
>>> framebuf.text("World!", 0, 9, 1)
>>> lcd.data(buffer)

## Referencias

[Modulo para pcd8544](https://github.com/mcauser/micropython-pcd8544 )
[Con sensor DHT](https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110)