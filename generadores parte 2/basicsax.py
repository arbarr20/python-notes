# basicsax.py
#
# Un ejemplo muy simple que ilustra la interfaz de análisis de XML SAX
# Debe tener el ficheto allroutes.xml

import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self,name,attrs):
        print ("startElement", name)
    def endElement(self,name):
        print ("endElement", name)
    def characters(self,text):
        print ("characters", repr(text)[:40])

xml.sax.parse("allroutes.xml",MyHandler())
