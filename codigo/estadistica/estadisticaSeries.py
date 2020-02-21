# Descripcion y tratamiento de estadisticas
# ideas https://www.pythond.com/19987/como-contar-la-frecuencia-de-los-elementos-en-una-lista.html

import random

def creaValores(N = 50):
    valores = []
    for i in range(0,N):
        valores.append(random.randint(100,120))
    return valores

def analiza(valores):
    valores.sort()
    media = 0
    N = len(valores)
    min = valores[0]
    max = valores[0]
    for valor in valores:
        media += valor
        if min > valor:
            min = valor
        if max < valor:
            max = valor
    media /= N
    dispersion = max - min
    dispersionRel = dispersion*100/media
    print('%d valores, media: %5.f disp: %d (%d-%d) %d%%'%(N,media,dispersion,min,max,dispersionRel))
    frecuencias = {x:valores.count(x) for x in valores}
    contaje = frecuencias.values()
    print(contaje)
    print(frecuencias)
    return N,media,min,max
    
                
                     
val = creaValores(200)
#print(val)

analiza(val)
