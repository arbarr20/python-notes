# Archivo: debugmethods_decorador_func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 30/12/2022
# Descripción: Funciones decoradoras en metaclases y decoradores normales
# modificando el comportamiento de una clase.


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


@debugattr
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

# Define una clase llamada `OtherClass`que NO utiliza la metaclase `debugmeta`.
# por Ende el debugmethod no se ejecuta


@debugattr
class OtherClass():
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
