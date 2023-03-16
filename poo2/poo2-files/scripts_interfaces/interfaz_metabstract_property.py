# Archivo: interfaz_metabstract_property.py
# Autor: Arbarr20 y ayuda online
# Fecha: 09/03/2023
# Descripción: la combinación de métodos abstractos y propertys en una interfaz 

"""
Módulo que define las clases Base, Integer y String para la gestión de valores numéricos y de texto.

Clases:
-------
- Base: clase abstracta base que define el comportamiento de las clases Integer y String.
- Integer: clase que representa un valor numérico entero.
- String: clase que representa un valor de texto.

Uso:
----
Se pueden crear objetos de las clases Integer y String. Se puede acceder y modificar el valor de
cada objeto a través de su atributo 'value'.
Si se intenta asignar un valor incorrecto, se generará una excepción ValueError.

Ejemplo:
--------
i = Integer()
print('Valor inicial de Integer:', i.value)

i.value = 42
print('Valor actualizado de Integer:', i.value)

s = String()
print('Valor inicial de String:', s.value)

s.value = 'Hola mundo'
print('Valor actualizado de String:', s.value)

s.value = 123  # Esto generará un error
"""

import abc


class Base(abc.ABC):
    """
    Clase abstracta que define el comportamiento de una propiedad value.

    Atributos:
    ----------
    Ninguno.

    Métodos:
    --------
    value (propiedad): Devuelve o asigna el valor de la propiedad.

    """
    @property
    def value(self):
        """
        Devuelve el valor de la propiedad value.

        Parámetros:
        ----------
        Ninguno.

        Retorna:
        --------
        El valor actual de la propiedad value.

        """
        return 'Should never reach here'

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        """
        Asigna el valor de la propiedad value.

        Parámetros:
        ----------
        new_value: cualquier tipo
            El valor a asignar a la propiedad value.

        Retorna:
        --------
        Ninguno.

        Raises:
        -------
        abc.ABCError:
            Si se intenta llamar a este método desde una subclase que no lo ha implementado.

        """
        return


class Integer(Base):
    """
    Clase que hereda de Base y define una propiedad value de tipo int.

    Atributos:
    ----------
    _value: int
        El valor actual de la propiedad value.

    Métodos:
    --------
    value (propiedad): Devuelve o asigna el valor de la propiedad.

    """
    _value = 0

    @property
    def value(self):
        """
        Devuelve el valor de la propiedad value.

        Parámetros:
        ----------
        Ninguno.

        Retorna:
        --------
        El valor actual de la propiedad value.

        """
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        """
        Asigna el valor de la propiedad value.

        Parámetros:
        ----------
        new_value: int
            El valor a asignar a la propiedad value.

        Retorna:
        --------
        Ninguno.

        Raises:
        -------
        ValueError:
            Si el valor pasado como parámetro no es de tipo int.

        """
        if not isinstance(new_value, int):
            raise ValueError('Value must be an integer')
        self._value = new_value


class String(Base):
    """
    Clase que hereda de Base y define una propiedad value de tipo str.

    Atributos:
    ----------
    _value: str
        El valor actual de la propiedad value.

    Métodos:
    --------
    value (propiedad): Devuelve o asigna el valor de la propiedad.

    """
    _value = ''

    @property
    def value(self):
        """
        Devuelve el valor de la propiedad value.

        Parámetros:
        ----------
        Ninguno.

        Retorna:
        --------
        El valor actual de la propiedad value.

        """
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        """
        Asigna el valor de la propiedad value.

        Parámetros:
        ----------
        new_value: str
            El valor a asignar a la propiedad value.

        Retorna:
        --------
        Ninguno.

        Raises:
        -------
        ValueError:
            Si el valor pasado como parámetro no es de tipo str.

        """
        if not isinstance(new_value, str):
            raise ValueError('Value must be a string')
        self._value = new_value
