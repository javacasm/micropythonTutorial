v = '1.4.6'

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
    print(str(e))
    myLog('SelfReset')
    # machine.reset()
    myLog('Not done')

# WebServerControlRele.runServer()
