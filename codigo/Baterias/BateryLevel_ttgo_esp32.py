import machine

def batLevel():
    adcBat = machine.ADC(machine.Pin(34))
    adcBat.atten(machine.ADC.ATTN_11DB) # rango de 3.6V
    adcBat.width(machine.ADC.WIDTH_12BIT)
    adcValue = adcBat.read()
    voltBat = adcValue * 2 * 3.6 / 4095 # el 2 por el divisor de tension
    percentBat = voltBat*100/4.2
    print('%1.2fv - %d%%'%(voltBat,percentBat))
    return percentBat