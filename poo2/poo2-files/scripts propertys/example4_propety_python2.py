# Archivo: example4_propety_python2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/01/2023
# Descripción: guardar en una cierta caché - property's

import time


class MiClase:
    """
    Clase que representa un valor que puede ser un número o una lista de números.
    Además, tiene un atributo llamado `transformada` que se puede calcular a partir del `valor`.

    Atributos:
        - valor (int, float, list): valor que se quiere almacenar
        - __transformada (float): valor transformado que se puede calcular a partir de `valor`
    """

    def __init__(self, valor=None):
        """
        Inicializa una instancia de la clase `MiClase`.

        Args:
            valor (int, float, list, opcional): valor que se quiere almacenar. Por defecto,
            es `None`
        """
        self.valor = valor
        self.__transformada = None

    @property
    def valor(self):
        """
        Propiedad que devuelve el valor almacenado en la instancia de `MiClase`.
        """
        return self.__valor

    @valor.setter
    def valor(self, mivalor):
        """
        Propiedad setter que permite asignar un valor a la instancia de `MiClase`.

        Args:
            mivalor (int, float, list): valor que se quiere almacenar en la instancia de `MiClase`

        Raises:
            ValueError: Si el valor no es válido (no es un número o una lista de números en el
            rango [0, 10])

        Returns:
            None
        """
        if isinstance(mivalor, (int, float)):
            self.__valor = mivalor if 0 <= mivalor <= 10 else 0
        elif isinstance(mivalor, list):
            self.__valor = list(filter(lambda x: 0 <= x <= 10, mivalor))
        else:
            raise ValueError("El dato introducido no es válido")

    @property
    def transformada(self):
        """
        Propiedad que devuelve el valor transformado. Si no ha sido calculado previamente,
        se calculará.

        Returns:
            float: Valor transformado.
        """
        if not self.__transformada:
            print("Calculando transformada...")
            time.sleep(3)
            self.__transformada = 123.79382
        else:
            print("Transformada en caché. Valor:")
        return self.__transformada

    @property
    def media(self):
        """
        Método para calcular la media de los valores.

        :return: Devuelve la media de los valores en forma de número flotante.
                 Si el valor almacenado es una lista, se realiza la suma de
                 todos sus elementos y se divide entre el número de elementos.
                 Si el valor no es una lista, se devuelve un mensaje indicando
                 que no es posible calcular la media.
        """

        if isinstance(self.valor, list):
            return sum(self.__valor) / len(self.__valor) if self.__valor else 0
        else:
            return "\nNo se puede calcular la media al no ser una lista"


datos = [12.21, 8.68, -2, 7.77]
print("Los datos introducidos son: ", datos)
a = MiClase(datos)
print("Los datos filtrados son: ", a.valor)
print("La media de los datos filtrados es:", a.media)
print(a.transformada)
print("haciendo otra cosa")
print(a.transformada)
