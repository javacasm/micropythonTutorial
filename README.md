# Tutorial micropython

## ¿Por qué usar micropython?

## Empezando

[Instalación del firmware micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

1. Borramos la flash

        esptool.py  --port /dev/ttyUSB0 erase_flash
        

2. Descargamos el firmware (para el ESP8266)

    http://micropython.org/download#esp8266

3. Copiamos el firmware


    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 Descargas/esp8266-512k-20190108-v1.9.4-773-gafecc124e.bin



4. Accedemos al prompt de micropython

        screen /dev/ttyUSB0 115200
        
ó         
        picocom  /dev/ttyUSB0 -b115200


## [Web_REPL](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html)

(Para ESP de al menos 1M (no disponible en los de 0.5M))

5. Configuramos el acceso con Wep_REPL

        import webrepl_setup

Contestamos que queremos activar el acceso y establecemos una contraseña de acceso

6. Conectamos a [http://micropython.org/webrepl/](http://micropython.org/webrepl/) para acceder al cliente 

7. Nos conectamos a una red wifi llamada MicroPython_xxxxxx (donde xxxxx es parte de la MAC de nuestro ESP) (vía 192.168.4.1:8266/)

8. Pulsamos conectar en la consola de webrepl y nos pedirá la contraseña de acceso
 
9. Configuramos la conexión a una red wifi determinada (siguiendo las intrucciones de **help()** )¿se mantiene después de un reset?


        import network                              # Importamos el modulo network completo
        sta_if = network.WLAN(network.STA_IF)       # Establecemos el modo punto de acceso (AP) 
        sta_if.active(True)                         # Activamos el wifi
        sta_if.scan()                               # Escaneamos las redes disponibles
        sta_if.connect("<AP_name>", "<password>")   # Conectamos al AP
        sta_if.isconnected()                        # Comprobamos si estamos conectados


## Controlando un pin 

Hay que empezar diciendo que la nomenclatura de los pines utiliza la especificación del fabricante (Normalmente GPIO)

Para activar el led incluido en la placa ESP12 (conectado inversamente al GPIO2)

        from machine import Pin     ## Importamos la clase 
        p2 = Pin(2,Pin.OUT)         ## Usaremos el GPIO02 como salida 
        p2.on()                     ## Activamos y se apagara el led
        p2.off()                    ##

Vamos a usar ahora el [relé del shield de wemos](https://wiki.wemos.cc/products:d1_mini_shields:relay_shield)


![Rele shield](https://wiki.wemos.cc/_media/products:d1_mini_shields:relay_v2.0.0_1_16x9.jpg)

        pReleWemos = Pin(5,Pin.OUT)
        pReleWemos.on()
        pReleWemos.off()  


## Ficheros

Podemos ver el contenido del sistema de archivos con

There are two files that are treated specially by the ESP8266 when it starts up: boot.py and main.py. The boot.py script is executed first (if it exists) and then once it completes the main.py script is executed. You can create these files yourself and populate them with the code that you want to run when the device starts up.


        import os
        
        os.listdir()

        You can make directories:

        >>> os.mkdir('dir')
        And remove entries:

        >>> os.remove('data.txt')



## Trabajando con ficheros

You can use rshell, ampy, WEB_REPL, etc.

## Mo'dulos o librer'ias

[Librer'ias](https://docs.micropython.org/en/latest/library/index.html)

Podemos ver los m'odulos disponibles con 

        help('modules')
        
Y podemos obtener ayuda de objeto    concreto con 

        help(objeto)

## Wemos D1 mini

[Especificación Wemos D1](https://wiki.wemos.cc/products:d1:d1_mini)

[Esquema](https://wiki.wemos.cc/_media/products:d1:sch_d1_mini_v3.0.0.pdf)

![Pinout wemos D1](https://www.esploradores.com/wp-content/uploads/2017/01/d1-mini-esp8266.jpg)

## Recursos

[Arranque del ESP8266](https://docs.micropython.org/en/latest/esp8266/general.html#boot-process)

[Especificación del ESP8266](https://docs.micropython.org/en/latest/esp8266/general.html#technical-specifications-and-soc-datasheets)

[Tutorial de micropython para ESP32](https://www.cnx-software.com/2017/10/16/esp32-micropython-tutorials/) 

[Tutorial de micropython para ESP8266 y ESP32](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)

[CircuitPython para ESP8266](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266)

[Configuración de Wep_REPL](https://medium.com/@JockDaRock/micropython-esp8266-quick-start-part-3-repl-base-in-range-standby-72ccc5dca57d)


## Proyectos con nokia 5110

[Termometro](https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110)

[Conway Game of life](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life#configure-access-point)


