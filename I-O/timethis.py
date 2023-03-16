"""
timethis.py

Author Original : David Beazley. 
Abarr20: solo es para estudio y traduccion
"""
import atexit
import time
import math
from   contextlib import contextmanager
from   collections import defaultdict

_stats = defaultdict(list)
def _printstats():
    if not _stats:
        return
    
    maxwidth = max(len(str(key)) for key in _stats)
    
    for key,times in sorted(_stats.items(),key=lambda x: str(x[0])):        
        mean = sum(times)/float(len(times))        
        stddev = math.sqrt(sum((x-mean)**2 for x in times)/len(times))
        # la siguite es una obcion para un error que aparece cuado se llama una funcion decorada como @timethis
        """ if str(key).startswith("<"):#what:<function count_to_a_million at 0x10d7b84c0>
            key = key.__name__ """  
        #el {str(key):<{maxwidth}}: str es necesrio para solucionar un problema de formateo  
        print(f"{str(key):<{maxwidth}} : {mean:0.5f}s : N={len(times):d} : stddev={stddev:0.5f}")


atexit.register(_printstats)

# Esta función de utilidad se utiliza para realizar evaluaciones comparativas de tiempo
def timethis(what):      
    @contextmanager
    def benchmark(): 
        start = time.time()
        yield
        end = time.time()
        
        _stats[what].append(end-start)
    if hasattr(what,"__call__"): 
        def timed(*args,**kwargs):            
            with benchmark():
                return what(*args,**kwargs)           
        return timed
    else:        
        return benchmark() 

# Ejemplo
if __name__ == '__main__':
    #Formas de llamar la utilidad    
    from timethis import timethis
    #decorando una funcion
    @timethis
    def count_500000():
        for i in range(50000):
            pass
    count_500000()

    #administrador de contexto con uan fucnion
    with  timethis("mi funcion hasta 2M"):
        def mi_fun():
            for i in range(2000000):
                pass
        mi_fun()
    
    with timethis("cuenta hasta 10M"):
        n = 0
        while n < 10000000:
            n += 1

    # Repetir varias veces 
        for i in range(10):
            with timethis("cuenta hasta 1M"):
                n = 0
                while n < 200000:
                    n += 1  
