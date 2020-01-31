v = '1.3.8'
import machine

try:

    import myDateTime

    import MQTT_test

    print(myDateTime.setRTC())

    MQTT_test.mainBeta()
    
except Exception as e:
    print(str(e))
    machine.reset()


