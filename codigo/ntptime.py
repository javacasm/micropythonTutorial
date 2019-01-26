# Obtener y ajustar el tiempo desde un servidor de internet

# Tiene que estar configurada la conexion wifi

from ntptime import settime
settime()  ## Ajusta el tiempo
rtc = machine.RTC()

print(rtc.datetime())
(2019, 1, 26, 5, 19, 53, 22, 494)

## OR 

import utime
utime.localtime()


## Para ajustar la zona horaria https://forum.micropython.org/viewtopic.php?t=3675

# for time convert to second
tampon1=utime.time() 
    
# for gmt. For me gmt+3. 
# 1 hour = 3600 seconds
# 3 hours = 10800 seconds
tampon2=tampon1+10800

# for second to convert time
(year, month, mday, hour, minute, second, weekday, yearday)=utime.localtime(tampon2)
