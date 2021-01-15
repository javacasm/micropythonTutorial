# Motor Shield
# from https://forum.micropython.org/viewtopic.php?t=3977
# Problemas de rendimiento https://www.instructables.com/id/Motorized-WiFi-IKEA-Roller-Blind/
# https://www.instructables.com/id/Motorize-IoT-With-ESP8266/

from machine import Pin, PWM

""" nodemcu pins from the motor shield """

# D1,GPIO 5 Enable A
# D2,GPIO 4 Enable B
# D3,GPIO 0 Direction A
# D4,GPIO 2 Direction B

v = '0.8'

pwm_frequency = 750

speed_STOP = 0
speed_min = 400 # Depends on batteries state
speed_med = 600
speed_max = 1023

current_speed = speed_med 

speedB = PWM(Pin(4,Pin.OUT), freq = pwm_frequency)
dirB = Pin(2,Pin.OUT)
dirA = Pin(0,Pin.OUT)
speedA = PWM(Pin(5,Pin.OUT), freq = 750)

def stop():
    speedA.duty(speed_STOP)
    speedB.duty(speed_STOP)


def backward(speed = current_speed):
    speedA.duty(speed)
    speedB.duty(speed)
    dirA.off()
    dirB.off()

def forward(speed = current_speed):
    speedA.duty(speed)
    speedB.duty(speed)
    dirA.on()
    dirB.on()

def right(speed = current_speed):
    speedA.duty(speed)
    speedB.duty(speed)
    dirA.off()
    dirB.on()

def left(speed = current_speed):
    speedA.duty(speed)
    speedB.duty(speed)
    dirA.on()
    dirB.off()






