# Archivo: bound-unbound-func-descript-metinstan-metclase-metestic.py
# Autor: Arbarr20 y ayuda online
# Fecha: 07/02/2023
# Descripción:Funciones como descriptores de No datos y su relación con  Métodos de instancia,
# Métodos estáticos y Métodos de clase 

'''
Un pequeño repaso antes de continuar con el script:

* método de instancia: aquellos que dentro de una clase llevan `self` como primer parámetro.

* método de clase : llevan como primer parámetro cls, puede ser accedido desde una instancia, o
  desde la propia clase
* método estático: no llevan ni `self`, ni `cls` como primer parámetro, no se necesita crear un
  objeto para acceder a ellos, se acceden A través del nombre de la clase.

* `types.MethodType(esta función, objeto al que se le va  vincular)`
  - obj.meth = func -> func es una Function
  - obj.meth = func.__get__(obj, MiClase) = es un método de instancia ya que lleva el (obj, ...)
     - agregue func al objeto (obj) que pertenece a la clase (MiClase), esto convierte a meth
       en un método de instancia.
    - si se quiere que sea estático , se debe poner obj.meth = func.__get__(None, MiClase), observe
      que el obj desaparecía,  y asi cumplimos lo que dice la teoría, de los métodos estáticos, que
      no llevan self ni cls.

    el resultado de func.__get__(obj, Miclase) retorna esto:
    - {'meth': <bound method func of <__main__.MiClase object at 0x1012afb80>>}:
           meth: corresponde a una función enlazada llamada func que pertenece a un objeto cuya
           dirección de memoria es 0x1012afb80 y pertenece a la clase MiClase
    el resultado de func.__get__(None, Miclase) retorna esto:
      - 'meth': <function func at 0x10dad6710>:
        meth: corresponde a una función no enlazada  que se encuentra dentro de la clase, por lo
        tanto se comporta como un método estático:

        def meth():
            return func ()

  - obj.meth = func.__get__(MiClase, type(MiClase)) = Método de clase = MiClase.meth = func
     - agregue func a la clase (MiClase) que pertenece a la metaclase (type(MiClase)),
       esto convierte a meth   en un atributo de clase, que prácticamente es lo  mismo que hacer
       MiClase.meth = func.
    el resultado de func.__get__(MiClase, type(MiClase) retorna esto:
         - {'meth': <bound method func of <class '__main__.MiClase'>>}:
           meth: corresponde a una función enlazada llamada func que pertenece a una CLASE
           llamada MiClase

  -  el siguiente método seria posiblemente como el __get__ de func, recibe la información:

            def __get__(self, obj, objtype=None):
                if obj is None:
                    return self
                return types.MethodType(self, obj)
'''


def func(*args, **kwargs):
    print(f"args:{args} kwargs:{kwargs}")


class MiClase:
    def __init__(self):
        pass


print("\ndireccion de func:", hex(id(func)))
obj = MiClase()

"""
las funciones son descriptores de no datos
entonces podemos añadirlas como atributos de clase de
forma dinámica
"""
print(
    "\nInico-------------------------------------------------------------------------"
)
# se crea un método de clase de forma dinámica
MiClase.metodo = func  
print(f"Diccionario de obj:{obj.__dict__}")
print(f"\nDiccionario de MiClase:{MiClase.__dict__}")
print(f"dirección de MiClase: {hex(id(MiClase))}")
print(f"dirección de obj: {hex(id(obj))}")
print(f"desde la clase MiClase.metodo: {hex(id(MiClase.metodo))}")
print(
    f"\nMiClase.metodo = func [obj.metodo] : {obj.metodo} dir obj.metodo: {hex(id(obj.metodo))}"
)
print(f"\nobj.metodo() :")
obj.metodo()
print(f"\nMiClase.metodo() :")
MiClase.metodo()
print(
    f"Fin----------------------------------------------------------------------------"
)
print(
    "\nInico-------------------------------------------------------------------------"
)

# se crea un método (No enlazado) de INSTANCIA de forma dinámica
# esto hace que meth se comporte como método estático
obj.meth = func
print(f"Diccionario de obj:{obj.__dict__}")
print(f"\nDiccionario de MiClase:{MiClase.__dict__}")
print(f"\nAsignándole descriptor a obj, No a MiClase obj.meth = func")

print(f"Dirección de obj.meth :{hex(id(obj.meth))}")
print(f"Dirección de obj :{hex(id(obj))}")
print(f"Ejecutando obj.meth : {obj.meth}")
print(f"\nEjecutando obj.meth()")
obj.meth()
print(f"\nejecutando la función func sola")
func()
print(
    "ejecutar func() es lo mismo que obj.meth que actua como METODO ESTATICO descriptores que no\
    estan enlazados a nada "
)
print(
    f"Fin----------------------------------------------------------------------------"
)
print(
    "\nInico3-------------------------------------------------------------------------"
)
# el método meth se enlaza a la instancia, esto permite que meth se comporte
# como metodo de instancia
obj.meth = func.__get__(None, MiClase)
print(f"Diccionario de obj:{obj.__dict__}")
print(f"\nDiccionario de MiClase:{MiClase.__dict__}")
print(
    f"""\nPara conseguir que el descriptor funcione como un método normal, 
    más de la clase MiClase necesitamos enlazarlo con la instancia:
    obj.meth=desc.__get__(obj, Cls) dinamicamente dentro de obj esta meth = descriptor func"""
)

print(f"Direccion de obj.meth :{hex(id(obj.meth))}")
print(f"Direccion de obj :{hex(id(obj))}")
print(f"Ejecutando obj.meth : {obj.meth}")
print(f"\nEjecutando obj.meth()")
obj.meth()

print(
    f"Fin----------------------------------------------------------------------------"
)

print(
    "\nInico-------------------------------------------------------------------------"
)
# el método meth se enlaza a la CLASE, esto permite que meth se comporte
# como metodo de CLASE
obj.meth = func.__get__(MiClase, type(MiClase))
print(f"Diccionario de obj:{obj.__dict__}")
print(f"\nDiccionario de MiClase:{MiClase.__dict__}")
print(
    """\nPodríamos enlazar el descriptor con la clase, pero
    vista como instancia, no como clase, con lo que obtenemos un “MÉTODO DE CLASE”:,
    obj.meth=func.__get__(MiClase,type(MiClase))"""
)

print(f"Dirección de obj.meth :{hex(id(obj.meth))}")
print(f"Dirección de obj :{hex(id(obj))}")
print(f"Ejecutando obj.meth : {obj.meth}")
print("\nEjecutando obj.meth()")
obj.meth()

print(
    "Fin----------------------------------------------------------------------------"
)
