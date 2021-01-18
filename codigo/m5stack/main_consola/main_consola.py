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


v = '0.9.15'
moduleName = 'main_consola'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)

### NEOPIXEL

# Indicador NeoPixel
neoP =  neopixel.NeoPixel(machine.Pin(config.pin_neoPixel),1)

def showLedRGBColor(color):
    neoP[0]=NeoPixelTHO.colorByName(c)
    neoP.write()

### UI

labelT = None
labelP = None
labelH = None

def initUI():
    global labelT, labelP, labelH
    myLog('Init UI')
    labelT = M5TextBox(0, 0, "T: --- ", lcd.FONT_DejaVu72, 0x88FFFF, rotate=0)
    labelP = M5TextBox(0, 85, "P: --- " , lcd.FONT_DejaVu40, 0x88FF88, rotate=0)
    labelH = M5TextBox(0, 130, "H: --- ", lcd.FONT_DejaVu40, 0xFF55FF, rotate=0)

def showUIData():
    global bme
    global labelT, labelP, labelH
    global temp, press, hum, strData
    
    if bme == None:
        initBME280()
    lcd.clear()
    if labelT == None:
        initUI()
    if bme != None:
        strTemp = str(temp)        
        labelT.setText(strTemp)
        myLog('T: ' + strTemp)
        labelP.setText("P: " + str(press))
        labelH.setText("H: " + str(hum))
    else:
        myLog('No sensor')    


### Sensores BME280

bme = None

temp = press = hum = strData = None

def initBME280():
    global bme
    try:
        #i2c = machine.I2C(sda = machine.Pin(21),scl = machine.Pin(22)) # configuramos el acceso al bus i2c
        i2c = machine.I2C(sda = machine.Pin(config.pin_SDA),scl = machine.Pin(config.pin_SDL)) # configuramos el acceso al bus i2c 
        print(i2c.scan()) # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
        bme = BME280.BME280(i2c = i2c, address = config.BME280_ADDRESS)
        myLog('BME280 found @ ' + str(config.BME280_ADDRESS))
    except  Exception as e:
        myLog('BME280 not found: ' + str(e), saveToFile = True)
        bme = None

def testBME280():
    global bme
    global temp, press, hum, strData
    
    if bme == None:
        initBME280()
    if bme != None:
        temp, press, hum = getDataBME280()
        strData = 'Temp: '+str(temp) + ' Pres: '+ str(press) + ' Hum: '+str(hum)
        myLog(strData)

def getDataBME280():
    return (bme.temperature, bme.pressure, bme.humidity)


### WIFI

def testWifi():
    wl = network.WLAN(network.STA_IF)
    wl.active(True)
    
    if wl.isconnected():
        print('Wifi - Connected to ' + wl.config('essid'))
        lcd.image(0, 200, '/flash/img/wifi-48.jpg', type=lcd.JPG)
    else:
        print('connecting')
        wifi_config = deviceCfg.get_wifi()
        if wifi_config == []:
            myLog('no wifi config')
        #    import wifiWebCfg
        #    wifiWebCfg.config_by_web()
        else:
            ssid = wifi_config[0]
            pwd  = wifi_config[1]
            print('wifi: ' + ssid)
            wl.connect(ssid, pwd)
            lcd.image(0, 200, '/flash/img/wifi-48.jpg', type=lcd.JPG)

### MQTT

def sub_CheckTopics(topic, msg):
    myLog(topic + ' : ' + msg)
    
    if topic == topic_subLedRGB:      ## Check for RGB Topic
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
    temp, press, hum = getDataBME280()
    msgTime = MyDateTime.getLocalTimeHumanFormat()
    MQTT_base.client.publish(config.topic_subTemp, temp)
    MQTT_base.client.publish(config.topic_subPress, press)
    MQTT_base.client.publish(config.topic_subHum, hum)
    msg = msgTime+', '+str(temp)+', '+press+', '+hum
    MQTT_base.client.publish(config.topic_subData, msg)  

def run():
    testWifi()

    MQTT_base.connect_and_subscribe() # connect and get a client reference    

    uiTemp()
    last_Beat = int(round(time.time() * 1000))
    while True:
        MQTT_base.client.check_msg() # Check por new messages and call the callBack function        
        now = int(round(time.time() * 1000))
        if (now - last_Beat) > config.tRefresco: # 60 segundos
            publishMQTTData()
            showUIData()
            last_Beat = now
        if btnC.wasPressed():
            uiTemp()
        if btnB.wasPressed():
            break
        if btnA.wasPressed():
            lcd.clear()
    
