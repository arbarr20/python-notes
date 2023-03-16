# Archivo: interfaz_informal_metaclase2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 24/02/2023
# Descripción: definición de una interfaz informal con metaclase


"""
Este script define una metaclase PersonMeta y una interfaz de persona llamada Person que se
construye a partir de la metaclase PersonMeta. Al heredar de Person, se crea implícitamente una
subclase virtual de Person que requiere la implementación de los métodos 'name' y 'age'. La clase
concreta Employee hereda de la super clase PersonSuper y aparece en el MRO de Employee. La clase
Friend se construye implícitamente a partir de la clase Person y es una subclase virtual de Person,
ya que ambos métodos requeridos se implementan en Friend, pero Person no está en el MRO de Friend.

"""


class PersonMeta(type):
    """Metaclase Person"""

    def __instancecheck__(cls, instance: object) -> bool:
        """Se llama cuando se invoca isinstance (esto, de esto)"""
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass: type) -> bool:
        return (
            hasattr(subclass, "name")
            and callable(subclass.name)
            and hasattr(subclass, "age")
            and callable(subclass.age)
        )


class PersonSuper():
    """
    - PersonSuper no es una clase base virtual
    - PersonSuper es una clase base de Employee
    - PersonSuper es subclase de Person

   """

    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


class Person(metaclass=PersonMeta):
    """Interfaz de persona construida a partir de la metaclase PersonMeta.
    Se convierte en una clase base virtual cuando por medio de ella
    se crea implícitamente una subclase, por ejemplo Friend, al incorporar los 2 métodos
    name y age"""

    pass


print(f"\nes PersonSuper subclase de Person:{issubclass(PersonSuper,Person)}")
print(f'PersonSuper-mro {PersonSuper.__mro__}aqui no está Person, Person es virtual')


class Employee(PersonSuper):
    """Hereda de PersonSuper. PersonSuper aparecerá en Employee .__ mro__"""

    pass


print(f"\nEs Employee subclase de PersonSuper:{issubclass(Employee,PersonSuper)}")
print(f'Employee-mro {Employee.__mro__} Aquí esta PersonSuper, asi que PersonSuper no es virtual')
print(f"\nEs Employee subclase de Person:{issubclass(Employee,Person)}")
print(f'Employee-mro {Employee.__mro__} aqui no está Person, Person es virtual')


class Friend:
    """Construido implícitamente a partir de la clase persona.
    Friend es una subclase virtual de Person, ya que existen ambos métodos requeridos.
    Persona que no esta en el .__ mro__ de friend"""

    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


print(f"\nes Friend subclase de Person:{issubclass(Friend,Person)}")
print(f'Friend-mro {Friend.__mro__} aqui no está Person, Person es virtual')
