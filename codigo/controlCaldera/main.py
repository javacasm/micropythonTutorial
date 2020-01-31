v = '1.3.8'

import machine

try:
    import myDateTime
    # import WebServerControlRele    
    import MQTT_caldera
    print(myDateTime.setRTC())

    MQTT_caldera.mainBeta()
except Exception as e:
    print(str(e))
    machine.reset()

# WebServerControlRele.runServer()
