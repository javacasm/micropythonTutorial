# Motor Shield
# from https://forum.micropython.org/viewtopic.php?t=3977


from machine import Pin, PWM

""" nodemcu pins from the motor shield """

# D1,GPIO 5 Enable A
# D2,GPIO 4 Enable B
# D3,GPIO 0 Direction A
# D4,GPIO 2 Direction B


pwm_frequency = 750

speed_STOP = 0
speed_min = 150 # Depends on batteries state
speed_med = 600
speed_max = 1023

current_speed = speed_med 

speedA = PWM(Pin(4,Pin.OUT), freq = pwm_frequency)
dirA = Pin(2,Pin.OUT
dirB = Pin(0,Pin.OUT)
speedB = PWM(Pin(5,Pin.OUT), freq = 750)

def stop():
    speedA.duty(speed_STOP)
    speedB.duty(speed_STOP)
    

def Backward():
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.off()
    dirB.off()

def forward():
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.on()
    dirB.on()

def right():
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.off()
    dirB.on()

def left():
    speedA.duty(current_speed)
    speedB.duty(current_speed)
    dirA.on()
    dirB.off()






