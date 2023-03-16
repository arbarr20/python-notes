def buenos_dias ():
    """
    esta es la función buenos Dias, y se va a decorar
    """
    print ("buenos Dias")
    
def buenas_noches ():
    """
    esta es la función buenas noches, y se va a decorar
    """
    print ("buenas noches")

def  decorador (funcion_decorada):
    """
    función decoradora, recibe como parámetro una funciones
    """
    print ("dentro la funcion_decorada")
    def funcion_envolvente():
        """esta es la funcion envolvente, la que normalmente inyecta la nueva funcionalidad
            a la funcion decorada
        """
        print ("Función envolvente: Programadores") #implementacion que inyecta el decorador
        print ("ejecutando la funcion decorada dentro la funcion envolvente")
        funcion_decorada()# aquí se ejecuta la función decorada buenos_dias()
    return funcion_envolvente # no lleva los ()
    

buenos_dias()
#buenos Dias

#primera forma de llamar el decorador rudimentariamente
decorador(buenos_dias)() # el () ejecuta el retorno de (decorador), y a que este no tiene () en su retorno 
"""
buenos Dias
dentro la funcion_decorada
Función envolvente: Programadores
ejecutando la funcion decorada dentro la funcion envolvente
buenos Dias
"""
print (f".__name__ = {buenas_noches.__name__}")
print (f".__doc__ = {buenas_noches.__doc__}")
print (f".__dict__ = {buenas_noches.__dict__}")

"""
.__name__ = buenas_noches
.__doc__ = 
    esta es la función buenas noches, y se va a decorar
    
.__dict__ = {}
"""
buenas_noches()
#buenas noches

#segunda forma de llamar el decorador rudimentariamente
buenas_noches = decorador(buenas_noches)
buenas_noches()
"""
buenas noches
dentro la funcion_decorada
Función envolvente: Programadores
ejecutando la funcion decorada dentro la funcion envolvente
buenas noches
"""

print (f".__name__ = {buenas_noches.__name__}")
print (f".__doc__ = {buenas_noches.__doc__}")
print (f".__dict__ = {buenas_noches.__dict__}")
"""
.__name__ = funcion_envolvente
.__doc__ = esta es la funcion envolvente, la que normalmente inyecta la nueva funcionalidad
            a la funcion decorada
        
.__dict__ = {}
"""