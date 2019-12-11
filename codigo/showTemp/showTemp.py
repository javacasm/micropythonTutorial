import machine
import time, utime
import bmp180
import dht
import onewire, ds18x20
import Wemos
import number_helper
import MyDateTime

# V1.2

# BMP180
def showTempBMP(tm):
    i2c = machine.I2C(sda = machine.Pin(Wemos.D2),scl = machine.Pin(Wemos.D1))
    bmp = bmp180.BMP180(i2c)
    tempBMP = bmp.temperature
    tm.write_int(0x0100000000000000)
    number_helper.show2FiguresNumberX3(tm,tempBMP)
    return tempBMP

# DHT
def showTempDHT(tm):
    dht11 = dht.DHT11(machine.Pin(Wemos.D4))
    dht11.measure()
    tempDHT = dht11.temperature()
    tm.write_int(0x1000000000000000)
    number_helper.show2FiguresNumberX3(tm, tempDHT)
    return tempDHT

# DS18x20
def showTempDS(tm):
    ds = ds18x20.DS18X20(onewire.OneWire(machine.Pin(Wemos.D2)))
    roms = ds.scan()
    if len(roms) > 0 :
        ds.convert_temp()
        tempDS = ds.read_temp(roms[0])
        tm.write_int(0x8000000000000000)
        number_helper.show2FiguresNumberX3(tm, tempDS)
        return tempDS

# main
def mainBeta():
    tm = number_helper.createTM1640()
    tm.brightness(0)
    print(MyDateTime.setRTC())
    print("# DateTime,BMP,DHT,DS")
    while True:
        tempDS = showTempDS(tm)
        tempDHT = showTempDHT(tm)
        tempBMP = showTempBMP(tm)
        print(MyDateTime.getLocalTimeHumanFormat() + ', '+str(tempBMP)+ ', '+str(tempDHT)+ ', '+str(tempDS))
        time.sleep(1000)

