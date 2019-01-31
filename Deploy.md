# Deploy

[deploy](https://github.com/radeklat/esp8266-deploy-micropython)

From [https://github.com/MikeTeachman/micropython-thingspeak-mqtt-esp8266]

        boot.py
        lib
          |
          umqtt
             simple.py
             robust.py
     

Example with Ampy:

        >ampy -pCOM27 -d1 ls
        boot.py
        >ampy -pCOM27 -d1 mkdir lib
        >ampy -pCOM27 -d1 mkdir lib/umqtt
        >ampy -pCOM27 -d1 put simple.py lib/umqtt/simple.py
        >ampy -pCOM27 -d1 put robust.py lib/umqtt/robust.py
        >ampy -pCOM27 -d1 ls
        boot.py
        lib
        >ampy -pCOM27 -d1 ls lib
        umqtt
        >ampy -pCOM27 -d1 ls lib/umqtt
        simple.py
        robust.py
        
        
**Validating the UMQTT package install**
From the REPL (using Putty, etc) execute the following commands and observe similar output

        >>> from umqtt.robust import MQTTClient

        >>> dir(MQTTClient)
        ['reconnect', 'log', 'publish', '__module__', 'wait_msg', 'delay', '__qualname__', 'DELAY', 'DEBUG']
        
        
If you see this result you have successfully installed the umqtt package. tada relieved
