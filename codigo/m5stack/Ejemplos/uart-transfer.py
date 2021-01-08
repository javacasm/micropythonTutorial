from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x292929)




label0 = M5TextBox(15, 106, "Slave Baud", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(12, 130, "115200", lcd.FONT_DejaVu40,0x00ff38, rotate=0)
label2 = M5TextBox(15, 20, "TX", lcd.FONT_Default,0xFFFFFF, rotate=0)
label3 = M5TextBox(139, 20, "RX", lcd.FONT_Default,0xFFFFFF, rotate=0)
label4 = M5TextBox(12, 40, "G17", lcd.FONT_DejaVu40,0x00ff38, rotate=0)
label5 = M5TextBox(136, 40, "G16", lcd.FONT_DejaVu40,0x00ff38, rotate=0)
label6 = M5TextBox(28, 221, "SET-BAUD", lcd.FONT_Default,0x00ff38, rotate=0)
label7 = M5TextBox(136, 221, "SET-TX", lcd.FONT_Default,0x00ff38, rotate=0)
label8 = M5TextBox(227, 221, "SET-RX", lcd.FONT_Default,0x00ff38, rotate=0)
label9 = M5TextBox(173, 106, "/", lcd.FONT_DejaVu72,0xFFFFFF, rotate=0)
label10 = M5TextBox(199, 125, "PC default baud", lcd.FONT_Default,0xFFFFFF, rotate=0)
label11 = M5TextBox(224, 149, "115200", lcd.FONT_Default,0xFFFFFF, rotate=0)

from numbers import Number

baud_list = None
baud = None
baud_index = None
tx_index = None
rx_index = None
pin_list = None
tx = None
rx = None

def uart2_init():
  global baud_list, baud, baud_index, tx_index, rx_index, pin_list, tx, rx
  baud = baud_list[int(baud_index - 1)]
  tx = pin_list[int(tx_index - 1)]
  rx = pin_list[int(rx_index - 1)]
  uart2 = machine.UART(2, tx=tx, rx=rx)
  uart2.init(baud, bits=8, parity=None, stop=1)
  label4.setText(str((str('G') + str(str(tx)))))
  label5.setText(str((str('G') + str(str(rx)))))
  label1.setText(str(baud))


def buttonA_wasPressed():
  global baud_list, baud, baud_index, tx_index, rx_index, pin_list, tx, rx
  if baud_index < len(baud_list):
    baud_index = (baud_index if isinstance(baud_index, Number) else 0) + 1
  else:
    baud_index = 1
  uart2_init()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global baud_list, baud, baud_index, tx_index, rx_index, pin_list, tx, rx
  if tx_index < len(pin_list):
    tx_index = (tx_index if isinstance(tx_index, Number) else 0) + 1
  else:
    tx_index = 1
  if rx_index == tx_index:
    tx_index = (tx_index if isinstance(tx_index, Number) else 0) + 1
    if tx_index > len(pin_list):
      tx_index = 1
  uart2_init()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global baud_list, baud, baud_index, tx_index, rx_index, pin_list, tx, rx
  if rx_index < len(pin_list):
    rx_index = (rx_index if isinstance(rx_index, Number) else 0) + 1
  else:
    rx_index = 1
  if rx_index == tx_index:
    rx_index = (rx_index if isinstance(rx_index, Number) else 0) + 1
    if rx_index > len(pin_list):
      rx_index = 1
  uart2_init()
  pass
btnC.wasPressed(buttonC_wasPressed)


baud_list = [9600, 115200, 230400, 256000, 512000, 921600]
pin_list = [16, 17, 21, 22, 2, 5, 12, 13, 15, 0]
baud_index = 2
tx_index = 2
rx_index = 1
uart1 = machine.UART(1, tx=1, rx=3)
uart1.init(115200, bits=8, parity=None, stop=1)
uart2 = machine.UART(2, tx=17, rx=16)
uart2.init(115200, bits=8, parity=None, stop=1)
uart2_init()
while True:
  if uart1.any():
    uart2.write(uart1.read())
  if uart2.any():
    uart1.write(uart2.read())
  wait_ms(2)
