# Archivo: example5_propety_solution_repeat_code.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/02/2023
# Descripción:Solucionar el problema de repetición de código del __init__, y la molesta
# repetición de código de las property's de una clase con Parameter y Signature Usando Metaclases
# (no crea el __init__) Lo que  se hace es convertir los atributos de una clase en los atributos
# de un objeto con metaclases)

"""

Nota importante: 
- Estos tipos de script donde se usan metaclases mas lento metaclases, generación dinámica
  de código para ahorrar código Son mas lentos que hacerlo de forma Normal
- Aunque sean mas lentos, creo que Ahorran espació en disco, pesan menos ya que se repite menos
  código

Se hace una fusion entre 2 scripts ya vistos:

1. descriptor_metaclass.py: Utiliza una Metaclase descriptora que:
  - Dinámicamente crea descriptores para validar y estructurar los atributos de una clase
  - CREA de forma dinámica el método __init__ con `exec` para no repetirlo cada que se crea
    una clase

2. no_repeat_init_args.py: Su misión principal es evitar la repetición de código del método
  __init__ pero a diferencia del script del item1, este usa:
    - las bibliotecas Parameter y Signature del modulo inspect
    - No usa la creación del código dinámico.
    - (no crea el __init__) Lo que  se hace es convertir los atributos de una clase en los atributos
       de un objeto con metaclases)

Ahora hablando de este script example5_propety_solution_repeat_code.py:

  - Usa una clase Descriptor donde se crean los métodos descriptores No de forma dinámica,
    sino Como se usa normalmente, para validar y estructurar los atributos de una clase
    (property's)

  -  evitar la repetición de código del método  __init__ usando
    - las bibliotecas Parameter y Signature del modulo inspect
    - No usa la creación del código dinámico.
    - (no crea el __init__) Lo que  se hace es convertir los atributos de una clase en los atributos
       de un objeto con metaclases)

  - Algo que no se había dado cuenta en los scripts del punto 1 y 2, es que se usan property's
    No con decoradores comose usan normalmente, so no por medio de metaclases,
    en este script pasa igual, y esto evita la repetición de código de las property's cuando
    se usan con decoradores, en la cual para cada atributo (propiedad) hay que crear prácticamente 3
    métodos.
"""

from inspect import Parameter, Signature
import re
from collections import OrderedDict

'''
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
            
        Crear un objeto Parameter
        Que sera insertado ademas de los ya existentes, para que de resultado algo como:
        (a: int, name = 'arbarr 20', *args, **kwargs)
        se realizaría asi:

        new_param = Parameter('name', Parameter.POSITIONAL_OR_KEYWORD, default='arbarr 20')

        # CONSULTAMOS la FIRMA de la función a la que añadiremos el parámetro
        firma = signature(my_function)

        # Creamos una lista con los valores de los parámetros originales de la función
        # Asi:
        [<Parameter "a: int">, <Parameter "*args">, <Parameter "**kwargs">]
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

# Podemos seguir con el script original

"""
class Descriptor:
    La clase Descriptor es una clase base que proporciona una implementación básica
    de los métodos __set__ y __delete__ de un descriptor en Python.

    El método __set__ se utiliza para establecer el valor de un atributo y el método __delete__ para
    borrar un atributo.

    Estos métodos permiten que un objeto actúe como un atributo en un objeto, permitiendo
    personalizar el comportamiento de la asignación y borrado de atributos en tiempo de ejecución.

    la clase Descriptor establece un nombre de atributo para cada objeto de descriptor y permite
    que los objetos de descriptor personalicen su comportamiento al  sobrescribir
    __set__ o __delete__.
"""


class Descriptor:
    """Clase base de los descriptores.

    Proporciona una implementación básica para la gestión de la asignación y eliminación de
    atributos.
    """

    def __init__(self, name=None):
        """Inicializa la instancia.

        :param name: Nombre del atributo que se gestionará.
        """
        self.name = name

    def __set__(self, instance, value):
        """Asigna un valor a un atributo en una instancia.

        :param instance: Instancia a la que se asignará el valor.
        :param value: Valor a asignar.
        """
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        """Elimina un atributo de una instancia.

        :param instance: Instancia de la que se eliminará el atributo.
        """
        raise AttributeError("No se puede eliminar")


class Typed(Descriptor):
    """Descriptor con tipado.

    Verifica que el valor asignado a un atributo sea del tipo especificado.
    """

    ty = object

    def __set__(self, instance, value):
        """Asigna un valor a un atributo en una instancia.

        Verifica que el valor sea del tipo especificado antes de asignarlo.

        :param instance: Instancia a la que se asignará el valor.
        :param value: Valor a asignar.
        """
        if not isinstance(value, self.ty):
            raise TypeError("Se esperaba %s" % self.ty)
        super().__set__(instance, value)


# Tipos especializados
class Integer(Typed):
    """Descriptor de tipo entero."""

    ty = int


class Float(Typed):
    """Descriptor de tipo float ."""

    ty = float


class String(Typed):
    """Descriptor de tipo String."""

    ty = str


class Positive(Descriptor):
    """
    Clase que hereda de `Descriptor` y se encarga de validar que el valor asignado
    sea mayor o igual a cero.

    Si se intenta asignar un valor negativo, lanzará una excepción `ValueError`
    """

    def __set__(self, instance, value):
        """
        Método que es llamado cuando se intenta asignar un valor a un atributo
        que usa este descriptor.

        :param instance: La instancia a la que se está asignando el atributo
        :param value: El valor que se intenta asignar
        :raises: ValueError si el valor asignado es menor a cero
        """
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


# More specialized types se usan clases mixin
class PosInteger(Integer, Positive):
    """
    La clase `PosInteger` es una combinación de `Integer` y `Positive` que permite agregar una
    validación de positiva a los atributos de tipo Entero.
    """

    pass


class PosFloat(Float, Positive):
    """
    La clase `PosInteger` es una combinación de `Float` y `Positive` que permite agregar una
    validación de positiva a los atributos de tipo Float.
    """

    pass


# Length checking
class Sized(Descriptor):
    """
    La clase `Sized` es una subclase de `Descriptor` que agrega una validación de longitud a los atributos.
    """

    def __init__(self, *args, maxlen, **kwargs):
        """
        Inicializa la clase `Sized` con un atributo `maxlen` que representa la longitud máxima permitida para el atributo.

        :param maxlen: La longitud máxima permitida para el atributo.
        :type maxlen: int
        """
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        """
        Verifica que el tamaño de `value` sea menor o igual a `self.maxlen`.
        Si `value` es demasiado largo, se genera una excepción `ValueError` con el mensaje "Too big".

        :param instance: La instancia donde se establecerá el valor.
        :param value: El valor a establecer.
        :raises: ValueError si el tamaño de `value` es mayor a `self.maxlen`.
        """
        if len(value) > self.maxlen:
            raise ValueError("Too big")
        super().__set__(instance, value)


class SizedString(String, Sized):
    """
    La clase `SizedString` es una combinación de `String` y `Sized` que permite agregar una
    validación de longitud a los atributos de tipo string.
    """

    pass


class Regex(Descriptor):
    """
    Descriptor para validar una cadena con un patrón.

    Atributos:
        pat (re.pattern): Patrón a validar.
    """

    def __init__(self, *args, pat, **kwargs):
        """
        Inicializa el Descriptor Regex.

        Args:
            pat (str): Patrón a validar.
        """
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        """
        Valida que `value` coincida con el patrón `self.pat`.

        Args:
            instance: Instancia de un objeto.
            value: Valor a asignar.

        Raises:
            ValueError: Si `value` no coincide con el patrón `self.pat`.
        """
        if not self.pat.match(value):
            raise ValueError("Invalid string")
        super().__set__(instance, value)


class SizedRegexString(SizedString, Regex):
    """
    Descriptor para validar una cadena con un tamaño máximo y un patrón.
    """

    pass


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

  Otra forma sin usar  un generador de compresión es:

  for name in names:
    list(Parameter((name, Parameter.POSITIONAL_OR_KEYWORD)))

Normalmente sale una advertencia por que no se usa list asi:
- return Signature(list(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names))
No se que implicaciones tenga



"""


def make_signature(names):
    """
    Crea un objeto `Signature` a partir de una lista de nombres de campos.

    Parameters:
    names (list of str): Lista de nombres de los campos.

    Returns:
    Signature: Un objeto `Signature` con un parámetro por cada nombre en `names`.
    """
    return Signature(
        list(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)
    )


"""
* class StructMeta(type):Metaclase personalizada para crear nuevas clases con una funcionalidad
  específica.Redefine el método new para personalizar la creación de nuevas clases

* __prepare__(cls, name, bases): se llama al comienzo de la creación de una
 nueva clase.Este método recibe:
  * cls: el nombre de su propia clase (que es la metaclase = StructMeta)
  * name: el nombre de la clase que implementa la metaclase
    * el nombre de la clase cuyo padre implementa la metaclase
  * bases: son las clases padres de la clase que se esta creando
podemos usar los valores de esto parámetros para hacer alguna operación o
modificación sobre ellos, pero lo mas importante que hace __prepare__ es
retornar un DICCIONARIO que se convertirá el el espacio de nombres de la clase
que se va a crear,(name).
 * podemos insertar algún valor en este espacio de nombres, seria como un valor
   dinámico a la clase que se crea. lo importarte de este DICCIONARIO es que se
   pasa al método __new__ como el parámetro `clsdict`
    def __prepare__(cls, name, bases):
        dic = {'NewVar':'MyNewVar'}
        d = OrderedDict(dic)
        return d
    # ahora la variable Newvar estará dentro del clsdict
    # y la clase y clsname tendrá este atributo dentro de su diccionario
    def __new__(cls, clsname, bases, clsdict):
* OrderDict(): me retorna un diccionario de lista de tuplas
    OrderedDict([('__module__', '__main__'), ('__qualname__', 'Structure')]}

* def __new__(cls, clsname, bases, clsdict):
  * cls, clsname, bases = cls, name, bases de __prepare__ respectivamente
  * clsdict: es un diccionario pasado por __prepare__ que generalmente viene
  vació, o con algún atributo dinámico que se haya agregado en el
  retorno de __prepare__.
    * Este diccionario se llena aquí en __new__ con los atributos y métodos de
    la clase clsname.

observe el siguiente bloque de código:
fields = [key for key, val in clsdict.items() if isinstance(val, Descriptor) ]

podemos traducirlo a:
fields = []
for key, val in clsdict.items():
    if isinstance(val, Descriptor):
        fields.append(key)

lo podemos dejar como:
fields = map(lambda key: key, filter(lambda key_val: isinstance(key_val[1],
    Descriptor), clsdict.items()))

filter: filtra los elementos de un iterable usando un criterio
Pero que traduce todo esto:
1. se itera sobre los items del clsdict
2. si el VALOR de una de las claves (que es un objeto) es una instancia
  de Descriptor, se agrega la CLAVE a la lista fields.

  2.1. Al ser una instancia de Descriptor esto implica varios cosas que
    tienen injerencia sobre las lineas de código que siguen. Segun el tipo de descriptor que implemente,
    se aplican las validaciones respectivas

    * Analicemos la siguiente Linea:
    for name in fields:
        clsdict[name].name = name
     
por cada un ode los objetos descriptores guardados en fields
acceda a su atributo name y asignale el su propio nombre. muy confuso no:
obj = Descriptor("aquí debe ir un parámetro que es el nombre del obj,
pero es OPCIONAL)

* El echo de ser opcional da paso aplicar el for anterior.
que traduciéndolo seria:

obj = Descriptor("obj") -- clsdict[name].name = name

El for anterior lo dejaríamos asi:

map(lambda x: setattr(clsdict[x], 'name', x), fields)

es diferente a usar

*list(map(lambda x: setattr(clsdict[x], 'name', x), fields))

El uso del list en este caso es necesario para evaluar el objeto map completo
y obtener una lista con el resultado. Si no se usa list, el objeto map solo se
evalúa hasta el primer elemento y se detiene.

Esto es porque map es un objeto iterable que retorna un objeto generador, que
se evalúa "lazy" o perezoso, es decir, solo se evalúa un elemento a la vez
cuando es necesario. Al usar list, se evalúa el objeto completo y se obtiene
una lista con el resultado de aplicar la función a cada uno de los elementos.
todo esto es por el modo en el que se ejecuta setattr que necesita de una lista
no de un objeto map.

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

En resumen:

* StructMeta se encargará CREAR LA FIRMA de estos "atributos de clase, que Irán " a su __init__",
ademas ASIGNAla firma a la clase creada
* y como heredan de un Descriptor, se aplicarán las validaciones especificas
  de cada descriptor ademas de estructurar toda su lógica descriptora
"""

# esta metaclase es muy clave
class StructMeta(type):
    """
    La clase StructMeta es una metaclase que se encarga de crear la estructura de una clase
    basada en Descriptores.
    """

    @classmethod
    def __prepare__(cls, name, bases):
        """
        Este método se encarga de preparar la estructura de un diccionario para los
        atributos de la clase que se está definiendo.
        """
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):
        """
        Este método se encarga de crear la clase que se está definiendo.
        """
        fields = [key for key, val in clsdict.items() if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name
        # Es muy importante que la clase se cree entes de crear la firma
        # hay un matiz importante: (dict(clsdict))
        # normalmente es: clsobj = ...(cls, clsname, bases, clsdict)
        # esto es un diccionario adecuado para el contenido de la clase
        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))
        print(f"field: {fields}")
        # se crea la firma con los parámetros respectivos
        sig = make_signature(fields)
        # se asigna la firma a la clase creada
        setattr(clsobj, "__signature__", sig)
        return clsobj


"""
* class Structure(metaclass=StructMeta):Clase base que utiliza la metaclase StructMeta para
  personalizar la creación de nuevas clases. Define  un método __init__.
 
  - def __init__(self, *args, **kwargs):El método __init__ se encarga de VINCULAR los argumentos
    recibidos al momento de crear una instancia de la clase con los nombres de los campos *args,
    y **kwargs para establecer los valores de estos campos como atributos de la instancia de la
    clase en el (__init__). Utiliza  el objeto Signature en el atributo __signature__ para vincular
    los argumentos recibidos con  los nombres de los campos *args, y**kwargs

      - self: es el objeto que se crea de una clase que hereda de Structure asi:
        * s = Stock("arbarr", 35, 2.588) en este caso `s` es self.
      - *args, **kwargs: son `"arbarr", 35, 2.588`

  - bound = self.__signature__.bind(*args, **kwargs):
    - self.__signature__:son los nombres atributos del objeto self. los que vincularon
    .`(name, shares, price)`
    - .bind(*args, **kwargs): ASIGNACIÓN de los valores creados ("arbarr", 35, 2.588) a cada
      uno de los valores pasados en *args, **kwargs:
        * name = arbarr
        * shares = 35
        * price = 2.588
  Al final bound queda asi: bound: <BoundArguments (name='arbarr', shares=35, price=2.588)>
  
  - for name, val in bound.arguments.items():
    - bound.arguments.items(): como bound es de tipo BoundArguments, esto permite usar `arguments`
    esta linea retorna algo asi:
      - dict_items([('name', 'arbarr'), ('shares', 35), ('price', 2.588)]), una tupla calve valor
    - setattr(self, name, val): se utiliza el método setattr para establecer el valor de val como
      atributo de la instancia de la clase con el nombre del campo name.Esto es equivalente a
      escribir
      - self.name = val  ---> self.name = arbarr
"""


class Structure(metaclass=StructMeta):
    """
    La clase Structure es la clase base que permite definir una estructura a partir de
    descriptores.
    """

    def __init__(self, *args, **kwargs):
        """
        Este método inicializa una instancia de la clase Structure.
        """
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


if __name__ == "__main__":
    """
    Nombre: Es un descriptor con su respectiva validación SizedRegexString,
    """

    class Persona(Structure):
        nombre = SizedRegexString(maxlen=8, pat="[A-Z]+$")
        edad = PosInteger()
        sueldo = PosFloat()

    arbarr = Persona("ARBARR", 34, 15.200)
    print(arbarr.__dict__)
    print(arbarr.edad)
    print(Persona.__dict__)
