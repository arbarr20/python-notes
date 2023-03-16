# Intermedio 3
#llamadas implícitas y Explícitas desde clase y objetos
# Arbarr20

class Meta(type):    
    
    def __getattribute__(cls,attr):        
        value = super().__getattribute__(attr)
        print(f"""\nEstas accediendo a el método especial sobrescrito 
        __getattribute__ de Metaclase :
        __getattr__(cls,attr):
        value = super().__getattr__(attr)
        self :{cls}
        attr:{attr}
        value: {value}""")       
        return value 
        
    def __len__(cls): 
        print("\nEjecutando...len desde Meta...........")       
        return 86000 


class MiClase (object,metaclass=Meta):  
    __metaclass__ = Meta
    s = 300
    def __getattribute__(self, attr):
        value=super().__getattribute__(attr)
        print (f"""\nEstas accediendo  a el método especial sobrescrito 
        __getattribute__ de MiClase:
        __getattribute__(self, attr)
        value=super().__getattribute__(attr)
        self :{self}
        attr:{attr}
        value: {value}""")       
        return value

    def __len__(self):
        print("\nEjecutando...len desde MiClase........... ")
        return 40 

obj = MiClase()

# Analizando llamadas  Implícita y Explicita de obj:
print("\nInicio:----------------------------------------------------------------")
print(f"""Llamada implícita de __len__ desde  obj:padre MiClase a un
        método especial __len__ sobrescrito
        [len(obj)] """)
print(f"Resultado: {len(obj)} len de su Padre MiClase")

print(f"""Llamada explicita de __len__ desde  obj:padre MiClase a un
        método especial __len__ sobrescrito, Pero a su vez es una llamada implícita a 
        __getattribute__ de Miclase
        como no existe len en su diccionario, toca hacer [obj.__len__=lambda:100]
        y luego si ejecutar [obj.__len__()], como se esta accediendo con la notación de punto
        sale un poco distinto a la llamada implícita por que se llama __getattribute__ de
        de MiClase
        """)
obj.__len__=lambda:100

print(f"Resultado: {obj.__len__()} len propio objeto por medio de __getattribute__ de su padre ")

print("Fin--------------------------------------------------------------------\n")

print("\nInicio:----------------------------------------------------------------")
print(f"""Llamada implícita de __len__ desde  MiClase:padre Meta a un
        método especial __len__ sobrescrito
        [len(MiClase)] """)
print(f"Resultado: {len(MiClase)} es el __len__ de Meta sobrescrito")

print(f"""\nLlamada Explicita de __len__ desde  MiClase:padre Meta a un
        método especial __len__ sobrescrito, Pero a su vez estoy llamando Implícitamente
        de __getattribute__ de (Meta) al mismo método especial __len__
        [MiClase.__len__(obj)], Ojo se utilizo notación de punto y se llamo a
        __getattribute__ de Meta   \n""")
print(f"""Resultado: {MiClase.__len__(obj)} es el __len__ de la Propia clase 

\nse usará el __getattribute__ de la metaclase para buscar el método __len__. 
Por orden de prioridad, se usará el __len__ de la clase ya que se busca primero
en el diccionario del Propio objeto. """)
print("Fin--------------------------------------------------------------------\n")

print("\nInicio:----------------------------------------------------------------")
print("""\nEn las lineas anteriores se hicieron llamadas
    Implícitas a __len__ desde el obj,MiClase
    Explicitas a __len__ desde obj,Miclase
    Implícitas a__getattribute__ desde obj,Miclase
    Ahora vamos hacer llamadas Explicitas a __getattribute__""")

print(f"""\nLlamada Explicita desde obj : padre  MiClase
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_obj =obj.__getattribute__("__len__")]
        Aquí ocurren varias cosas:
        * Implícitamente, el operador ‘.‘ accede directamente al método __getattribute__, 
        aplicando las optimizaciones.Por esto attr = __getattribute__
        * Se invoca explícitamente a __getattribute__ para que retorne el valor del "atributo" """)
        
funcion_len_obj =obj.__getattribute__("__len__")
print(f"""\n 2. [funcion_len_obj]
        {funcion_len_obj}
\n 3. [funcion_len_obj()])
        {funcion_len_obj()}\n""") 
    
print(f"""\nLlamada Explicita desde MiClase : padre  Meta
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_Miclase =MiClase.__getattribute__(obj,"__len__")]
        """)

funcion_len_Miclase =MiClase.__getattribute__(obj,"__len__")
print(f"""\n 2. [funcion_len_Miclase]
        {funcion_len_Miclase}
\n 3. [funcion_len_Miclase()])
        {funcion_len_Miclase()}\n""") 
        

print(f"""\nLlamada Explicita desde Meta : padre  Type
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_Meta =type(MiClase).__getattribute__(MiClase,"__len__")]
        """)

funcion_len_Meta =type(MiClase).__getattribute__(MiClase,"__len__")
print(f"""\n 2. [funcion_len_Miclase]
        {funcion_len_Meta}
\n 3. [funcion_len_Miclase()])
        {funcion_len_Meta(MiClase)}\n""") 
"""
IInicio:----------------------------------------------------------------
Llamada implícita de __len__ desde  obj:padre MiClase a un
        método especial __len__ sobrescrito
        [len(obj)] 

Ejecutando...len desde MiClase........... 
Resultado: 40 len de su Padre MiClase
Llamada explicita de __len__ desde  obj:padre MiClase a un
        método especial __len__ sobrescrito, Pero a su vez es una llamada implícita a 
        __getattribute__ de Miclase
        como no existe len en su diccionario, toca hacer [obj.__len__=lambda:100]
        y luego si ejecutar [obj.__len__()], como se esta accediendo con la notación de punto
        sale un poco distinto a la llamada implícita por que se llama __getattribute__ de
        de MiClase
        

Estas accediendo  a el método especial sobrescrito 
        __getattribute__ de MiClase:
        __getattribute__(self, attr)
        value=super().__getattribute__(attr)
        self :<__main__.MiClase object at 0x10bbfeeb0>
        attr:__len__
        value: <function <lambda> at 0x10bb54310>
Resultado: 100 len propio objeto por medio de __getattribute__ de su padre 
Fin--------------------------------------------------------------------


Inicio:----------------------------------------------------------------
Llamada implícita de __len__ desde  MiClase:padre Meta a un
        método especial __len__ sobrescrito
        [len(MiClase)] 

Ejecutando...len desde Meta...........
Resultado: 86000 es el __len__ de Meta sobrescrito

Llamada Explicita de __len__ desde  MiClase:padre Meta a un
        método especial __len__ sobrescrito, Pero a su vez estoy llamando Implícitamente
        de __getattribute__ de (Meta) al mismo método especial __len__
        [MiClase.__len__(obj)], Ojo se utilizo notación de punto y se llamo a
        __getattribute__ de Meta   


Estas accediendo a el método especial sobrescrito 
        __getattribute__ de Metaclase :
        __getattr__(cls,attr):
        value = super().__getattr__(attr)
        self :<class '__main__.MiClase'>
        attr:__len__
        value: <function MiClase.__len__ at 0x10bbf0c10>

Ejecutando...len desde MiClase........... 
Resultado: 40 es el __len__ de la Propia clase 


se usará el __getattribute__ de la metaclase para buscar el método __len__. 
Por orden de prioridad, se usará el __len__ de la clase ya que se busca primero
en el diccionario del Propio objeto. 
Fin--------------------------------------------------------------------


Inicio:----------------------------------------------------------------

En las lineas anteriores se hicieron llamadas
    Implícitas a __len__ desde el obj,MiClase
    Explicitas a __len__ desde obj,Miclase
    Implícitas a__getattribute__ desde obj,Miclase
    Ahora vamos hacer llamadas Explicitas a __getattribute__

Llamada Explicita desde obj : padre  MiClase
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_obj =obj.__getattribute__("__len__")]
        Aquí ocurren varias cosas:
        * Implícitamente, el operador ‘.‘ accede directamente al método __getattribute__, 
        aplicando las optimizaciones.Por esto attr = __getattribute__
        * Se invoca explícitamente a __getattribute__ para que retorne el valor del "atributo" 

Estas accediendo  a el método especial sobrescrito 
        __getattribute__ de MiClase:
        __getattribute__(self, attr)
        value=super().__getattribute__(attr)
        self :<__main__.MiClase object at 0x10bbfeeb0>
        attr:__getattribute__
        value: <bound method MiClase.__getattribute__ of <__main__.MiClase object at 0x10bbfeeb0>>

Estas accediendo  a el método especial sobrescrito 
        __getattribute__ de MiClase:
        __getattribute__(self, attr)
        value=super().__getattribute__(attr)
        self :<__main__.MiClase object at 0x10bbfeeb0>
        attr:__len__
        value: <function <lambda> at 0x10bb54310>

 2. [funcion_len_obj]
        <function <lambda> at 0x10bb54310>

 3. [funcion_len_obj()])
        100


Llamada Explicita desde MiClase : padre  Meta
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_Miclase =MiClase.__getattribute__(obj,"__len__")]
        

Estas accediendo a el método especial sobrescrito 
        __getattribute__ de Metaclase :
        __getattr__(cls,attr):
        value = super().__getattr__(attr)
        self :<class '__main__.MiClase'>
        attr:__getattribute__
        value: <function MiClase.__getattribute__ at 0x10bbf0b80>

Estas accediendo  a el método especial sobrescrito 
        __getattribute__ de MiClase:
        __getattribute__(self, attr)
        value=super().__getattribute__(attr)
        self :<__main__.MiClase object at 0x10bbfeeb0>
        attr:__len__
        value: <function <lambda> at 0x10bb54310>

 2. [funcion_len_Miclase]
        <function <lambda> at 0x10bb54310>

 3. [funcion_len_Miclase()])
        100


Llamada Explicita desde Meta : padre  Type
        a método __getattribute__ para recuperar el valor __len__
        1.[funcion_len_Meta =type(MiClase).__getattribute__(MiClase,"__len__")]
        

Estas accediendo a el método especial sobrescrito 
        __getattribute__ de Metaclase :
        __getattr__(cls,attr):
        value = super().__getattr__(attr)
        self :<class '__main__.MiClase'>
        attr:__len__
        value: <function MiClase.__len__ at 0x10bbf0c10>

Ejecutando...len desde MiClase........... 

 2. [funcion_len_Miclase]
        <function MiClase.__len__ at 0x10bbf0c10>

 3. [funcion_len_Miclase()])
        40
"""