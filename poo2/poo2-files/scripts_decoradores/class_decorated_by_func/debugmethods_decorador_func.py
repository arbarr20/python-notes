# Archivo: debugmethods_decorador_func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 28/12/2022
# Descripción: decorador, el cual aplica depuración
#  a todos los métodos (llamables) de una clase
"""
algunas ayudas para entender debugmethods:
    # vars: es el dict de cls=Spam
    # items: retorna en una lista de tuplas los vars
    # serattr (objeto, atributo, valor)
    # objeto: Al que se le pondrá el atributo
    # atributo: Que se le añadirá el atributo
    # valor: contenido del atributo
    # setattr (Spam,grok-bar-foo, debug(0x4444-0x35e33-0x34dt = wrapper))
    # class.grok = wrapper
    # el debug encapsula el simple método grok por un Wrapper
    # debub : <function Spam.grok at 0x10b1065f0>
    # wrapper = nueva funcionalidad del descriptor
    # y         * el grok original
    # wrapper:<function Spam.grok at 0x10b062cb0> 
"""

from debug_decorator_func import debug

# Define una función que aplica el decorador `debug`
#  a todos los métodos de una clase.


def debugmethods(cls):
    # Itera sobre todos los atributos de la clase.
    # los métodos de clase son atributos de clase
    for name, val in vars(cls).items():
        # Si el atributo es una función, aplica el decorador `debug` a él.
        # y le proporciona un valor a prefix
        if callable(val):
            setattr(cls, name, debug(val, prefix='método - '))
    # Devuelve la clase modificada.
    return cls


if __name__ == '__main__':
    # Decora la Clase Spam el decorador debugmethods,
    # lo que implica que se aplicara el métodos debug
    # a todos lo llamables de la clase
    @debugmethods
    class Spam:
        def grok(self):
            pass

        def bar(self):
            pass

        def foo(self):
            pass
    # Se crea una instancia de Spam, y se llaman sus métodos
    s = Spam()
    s.grok()
    s.bar()