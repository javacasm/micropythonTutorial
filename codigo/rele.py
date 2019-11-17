import Machine

# Using a wemos https://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png

rele = machine.Pin(5,machine.Pin.OUT)  # Rele shield en D1 (GPIO5)
rele.on() 
# rele.off()
