# Intermedio 1
# llamada Implícita y Explicita a los métodos especiales de una clase cuando no 
# están definidos y sobrescritos en su metaclass (padre = type)
# Arbarr20

class MiClase (object):  
    s = 300 
    def __getattribute__(self, attr):
        value=super().__getattribute__(attr)
        print (f"""\nEstas accediendo Implícitamente 
        a el método especial sobrescrito __getattribute__ de MiClase:
        self :{self}
        attr:{attr}
        value: {value}""")       
        return value

    def __len__(self):
        return 40 

obj = MiClase()

print(f"""\nNota: los Accesos Implícitos buscan primero en el Diccionario del Padre (Clase)
        No en el Diccionario el Objeto""")
print(f"""\nDespués del Acceso Implícito El resultado
    con la notación de punto al atributo s (obj.s),Es:{obj.s}""") 

print(f"""\nRecordar que Una clase es un Objeto, por lo tanto las llamadas implícitas de 
sus métodos especiales se buscaran en el diccionario de su PADRE (Type), si queremos una de
funcionalidad adicional a la llamada implícita de un método especial de una clase se debe
sobrescribir el método especial en su padre (metaclass type())
de lo contrario No esperemos que nos regrese de forma Implícita 
el método especial sobrescrito de su propio Diccionario""")
print(f"""\nAccediendo implícitamente Desde una clase a su propio método sobrescrito
    Miclase.s: {MiClase.s}
    Sorpresa: NO nos muesca el mismo resultado cuando llamamos a obj.s 
    "Estas accediendo Implícitamente ........."
    con esto sustentamos lo dicho anteriormente""")

print(f"""\nLa LLamada Explicita "MiClase.__getattribute__(obj,"s"))" 
    Si busca en el diccionario de la clase por lo tanto retornara el mismo resultado que 
    al llamar a obj.s:""")
print(MiClase.__getattribute__(obj,"s"))   

"""
Nota: los Accesos Implícitos buscan primero en el Diccionario del Padre (Clase)
        No en el Diccionario el Objeto

Estas accediendo Implícitamente 
        a el método especial sobrescrito __getattribute__ de MiClase:
        self :<__main__.MiClase object at 0x104824fa0>
        attr:s
        value: 300

Después del Acceso Implícito El resultado
    con la notación de punto al atributo s (obj.s),Es:300

Recordar que Una clase es un Objeto, por lo tanto las llamadas implícitas de 
sus métodos especiales se buscaran en el diccionario de su PADRE (Type), si queremos una de
funcionalidad adicional a la llamada implícita de un método especial de una clase se debe
sobrescribir el método especial en su padre (metaclass type())
de lo contrario No esperemos que nos regrese de forma Implícita 
el método especial sobrescrito de su propio Diccionario

Accediendo implícitamente Desde una clase a su propio método sobrescrito
    Miclase.s: 300
    Sorpresa: NO nos muesca el mismo resultado cuando llamamos a obj.s 
    "Estas accediendo Implícitamente ........."
    con esto sustentamos lo dicho anteriormente

La LLamada Explicita "MiClase.__getattribute__(obj,"s"))" 
    Si busca en el diccionario de la clase por lo tanto retornara el mismo resultado que 
    al llamar a obj.s:

Estas accediendo Implícitamente 
        a el método especial sobrescrito __getattribute__ de MiClase:
        self :<__main__.MiClase object at 0x104824fa0>
        attr:s
        value: 300
300
"""