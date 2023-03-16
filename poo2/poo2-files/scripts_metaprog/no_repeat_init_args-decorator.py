# Archivo: descriptor_metaclass.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/01/2023
# Descripción: Solucionar el problema de repetición de código del __init__
# de una clase con Parameter y Signature Implementando Decoradores
# Use un decorador de clases si el objetivo es modificar clases que podrían NO estar relacionadas
# Use una metaclase si está tratando de realizar acciones en combinación con la herencia

from inspect import Parameter, Signature

"""

Nota importante: 
- Estos tipos de script donde se usan metaclases mas lento metaclases, generación dinámica
  de código para ahorrar código Son mas lentos que hacerlo de forma Normal
- Aunque sean mas lentos, creo que Ahorran espació en disco, pesan menos ya que se repite menos
  código
  
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
    # el script original no tiene el list, se puede quitar
    return Signature(
        list(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)
    )


"""
La función add_signature es un decorador. Los decoradores son funciones que reciben una función o clase como argumento
y regresan una nueva función o clase modificada. En este caso, add_signature recibe una lista de nombres y utiliza la
función make_signature para crear una instancia de Signature con esos nombres. Luego, agrega la firma creada como un
atributo de clase llamado __signature__ a la clase que se está decorando.

La función decorate es una función interna que es la que realiza la tarea de agregar el atributo signature a la clase
que recibe, y retorna la clase modificada.

@add_signature("name", "shares", "price") es como se aplica el decorador a una clase en este caso se esta creando una
instancia de Signature con los nombres "name", "shares" y "price".
"""


def add_signature(*names):
    def decorate(cls):
        cls.__signature__ = make_signature(names)
        return cls

    return decorate


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
      en los argumentos del decorador: @add_signature("name", "shares", "price")
    - .bind(*args, **kwargs): ASIGNACIÓN de los valores creados ("arbarr", 35, 2.588) a cada
      uno de los argumentos del decorador, lo entiendo de la siguiente manera:
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


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


# Examples
if __name__ == "__main__":

    @add_signature("name", "shares", "price")
    class Stock(Structure):
        pass

    @add_signature("x", "y")
    class Point(Structure):
        pass

    @add_signature("address", "port")
    class Host(Structure):
        pass

    s = Stock("arbarr", 29, 12.500)
    s = Stock("arbarr", 35, 2.588)
    print(s.__dict__["name"])
    # arbarr
    s.name = "otra cosa"
    print(s.__dict__)
    # {'name': 'otra cosa', 'shares': 35, 'price': 2.588}
