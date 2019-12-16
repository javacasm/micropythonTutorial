import machine
import ntptime
import utime

# DateTime utility

# v1.3.1

def setRTC():
    ntptime.settime()
    return getLocalTimeHumanFormat()

def getLocalTimeHumanFormat():
    strLocalTime = "{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time()+3600)[0:6])
    return strLocalTime
    
