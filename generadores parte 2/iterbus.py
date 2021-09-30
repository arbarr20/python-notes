# iterbus.py
#
# Un ejemplo de análisis XML incremental con la biblioteca ElementTree

from xml.etree.cElementTree import iterparse

for event,elem in iterparse("Concurrencia_coorutinas/allroutes.xml",('start','end')):
    if event == 'start' and elem.tag == 'buses':
        buses = elem
    elif event == 'end' and elem.tag == 'bus':
        busdict = dict((child.tag,child.text) 
                        for child in elem)
        if (busdict['route'] == '22' and 
            busdict['direction'] == 'North Bound'):
            print ("%(id)s,%(route)s,\"%(direction)s\","\
                "%(latitude)s,%(longitude)s" % busdict)
        buses.remove(elem) 

