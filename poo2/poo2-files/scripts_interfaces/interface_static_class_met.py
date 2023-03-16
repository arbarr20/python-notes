# Archivo: interfaz_formal_metaclass_abc.py
# Autor: Arbarr20 y ayuda online
# Fecha: 28/02/2023
# Descripción: Interfaz formal con una metaclase abc

"""
Este script define dos clases: Base e Implementation, que utilizan el patrón de diseño
"Factory Method" para crear objetos.

La clase Base es una clase abstracta que define dos métodos abstractos: factory() y
const_behavior(),que deben ser implementados por las subclases. La clase Implementation es una
subclase de Base y sobrescribe ambos métodos abstractos.

El método factory() es un método de fábrica que crea y devuelve un objeto de la clase. El método
const_behavior() es un método estático que devuelve una cadena.

Ejemplo de uso:

    i = Implementation.factory()
    print('Implementation.const_behavior:', i.const_behavior())

"""

import abc


class Base(abc.ABC):
    """
    Clase abstracta que define el método factory y el método const_behavior que deben ser
    implementados por las subclases.
    """

    @classmethod
    @abc.abstractmethod
    def factory(cls, *args):
        """
        Método de fábrica que crea y devuelve un objeto de la clase.

        Args:
            cls (type): La clase que está llamando al método.
            args: Argumentos adicionales para la creación del objeto.

        Returns:
            object: Objeto creado por la clase.

        Raises:
            Ninguno.
        """
        return cls()

    @staticmethod
    @abc.abstractmethod
    def const_behavior():
        """
        Método estático que devuelve una cadena.

        Returns:
            str: Una cadena.

        Raises:
            Ninguno.
        """
        return 'Should never reach here'


class Implementation(Base):
    """
    Subclase de Base que implementa el método factory y el método const_behavior.
    """

    def do_something(self):
        """
        Método que no hace nada.

        Args:
            Ninguno.

        Returns:
            Ninguno.

        Raises:
            Ninguno.
        """
        pass

    @classmethod
    def factory(cls, *args):
        """
        Método de fábrica que crea y devuelve un objeto de la clase.

        Args:
            cls (type): La clase que está llamando al método.
            args: Argumentos adicionales para la creación del objeto.

        Returns:
            object: Objeto creado por la clase.

        Raises:
            Ninguno.
        """
        obj = cls(*args)
        obj.do_something()
        return obj

    @staticmethod
    def const_behavior():
        """
        Método estático que devuelve una cadena.

        Returns:
            str: Una cadena.

        Raises:
            Ninguno.
        """
        return 'Static behavior differs'


try:
    o = Base.factory()
    print('Base.value:', o.const_behavior())
except Exception as err:
    print('ERROR:', str(err))

i = Implementation.factory()
print('Implementation.const_behavior:', i.const_behavior())
