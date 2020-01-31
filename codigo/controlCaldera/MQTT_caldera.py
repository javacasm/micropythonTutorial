# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

v = '1.2.3'

from umqttsimple import MQTTClient
import ubinascii
import machine
import Wemos        # Facilita el identificar los pines
import time         # Para las esperas
import helpFiles    # para free y df
import utime
import caldera_test
import MyDateTime
from Utils import myLog

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'MeteoSalon'
topic_subCalderaStatus = topic_sub + b'/calderaStatus'
topic_subCaldera = topic_sub + b'/caldera'
topic_subFree = topic_sub + b'/free'
topic_subMem = topic_sub + b'/mem'
topic_subLedRGB = topic_sub + b'/ledRGB'
topic_subBatRaw = topic_sub + b'/CalBatteryRaw'
topic_subBatVolt = topic_sub + b'/CalBatteryVolt'

mqtt_server = '192.168.1.100'

def sub_CheckTopics(topic, msg):
    global client
    try:
        myLog("MQTT < " + str(topic.decode("utf-8")) + ':' + str(msg.decode("utf-8")))
        if topic == topic_subCaldera:     # Check for Led Topic
            if msg == b'On':
                caldera_test.enciendeCaldera()
            else:
                caldera_test.apagaCaldera()
            showSetCalderaStatus()
        elif topic == topic_subFree:        ## Check for free memory
            freeMem = helpFiles.free()
            publicaMQTT(topic_subMem, str(freeMem))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        myLog('Error checking topics>' + str(e))

def connect_and_subscribe():
    global client, client_id, mqtt_server, topic_sub, topic_subLedRGB, topic_subLed
    try:
        client = MQTTClient(client_id, mqtt_server)
        client.set_callback(sub_CheckTopics)
        client.connect()
        client.subscribe(topic_subFree)
        client.subscribe(topic_subCaldera)
        myLog('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subCaldera))
        return client
    except KeyboardInterrupt:
        pass        
    except Exception as e:
        myLog('Connect&Subscribe>'+str(e))
        restart_and_reconnect()

def restart_and_reconnect():
    myLog('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(5)
    myLog('Reset!!')
    machine.reset()

def publicaMQTT(topic,msg):
    global client
    try:
        myLog('MQTT > ' + str(topic.decode("utf-8"))+ ':' + str(msg.decode("utf-8")))    
        client.publish(topic,msg) # qos = 1 
    except KeyboardInterrupt:
        pass        
    except Exception as e:
        myLog('Publish>' + str(e))

def showSetCalderaStatus():
    global client
    state = caldera_test.checkCaldera()
    publicaMQTT(topic_subCalderaStatus, state.encode("utf-8"))
    # myLog('Caldera: '+state)


def mainBeta(everySeconds=10):
    global client
    client = connect_and_subscribe() # connect and get a client reference
    last_Temp = 0
    showSetCalderaStatus()
    adc = machine.ADC(0)
    while True :
        try:
            client.check_msg() # Check por new messages and call the callBack function
        except KeyboardInterrupt:
            pass
        except Exception as e:
            myLog('Error check_msg: ' + str(e))
            restart_and_reconnect()
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            last_Temp = now
            showSetCalderaStatus()
            batRaw = adc.read()
            publicaMQTT(topic_subBatRaw,str(batRaw).encode('utf-8'))            
            batVolt = batRaw*4.36/1023
            publicaMQTT(topic_subBatVolt,('%.2f' % batVolt).encode('utf-8'))                   
        time.sleep_ms(100)

