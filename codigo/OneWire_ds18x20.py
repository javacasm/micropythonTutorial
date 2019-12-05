# https://docs.micropython.org/en/latest/esp8266/quickref.html#deep-sleep-mode

# Wemos ds18x20 shield uses D2

# You must also power the sensors and connect a 4.7k Ohm resistor between the data pin and the power pin.    
import time
import machine
import onewire, ds18x20

# the device is on GPIO12
dat = machine.Pin(12)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# loop 10 times and print all temperatures
for i in range(10):
    print('temperatures:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds.read_temp(rom), end=' ')
    print()
