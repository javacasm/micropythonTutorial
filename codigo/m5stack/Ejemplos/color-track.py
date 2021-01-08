from m5stack import *
from uiflow import *
import time,sys
import m5ui
import unit

m5ui.setScreenColor(0x222222)
label0 = m5ui.M5TextBox(45, 10, "Color Track", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label1 = m5ui.M5TextBox(10, 50, "trace coordinates:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label2 = m5ui.M5TextBox(10, 100, "X:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label3 = m5ui.M5TextBox(10, 130, "Y:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label4 = m5ui.M5TextBox(170, 100, "W:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label5 = m5ui.M5TextBox(170, 130, "H:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label6 = m5ui.M5TextBox(10, 160, "Pixel:", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label7 = m5ui.M5TextBox(10, 210, " ", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)

vfunc = unit.get(unit.V_FUNCTION, unit.PORTB)
track = vfunc.init(vfunc.COLOR_TRACK)

def buttonA_wasPressed():
    track.setTrackColorByLAB(0, 100, -22, 1, -48, -9)
    label7.setText("L:0~100 A:-22~1 B:-48~-9")

btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
    track.setTrackColorByLAB(0, 100, 2, 30, 33, 83)
    label7.setText("L:0~100 A:2~30 B:33~83")

btnB.wasPressed(buttonB_wasPressed)

while True:
    try:
        wait_ms(100)
        data = track.getBoxDetail(1)
        label2.setText("X: " + str(data[1]))
        label3.setText("Y: " + str(data[2]))
        label4.setText("W: " + str(data[3]))
        label5.setText("H: " + str(data[4]))
        label6.setText("Pixel: " + str(data[0]))
    except KeyboardInterrupt:
        vfunc.deinit()
        m5ui.setScreenColor(0x222222)
