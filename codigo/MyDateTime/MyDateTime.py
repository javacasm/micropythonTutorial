import machine
import ntptime
import utime

# from Utils import identifyModule

# DateTime utility

v = '1.3.6'
moduleName = 'MyDateTime'

# No usamos Utils porque depende de MyDateTime
'''
def setRTC():
    ntptime.settime()
    return getLocalTimeHumanFormat()
''''
def getLocalTimeHumanFormat():
    strLocalTime = "{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time()+3600)[0:6])
    return strLocalTime

sDate = getLocalTimeHumanFormat()
print(sDate + ' Module ' + moduleName + ' ' + v)
