# AsyncWebServer

## uasyncio
"""
Usaremos [uasyncio](https://github.com/micropython/micropython-lib/tree/master/uasyncio)

[Tutorial](https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md)

[Ejemplo de webserver](https://github.com/micropython/micropython-lib/blob/master/uasyncio/example_http_server.py)  

https://forum.micropython.org/viewtopic.php?t=4828
"""

import uasyncio

@asyncio.coroutine
def serve(reader, writer):
    print(reader, writer)
    print("================")
    print((yield from reader.read()))
    yield from writer.awrite("HTTP/1.0 200 OK\r\n\r\nHello.\r\n")
    print("After response write")
    yield from writer.aclose()
    print("Finished processing request")


#import logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
loop = uasyncio.get_event_loop()
loop.call_soon(uasyncio.start_server(serve, "0.0.0.0", 8081))
loop.run_forever()
loop.close()

## Instalamos con 

## uhttpd

https://forum.micropython.org/viewtopic.php?f=16&t=2711&sid=7a2b5596ce021f2d220f6b06b3517505

## ws https://forum.micropython.org/viewtopic.php?t=4010




