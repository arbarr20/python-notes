# Archivo: bound-unbound-func-descript1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 07/02/2023
# Descripción:En el siguiente script hay una simulación de como posiblemente trabaje
# `types.MethodType` como descriptor de No datos, esto es solo un ejemplo para mostrar
# como funciona

"""
Este script define tres clases: Descriptor, AdditionalClass y MyClass. La clase Descriptor define
un descriptor para una propiedad de una clase. La clase AdditionalClass define un método estático.
La clase MyClass utiliza el descriptor Descriptor para crear una propiedad que utiliza el método
estático de AdditionalClass. Al ejecutar my_object.my_property(), se invoca el método enlazado
a la instancia de MyClass, que imprime un
"""
import types


class Descriptor:
    """
    Descriptor es una clase que define un descriptor para una propiedad de una clase.

    Args:
        value (callable): Función o método que será utilizado como descriptor.

    Atributos:
        value (callable): Función o método que será utilizado como descriptor.
    """

    def __init__(self, value: callable):
        self.value = value

    def __get__(self, obj, objtype=None):
        """
        Método que se invoca cuando se accede a la propiedad que utiliza el descriptor.

        Args:
            obj (object): Instancia de la clase que contiene la propiedad que utiliza el descriptor.
            objtype (type): Clase que contiene la propiedad que utiliza el descriptor.

        Returns:
            Función o método enlazado a la instancia de la clase `obj`.
        """
        print(f"Método No enlazado:{type(self.value)}")
        if obj is None:
            return self
        return types.MethodType(self.value, obj)


class AdditionalClass:
    """
    AdditionalClass es una clase que define un método estático.

    Métodos:
        some_method: Método estático que imprime un mensaje.
    """

    @staticmethod
    def some_method(obj) -> None:
        """
        Método estático que imprime un mensaje y el objeto que se utiliza como argumento.

        Args:
            obj (object): Objeto que se utiliza como argumento.
        """
        print(f"obj: {obj}")
        print("Hola desde AdditionalClass.some_method!")


class MyClass:
    """
    MyClass es una clase que utiliza el descriptor `Descriptor` para crear una propiedad.

    """

    my_property = Descriptor(value=AdditionalClass.some_method)


my_object = MyClass()
my_object.my_property()
