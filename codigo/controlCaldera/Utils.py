import MyDateTime


v = '1.2.3'

moduleName = 'Utils'


def myLog(msg):
    sDate = MyDateTime.getLocalTimeHumanFormat()
    print(sDate + ' ' + msg)
    

def identifyModule(module, version):
    myLog('Module ' + module + ' ' + version)


identifyModule(moduleName, v)