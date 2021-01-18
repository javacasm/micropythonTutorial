# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/


v = '1.5.2'
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
import MQTT_base
import main_consola

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


def CheckTopics(topic, msg):
    print('MQTT-test' + str((topic, msg)))
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

def mainMQTT(everySeconds=60):
    #print(MyDateTime.setRTC())
    MQTT_base.connect_and_subscribe(topic_sub, CheckTopics) # connect and get a client reference
    last_Temp = 0 # utime.ticks_ms()
    main_consola.initBME280()
    while True :
        MQTT_base.client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            msgTime = MyDateTime.getLocalTimeHumanFormat()
            MQTT_base.client.publish(topic_subTime,msgTime)
            if main_consola.bme != None:
                temp, press, hum = main_consola.getDataBME280()
                MQTT_base.client.publish(topic_subTemp, temp)
                MQTT_base.client.publish(topic_subPress, press)
                MQTT_base.client.publish(topic_subHum, hum)
                msg = msgTime+', '+str(temp)+', '+press+', '+hum
                MQTT_base.client.publish(topic_subData, msg)
                print(msg)
            last_Temp = now
        time.sleep_ms(100)



