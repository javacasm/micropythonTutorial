import machine
import time,utime
import bmp180
import dht
import onewire, ds18x20
import Wemos
import number_helper

# BMP180
def showTempBMP(tm):
    i2c = machine.I2C(sda = machine.Pin(Wemos.D2),scl = machine.Pin(Wemos.D1))
    bmp = bmp180.BMP180(i2c)
    tempBMP = bmp.temperature
    print("{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time()+3600)[0:6]) + ' BMP: '+str(tempBMP))
    tm.write_int(0x0100000000000000)
    number_helper.show2FiguresNumberX3(tm,tempBMP)

# DHT
def showTempDHT(tm):
    dht11 = dht.DHT11(machine.Pin(Wemos.D4))
    dht11.measure()
    tempDHT = dht11.temperature()
    print("{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time()+3600)[0:6]) + ' DHT: '+str(tempDHT))
    tm.write_int(0x1000000000000000)
    number_helper.show2FiguresNumberX3(tm, tempDHT)

# DS18x20
def showTempDS(tm):
    ds = ds18x20.DS18X20(onewire.OneWire(machine.Pin(Wemos.D2)))
    roms = ds.scan()
    if len(roms) > 0 :
        ds.convert_temp()
        tempDS = ds.read_temp(roms[0])
        print("{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time()+3600)[0:6]) + ' DS: '+str(tempDS))
        tm.write_int(0x8000000000000000)
        number_helper.show2FiguresNumberX3(tm, tempDS)


# main
def mainBeta():
    tm = number_helper.createTM1640()
    tm.brightness(0)
    while True:
        showTempDS(tm)
        time.sleep(10)
        showTempDHT(tm)
        time.sleep(10)
        showTempBMP(tm)
        time.sleep(10)
        
