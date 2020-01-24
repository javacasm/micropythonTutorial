import time
import machine 
import pcd8544_test 
import machine 
import sys
pcd8544_test.init()
pcd8544_test.initFB()

v = '1.4.17'

N = 50 
def test(N = 50 ):
    adc = machine.ADC(0) 

    pcd8544_test.showText(0,0,'Midiendo')
    time.sleep(1)
    pcd8544_test.clear() 
    N = 50
    
    uart = machine.UART(0,9600)
    uart.init(9600)
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
        sys.stdout.write('<')
        msg = sys.stdin.readline().rstrip()
        if len(msg)<1:
            msg = sys.stdin.readline().rstrip()
        pcd8544_test.showText(0,10,msg)
        print( msg)
        try:
            v = float(msg)
            cte = v * 1023 / value
            pcd8544_test.showText(0,40,str(cte))
            print(cte)
        except Exception as e:
            print(str(e))
