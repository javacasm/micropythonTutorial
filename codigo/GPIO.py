# https://docs.micropython.org/en/latest/esp8266/quickref.html#pins-and-gpio

# Available pins are: 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16,
# Pin(1) and Pin(3) are REPL UART TX and RX
# Pin(16) is a special pin (used for wakeup from deepsleep mode)  

## Uso como lectura
  
pin = machine.Pin(0)
pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
pin.value()

## Uso como salida

pin = machine.Pin(0, machine.Pin.OUT)

pin.value(0)
pin.value(1)

# Or:

pin.off()
pin.on()
