# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

v = '1.4'
moduleName = 'boot_caldera'

from Utils import identifyModule
identifyModule(moduleName, v)

import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc
import webrepl
webrepl.start()
gc.collect()

