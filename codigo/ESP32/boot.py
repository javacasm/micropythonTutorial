# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
iw = network.WLAN(network.STA_IF)
iw.active(True)
iw.connect('OpenWrt','qazxcvbgtrewsdf')
webrepl.start()
iw.ifconfig()
print('esp32 Lolin32.34')
