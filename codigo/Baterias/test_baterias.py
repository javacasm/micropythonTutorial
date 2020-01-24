import time
import machine 
import pcd8544_test  
pcd8544_test.init()
pcd8544_test.initFB()

v = '1.1'

N = 50 
def test(N = 50 ):
    adc = machine.ADC(0) 

    pcd8544_test.showText(0,0,'Midiendo')
    time.sleep(1)
    pcd8544_test.clear() 
    N = 50
    while True:
        media = 0
        for i in range(0,N):
            value = adc.read()
            media += value*1.0
            time.sleep(0.1)
        value = media/N
        print(value)
        pcd8544_test.clear()
        pcd8544_test.showText(0,0,str(value))  