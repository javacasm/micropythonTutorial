# Config file

v = '0.3.0'
moduleName = 'config'

from Utils import identifyModule, myLog
identifyModule(moduleName, v)


tRefresco = 10000

mqtt_server = '192.168.1.88'

pin_neoPixel = 2

pin_SDA = 21
pin_SDL = 22

BME280_ADDRESS = 118

# Topics

topic_sub = b'MeteoSalon'
topic_subTime = topic_sub + b'/Time'
topic_subTemp = topic_sub + b'/Temp'
topic_subHum = topic_sub + b'/Hum'
topic_subPress = topic_sub + b'/Press'
topic_subLedRGB = topic_sub + b'/ledRGB'
topic_subData = topic_sub + b'/SensorData'
topic_subCalderaAction = topic_sub + b'/caldera'
topic_subCalderaStatus = topic_sub + b'/calderaStatus'
topic_subInitConsola = topic_sub + b'/initConsola'
topic_subConsolaStatus = topic_sub + b'/consolaStatus'

msg_calderaOn = 'On'
msg_calderaOff = 'Off'