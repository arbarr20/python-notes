# Archivo: example2_own_property_decorator.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/01/2023
# Descripción: Implementación de una property desde cero con decoradores


"""
En esta implementación los métodos
    - getter
    - setter
    - deleter
    SI se usan, La linea que reemplaza los decoradores es
      - nombre = propert(get_nombre, set_nombre, del_nombre, "Mi información")
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


class Propert(object):
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
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

    # nombre = propert(get_nombre, set_nombre, del_nombre, "Mi información")


class Persona(object):  # Declaramos la clase principal Perros
    def __init__(self, nombre):  # Definimos los parámetros
        self.__nombre = nombre  # Declaramos los atributos

    @Propert
    def nombre(self):  # Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla"  # Doc del método
        try:
            print("Estamos recuperando el atibuto nombre")
            return (
                self.__nombre
            )  # Aquí simplemente estamos retornando el atributo privado
        except Exception as e:
            print(f"hay un error {repr(e)} al recuperar nombre, intenta de nuevo")

    # Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
    # Ahora vamos a utilizar setter y deleter para modificarlos

    @nombre.setter  # Propiedad SETTER
    def nombre(self, nuevo):
        print("Modificando nombre..")
        self.__nombre = nuevo
        print("El nombre se ha modificado por")
        # Aquí vuelvo a pedir que retorne el atributo para confirmar
        print(self.__nombre)

    @nombre.deleter  # Propiedad DELETER
    def nombre(self):
        try:
            print("Borrando nombre..", self.__nombre)
            del self.__nombre
        except Exception as e:
            print(f"hay un error {repr(e)} al Eliminar nombre, intenta de nuevo")
        return None


a = Persona("Arbarr")
a.nombre = "Otro Arbarr"
print(a.nombre)
del a.nombre
del a.nombre
print(a.nombre)
a.nombre = "Arbarr de Nuevo"
print(a.nombre)
