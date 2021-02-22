# ejemplo basado en  http://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html?highlight=onewire
import onewire
import ds18x20
import machine

datos = machine.Pin(13)
ds = ds18x20.DS18X20(onewire.OneWire(datos))

ids=ds.scan()
# ids [bytearray(b'(\xf4\xe9\x00\x00\x00\x80\x15')]

ds.convert_temp()

ds.read_temp(ids[0])
