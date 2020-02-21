import machine
import time

v = '1.3'

def batLevel(N = 50,espera = 10):
    adcBat = machine.ADC(machine.Pin(34))
    adcBat.atten(machine.ADC.ATTN_11DB) # rango de 3.6V
    adcBat.width(machine.ADC.WIDTH_12BIT)
    media = 0
    min = -1
    max = -1
    for i in range(0,N):
        value = adcBat.read()
        media += value
        if min == -1:
            min = value
        if max == -1:
            max = value            
        if min > value: 
            min = value
        if max < value: 
            max = value            
        time.sleep_ms(espera)
    adcValue = media/N    
    voltBat = voltFromADC(adcValue)
    percentBat = voltBat*100/4.2 # Maximo voltaje 4.2
    print('%1.2fv - %d%% (%1.2f-%1.2f) %d%%'%(voltBat,percentBat,voltFromADC(min),voltFromADC(max),(max-min)*100/adcValue))
    return percentBat

def voltFromADC(adcValue):
    voltBat = adcValue * 2 * 3.6 / 4095 # el 2 por el divisor de tension
    return voltBat