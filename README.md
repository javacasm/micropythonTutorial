# Tutorial micropython

## ¿Por qué usar micropython?

## Empezando

Instalación del firmware micropython

1. Borramos la flash

        esptool.py  --port /dev/ttyUSB0 erase_flash
        

2. Descargamos el firmware (para el ESP8266)

    http://micropython.org/download#esp8266

3. Copiamos el firmware


    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 Descargas/esp8266-512k-20190108-v1.9.4-773-gafecc124e.bin

## Recursos

[Tutorial de micropython para ESP32](https://www.cnx-software.com/2017/10/16/esp32-micropython-tutorials/) 

[Tutorial de micropython para ESP8266 y ESP32](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)

[CircuitPython para ESP8266](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266)


## Proyectos con nokia 5110

[Termometro](https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110)

[Conway Game of life](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life#configure-access-point)


