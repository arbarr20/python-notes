# Decoradores 4
#Plantilla General de como usar decoradores simples
# Arbarr20

from functools import wraps
def nombre_decorador(f): #(1)
    @wraps(f) #(2)
    def decorada(*args, **kwargs):#(5)
        print(f"args:{args}, kwargs: {kwargs}")#(6)
        if not can_run: # si can_run es falso#(7)
            return "La función no se ejecutará"#(8)
        return f(*args, **kwargs)#(9)
    return decorada#(3)

# primero se ejecuta el @nonbre_decorador
@nombre_decorador
def func():
    return("La función se esta ejecutando")

can_run = True
# En este momento es cuando se llama a decorada
print(func()) # (4)
# Salida: La función se esta ejecutando

can_run = False
print(func())
# Salida: La función no se ejecutará