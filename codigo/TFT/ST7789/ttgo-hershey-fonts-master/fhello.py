import sys
import time
import machine
import st7789py as st7789
import uos
import random

import ftext

v = '1.8'

def pick_item(sequence):
    div = 0x3fffffff // len(sequence)
    return sequence[random.getrandbits(30) // div]

display = None

def init():
    bl = machine.Pin(4, machine.Pin.OUT)
    bl.on()

    spi = machine.SPI(
        2,
        baudrate=30000000,
        polarity=1,
        phase=1,
        sck=machine.Pin(18),
        mosi=machine.Pin(19))
    
    global display

    display = st7789.ST7789(
        spi, 135, 240,
        reset=machine.Pin(23, machine.Pin.OUT),
        cs=machine.Pin(5, machine.Pin.OUT),
        dc=machine.Pin(16, machine.Pin.OUT))

    display.init()
    clear()

def clear():
    global display
    display.fill(st7789.BLACK)

fonts = ["astrol.fnt", "cyrilc.fnt", "gotheng.fnt", "greeks.fnt",
         "italicc.fnt", "italiccs.fnt", "meteo.fnt", "music.fnt",
         "romanc.fnt", "romancs.fnt", "romand.fnt", "romanp.fnt",
         "romans.fnt", "romant.fnt", "scriptc.fnt", "scripts.fnt"]

def test():
    row = 32
    while True:
        color = st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8))

        font_file = "/fonts/" + pick_item(fonts)
        ftext.text(display, font_file, "Hello!", row, 0, color, 2.0, True)

        row += 32

        if row > 192: 
            display.fill(st7789.BLACK)
            row = 0

def text(font, text, row, column, color = st7789.WHITE, scale = 1.0, rotate = False):
    font_file = "/fonts/" + font
    global display
    ftext.text(display, font_file, text, row, column, color, scale, rotate)