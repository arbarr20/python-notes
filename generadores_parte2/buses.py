# buses.py
#
# Un ejemplo de cómo configurar una Pipeline de manejador de eventos con corrutinas
# y análisis XML.

from coroutine import *
import threading
@coroutine
def buses_to_dicts(target):
    while True:        
        event, value = (yield)
        # Busque el inicio de un elemento <bus> 
        if event == 'start' and value[0] == 'bus':
            busdict = { }
            fragments = []
            # Capture el texto que esta dentro de la etiquetas y pongalas en busdict
            while True:
                event, value = (yield)
                if event == 'start':   fragments = []
                elif event == 'text':  fragments.append(value)
                elif event == 'end':
                    if value != 'bus': 
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break

@coroutine
def filter_on_field(fieldname,value,target):
    
    while True:        
        d = (yield)        
        if d.get(fieldname) == value:           
            target.send(d)

@coroutine
def bus_locations():    
    while True:                
        bus = (yield)               
        print(f"Ruta:{bus['route']}-Direction:{bus['direction']}-lat:{bus['latitude']}-long:{bus['longitude']}-id:{bus['id']}")   
        
    

# Example 
if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler   

    #no_filter = buses_to_dicts(bus_locations())
    #mi_manejador = EventHandler(no_filter)

    #filtro_sin_anidar = buses_to_dicts(filter_on_field("route","22",bus_locations()))
    #mi_manejador = EventHandler(filtro_sin_anidar)

    filtro_Anidado = buses_to_dicts(filter_on_field("route","22",filter_on_field("direction","North Bound",bus_locations())))
    
    mi_manejador = EventHandler(filtro_Anidado)   
    xml.sax.parse("allroutes.xml",mi_manejador)
    
            
