# Archivo: debutattr_debugmethod_metaclass.py
# Autor: Arbarr20 y ayuda online
# Fecha: 30/12/2022
# Descripción: decoradores de atributos y métodos usando metaclases
#  a todos los métodos (llamables) de una clase

"""
El siguiente script es un ejemplo de cómo implementar decoradores y metaclases
en Python. Algunos de los conceptos que se utilizan son:

* Decoradores: son funciones que toman como argumento otra función y modifican
su comportamiento. En este caso, se utiliza el decorador debug, que imprime el
nombre de la función que está siendo ejecutada.

* Metaclases: son clases que son utilizadas para crear otras clases. En este
caso, se utiliza la metaclase debugmeta, que modifica el comportamiento de las
clases que se crean a partir de ella.

* Wraps: es un decorador que se utiliza para preservar la información de la
función original, como su nombre y docstring, cuando se le aplica un decorador.
En concreto, el script define tres decoradores:

1. debug, que imprime el nombre de la función que está siendo ejecutada.
2. debugmethods, que aplica el decorador debug a todos los métodos de una
clase.
3. debugattr, que imprime un mensaje cada vez que se accede a un atributo de
una clase, ademas verifica si el argumento pasado es una función o un método,
hay dos formad de hacer esto
    1. if not inspect.isroutine(orig_getattribute(self, name)):
            print(f'Obteniendo atributo {name} de la clase {cls.__name__}')
    2. if not (isinstance(orig_getattribute(self, name), FunctionType)
                or isinstance(orig_getattribute(self, name), MethodType)):
            print(f'Obteniendo atributo {name} de la clase {cls.__name__}')


Además, se define una metaclase debugmeta, que modifica el comportamiento de
las clases que se crean a partir de ella de la siguiente manera:

1. Aplica el decorador debugmethods a todos los métodos de la clase.
2. Si la clase tiene un método __init__, le aplica el decorador debugattr para
que imprima un mensaje cada vez que se accede a un atributo de la clase.

El script también define tres clases:

1. Base, que es una clase simple que tiene dos métodos, a y b.
2. Grok, que hereda de Base y tiene un método adicional, c.
3. Mondo, que hereda de Grok y tiene un método __init__ y un método
adicional, d.
4. OtherClass q y tiene un método __init__ y un método adicional, e, no
sigue la cadena de herencia de las otras clases, si no que mas bien define
directamente la metaclase.
La clase Base es creada a partir de la metaclase debugmeta, por lo que sus
métodos estarán decorados con debug. La clase Grok también está creada a
partir de debugmeta, por lo que también tendrá los métodos decorados con debug.
La clase Mondo, sin embargo, tiene un método __init__, por lo que además de
tener sus métodos decorados con debug, también tendrá el comportamiento
modificado por el decorador debugattr cuando se acceda a sus atributos.
"""
# Importa la función `wraps` y la función `partial` del módulo `functools`.
# La función `wraps` se usa para preservar algunos atributos de
#  la función original
# cuando se crea una función de envoltorio.
# La función `partial` se usa para crear una función parcialmente aplicada
# a partir de otra función.

from functools import wraps, partial
# import inspect
from types import FunctionType, MethodType

# Define un decorador de clase llamado `debugattr` que modifica
# el comportamiento del acceso a atributos de la clase.


def debugattr(cls):
    # Guarda la implementación original del método __getattribute__
    # de la clase en una variable.
    orig_getattribute = cls.__getattribute__
    # Define una nueva implementación del método __getattribute__.
    # Esta implementación imprime un mensaje y luego llama a la
    # implementación original para obtener el atributo de forma normal.

    def __getattribute__(self, name):
        # Si el atributo que se está intentando obtener no es ni una función ni
        # un método, imprimimos el nombre del atributo y la clase a la que
        # pertenece.
        if not (isinstance(orig_getattribute(self, name), FunctionType)
                or isinstance(orig_getattribute(self, name), MethodType)):
            print(f'Obteniendo atributo {name} de la clase {cls.__name__}')
        # Devolvemos el atributo original utilizando el método __getattribute__
        # original de la clase.
        return orig_getattribute(self, name)
    # Sobrescribe el método __getattribute__ original de la clase con
    # la nueva implementación.
    cls.__getattribute__ = __getattribute__
    return cls

# Define un decorador de función llamado `debug`.
# Esta función acepta una función y un argumento opcional `prefix`.


def debug(func=None, *, prefix=''):
    # Si no se proporciona una función, devuelve una función parcialmente
    # aplicada que puede usarse como decorador y mantiene el prefijo como
    # argumento para su uso posterior.
    if func is None:
        return partial(debug, prefix=prefix)

    # Define un mensaje que incluye el prefijo y el nombre cualificado
    # de la función.
    msg = prefix + func.__qualname__

    # función original.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    # Devuelve la función de envoltorio como resultado del decorador.
    return wrapper


# Define una función que aplica el decorador `debug` a todos los métodos de
# una clase.
def debugmethods(cls):
    # Itera sobre todos los atributos de la clase.
    # Los métodos de clase son atributos de clase.
    for name, val in vars(cls).items():
        # Si el atributo es una función, aplica el decorador `debug` a él.
        if callable(val):
            setattr(cls, name, debug(val, prefix='Accediendo al Method - '))
    # Devuelve la clase modificada.
    return cls


# Define una metaclase llamada `debugmeta` que tiene un método especial
# llamado `__new__`.
class debugmeta(type):
    # El método __new__ se ejecuta cuando se crea una nueva clase.
    def __new__(cls, clsname, bases, clsdict):

        clsobj = super().__new__(cls, clsname, bases, clsdict)
        # Aplica el decorador de clase `debugmethods` a la clase que se está
        # creando.
        clsobj = debugmethods(clsobj)
        # Si la clase que se está creando tiene un método `__init__`,
        # aplica el decorador de clase `debugattr` a la clase.
        if '__init__' in clsdict.keys():
            clsobj_attr = debugattr(clsobj)
            return clsobj_attr
        # Devuelve la clase modificada.
        return clsobj

# Define una clase base llamada `Base` que utiliza la metaclase `debugmeta`.


class Base(metaclass=debugmeta):
    def a(self):
        # Obtiene el nombre del método y lo imprime junto con el nombre de
        # la clase.
        name_method = Base.__dict__['a'].__name__
        print(
            f'ejecutando method <{name_method}> \
                de la clase <{self.__class__.__name__}>')

    def b(self):
        # Obtiene el nombre del método y lo imprime junto con el nombre de
        # la clase.
        name_method = Base.__dict__['b'].__name__
        print(
            f'ejecutando method <{name_method}> \
                de la clase <{self.__class__.__name__}>')
# Define una clase llamada `Grok` que hereda de `Base`.


class Grok(Base):
    def c(self):
        # Obtiene el nombre del método y lo imprime junto con el
        # nombre de la clase.
        name_method = Grok.__dict__['c'].__name__
        print(
            f'ejecutando method <{name_method}> \
                de la clase <{self.__class__.__name__}>')

# Define una clase llamada `Mondo` que hereda de `Grok`.


class Mondo(Grok):
    # Inicializa los atributos `x` e `y` de la instancia.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def d(self):
        # Obtiene el nombre del método y lo imprime junto con el
        # nombre de la clase.
        name_method = Mondo.__dict__['d'].__name__
        print(
            f'ejecutando method <{name_method}> \
                de la clase <{self.__class__.__name__}>')

# Define una clase llamada `OtherClass` que utiliza la metaclase `debugmeta`.


class OtherClass(metaclass=debugmeta):
    def __init__(self, x, y):
        # Inicializa los atributos `n` y `m` de la instancia.
        self.n = x
        self.m = y

    def e(self):
        # Obtiene el nombre del método y lo imprime junto con el
        # nombre de la clase.
        name_method = OtherClass.__dict__['e'].__name__
        print(
            f'ejecutando method <{name_method}> \
                de la clase <{self.__class__.__name__}>')


# Crea una instancia de la clase `Base` y llama a sus métodos.
base = Base()
base.a()
base.b()
print('\n')
# Crea una instancia de la clase `Mondo` y llama a sus métodos
m = Mondo(3, 4)
m.a()
m.b()
m.c()
m.d()
# Imprime los valores de los atributos de la instancia.
print(m.y)
print(m.x)
print('\n')
# Crea una instancia de la clase `OtherClass` y llama a su método.
o = OtherClass(200, 300)
# Imprime los valores de los atributos de la instancia.
print(f'{o.n} - {o.m}')
o.e()
