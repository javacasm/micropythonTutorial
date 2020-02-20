# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

v = '0.9.3'

from umqttsimple import MQTTClient
import ubinascii
import machine
import time         # Para las esperas
import utime
import ntptime
import MyDateTime
import BateryLevel_ttgo_esp32


client_id = ubinascii.hexlify(machine.unique_id())

## topic_sub = b'MeteoExt' Para probar
topic_sub = b'MeteoSalon'
topic_subBat = topic_sub + b'/batTTYGO'
topic_subLed = topic_sub + b'/ledTTYGO'

mqtt_server = '192.168.1.100'

# Encendemos la backlight de la pantalla
backLight = machine.Pin(4,machine.Pin.OUT)

def sub_CheckTopics(topic, msg):
    print((topic, msg))
    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
            backLight.on()
        else:
            print('Led:Off')
            backLight.off()

def connect_and_subscribe():
  global client, client_id, mqtt_server, topic_sub,  topic_subLed
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_CheckTopics)
  client.connect()
  client.subscribe(topic_subLed)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subLed))
  return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def mainBeta(everySeconds=60):
    print(MyDateTime.setRTC())
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0 # utime.ticks_ms()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            batLevel = BateryLevel_ttgo_esp32.batLevel()
            client.publish(topic_subBat, str(batLevel))
            last_Temp = now                
        time.sleep_ms(100) # Podriamos quitarlo

