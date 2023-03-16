# Archivo: clase_decoradora0.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/01/2023
# Descripción: Clases que decoran Funciones,  se usa __call__
# y un método estático

class MyDecorator:
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Nueva funcionalidad del decorador: {self.name}")
        print("Before calling the decorated function ADD")
        result = self.func(*args, **kwargs)
        print("After calling the decorated function")
        return result

    @staticmethod
    def funcion(name):
        def wrapper(func):
            def wrapped_func(*args, **kwargs):
                decorator = MyDecorator(func, name)
                # El método __cal__ se llama en la siguiente linea
                # El método __call__ se llama cuando se llama un objeto de esa clase
                resultado = decorator(*args, **kwargs)
                return resultado

            return wrapped_func

        return wrapper


"""
Para que se entienda un poco mas, la linea
  - @MyDecorator.funcion(name="arbarr"): es equivalente a:

    f1 = MyDecorator.funcion(name="arbarr") # f1= funcion(name)
    f2 = f1(add) # f2 = wrapped_func(*args, **kwargs)
    f3 = f2(2,3) # f3= wrapped_func(*args, **kwargs)
    print(f3) # resultado = return x + y

  - También es equivalente a:

    add = MyDecorator.funcion(name = 'arbarr')(add)(2,3)
    print(add)
"""


@MyDecorator.funcion(name="arbarr")
def add(x, y):
    print("adddd")
    return x + y


result = add(2, 3)
print(result)
