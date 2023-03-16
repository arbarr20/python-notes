# Archivo: descriptor_metaclass.py
# Autor: Arbarr20 y ayuda online
# Fecha: 15/01/2023
# Descripción: Decoradores y metaclases
# crear un mecanismo de importación personalizado y Dinámico
# para que desde una estructura XML se cree un script python
#
'''

Nota importante: 
- Estos tipos de script donde se usan metaclases mas lento metaclases, generación dinámica
  de código para ahorrar código Son mas lentos que hacerlo de forma Normal
- Aunque sean mas lentos, creo que Ahorran espació en disco, pesan menos ya que se repite menos
  código
  
Lo nuevo de este script, ya que lo viejo se describe en
https://github.com/arbarr20/python-notes/blob/poo2/poo2/poo2-files/scripts_descriptores/descriptor_metaclass.py

Entonces de que se trata:
Este script define un mecanismo para cargar clases desde archivos XML, y luego
crear instancias de estas clases. La clase StructImporter es un importador de
meta path que busca archivos XML en la ruta de búsqueda especificada y
devuelve un objeto StructXMLLoader que luego puede cargar el módulo.
'''
# from inspect import Parameter, Signature
import re
from collections import OrderedDict
from xml.etree.ElementTree import parse
import os
import importlib.util
import sys


# Utility functions
def _make_init(fields):
    '''
    Give a list of field names, make an __init__ method
    '''
    code = 'def __init__(self, %s):\n' % \
        ','.join(fields)

    for name in fields:
        code += '    self.%s = %s\n' % (name, name)
    return code


def _make_setter(dcls):
    code = 'def __set__(self, instance, value):\n'
    for d in dcls.__mro__:
        if 'set_code' in d.__dict__:
            for line in d.set_code():
                code += '    ' + line + '\n'
    return code


class DescriptorMeta(type):
    def __init__(self, clsname, bases, clsdict):
        if '__set__' not in clsdict:
            code = _make_setter(self)
            exec(code, globals(), clsdict)
            setattr(self, '__set__', clsdict['__set__'])
        else:
            raise TypeError('Define set_code(), not __set__()')


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


class Typed(Descriptor):
    ty = object

    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.ty):',
            '    raise TypeError("Expected %s" % self.ty)'
            ]


# Specialized types
class Integer(Typed):
    ty = int


class Float(Typed):
    ty = float


class String(Typed):
    ty = str


# Value checking
class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '    raise ValueError("Expected >= 0")',
            ]
        # super().__set__(instance, value)


# More specialized types
class PosInteger(Integer, Positive):
    pass


class PosFloat(Float, Positive):
    pass


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


class SizedString(String, Sized):
    pass


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


# Structure definition code

class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):
        fields = [key for key, val in clsdict.items()
                  if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name

        # Make the init function
        if fields:
            exec(_make_init(fields), globals(), clsdict)

        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))
        setattr(clsobj, '_fields', fields)
        return clsobj


class Structure(metaclass=StructMeta):
    pass


'''
es una función que genera código Python a partir de un archivo XML específico
* def _xml_to_code(filename):
    filename:que es el nombre del archivo XML del cual se generará el código

* doc = parse(filename): Utiliza la función parse() del módulo
    xml.etree.ElementTree para analizar el archivo xml dado y obtener
    un objeto ElementTree,
* code = 'import dinamic_code_importer as _i\n': es simplemente una variable
  con una cadena de texto que mas adelante hace parte de un  exec. es como si
  se iniciara a crear un fichero de python dinámico y se importara este mismo
  programa el que estamos comentando ahora mismo.

* for st in doc.findall('structure'): encuentra todas la etiquetas structure
 del xml parseado (doc) el xml sin parsear se ve asi:
    -  `<structure name="Stock">`
  de este modo `st` tomaría valores como
    - st:<Element 'structure' at 0x10afdcef0>

* code += _xml_struct_code(st): a la variable code se le concatena el resultado
  de _xml_struct_code(st) (ver la descripción de esta función)

*return code: finalmente se retorna la variable code con una estructura de
 código asi:

import dinamic_code_importer as _i
class Stock(_i.Structure):
    name = _i.SizedRegexString(maxlen=8, pat='[A-Z]+$')
    shares = _i.PosInteger()
    price = _i.PosFloat()
class Point(_i.Structure):
    x = _i.Integer()
    y = _i.Integer()
class Address(_i.Structure):
    hostname = _i.String()
    port = _i.Integer()
'''


# Aquí Inicia lo Nuevo
# Import hooks
def _xml_to_code(filename):
    doc = parse(filename)
    code = 'import dinamic_code_importer as _i\n'
    for st in doc.findall('structure'):
        code += _xml_struct_code(st)
    return code


'''
* stname = st.get('name'): obtengame el valor del atributo name de cada
  etiqueta `structure` parseada `st`
    - <structure name="Stock">
    - st:<Element 'structure' at 0x10afdcef0>
    - stname = Stock

* code = 'class %s(_i.Structure):\n' % stname: se asigna a la variable code
  un string, que dará como resultado algo como:
    - class Stock(_i.Structure):

* for field in st.findall('field'): Encuentra todas las etiquetas field que
  estén dentro de un st. el xml esta algo asi:
     <structure name="Stock">
       <field type="SizedRegexString" maxlen="8" pat="'[A-Z]+$'">name</field>
    st = todas las structure
    field = son todas las etiquetas fields dentro de estas structure

* name = field.text.strip():
  - text hace referencia al texto que hay dentro de una etiqueta xml asi:
     - <field type="PosInteger">shares</field>
  - text = shares
  - strip() es un método de python para eliminar espacios en blanco al inicio
    y al final de una cadena de texto.
  - name: tomo el texto de la etiqueta en cuestión y le quita los espacios
   en blanco
* dtype = '_i.' + field.get('type'): es una cadena de texto "_i," a la cual
  se le   concatena el valor obtenido por el atributo type de la etiqueta
  guardada en  la variable field asi:

    - <field type="SizedRegexString" maxlen="8" pat="'[A-Z]+$'">name</field>
    - field:field:<Element 'field' at 0x108471170>
    - name = name
    - dtype:_i.SizedRegexString

* kwargs = ', '.join('%s=%s' % (key, val)
   for key, val in field.items() if key != 'type'): vamos por partes:

    el xml tiene la siguiente forma:
      - <field type="SizedRegexString" maxlen="8" pat="'[A-Z]+$'">name</field>

* field.items() = [('type', 'SizedRegexString'), ('maxlen', '8'),
  ('pat', "'[A-Z]+$'")]

* Los valores de key y val para cada iteración del for:
  - key: 'type'
  - val: 'SizedRegexString'
    - key: 'maxlen'
    - val: '8'

* retorne un GENERADOR DE TUPLAS ASI ('%s=%s' % (key, val) DE ('maxlen', '8')
con una condición:
  - if key != 'type'
  - El resultado seria (['maxlen=8',pat='[A-Z]+$])

* ahora entra en acción el `', '.join('%s=%s' % (key, val)`:
  - esto convierte el ultimo resultado a un único string separado por comas.
  el join se consume el  generador
    - kwargs: "maxlen=8, pat='[A-Z]+$'"

* Podemos reemplazar esa linea de código por :
 - kwargs = ', '.join(f'{key}={val}' for key, val in field.items()
  if key != 'type')
 Sería algo mas legible

* code += '    %s = %s(%s)\n' % (name, dtype, kwargs): se le concatena a la
  variable code el resultado de las variables hay un espacio que no se debe
  omitir :code += '    %s
    - name = name
    - dtype:_i.SizedRegexString
    - kwargs: "maxlen=8, pat='[A-Z]+$'"

  Quedando asi después de terminar la iteración `st.findall('field')`:
    - el XML:
    <structure name="Stock">
        <field type="SizedRegexString" maxlen="8" pat="'[A-Z]+$'">name</field>
        <field type="PosInteger">shares</field>
        <field type="PosFloat">price</field>
    </structure>

    - El python generado:
    code :
    class Stock(_i.Structure):
        name = _i.SizedRegexString(maxlen=8, pat='[A-Z]+$')
        shares = _i.PosInteger()
        price = _i.PosFloat()
* return code: se retorna el code a la función `_xml_to_code`
'''


def _xml_struct_code(st):
    stname = st.get('name')
    code = 'class %s(_i.Structure):\n' % stname
    for field in st.findall('field'):
        name = field.text.strip()
        dtype = '_i.' + field.get('type')
        kwargs = ', '.join(
            f'{key}={val}' for key, val in field.items() if key != 'type')
        code += '    %s = %s(%s)\n' % (name, dtype, kwargs)
    return code


'''
class StructImporter: La clase StructImporter es el objeto que implementa la
interfaz de cargador de módulos, y su método find_module se utiliza para
determinar si un módulo especificado puede ser importado a partir de un
archivo XML específico y su método load_module se utiliza para cargar y
configurar el módulo.
Esta clase genera un objeto buscador que es agregado  por la función
`install_importer` al `meta_path`, y se ejecuta cuando:
  1. se encuentra una sentencia de importación en este caso import data
  2. Cuando por medio de otra biblioteca como importlib.util. se obliga a
        crear ejecutar de nuevo Buscador1, este crea un nuevo CARGADOR2 con un
        __loader2__,  Tener mucho cuidado por que este cambio de contexto puede
        causar problemas HA QUE TENER MUY CLARO QUE  BUSCADOR Y __LOADER__
        SE VA A UTILIZAR, el segundo cargador se crea en la linea:

          -mod = importlib.util.module_from_spec(importlib.util.find_spec
            (fullname))
  3. cuando no se encuentra el data en el sys.path

* self._path = path: Donde path es `sys.path`
* def find_module(self, fullname, path=None): Este método se ejecuta
  automáticamente su argumentos son:
    - self: objeto
    - fullname: es el nombre del modulo que se esta importando
    - path: en este caso es None
* name = fullname.rpartition('.')[-1]:
  - El método rpartition() es similar al método partition(), pero en lugar de
  buscar el separador desde el principio de la cadena, lo busca desde el final
  de la cadena. `str.rpartition(separator)`
  - Donde separator es la cadena que se utiliza como separador.
  Si el separador no se encuentra en la cadena, el método devuelve una tupla
  con `('', '', 'str')` que es lo que pasa en este caso, pero como se usa [-1]
  solo se muestra el `str`.
  - name = data.rpartition('.')[-1] = data

* path = self._path = path obtiene el valor de sys.path

Antes de continuar aclarar lo que es os.path:es un módulo que nos ayuda a
trabajar con rutas de archivos y directorios en nuestro sistema operativo

* for dn in path: filename = os.path.join(dn, name+'.xml'): se itera sobre
  cada una de las rutas de path y se le asigna a la variable filename lo
  siguiente:

  - os.path.join(dn, name+'.xml') =  unir cada una de las rutas por defecto
    de sys.path con name, a la cual se le concatena el .xml

    -  filename = la/ruta/del/sys.path/data.xml

* os.path.exists(filename): si el el fichero en la ruta anterior existe
* return StructXMLLoader(filename): retorna un objeto StructXmLLoader(filename)
'''


class StructImporter:
    def __init__(self, path):
        self._path = path

    def find_module(self, fullname, path=None):
        name = fullname.rpartition('.')[-1]
        if path is None:
            path = self._path
        for dn in path:
            filename = os.path.join(dn, name+'.xml')
            if os.path.exists(filename):
                return StructXMLLoader(filename)
        return None


'''
* self._filename = filename: ruta/data.xml
* importlib.util:proporciona funciones útiles para trabajar con módulos, dentro
  de sus funciones mas comunes esta:

  -  importlib.util.find_spec(name): Esta función busca un módulo específico
   al cual se le pasa el nombre del modulo y devuelve un objeto de
   especificación de módulo. Este objeto contiene información sobre el módulo,
   como su ruta, si está disponible y si  es un paquete.

     - Pero donde busca: Pues en el Objeto Buscador1, lo que implica que
     EJECUTA a Buscador1, y por ende crea un nuevo CARGADOR2 __loader__2

  - La función importlib.util.module_from_spec(): es una función del módulo
    importlib.util que se utiliza para crear un objeto de módulo a partir de un
    objeto de especificación de módulo. El objeto de módulo creado no está
    insertado en el espacio de nombres global, por lo que todavía es necesario
    usar sys.modules para insertarlo en el espacio de nombres global. el valor
    que retorna es un objeto como este:
     - la variable mod quedaría:
        -<module 'data' (<__main__.StructXMLLoader object at 0x105933a60>)>
     - MOD: Aquí tiene un atributo __loader2__ =  ..a60, pero mas adelante
       cambia a:
         -  mod.__loader__ = self = ...0x100f478e0 = __LOADER1__

* sys.modules.setdefault(fullname, mod): Inserte en el espacio de nombres
  global el modulo (mod) con el nombre "fullname"  y si ya existe en el
  espacio de nombres global no lo  sobre escribas.
  Es importante tener en cuenta que en general se recomienda usar la sintaxis
  import para importar los módulos y no utilizar esta forma ya que puede
  ocurrir conflictos o problemas de rendimiento.ejemplo:

    import math

    # Insertar una versión diferente del módulo math en el espacio de nombres
      global
    sys.modules.setdefault('math', my_math_module)

    # Usar el módulo math
    print(math.sqrt(4))
    En este ejemplo, se esta insertando el módulo my_math_module en el espacio
    de nombres global con el nombre math, pero al mismo tiempo se ha importado
    el módulo math de la biblioteca estándar y se esta sobrescribiendo el
    anterior.    Esto puede causar problemas ya que el código puede estar
    esperando la funcionalidad del módulo math de la biblioteca estándar y no
    la del módulo  my_math_module, causando errores en tiempo de ejecución.

* mod.__file__ = self._filename: En el caso del código que me proporcionaste,
  self._filename es una variable de instancia de la clase StructXMLLoader que
  se establece en el constructor y contiene la ruta del archivo XML que se
  está cargando. Al establecer mod.__file__ = self._filename, se está
  indicando al sistema de carga de módulos de Python, que el código del módulo
  se encuentra en el archivo XML especificado.

* mod.__loader__ = self:especifica la instancia del objeto que cargó el módulo.
 Esto permite al sistema tener una traza de quien fue el cargador del módulo y
 poder tomar decisiones en consecuencia.esta línea es especialmente importante
 porque se está cargando el módulo de forma dinámica, y no mediante el sistema
 de carga de módulos estándar de Python. Al indicar que la instancia de
 StructXMLLoader es el cargador del módulo, se está dando al sistema de carga
 de módulos de Python una forma de identificar y controlar ese módulo cargado
 de forma dinámica.
 El cargador a usar el el __loader1__

* code = _xml_to_code(self._filename): está llamando a una función auxiliar
  llamada _xml_to_code(), que se encarga de convertir el contenido de un
  archivo XML(que se encuentra en la ruta self._filename) especificado en una
  cadena de código Python.
  Esta función es la encargada de leer  y convertir el contenido del mismo en
  una cadena de código Python válida. Esa cadena de código se asigna a la
  variable code.Code tiene la siguiente estructura:

    import dinamic_code_importer as _i
    class Stock(_i.Structure):
        name = _i.SizedRegexString(maxlen=8, pat='[A-Z]+$')
        shares = _i.PosInteger()
        price = _i.PosFloat()
    class Point(_i.Structure):
        x = _i.Integer()
        y = _i.Integer()
    class Address(_i.Structure):
        hostname = _i.String()
        port = _i.Integer()

  En este caso, el código generado por la función _xml_to_code() se ejecutará
  en un contexto donde el módulo mod ya ha sido creado y está listo para ser
  rellenado con el código leído del archivo xml, esto se realiza en la
  siguiente linea:
    - exec(code, mod.__dict__, mod.__dict__)

* exec(code, mod.__dict__, mod.__dict__):La función exec acepta tres argumento
  : el primer argumento es la cadena de código Python que se desea ejecutar, el
  segundo argumento es el diccionario de nombres en el que se deben definir las
  variables y funciones del código ejecutado, y el tercer argumento es el
  diccionario de nombres en el que se deben buscar las variables y funciones
  del código ejecutado.
  En este caso, se está pasando mod.__dict__ como el segundo y tercer argumento
  para exec(), lo que significa que las variables y funciones definidas en el
  código code se agregarán al diccionario de nombres del módulo mod, y las
  variables y funciones utilizadas en el código code serán buscadas en el
  diccionario de nombres del módulo mod.

  En resumen, esta linea ejecuta el código contenido en la variable code en el
  contexto del módulo mod, es decir, agregando las variables y funciones
  definidas en el código a la estructura del módulo.

* return(mod):Retornando el objeto mod permite que el sistema de módulos de
  Python lo utilice como si hubiera sido importado de manera tradicional, y
  permite que otros módulos puedan acceder a las variables y funciones
  definidas dentro del archivo xml que se esta cargando.

'''


class StructXMLLoader:
    def __init__(self, filename):
        self._filename = filename

    def load_module(self, fullname):
        mod = importlib.util.module_from_spec(importlib.util.find_spec(fullname))
        sys.modules.setdefault(fullname, mod)
        mod.__file__ = self._filename
        mod.__loader__ = self
        code = _xml_to_code(self._filename)
        exec(code, mod.__dict__, mod.__dict__)


'''
* sys.path: es una variable global en Python que contiene una lista de rutas
  de directorios. Estas rutas se utilizan para buscar los módulos y paquetes
  que se importan en un script. El intérprete de Python busca en estas rutas en
  orden, de principio a fin, hasta encontrar el módulo o paquete especificado.

  La primera ruta en sys.path es el directorio actual (.), seguida de la lista
  de rutas que están especificadas en la variable de entorno PYTHONPATH, y
  luego las rutas predeterminadas que vienen con Python.

* sys.meta_path: es una lista de objetos de "buscadores de módulos" que Python
  utiliza para buscar módulos importados, Es importante notar que para
  importar un modulo, python buscara en la lista de
  sys.path, y si no lo encuentra, utilizara los buscadores de sys.meta_path
  para buscar el modulo, estos buscadores se pueden crear como es nuestro
  en la linea `sys.meta_path.append(StructImporter(path))`, o hay unos que ya
  vienen por defecto con python

  Ademas de Buscadores, Hay CARGADORES, un Buscador1 (find_module de la clase
  StructImporter) en este contexto, CREA UN CARGADOR1 por medio de
  (load_module de la clase StructXMLLoader) con un __loader1__ especifico

    - un buscador crea un cargador
    - un buscador se ejecuta cuando:
      1. se encuentra una sentencia de importación en este caso import data
      2. Cuando por medio de otra biblioteca como importlib.util. se obliga a
        crear ejecutar de nuevo Buscador1, este crea un nuevo CARGADOR2 con un
        __loader2__,  Tener mucho cuidado por que este cambio de contexto puede
        causar problemas HA QUE TENER MUY CLARO QUE  BUSCADOR Y __LOADER__
        SE VA A UTILIZAR, el segundo cargador se crea en la linea:

          -mod = importlib.util.module_from_spec(importlib.util.find_spec
            (fullname))
      3. cuando no se encuentra el data en el sys.path
    - Un cargador  carga el modulo a nuestro programa para utilizarlo,es
      utilizado por el sistema de carga de módulos de Python para poder
      identificar y controlar cómo se cargaron los módulos en un programa.
      Por ejemplo, el sistema de carga de módulos de Python puede usar el
      atributo __loader__ para controlar la recarga de módulos o para
      verificar si un módulo se cargó de forma segura.


* install_importer(): no es una función inventada, es una función del módulo
  importlib.util en Python que permite agregar un nuevo mecanismo de
  importación   al sistema de módulos de Python. Esto significa que permite
  importar módulos   de una manera diferente a la manera tradicional,
  utilizando un objeto que   implemente una interfaz específica
  (conocida como un "cargador de módulos").

  La función install_importer toma un argumento, que es un objeto que
  implemente la interfaz de cargador de módulos. La interfaz de cargador de
  módulos consta de dos métodos: find_module y load_module. El método
  find_module se utiliza para determinar si un módulo especificado puede ser
  importado por el cargador de módulos, y el método load_module se utiliza
  para cargar y configurar el módulo.
  Una vez que se ha instalado un cargador de módulos mediante la función
  install_importer, el sistema de módulos de Python lo utilizará para intentar
  importar módulos. Si el cargador de módulos es capaz de importar el módulo
  especificado (es decir, si su método find_module devuelve un objeto no nulo),
  el sistema de módulos utilizará el método load_module del cargador para
  cargar y configurar el módulo.

  La clase StructImporter es instalada en el sistema de módulos de Python
  mediante una llamada a install_importer(StructImporter(sys.path)), esto hace
  que cualquier intento de importar un módulo a través del sistema de módulos
  de Python, use StructImporter para buscar el módulo en un archivo xml
  específico y cargarlo.

  El script utiliza estas clases y funciones para permitir la importación de
  módulos a partir de archivos XML específicos, en lugar de utilizar la forma
  tradicional de importar módulos a través de archivos Python.

Teniendo en cuenta lo anterior podemos iniciar con
install_importer(path=sys.path):
  - path=sys.path: ya lo explicamos
  - sys.meta_path.append(StructImporter(path)):
   se agrega al meta_path el objeto buscador StructImporter(path)
     - meta_path [<__main__.StructImporter object at 0x10d22e7d0>]]
'''


def install_importer(path=sys.path):
    sys.meta_path.append(StructImporter(path))


if __name__ == '__main__':
    '''
    * install_importer(): inicia el mecanismo de importación al sistema de
    módulos de Python de forma NO tradicional, en este caso de forma dinámica

    * import data: ejecuta toda la estructura de inicializaion realizada
    por install_importer, ademas de otras cosa, en resumen este es el
    detonador para que se realicen las siguientes operaciones:

     - Importa de forma dinámica a data.py (magia invisible, no se ve),
      también sirve como palabra clave para buscar el fichero data.xml
    -  En este proceso de importación, ademas de la importación se realizan
      otras tareas:
        - Se busca el fichero data con extension  xml
        - Se lee la estructura de este `.xml` para generar un script en python
          de forma dinámica, para pasar de algo como:

        <structure name="Stock">
            <field type="SizedRegexString" maxlen="8" pat="'[A-Z]+$'">name</field>
            <field type="PosInteger">shares</field>
            <field type="PosFloat">price</field>
        </structure>

        A algo como esto en python:
        Nombre del fichero: data.py (este nombre es magia, ya que no esta)
        en el árbol de directorios, solo se crea de forma dinámica, invisible
        esto permite usar `s = data.Stock('GOOG', 100, 490.1)`

        import dinamic_code_importer as _i
        class Stock(_i.Structure):
            name = _i.SizedRegexString(maxlen=8, pat='[A-Z]+$')
            shares = _i.PosInteger()
            price = _i.PosFloat()
        Como puede ver, la estructura del xml esta estructurada de tal forma
        que al pasarlo a código python se usen las interfaces de las metaclases
        descriptores, es por esto también que se importa el
        import dinamic_code_importer as _i de forma dinámica

    En las siguientes lineas se crean objetos del código generado dinámicamente

    * s = data.Stock('GOOG', 100, 490.1)
    * p = data.Point(2,3)
    * h = data.Address('www.python.org', 80)
    '''

    install_importer()
    import data    
    s = data.Stock('ARBARR', 28, 1.500)
    p = data.Point(2, 3)
    h = data.Address('www.arbarr.io', 80)
    print(f'''
    Nombre: {s.nombre}
    Edad: {s.edad}
    Salario: {s.salario}\n''')
    print(f"Point: ({p.x},{p.y})")
    print(f"Web: {h.hostname}:{h.port}")
