import MyDateTime


v = '1.3.6'

moduleName = 'Utils'

logFile = 'log.txt'

def myLog(msg, saveToFile = False):
    sDate = MyDateTime.getLocalTimeHumanFormat()
    totalMsg = sDate + ' ' + msg
    print(totalMsg)
    if saveToFile:
        saveLogMsg(totalMsg)
    

def identifyModule(module, version):
    myLog('Module ' + module + ' ' + version)

def saveLogMsg(errorMsg):
    with open(logFile, 'a') as f:
        f.write(errorMsg + '\n')

def showLog():
    with open(logFile, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                print(line.strip())
    
identifyModule(moduleName, v)