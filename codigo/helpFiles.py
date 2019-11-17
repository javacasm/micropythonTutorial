# Files
# https://docs.micropython.org/en/latest/esp8266/tutorial/filesystem.html

import os
import gc

# from https://forum.micropython.org/viewtopic.php?t=3499
def df():
    s = os.statvfs('//')
    return ('{0} MB'.format((s[0]*s[3])/1048576))

# from https://forum.micropython.org/viewtopic.php?t=3499
def free(full=False):
    gc.collect()
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F+A
    P = '{0:.2f}%'.format(F/T*100)
    if not full: return P
    else : return ('Total:{0} Free:{1} ({2})'.format(T,F,P))


def printFile(fichero):
    f = open(fichero)
    for linea in f.readlines():
        print(linea)
    f.close()


"""

Ejemplos

## Crear un fichero
f = open('data.txt', 'w')
f.write('some data')
# 9
f.close()

print(os.listdir()) ## Mostramos los ficheros


f = open('data.txt')
f.read()
# 'some data'
f.close()


os.mkdir('dir') ## Creamos el directorio 'dir'

os.remove('data.txt') ## Borramos un fichero
"""

