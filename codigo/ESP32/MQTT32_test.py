# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

# v1.3

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
import meteoExt

client_id = ubinascii.hexlify(machine.unique_id())

## topic_sub = b'MeteoExt' Para probar
topic_sub = b'MeteoSalon'
topic_subFree = topic_sub + b'/freeExt'
topic_subMem = topic_sub + b'/memExt'
topic_subLed = topic_sub + b'/ledExt'
topic_subTime = topic_sub + b'/TimeExt'
topic_subTemp = topic_sub + b'/TempExt'
topic_subHum = topic_sub + b'/HumExt'
topic_subPress = topic_sub + b'/PressExt'
topic_subLedRGB = topic_sub + b'/ledRGBExt'
topic_pub = b'hello'

mqtt_server = '192.168.1.200'

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
    last_Temp = utime.ticks_ms()
    bme = meteoExt.initSensor()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            last_Temp = now
            client.publish(topic_subTime,MyDateTime.getLocalTimeHumanFormat())
            if bme != None:
                client.publish(topic_subTemp, bme.temperature)
                client.publish(topic_subPress, bme.pressure)
                client.publish(topic_subHum, bme.humidity)
        time.sleep_ms(200)

