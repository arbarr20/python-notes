# Archivo: property-cache-simulation1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 16/02/2023
# Descripción: La simulación de no repetir un calculo costoso. solo se calcula la primera vez,
# y las veces posteriores solo se llama el resultado, parecido a una caché

"""
Se define una clase llamada DeepThought con un atributo llamado meaning_of_life, el cual es
decorado con la clase LazyProperty. Esta clase actúa como un descriptor, permitiendo que el valor
del atributo se calcule perezosamente (lazy evaluation), es decir, se calcula sólo cuando se
solicita por primera vez y luego se almacena en el diccionario del objeto para su uso futuro.

Cuando se crea una instancia de DeepThought, su diccionario está vacío. Cuando se llama por primera
vez al atributo meaning_of_life, la función __get__ de LazyProperty se activa, la cual ejecuta la
función asociada y almacena el resultado en el diccionario de la instancia. Luego, retorna el
resultado.

En las llamadas posteriores al atributo meaning_of_life, en lugar de llamar a la función de nuevo,
simplemente devuelve el valor ya calculado. Esto permite una mejora en el rendimiento de la
aplicación, ya que el valor se calcula sólo cuando es necesario.

"""

import time


class LazyProperty:
    def __init__(self, function):
        """
        Constructor de la clase LazyProperty.

        Parameters:
        function (callable): Función a decorar.

        Returns:
        None.
        """
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        """
        Método que se ejecuta al acceder al atributo decorado.

        Parameters:
        obj (object): Instancia de la clase.
        type (type): Tipo de la instancia.

        Returns:
        object: El valor calculado para el atributo decorado.
        """
        if obj is None:
            return self
        # guarda en el dic del obj meaning_of_life': 42
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]


class DeepThought:
    # meaning_of_life = LazyProperty(meaning_of_life)
    @LazyProperty
    def meaning_of_life(self) -> int:
        """
        Atributo decorado con la clase LazyProperty.
        Retorna el valor 42 después de esperar 3 segundos.

        Parameters:
        self (object): Instancia de la clase.

        Returns:
        int: El valor 42.
        """
        time.sleep(3)
        return 42


my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.__dict__)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.__dict__)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
