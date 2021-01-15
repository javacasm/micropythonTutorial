## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import network
from m5stack import *
from m5ui import *
import deviceCfg
import time

import BME280  # Importamos la clase BME280
import config

v = '0.9.6'
moduleName = 'main_consola'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)

BME280_ADDRESS = 118

bme = None
def initBME280():
    global bme
    try:
        i2c = machine.I2C(sda = machine.Pin(21),scl = machine.Pin(22)) # configuramos el acceso al bus i2c 
        print(i2c.scan()) # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
        bme = BME280.BME280(i2c = i2c, address = BME280_ADDRESS)
        myLog('BME280 found @ ' + str(BME280_ADDRESS))
    except  Exception as e:
        myLog('BME280 not found: ' + str(e), saveToFile = True)
        bme = None

def testBME280():
    global bme
    if bme == None:
        initBME280()
    if bme != None:
        myLog('Temp: '+str(bme.temperature) + ' Pres: '+ str(bme.pressure) + ' Hum: '+str(bme.humidity))


def testBME280Wireless():
    global bme
    if bme == None:
        initBME280()
    if bme != None:
        myLog(bme.temperature) 

labelT = None
labelP = None
labelH = None

def initUI():
    global labelT, labelP, labelH
    myLog('Init UI')
    labelT = M5TextBox(0, 0, "T: --- ", lcd.FONT_DejaVu72, 0x88FFFF, rotate=0)
    labelP = M5TextBox(0, 85, "P: --- " , lcd.FONT_DejaVu40, 0x88FF88, rotate=0)
    labelH = M5TextBox(0, 130, "H: --- ", lcd.FONT_DejaVu40, 0xFF55FF, rotate=0)

def getDataBME280():
    return (bme.temperature, bme.pressure, bme.humidity)

def uiTemp():
    global bme
    global labelT, labelP, labelH
    
    if bme == None:
        initBME280()
    lcd.clear()
    global labelT, labelP, labelH
    if labelT == None:
        initUI()
    if bme != None:
        temp, press, hum = getDataBME280()
        strTemp = str(temp)        
        labelT.setText(strTemp)
        myLog('T: ' + strTemp)
        labelP.setText("P: " + str(press))
        labelH.setText("H: " + str(hum))
    else:
        myLog('No sensor')    
    
def testWifi():
    wl = network.WLAN(network.STA_IF)
    wl.active(True)
    
    if wl.isconnected():
        print('Wifi - Connected')
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


def run():
    testWifi()

    uiTemp()
    last_Beat = int(round(time.time() * 1000))
    while True:
        now = int(round(time.time() * 1000))
        if (now - last_Beat) > config.tRefresco: # 60 segundos
            last_Beat = now
            uiTemp()
        if btnC.wasPressed():
            uiTemp()
        if btnB.wasPressed():
            break
        if btnA.wasPressed():
            lcd.clear()
    
