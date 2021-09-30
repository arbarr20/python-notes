# cosax.py
#
# Un ejemplo que muestra cómo enviar eventos SAX a un target de corrutina

import xml.sax

class EventHandler(xml.sax.ContentHandler):
    def __init__(self,target): # se declara el target- corrutina printer()
        self.target = target
    def startElement(self,name,attrs):
        self.target.send(('start',(name,attrs._attrs)))# tupla (tipo_evento,valor de evento)
    def characters(self,text):
        self.target.send(('text',text)) # tupla(tipo_evento,valor de evento)
    def endElement(self,name):
        self.target.send(('end',name))# tupla (tipo_evento,valor de evento)

# Ejemplo de uso
if __name__ == '__main__':
    from coroutine import *

    @coroutine
    def printer():
        while True:
            event = (yield) # event es una tupla
            print (event) # o event[1] oevent[0]
    mi_manejador = EventHandler(printer())
    xml.sax.parse("allroutes.xml",mi_manejador)
    
