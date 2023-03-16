# Archivo: memoized_decorator2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/02/2023
# Descripción: se implementa una cache para simular el uso del decorador @lru.cache, es este caso
# se aplica a una función recursiva.

from decimal import Decimal


class memoized(object):
    """
    Implementa un decorador de memoización.

    Memoization (o memoización) es una técnica de optimización utilizada para acelerar el cálculo
    al almacenar en caché los resultados de las llamadas a una función costosa. Con memoization, si
    la función se llama de nuevo con los mismos argumentos, no es necesario volver a calcular los
    resultados, ya que se pueden recuperar de la caché.

    Attributes:
        func: La función que se memoiza.
        cache: El diccionario que se utiliza para almacenar los resultados en caché.

    Methods:
        __call__(self, *args): Verifica si el resultado de la función ya está en caché, si es así,
        devuelve el resultado almacenado en caché. De lo contrario, calcula el resultado y lo
        almacena en caché antes de devolverlo.

        __repr__(self): Devuelve la documentación de la función original.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            print(self.cache)
            return self.cache[args]
        # se ejecuta cuando se intenta acceder a una clave que no existe en el
        # diccionario self.cache
        except KeyError:
            self.cache[args] = value = self.func(*args)
            print(self.cache)
            return value
        except TypeError:
            return self.func(*args)

    def __repr__(self):
        return self.func.__doc__


# fibonacci = memoized(fibonaci)
@memoized
def fibonacci(n):  # llama al init de memoized
    """
    Función recursiva que retorna la sucesión de fibonacci

    Atributes:
        n: numero entero al cual se le calculará la sucesión
           de Fibonacci

    """
    if n in (0, 1):
        return n
    menos_uno = fibonacci(n - 1)
    menos_dos = fibonacci(n - 2)
    return menos_uno + menos_dos


print(fibonacci(1000))  # ejecuta el call de la clase y es una instancia de ella
