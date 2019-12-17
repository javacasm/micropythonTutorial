# MQTT

TODO: ¿Qué es MQTT? ¿para qué sirve? ¿Ventajas?

MQTT es un servicio sencillo y ligero



Concepto de topic y su arquitectura arbórea

Instalamos servidor mosquitto en la raspberry

```
sudo apt install mosquitto
```

Ejecutamos mosquitto 
TODO: ¿Cómo hacer que arranque sólo?

Para publicar

```
mosquitto_pub -h servidorMQTT -t Topic -m Mensaje
```

## Ejemplos

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

Podemos suscribirnos a un tema/topic con el comando 

```
mosquitto_sub -h servidorMQTT -t Tema
``` 


### Ejemplo de arquitectura de topics


    state_topic: "stat/sonoff/1/POWER"
    command_topic: "cmnd/sonoff/1/POWER"
    availability_topic: "tele/sonoff/1/LWT"

Telemetria para que cuenten sus cosas ¿Por ejemplo los sensores?
Command para peticiones ¿request?
Stat para confirmaciones de estados


[tomado de aqui](https://ricveal.com/blog/sonoff-mqtt/)

## Recursos

https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266

https://geekytheory.com/tutorial-raspberry-pi-gpio-y-mqtt-parte-1
