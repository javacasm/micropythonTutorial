# Sockets 
  # https://docs.micropython.org/en/latest/esp8266/tutorial/network_tcp.html#star-wars-asciimation
  

import socket

addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]

s = socket.socket()
s.connect(addr)


while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')
