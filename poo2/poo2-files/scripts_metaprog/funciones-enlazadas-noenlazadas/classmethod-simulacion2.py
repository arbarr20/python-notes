# Archivo:classmethod-simulacion2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 14/02/2023
# Descripción: Simulación con descriptores de No datos, y  Decoradores de como
# podría funcionar el decorador  @classmethod

"""
Este script define una clase ClassMethodDescriptor que se usa para crear métodos de clase.
El método de clase my_class_method de la clase MyClass se convierte en un método de clase cuando se
pasa a ClassMethodDescriptor. El método de clase my_class_method toma dos argumentos, los cuales
son impresos en la consola cuando el método es llamado. Finalmente, el método de clase es asignado
a la variable bond, que se utiliza para llamar al método con dos argumentos.
"""


class ClassMethodDescriptor:
    def __init__(self, func):
        """
        Inicializa una nueva instancia de ClassMethodDescriptor con una función como parámetro.

        :param func: La función que se usará para crear un método de clase.
        """
        self.func = func
        print(f"self.func:{self.func}")

    def __get__(self, obj, objtype=None):
        """
        Retorna un método de clase asociado con un objeto.

        :param obj: El objeto asociado con el método de clase.
        :param objtype: El tipo de objeto asociado con el método de clase.

        :return: Retorna un método de clase.
        """

        print("Dentro de __get__")
        if objtype is None:
            objtype = type(obj)

        def _bound_method(*args, **kwargs):
            """
            Retorna un método de clase con los argumentos pasados como parámetros.

            :param args: Los argumentos posicionales.
            :param kwargs: Los argumentos de palabra clave.

            :return: Retorna un método de clase con los argumentos especificados.
            """
            print("bound method from __get__")
            return self.func(objtype, *args, **kwargs)

        return _bound_method


class MyClass:
    # @ClassMethodDescriptor
    def my_class_method(cls, arg1: int, arg2: int) -> None:
        # se ejecuta cuando se llama a self.func(objtype, *args, **kwargs), esto sucede
        # cunando bond(1, 2) es ejecutado
        print(f"Class method called on {cls} with arguments {arg1} and {arg2}")

    # Esto reemplaza al descriptor =  #@ClassMethodDescriptor
    my_class_method = ClassMethodDescriptor(my_class_method)


return_get = MyClass.my_class_method
"""
Explicacion de la salida del siguiente print:

<function ClassMethodDescriptor.__get__.<locals>._bound_method at 0x106be7880>:
  lo anterior significa:
   - es una descripción del objeto que representa a la función _bound_method. Esta función es creada dinámicamente dentro del método __get__ de la clase ClassMethodDescriptor y devuelve un objeto de función que ha sido "vinculado" al objeto MyClass

   - la cadena <function ClassMethodDescriptor.__get__.<locals>._bound_method indica que se trata de un objeto de función llamado _bound_method, que es una función local definida dentro del método __get__ de la clase ClassMethodDescriptor. El prefijo <locals> indica que la función se ha definido localmente en otro método.

   - En resumen, esta cadena representa el objeto de función que se ha creado dinámicamente dentro del descriptor ClassMethodDescriptor y que ha sido "vinculado" al objeto MyClass. Este objeto de función puede ser llamado directamente y se comporta como un método de clase de la clase MyClass
"""
print(f"return_get:{return_get}")
# la siguiente linea ejecuta self.func(objtype, *args, **kwargs) que es equivalente a
# my_class_method(MyClass, 1,2)
return_get(1, 2)
