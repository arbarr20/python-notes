# Archivo: debug_decorator_func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 27/12/2022
# Descripción: decorador simple de depuración llamado debug
# con argumentos opcionales


# Importamos la función wraps del módulo functools

from functools import wraps, partial

# Define un decorador llamado `debug` que acepta una función y un argumento
#  opcional `prefix`.
# Si no se proporciona una función, devuelve una función parcialmente aplicada 
# que puede usarse como decorador.


def debug(func=None, *, prefix='prefix '):
    '''
    Un decorador que muestra el nombre
    del método o función que se esta ejecutando
    '''

    if func is None:
        # Devuelve una función parcialmente aplicada que puede usarse como 
        # decorador.
        # El prefijo se mantiene como argumento para que se pueda especificar 
        # cuando se aplique el decorador.
        return partial(debug, prefix=prefix)

    # Define un mensaje que incluye el prefijo y el nombre cualificado
    #  de la función.
    msg = prefix + func.__qualname__

    # Define una función de envoltorio que imprime el mensaje y luego llama a 
    # la función original.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Se llamó a la {msg}')
        return func(*args, **kwargs)

    # Devuelve la función de envoltorio como resultado del decorador.
    return wrapper


if __name__ == '__main__':
    # Decora la función mul con el decorador debug, proporcionando
    #  un valor para prefix
    @debug(prefix='función ')
    def mul(x, y):
        return x * y
    # Llama a la función mul y muestra el resultado
    print(mul(2, 3))