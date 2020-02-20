import webrepl
import network
iw = network.WLAN(network.STA_IF)
iw.active(True)
iw.connect('OpenWrt','qazxcvbgtrewsdf')
webrepl.start()
iw.ifconfig()
print('TTGO - esp32')