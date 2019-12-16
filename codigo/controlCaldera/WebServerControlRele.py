# Webserver control rele
# Reference
# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
# https://forum.micropython.org/viewtopic.php?t=1940

# v1.3.2

try:
    import usocket as socket
except:
    import socket

import gc

import machine, network

import myDateTime
import helpFiles
import Wemos
import caldera_test
import Wemos


def web_page():
    releLocal = machine.Pin(Wemos.D1,machine.Pin.OUT)  # Rele shield en D1 (GPIO5)
    if releLocal.value() == 1:
      gpio_state="ON"
    else:
      gpio_state="OFF"
  
    html = """<html><head> <title>Caldera Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
    <p>Calefaccion: <strong>""" + gpio_state + """</strong></p><p><a href="/?rele=on"><button class="button">ON</button></a></p>
    <p>"""+ myDateTime.getLocalTimeHumanFormat() +"""</p>
    <p><a href="/?rele=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html

def runServer():
    caldera_test.checkCaldera()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        print('Esperando conexiones')
        conn, addr = s.accept()
        try:
            print(myDateTime.getLocalTimeHumanFormat() +' Conexion desde %s' % str(addr))
            conn.settimeout(5)
            request = conn.recv(1024)
            request = str(request)
            # print('Contenido = %s' % request)
            rele_on = request.find('/?rele=on')
            rele_off = request.find('/?rele=off')
            if rele_on == 6:
                print('CALDERA ON')
                caldera_test.enciendeCaldera()
            if rele_off == 6:
                print('CALDERA OFF')
                caldera_test.apagaCaldera()
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            print('Close socket')
        except :
            print('Timeout!!')
        print(helpFiles.free())
