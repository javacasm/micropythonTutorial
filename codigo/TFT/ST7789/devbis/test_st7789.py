# code for micropython 1.10 on esp8266

import random

import machine
import st7789py as st7789
import time

v = '0.6.4'

def main2():
    bl = machine.Pin(4, machine.Pin.OUT)
    bl.value(1)

    spi = machine.SPI(2, baudrate=30000000, polarity=1,phase=1,
        sck=machine.Pin(18), mosi=machine.Pin(19))

    display = st7789.ST7789(
        spi, 135, 240,
        reset=machine.Pin(23, machine.Pin.OUT),
        cs=machine.Pin(5, machine.Pin.OUT),
        dc=machine.Pin(16, machine.Pin.OUT))

    display.init()
    display.pixel(120, 120, st7789.YELLOW)
    time.sleep(1)
    while True:
        display.fill(
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ),
        )
        # Pause 2 seconds.
        time.sleep(2)

def main():
    spi = machine.SPI(2, baudrate = 40000000, polarity = 1, phase = 1,
        sck=machine.Pin(18), mosi=machine.Pin(19) )
    display = st7789.ST7789(
        spi, 135, 240,
        reset = machine.Pin(23, machine.Pin.OUT),
        dc = machine.Pin(16, machine.Pin.OUT),
        cs = machine.Pin(5, machine.Pin.OUT))

    display.init()
    display.pixel(120, 120, st7789.YELLOW)
    time.sleep(1)
    while True:
        display.fill(
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ),
        )
        # Pause 2
        # 0.01 seconds.
        time.sleep_ms(10)
