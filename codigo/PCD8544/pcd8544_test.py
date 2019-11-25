# Ejemplo de uso de pantalla Nokia 5119 con pcd8544
# Tomado de https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110/blob/master/readme.md


from machine import Pin, SPI

import time
import pcd8544

spi = SPI(1, baudrate=80000000, polarity=0, phase=0)

cs = Pin(5)
dc = Pin(15)
rst = Pin(16)

bl = Pin(12, Pin.OUT, value=1) # Backlight On
lcd = pcd8544.PCD8544(spi, cs, dc, rst)

import framebuf

buffer = bytearray((lcd.height // 8) * lcd.width)
framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)

# Light every pixel:

framebuf.fill(1)
lcd.data(buffer)

#Clear screen:

framebuf.fill(0)
lcd.data(buffer)

# Print Hello, World! using the 8x8 font:

framebuf.text("Hello,", 0, 0, 1)
framebuf.text("World!", 0, 9, 1)
lcd.data(buffer)
