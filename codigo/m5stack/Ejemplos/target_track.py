from m5stack import *
from uiflow import *
import time,sys
import m5ui
import unit

m5ui.setScreenColor(0x222222)
label0 = m5ui.M5TextBox(35, 10, "Target Track", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label1 = m5ui.M5TextBox(10, 70, "track coordinates:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label2 = m5ui.M5TextBox(10, 120, "X:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label3 = m5ui.M5TextBox(10, 160, "Y:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label4 = m5ui.M5TextBox(170, 120, "W:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label5 = m5ui.M5TextBox(170, 160, "H:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

vfunc = unit.get(unit.V_FUNCTION, unit.PORTB)
track = vfunc.init(vfunc.TARGET_TRACK)

def buttonB_wasPressed():
    track.setTrackAreaCoordinate(135, 95, 50, 50)
btnB.wasPressed(buttonB_wasPressed)


while True:
    try:
        wait_ms(100)
        data = track.getBoxDetail()
        label2.setText("X: " + str(data[0]))
        label3.setText("Y: " + str(data[1]))
        label4.setText("W: " + str(data[2]))
        label5.setText("H: " + str(data[3]))
    except KeyboardInterrupt:
        track.deinit()
        m5ui.setScreenColor(0x222222)
