# Archivo: staticmethod-simulacion1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 15/03/2023
# Descripción: se usan Métodos No Enlazados - descriptores - decoradores - para
# simular el comportamiento del decorador @estaticmethod

'''
El script define una clase staticmetho, que se utiliza como un decorador para definir métodos 
estáticos. Además, define la clase MyClass, que tiene tanto un método de clase como un método
estático definidos. Luego crea una instancia de MyClass y llama a los métodos de clase y estáticos
en la clase y en la instancia. Cuando se llama a los métodos, se imprimen mensajes en la consola
para mostrar cuándo se llaman los métodos y qué argumentos se pasan a ellos. En resumen, el script 
cómo usar la clase staticmetho para definir métodos estáticos y cómo llamar a métodos de clase y 
estáticos en una clase y en una instancia.

El método __call__ no hace mayor cosa, pero puede ser llamado en __get__ solo haciendo `self()`,
recuerde que __call__ hace que se pueda llamar una instancia como una función.

El Método __repl__ da una descripción de un objeto, aunque solo es recomendable usar para
depuración y pruebas, aquí lo usamos para recordar como se usa (:, este método se llama cuando
intentamos imprimir por consola el objeto descriptor my_class_method, y eso ocurre cuando hacemos
`print(self)` en la clase `staticmetho`

Recuerde que los métodos estáticos pueden ser llamados por:
_ la clase
- por un objeto
- no llevan cls ni self
- no pueden acceder a los atributos del objeto ni la clase
'''

class staticmetho():
    """
    Descriptor para un método estático.

    Este descriptor se puede usar como decorador para convertir un método en un método estático.

    Attributes:
    -----------
    func: function
        El método que se va a convertir en un método estático.
    """

    def __init__(self, func: object) -> None:
        """
        Inicializa la instancia del descriptor.

        Parameters:
        -----------
        func: function
            El método que se va a convertir en un método estático.
        """
        self.func = func

    def __get__(self, obj: object, objtype: type = None) -> object:
        """
        Devuelve el método estático.

        Parameters:
        -----------
        obj: object
            La instancia del objeto que contiene el descriptor.
        objtype: type
            El tipo del objeto que contiene el descriptor.

        Returns:
        --------
        callable:
            El método estático.
        """
        print('__get__')
        print(f'self-repr:{self}')
        print(f'self()-__call__: {self()}')
        if objtype is None:
            objtype = type(obj)
        return self._get_impl(objtype)

    def _get_impl(self, objtype: type) -> object:
        """
        Devuelve el método estático.

        Parameters:
        -----------
        objtype: type
            El tipo del objeto que contiene el descriptor.

        Returns:
        --------
        callable:
            El método estático.
        """
        # no asigna ningún objeto al método, ya que es un método estático
        # esta linea es la clave para que self.func = my_class_method = método estático
        result = self.func.__get__(None, objtype)
        return result

    def __call__(self, *args, **kwds) -> callable:
        """
        Llama al método estático.

        Parameters:
        -----------
        *args: Any
            Argumentos posicionales pasados al método.
        **kwds: Any
            Argumentos de palabras clave pasados al método.

        Returns:
        --------
        callable:
            El resultado del método estático.
        """
        print('inside __call__')
        return self.func(*args, **kwds)

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del descriptor.

        Returns:
        --------
        str:
            Una cadena que representa el descriptor.
        """
        return 'inside __repr__ <staticmetho object at %s>' % hex(id(self))


class MyClass:
    """
    Clase de ejemplo para demostrar el uso del descriptor staticmetho.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Inicializa una instancia de MyClass.

        Parameters:
        -----------
        x: int
            El valor de x.
        y: int
            El valor de y.
        """
        self.x = x
        self.y = y

    @staticmetho
    def my_static_method() -> str:
        """
        Método estático de ejemplo.

        Returns:
        --------
        str:
            Una cadena de ejemplo.
        """
        return "Hello, I'm a static method!"

    @classmethod
    def my_class_method(cls, z: int) -> str:
        """
        Método de clase de ejemplo.

        Parameters:
        -----------
        z: int
            Un número de ejemplo.

        Returns:
        --------
        str:
            Una cadena de ejemplo.
        """
        return f"Hello, I'm a class method of {cls} with argument {z}!"

my_instance = MyClass(1, 2)

# calling a static method
result = MyClass.my_static_method()
print(result)


# calling a class method
result = MyClass.my_class_method(3)
print(result)

# calling a static method on an instance
result = my_instance.my_static_method()
print(result)

# calling a class method on an instance
result = my_instance.my_class_method(4)
print(result)


