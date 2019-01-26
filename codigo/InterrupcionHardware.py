# Hardware Interrupt

# A hard interrupt will trigger as soon as the event occurs and will interrupt any running code, including Python code. As such your callback functions are limited in what they can do (they cannot allocate memory, for example) and should be as short and simple as possible.

def callback(p):
     print('pin change', p)


from machine import Pin
p0 = Pin(0, Pin.IN)
p2 = Pin(2, Pin.IN)

p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)


