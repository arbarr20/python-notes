# Descriptor 3
# Los descriptores solo se instancian una vez (aquí corregimos esto)
# Arbarr20

class OneDigitNumericValue():
    def __init__(self):
        self.value = {}
        """
        value: es el atributo  al que apunta el descriptor, pero es un atributo tipo diccionario,
        donde se guardan los diferentes objetos que modifican el atributo del descriptor
        esto es para que varios objetos puedan apuntar a su propio descriptor y de cierta forma
        solucionar lo del script anterior
        
        """

    def __get__(self, obj, type=None) -> object:                
        try:       
            print(f"self.value [{hex(id(obj))}] : {self.value[obj]}")  
            return self.value[obj]
            """
            return self.value[obj]:
            self: number
            value : es el diccionario
            []: campo donde va la clave del diccionario a buscar o modificar
            [obj]: [las instancias de la clase Foo] su valor depende de que objeto no este llamando
                       
            """
        except:            
            return 0
        

    def __set__(self, obj, valor) -> None:
        if valor > 9 or valor < 0 or int(valor) != valor:
            raise AttributeError("The value is invalid")        
        self.value[obj] = valor
        """
        self.value[obj] = value:
        self: number
        value : es el diccionario
        []: campo donde va la clave del diccionario a buscar o modificar
        [obj]: [las instancias de la clase Foo su valor depende de que objeto no este llamando, en este ejemplo puede se:
            * my_foo_object
            * my_second_foo_object
            * my_third_foo_object
        valor: es el valor que se asigna al atributo al llamar:
            my_foo_object.number = 4 donde 4 = valor
                    
        """
        print(f"dict-self-number :{self.value}")

    def __delete__(self, obj):
        print (f"Eliminando a {self.value}")
        del self.value
        

class Foo():
    
    number = OneDigitNumericValue()
    print (f"diccionario number {number.__dict__}")
    

my_foo_object = Foo()
my_second_foo_object = Foo()
my_third_foo_object = Foo()
my_foo_object.number = 4
my_second_foo_object.number =5
my_third_foo_object.number =8
"""

El diccionario value quedaría asi:
number.value = {
    "my_foo_object": 4,
    "my_second_foo_object":5,
    "my_third_foo_object.number":8
}
"""
print(f"my_foo_object.number : {my_foo_object.number}, la dirección de memoria es : {hex(id(my_foo_object))}")
print(f"my_second_foo_object : {my_second_foo_object.number}, la dirección de memoria es : {hex(id(my_second_foo_object))}")
print(f"my_third_foo_object.number : {my_third_foo_object.number}, la dirección de memoria es : {hex(id(my_third_foo_object))}")
del(my_foo_object.number)
print(f"my_foo_object.number : {my_foo_object.number}, la dirección de memoria es : {hex(id(my_foo_object))}")
print(f"my_second_foo_object : {my_second_foo_object.number}, la dirección de memoria es : {hex(id(my_second_foo_object))}")