# Intermedio 2
#llamadas implícitas a métodos especiales desde las CLASES
# Arbarr20

class Meta(type):
   
    
    def __len__(cls):        
        return 866666

    def __getattr__(cls,attr):
        value = super().__getattr__(attr)
        print(f"""\nEstas accediendo Implícitamente 
        a el método especial sobrescrito __getattribute__ de Metaclase :
        self :{cls}
        attr:{attr}
        value: {value}""")       
        return value    


class MiClase (metaclass=Meta):  
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
    de len(obj),Es:{len(obj)}""") 

print(f"""\nRecordar que Una clase es un Objeto, por lo tanto las llamadas implícitas de 
sus métodos especiales se buscaran en el diccionario de su PADRE (Type), si queremos una de
funcionalidad adicional a la llamada implícita de un método especial de una clase se debe
sobrescribir el método especial en su padre (metaclass type())
de lo contrario No esperemos que nos regrese de forma Implícita 
el método especial sobrescrito de su propio Diccionario""")

print(f"""\nAccediendo implícitamente Desde una clase a su propio método sobrescrito
    len(MiClase): {len(MiClase)}
    """)
"""
Nota: los Accesos Implícitos buscan primero en el Diccionario del Padre (Clase)
        No en el Diccionario el Objeto

Después del Acceso Implícito El resultado
    de len(obj),Es:40

Recordar que Una clase es un Objeto, por lo tanto las llamadas implícitas de 
sus métodos especiales se buscaran en el diccionario de su PADRE (Type), si queremos una de
funcionalidad adicional a la llamada implícita de un método especial de una clase se debe
sobrescribir el método especial en su padre (metaclass type())
de lo contrario No esperemos que nos regrese de forma Implícita 
el método especial sobrescrito de su propio Diccionario

Accediendo implícitamente Desde una clase a su propio método sobrescrito
    len(MiClase): 866666
"""