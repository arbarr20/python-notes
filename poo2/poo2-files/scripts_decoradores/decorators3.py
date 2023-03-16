from functools import wraps

def  decorador (funcion_decorada):
    """
    función decoradora, recibe como parámetro una funciones
    """
    print ("dentro la funcion_decorada")

    @wraps(funcion_decorada)
    def funcion_envolvente():
        """esta es la funcion envolvente, la que normalmente inyecta la nueva funcionalidad
            a la funcion decorada
        """
        print ("Función envolvente: Programadores") #implementacion que inyecta el decorador
        print ("ejecutando la funcion decorada dentro la funcion envolvente")
        funcion_decorada()# aquí se ejecuta la función decorada buenos_dias()
    return funcion_envolvente # no lleva los ()

def buenos_dias ():
    """
    esta es la función buenos Dias, y se va a decorar
    """
    print ("buenos Dias")


@decorador 
def buenas_noches ():
    """
    esta es la función buenas noches, y se va a decorar
    """
    print ("buenas noches")

buenas_noches() # se ejecuta buenas noches con el decorador

print (f".__name__ = {buenas_noches.__name__}")
print (f".__doc__ = {buenas_noches.__doc__}")
print (f".__dict__ = {buenas_noches.__dict__}")
"""
__name__ = buenas_noches
.__doc__ = 
    esta es la función buenas noches, y se va a decorar
    
.__dict__ = {'__wrapped__': <function buenas_noches at 0x108bf9c10>}}
"""



