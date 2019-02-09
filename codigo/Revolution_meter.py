# Revolution metter

from machine import Pin, PWM

steps = 0
direccion = 1

def callback(p):
    step = steps + direccion
    print(steps)

def stop():
    speedA.duty(speed_STOP)
    speedB.duty(speed_STOP)

def backward():
    direccion = -1
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.off()
    dirB.off()

def forward():
    direccion = 1
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.on()
    dirB.on()

stop()
step = 0
while( step <100 ):
    forward()
stop()

pwm_frequency = 750

speed_STOP = 0
speed_min = 150 # Depends on batteries state
speed_med = 600
speed_max = 1023

current_speed = speed_med 

p15 = Pin(15,Pin.IN)

p15.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = callback)

speedB = PWM(Pin(4,Pin.OUT), freq = 750)
dirB = Pin(2,Pin.OUT)
dirA = Pin(0,Pin.OUT)
speedA = PWM(Pin(5,Pin.OUT), freq = 750)
