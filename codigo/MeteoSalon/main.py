v = '1.3.6'
import machine
import myDateTime

import MQTT_test

print(myDateTime.setRTC())

try:
    MQTT_test.mainBeta()
except Exception as e:
    print(str(e))
    machine.reset()


