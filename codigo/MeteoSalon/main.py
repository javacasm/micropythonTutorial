v = '1.3.9'
import machine

try:

    import myDateTime
    print(myDateTime.setRTC())
except Exception as e:
    print(str(e))

try:
    import MQTT_test
    MQTT_test.mainBeta()
    
except Exception as e:
    print(str(e))
    machine.reset()


