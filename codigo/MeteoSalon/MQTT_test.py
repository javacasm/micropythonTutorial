# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

from umqttsimple import MQTTClient
import ubinascii
import machine
import Wemos        # Facilita el identificar los pines
import MeteoSalon   # Relacionado con los dispositivos conectados
import NeoPixelTHO  # Relacioniado con el ledRGB
import time         # Para las esperas
import helpFiles    # para free y df
import utime
from Utils import myLog

v = '1.3.12'

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'MeteoSalon'
topic_subFree = topic_sub + b'/free'
topic_subMem = topic_sub + b'/mem'
topic_subLed = topic_sub + b'/led'
topic_subTemp = topic_sub + b'/Temp'
topic_subHum = topic_sub + b'/Hum'
topic_subPress = topic_sub + b'/Press'
topic_subLedRGB = topic_sub + b'/ledRGB'
topic_subBatRaw = topic_sub + b'/BatteryRaw'
topic_subBatVolt = topic_sub + b'/BatteryVolt'
topic_pub = b'hello'

mqtt_server = '192.168.1.100'


def sub_CheckTopics(topic, msg):
    global client
    try:
        myLog("MQTT < " + str(topic.decode("utf-8")) + ':' + str(msg.decode("utf-8")))
        if topic == topic_subLed:     # Check for Led Topic
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
            client.publish(topic_subMem, str(freeMem))
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
        client.subscribe(topic_subLed)
        client.subscribe(topic_subLedRGB)
        print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_subLedRGB))
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

def mainBeta(everySeconds=60):
    connect_and_subscribe() # connect and get a client reference
    last_Temp = 0
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
            try:
                batRaw = adc.read()
                publicaMQTT(topic_subBatRaw,str(batRaw).encode('utf-8'))            
                batVolt = batRaw*4.367/1023
                publicaMQTT(topic_subBatVolt,('%.2f' % batVolt).encode('utf-8'))                   
                publicaMQTT(topic_subTemp, MeteoSalon.bme.temperature.encode('utf-8'))
                publicaMQTT(topic_subPress, MeteoSalon.bme.pressure.encode('utf-8'))
                publicaMQTT(topic_subHum, MeteoSalon.bme.humidity.encode('utf-8'))
            except KeyboardInterrupt:
                pass
            except Exception as e:
                myLog('Error check_msg: ' + str(e))
                restart_and_reconnect()                
        time.sleep_ms(200)

