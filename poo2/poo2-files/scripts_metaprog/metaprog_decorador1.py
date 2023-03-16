# Archivo: Metaprog_decorador1
# Autor: Arbarr20
# Fecha: 29/11/2022
# Referencia:http://www.dabeaz.com
# Descripción: Es un decorador que se puede usar con parámetros o sin
# parámetros

from functools import wraps, partial


def debug(func=None, *, prefix=''):

    if func is None:
        return partial(debug, prefix=prefix)    
    msg = prefix + func.__qualname__    

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{msg}")
        return func(*args, **kwargs)
    return wrapper


"""
Recordemos:
* @debug: func = debug(func)
  * el primer parámetro es func, No es un parámetro clave valor
* debug(func=None, *, prefix='')
  * (parámetro antes del * SOO UNO, solo palabras clave después del *)
cuando el decorador se pone @debug sin los paréntesis:
  * func=<function add at 0x101d3be50> sin clave valor,
    parámetro normal
Lo contrario ocurre cuando se llama @debug(prefix='***'):
  * debido a la forma  y orden como se ejecuta este decorador 
  * func=None que es el parámetro por defecto de debug, esto ocasione que
   ingrese al if de debug
"""


@debug
def add(x, y):
    return x + y


@debug(prefix='***')
def sum(a, b):
    return a + b


print(add(2, 3))
print(sum(3, 3))

"""
add
5
***sum
6
"""
