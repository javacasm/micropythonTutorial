# Servo

servo = machine.PWM(machine.Pin(12), freq=50)
servo.duty(40)      # Minimo
servo.duty(115)     # Maximo 
servo.duty(77)      # Centro
