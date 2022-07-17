"""
timethis.py

Author Original : David Beazley, yo solo la utilizo para aprender y traducil malamente uan parte 

timethis es una biblioteca de utilidades para hacer comparativas de tiempo simples. A
se proporciona una sola función timethis (). La función opera como
ya sea un administrador de contexto o un decorador. Aquí hay unos ejemplos

Si desea cronometrar un bloque de código, haga esto:

with timethis("Counting to a million"):
    n = 0
    while n < 1000000:
        n += 1

La cadena entre comillas es una descripción que describe el bloque de código.
en cuestión. Se imprimirá en la salida.

Si desea cronometrar una función, puede utilizar un decorador:

@timethis
def count_to_a_million():
    n = 0
    while n < 1000000:
        n += 1

count_to_a_million()

Toda la salida de temporización se recopila y no se imprime hasta que se ejecuta un programa.
salidas. Si cualquier bloque de código o función marcada con timethis () es
ejecutado más de una vez, las mediciones de tiempo se recopilan
y se utiliza para calcular una desviación estándar y media.
"""

import atexit
import time
import math
from   contextlib import contextmanager
from   collections import defaultdict

# Diccionario con medidas de tiempo
_stats = defaultdict(list)

# Salir del procesamiento para imprimir resultados de rendimiento
def _printstats():
    if not _stats:
        return
    # max retorna el maximo numero de una caleccion
    # se itera sobre las llaves del dic _stats, cada lllave se convierte a string
    # se determina cuantos catacteres tienen con len y con max solo 
    # se asigna la clve que tenga mas caracteres
    maxwidth = max(len(str(key)) for key in _stats)
    #_stats.items(): lista de tuplas con clve y valor [('clave','valor),('clave2','valor2')]
    #key=lambda x: str(x[0])): key recibe cada tupla  key(('clave','valor))y la pasa a lambda
    #lambda solo retorna la possicion 0 de cada tupla 'clave'
    #sorted'organice por numero de caracteres mayor a menor la lista de tuplas asi':
    # (de cada tupla de los items del dict,escoja solo la posicion 0 y conviertalo a string):
    # esto retorna los _stats.items() pero ordenados segun el nuemro de caracteres de cada clave
    #times: valor de cada clave (son numeros = tiempo)
    for key,times in sorted(_stats.items(),key=lambda x: str(x[0])):
        # Calcular la desviación estándar y promedio
        # mean promedio= sumade de times/ cuantos times hay
        mean = sum(times)/float(len(times))
        #stddev= desviacionestandar poblacional
        stddev = math.sqrt(sum((x-mean)**2 for x in times)/len(times))
        # la siguite es una obcion para un error que aparece cuado se llama una funcion decorada como @timethis
        """ if str(key).startswith("<"):#what:<function count_to_a_million at 0x10d7b84c0>
            key = key.__name__ """
            
        #print("{0:<{maxwidth}s} : {1:0.5f}s : N={2:5d} : stddev={3:0.5f}".format(key,mean,len(times),stddev,maxwidth=maxwidth))
        print(f"{str(key):<{maxwidth}} : {mean:0.5f}s : N={len(times):d} : stddev={stddev:0.5f}")

# esto es lo ultima que se ejecuta del programa
atexit.register(_printstats)

# Esta función de utilidad se utiliza para realizar evaluaciones comparativas de tiempo
#para entender que hace esto debes estar falimiarizado con los decoradores
def timethis(what):      
    @contextmanager
    def benchmark(): #inyecta la nueva funcionalid
        start = time.time()
        yield
        end = time.time()
        
        _stats[what].append(end-start)
    if hasattr(what,"__call__"): # si what es una funcion la funcion que retorna el dcorador es timed
        def timed(*args,**kwargs):            
            with benchmark():
                return what(*args,**kwargs) # ejecute la funcion what              
        return timed
    else:
        # si la siguiente linea no tuviera el ()  junto con el  @contextmanager no serviria el llamado
        # desde with timethis("cuenta hasta diez millones")
        return benchmark() 

# Ejemplo
if __name__ == '__main__':
    # Una medida simple
    with timethis("cuenta hasta diez millones"):
        n = 0
        while n < 5:
            n += 1

    """  # Repita la medicion
        for i in range(10):
            with timethis("cuenta hasta un millón"):
                n = 0
                while n < 1000000:
                    n += 1
    """
        #Una llamada de 
        #count_to_a_million = timethis (count_to_a_million)
        #count_to_a_million()
    """  @timethis
        def count_to_a_million():
            n = 0
            while n < 10:
                n += 1

        count_to_a_million()
        count_to_a_million()
        count_to_a_million()
    """
