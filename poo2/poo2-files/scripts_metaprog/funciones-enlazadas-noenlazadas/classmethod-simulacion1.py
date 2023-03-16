# Archivo: bound-unbound-func-descript2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 08/02/2023
# Descripción:En el siguiente script hay una simulación de como posiblemente trabaje
# `types.MethodType` como descriptor de No datos, esto es solo un ejemplo para mostrar
# como funciona

import types

class ClassMethodDescriptor:
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):
        print('gett')
        return types.MethodType(self.method, objtype)

class MyClass:
    def __init__(self):
        self.value = 10

    def my_class_method(cls, arg1: int, arg2: int) -> None:
        # se ejecuta cuando se llama a self.func(objtype, *args, **kwargs), esto sucede
        # cunando bond(1, 2) es ejecutado
        print(f"Class method called on {cls} with arguments {arg1} and {arg2}")

    my_class_method = ClassMethodDescriptor(my_class_method)

return_get = MyClass.my_class_method
"""
Explicacion de la salida del siguiente print:

<bound method MyClass.my_class_method of <class '__main__.MyClass'>>:
  lo anterior significa:
   - es una descripción del objeto que representa a un método de clase de la clase MyClass. Este 
   objeto ha sido "vinculado" a la clase MyClass, lo que significa que la función que representa se 
   comporta como un método de clase de MyClass.

   - La cadena <bound method MyClass.my_class_method indica que se trata de un objeto de método de 
   clase que está vinculado al método de clase my_class_method de la clase MyClass. El prefijo
   <class '__main__.MyClass'> indica que el objeto de método de clase está "vinculado" a la clase 
   MyClass en el módulo __main__.

   - En resumen, esta cadena representa un objeto de método de clase que ha sido creado a partir
   del método de clase my_class_method de la clase MyClass. Este objeto puede ser llamado 
   directamente como un método de clase de MyClass, y se comporta como tal debido a que ha sido "vinculado" a la clase MyClass.
"""
print(f"return_get:{return_get}")
# la siguiente linea ejecuta types.MethodType(self.method, objtype) que es equivalente a
# MyClass.my_class_method(MyClass, 1,2)
return_get(1, 2)

