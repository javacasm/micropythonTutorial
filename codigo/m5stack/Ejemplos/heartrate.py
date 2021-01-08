from m5stack import *
import i2c_bus
import max30100
import time,sys
from m5ui import *
import unit

setScreenColor(0x222222)

label0 = M5TextBox(10, 10, "Heart Rate", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=0)
label1 = M5TextBox(50, 80, "0", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label2 = M5TextBox(50, 130, " ", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label3 = M5TextBox(10, 60, " ", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

try:
    Heart = unit.get(unit.HEART, unit.PORTA)
except Exception as e:
    label1.setColor(0xff0000)
    label1.setPosition(x=10, y=100)
    label1.setText("Please connect   HEART unit!")

while True:
    try:
        time.sleep(0.1)
        rate = Heart.getHeartRate()
        spo2 = Heart.getSpO2()
        label1.setText("BPM:  " + str(rate))
        label2.setText("Sp02: " + str(spo2) + "%")
        if rate > 100:
            label1.setColor(0xff0000)
        else:
            label1.setColor(0xFFFFFF)
        
        if btnB.wasPressed():
            setScreenColor(0x222222)
            label3.setText("Stop.  Please  reboot.")
            Heart.deinit()
            sys.exit()
    except KeyboardInterrupt as e:
        setScreenColor(0x222222)
        Heart.deinit()
        sys.exit()