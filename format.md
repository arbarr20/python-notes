# Tipos y estructuras de datos

## Variables en python

Es un espacio de memoria que se reserva en la computadora para guardar un dato, y cuyos valores pueden ser cambiados durante la ejecución del programa.Para identificar mas facilmente estos espacios de memoria se le asignan **Etiquetas** `variables`.

las variables en python pueden ser:

- **Mutables**: Su contenido puede cambiarse
- **Inmutables** : Su contenido No puede cambiarse

Hay reglas para definir los nombres de las variables en python

Buenas:

- spam
- eggs
- spam23
- \_speed

Malas:

- 23spam
- #eggs
- spam.23
- \_speed

Son Sensible a Mayusculas, Las siguientes etiquetas son distintas:

- spam
- Spam
- SPAM

> No se puede dar nombre a una variables que sea una palabra reservada del lenguaje

Alguno de los tipos de datos estándar en python son los que se relacionan en la siguiente imagen:

![tipos de datos](https://github.com/arbarr/aprendiendo_python/blob/master/tipos_datos.png)

> tomado de:_readthedocs.io_
> Para saber el tipo de dato de una variable solo basta con escribir `type(nombre_variable)`

### Alcance se las variables

por defecto las variables en python son locales, esto quiere decir que si declaramos una variable dentro de una función esta solo estará definida dentro de la función, y no interfiere con otra variable fuera del código. por lo tanto las variables que son declaradas fuera de una función, no son accesibles dentro la misma (función).
en los casos estrictamente necesarios por el programador una variable local puede convertirse en global, declarándola con la sentencia `global`

**_Ejemplo_**

```python
variable = "esta es una variable"
def modidicavar():
    var3 = "esta no es una variable global"
    global variable
    variable = " esta es la variable modificada a global"
print (variable)
modidicavar()
print (variable) # esto arrojara un error Tipo NameError print (var3)
```

Cuando los nombres de variables inician con guiones bajos, estas variables deben reservarse para para (variables especiales)
`__variable_especial__`

```python
x = 12.2
y = 34
x = 23 #se sobrescribe el valor de x
```

> x es la etiqueta  
> 12.2 es el valor del dato

Tambien se pueden asignar multiples valores a multiples variables en una linea de código

```python
numero, caracter, string, flotante = 12,"c","esto es una cadena de texto", 12.34
```

### Constantes

las constantes son por lo general valores que no cambian, en python, las constantes son declaradas en un modulo, **Un modulo** es un fichero `.py` distinto al fichero principal de nuestro proyecto. algo importante de las constantes, es que por convención se escriben en MAYUSCULAS.

**_Ejemplo_**

```python
IP_DB_SERVER = "127.0.0.1"
PORT_DB_SERVER = 3307
USER_DB_SERVER = "root"
PASSWORD_DB_SERVER = "123456"
DB_NAME = "clientes"
```

### Palabras Reservadas

Aquellas que son **Exclusivamente** utilizadas por Pyhon

> Algunas de ellas son:

| alse   | class | return | is     | finally  |
| ------ | ----- | ------ | ------ | -------- |
| none   | if    | for    | lambda | continue |
| true   | def   | from   | while  | nonlocal |
| and    | del   | global | not    | with     |
| as     | elif  | try    | or     | yield    |
| assert | else  | import | pass   | break    |
| except | in    | raise  |        |          |

### Operadores

| Nombre                |  Simbolo  | Significado (todo se almacena en el lado izquierdo del operador) |
| :-------------------- | :-------: | ---------------------------------------------------------------: |
| Asignacion            |     =     |                                              aqui (=guarda) esto |
| mas igual             |    +=     |                                       le_suma_aqui += lo_de_aqui |
| menos igual           |    -=     |                                    le_resta_aqui (-=) lo_de_aqui |
| por igual             |    \*=    |                            le_multiplica_a_esto (\*=) lo_de_aqui |
| divide igual          |    /=     |                                          esto_dividido (/=) esto |
| potencia igual        |   \*\*=   |                                    esto_lo eleva_a (\*\*=0) esto |
| divicion entera igual |    //=    |                     resultado_entero_de esto (//= dividido_esto) |
| modulo igual          |    %=     |                             resto_de_esto_dividido (%=) con esto |
| incremento            | +=(valor) |                                        incrementeme (+=) en esto |

#### Operadores Aritméticos

los operadores aritméticos son los mas comunes
suma, resta, multiplicación, modulo, división, división entera, potencia.

#### Operadores Relacionales

- ==
- !=
- <
- >
- <=
- > =

**_Ejemplo_**

```python
cadena = "johan arley"
a = 4
b = 5
c= 5
lista = [2, "jesii" , "johan arley"]
resultado1 = a !=b
resultado2 = cadena == lista[2]
resultado3 = a > b
print (resultado1, resultado2, resultado3
#resultado
>>> True True False
```

### Tipos de datos Numéricos

![tipos_numericos](https://github.com/arbarr/aprendiendo_python/blob/master/tipos_datos.png)

### Tipo de dato numerico Enteros

las variables de tipo numerico son de tipo `int` entero, que en computadoras de 32 bits va desde `-2.147.483.648 a 2.147.483.647.` En plataformas de 64 bits, el rango es de `-9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807.`

los tipos numéricos enteros `Long` permite almacenar números de cualquier precisión, limitado por la memoria disponible en la máquina.
se aconseja que solo se declaren variables numéricas de este tipo solo si es estrictamente necesario, esto con el fin de ahorrar memoria, la declaración de este tipo Long se hace `entero_long = 23L`

> Se puede anteponer un literal para representar el numero en octal `023` o en hexadecimal `0x17`

### Tipo de dato numerico de coma flotante

Python siempre se utiliza doble precisión, y en concreto se sigue el estándar IEEE 754: 1 bit para el signo, 11 para el exponente, y 52 para la mantisa. Esto significa que los valores que puede representar van desde ±2,2250738585072020 x 10-308 hasta ±1,7976931348623157×10308.
Para representar un número real en Python se escribe primero la parte entera, seguido de un punto y por último la parte decimal.

`real = 0.2703`  
También se puede utilizar notación científica, y añadir una e (de exponente) para indicar un exponente en base 10. Por ejemplo:

`real = 0.1e-3`

### Tipo de dato numerico complejo

Estos números son utilizados en matemáticas (especiales) por ingenieros, y otras especialidades, esto numero complejos estan compuestos por una parte real y una parte imaginaria, y en python se declaran de la siguiente forma `complejo = 3 + 4j`
**Convertir datos numericos a otros tipos de datos numericos**

**_Ejemplo_**

```python
a = 4.5
print (complex(a))
#la salida es
>>> (4.5+0j)
```

asi como el ejemplo anterior se hace con los demas tipos de datos numericos

> Nota: se puede utilizar la duncion `help()` para obtener ayuda.

`help(int)` Esto retornara una serie de documentacion de las funciones y operaciones disponibles con `int`

### Tipo de dato `Boleeano`

Loa tipos de datos booleanos pueden ser:

- verdaderos (True)
- falsos (False)
  Los siguientes operaciones son considerados como `False`:

1. False
2. None
3. cadena de caracteres vacía
4. el numero cero (0)
5. diccionarios (vacíos)
6. tuplas vacías
7. lista vacías

`{}` retornara un false, por que es un diccionario vacio
los tipos de dato booleano se pueden convertir a entero `int (false)` arrojara como resultado un `0`, pero al convertir un tipo de dato booleano a un string, `str(False)` efectivamente si retorna un string.

**_Ejemplo_**

```python
booleano = False
convert_boll_to_string = str (booleano)
print (convert_boll_to_string, type (convert_boll_to_string))
boolean = True
convert_boll_to_int = int (boolean)
print (convert_boll_to_int,type(convert_boll_to_int))
# La salida es:
>>> False <class 'str'>
>>> 1 <class 'int'>
```

**Operadores para tipos de datos Booleanos:**

1. and
2. or
3. not

> Para recordar, igual que en el tipo de datos entero, en el tipo de datos booleano se puede usar la ayuda `help(bool)`

### Tipo de dato `string` Cadena de caracteres

los tipo de datos `String` son de tipo **_SECUENCIA_** de caracteres encerrados entre comillas simples o dobles

secuencia de caracteres sencillos, van encerrados entre comillas simples o entre comillas dobles.

secuencias de caracteres largos, se utilizar la triples comillas, esto nos permite escribir string sin preocuparnos del salto de linea.

```python
print ("secuencia de caracteres simples")
print (""" secuencia de caracteres larga
puedo dar un salto de linea y no preocuparme de errores""")
```

la CLASE principal de las cadenas de caracteres es la `basestring`, y esta a su vez es la clase base de las clases

- string (str)
- unicode(U)

la clase str, la usamos a diario, y no sabíamos que la usábamos, cuando escribimos una cadena de caracteres, ya sea las cortas o las largas, estas son un _objeto de tipo str_

```python
cadena_simple = "cadena corta"
cadena_larga = """ esta es una cadena larga,
va dentro de comillas simples o dobles, pero triples no
preocupa escribir con los saltos de linea"""

print (type(cadena_simple), cadena_simple)
print (type(cadena_larga), cadena_larga)
```

la clase unicode, es una clase que me permite informar a python que voy a utilizar una cadena de caracteres unicode, estos caracteres nos permite imprimir símbolos distintos, por lo general de diferentes dialectos.
la forma de hacer esto en python es

```python
cadena_unicode = "\u0180"
print (cadena_unicade)
# imprimira
>>>ƀ
```

> existen muchas mas aplicaciones con la clase unicode, la cual se deben estudiar mas a fondo.

### Prefijos de cadenas

son letras que van antes de una cadena de caracteres y modifican su formato:
Alguno de los prefijos son:

- r/R, cualquiera de estos prefijos en una secuencia de caracteres "inhabilita" los caracteres especiales, por ejemplo `r"\n\thola"` esto imprime `\n\thola` como vemos no "formatea", no ejecuta las caracteres de escape,ni tampoco el salto de linea ni la tabulacion, imprime la cadenadena caracteres de forma _cruda_

- u/U ya lo habíamos visto antes para indicar que se imprimirán tipo de secuencias de caracteres unicode

#### Caracteres de escape

en esta imagen se logra visualizar los caracteres de escape.
![caracteres de escape](https://github.com/arbarr/aprendiendo_python/blob/master/caracteres_de_escape.png)

### Operaciones con `strings`

con los strings se puede:

- sumar (concatenar +)
- Multiplicar (repetir un números de veces una cadena)

### Comentarios

existen comentarios

- Una linea que inician con el #
- Multilinea que van entre """ comillas dobles triples.

### Docs Strings

son comentarios de documentación, estos nos ayudan a comentar o documentar de forma profesional nuestro código, optimizando las herramientas que nos da python para este fin, existen docString para:

- Funciones
- Metodos
- Modulos

todos los objetos en python cuentan con una variable especial `__doc__` la cual nos retorna una descripción de _para que sirve_ y _como se utilizan_ los objetos.

siempre y cuando se estudia programación se nos recomienda comentar nuestro código, y es muy importante hacerlo. en python hacerlo de la siguiente forma nos permite "automatizar" en cierta forma nuestros objetos. y podemos acceder por medio de del metodo `help(objetodocumentado)` o `nombreObjetoDocumentado.__doc__`, esto retornara nuestros comentarios.

para mas claridad unos ejemplos:

**_DocString de funciones_**

```python
def my_funcion ():
    """ esta es una función que imprime una cadena de caracteres"""
    print ("cadena de caracteres")

help(my_funcion)
print (my_funcion.__doc__

# La salida Imprime lo siguiente

>>> Help on function my_funcion in module __main__:

my_funcion()
    esta es una función que imprime una cadena de caracteres

 esta es una función que imprime una cadena de caracteres
```

**DocString en Clases y metodos:**

```python
class MyClase:
    """ Esta es una clase llamada MyClse y solo tine dos atributos"""

    def __init__ (self, nombre = "Sin nombre" , apellido = "Sin apellido"):
        "este es el constructor de la clse MyClase"

        self.nombre = nombre
        self.apellido = apellido

    def my_metodo (self):
        """ esta es un metodo que imprime  el nombre y apellido"""

        cadena = f'hola {self.nombre} su apellido es {self.apellido}'
        print(cadena)

instancia = MyClase("johan", "jimenez")
instancia.my_metodo()
#para imprimir las ayudas o los comentarios se hace de la siguiente forma
help(MyClase)
# o de esta forma, aunque es mas completa la anterior
print(MyClase.__doc__)
```

Tambien se puede acceder especificamente al metodo de una clase de la siguiente forma:
`help(instancia.my_metodo)` o `instancia.my_metodo.__doc__`

**\*DocsStrins de scrips y Modulos**
los scrips y lo modulos son código python en un archivo diferente al que estamos traabajando y cuando necesitamos alguno de estos lo importamos a nuestro proyecto, cuando creamos un modulo es igul de copmveniente comentarlo y documentarlo muy bien. como se explico anterior mente con los docstring de las clases y metodos, con los modulos se hace de una forma igual, como por ejemplo:

```python
#este es un modulo
""" este es un Modulo... esta primera linea es para comentar de que trata el modulo en general, aqui ponemos  para que sirve y como se utiliza"""

def funcion_del_modulo ():
    """docstring de la funcion_del_modulo"""
    print ("esta es una función de un modulo")

def otra_funcion_del_modulo (parametro):
    """doc string de otra_funcion_del_modulo, esta función recibe como parametro un strig y retorna otro estrig"""
    print ("retorno de otro_funcion_del_modulo",parametro)

# aqui estamos en nuestro proyecto

import modulo
# de esta forma accedo a la ayuda general del modulo.
help(modulo)
# si no se quiere tanta información, si no mas bien información mas especifica, como de una función por ejemplo, se hace de la siguiente forma

print (constantes.otra_funcion_del_modulo.__doc__)
help (constantes.otra_funcion_del_modulo)
```

> se pueden listar todas las funciones de un modulo con la función `dir(nombre del modulo, o funcion, o clase)`, esto retorna las funciones propias del modulo que construimos, y ademas otras funciones especiales `(__funcion_especial__)` que incorpora python automaticamente. se pueden acceder a estas funciones especiales asi `modulo.__name__` esto retornara el nombre del modulo.

### Formateo de cadenas

Este tema es muy interezante, ya que cambia un poco la forma como normalmente escribimos el formato de caracteres que mostramos por consola. con el formateo de cadenas podemos adornar de una forma mas interezante la informacion que queremos mostrar.

Algunos tipos de formateo de string en python son:

**% Opereador de interpolacion**
Usted necesitará proveer el % seguido por el tipo que necesita ser formateado o convertido. El operador % entonces substituye la frase ‘%tipodato’ con cero o mas elementos del tipo de datos especificado
Tipos de objetos con el operador de interpolacion:

- %c = str, simple carácter.
- %s = str, cadena de carácter.
- %d = int, enteros.
- %f = float, coma flotante.
- %o = octal.
- %x = hexadecimal.

**_Ejemplo_**

```python
  print ("usted %s, De5sea continuar ? Si O No?: %c "%("joan","s"))
  print ("usted tiene %d manzanas que valen %f pesos"%(5,12.567))
  print ("el numero 10 decimal en hexadecimal es %x, el numero decimal 10 en octal es %o " %(0xA, 10))
  # la salida es la siguiente
  >>>usted joan, Desea continuar ? Si O No?: s
usted tiene 5 manzanas que valen 12.567000 pesos
el numero 10 decimal en hexadecimal es a, el numero decimal 10 en octal es 12
```

**Clase Formatter**
Esta es una clase integrada de `string`. es la encargada de proveer la funcionalidad de hacer substituciones utilizando el metodo `format()`.

El metodo **Format()** regresa una versión nodificada (formateada) de la cadena de caracteres usando substituciones desde argumentos args y kwargs. Las substituciones son identificadas entre llaves { } dentro de la cadena de caracteres (llamados campos de formato), y son sustituidos en el orden con que aparecen como argumentos de format(), contando a partir de cero (argumentos posicionales).

Podemos pensar en esto como una forma mas profesional de mostrar los datos:

```python
nombre = "smith"
edad = 23
estatura = 1.80

print ("El señor {} tiene una edad de {} Años y mide {} metros de altura".format(nombre,edad,estatura))
# La salida del programa es el siguiente:
>>>El señor smith tiene una edad de 23 Años y mide 1.8 metros de altura
```

Tambien podemos cambiar el orden de los argumentos, poniendo indices.

```python
nombre = "smith"
edad = 23
estatura = 1.80

print ("El señor {0} mide {2} metros de altura, tiene una edad de {1} Años ".format(nombre,edad,estatura))
#El señor smith mide 1.8 metros de altura, tiene una edad de 23 Años
```

Podemos complicar un poco mas este forma de mostrar los datos:

- `{:>30}` Alinea una cadena de caracteres a la derecha en 30 caracteres, con la siguiente sentencia
- `{:30}` Alinear una cadena de caracteres a la izquierda en 30 caracteres, es decir crea espacios a la derecha
- `{:ˆ30}` Alinear una cadena de caracteres al centro en 30 caracteres, con la siguiente sentencia.
- `{:.9}` Truncamiento a 9 caracteres, con la siguiente sentencia.
- `{:>30.9}` Alinear una cadena de caracteres a la derecha 30 caracteres con truncamiento de 9.

```python
nombre = "smith"
edad = 23
estatura = 1.80
dinero = 12334.45623423489

print ("El señor {0:>30} mide {2:30} metros de altura, tiene una edad de {1:} Años, tiene ahorrado la suma de {3:.9} pesos ".format(nombre,edad,estatura,dinero))
#El señor                          smith mide                            1.8 metros de altura, tiene una edad de 23 Años, tiene ahorrado la suma de 12334.4562 pesos
```

**Formato por Tipo**
Como lo dice su nombre, dentro de las llaves se especifica el tipo de dato que contendrá.

- s para cadenas de caracteres (tipo str).
- d para números enteros (tipo int).
- f para números de coma flotante (tipo float).
  > .3f significara que un numero de coma flotante se imprima con 3 dígitos después de la como (.3).

```python
numero = 23.233344
print ("este numero {flotante:.3f} solo imprime 3 números decimales ".format(flotante = numero))
#este numero 23.233 solo imprime 3 números decimales
```

Podemos rellenar con ceros o espacios números enteros y números de punto flotantes:

```python
for i in [10,100,1000,10000,100000]:
    print(" Rellena con ceros y luego el numero {0:06d} Rellena con espacios y luego el numero {0:10d}".format(i))


for x in [12.00,12.000,12.0000] :
    print("diez espacios y luego el numero {0:10.3f} Rellena con ceros los espacios para completar 10 numeros {0:010.3f} ".format(x))
"""
Rellena con ceros y luego el numero 000010 Rellena con espacios y luego el numero         10
Rellena con ceros y luego el numero 000100 Rellena con espacios y luego el numero        100
Rellena con ceros y luego el numero 001000 Rellena con espacios y luego el numero       1000
Rellena con ceros y luego el numero 010000 Rellena con espacios y luego el numero      10000
Rellena con ceros y luego el numero 100000 Rellena con espacios y luego el numero     100000
diez espacios y luego el numero     12.000 Rellena con ceros y luego el numero 000012.000
diez espacios y luego el numero     12.000 Rellena con ceros y luego el numero 000012.000
diez espacios y luego el numero     12.000 Rellena con ceros y luego el numero 000012.000
"""
```

**Lo mejor para el final `f-Strings`**
Es para mi la mejor forma de dar formato a las cadenas de caracteres en python, es facil y muy entendible,
lo unico que tenemos que hacer, es anteponer el literal `f o F` a nuestra cadena de caracteres, y poner entre llaves la variable o sentencia, a combinación de lo que ya hemos visto dentri de las mismas.

```python
class pelicula:
    def __init__ (self):
        self.nombre = "hacker"
        self.duracion = 2

    def __str__(self):
        return f" Esta pelicula {self.nombre}  dura {self.duracion} horas"

    def __repr__(self):
        return f" Esta pelicula {self.nombre}  dura {self.duracion} horas. este es con __repr__"



peli1 = pelicula()
nombre = "johan"
print (f"hola a este f-string {2*3}, puedo hacer esto {nombre.upper()} y esto {peli1 } y esto {peli1 !r}")
#La salida  es la siguiente:
>>>hola a este f-string 6, puedo hacer esto JOHAN y esto  Esta pelicula hacker  dura 2 horas y esto  Esta pelicula hacker  dura 2 horas. este es con __repr__
```

> Nota:Los métodos **str**()y se**repr**() ocupan de cómo se presentan los objetos como cadenas, por lo que deberá asegurarse de incluir al menos uno de esos métodos en su definición de clase. Si tiene que elegir uno, elija **repr**()porque puede usarse en lugar de **str**().
> La cadena devuelta por **str**()es la representación informal de cadena de un objeto y debe ser legible. La
> cadena devuelta por **repr**()es la representación oficial y no debe ser ambigua. Llamando str()y repr()es
> preferible utilizar **str**()y **repr**()directamente.
> De forma predeterminada, se usarán las cadenas f **str**(), pero puede asegurarse de que se usen **repr**()si
> incluye el indicador de conversión !r. (ver ejemplo anterior).

### Buscando strings con `find()`

find lo que hace es, encontrar el indice del la primera letra del string que se pretende buscar. ejemplo:

```python
nombre = 'raboncita'
buscar = nombre.find('bon')
print (buscar)
#Resultado:2 = es el indice donde esta bon
```

tambien puedo decirle a `find ()` desde que numero de indice quiero que inicie la búsqueda. `find ('busca esto', 2 aportir de este indice)`.

Ejemplo: buscar un espacio a partir de el indice 2 ('b'):

```ptyhon
nombre = 'rabonc ita'
buscar = nombre.find(' ',2)
print (buscar)
#resultado = 6 indice
```

### Buscar y reemplazar strings con `replace()`

Ejemplo: `replace ('palabra a reemplazar', 'reemplazo')`

```python
greet = 'Significa saludo'
remplazar = greet.replace('Significa','Traducción al español = ')
print (remplazar)
#resultado: tradución al español = saludo
```

### Qutar los espacios en blanco de un `string`

`lstrip()`, ls hace referencia a left (izquierda), por lo tanto quita los espacios en blanco del lado izquierdo del `string`.
`rstrip()`,ls hace referencia a right (derecha), por lo tanto quita los espacios en blanco del lado derecho del `string`.
`strip`, elimina los espacios en blanco tanto de la derecha como de la izquierda.
Ejemplo:

```python
greet = '    *greet significa saludo*     '
print (greet)
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())
#Resultados Observe los espacios:
#*greet significa saludo*
#*greet significa saludo*
#    *greet significa saludo*
#*greet significa saludo*
```

### Prefijos `startwith()`

cuando necesitamos saber si una cadena inicia con una letra especifica, o una palabra especifica, ó deseamos especificar si en cierto rango de indices existe una palabra que inicie con un string espefifco, utilizamos `starwith ('string a buscaer',indice_star,indice_stop)`, el indice de star y stop no son necesarios, se pueden dejar sin parametros y la búsqueda iniciará desde el indice 0.

Ejemplo: es importante que el indice de star coincida para que retorne un true, de lo contrario retornará un false.

```python
parabra = 'es un bonito dia hoy domingo'
print (parabra.startswith('bonito',6,17))
#resultado: true
parabra = 'es un bonito dia hoy domingo'
print (parabra.startswith('bonito',5,17))
#resultado: false
```

### Análisis y extracción

Ejemplo:

```python
datos = 'Escrito por johan.jimenez@perex.sern.us en febrero 15 de 2020'
inicio = datos.find ('@')
print (inicio)
fin = datos.find (' ',inicio)
print (fin)
terminal = datos [inicio +1 : fin]
print (terminal)
#Resultado:
#25
#39
#perex.sern.us
```

### Tipos de datos Listas

Este tipo de datos hace parte de los datos compuestos, y a su vez esta dentro de las secuencias (como los string, que tambien son secuencias).
las listas son las mas maniobrables, dentro dentro a lo que a secuencias compete. para escribir una lista en python, se hace dentro de corchetes `[]` y sus elementos separados por comas `[1, "johan", 12.4], como puedes ver, los elementos pueden ser de tipos de datos distintos.

los elementos de una lista pueden ser accedidos por sus indices:

```python
lista = [1, "johan",12.4]
print (f"Accediendo a una lista por indice = {lista[1]}")

print (f"Tambien se puede acceder a los elementos con un indice negativo ej: lista[-1] = {lista[-1]}")
#Tambien se puede acceder a los elementos con un indice negativo ej: lista[-1] = 12.4
```

con la función `len()` nos regresa la longitud de la lista (que traduce la cantidad de elementos que tienen),por lo tanto la longitud de la lista se incrementa sólo en 1. Los índices negativos van entonces de -1 (último elemento) a -len(lista (primer elemento).:

```python
lista = [1, "johan",12.4]
print (f"la cantidad de elementos de la lista es {len(lista)}")
# la cantidad de elementos de la lista es 3
```

#### Algunos metodos

- `append(agragame_solo_un_elemento)`

  - Este metodo agrega un elemento al final de una lista:

    ```python
      lista = [1, "johan",12.4]
      print (f"agregando un elemento con append {lista.append('jessi')}{lista}")
      #agregando un elemento con append None[1, 'johan', 12.4, 'jessi']
    ```

- `count(cuantas_veces_estoy_en_la_lista)`

  - Este metodo recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista:

  ````python
     lista = [1, "johan",12.4,1,3,1]
     print (f"""contando con metodo count(). cuantas veces
     esta el numero 1 en la lista = {lista.count(1)}""")
     #contando con metodo count(). cuantas veces
     #esta el numero 1 en la lista = 3
     ```
  ````

- `extend(agrega_una_lista)`

  - añade todos los elementos del objeto dado al final de la lista, por lo que la longitud de la lista aumenta
    en la longitud del objeto dado.solo admite listas (elementos iterables).

  ```python
  lista = [1, "johan",12.4,1,3,1]
  print (f"""Utilizando el metodo extend(). {lista.extend(["cursos", "python"])}, {lista}""")
  # Utilizando el metodo extend(). None, [1, 'johan', 12.4, 1, 3, 1, 'cursos', 'python']
  ```

  ```python
  lista = [1, "johan",12.4,1,3,1]
  print (f"""Utilizando  Mal el metodo extend(). {lista.extend(3)}, {lista}""")
  # TypeError: 'int' object is not iterable
  ```

- `index(en_que_indice_estoy)`

  - Este metodo regresa la posición, o indice del elemento que le pasemos como argumento:

  ```python
  lista = [1, "johan",12.4,1,3,1]
  print (f"""Jonan esta en la posición  {lista.index('johan')} de la lista """)
  # Jonan esta en la posición  1 de la lista
  ```

- `insert(en_esta_posición, insertame)`

  - Este metodo inserta un elemento cualquiera, en el indice indicado en el argumento.

  ```python
  lista = [1, "johan",12.4,1,3,1]
  print (f"""Insetemos el nombre 'smit en el indice 3' {lista.insert(3,"smit")}, {lista} """)
  # Insetemos el nombre 'smit en el indice 3' None, [1, 'johan', 12.4, 'smit', 1, 3, 1]
  ```

- `pop(elimina_valor_del_indice_que_escriba_aqui)`

  - Por defecto Retorna el ultimo elemento de una lista y lo borra, pero se le puede pasar como argumento el
    indice a eliminar.

    ```python
    lista = [1, "johan",12.4,1,3]
    print (f"""la lista original es {lista},
    Eliminando el ultimo elemento de la lista que es {lista.pop()},
    la lista queda asi: {lista} """)
    # la lista original es [1, 'johan', 12.4, 1, 3],
    #Eliminando el ultimo elemento de la lista que es 3,
    #la lista queda asi: [1, 'johan', 12.4, 1]
    ```

- `remove()`

  - Este metodo es un poco parecido al alterior (pop), pero este metodo remueve el `VALOR` que le pasemos como
    parametro, si el valor no se encuentra dentro de la lista, el metodo devuelve una excepción (ValurError).

  ```python
  lista = [1, "johan",12.4,1,3]
  print (f"""la lista original es {lista},
  Para eliminar un valor, por ejempo (johan) se hace de la siguiente forma: {lista.remove("johan")},
  la lista queda asi: {lista} """)
  # la lista original es [1, 'johan', 12.4, 1, 3],
  #Para eliminar un valor, por ejempo (johan) se hace de la siguiente forma: None,
  #la lista queda asi: [1, 12.4, 1, 3]
  ```

  **_Ejemplo de retorno de ValueError_**

  ```python
  lista = [1, "johan",12.4,1,3]
  print (f"""Cuando se pasa un parametro al metodo remove() que no esta en la lista
  el metodo devuelve ValuError.
  esto retorna una Exepción {lista.remove(200)} """)
  # ValueError: list.remove(x): x not in list
  ```

- `reverse()`

  - Este metodo invierte el orden de los elementos de una lista:

  ```python
  lista = list(range(1,11,1))
  print (f"""esta lista {lista}, la podemos poner en orden descendente con el metodo reverse() Asi:
  {lista.reverse()} {lista}""")
  #esta lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], la podemos poner en orden descendente con el metodo reverse()
  #Asi:
  #None [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  ```

- `sort()`

  - Este motodo ordena los elementos de una lista:

  ```python
  lista = list(range(10,0,-1))
  print (f"""esta lista {lista}, la podemos ordenar con el metodo sort() Asi: {lista.sort()} {lista},
  y podemos ponerla de forma original {lista.sort(reverse = True)}{lista}""")
  #esta lista [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], la podemos ordenar con el metodo sort() Asi: None [1, 2, 3, 4,
  5, 6, 7, 8, 9, 10],
  #y podemos ponerla de forma original None[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  ```

### convertir a tipo lista

para convertir a tipo lista se utiliza el metodo `list()`:

```python
tupla = (1,4)
convert_to_lista = list(tupla)
print (f"""Esto es una tupla {tupla}, aqi se convirtio a una lista {convert_to_lista}
como ya es una lista puedo cambiar sus elementos {convert_to_lista.insert(2,"jessi")}
la lista quedaría {convert_to_lista}""")
#Esto es una tupla (1, 4), aqi se convirtio a una lista [1, 4]
#como ya es una lista puedo cambiar sus elementos None
#a lista quedaría [1, 4, 'jessi']
```

### Bonus

Obteniendo rangos específicos de una lista:

- [:] Muestra todos los elementos de una lista:

  ```python
  lista = list(range(10,0,-1))
   print (f"""Mostrar todos los elementos de una lista [:] asi: {lista[:]}""")
  #Mostrar todos los elementos de una lista [:] asi: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  ```

- [`indice`:] Muestra el valor desde el `(indice)` hasta el final de la lista:

  ```python
  lista = list(range(10,0,-1))
  print (f"""Muestra el valor desde el indice 4 hasta el final de la lista: {lista[4:]}""")
  #Muestra el valor desde el indice 4 hasta el final de la lista: [6, 5, 4, 3, 2, 1]
  ```

- [:`indice`]: Muestra el valor desde el indice 0 hasta el valor del `indice -1`:

  ```python
  lista = list(range(10,0,-1))
  print (f"""Muestra el valor  de la lista {lista} desde el indice 0 hasta el valor del `8 -1 = 7` de la lista:
  {lista[:8]}""")
  #Muestra el valor  de la lista [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] desde el indice 0 hasta el valor del `8 -1 =
  #7` de la lista: [10, 9, 8, 7, 6, 5, 4, 3]
  ```

- [desde_este_indice : hasta_este_indice-1 : con_este_salto] Tambien podemos obtener un rango con saltos
  especificos:

  ```python
  lista = list(range(10,0,-1))
  print (f"""Solo Muestra el valor  de la lista {lista} : desde el indice 0 hasta el indice 10-1 = 9 en saltos
  de 2.
  esto da como resultado: {lista[0:10:2]}""")
  #Solo Muestra el valor  de la lista [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] : desde el indice 0 hasta el indice 10-1
  #= 9 en saltos de 2.
  #esto da como resultado: [10, 8, 6, 4, 2]
  ```

### El metodo `lista.split()`: separa las palabras de un string y las guarda en una lista

```python
oracion= "este es un pequeño curso de python"
print (f"""Separando las palabras de la oración con split() Asi: {oracion.split()}""")
#Separando las palabras de la oración con split() Asi: ['este', 'es', 'un', 'pequeño', 'curso', 'de', 'python']
```

### Iterar sobre dos o mas secuencias

```python
nombres = ["johan","estella","javier","yeison"]
edades = [29,48,53,25]
ocupacion = ["sevidor","Ama de casa","Agricultor","Servidor"]

for name, age, labor in zip (nombres,edades,ocupacion):
    print (f"""{name}, tiene {age} años, y trabaja como {labor}""")

"""
johan, tiene 29 años, y trabaja como sevidor
estella, tiene 48 años, y trabaja como Ama de casa
javier, tiene 53 años, y trabaja como Agricultor
yeison, tiene 25 años, y trabaja como Servidor
"""
```

### Datos Tipo Tuplas

Al igual que los `strings`, las las `listas`, las tuplas son de tipo **_secuencia_**, y son **Inmutables**, esto quiere decir que no se puede modificar.`tupla = (ele1,ele2) o tupla = (ele1,)`

### Metodos de la tuplas

- `count(cuantas_vece_estoy_en_la_tupla)`: recibe el valor de un elemento y regresa el numero de veces que ese
  elemento se encuentra en la tupla:

  ```python
  tupla = ("d","nombre",2,78.23,"d")
  print(f"Cuantas veces esta el literal 'd' en la tupla?: esta {tupla.count('d')} veces")
  #Cuantas veces esta el literal 'd' en la tupla?: esta 2 veces
  ```

- Metodo `Index(en_que_indice_estoy)` Tiene la misma funcionalidad cuando se aplica a las lista, este metodo recibe un parametro, que es el valor al que le queremos conocer su ubicación en la tupla:

  > Nota: El metodo regresa una Excepción `ValueError` si no se encuentra en la tupla.

  ```python
  tupla = ("d","nombre",2,78.23,"d")
  print(f"En que indice esta el valor 2 en la tupla?, el valor 2 esta en el indice {tupla.index(2)}")
  #En que indice esta el valor 2 en la tupla?, el valor 2 esta en el indice 2

  print(f"En que indice esta el valor 2 en la tupla?, el valor 2 esta en el indice {tupla.index(9)}")
  #ValueError: tuple.index(x): x not in tuple
  ```

- Convertir a Tuplas: se puede convertir a tipo de dato `tupla` utilizando el metodo `tuple()`

  ```python
  lista = range(6)
  print (f"esta es una lista {lista}, y la convertimos a una tupla {tuple(lista)}")
  #esta es una lista range(0, 6), y la convertimos a una tupla (0, 1, 2, 3, 4, 5)
  ```

### Bonus de tuplas

**Formas de declarar tuplas**:

- `tupla = 12,5,6,'e'`
- `tupla = (12,5,6,'e')`  
  **tuplas anidadas**:
- `tupla2 = tupla, (9, 89, 12.4)`  
  **se pueden asignar a variables los valores de los indices de una tupla**:
- `a,b,c,d = tupla`  
  \*\*Metodo `enum()`: me permite enumerar facilmente los elemtos de una tupla, lista con un ciclo for:

```python
tupla = ("johan","jessi","smit","leion")
print (tupla)
for indice, tup in enumerate (tupla):
    print (indice,tup)
"""
esta es la salida:
0 johan
1 jessi
2 smit
3 leion
```

**aplicación de las tuplas:**

```python
print ("\nDefiniendo conexión a BD MySQL")
print ("==============================\n")

conexion_bd = "127.0.0.1","root","qwerty","nomina",
print ("Conexión típica:", conexion_bd)
print (type(conexion_bd))
conexion_completa = conexion_bd, "3307","10",
print ("\nConexión con parámetros adicionales:", conexion_completa)
print (type(conexion_completa))

print ("\n")

print ("IP de la BD:",  conexion_completa[0][0])
print ("Usuario de la BD:",  conexion_completa[0][1])
print ("Contraseña de la BD:",  conexion_completa[0][2])
print ("Nombre de la BD:",  conexion_completa[0][3])
print ("Puerto de conexión:", conexion_completa[1])
print ("Tiempo de espera en conexión:", conexion_completa[2])

print ("""\nMás información acerca de MySQL y Python \
http://mysql-python.sf.net/MySQLdb.html\n""")
"""
salida es la siguiete:

Definiendo conexión a BD MySQL
==============================

Conexión típica: ('127.0.0.1', 'root', 'qwerty', 'nomina')
<class 'tuple'>

Conexión con parámetros adicionales: (('127.0.0.1', 'root', 'qwerty', 'nomina'), '3307', '10')
<class 'tuple'>


IP de la BD: 127.0.0.1
Usuario de la BD: root
Contraseña de la BD: qwerty
Nombre de la BD: nomina
Puerto de conexión: 3307
Tiempo de espera en conexión: 10
"""
```

### Tipo de dato diccionario

la clase `dict()` es de tipo `Mapeos`,es la unica en su clase, algo que normalmente no se explica. Los diccionarios se crean con una lista separada de par {"claave":valor} y si queremos incluir otro par, lo separmos por comas:

```python
diccionario = {"televisor": "samsug","pulgadas": 42,"precio": 1200000}
print(f"esto es un diccionario{diccionario}")
#esto es un diccionario{'televisor': 'samsug', 'pulgadas': 42, 'precio': 1200000}
```

**Podemos acceder a un valor del diccionario con su clave Asi**:

```python
diccionario = {"televisor": "samsug","pulgadas": 42,"precio": 1200000}
print(f"Puedo accder a un valor con su clave, el tv es de {diccionario['pulgadas']} pulgadas" )
#Puedo accder a un valor con su clave, el tv es de 42 pulgadas
```

Otra forma de crear un diccionario es desde su constructor:

```python
diccionario = dict (nombre = "johan", edad = 29, estado_civil = "soltero")
print (f"{diccionario['nombre']} es {diccionario['estado_civil']}")
#johan es soltero
```

**Asignando valor de una clave**:

```python
diccionario = dict (nombre = "johan", edad = 29, estado_civil = "soltero")
diccionario['edad'] = 32
print (f"La edad fue modificada al valor:  {diccionario['edad']}")
#La edad fue modificada al valor:  32
```

\*\*Iteración `in`
una de sus aplicaciones es como operador de comparación Asi:

```python
diccionario = dict (nombre = "johan", edad = 29, estado_civil = "soltero")
if 'nombre' in diccionario:
    print (f"{diccionario['nombre']} esta en el dicionario")
#johan esta en el dicionario
```

### Metodos aplicados a los Diccionarios

- `clear()`: Remueve todos los elementos del diccionario:

  ```python
  diccionario = dict (nombre = "johan", edad = 29, estado_civil = "soltero")
  print (f"""Este dicionario{diccionario} lo podemos limpiar con clear().
  {diccionario.clear()}
  ahora el diccionario esta vacio {diccionario}""")
  """
  Este dicionario{'nombre': 'johan', 'edad': 29, 'estado_civil': 'soltero'} lo podemos limpiar con clear().
  None
  ahora el diccionario esta vacio {}
  """
  ```

- `copy()`: Este metodo retorna una copia de un diccionario:

  ```python
  diccionario = dict (nombre = "johan", edad = 29, estado_civil = "soltero")
  copia_diccionario = diccionario.copy()
  if diccionario == copia_diccionario :
      print (f"diccionario{diccionario} es igual a\n \t   {copia_diccionario}")
  """
  diccionario{'nombre': 'johan', 'edad': 29, 'estado_civil': 'soltero'} es igual a
             {'nombre': 'johan', 'edad': 29, 'estado_civil': 'soltero'}
             """
  ```

- `fromekeys(lista_de_llaves, valor_de_cada_llave)`: este método crea un nuevo **diccionario** con **_claves_** a partir de un tipo de dato **_secuencia_**. El valor de _value_ por defecto es de tipo None.

  ```python
  lista_llaves = {"edad1","edad2","edad3"}
  valor_edades = dict.fromkeys(lista_llaves,20)
  print (f"esta es la lista de llaves:{lista_llaves}, aqui se le asignan valorea: {valor_edades}")
  #esta es la lista de llaves:{'edad3', 'edad1', 'edad2'}, aqui se le asignan valorea: {'edad3': 20, 'edad1':
  #20, 'edad2': 20}
  ```

- `get(valor_de_esta_llave)`: Este método regresa el valor de una llave que se pasa como parametro, si no es encontrada este método retornará None:

  ```python
  lista_llaves = {"edad1":30,"edad2":19,"edad3":80}
  print (f"Encontremos el valor de la edad2 con get(): {lista_llaves.get('edad2')}")

  #Encontremos el valor de la edad2 con get(): 19
  ```

- `has_key(esta_clacve_existe)`: Retorna True si encuentra la clave enviada como argumento. no me ha funcionado, pero es mejor utilizar `in`.

- `items()`: este metodo retorna una lista de pares de diccionarios, pero como `tuplas`:

```python
diccionario = dict(edad1 = 23, edad2 = 78, edad3 = 18)
print (f"este diccionario {diccionario} lo podemos convertir a tuplas Asi: {diccionario.items()}")
#este diccionario {'edad1': 23, 'edad2': 78, 'edad3': 18} lo podemos convertir a tuplas Asi:
#dict_items([('edad1', 23), ('edad2', 78), ('edad3', 18)])
```

> El método `items()` tambien me permite iterar sobre un diccionario:
>
> ```python
> diccionario = dict(edad1 = 23, edad2 = 78, edad3 = 18)
> for clave, valor in diccionario.items():
>    print (clave, valor)
> """
> edad1 23
> edad2 78
> edad3 18
> """
> ```

- `keys()`: regresa una lista con las llaves del diccionario

  ```python
  diccionario = {"edad1" : 23, "edad2" : 78, "edad3" : 18}
  print (diccionario.keys())
  #dict_keys(['edad1', 'edad2', 'edad3'])
  ```

  Para iterar sobre las llaves podemos hacer los siguiente:

  ```python
  diccionario = {"edad1" : 23, "edad2" : 78, "edad3" : 18}
  for llaves in diccionario.keys():
      print(llaves)
  """
  edad1
  edad2
  edad3
  """
  ```

  - `pop(clave_a_eliminar)`:Este método se le pasa un argumento que es la clve del valor que deseamos eliminar,
    retorna el valor de la llave y la elimina, si la clave no es en contrada lanza una excepción KeyError

  ```python
  diccionario = {"johan":"ingeniero", "hobie":"programación","estado_civil":"soltero"}
  print (f"Eliminaremos el hobie con pop() {diccionario.pop('hobie')}, el diccionario queda asi:
  {diccionario}")
  #Eliminaremos el hobie con pop() programación, el diccionario queda asi: {'johan': 'ingeniero',
  #'estado_civil': 'soltero'}
  ```

- `popitem()`: No recibe parametros, regresa una tupla con la ultima clave-valor del diccionario y lo elimina.

```python
diccionario = {"johan":"ingeniero", "hobie":"programación","estado_civil":"soltero"}
print (f"""Eliminaremos el ultipo par del diccionario {diccionario.popitem()},
el diccionario queda asi: {diccionario}""")

#Eliminaremos el ultipo par del diccionario ('estado_civil', 'soltero'),
#el diccionario queda asi: {'johan': 'ingeniero', 'hobie': 'programación'}
```

- serdefault()`:en pocas palabra me permite agregar un par llavea:valor a un diccionario, me permite asignarle un valor a la llave si no la tiene, y a su vez asignar este par a una variable cualquiera.

```python
diccionario = {"nombre":"johan", "edad":29, "estatura":1.75}
print(f"""el diccionario original es este: {diccionario},
El nuevo valor de la llave (ocupación)  que se va a agregar es esta: { diccionario.setdefault("ocupacion","ing. Elenctronico")},
El diccionario queda de la siguiente manera {diccionario}""")

"""
el diccionario original es este: {'nombre': 'johan', 'edad': 29, 'estatura': 1.75},
El nuevo valor de la llave (ocupación)  que se va a agregar es esta: ing. Elenctronico,
El diccionario queda de la siguiente manera {'nombre': 'johan', 'edad': 29, 'estatura': 1.75, 'ocupacion': 'ing. Elenctronico'}
"""
```

- setdefault() tambien tiene una aplicación importante, y es la de agrupar N tuplas por el valor el cual se repite más y construir un diccionario que cuyas claves son los valores mas repetidos y cuyos valores este agrupados en tipo listas:
  cada tupla anidada es un par llave, valor. `setdefault(clave,[lista de valores]).append(valores)` lo que hace es agregar a cada llave repetida una lista con sus valores, en vez de reemplazar la llave por otra.

para entender mejor, cuando estamos creando un diccionario y deseamos crear una llave repetida, aunque tenga diferente valor, al imprimir el diccionario, este solo nos tomara una de las 2 paras (llave valor):

```python
diccionario = {"nombre":"johan", "nombre":"estella","edad":29}
print (diccionario)

#la salidas es la siguiente:
# {'nombre': 'estella', 'edad': 29}
```

Como se puede ver en el ejemplo anterior, apesar de que hay 2 pares (llave:valor), y 2 de sus claves son iguales, pero sus valores son diferentes, solo toma 1.

para solucionar esto, podemos guardar los valores de las claves que son iguales en una lista como segundo parametro del método `setdefault(llave,[]).append(valor ve la llave repetida)`.

**_Ejemplo1_**

```python
tupla = (("nombre","johan"), ("edad",29),("estatura",1.73))
dicionario = {}
#print (dicionario['nombre'])
dicionario.setdefault('nombre',['estella'])
dicionario.setdefault(tupla[0][0],tupla[0][1]).append(tupla[0][1])
print (dicionario)

#{'nombre': ['estella', 'johan']}
```

**_Ejemplo2_**

```python
tupla = (("nombre","johan"), ("edad",29),("estatura",1.73),("nombre","yeison"),("edad",23))
diccionario = {}
for clave , valor in tupla:
    diccionario.setdefault(clave,[]).append(valor)
print (diccionario)
# la salida es la siguiente:
#{'nombre': ['johan', 'yeison'], 'edad': [29, 23], 'estatura': [1.73]}
```

- `update(dic_que_voy_agregar)`:No retorna nada, y recibe como parametro un objeto iterable, que será agregado a otro.

```python
diccionario = {"nombre":"johan", "madre":"estella","edad":29}
diccionario2 = {"peso":90,"estado_civil":"soltero"}
diccionario.update(diccionario2)
print (f"""Actualizando el diccionario con el contenido del diccionanario2
{diccionario2}
{diccionario}""")

"""
Actualizando el diccionario con el contenido del diccionanario2
{'peso': 90, 'estado_civil': 'soltero'}
{'nombre': 'johan', 'madre': 'estella', 'edad': 29, 'peso': 90, 'estado_civil': 'soltero'}
"""
```

> Nota:cuando se pone una clave repetida en el objeto iterable2, este es reemplazo, NO duplicado.

\*`values()`: este método regresa una lista con los valores del diccionario.

```python
diccionario = {"nombre":"johan", "madre":"estella","edad":29}
print (f"los valores del diccionaraio son:{diccionario.values()}")
#los valores del diccionario son:dict_values(['johan', 'estella', 29])
```

### Funciones integradas en python aplicables a los diccionarios

- `len ()`:se usa para ver la cantidad de paras llave:valor que tiene el diccionario.

```python
 diccionario = {"nombre":"johan", "madre":"estella","edad":29}
print(f"Cuantos parres tiene el diccionario?, el diccionario tiene: {len (diccionario)} pares llave:valor")
#Cuantos pares tiene el diccionario, el diccionario tiene: 3 pares llave:valor
```

### convertir a diccionarios

para convertir a diccinarios solo basta con usar la función `dict()`.

```python
tupla = ("nombre","johan"),("apellido","jimenez")
dic = dict(tupla)
print(dic)
#{'nombre': 'johan', 'apellido': 'jimenez'}
```

## Tipo de datos `conjunto`- `set`

Un conjunto, es una colección no ordenada y sin elementos repetidos. Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas. son mutables, sin orden, no contienen duplicados.

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
#{1, 2, 3, 4, 5, 7, 11}
```

como se puede ver en el ejemplo anterior, cuando de declara el set,

1. los datos estan desordenados.
   2.el dato con el valor 4 esta repetido
   pero al imprimir por consola el `set()` este muestra los datos ordenados de menor a mayor, y no muestra datos repetidos.

### Algunos metodos set()

#### add(): agrega un elemento al conjunto mutable, no tiene efecto si el elemento a agregar ya existe

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(f"""El set original {set_mutable1}, agregamos 45,
{set_mutable1.add(45)}, el set queda de la siguiente forma:
{set_mutable1}""")

"""
El set original {1, 2, 3, 4, 5, 7, 11}, agregamos 45,
None, el set queda de la siguiente forma:
{1, 2, 3, 4, 5, 7, 11, 45}
"""
```

#### clear(): elimina todos los elementos desde el **conjunto mutable**

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(f"""El set original {set_mutable1}, borremos todos los elementos,
{set_mutable1.clear()}, el set queda de la siguiente forma:
{set_mutable1}""")

"""
El set original {1, 2, 3, 4, 5, 7, 11}, borremos todos los elementos,
None, el set queda de la siguiente forma:
set()
"""
```

#### copy(): este método retorna una copia superficial del **conjunto**

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
conjunto2 = set_mutable1.copy()
print(f"""El set original {set_mutable1}, y la siguiente es una copia,
\t\t{conjunto2}""")

"""
El set original {1, 2, 3, 4, 5, 7, 11}, y la siguiente es una copia,
                {1, 2, 3, 4, 5, 7, 11}
"""
```

#### difference():Este método devuelve la diferencia entre dos conjunto mutable o conjunto inmutable: todos los elementos que están en el primero, pero no en el argumento. `los_que_no_coincidan_con.difference(con_este)>son los que retornan.`

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4,345,6543])
conjunto2 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(f"""verificanco la diferencia entre conjuntos {set_mutable1.difference(conjunto2)}""")

"""
verificando la diferencia entre conjuntos {345, 6543}
"""
```

**_otro ejemplo_**

```python
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
conjunto2 = set([4, 3, 11, 7, 5, 2, 1, 4,23,45,89])
print(f"""verificanco la diferencia entre conjuntos {conjunto2.difference(set_mutable1)}""")

"""
verificando la diferencia entre conjuntos {89, 45, 23}
"""
```

#### difference_update():este método actualiza un tipo de dato conjunto, con la diferencia de los conjuntos

`me_modifico_con_la_diferencia.difference_update(con_este_conjunto)`:

```python
conjunto1 = set([4, 3, 11, 7, 5, 2, 1, 4])
conjunto2 = set([4, 3, 11, 7, 5, 2, 1, 4,23,45,89])
print(f"""Este es el conjunto2 = {conjunto2},
este es el conjunto1 = {conjunto1}
Actualizando el conjunto2 con los valores que no coinciden con el conjunto1
{conjunto2.difference_update(conjunto1)}
conjunto2 ={conjunto2}""")

"""
Este es el conjunto2 = {1, 2, 3, 4, 5, 7, 11, 45, 23, 89},
este es el conjunto1 = {1, 2, 3, 4, 5, 7, 11}
Actualizando el conjunto2 con los valores que no coinciden con el conjunto1
None
conjunto2 ={45, 23, 89}
"""
```

### discard(): Remueve un elemento de un conjunto

```python
conjunto1 = set([4, 3, 11, 7, 5, 2, 1, 4])
conjunto2 = set([4, 3, 11, 7, 5, 2, 1, 4,23,45,89])
print(f"""Eliminando un elemento con discard(): {conjunto1.discard(11)}
asi quedaría el conjunto1 = {conjunto1}""")

"""
Eliminando un elemento con discard(): None
asi quedaría el conjunto1 = {1, 2, 3, 4, 5, 7}
"""
```

#### intersection():hace lo contrerio que difference, retorna los elementos que estas repetidos en los conjuntos

```python
conjunto1 = set([4, 3, 11, 7, 5, 2, 1, 4])
conjunto2 = set([4, 3, 11, 7, 5, 2, 1, 4,23,45,89])
print(f"""Conparando conjunto1:{conjunto1}
con el conjunto 2 {conjunto2}
la intersección es : {conjunto1.intersection(conjunto2)}""")

"""
Conparando conjunto1:{1, 2, 3, 4, 5, 7, 11}
con el conjunto 2 {1, 2, 3, 4, 5, 7, 11, 45, 23, 89}
la intersección es : {1, 2, 3, 4, 5, 7, 11}
"""
```

## intersection_update()

Este método puede recibir varios conjuntos como parámetro, y regresa las intersecciones de los mismos (LOS REPERIDOS)

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
conjunto_3 = {'smit',98,'ronal','jhan',23,34}
conjunto_3.intersection_update(conjunto_1,conjunto_2)
print(f"la intersección de los 3 conjuntos es:{conjunto_3}")
# la intersección de los 3 conjuntos es:{'ronal', 34, 'smit', 23, 'jhan'}
```

### isdisjoint()

Regresa `True` si No hay elementos comunes, o más bien, si todos los elementos son distintos, el método retorna true.

```python
conjunto_4 = {'nombre','ocupacion',34}
conjunto_5 = {'johan','ing',45}
print (f"El conjunto 1 y el conjunto 2 es {conjunto_4.isdisjoint(conjunto_5)} que no son iguales")
#El conjunto 1 y el conjunto 2 es True que no son iguales
```

### issubset()

Este método retorna valor `True`, si el conjunto pasado por parámetros contiene todos los valores del conjunto que ejecuta el método, dicho de otra manera, si el conjunto que ejecuta el método es un subconjunto del conjunto que se pasa como parámetros.

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
conjunto_3 = {'smit',98,'ronal','jhan'}
conjunto_3.intersection_update(conjunto_1,conjunto_2)
print(f"Es {conjunto_3.issubset(conjunto_1)} que el conjunto 3 es un subconjunto del conjunto 1")
# Es True que el conjunto 3 es un subconjunto del conjunto 1
```

### issuperset()

El método issuperset () devuelve True si todos los elementos de un conjunto A ocupan el conjunto B que se pasa como argumento y devuelve falso si todos los elementos de B no están presentes en A.
Esto significa que, si A es un superconjunto de B, entonces devuelve verdadero; más falso

Sintaxis:

`A. superconjunto (B)`
comprueba si A es un superconjunto de B o no:

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
conjunto_3 = {'smit','ronal','jhan'}
conjunto_3.intersection_update(conjunto_1,conjunto_2)
print(f"Es {conjunto_1.issuperset(conjunto_3)} que el conjunto 1 es superconjunto de conjunto 3")
# Es True que el conjunto 1 es superconjunto de conjunto 3
```

#### pop)()

Este método, no toma ningún argumento, elimina un elemento arbitrariamente del conjunto y lo retorna, si el conjunto esta vacío, lanza una excepción `leyeron`.

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
print (eliminando un elemento aleatoriamente:{conjunto_1.pop()}, el conjunto queda así:{conjunto_1}")
#eliminando un elemento aleatoriamente:34, el conjunto queda así:{'smit', 'ronal', 23, 'jhan', 'autos'}
```

#### remove(`elimíname`)

Remueve un elemento especificado en su argumento.

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
print (removiendo a ronal del conjunto_1 {conjunto_1.remove('ronal')}, así queda el conjunto:{conjunto_1}")
#Removiendo a ronal del conjunto_1 None, así queda el conjunto:{34, 'autos', 23, 'smit', 'jhan'}
```

#### symmetric_difference()

Retorna la diferencia entre 2 conjuntos (los valores que no se repiten).

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
print (f"los valores que no se repiten son: {conjunto_1. symmetric_difference(conjunto_2)}")
#los valores que no se repiten son: {'autos', 445}
```

#### symmetric_difference_update()

Retorna un conjunto con el motos de los elementos de los 2 conjuntos que no se repiten, pero los guarda en el conjunto que ejecuta la función.

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
print (f"los valores que no se repiten se guardan en conjunto_1 {conjunto_1. symmetric_difference_update(conjunto_2)}, {conjunto_1}")
#los valores que no se repiten se guardan en conjunto_1 None, {'autos', 445}
```

#### union()

Retorna la union de 2 conjunto de datos (todos los datos de los 2 conjuntos pero sin repetir elementos).

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
conjunto_2 = {'smit','ronal','jhan',23,34,445}
print (f"La union de los los 2 conjuntos es:{conjunto_1.union(conjunto_2)}")
#La union de los los 2 conjuntos es:{'jhan', 34, #'smit', 'autos', 'ronal', 23, 44}
```

#### update()

Este método agrega un tipo lista, tupla, diccionario a un conjunto.

#### ejemplo lista

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
lista = ['sorevany',24,'prima']
print (agregando los elemento de la lista al conjunto1 {conjunto_1.update(lista)}, {conjunto_1}")
#agregando los elemento de la lista al conjunto1 None, {34, 'prima', 'autos', 'jhan', 'sorevany', 'smit', 23, 24, 'ronal'}
```

#### Ejemplo tuplas

```python
conjunto_1 = {'smit','ronal','autos','jhan',23,34}
tupla = (('sorevany',24,'prima'),('yeison',24,'hermano'))
print (agregando los elemento de la tupla al conjunto1 {conjunto_1.update(tupla)}, {conjunto_1}")
#agregando los elemento de la tupla al conjunto1 None, #{34, 'ronal', 'jhan', 'smit', 'autos', ('sorevany', #24, 'prima'), 23, ('yeison', 24, 'hermano')}
```

**Ejemplo diccionarios**
por defecto se agregan las llaves del diccionario, para agregar los valores de las llaves se utiliza `diccionario.values()`.

```python

conjunto_1 = {'smit','ronal','autos','jhan',23,34}
diccionario = {'nombre': 'johan','edad':29}
print (agregando los valores de la llaves del diccionario al conjunto1 {conjunto_1.update(diccionario.values())}, {conjunto_1}")
#agregando los valores de la llaves del diccionario al conjunto1 None, {34, 'smit', 'johan', 'jhan', 'ronal', 23, 'autos', 29}
```