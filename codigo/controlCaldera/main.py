v = '1.5.6'

# import machine

moduleName = 'main-Caldera'
from Utils import identifyModule, myLog
identifyModule(moduleName, v)

try:
    import MyDateTime
    # import WebServerControlRele    
    import MQTT_caldera
    myLog('start Time: ' + MyDateTime.getLocalTimeHumanFormat(), saveToFile=True)
    import network, time
    import config
    w = network.WLAN(network.STA_IF)
    w.active(True)
    print('Conectando a Wifi')
    w.connect(config.SSID, config.SSID_PASSWD)
    while not w.isconnected():
        print('.',end='')
        time.sleep(0.5)
    print('Conectado a wifi')
    
    MQTT_caldera.mainBeta()

except Exception as e:
    errorMsg = str(e)
    myLog(errorMsg,saveToFile = True)
    myLog('SelfReset',saveToFile = True)
    machine.reset()

# WebServerControlRele.runServer()
