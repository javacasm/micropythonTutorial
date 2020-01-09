# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

from umqttsimple import MQTTClient
import ubinascii
import machine
import Wemos        # Facilita el identificar los pines
import time         # Para las esperas
import helpFiles    # para free y df
import utime
import caldera_test

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'MeteoSalon'
topic_subCalderaStatus = topic_sub + b'/calderaStatus'
topic_subCaldera = topic_sub + b'/caldera'
topic_subFree = topic_sub + b'/free'
topic_subMem = topic_sub + b'/mem'
topic_subLedRGB = topic_sub + b'/ledRGB'

mqtt_server = '192.168.1.100'


def sub_CheckTopics(topic, msg):
    global client
    print((topic, msg))
    if topic == topic_subCaldera:     # Check for Led Topic
        if msg == b'On':
            caldera_test.enciendeCaldera()
        else:
            caldera_test.apagaCaldera()
        showCalderaStatus()
    elif topic == topic_subFree:        ## Check for free memory
        freeMem = helpFiles.free()
        client.publish(topic_subMem, str(freeMem))

def connect_and_subscribe():
  global client, client_id, mqtt_server, topic_sub, topic_subLedRGB, topic_subLed
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_CheckTopics)
  client.connect()
  client.subscribe(topic_subFree)
  client.subscribe(topic_subCaldera)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subCaldera))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def showCalderaStatus():
   msg = caldera_test.checkCaldera()
   if msg == 'On':
       print('Caldera:On')
       client.publish(topic_subLedRGB, "Red")
   else:
       print('Caldera:Off')
       client.publish(topic_subLedRGB, "Black")
   client.publish(topic_subCalderaStatus, msg)
   
def mainBeta(everySeconds=60):
    global client
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0
    showCalderaStatus()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            last_Temp = now
            showCalderaStatus()
        time.sleep_ms(100)

