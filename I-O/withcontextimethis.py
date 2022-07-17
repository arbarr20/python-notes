import sys
"""
Para que en realidad entienda como es que trabaja @contextmanager
debe analizar la clase GeneratorContextManager, la funcion def contextmanager(func)
y logicamente inplemtentar su fucnonamiento.

Ejeccute paso a paso y  onserve sus compartamientos.
"""

class GeneratorContextManager(object):

    def __init__(self, gen):
        self.gen = gen # = def funcion_decorada(parametro funcion decorada)    
        # retorna a return GeneratorContextManager(func(*args, **kwds))   

    def __enter__(self):
        try:
            #inicicaliza el generador (como no es llamado por un for se usa next)
            #ejecuta funcion_decorada(parametro funcion decorada)
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator didn't yield")

    def __exit__(self, type, value, traceback):
        if type is None: #aqui retorna despues del yiel de funcion_decorada
            try:
                next(self.gen) # depues del yiel de la funcion generadora
            except StopIteration:
                return # se termino el generador se cierra el generador funcion_decorada
            else:
                raise RuntimeError("generator didn't stop")
        else:
            try:
                self.gen.throw(type, value, traceback)
                raise RuntimeError("generator didn't stop after throw()")
            except StopIteration:
                return True
            except:
                # solo vuelve a subir si * no * es la excepción que fue
                # pasado a throw (), porque __exit __ () no debe subir
                # una excepción a menos que __exit __ () fallara. Pero
                # throw () tiene que generar la excepción para señalar
                # propagación, por lo que esto corrige el desajuste de impedancia
                # entre el protocolo throw () y __exit __ ()
                # protocolo.
                #
                if sys.exc_info()[1] is not value:
                    raise


def contextmanager(func):
    def helper(*args, **kwds):
        # los args y kwarg son los argumentos de  funcion decorada
        print(f"args: {args} kwargs: {kwds}")
        return GeneratorContextManager(func(*args, **kwds))
    return helper

# Funcion a la que implementaremos la funcionalidad
#funcion_decorada =contextmanager(funcion_decorada) esto es lo que hace el decorador
#@contextmanager # descomente para usar con with
def funcion_decorada(f = "None"):
        print("antes")  
        try:                 
            yield
            print(f) 
            
        finally:
            print("despues")

########################################################################################
#                            Analizando Comportamientos                                #
########################################################################################


#funcion_decorada("parametro funcion decorada") esto solo es de muestra es lo que hace with en su primera ejecución
#with funcion_decorada("parametro funcion decorada"):
    #print("dentro del contexto with")


"""
# La siguiente es una forma analoga de hacerlo SIN EL WITH
# para entender como funciona el with
funcion_decorada =contextmanager(funcion_decorada):def contextmanager(func)->helper 
VAR = funcion_decorada('parametro funcion decorada'):helper()-> init GeneratorContextManager
VAR.__enter__()=return next(self.gen): ejecuta lo que esta antes del yield de funcion_decorada
--- ejecucion de mi contexto =  print("dentro del contexto with")
VAR.__exit__(None,None,None)=next(self.gen): ejecuta lo que esta despues del yield -- print("despues") termina generador
como ya se termino el genrador ingresa al StopIteration y termina el programa
"""
funcion_decorada =contextmanager(funcion_decorada) # esto es analogo al decorador
VAR = funcion_decorada('parametro funcion decorada') # primera ejecucion del with
VAR.__enter__()# segunda ejecucion del with
try:
    print("dentro del contexto with") # lo que estaria dentro del with: tercera ejecucion del with
finally:
    VAR.__exit__(None,None,None)# cuarta ejecucion del with


"""
Unas conclusiones:

1.- el with ejecula la funcion que sigue despues de su ejecucion (debe ser un generador)
with funcion_decorada("parametro funcion decorada"), en este caso funcion_decorada("parametro funcion decorada")
2- with espera que esta fucion implemente o llame interna mente una clase  o algo que cotenga el metodo __enter__
3- ejecuta lo  que contenga el __enter__ que en realidad es el generador (lo que este antes del yield)
4- cuando se llega al yiel de la funcion genradora este retorna la ejecucion al with de nuevo, ejecutando
lo que tengamos dentro del with, en este caso "print("dentro del contexto with")"
5-retorna a la funcion generadora ejecutando lo que este despues del yield. apenas temina lo que esta despues
del yield, por la naturaleza del genrador, el generador genra un "StopIteration"
6- despues de que se ejecuta lo que esta despues del yield se ejecuta el metodo __exit__, esto conlleva
a llamar un nuevo "next(self.gen)" pero esto no sucede por que el generador ya termino y se captura un "StopIteration"
dentro de la clase "class GeneratorContextManager(object)" terminando la ejecucion del programa
"""

