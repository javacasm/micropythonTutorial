# Ejemplo de uso de pantalla Nokia 5119 con pcd8544
# https://github.com/mcauser/micropython-pcd8544
# Tomado de https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110/blob/master/readme.md


# Test en http://micropython.org/webrepl/#192.168.1.46:8266/

## TODO
# Fuente 4x5 https://forum.micropython.org/viewtopic.php?t=3839
# utilidad para usar otros fonts https://github.com/peterhinch/micropython-font-to-py

import pcd8544
from machine import Pin, SPI
import time
lcd = None
fb = None
buffer = None
bl = None
def init():
    global lcd
    global bl
    spi = SPI(1)
    spi.init(baudrate=2000000, polarity=0, phase=0)
    cs = Pin(2)
    dc = Pin(15)
    rst = Pin(0)

    # backlight on
    bl = Pin(12, Pin.OUT, value=1)

    lcd = pcd8544.PCD8544(spi, cs, dc, rst)

    lcd.init()
    print('LCD init')
    lcd.contrast(50)
def contrast(value):
    global lcd
    lcd.contrast(value)
        
def blOn():
    global bl
    bl.off()

def blOff():
    global bl
    bl.on()

def test():
    global lcd
    # bitmap smiley (horzontal msb)
    lcd.clear()
    # draw 8x16 in bank 0 (rows 0..7)
    lcd.position(0, 0)
    lcd.data(bytearray(b'\xE0\x38\xE4\x22\xA2\xE1\xE1\x61\xE1\x21\xA2\xE2\xE4\x38\xE0\x00'))
    # draw 8x16 in bank 1 (rows 8..15)
    lcd.position(0, 1)
    lcd.data(bytearray(b'\x03\x0C\x10\x21\x21\x41\x48\x48\x48\x49\x25\x21\x10\x0C\x03\x00'))
    time.sleep(2)
    print('apagamos')
    # toggle display, image persists in DDRAM
    lcd.power_off()
    time.sleep(2)
    print('encendemos')
    lcd.power_on()

def initFB():
    global lcd
    global buffer
    global fb
    import framebuf
    print('Init framebuffer')
    buffer = bytearray((lcd.height // 8) * lcd.width)
    fb = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)

def showText(x,y,texto):
    global lcd
    global fb
    global buffer
    fb.text(texto, x, y, 1)
    lcd.data(buffer)

def clear():
    global lcd
    fb.fill(0)
    lcd.clear()

def testFB():

    # https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110
    global lcd
    global fb
    
    print('test framebuffer')

    # Light every pixel:
    print('todo a 1')
    fb.fill(1)
    lcd.data(buffer)
    time.sleep(2)
    #Clear screen:
    print('todo a 0')
    fb.fill(0)
    lcd.data(buffer)
    time.sleep(2)
    print('Print Hello, World! using the 8x8 font:')

    fb.text("Hello,", 0, 0, 1)
    fb.text("World!", 0, 9, 1)
    lcd.data(buffer)
