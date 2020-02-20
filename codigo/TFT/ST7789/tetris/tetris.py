# Tetris

v = '0.5.4'
import time
import st7789py as st7789
import fhello

fhello.init()

back_color = st7789.color565(10,10,10)
def tile(x,y,l,r,g,b,ancho = 3):
    fhello.display.fill_rect(x, y ,l, l, st7789.color565(r,g,b))
    for i in range(1,ancho):
        fhello.display.hline(x + i, y + i, l - 2 * i, st7789.color565(r+50,g+50,b+50))
        fhello.display.vline(x + i, y + i, l - 2 * i, st7789.color565(r+100,g+100,b+100))
        fhello.display.vline(x + l -i, y + i, l - 2 * i, st7789.color565(r//3,g//3,b//3))
        fhello.display.hline(x + i, y + l - i , l - 2 * i, st7789.color565(r//2,g//2,b//2))

def test_fill(l = 20 ):
    for x in range(0,fhello.display.width//l):
        for y in range(0,fhello.display.height//l):
            tile(x*l,y*l,l,x*l,y*l,(x+y)*l//2)

def fall(x=fhello.display.width//2,y=0,l=20,r=0,g=0,b=150):
    frame()
    while y+l<fhello.display.height:
        fhello.display.fill_rect(x,y,l,l,back_color)
        y+=1
        tile(x,y,l,r,g,b)
        time.sleep(0.1)
        


def frame():
    fhello.display.fill(back_color)
    fhello.display.vline(0,0,fhello.display.height-1,st7789.WHITE)
    fhello.display.vline(fhello.display.width-1,0,fhello.display.height-1,st7789.WHITE)
    fhello.display.hline(0,fhello.display.height-1,fhello.display.width-1,st7789.WHITE)
