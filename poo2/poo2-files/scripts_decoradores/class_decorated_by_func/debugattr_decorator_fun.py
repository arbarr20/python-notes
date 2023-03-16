# Archivo: debugattr_decorator_fun.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/12/2022
# Descripción: Función decoradora.
"""
Descripción

Este script define un decorador llamado debugattr que se puede usar para
añadir una funcionalidad de registro a la acceso a atributos de una clase.
El decorador toma una clase como argumento y reemplaza el método mágico
__getattribute__ de la clase con una función envoltorio que imprime el
nombre del atributo que se está accediendo y luego llama al método original
__getattribute__ con los mismos argumentos. La función envoltorio se
devuelve como el resultado del decorador.

La clase Point se ha decorado con el decorador debugattr. Cuando se crea una
instancia de Point y se accede a sus atributos x y y, se ejecuta la función
envoltorio y se imprime el nombre del atributo que se está accediendo.

"""


def debugattr(cls):
    # Esta es la función decoradora que se utilizará para modificar
    # el comportamiento del acceso a atributos de la clase
    # El parámetro cls representa la clase que se va a decorar.

    orig_getattribute = cls.__getattribute__
    # Se guarda la implementación original del método __getattribute__
    #  de la clase en una variable.

    def __getattribute__(self, name):
        # Esta es la nueva implementación del método __getattribute__ que se
        # va a utilizar para modificar el comportamiento del acceso a
        # atributos.
        # El parámetro self representa la instancia de la clase y el
        # parámetro name representa el nombre del atributo.
        # Point.__getattribute__(p, x or y)
        print('Get:', name)
        # Se imprime un mensaje con el nombre del atributo.
        # Point.__getattribute__ = __getattribute__
        # setattr(cls, '__getattribute__', __getattribute__)
        return orig_getattribute(self, name)
        # Se llama a la implementación original del método
        # __getattribute__ para recuperar el atributo de forma normal.

    # Se sobrescribe el método __getattribute__ original de la clase con
    #  la nueva implementación que se ha definido en la función decoradora.
    cls.__getattribute__ = __getattribute__

    return cls

# Se aplica el decorador a la clase Point.
# forma como se llama el decorador
# Point = debugattr(Point)
# Point()
# print(Point.__getattribute__(p,"x"))


@debugattr
class Point:
    def __init__(self, x, y):
        # Este es el método constructor de la clase Point.
        # Se llama cuando se crea una instancia de la clase.
        print('init')
        # Se imprime un mensaje.
        self.x = x
        # Se establece el atributo x de la instancia.
        self.y = y
        # Se establece el atributo y de la instancia.

# Alternativa al scrip anterior, para entender mejor
# descomente las lines si quiere ejecutar.


p = Point(2, 3)
print(p.x)
print(p.y)
"""
Este script define una metaclase llamada PointMeta que sobrescribe el método
mágico __getattribute__. El método __getattribute__ se llama cada vez que
se accede a un atributo de una clase o instancia de clase. La implementación
sobrescrita del método __getattribute__ en PointMeta imprime el nombre del
atributo y luego llama al método __getattribute__ original de la clase
padre (type en este caso) con los mismos argumentos.

La clase Point se define con PointMeta como su metaclase. Esto significa
que la clase Point heredará el método __getattribute__ sobrescrito de
PointMeta. Cuando se crea una instancia de Point y se accede a sus
atributos x y y, se ejecuta el método __getattribute__ sobrescrito
y se imprime el nombre del atributo que se está accediendo
"""

"""

class PointMeta(type):
    def __getattribute__(cls, name):
        print('Get:', name)
        return type.__getattribute__(cls, name)

class Point(metaclass=PointMeta):
    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(p.y)
"""
