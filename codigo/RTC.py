# Cuidados a tener https://docs.micropython.org/en/latest/esp8266/general.html#real-time-clock
from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # set a specific date and time
rtc.datetime() # get date and time
