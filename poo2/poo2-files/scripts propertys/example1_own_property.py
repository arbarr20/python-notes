# Archivo: example1_own_property.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/01/2023
# Descripción: Implementación de una property desde cero

"""
En esta implementación los métodos
    - getter
    - setter
    - deleter
    No se usan, en el proximo ejemplo donde se usan decoradores, si que se hacen
    uso de estos métodos
Otra forma de representar la siguiente linea:
 - return type(self)(fget, self.fset, self.fdel, self.__doc__)
Es:
        def getter(self, fget):
            self.fget = fget
            return self
Otra forma solo para entender es:
 - return propert(self.fget, self.fset, fdel, self.__doc__)
   solo es para entender, ya que hay que asegurarse que proper se
"""


class Propert():
    """
    Clase que permite implementar una propiedad en una clase.

    :param fget: Función que se ejecutará cuando se acceda a la propiedad
    :param fset: Función que se ejecutará cuando se asigne un valor a la propiedad
    :param fdel: Función que se ejecutará cuando se borre la propiedad
    :param doc: Documentación de la propiedad
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        """
        Establece la función que se ejecutará cuando se acceda a la propiedad.

        :param fget: Función que se ejecutará cuando se acceda a la propiedad
        :return: La propiedad actualizada
        """
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        """
        Establece la función que se ejecutará cuando se asigne un valor a la propiedad.

        :param fset: Función que se ejecutará cuando se asigne un valor a la propiedad
        :return: La propiedad actualizada
        """
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        """
        Establece la función que se ejecutará cuando se borre la propiedad.

        :param fdel: Función que se ejecutará cuando se borre la propiedad
        :return: La propiedad actualizada
        """
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Persona():
    """Clase que representa a una persona.

    Atributos:
        nombre (str): El nombre de la persona.

    """

    def __init__(self, nombre):
        """Constructor de la clase.

        Args:
            nombre (str): El nombre de la persona.

        """
        self.set_nombre(nombre)

    def get_nombre(self):
        """Getter del atributo nombre.

        Returns:
            str: El nombre de la persona.

        """
        try:
            print("Pedimos atributo:")
            return self.__nombre
        except AttributeError:
            print("Error. No existe el atributo indicado")
        except Exception as e:
            print("Error al acceder al atributo", e)

    def set_nombre(self, nuevo_nombre):
        """Setter del atributo nombre.

        Args:
            nuevo_nombre (str): El nuevo nombre para la persona.

        """
        print("Asignamos el valor", nuevo_nombre, "al atributo 'nombre'")
        self.__nombre = nuevo_nombre
        return None

    def del_nombre(self):
        """Deleter del atributo nombre."""
        try:
            print("Borramos atributo", self.__nombre)
            del self.__nombre
        except AttributeError:
            print("Error. No existe el atributo que desea borrar")
        except Exception as e:
            print("Error al intentar borrar el atributo", e)
        return None

    nombre = Propert(get_nombre, set_nombre, del_nombre, "Mi información")


a = Persona("Arbarr")
a.nombre = "Otro Arbarr"
print(a.nombre)
del a.nombre
del a.nombre
print(a.nombre)
a.nombre = "Arbarr de Nuevo"
print(a.nombre)
