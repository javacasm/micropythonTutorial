# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/


v = '1.4.6'
moduleName = 'MQTT_test'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)

from umqttsimple import MQTTClient
import ubinascii
import machine
import ntptime
import time         # Para las esperas
import utime
#import Wemos        # Facilita el identificar los pines
#import MeteoSalon   # Relacionado con los dispositivos conectados
#import NeoPixelTHO  # Relacioniado con el ledRGB
#import helpFiles    # para free y df
import MyDateTime

import config
import main_consola

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'MeteoSalon'
topic_subFree = topic_sub + b'/free'
topic_subMem = topic_sub + b'/mem'
topic_subLed = topic_sub + b'/led'
topic_subTime = topic_sub + b'/Time'
topic_subTemp = topic_sub + b'/Temp'
topic_subHum = topic_sub + b'/Hum'
topic_subPress = topic_sub + b'/Press'
topic_subLedRGB = topic_sub + b'/ledRGB'
topic_subData = topic_sub + b'/SensorData'
topic_pub = b'hello'

def sub_CheckTopics(topic, msg):
    print((topic, msg))
"""    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
            MeteoSalon.led.off()
        else:
            print('Led:Off')
            MeteoSalon.led.on()
    elif topic == topic_subLedRGB:      ## Check for RGB Topic
        MeteoSalon.color(msg)
    elif topic == topic_subFree:        ## Check for free memory
        freeMem = helpFiles.free()
        client.publish(topic_subMem, str(freeMem))"""

def connect_and_subscribe():
    global client, client_id, topic_sub, topic_subLedRGB, topic_subLed
    client = MQTTClient(client_id, config.mqtt_server)
    client.set_callback(sub_CheckTopics)
    try:
        client.connect()
        client.subscribe(topic_subFree)
        client.subscribe(topic_subLed)
        client.subscribe(topic_subLedRGB)
        print('Connected to %s MQTT broker, subscribed to %s topic' % (config.mqtt_server, topic_subFree))
        return client
    except:
        restart_and_reconnect()

def restart_and_reconnect():
    print('Failed to connect to MQTT broker ' + config.mqtt_server + '. Reconnecting...')
    time.sleep(10)
    machine.reset()

def mainMQTT(everySeconds=60):
    #print(MyDateTime.setRTC())
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0 # utime.ticks_ms()
    main_consola.initBME280()
    while True :
        client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            msgTime = MyDateTime.getLocalTimeHumanFormat()
            client.publish(topic_subTime,msgTime)
            if main_consola.bme != None:
                temp, press, hum = main_consola.getDataBME280()
                client.publish(topic_subTemp, temp)
                client.publish(topic_subPress, press)
                client.publish(topic_subHum, hum)
                msg = msgTime+', '+str(temp)+', '+press+', '+hum
                client.publish(topic_subData, msg)
                print(msg)
            last_Temp = now
        time.sleep_ms(100)


