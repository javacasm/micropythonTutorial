# 

import network
## Conecta a Wifi externa
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.connect('essid', 'password') # connect to an AP
wlan.isconnected()      # check if the station is connected to an AP
wlan.config('mac')      # get the interface's MAC adddress
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses


## Genera una red Wifi propia 

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP') # set the ESSID of the access point

# Ejemplo de uso


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    ssid = 'miSSID'
    if not wlan.isconnected():
        print('connecting to network '+ ssid)
        wlan.connect(ssid, 'password')
        while not wlan.isconnected():
            print('.')
    print('network config:', wlan.ifconfig())
