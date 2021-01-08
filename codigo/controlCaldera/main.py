v = '1.5.0'

# import machine

moduleName = 'main-Caldera'
from Utils import identifyModule, myLog
identifyModule(moduleName, v)

try:
    import myDateTime
    # import WebServerControlRele    
    import MQTT_caldera
    print('Time: ' + myDateTime.setRTC())
    MQTT_caldera.mainBeta()

except Exception as e:
    errorMsg = str(e)
    myLog(errorMsg,saveToFile = True)
    myLog('SelfReset',saveToFile = True)
    machine.reset()

# WebServerControlRele.runServer()
