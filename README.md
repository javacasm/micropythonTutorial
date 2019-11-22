# Tutorial micropython

Tutorial/cookbook de nivel inicial de micropython sobre todo para ESPs

José Antonio Vacas @javacasm

![Licencia CC](./images/Licencia_CC.png)

## ¿Por qué usar micropython?

Micropython es una versión reducida del lenguaje python, pensado para que pueda ser ejecutado en dispositivos con menor capacidad de almacenamiento y procesamiento, como por ejemplo micro:bit o los distintos ESP

Al ser python un lenguaje interpretado lo que haremos será flasear el dispositivo con un firmware capaz de interpretarlo y al que podremos ir enviando los ficheros .py con el código python

## Empezando


Para flashear nuestro ESP8266 necesitamos la herramienta esptool. Nos aseguramos de tener instalado **pip** para python 3 con (más información sobre le herramienta pip en [este enlace](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/	))

		sudo apt install python3-pip
	
y ahora instalamos la herramienta **esptool** para flashear nuestro dispositivo

		pip3 install esptool


[Instalación del firmware micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) (Para los dispositivos esp8266 tenemos que arrancarlo con el pin GPIO00 conectado a GND)

1. Borramos la flash

		esptool.py  --port /dev/ttyUSB0 erase_flash


2. Descargamos el firmware (para el ESP8266) de http://micropython.org/download#esp8266 teniendo en cuenta la memoria de nuestro dispositivo (512Kb en el ejemplo)

3. Conectamos nuestra placa por USB y la flasheamos la placa con el firmware

		esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 ~/Descargas/esp8266-512k-20191118-v1.11-580-g973f68780.bin


4. Accedemos al prompt de micropython para ver que todo ha ido bien

		screen /dev/ttyUSB0 115200
ó

		picocom  /dev/ttyUSB0 -b115200


Esta forma de conexión se denomina REPL ("Read-Eval-Print-Loop"): una shell de python que nos permite trabajar y probar nuestro código de manera interactiva

Incluye algunas de utilidades a las que estamos acostumbrados en las shels, como recuperar los [comandos ya usados](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#input-history) usando las teclas del curso arriba y abajo o el [completado de método y nombre con la tecla TAB](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#tab-completion). Si queremos [pegar código](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#paste-mode) podemos hacerlo pulsando antes Ctrl-E y [más opciones](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#other-control-commands)

Por defecto todo dispositivo micropython crea una red wifi llamada ESSID MicroPython-xxxxxx con ip 192.168.4.1 y contraseña **micropythoN** ([detalles](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#wifi))

## [Web_REPL](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html)

Web_REPL nos permite acceder a una shell REPL vía wifi

Para ESP de al menos 1M (no disponible en los de 512Kb))

5. Configuramos el acceso con Wep_REPL

```python
import webrepl_setup
```

Contestamos que queremos activar el acceso pulsando E y establecemos una contraseña de acceso. A partir de ahora quedará activado en cada arranque.

6. Conectamos a [http://micropython.org/webrepl/](http://micropython.org/webrepl/) para acceder al cliente

7. Nos conectamos a una red wifi llamada MicroPython_xxxxxx (donde xxxxx es parte de la MAC de nuestro ESP) (vía 192.168.4.1:8266/)

8. Pulsamos conectar en la consola de webrepl y nos pedirá la contraseña de acceso

9. Configuramos la conexión a una red wifi determinada (siguiendo las intrucciones de **help()**  y ayudándonos de la tecla TAB para completar) Esta configuración se mantiene después de un reset. Al ser interactivo, cada línea tiene una salida indicando el resultado

```python
import network                              # Importamos el modulo network completo
sta_if = network.WLAN(network.STA_IF)       # Establecemos el modo punto de acceso (AP)
sta_if.active(True)                         # Activamos el wifi
sta_if.scan()                               # Escaneamos las redes disponibles
sta_if.connect("<AP_name>", "<password>")   # Conectamos al AP
sta_if.isconnected()                        # Comprobamos si estamos conectados
sta_if.ifconfig()                           # Vemos la ip ('192.168.1.137', '255.255.255.0', '192.168.1.1', '87.216.1.65')
```


## Controlando un pin

Hay que empezar diciendo que la nomenclatura de los pines utiliza la especificación del fabricante (Normalmente GPIO)

Para activar el led incluido en la placa ESP12 (conectado inversamente al GPIO2)

```python
from machine import Pin     ## Importamos la clase
p2 = Pin(2,Pin.OUT)         ## Usaremos el GPIO02 como salida
p2.on()                     ## Activamos y se apagara el led
p2.off()                    ##
```

Vamos a usar ahora el [relé del shield de wemos](https://wiki.wemos.cc/products:d1_mini_shields:relay_shield)


![Rele shield](https://wiki.wemos.cc/_media/products:d1_mini_shields:relay_v2.0.0_1_16x9.jpg)

```python
pReleWemos = Pin(5,Pin.OUT)
pReleWemos.on()
pReleWemos.off()  
```


## Ficheros

Podemos ver el contenido del sistema de archivos con

There are two files that are treated specially by the ESP8266 when it starts up: boot.py and main.py. The boot.py script is executed first (if it exists) and then once it completes the main.py script is executed. You can create these files yourself and populate them with the code that you want to run when the device starts up.

```python
import os
os.listdir()
```

Crear directorios:

```python
os.mkdir('dir')
```
O borrar archivos

```python
os.remove('data.txt')
```



## Trabajando con ficheros

You can use rshell, ampy, WEB_REPL, etc.

## Módulos o librerías

[Librerías](https://docs.micropython.org/en/latest/library/index.html)

Podemos ver los módulos disponibles con

        help('modules')

Y podemos obtener ayuda de objeto concreto con

        help(objeto)

## IDEs

### uPyCraft


[Instalación](https://randomnerdtutorials.com/install-upycraft-ide-linux-ubuntu-instructions/)
[Tutorial](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)

[Descargar uPyCraft](https://randomnerdtutorials.com/uPyCraftLinux)

# Placas


## ESP12


![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP8266-ESP-12E-chip-pinout-gpio-pin.png?ssl=1)


```python
# Ejemplo parpadeo led incluido en la placa (que tiene el estado invertido)

import machine                                                                                                                            
led = machine.Pin(1,machine.Pin.OUT)                                                                                                      
led.off()                                                                                                                                 
led.on()   

```

## Wemos D1 mini

[Especificación Wemos D1](https://wiki.wemos.cc/products:d1:d1_mini)

[Esquema](https://wiki.wemos.cc/_media/products:d1:sch_d1_mini_v3.0.0.pdf)

![Pinout wemos D1](https://www.esploradores.com/wp-content/uploads/2017/01/d1-mini-esp8266.jpg)


```python
# Ejemplo parpadeo led incluido en la placa (que tiene el estado invertido)

import machine                                                                                                                            
led = machine.Pin(1,machine.Pin.OUT)                                                                                                      
led.off()                                                                                                                                 
led.on()   

```

## NodeMCU

![Pinout NodeMCU](https://external-preview.redd.it/nUkII641DY7O3_gbcxq2W4RlYgRI1jBwaHHoJLf2kKE.png?width=960&crop=smart&auto=webp&s=879b177f118c0b0aa8fe21b1ffb96f581b3bc450)


```python
# Ejemplo parpadeo led incluido en la placa (que tiene el estado invertido)

import machine                                                                                                                            
led = machine.Pin(1,machine.Pin.OUT)                                                                                                      
led.off()                                                                                                                                 
led.on()   

```

## ESP01 (ESP8266)

![Pinout ESP8266](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP-01-ESP8266-pinout-gpio-pin.png?ssl=1)


```python
# Ejemplo parpadeo led incluido en la placa (que tiene el estado invertido)

import machine                                                                                                                            
led = machine.Pin(1,machine.Pin.OUT)                                                                                                      
led.off()                                                                                                                                 
led.on()   

```

## Otras placas


[Colección de placas](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)

[Más detalles sobre las placas](https://www.aprendiendoarduino.com/tag/modemcu/)

## Recursos

[Multitud de librer'ias](https://github.com/micropython/micropython-lib)

[Arranque del ESP8266](https://docs.micropython.org/en/latest/esp8266/general.html#boot-process)

[Especificación del ESP8266](https://docs.micropython.org/en/latest/esp8266/general.html#technical-specifications-and-soc-datasheets)

[Tutorial de micropython para ESP32](https://www.cnx-software.com/2017/10/16/esp32-micropython-tutorials/)

[Tutorial de micropython para ESP8266 y ESP32](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)

[CircuitPython para ESP8266](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266)

[Configuración de Wep_REPL](https://medium.com/@JockDaRock/micropython-esp8266-quick-start-part-3-repl-base-in-range-standby-72ccc5dca57d)


## Proyectos con nokia 5110

[Termometro](https://github.com/mcauser/MicroPython-ESP8266-DHT-Nokia-5110)

[Conway Game of life](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life#configure-access-point)
