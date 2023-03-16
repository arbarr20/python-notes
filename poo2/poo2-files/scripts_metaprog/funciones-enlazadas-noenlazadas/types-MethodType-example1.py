# Archivo: types-MethodType-example1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 08/02/2023
# Descripción: Descubriendo a types.MethodType

"""
Este script importa el módulo types y define una función my_func que imprime un mensaje en consola.
También define una clase Persona con un constructor y un método datos que imprime los datos de la
persona en consola. Se crea un objeto de la clase Persona y se asigna el método datos a una
variable method_enlazado. Finalmente, se imprimen mensajes con información sobre el tipo de
method_enlazado y se crea otro método enlazado usando types.MethodType.
"""
import types


def my_func():
    """Esta función imprime un mensaje en consola."""
    print("esta es my_func")


class Persona:
    def __init__(self, nombre: str, fecha_nacimiento: str):
        """Constructor de la clase Persona.

        Args:
            nombre (str): Nombre de la persona.
            fecha_nacimiento (str): Fecha de nacimiento de la persona.
        """
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def datos(self) -> None:
        """Imprime en consola los datos de la persona."""
        print(
            f"los datos de esa persona son son : {self.nombre}:{self.fecha_nacimiento}"
        )


# Creación de un objeto de la clase Persona
per = Persona("arbarr", "01/01/19980")

# Asignación del método datos a una variable
method_enlazado = per.datos

# Imprimir mensajes con información sobre el método enlazado
print(
    f"""Método enlazado (llamado desde un Objeto):
    {method_enlazado}"""
)
print(
    f"""\nImprime typo del método enlazado type(método_enlazado):
    {type(method_enlazado)}"""
)
print(
    f"""\nAhora que es types.MethodType:
    {types.MethodType}"""
)
print(
    f"""\nPodemos decir que type(method_enlazado) == types.MethodType:
        {type(method_enlazado) == types.MethodType}"""
)
print(
    f"""\n Creando otro method_enlazado con types.MethodType:
        Método_enlazado2 = types.MethodType(Persona.datos,per)
        {types.MethodType(Persona.datos,per)}"""
)
