# from https://github.com/hosaka/micropython-st7735
# MicroPython ST7735 TFT display driver example usage

from machine import Pin, SPI
from tft import TFT_GREEN
import Wemos

v = '0.1'

# DC       - RS/DC data/command flag
# CS       - Chip Select, enable communication
# RST/RES  - Reset
# dc  = Pin('GP3', Pin.OUT)
dc  = Pin(Wemos.D3, Pin.OUT)
cs  = Pin(Wemos.D7, Pin.OUT)
rst = Pin(Wemos.D4, Pin.OUT)

# SPI Bus (CLK/MOSI/MISO)
# check your port docs to see which Pins you can use
# spi = SPI(0, mode=SPI.MASTER, baudrate=8000000, polarity=1, phase=0)
# https://docs.micropython.org/en/latest/esp8266/quickref.html#software-spi-bus

# TFT object, this is ST7735R green tab version
tft = TFT_GREEN(128, 160, spi, dc, cs, rst)

# init TFT
tft.init() # error

# start using the driver
tft.clear(tft.rgbcolor(255, 0, 0))