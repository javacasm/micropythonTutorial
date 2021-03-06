# Sonoff

## Pinout

### Sonoff basic

![](../images/sonoff_basic_pinout.jpg)

TODO: ¿qué es sonoff?

[Flashing micropython](https://medium.com/cloud4rpi/getting-micropython-on-a-sonoff-smart-switch-1df6c071720a)

http://blog.thebestjohn.com/posts/sonoff-micropython-wonderland/

### Sonoff Pow

Dispositivo que además de la activación remota mide el consumo del dispositivo al que está conectado

Para ello usa un HLW8012 ([Enlace](https://tinkerman.cat/post/hlw8012-ic-new-sonoff-pow))

[Modulo con HLW8032](https://es.aliexpress.com/item/33029897807.html) [Libreria](https://github.com/xoseperez/hlw8012)

![conexion](https://microsolution.com.pk/wp-content/uploads/2019/08/HLW8012_High-Precision_Energy_Metering_Module_Arduino_Energy_Monitoring.png)

[Descripción](https://tinkerman.cat/post/the-sonoff-pow/)

[Pagina del producto](https://www.itead.cc/wiki/Sonoff_Pow)

[Esquemático](https://www.itead.cc/wiki/images/5/52/Sonoff_POW_Schematic.pdf)

[User guide](http://ewelink.coolkit.cc/?p=188)

## Control de un sonoff vía MQTT

[codigo](https://github.com/kfricke/micropython-sonoff-switch) Además usa thread para ejecutar varias tareas

## Nodo a partir de Sonoff basic

* Neopixel conectado al pin del LED (GPIO13) (En una primera versión para no des-soldar el led usaremos el GPIO14)
* Rele en GPIO12
* DHT22 en GPIO14
* BME280 via I2C en TX/RX? Segun [el enlace](https://github.com/arendst/Tasmota/issues/1865)

```
BME280-3.3V -> Sonoff-3.3V
BME280-GND -> Sonoff-GND
BME280-SCL -> Sonoff-TX
BME280-SDA -> Sonoff-RX

GPIO1 Serial Out (TX)-> I2C SCL
GPIO3 Serial In (RX)-> I2C SDA
```

## micropython en sonoff

```
esptool.py --port /dev/ttyACM0  write_flash -fs 1MB -fm dout 0x0 firmware.bin
```


## Sonoff RF 433MHz

### Pulsadores

[Producto](https://www.banggood.com/Wireless-Remote-Transmitter-Sticky-RF-TX-Smart-For-Home-Living-Room-Bedroom-433MHZ-86-Wall-Panel-Works-With-SONOFF-RFRFR3SlampheriFan034CHProR2TX-Series433-RF-Bridge-p-1540771.html)

### Bridge RF

[Producto](https://www.banggood.com/SONOFF-RF-Bridge-WiFi-433-MHz-Replacement-Smart-Home-Automation-Universal-Switch-p-1179900.html)




[Detalles y modificaciones](https://github.com/arendst/Tasmota/wiki/Sonoff-RF-Bridge-433)

[How to Flash](https://github.com/arendst/Tasmota/wiki/How-to-Flash-the-RF-Bridge)

[Funcionamiento del bridge](https://hometechhacker.com/using-a-sonoff-rf-bridge-to-expand-your-smarthome/)

### Add RF to sonoff

[Add RF to sonoff](https://tinkerman.cat/post/adding-rf-to-a-non-rf-itead-sonoff/)

## Controlando sonoff con MQTT

[Controlando sonoff con MQTT](https://github.com/kfricke/micropython-sonoff-switch)
 
## Referencia

[Sonoff y mqtt](https://ricveal.com/blog/sonoff-mqtt/)
