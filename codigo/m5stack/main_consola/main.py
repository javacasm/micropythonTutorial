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

v = '1.1.21'
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
    showLedRGBColor(b'Green')
    showLedRGBColor(b'Red')
    showLedRGBColor(b'Black')

### UI

labelT = None
labelP = None
labelH = None
bCalderaOn = None
def testUI():
    myLog('Black background')
    setScreenColor(0x000000)
    myLog('image', level = 2 )
    lcd.image(100, 100, '/flash/img/paper_128.jpg', type=lcd.JPG)
    myLog('Circle', level = 2 )
    lcd.circle(130,201,60, 0xd7ceca,0xf5be2b)
    myLog('Label', level = 2 )
    label0 = M5TextBox(10, 10, "Consola", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=0)
    myLog('speaker', level = 2 )
    speaker.tone(880, 120, 1)

def clearUI():
    lcd.clear()

def initUI():
    myLog('Init UI', level = 1)
    myLog('Initted UI', level = 1)

def myPrint(x, y , texto, fuente,color):
    lcd.font(fuente)
    # w,h=lcd.fontSize()
    # lcd.setColor(color)
    # lcd.clearwin(w*lenLabel,h)
    lcd.text(x,y, texto, color = color)

def marco(x,y,w,h,grosor,color):
    for i in range(0,grosor):
        lcd.rect(x+i,y+i,w-2*i,h-2*i,color=color)

def showUIData():
    global bme
    global labelT, labelP, labelH
    global temp, press, hum, strData
    global bCalderaOn
    myLog('Show UI Data', level = 1)
    if bme == None:
        initBME280()
    if labelT == None:
        initUI()
    if bme != None:
        lcd.clear()
        strTemp = str(temp)        
        myPrint(0, 0, strTemp, lcd.FONT_DejaVu72, 0x88FFFF)
        myLog('T: ' + strTemp)
        myPrint(0, 75, "P: " + str(press) , lcd.FONT_DejaVu40, 0x88FF88)
        myPrint(0, 115, "H: " + str(hum), lcd.FONT_DejaVu40, 0xFF55FF)
        text = ' - '
        color = 0xffffff
        if bCalderaOn == True:
            color = 0xf54242
            text = 'On'
        elif bCalderaOn == False :
            color = 0x20C8F5
            text = 'Off'
        myPrint(5, 168, text, lcd.FONT_DejaVu72, color)
        marco(0, 165, 120, 70, 5, color)

        
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
    global bCalderaOn
    myLog(str(topic) + ' : ' + str(msg))
    
    if topic == config.topic_subLedRGB:      ## Check for RGB Topic
        showLedRGBColor(msg)
    elif topic == config.topic_subCalderaStatus:
        if msg == b'On':
            if bCalderaOn != True:
                showUIData()
                bCalderaOn = True
            myLog('StatusCaldera: On')
                
        else:
            if bCalderaOn != False:
                showUIData()
                bCalderaOn = False
            myLog('StatusCaldera: Off')

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
    MQTT_base.client.publish(config.topic_subConsolaStatus, 'On')
    myLog('Published: ' + msg);
    

### RUN

def test():
    testWifi()
    testBME280()
    #testUI()
    testLed()

def sendCalderaOff():
    MQTT_base.client.publish(config.topic_subCalderaAction, config.msg_calderaOff)
    myLog('Sent Caldera Off', saveToFile = True)
    speaker.tone(880, 120, 1)
    
def sendCalderaOn():
    MQTT_base.client.publish(config.topic_subCalderaAction, config.msg_calderaOn)
    myLog('Sent Caldera On', saveToFile = True)
    speaker.tone(440, 120, 1)


def wait4Wifi(tiempo):
    for i in range(0,tiempo):
        getSensorData()
        myPrint(0, 0, str(temp), lcd.FONT_DejaVu72, 0x88FFFF)
        myPrint(130, 120, str(5 - i) , lcd.FONT_DejaVu40, 0x88FF88)
        marco(122,116,40,40,5,0x88FF88)
        time.sleep(1)
        testLed()
        clearUI()   

def run():
    test()
    
    myLog('Waiting 5 seconds for wifi setup...')
    wait4Wifi(5)
    
    MQTT_base.connect_and_subscribe((config.topic_subLedRGB, config.topic_subCalderaStatus), MySubCheckTopics) # connect and get a client reference    

    last_Beat = 0 # int(round(time.time() * 1000))
    MQTT_base.client.publish(config.topic_subInitConsola,'On')
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

if __name__ == '__main__':
    run()