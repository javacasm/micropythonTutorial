# https://github.com/javacasm/SmartESP32Car/blob/master/images/Pinout-Arduino-WemosD1R32.png

# Led builtin 2

LED_BUILTIN = 2

l = machine.Pin(LED_BUILTIN, machine.Pin.OUT)
l.on()
l.off()

# PWM

pwm = machine.PWM(machine.Pin(2), freq = 50)  # estandard
pwm.duty(20) # 20%
pwm = machine.PWM(machine.Pin(2), freq = 1) # Frecuencia 1Hz
pwm = machine.PWM(machine.Pin(2), freq = 10) # frecuencia 10Hz

# Pinout

D2 = 26
D3 = 25
D4 = 17
D5 = 16
D6 = 27
D7 = 14
D8 = 12
D9 = 13
D10 = 5
D11 = 23
D12 = 19
D13 = 18
A0 = 2
A1 = 41
A3 = 34
A4 = 36
A5 = 39

# Extra 15, 33, 32 
# SD2, SD3, CMD, CLK, SD0, SD
# SDL,SDA