# MQTT

MQTT es un servicio sencillo y ligero

¿Ventajas?

Concepto de topic y su arquitectura arbórea

Instalamos servidor mosquitto en la raspberry

sudo apt install mosquitto

Ejecutamos mosquitto 
TODO: ¿Cómo hacer que arranque sólo?

Para publicar

    mosquitto_pub -h servidorMQTT -t Topic -m Mensaje

## Ejemplos

Desde el mismo servidor podemos probar que funciona con la utilidad **mosquitto_pub**

    mosquitto_pub -h 192.168.1.200 -t "MeteoSalon/led" -m "On"

En el servidor vemos la siguiente traza

1574598811: New connection from 192.168.1.200 on port 1883.
1574598811: New client connected from 192.168.1.200 as mosqpub/7375-raspberryp (c1, k60).
1574598811: Client mosqpub/7375-raspberryp disconnected.

Podemos suscribirnos a un tema/topic con el comando 

    mosquitto_sub -h servidorMQTT -t Tema 

## Recursos

https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266

https://geekytheory.com/tutorial-raspberry-pi-gpio-y-mqtt-parte-1
