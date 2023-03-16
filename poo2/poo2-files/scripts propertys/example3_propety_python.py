# Archivo: example3_propety_python.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/01/2023
# Descripción: Uso real property's en python


class Perros(object):
    """
    Clase Perros que representa a un perro con un nombre y un peso.
    """
    def __init__(self, nombre, peso):
        """
        Constructor de la clase Perros.
        :param nombre: nombre del perro.
        :param peso: peso del perro.
        """
        self.__nombre = nombre
        self.__peso = peso

    @property
    def nombre(self):
        """
        Propiedad que representa el nombre del perro.
        """
        try:
            print("Estamos recuperando el atributo nombre")
            return self.__nombre
        except Exception as e:
            print(f"hay un error {repr(e)} al recuperar nombre, intenta de nuevo")

    @nombre.setter
    def nombre(self, nuevo):
        """
        Setter que modifica el nombre del perro.
        :param nuevo: nuevo nombre del perro.
        """
        print("Modificando nombre..")
        self.__nombre = nuevo
        print("El nombre se ha modificado por")
        print(self.__nombre)

    @nombre.deleter
    def nombre(self):
        """
        Deleter que elimina el nombre del perro.
        """
        try:
            print("Borrando nombre..", self.__nombre)
            del self.__nombre
        except Exception as e:
            print(f"hay un error {repr(e)} al Eliminar nombre, intenta de nuevo")
        return None

    @property
    def peso(self):
        """
        Propiedad que representa el peso del perro.
        """
        try:
            print("recuperando el atributo peso")
            return self.__peso
        except Exception as e:
            print(f"hay un error {repr(e)} al recuperar el atributo peso, intenta de nuevo")

    @peso.setter
    def peso(self, nuevo_peso):
        """
        Setter que modifica el peso del perro.
        :param nuevo_peso: nuevo peso del perro.
        """
        self.__peso = nuevo_peso
        print("El peso ahora es")
        print(self.__peso)

    @peso.deleter
    def peso(self):
        """
        Deleter que elimina el peso del perro.
        """
        try:
            print("Borrando peso..", self.__peso)
            del self.__peso
        except Exception as e:
            print(f"hay un error {repr(e)} al Eliminar peso, intenta de nuevo")
        return None


Tomas = Perros("Tom", 27)
print(Tomas.nombre)
Tomas.nombre = "Tomasito"
print(Tomas.nombre)
Tomas.peso = 28
del Tomas.nombre
print(Tomas.nombre)
