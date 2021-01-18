# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/


v = '1.5.12'
moduleName = 'MQTT_base'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)

from umqttsimple import MQTTClient, MQTTException
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

client = None
client_id = ubinascii.hexlify(machine.unique_id())

def sub_CheckTopics(topic, msg):
    myLog('Base:' + str((topic, msg)))
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

def connect_and_subscribe(topics2Subscribe,callbackFunc):
    global client, client_id
    myLog('create client')
    client = MQTTClient(client_id, config.mqtt_server)
    myLog('set callback')
    client.set_callback(callbackFunc)
    try:
        myLog('Connecting to %s MQTT broker ' % (config.mqtt_server), saveToFile = True)
        client.connect()
        myLog('connected')
        for topic in topics2Subscribe:
            myLog('subscribe 2 ' + str(topic))
            client.subscribe(topic)
            myLog('Subscribed to ' + str(topic))
        return client
    except MQTTException as e:
        myLog('MQTT exception: ' + str(e), saveToFile = True)
        #restart_and_reconnect()
        exit()

def restart_and_reconnect():
    myLog('Failed to connect to MQTT broker ' + config.mqtt_server + '. Reconnecting...')
    time.sleep(10)
    myLog('Reset...')
    machine.reset()

"""def mainMQTT(everySeconds=60):
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

"""
