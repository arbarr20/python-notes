# coprocess.py
#
# Un ejemplo de ejecución de una corrutina en un subproceso conectado por una tubería

import  pickle
from coroutine import *

@coroutine
def sendto(f):
    
    try:                        
        while True:
            item = (yield)
            pickle.dump(item,f)
            f.flush()
    except (IOError):                                     
        f.close()

def recvfrom(f,target):
    try:        
        while True:                        
            item = pickle.load(f)            
            target.send(item)
    except EOFError:
        
        target.close()


# Ejemplo de USo
if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler
    from buses import *

    import subprocess
    p = subprocess.Popen(['python3','busproc.py'],stdin=subprocess.PIPE)    
    print(f"este es el pipeline del hijo:{p.stdin}")
    xml.sax.parse("allroutes.xml",EventHandler(buses_to_dicts(sendto(p.stdin))))
