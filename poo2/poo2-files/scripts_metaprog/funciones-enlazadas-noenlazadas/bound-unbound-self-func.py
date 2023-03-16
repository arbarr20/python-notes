# Archivo: bound-unbound-self-func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 09/02/2023
# Descripción: __self__ y __func__ de los métodos enlazados, los No enlazados no tiene estos
# atributos

"""
Conceptos previos:

* __self__: es un atributo de un método en Python que contiene una referencia al objeto al que está
  vinculado el método. Por lo general, __self__ se utiliza internamente por Python para implementar
  la mecánica de los métodos de clase y de instancia. Es decir, es parte de la mecánica de
  descripción de los métodos de clase y de instancia en Python.

  No es recomendable acceder a __self__ directamente en tu código, ya que es una parte interna de la
  implementación de Python y su comportamiento puede cambiar en versiones futuras.

    class MyClass:
        def __init__(self, x):
            self.x = x

        def my_method(self, y):
            return self.x + y

    obj = MyClass(10)
    print(obj) # <__main__.MyClass object at 0x10d9673d0>
    print(obj.my_method.__self__) # <__main__.MyClass object at 0x10d9673d0>

    if '__self__' in dir(obj.my_method):
    print(f'\nmy_method es bounded tiene un {dir(obj.my_method)[-5]}\
    =: {obj.my_method.__self__} ')
    # my_method es bounded tiene un __self__ =: <__main__.MyClass object at 0x10cf02710>

    if '__self__' not in dir(MyClass.__dict__['my_method']):
        print('my_method  No es bounded No tiene un __self__')
    # my_method  No es bounded No tiene un __self__

* __func__: es una referencia a la función real que está asociada con el método.
  - __func__ es una característica SOLO de los métodos enlazados

  teniendo en cuenta lo dicho en este link,(https://github.com/arbarr20/python-notes/wiki/8.2.
  1-Metaprogramaci%C3%B3n#m%C3%A9todos-enlazados-y-m%C3%A9todos-no-enlazados, __func__ es una
  FUNCIÓN a  secas, que se ENLAZA a otra función llamada método por medio de un objeto y como
  resultado es un   método enlazado. esto funciona asi:

        class MyClass:
            def __init__(self, x):
                self.x = x

            def my_method(self, y):
                return self.x + y


        obj = MyClass(10)

        print(f'\nobj.my_method=método enlazado = {type(obj.my_method)}')
        print(f'Atributo __func__ de my_method = Función: {type(obj.my_method.__func__)}')

        función_del_obj = obj.my_method.__func__
        print(f'\nla función enlazada el objeto es: {función_del_obj}')
        # función_del_obj(obj,10) = my_method(self, y)
        print(f'ejecutemos la función del objeto: {función_del_obj(obj,10)}')

        if '__func__' in dir(obj.my_method):
            print('\nmy_method es bounded tiene un __func__')
        # my_method es bounded tiene un __func__

        if '__func__' not in dir(MyClass.__dict__['my_method']):
            print('my_method  No es bounded No tiene un __func__')
        # my_method  No es bounded No tiene un __func__

"""
# Después de los conceptos previos ahora si el script:


def my_func():
    """Esta función imprime un mensaje en consola."""
    print("esta es my_func")


class Persona:
    def __init__(self, nombre: str, fecha_nacimiento: str):
        """Constructor de la clase Persona.

        Args:
            nombre (str): Nombre de la persona.
            fecha_nacimiento (str): Fecha de nacimiento de la persona.
        """
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def datos(self) -> None:
        """Imprime en consola los datos de la persona."""
        print(
            f"los datos de esa persona son son : {self.nombre}:{self.fecha_nacimiento}"
        )


# Creación de un objeto de la clase Persona
per = Persona("arbarr", "01/01/19980")

print(
    f"""diccionario de Persona:
            {Persona.__dict__}"""
)
print(
    f"""\nMétodo enlazado Bounded (método) per.datos:
        El acceso punteado desde una instancia (per.datos)llama a __get__ ()
        que devuelve la función enlazada en un objeto (es la dirección de per)
        de método enlazado
        {per.datos} """
)
print(
    f"""\nInternamente, el método enlazado almacena la función subyacente (per.datos.__func__)
            {per.datos.__func__}
        -> y  la instancia vinculada al Método per.datos.__self__:
            {per.datos.__self__}
        -> Que es lo mismo que hex(id(per)) per es un Objeto
            {hex(id(per))}"""
)
print(
    f"""\n Método no enlazado (unbounded) Función como Método Persona.__dict__["datos"]:
        {Persona.__dict__["datos"]} """
)
print(
    f"""\n Método no enlazado (unbounded) Función como Método Persona.datos :
        El acceso punteado desde una clase llama a __get __ () que solo devuelve
        la función subyacente sin cambios.
        {Persona.datos} """
)
