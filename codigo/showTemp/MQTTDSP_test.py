# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

# v1.4.5

from umqttsimple import MQTTClient
import ubinascii
import machine
import time         # Para las esperas
import utime
import neopixel
import time
import ntptime
import NeoPixelTHO  # Relacioniado con el ledRGB
import helpFiles    # para free y df
import MyDateTime
import Wemos
import showTemp

client_id = ubinascii.hexlify(machine.unique_id())

## topic_sub = b'MeteoDSP' Para probar
topic_sub = b'MeteoSalon'
topic_subFree = topic_sub + b'/freeDSP'
topic_subMem = topic_sub + b'/memDSP'
topic_subLed = topic_sub + b'/ledDSP'
topic_subTime = topic_sub + b'/TimeDSP'
topic_subData = topic_sub + b'/SensorDataDSP'
topic_pub = b'hello'

mqtt_server = '192.168.1.200'


# Builtin Led
led = machine.Pin(Wemos.BUILTIN_LED,machine.Pin.OUT)

def sub_CheckTopics(topic, msg):
    print((topic, msg))
    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
            led.off()
        else:
            print('Led:Off')
            led.on()
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
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subFree))
  return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


def mainBeta(everySeconds=60):
    print(MyDateTime.setRTC())
    tm = showTemp.initLedMatrix()
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0 # utime.ticks_ms()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            client.publish(topic_subTime,MyDateTime.getLocalTimeHumanFormat())
            msg = showTemp.getSensorsData(tm)
            if msg != None:
                client.publish(topic_subData, msg)
                print(msg)
            last_Temp = now                
        time.sleep_ms(100) # Podriamos quitarlo

