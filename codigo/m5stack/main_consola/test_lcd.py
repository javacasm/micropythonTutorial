from m5stack import *
from m5ui import *
import network
import deviceCfg



# Configuracion wifi
wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)

wifi_config = deviceCfg.get_wifi()
if wifi_config == []:
    print('no wifi config')
#    import wifiWebCfg
#    wifiWebCfg.config_by_web()
else:
    ssid = wifi_config[0]
    pwd = wifi_config[1]
    print('wifi: ' + ssid)
    wlan_sta.connect(ssid, pwd)

# dibujando

setScreenColor(0x222222)

lcd.circle(147,201,40, 0xd7ceca,0xf5be2b)

label0 = M5TextBox(10, 10, "Heart Rate", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=0)