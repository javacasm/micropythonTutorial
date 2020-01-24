v = '1.4.10'

import myDateTime

fecha = myDateTime.setRTC()

import test_baterias
import pcd8544_test 

pcd8544_test.showText(0,0,fecha)
print(fecha)

test_baterias.test()    