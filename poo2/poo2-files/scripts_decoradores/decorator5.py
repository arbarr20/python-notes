# Decoradores 4
#Plantilla General de como usar decoradores simples
# Arbarr20

from functools import wraps

def uppercase(f):
        "Dada una función f que devuelve un string lo pasa todo a mayúsculas"
        @wraps(f)
        def wrap():
            return f().upper()
        return wrap

def add_quotes(f):
        "Dada una función f que devuelve un string le añade los tags By - Arbarr"
        @wraps(f)
        def wrap():
            return f"{f()} - By Arbarr"
        return wrap    

@add_quotes # este decorador se ejecuta primero
@uppercase # este se ejecuta despues
def say_hello():
    return "hello world"

print (say_hello())
#Imprime: HELLO WORLD - By Arbarr

