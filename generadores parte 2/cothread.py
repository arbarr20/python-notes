# cothread.py
#
# Un objeto de hilo que ejecuta una corrutina dentro de él. Se envían mensajes
# a través de un objeto Queue

from threading import Thread
from queue import Queue
import threading
from coroutine import *

@coroutine
def threaded(target):
    messages = Queue()    
    def run_target():        
        while True:                    
            item = messages.get()
            if item is GeneratorExit:
                target.close()
                return 
            else:                 
                target.send(item)
    Thread(target=run_target).start()
    try:
        while True:
            item = (yield)            
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)

# Ejemplo de Uso

if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler
    from buses import *    
    mi_manejador = EventHandler(buses_to_dicts(threaded(filter_on_field("route","22",
                        filter_on_field("direction","North Bound",
                        bus_locations())))))    
    xml.sax.parse("allroutes.xml",mi_manejador )
                
