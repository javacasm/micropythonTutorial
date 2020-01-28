v = '1.3.7'

import machine
import myDateTime
# import WebServerControlRele

import MQTT_caldera

print(myDateTime.setRTC())

try:
    MQTT_caldera.mainBeta()
except Exception as e:
    print(str(e))
    machine.reset()

# WebServerControlRele.runServer()
