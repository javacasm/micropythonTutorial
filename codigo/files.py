# Files
# https://docs.micropython.org/en/latest/esp8266/tutorial/filesystem.html

import os


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


