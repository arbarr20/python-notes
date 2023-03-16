# Archivo: descriptor_metaclass.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/01/2023
# Descripción: Solucionar el problema de repetición de código del __init__
# de una clase con Parameter y Signature Usando Metaclases (no crea el __init__) Lo que 
# se hace es convertir los atributos de una clase en los atributos de un objeto con metaclases)

# Use un decorador de clases si el objetivo es modificar clases que podrían NO estar relacionadas
# Use una metaclase si está tratando de realizar acciones en combinación con la herencia

'''
Nota importante: 
- Estos tipos de script donde se usan metaclases mas lento metaclases, generación dinámica
  de código para ahorrar código Son mas lentos que hacerlo de forma Normal
- Aunque sean mas lentos, creo que Ahorran espació en disco, pesan menos ya que se repite menos
  código
  
Conceptos Previos

* Hablemos primero de `inspect.signature`: es utilizada para obtener la firma
  de un objeto, que incluye información sobre los argumentos y los valores
  predeterminados de los argumentos de una función o método.La firma se
  devuelve como un objeto Signature, el cual tiene información sobre los
  parámetros del objeto, como el nombre, el tipo y el valor predeterminado
  (si lo tiene). También se pueden obtener información sobre los argumentos
  posicionales y los argumentos con nombre:

    def my_function(a,b:str='arbarr', *args, **kwargs):
        pass

    sig = inspect.signature(my_function)
    print(sig)
    # print(my_function.__signature__) es igual a sig
    # (a, b: str = 'arbarr', *args, **kwargs)

 Con esta información se puede ver el nombre, el tipo y el valor
 predeterminado de cada parámetro de la función.

  - No solo se puede ver información, Se puede crear un Signature:
     1. definir la función a la que se le aplicarán los parámetros
     2. Crear un objeto Parameter (obj_parameter)
     3. Crear el objeto signature (obj_sig) del `obj_parameter` para cada uno
       de los argumentos de la función (hay que iterar sobre ellos)
     4. Asignar la firma a la función por medio del método especial
       `__signature__` (my_funcion.__signature__=obj_sig)

 - Como se crea en realidad la firma Signature:
   - La clase Signature del módulo inspect en Python, tiene un constructor que
     recibe los siguientes parámetros:

      - `parameters`: Una secuencia de objetos Parameter que representan los
        parámetros de la función o método. Este parámetro es obligatorio.

      - return_annotation: Un objeto que representa la anotación de retorno de
        la función o método. Este parámetro es opcional y por defecto es
        `Signature.empty`. Una anotación de retorno es un objeto que se
        utiliza para especificar el tipo de retorno de una función o método.
        En Python, las anotaciones de retorno son opcionales, y se pueden
        especificar mediante el uso de la sintaxis -> seguida del tipo de
        retorno, justo antes de los dos puntos que indican el final de la
        definición de la función

        def my_function(a: int) -> str:
            return str(a)

        from inspect import Signature
        sig = Signature(parameters=[], return_annotation=str)
        print(sig.return_annotation)
        # <class 'str'>

    - La opción bind: de la clase Signature se utiliza para vincular los
      parámetros de una función o método con valores específicos.
      La clase BoundArguments es la implementación predeterminada que se
      utiliza para este propósito, pero se puede proporcionar una clase
      personalizada que herede de BoundArguments y sobrescriba su
      comportamiento.
      La clase BoundArguments es una clase que almacena los argumentos de una
      función o método vinculados a una instancia de Signature. Una vez que se
      ha vinculado una instancia de BoundArguments a una instancia de
      Signature, se pueden acceder a los argumentos mediante el uso de la
      notación de punto.
      Es por esto que al usar bind, se puede usar el atributo `arguments` de
      la clase `BoundArguments` que es un diccionario con los argumentos
      vinculados y sus valores

      from inspect import Parameter, Signature,signature


        # El orden de los parámetros es importante respetarlo
        # no es lo mismo (a: int, *args, **kwargs)
        # que (a: int,**kwargs, *args, )

        def my_function(a: int, *args, **kwargs):
            pass


        # Crear un objeto Parameter
        # Que sera insertado ademas de los ya existentes, quedaría algo como
        # (a: int, name = 'arbarr 20', *args, **kwargs)
        new_param = Parameter('name', Parameter.POSITIONAL_OR_KEYWORD, default='arbarr 20')

        # CONSULTAMOS la FIRMA de la función a la que añadiremos el parámetro
        firma = signature(my_function)

        # Creamos una lista con los valores de los parámetros originales de la función
        # Asi [<Parameter "a: int">, <Parameter "*args">, <Parameter "**kwargs">]
        orig_param = list(firma.parameters.values())

        # Aquí es donde insertamos el nuevo parámetro a la función original
        # OJO respetar el orden de los parámetros, en este caso como es name = ''
        # se inserta en la posición 1
        orig_param.insert(1, new_param)


        # De esta otra forma podríamos crear una lista de parámetros
        # para ser insertados en la función o método
        """ p = [
            Parameter('a', Parameter.POSITIONAL_OR_KEYWORD, annotation=int),
            Parameter('b', Parameter.POSITIONAL_OR_KEYWORD, annotation=str),
            Parameter('c', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
            Parameter('args', Parameter.VAR_POSITIONAL),
            Parameter('kwargs', Parameter.VAR_KEYWORD)
            ]
        # Crear un objeto Signature con el parámetro creado
        sig = Signature(p) """


        # CREAMOS una FIRMA con los parámetros totales de la función
        sig = Signature(orig_param)
        # Asignar la firma a la función
        my_function.__signature__ = sig

        # Vincular los argumentos de la función a una instancia de Signature
        bound_args = sig.bind(1, 'arbarr dev', 5, 2, 3, 4, d=6)
        print(bound_args.arguments)
        # Salida:
        # {'a': 1, 'name': 'arbarr dev', 'args': (5, 2, 3, 4), 'kwargs': {'d': 6}}


* Parameter: es utilizada para representar un parámetro de una función o
  método. Cada objeto Parameter tiene información sobre el nombre, el tipo, el
  valor predeterminado y otros atributos del parámetro.

  La clase Parameter del módulo inspect de Python, recibe los siguientes
  argumentos:
    1. name (str): es el nombre del parámetro. Este es un argumento
    obligatorio.
    2. kind (int): Este es un argumento obligatorio, es el tipo de parámetro,
      puede ser:
      - POSITIONAL_OR_KEYWORD
      - VAR_POSITIONAL
      - VAR_KEYWORD
      - POSITIONAL_ONLY
      - KEYWORD_ONLY.
    3. default (Any): es el valor por defecto del parámetro, si no tiene valor
    por defecto, este debe ser inspect.Parameter.empty. Este es un argumento
    opcional.
    4. annotation (Any): es la anotación del tipo del parámetro, si no tiene
    anotación, este debe ser inspect.Parameter.empty.
    Este es un argumento opcional.

   - No solo es para extraer información de la firma de los parámetro de una
      función
   - También sirve para asignar atributos a los (atributos o argumentos
     de alguna función o método): Ver el ejemplo de mas arriba

* __signature__: es un atributo especial en Python que contiene información sobre
los parámetros esperados y el orden en el que deben ser proporcionados al momento de llamar a una
función o método. Este atributo es proporcionado por la biblioteca inspect y se utiliza para
obtener información sobre los parámetros de una función o método, como su nombre, tipo, modo
(posicional, clave-valor, etc.) y valor predeterminado.
'''


from inspect import Parameter, Signature

# Aquí en Adelante la Explicación del código

"""
* def make_signature(names):recibe como argumento una lista de nombres, y
  utiliza un generador de comprensión para iterar sobre cada nombre y crear un
  objeto "Parameter" utilizando el nombre y el modo "POSITIONAL_OR_KEYWORD".
  El objeto "Parameter" se utiliza para crear un objeto "Signature" que
  contiene información sobre los parámetros esperados y el orden en el que
  deben ser proporcionados al momento de crear una instancia de la clase .

  la función devuelve el objeto "Signature" que se utiliza en la clase "Structure" para vincular
  los argumentos recibidos al momento de crear una instancia de la clase con los nombres de los
  campos "_fields" y establecer los valores de estos campos como atributos de la instancia de la
  clase.
"""


def make_signature(names):
    # se podría quitar el list
    return Signature(list(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names))


"""
* class StructMeta(type):Metaclase personalizada para crear nuevas clases con una funcionalidad
  específica.Redefine el método new para personalizar la creación de nuevas clases

  - clsobj = es la clase que se crea, esta clase TRAE como parámetro una variable `_fields`
    que es una lista de nombres que se convertirán el los argumentos del constructor de clsobj.

  - sig = make_signature(clsobj._fields): Es la `Signature` la firma que certifica que cada uno
    de los elementos de `_fields` SON PARÁMETROS. sig adquiere valores como:
      - sig=(name, shares, price) que es de tipo <class 'inspect.Signature'>

  - setattr(clsobj, "__signature__", sig): agrega este objeto Signature (sig) como atributo de la
    clase recién creada (clsobj) con el nombre __signature__.
    - traduciendo esta linea sería algo como:
      clsobj.__signature__ = sig

* return clsobj: Retorna la clase recién creada
"""


class StructMeta(type):
    # _fields = []  # Fue agregado

    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, "__signature__", sig)
        return clsobj


"""
* class Structure(metaclass=StructMeta):Clase base que utiliza la metaclase StructMeta para
  personalizar la creación de nuevas clases. Define una lista vacía "_fields" y un método __init__.

  - _fields = []:La lista vacía _fields se utiliza para especificar los campos que se esperan en
    las clases que heredan de Structure. Cada una de estas clases debe definir su propia lista
    _fields con los nombres de los campos esperados.

  - def __init__(self, *args, **kwargs):El método __init__ se encarga de vincular los argumentos
    recibidos al momento de crear una instancia de la clase con los nombres de los campos _fields
    y establecer los valores de estos campos como atributos de la instancia de la clase. Utiliza
    el objeto Signature en el atributo __signature__ para vincular los argumentos recibidos con
    los nombres de los campos _fields

      - self: es el objeto que se crea de una clase que hereda de Structure asi:
        * s = Stock("arbarr", 35, 2.588) en este caso `s` es self.
      - *args, **kwargs: son `"arbarr", 35, 2.588` los valores de cada uno de los indices de
        _fields

  - bound = self.__signature__.bind(*args, **kwargs):

    - self.__signature__:son los nombres atributos del objeto self. los que se definieron
      en la lista _fields.`(name, shares, price)`
    - .bind(*args, **kwargs): ASIGNACIÓN de los valores creados ("arbarr", 35, 2.588) a cada
      uno de los indicies de _fields, lo entiendo de la siguiente manera:
        * name = arbarr
        * shares = 35
        * price = 2.588
  Al final bound queda asi: bound: <BoundArguments (name='arbarr', shares=35, price=2.588)>

  - for name, val in bound.arguments.items():
    - bound.arguments.items(): como bound es de tipo BoundArguments, esto permite usar `arguments`
    esta linea retorna algo asi:
      - dict_items([('name', 'arbarr'), ('shares', 35), ('price', 2.588)]), una tupla calve valor
    - setattr(self, name, val): e utiliza el método setattr para establecer el valor de val como
      atributo de la instancia de la clase con el nombre del campo name.Esto es equivalente a escribir
      - self.name = val  ---> self.name = arbarr
"""


class Structure(metaclass=StructMeta):
    _fields = []
    # __signature__ = Signature()  # Fue agregado

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


# Ejemplo
if __name__ == "__main__":

    """
    En resumen lo que se trata de hacer con este script es  convertir lo que normalmente se haría Asi:

      class Stock(Structure):

        def __init__(self, name, shares, price):
          self.name = name
          self.shares = shares
          self.price = price

    A algo como esto:

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    """

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    class Point(Structure):
        _fields = ["x", "y"]

    class Host(Structure):
        _fields = ["address", "port"]

    s = Stock("arbarr", 35, 2.588)
    print(s.__dict__['name'])
    # arbarr
    s.name = 'otra cosa'
    print(s.__dict__)
    # {'name': 'otra cosa', 'shares': 35, 'price': 2.588}
   
