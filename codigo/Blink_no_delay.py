# Mirar async task https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md

import utime

last_led = utime.ticks_ms()

while True:
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_led) > 500:
        last_led = now
        
        
