# Descriptor 4
# Guardando valor del atributo en el objeto NO en el descriptor
# Arbarr20

class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        print(f"get-obj-dic {obj.__dict__}")
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        print (f"Eliminando a {obj.__dict__}")
        del obj.__dict__

class Foo():
    number = OneDigitNumericValue("number")

    print (f"diccionario number-self {number.__dict__}")

my_foo_object = Foo()
my_second_foo_object = Foo()
my_third_foo_object = Foo()
my_foo_object.number = 4
my_second_foo_object.number =5
my_third_foo_object.number =8

print(my_foo_object.__dict__)
print(f"my_foo_object.number : {my_foo_object.number}, la dirección de memoria es : {hex(id(my_foo_object))}")
print(f"my_foo_object.number : {my_second_foo_object.number}, la dirección de memoria es : {hex(id(my_second_foo_object))}")
print(f"my_foo_object.number : {my_third_foo_object.number}, la dirección de memoria es : {hex(id(my_third_foo_object))}")

print (f"diccionario my_foo_object-obj {my_foo_object.__dict__}")
print (f"diccionario my_second_foo_object {my_second_foo_object.__dict__}")
print (f"diccionario my_third_foo_object {my_third_foo_object.__dict__}")

del(my_foo_object.number)
print(f"my_foo_object.number : {my_foo_object.number}, la dirección de memoria es : {hex(id(my_foo_object))}")