from m5stack import *
import time,sys
import m5ui
import unit

m5ui.setScreenColor(0x222222)
label0 = m5ui.M5TextBox(16, 10, "Motion Detect", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)
label1 = m5ui.M5TextBox(25, 70, "dynamic mode", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label2 = m5ui.M5TextBox(100, 130, "Text", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label3 = m5ui.M5TextBox(10, 191, "Text", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)

vfunc = unit.get(unit.V_FUNCTION, unit.PORTB)
motion = vfunc.init(vfunc.MOTION)

def buttonA_wasPressed():
    motion.setScanInterval(1, 2)

btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
    motion.setScanInterval(0, 0)

btnB.wasPressed(buttonB_wasPressed)

while True:
    try:
        time.sleep(0.1)
        if motion.getMaxDiff() > 50:
            label2.setText("Moved!")
            label2.setColor(0xff0000)
        else:
            label2.setColor(0xFFFFFF)
            label2.setText("No move")
        label3.setText("Rate of difference: " + str(motion.getRateOfDiff()))
    except KeyboardInterrupt as e:
        vfunc.deinit()
        sys.exit()
