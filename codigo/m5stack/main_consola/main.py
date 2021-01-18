## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import network
from m5stack import *
from m5ui import *
import deviceCfg
import time
import neopixel

import BME280  # Importamos la clase BME280
import MQTT_base
import NeoPixelTHO
import config
import MyDateTime

   
v = '1.0.4'
moduleName = 'main_consola'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)

### NEOPIXEL

# Indicador NeoPixel
neoP =  neopixel.NeoPixel(machine.Pin(config.pin_neoPixel),1)

def showLedRGBColor(c):
    neoP[0]=NeoPixelTHO.colorByName(c)
    myLog('Color:' + str(c))
    neoP.write()

def testLed():
    showLedRGBColor(b'Blue')
    showLedRGBColor(b'Red')
    showLedRGBColor(b'Black')

### UI

labelT = None
labelP = None
labelH = None

def testUI():
    myLog('Black background')
    setScreenColor(0x000000)
    myLog('Circle', level = 2 )
    lcd.circle(147,201,40, 0xd7ceca,0xf5be2b)
    myLog('image', level = 2 )
    lcd.image(100, 100, '/flash/img/paper_128.jpg', type=lcd.JPG)
    myLog('Label', level = 2 )
    label0 = M5TextBox(10, 10, "Heart Rate", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=0)
    myLog('speaker', level = 2 )
    speaker.tone(880, 120, 1)

def clearUI():
    lcd.clear()

def initUI():
    global labelT, labelP, labelH
    myLog('Init UI', level = 1)
    labelT = M5TextBox(0, 0, "T: --- ", lcd.FONT_DejaVu72, 0x88FFFF, rotate=0)
    labelP = M5TextBox(0, 85, "P: --- " , lcd.FONT_DejaVu40, 0x88FF88, rotate=0)
    labelH = M5TextBox(0, 130, "H: --- ", lcd.FONT_DejaVu40, 0xFF55FF, rotate=0)
    myLog('Initted UI', level = 1)

def showUIData():
    global bme
    global labelT, labelP, labelH
    global temp, press, hum, strData
    myLog('Show UI Data', level = 1)
    if bme == None:
        initBME280()
    if labelT == None:
        initUI()
    if bme != None:
        lcd.clear()
        strTemp = str(temp)        
        labelT.setText(strTemp)
        myLog('T: ' + strTemp)
        labelP.setText("P: " + str(press))
        labelH.setText("H: " + str(hum))
        # lcd.circle(48, 200, 30, 0xd7ceca,0xf54220)
        lcd.circle(163, 200, 30, 0xd7ceca,0x20C8F5)
        lcd.circle(258, 200, 30, 0xd7ceca,0xf54220)         
        myLog('Showed UI Data', level = 1)
    else:
        myLog('No sensor', saveToFile = True)    


### Sensores BME280 & Data

bme = None

temp = press = hum = strData = None

def initBME280():
    global bme
    try:
        #i2c = machine.I2C(sda = machine.Pin(21),scl = machine.Pin(22)) # configuramos el acceso al bus i2c
        i2c = machine.I2C(sda = machine.Pin(config.pin_SDA),scl = machine.Pin(config.pin_SDL)) # configuramos el acceso al bus i2c 
        # myLog(i2c.scan()) # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
        bme = BME280.BME280(i2c = i2c, address = config.BME280_ADDRESS)
        myLog('BME280 found @ ' + str(config.BME280_ADDRESS), saveToFile = True)
    except  Exception as e:
        myLog('BME280 not found: ' + str(e), saveToFile = True)
        bme = None

def testBME280():
    global bme
  
    if bme == None:
        initBME280()
    if bme != None:
        getSensorData()
        myLog(strData)

def getDataBME280():
    if bme == None:
        initBME280()
    return (bme.temperature, bme.pressure, bme.humidity)

def getSensorData():
    global temp, press, hum, strData
    temp, press, hum = getDataBME280()
    strData = 'Temp: '+str(temp) + ' Pres: '+ str(press) + ' Hum: '+str(hum)

### WIFI

def testWifi():
    wl = network.WLAN(network.STA_IF)
    wl.active(True)
    
    if wl.isconnected():
        myLog('Wifi - Connected to ' + wl.config('essid'))
        lcd.image(0, 200, '/flash/img/wifi-48.jpg', type=lcd.JPG)
    else:
        myLog('Connecting ')
        wifi_config = deviceCfg.get_wifi()
        if wifi_config == []:
            myLog('no wifi config', saveToFile = True)
        #    import wifiWebCfg
        #    wifiWebCfg.config_by_web()
        else:
            ssid = wifi_config[0]
            pwd  = wifi_config[1]
            myLog('Connected to wifi: ' + ssid, saveToFile = True)
            wl.connect(ssid, pwd)
            lcd.image(0, 200, '/flash/img/wifi-48.jpg', type=lcd.JPG)

### MQTT

def MySubCheckTopics(topic, msg):
    myLog(str(topic) + ' : ' + str(msg))
    
    if topic == config.topic_subLedRGB:      ## Check for RGB Topic
        showLedRGBColor(msg)
       
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

    

def publishMQTTData():
    global temp, press, hum, strData
    
    msgTime = MyDateTime.getLocalTimeHumanFormat()
    MQTT_base.client.publish(config.topic_subTemp, temp)
    MQTT_base.client.publish(config.topic_subPress, press)
    MQTT_base.client.publish(config.topic_subHum, hum)
    msg = msgTime+', ' + strData
    MQTT_base.client.publish(config.topic_subData, msg)
    myLog('Published: ' + msg);

### RUN

def test():
    testWifi()
    testBME280()
    testUI()
    clearUI()
    testLed()

def sendCalderaOff():
    MQTT_base.client.publish(config.topic_subData, config.msg_calderaOff)
    myLog('Sent Caldera Off', saveToFile = True)
    speaker.tone(880, 120, 1)
    
def sendCalderaOn():
    MQTT_base.client.publish(config.topic_subData, config.msg_calderaOn)
    myLog('Sent Caldera On', saveToFile = True)
    speaker.tone(440, 120, 1)


def run():
    test()
    myLog('Waiting 10 seconds...')
    time.sleep(10)
    
    MQTT_base.connect_and_subscribe(config.topic_subLedRGB, MySubCheckTopics) # connect and get a client reference    

    last_Beat = 0 # int(round(time.time() * 1000))
    
    while True:
        try:
            MQTT_base.client.check_msg() # Check por new messages and call the callBack function        
            now = int(round(time.time() * 1000))
            if (now - last_Beat) > config.tRefresco: # 60 segundos
                getSensorData()
                publishMQTTData()
                showUIData()
                last_Beat = now
            if btnA.wasPressed():
                last_Beat = 0 # fuerza un refresco
            if btnC.wasPressed():
                sendCalderaOn()
            if btnB.wasPressed():
                sendCalderaOff()
        except Exception as e:
            myLog('Main exception: ' + str(e), saveToFile = True)



run()