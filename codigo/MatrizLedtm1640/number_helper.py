
# Numbers 0 al 9 de 4x6

digits_4x6 = [
0x3c42423c00000000,
0x00447e4000000000,
0x64524a4400000000,
0x424a4a3400000000,
0x1e10107c00000000,
0x4e4a4a3200000000,
0x3c4a4a3200000000,
0x0262120e00000000,
0x344a4a3400000000,
0x0c52523c00000000,
]

def createTM1640()
    import machine
    import tm1640
    import Wemos
    tm = tm1640.TM1640(clk = machine.Pin(Wemos.D5), dio = machine.Pin(Wemos.D7))
    return tm
    
def count(tm ):
    import time
    import tm1640
    for i in range(10):
        tm.write_int(digits_4x6[i])
        time.sleep(1)

def show2FiguresNumber(tm, numero):
    import tm1640
    numero = int(numero)
    units = numero % 10
    tens = numero // 10
    tm.write_int(digits_4x6[tens])
    tm.write_int(digits_4x6[units],4)
    

