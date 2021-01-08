v = '1.5.2'

# import machine

moduleName = 'main-Caldera'
from Utils import identifyModule, myLog
identifyModule(moduleName, v)

try:
    import myDateTime
    # import WebServerControlRele    
    import MQTT_caldera
    myLog('start Time: ' + myDateTime.setRTC(), saveToFile=True)
    MQTT_caldera.mainBeta()

except Exception as e:
    errorMsg = str(e)
    myLog(errorMsg,saveToFile = True)
    myLog('SelfReset',saveToFile = True)
    machine.reset()

# WebServerControlRele.runServer()
