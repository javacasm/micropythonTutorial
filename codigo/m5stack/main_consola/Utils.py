import MyDateTime


v = '1.4.0'

moduleName = 'Utils'

logFile = 'log.txt'

logLevel = 0

def myLog(msg, saveToFile = False, level = 1):
    global logLevel
    if level > logLevel:
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
