# Archivo: descriptor_metaclass.py
# Autor: Arbarr20 y ayuda online
# Fecha: 08/01/2023
# Descripción: Descriptor con metaclases
# Este código define una serie de clases que se pueden usar como descriptores
# para validar y estructurar los atributos de una clase.

# from inspect import Parameter, Signature
import re
from collections import OrderedDict

'''
Nota importante:
- Estos tipos de script donde se usan metaclases mas lento metaclases, generación dinámica
  de código para ahorrar código Son mas lentos que hacerlo de forma Normal
- Aunque sean mas lentos, creo que Ahorran espació en disco, pesan menos ya que se repite menos
  código
El marco común para crear un descriptor es el siguiente:

https://github.com/arbarr20/python-notes/blob/poo2/poo2/poo2-files/scripts_descriptores/descriptor4.py

'''


# Utility functions
def _make_init(fields):
    '''
    Recibe una lista[] de parámetros, que se usaran para crear un método
    __init__

    lo podríamos reemplazar por este otro código:

    fields = ['name', 'edad']
    code1 = f'def __init__(self, {",".join(["name", "edad"])}):\n'
    for name in fields:
        # Cuidado con los espacios son muy importantes
        code1 += f'    self.{name} = {name}\n'
    print(code1)

    # la salida es la siguiente
    def __init__(self, name,edad):
        self.name = name
        self.edad = edad
    '''

    code = 'def __init__(self, %s):\n' % \
        ','.join(fields)

    for name in fields:
        code += '    self.%s = %s\n' % (name, name)
    return code


'''
Descripción de def _make_setter(dcls):
    * es una función auxiliar que se utiliza para crear el método __set__
    de un descriptor, ademas de implementar validaciones (set_code)
    dependiendo de la  clase(dcls) que lo llame

        * def __set__(self, instance, value) -> None:
            instance.__dict__[self.name] = value

        * def __set__(self, instance, value) -> None:
|||||||       if not isinstance(value, self.ty):
por la|||||       raise TypeError("Expected %s" % self.ty)
herencia ->|  instance.__dict__[self.name] = value
se inserta esta linea|
||||||||||||||||||||||

        * def __set__(self, instance, value) -> None:
            if value < 0:
                raise ValueError("Expected >= 0")
            instance.__dict__[self.name] = value

        * def __set__(self, instance, value) -> None:
            if len(value) > self.maxlen:
                raise ValueError("Too big")
            instance.__dict__[self.name] = value

        * def __set__(self, instance, value) -> None:
            if not self.pat.match(value):
                raise ValueError("Invalid string")
            instance.__dict__[self.name] = value

    * La función _make_setter crea el código para el método __set__ de forma
    dinámica en tiempo de ejecución, utilizando el método set_code de cada
    clase en la jerarquía de herencia del descriptor. El método set_code es un
    método estático que debe definirse en cada clase de descriptor y que
    devuelve una lista de líneas de código que se deben ejecutar para validar
    y estructurar el valor asignado.

    * La función _make_setter recorre la jerarquía de herencia del descriptor
    (dcls.__mro__) y, para cada clase en la jerarquía, si la clase tiene un
    método set_code, añade las líneas de código devueltas por este método al
    código del método __set__. De esta forma, se pueden añadir validaciones y
    estructuraciones adicionales en clases derivadas sin tener que escribir
    todo el código del método __set__ de nuevo.

* code = 'def __set__(self, instance, value):\n': es un constante para ir
armando el cuerpo del setter del descriptor

* dcls: En este contexto dcls siempre hace referencia a una clase que hereda o
implementa una metaclase

* for d in dcls.__mro__: recorre toda la linea de herencia, recordar que en
este contexto se trabaja con metaclase, y todas las clases que hereden de una
clase la cual implemente una metaclase, se ejecuta el código de la metaclase

* if 'set_code' in d.__dict__: si cada clase que tiene que ver con la metaclase
 tiene un método set_code en palabra clave de su diccionario

  * for line in d.set_code(): el set_code de las clases es una arreglo de
    strings, por esto  este for.

      * code += '    ' + line + '\n': se agrega cada linea del set_code de
      la clase llamada, para armar su setter del descriptor

      * El d.set_code(): es la razón por la que en las clases descriptoras
      set_code es un método estático, ya que este tipo de métodos es común que
      sea llamado solo por su clase y d es la clase

* return code: retorna el método __set__ final de cada clase descriptora, por
ejemplo:
  def __set__(self, instance, value) -> None:
            if len(value) > self.maxlen:
                raise ValueError("Too big")
            instance.__dict__[self.name] = value


'''


# función auxiliar que se utiliza para crear el método __set__ de un descriptor
def _make_setter(dcls):
    code = 'def __set__(self, instance, value):\n'
    for d in dcls.__mro__:

        if 'set_code' in d.__dict__:
            for line in d.set_code():

                code += '    ' + line + '\n'
    return code


''''
Descripción de class DescriptorMeta(type):

* def __init__(self, clsname, bases, clsdict):Este es el método __init__ de
la metaclase, que se ejecuta al momento de crear una nueva clase de descriptor.
Toma como argumentos el nombre de la clase (clsname), la tupla de clases base
(bases) y el diccionario de atributos y métodos de la clase (clsdict).

* if '__set__' not in clsdict:Este código verifica si la clase que se está
creando tiene un método __set__ definido. Si no lo tiene, significa que la
clase es una clase base de descriptor y necesita generar el método __set__
de forma dinámica.

* code = _make_setter(self): Aquí se llama a la función _make_setter para
generar el código del método __set__ de forma dinámica. La clase de descriptor
que se está creando (self) se pasa como argumento a la función.

* exec(code, globals(), clsdict): Aquí se utiliza la función exec para
ejecutar el código del método __set__ generado por _make_setter. El código se
ejecuta en el contexto global y se agrega al diccionario de atributos y
métodos de la clase (clsdict).

Aclaraciones de exec:

* La función predefinida exec() en Python permite ejecutar
código dinámicamente. Acepta los siguientes parámetros:

  * code: es una cadena de texto que contiene el código Python a ejecutar.
    Este parámetro es obligatorio.

  *globals: es un diccionario que representa el espacio de nombres global
  en el que se ejecutará el código. Si no se proporciona, se utilizará el
  espacio de nombres global actual. Este parámetro es opcional.

    globals_dict = {"x": 5, "y": 15}
    code = "print(x + y)"
    exec(code, globals_dict)  # Imprime: 20


  * locals: es un diccionario que representa el espacio de nombres local en el
  que se ejecutará el código. Si no se proporciona, se utilizará el espacio de
  nombres local actual. Este parámetro es opcional.

  locals_dict = {"x": 50, "y": 100}
  code = "print(x + y)"
  exec(code, globals(), locals_dict)  # Imprime: 150

Es importante tener en cuenta que si una variable existe tanto en el espacio
de nombres global como en el local, se utilizará la variable del espacio de
nombres local.

# Definimos un diccionario de variables globales
globals_dict = {"x": 5, "y": 15, "z": 25}

# Definimos un diccionario de variables locales
locals_dict = {"x": 50, "y": 100, "w": 200}

# Ejecutamos el código utilizando los diccionarios de variables
# globales y locales
code = """
print(x + y + z + w)  # Usa las variables globales x, y y z y la variable
local w
"""
exec(code, globals_dict, locals_dict)  # Imprime: 280

* exec(code, globals(), clsdict):el código se ejecuta en el contexto de los
espacios de nombres proporcionados y puede acceder a las variables y funciones
definidas en esos espacios de nombres. Cualquier cosa que se asigne o defina
en el código se agrega al espacio de nombres local (clsdict) y puede
ser accedida desde allí.

Aclaraciones de setattr:

* setattr(self, '__set__', clsdict['__set__'])
* setattr(objeto, nombre_atributo, valor): La función setattr es una función
incorporada de Python que permite asignar un valor a un atributo de un objeto.

En este caso, setattr se está usando para asignar el método __set__ generado
dinámicamente al objeto self. self es la clase de descriptor que se está
creando, y __set__ es el nombre del atributo que se va a asignar.
El valor del atributo es el método __set__ obtenido del diccionario de
atributos y métodos de la clase (clsdict).

En resumen, la línea de código setattr(self, '__set__', clsdict['__set__'])
se utiliza para asignar el método __set__ generado dinámicamente a la clase de
descriptor que se está creando.

* raise TypeError('Define set_code(), not __set__()'):Si la clase de
descriptor que se está creando tiene un método __set__ definido, se lanza una
excepción TypeError indicando que se debe definir el método set_code,
no __set__.
'''


class DescriptorMeta(type):
    def __init__(self, clsname, bases, clsdict):
        if '__set__' not in clsdict:
            code = _make_setter(self)
            exec(code, globals(), clsdict)
            setattr(self, '__set__', clsdict['__set__'])

        else:
            raise TypeError('Define set_code(), not __set__()')


'''
Clase Descriptor:
La clase Descriptor es una clase base para crear diferentes tipos de
descriptores. Un descriptor es un tipo especial de objeto que se
puede usar en una clase para proporcionar cierta funcionalidad cuando
se accede a sus atributos.

La clase Descriptor tiene un método llamado set_code que se espera que sea
implementado por cualquier clase que herede de Descriptor. El método set_code
debe devolver una lista de cadenas de código que se ejecutarán cuando se llame
al método __set__ del descriptor.
'''


class Descriptor(metaclass=DescriptorMeta):
    def __init__(self, name=None):
        self.name = name

    @staticmethod
    def set_code():
        return [
            'instance.__dict__[self.name] = value'
            ]

    def __delete__(self, instance):
        raise AttributeError("Can't delete")


'''
Descripción de la clase Typed:
La clase Typed es un descriptor que se utiliza para verificar si un atributo
se establece con un valor del tipo correcto. La clase Typed tiene un atributo
ty que se establece en object por defecto, pero se puede cambiar para
especificar el tipo esperado. La clase Typed implementa el método set_code
para verificar si el valor asignado es del tipo correcto y lanzar una
excepción si no es así.

En este punto Es importante comprender a fondo los conceptos de herencia
, ya que esto da forma a Typed asi:
class Typed(Descriptor):
    ty = object
    def __init__(self, name=None):
            self.name = name

        def __set__(self, instance, value) -> None:
            if not isinstance(value, self.ty):
                raise TypeError("Expected %s" % self.ty)
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            raise AttributeError("Can't delete")

        @staticmethod
        def set_code():
            return [
                'if not isinstance(value, self.ty):',
                '    raise TypeError("Expected %s" % self.ty)'
                ]
'''


class Typed(Descriptor):
    ty = object

    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.ty):',
            '    raise TypeError("Expected %s" % self.ty)'
            ]


'''
Para evitar las dudas, hasta este punto vale la pena aclarar 2 cosas:

1.  solo se han creado clases Descriptoras y funciones auxiliares
para que estas funcionen
2.  no se han creado clases que implementando estos descriptores,
estas clases las creamos nosotros.

Descripción de las clases
Float
String
Integer

Estas clases simplemente especifican un atributo de clase, que será clave para
validar si la el atributo de la instancia  de la clase que implementa
cualquiera de estos descriptores es del tipo especificado por el descriptor

Por herencia, estas clases quedan de la siguiente manera:
class Float(Typed):
    ty = float

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value) -> None:
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s" % self.ty)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete")

# para usar hasta el momento estos descriptores se hance lo siguiente:

class MyClass():
    entero =Integer('entero')

tipo = MyClass()
tipo.entero = 2
print(tipo.__dict__) # {'entero': 2}

'''


# Tipos Especializados
class Float(Typed):
    ty = float


class String(Typed):
    ty = str


class Integer(Typed):
    ty = int


# Value checking
class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '    raise ValueError("Expected >= 0")',
            ]
        # esta linea, a mi parecer no tiene ningún efecto
        # ya que se llama luego del return
        # super().__set__(instance, value)


'''
las clases PosInteger y PosFloat según su herencia se verían asi:
class PosInteger(Integer, Positive):
    ty = Integer

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value) -> None:
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s" % self.ty)
        if value < 0:
            raise ValueError("Expected >= 0")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete")
'''


# More specialized types
class PosInteger(Integer, Positive):
    pass


class PosFloat(Float, Positive):
    pass


'''
class Sized(Descriptor): esta clase tiene algo distinto a las demás y es
que tiene un __init__, en el cual se le pasan varios argumentos,
cuyo orden IMPORTA:

def __init__(self, *args, maxlen, **kwargs):
    self: el de siempre
    * por que *args, maxlen y no maxlen, *args: esto tiene que ver por
    la linea `super().__init__(*args,**kwargs), la clase Descriptor  a
    la que hace referencia este `super`, recibe como primer parámetro
    opcional un string o nada, y poner maxlen que es una palabra clave
    ocasiona problemas.

la forma de implementar la clase Sized:

class MyClass():
    imple_descript = Sized('imple_descript',maxlen=4)

obj = MyClass()
obj.imple_descript ='arba'
print(obj.__dict__)
'''


# Length checking
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if len(value) > self.maxlen:',
            '    raise ValueError("Too big")',
            ]


# Se arma la estructura de una Descriptor de un string de un tamaño especifico
class SizedString(String, Sized):
    pass


'''
Descripción de la clase Regex:

esta clase Crea la Interfaz de un Descriptor al cual que se utiliza para
validar que una cadena de texto cumpla con una expresión regular dada.

* self.pat = re.compile(pat):
*re.compile(pattern, flags=0): Compila un patrón de expresión regular en un
objeto de expresión regular, que puede ser usado para las coincidencias usando
match(), search().

la función match se utiliza para buscar un patrón al PRINCIPIO de una cadena de
texto. Si el patrón se encuentra, devuelve un objeto de coincidencia que
contiene información sobre la coincidencia. Si el patrón no se encuentra,
devuelve None
'''


# Pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if not self.pat.match(value):',
            '    raise ValueError("Invalid string")',
            ]


class SizedRegexString(SizedString, Regex):
    pass


'''
class StructMeta(type):se utiliza para crear clases de estructuras de datos.
modifica todas las clases cuyo padre implementa esta metaclase (StructMeta)
Así:



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
    tienen injerencia sobre las lineas de código que siguen, estas
    implicaciones   son:

    2.1.1 Su estructura según el tipo de descriptor que implemente es mas
    o menos asi:

    ty = Integer

    def __init__(self, name=None):
        self.name = name --> este name se usará mas adelante

    def __set__(self, instance, value) -> None:
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s" % self.ty)
        if value < 0:
            raise ValueError("Expected >= 0")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete")

* Analicemos la siguiente Linea:

for name in fields:
        clsdict[name].name = name

por casa un ode los objetos descriptores guardados en fields
acceda a su atributo name y asignale el su propio nombre. muy confuso no:
obj = Descriptor("aquí debe ir un parámetro que es el nombre del obj,
pero es OPCIONAL)

* El echo de ser opcional da paso aplicar el for anterior.
que traduciéndolo seria:

obj = Descriptor("obj") -- clsdict[name].name = name

El for anterior lo dejaríamos asi:

map(lambda x: setattr(clsdict[x], 'name', x), fields)

* exec(_make_init(fields), globals(), clsdict): incrusta el método __init__ con
los fields antes descritos, y lo guarda en el clsdict. con esto
cada clase cuyo padre implemente la metaclase StructMeta, y cuyos atributos de
clase sean instancias de un Descriptor y se tengan en mente usar como parte del
método __init__:

* StructMeta se encargará de agregar estos "atributos de clase" a su __init__
* y como heredan de un Descriptor, se aplicarán las validaciones especificas
  de cada descriptor ademas de estructurar toda su lógica descriptora de
  forma dinámica

Importante: en este contexto

* map(lambda x: setattr(clsdict[x], 'name', x), fields)
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
'''


# Structure definition code
class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):

        fields = list(
            map(
                lambda key: key[0],
                filter(lambda key_val: isinstance(key_val[1], Descriptor),
                       clsdict.items())))

        list(map(lambda x: setattr(clsdict[x], 'name', x), fields))

        if fields:
            exec(_make_init(fields), globals(), clsdict)

        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))
        setattr(clsobj, '_fields', fields)
        return clsobj


class Structure(metaclass=StructMeta):
    pass


if __name__ == '__main__':
    '''
    Pondremos en uso todo lo anterior
    Supongamos que vamos a crear una clase, nos piden que los valores de
    inicializaion de sus objetos, lo que normalmente va dentro de su
    __init__ tengan cierta validaciones
    como por ejemplo:
    * nombre: no sea mas largo de 8 caracteres y cumpla con un patron
    especifico
    * edad: sea un entero positivo
    * sueldo: sea un flotante positivo

    Como ya implementamos nuestras metaclases pues no tenemos que hacer:
    class Persona():
        def __init__ (self, name, edad, sueldo):
            self.name = name
            self.edad = edad
            self.sueldo = sueldo
        # implementar las validaciones ?
    En vez de esto implementamos la clase Stock como se muestra a continuación.    
    '''
    class Persona(Structure):
        nombre = SizedRegexString(maxlen=8, pat='[A-Z]+$')
        edad = PosInteger()
        sueldo = PosFloat()

    arbarr = Persona('ARBARR', 34, 15.200)
    print(arbarr.__dict__)
    print(arbarr.edad)
