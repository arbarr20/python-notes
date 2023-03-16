# Archivo: descriptor-base.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/12/2022
# Descripción: __set_name__(self, owner=type=cls, name)
#              para descriptor final base,
#             - se pone un __init__ en el descriptor Person para ver como se trabaja con el.


class RequiereString:
    def __set_name__(self, owner, name):
        print(f"__set_name__ was called with owner={owner} and name={name}")
        self.property_name = name
        print(f"__set_name__ self.property: {self.property_name}")

    def __get__(self, obj, owner=None) -> object:
        print(f"__get__ was called with obj={obj} and owner={owner}")
        print(f"get-obj-dic {obj.__dict__}")
        if obj is None:
            return self
        return obj.__dict__.get(self.property_name) or None

    def __set__(self, obj, value) -> None:
        print(
            f"__set__ was called with obj={obj} and value={value} obj.edad: {obj.edad}"
        )

        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must a string")

        if not isinstance(obj.edad, int):
            raise ValueError(f"The {obj.edad} must a int")
        # obj.edad es la forma de acceder al __init__ de person
        if len(value) == 0 or obj.edad == 0:
            raise ValueError(
                f"The {self.property_name} and edad {obj.edad} cannot be empty"
            )
        # instance.__dict__[self.property_name] = value
        # La anterior es una alternativa a la linea siguiente
        obj.__dict__[self.property_name] = value

    def __delete__(self, obj):
        print(f"Eliminando a {obj.__dict__}")
        del obj.__dict__


class Person:
    # nombre.__set_name__(Person, 'first_name')
    nombre = RequiereString()
    apellido = RequiereString()

    def __init__(self, edad):
        self.edad = edad
        print(f"self.value init {self.edad}")


pepito_perez = Person(20)
pepito_perez.nombre = "Pepito"
pepito_perez.apellido = "Perez"

jhon_santos = Person(32)
jhon_santos.nombre = "Jhon"
jhon_santos.nombre = "Santos"

erika_gomez = Person(45)
erika_gomez.nombre = "Erika"
erika_gomez.apellido = "Gomez"


print(
    f"pepito_perez.nombre : {pepito_perez.nombre}, la direccion de memoria es : {hex(id(pepito_perez))}"
)
print(
    f"pepito_perez.apellido : {pepito_perez.apellido}, la direccion de memoria es : {hex(id(pepito_perez))}"
)
print(
    f"jhon_santos.nombre: {jhon_santos.nombre}, la direccion de memoria es : {hex(id(jhon_santos))}"
)
print(
    f"jhon_santos.apellido : {jhon_santos.apellido}, la direccion de memoria es : {hex(id(jhon_santos))}"
)
print(
    f"erika_gomez.nombre : {erika_gomez.nombre}, la direccion de memoria es : {hex(id(erika_gomez))}"
)
print(
    f"erika_gomez.apellido : {erika_gomez.apellido}, la direccion de memoria es : {hex(id(erika_gomez))}"
)

print("\n")

print(f"diccionario pepito_perez-obj {pepito_perez.__dict__}")
print(f"diccionario jhon_santos-obj {jhon_santos.__dict__}")
print(f"diccionario erika_gomez-obj {erika_gomez.__dict__}")

print("\n")
del pepito_perez.nombre
print(
    f"pepito_perez.nombre : {pepito_perez.nombre}, la dirección de memoria es : {hex(id(pepito_perez))}"
)

del pepito_perez
try:
    print(
        f"pepito_perez.nombre : {pepito_perez.nombre}, la dirección de memoria es : {hex(id(pepito_perez))}"
    )
except Exception as e:
    print(f"Error {e} - Eliminado")

print("\n")
print(Person.__dict__["nombre"].__dict__)
print(Person.__dict__["apellido"].__dict__)

print("\n")
# como se llama primero al __init__ nose valida el tipo de dato en esta linea
otra_persona = Person(50)
# Pero en esta linea si se valida ya que se valida en el descriptor
otra_persona.nombre = "otro nombre"
try:
    # se validan el campo apellido, no debe estar vació, genera una Excepción
    otra_persona.apellido = ""
except Exception:
    print("Error No cumple con los parámetros del descriptor")
