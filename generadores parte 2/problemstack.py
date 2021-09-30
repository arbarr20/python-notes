#problemasstack.py
#
# Algunos eejmplo del problema de call stac y su solucion con
#trampolines



# ------------------------------------------------------------
#           === call stack problem cuenta regresiva===
# ------------------------------------------------------------

# Descomente las linea y ejecute paso a paso y observe
#las llamadas a la pila
""" def countdown(start):
    print (start)
    if start == 0:
        return 0
    else:
        return countdown(start - 1)
countdown(5) """

# ------------------------------------------------------------
#   === call stack problem cuenta regresiva generador===
# ------------------------------------------------------------

# esta es la version de la cuenta regresiva, pero con generadores
# este metodo ahorra memoria, pero las llamadas a la pila
# siguen siendo un problema. ejecute paso a paso y observe
#como se debe llamar el generador
""" def countdown(start):   
    print(start)           
    if start == 0:
        #cuando se ejecuta la ultima llamada, 
        # CLAVE: ya no se retorna un generador, 
        # se Retora un VALOR
        yield 0
        
    else:
        #este yield retorna un generador No un valor
        yield countdown(start - 1)
        
c =countdown(4)
while True:
    c= next(c)
    if c == 0:
        print (f'valor final: {c}')
        break
    print(f'Retorno del generador: {c}') """


# ------------------------------------------------------------
#   === call stack problem cuenta regresiva generador
#        trampolin Solución al call stack===
# ------------------------------------------------------------
"""
La idea es que cada llamada recursiva sea "trampolíneada" fuera 
del corredor del trampolín (la la funcion trampolin en este caso).
Es decir, cada llamada recursiva se devuelve al trampolin y se rebota
en ella. 
"""
""" import types

def countdown(start):   
    print(start)           
    if start == 0:
        #cuando se ejecuta la ultima llamada, 
        # ESTA ES LA CLAVE ya no se retorna un generador, 
        # se Retora un VALOR
        yield 0
        
    else:
        #este yield retorna un generador No un valor
        yield countdown(start - 1)

        
def trampolin(gen, *args, **kwargs):
    g = gen(*args, **kwargs) 
    #mientra se retorne un generador desde countdown
    # se sobrescribe el genrador retornado a g y pide su proximo valor
    # con next  
    while isinstance(g, types.GeneratorType):
        g=next(g)    
    #Cuando se retorna el valor final de la "Recursion"
    # se retorna el VALOR            
    return g

# trampolineando a countdown
trampolin(countdown, 5) """ 
