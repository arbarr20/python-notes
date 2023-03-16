# Archivo: bound-unbound-func-descript2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 08/02/2023
# Descripción:En el siguiente script hay una simulación de como posiblemente trabaje
# `types.MethodType` como descriptor de No datos, esto es solo un ejemplo para mostrar
# como funciona

import types


class Function(object):
    """
    La clase Function simula el comportamiento del tipo de función incorporado de Python.
    Permite acceder a una función tanto como función como como método.
    """

    def __init__(self, func):
        """
        Inicializa un objeto Function con la función dada.

        Args:
        func (callable): La función que se almacenará en el objeto Function.
        """
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        Llama a la función almacenada con los argumentos dados.

        Args:
        *args: Los argumentos posicionales a pasar a la función.
        **kwargs: Los argumentos con palabra clave a pasar a la función.

        Devuelve:
        El resultado de llamar a la función almacenada.
        """
        print("__call__ Fue llamdo")
        return self.func(*args, **kwargs)

    def __get__(self, obj, objtype=None):
        """
        Obtiene la función almacenada como método del objeto dado.

        Args:
        obj (object): El objeto al que se debe vincular la función como método.
        objtype (type): El tipo del objeto.

        Devuelve:
        La función almacenada como método del objeto dado.
        """

        if obj is None:
            print("obj-none ")
            return self
        return types.MethodType(self, obj)


class MyClass(object):

    """
    La clase MyClass representa una clase simple con un solo método.
    """

    def __init__(self, x: int):
        """
        Inicializa un objeto MyClass con el valor dado para x.

        Args:
        x (int): El valor de x.
        """
        self.x = x

    def my_method(self, y: int) -> int:

        """
        Devuelve la suma de x e y.

        Args:
        y (int): El valor de y.

        Devuelve:
        La suma de x e y.
        """
        return self.x + y


# Crear una instancia de MyClass--------------------------------
obj = MyClass(10)
# Acceder al método my_method como método de la instancia
# my_method es un método enlazado
result = obj.my_method(5)
print(f"Método enlazado - obj.my_method: {type(obj.my_method)}")
print(result)  # Salida: 15

# Crear un objeto Function de my_method-----------------------
obj_func = Function(obj.my_method)
print(f"Método enlazado-obj_func.func): {type(obj_func.func)}")
# Acceder al objeto Function como una función
# esto es gracias a la implementación de __call__
result = obj_func(5)
print(f"\nresult-obj_func(5): {result}\n")  # Salida: 15
# LLamado normal con Punto
print(obj_func.func(5))


# Creamos un Método dinámico de instancia por medio de __get__ del descriptor--------------------
# la linea obj_func.__get__(obj_func,obj) =inst_desc.__get__(inst_desc,instancia de clase que
# implementa descriptor)
obj.fun_add = obj_func.__get__(obj_func, obj)
print(f"\nMétodo enlazado-obj.fun_add: {obj.fun_add}\n")
# lo que regresa __get__ es un objeto Function, asignamos
# el método func de Function a nuestro Método dinámico
obj.fun_add = obj.fun_add.func

print(f"\nMétodo enlazado-obj.fun_add: {obj.fun_add}\n")
# Ejecutamos el nuevo Método Enlazado de obj
result = obj.fun_add(5)
print(f"\nresult-obj.fun_add(5): {result}\n")
