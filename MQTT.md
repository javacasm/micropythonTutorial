# MQTT

TODO: ¿Qué es MQTT? ¿para qué sirve? ¿Ventajas?

MQTT es un servicio sencillo y ligero



Concepto de topic y su arquitectura arbórea
## Instalación

Instalamos servidor mosquitto en la raspberry

```
sudo apt install mosquitto
```

Ejecutamos mosquitto 


Si queremos que se arranque como servicio al iniciar la raspberry, hacemos

```
sudo systemctl enable mosquitto.service
```



Para depurar el funcionamiento de mosquitto y ver los logs cuando funciona como servicio podemos usar

https://community.home-assistant.io/t/how-to-debug-mosquitto-mqtt/107709/20
http://www.steves-internet-guide.com/mosquitto-logging/
https://github.com/thomasnordquist/MQTT-Explorer

Para publicar y recibir mensajes necesitaremos las herramientas cliente, que podemos instalar con

```
sudo apt install mosquitto-clients
```


Podemos suscribirnos a un tema/topic con el comando 

```
mosquitto_sub -h servidorMQTT -t Tema
``` 

Para publicar en un "Topic" un "Mensaje" (siempre son cadenas)

```
mosquitto_pub -h servidorMQTT -t "Topic" -m "Mensaje"
```




## Ejemplos

Vamos a suscribirnos al topic "MeteoSalon/#", es decir a todos los mensajes que "cuelgen" del topic "MeteoSalon".
La opción **-v** es para que muestre más detalles sobre los mensajes

```
mosquitto_sub -h 192.168.1.200 -t "MeteoSalon/#" -v

```

y la aplicación quedará esperando hasta que se reciban mensajes con un topic compatible

Desde el mismo servidor podemos probar que funciona con la utilidad **mosquitto_pub**

```
mosquitto_pub -h 192.168.1.200 -t "MeteoSalon/led" -m "On"
```

En el servidor vemos la siguiente traza

```
1574598811: New connection from 192.168.1.200 on port 1883.
1574598811: New client connected from 192.168.1.200 as mosqpub/7375-raspberryp (c1, k60).
1574598811: Client mosqpub/7375-raspberryp disconnected.
```

y en la aplicación cliente

```
MeteoSalon/led On
```

### Ejemplo de arquitectura de topics

A medida que vamos añadiendo dispositivos y enviado más mensajes se puede complicar el árbol de topics

Para ellos es mejor usar una arquitectura. Por ejemplo esta [tomada del blog de ricardo veal](https://ricveal.com/blog/sonoff-mqtt/)


    state_topic: "stat/sonoff/1/POWER"
    command_topic: "cmnd/sonoff/1/POWER"
    availability_topic: "tele/sonoff/1/LWT"

Telemetría para que cuenten sus cosas ¿Por ejemplo los sensores?
Command para peticiones ¿request?
Stat para confirmaciones de estados




## Recursos

[Instalación de mosquito en la Raspberry)[https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/]

https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266

https://geekytheory.com/tutorial-raspberry-pi-gpio-y-mqtt-parte-1
