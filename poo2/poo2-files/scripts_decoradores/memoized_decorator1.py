# Archivo: memoized_decorator1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/02/2023
# Descripción: se implementa una cache para simular el uso del decorador @lru.cache, es este caso
# se aplica a una función iterativa.

"""
Este script implementa una función para calcular la sucesión de Fibonacci utilizando memoization.
La sucesión de Fibonacci es una serie de números en la que cada número es la suma de los dos
números anteriores, comenzando con 0 y 1. La función fibonacci(n) devuelve el valor de la
sucesión de Fibonacci para un número entero n utilizando memoization para almacenar en caché los
resultados de llamadas previas a la función. La memoization se implementa mediante el uso de un
decorador llamado memoized. El decorador almacena en caché los resultados de las llamadas a la
 utilizando un diccionario.
"""


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
            return value
        except TypeError:
            return self.func(*args)

    def __repr__(self):
        return self.func.__doc__


# fibonacci = memoized(fibonaci)
@memoized
def fibonacci(n: int) -> Decimal:
    """
    Retorna la sucesión de Fibonacci para un número entero n.

    Args:
        n (int): El número entero para el cual se desea obtener la sucesión de Fibonacci.

    Returns:
        Decimal: El valor de la sucesión de Fibonacci para el número n.

    Raises:
        TypeError: Si se pasa un argumento que no es un entero.
    """
    if n in (0, 1):
        return Decimal(n)

    # utilizamos un enfoque iterativo en lugar de recursivo
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[n]


res = Decimal(fibonacci(1000)).to_eng_string()
print(res)
r = Decimal(fibonacci(1000)).to_eng_string()
print(r)
