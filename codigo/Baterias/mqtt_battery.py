# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

v = '0.9'

from umqttsimple import MQTTClient
import ubinascii
import machine
import time         # Para las esperas
import utime
import time
import ntptime
import MyDateTime


client_id = ubinascii.hexlify(machine.unique_id())

## topic_sub = b'MeteoExt' Para probar
topic_sub = b'MeteoSalon'
topic_subBat = topic_sub + b'/batTTYGO'
topic_subLed = topic_sub + b'/ledTTYGO'

mqtt_server = '192.168.1.100'

# LedRGBN
ledRGB = neopixel.NeoPixel(machine.Pin(17),1) # Led RGB through the Hole en pin GPIO17

# Builtin Led
led = machine.Pin(5,machine.Pin.OUT)

def sub_CheckTopics(topic, msg):
    print((topic, msg))
    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
            led.off()
        else:
            print('Led:Off')
            led.on()
    elif topic == topic_subLedRGB:      ## Check for RGB Topic
        ledRGB[0]=NeoPixelTHO.colorByName(msg)
        ledRGB.write()
    elif topic == topic_subFree:        ## Check for free memory
        freeMem = helpFiles.free()
        client.publish(topic_subMem, str(freeMem))

def connect_and_subscribe():
  global client, client_id, mqtt_server, topic_sub, topic_subLedRGB, topic_subLed
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_CheckTopics)
  client.connect()
  client.subscribe(topic_subFree)
  client.subscribe(topic_subLed)
  client.subscribe(topic_subLedRGB)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subFree))
  return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


def mainBeta(everySeconds=60):
    print(MyDateTime.setRTC())
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0 # utime.ticks_ms()
    bme = meteoExt.initSensor()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            client.publish(topic_subTime,MyDateTime.getLocalTimeHumanFormat())
            if bme != None:
                client.publish(topic_subTemp, bme.temperature)
                client.publish(topic_subPress, bme.pressure)
                client.publish(topic_subHum, bme.humidity)
            last_Temp = now                
        time.sleep_ms(100) # Podriamos quitarlo

