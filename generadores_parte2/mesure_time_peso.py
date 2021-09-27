import time
import sys

"""Esta es la descripcion del modulo mesure_time_peso.py

Este modulo es simple mente para medir el tiempo de ejecucion de alguna funcion (mide_tiempo(func))
y uan pequeña implementacion para saber que espacio en memorio ocupa una variable con peso(var)
"""
def mide_tiempo(funcion):
    """ esta funcion es un decorador que mide el timepo de ejecucion de una funcion
    Declare
    ----------    
        mide_tiempo
        mifunc().......

    parameters
    ----------   
    Name: rtipo
        description

    return: 
    ----------
    c : func   
        muestra en consola el tiempo de ejecucion de la funcion decorada (mifunc)

    Raises
    ----------
    No implementa
    
    """
    def funcion_medida(*args, **kwargs):
        promedio = []
        for ejecucion in range(5):
            inicio = time.time()
            c = funcion(*args, **kwargs)
            final = time.time() - inicio
            promedio.append(final)
        print(f"Tiempo de ejecucion de {funcion.__name__} es :{sum(promedio)/(len(range(10)))}")
        return c
    return funcion_medida


def peso (var):
    """ esta funcion es un decorador que mide el timepo de ejecucion de una funcion
    Declare
    ----------    
        mide_tiempo
        mifunc().......

    parameters
    ----------   
    Name: rtipo
        description

    return: 
    ----------
    c : func   
        muestra en consola el tiempo de ejecucion de la funcion decorada (mifunc)

    Raises
    ----------
    No implementa 
    >>> var = [0,1,2,3,4,5,6,7,8,9,10]
    >>> peso(var)
    '144 bytes'
    """
    return f"{sys.getsizeof(var)} bytes"

# futura implementation
#tiempo = timeit.timeit('lista = [i for i in range(1000000) if i%2==0]', number=5)
# Calculamos el tiempo medio
#print(tiempo/5) # 0.18671

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)