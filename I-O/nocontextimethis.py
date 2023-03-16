import sys
"""
lo que se trata de mostrar en este escrip es como en realidad de implenta 
el administrador de contexto con generadores.

su Ojetivo principal es entender 
el timethis.py en su metodo "def timethis(what):"

Recomiendo que primero vea y analice el script withcontextimethis.py y luego regrese a 
este script
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
                # entre el metodo throw () y  metodo __exit __ ()
            #
                #
                if sys.exc_info()[1] is not value:
                    raise


def contextmanager(func):
    def helper(*args, **kwds):
        # los args y kwarg son los argumentos de  funcion decorada         
        print(f"args: {args} kwargs: {kwds}")
        return GeneratorContextManager(func(*args, **kwds))
    return helper


def funcion_nocontex(f):
    #funcion_decorada =contextmanager(funcion_decorada)
    #funcion_decorada(soy la funcon)
    @contextmanager
    def funcion_decorada(x):
            print("antes")  
            try:      
                yield
                print(f)
                print(x)
            finally:
                print("despues")
    # en esta linea esta el truco para convertir a funcion_nocontex(f)
    # en un contextmanager, funcion_decorada()  en realidad es la ejecucion 
    # de def helper(*args, **kwds) este return retorna in obj de 
    return funcion_decorada("parametro funcion decorada") 
"""
# por que es que la siguente instruccion  funciona?

with funcion_nocontex("parametro funcion decorada"):
    print("dentro del contexto with")

# si funcion_nocontex no esta especificada asi:

@contextmanager
    def funcion_nocontex(f):
        ....

por que se ejecuta sin problemas?
1. que es lo que en realidad hace with:
en su primera ejecucion lo
2. return funcion_decorada() es la clave

with1: 
- en su primera ejecucion ejecuta def funcion_nocontex(f):
    esto va al decorador  @contextmanager y retorna el helper, gracias al 
    return funcion_decorada()  se ejecuta el init de GeneratorContextManager 
    y retorna de nuevo al with2
- segunda ejecucion (depues del init de Generator..): esto va al __enter__ de la clase GeneratorContextManager y 
    ejecuta el generador con next, y ejecuta lo que esta antes del yield, cuando llega 
    al yield, retorna de nuevo al with3
- tercera ejecucion (depues que  encuantra el yield):esto va al __exit__ de la clase GeneratorContextManager y 
    ejecuta el generador con next, y ejecuta lo que esta despues del yield, cuando llega 
    al final de estas lineas procede al bloque finally (donde termina el generador), retorna de nuevo al al __exit__
    seguidamente se ejecuta el StopIteration ya que el genrador termino etorna de nuevo al with4
- cuarta ejecucion (depues de StopIteration): termina el programa
"""
with funcion_nocontex("parametro uncion_nocontex"):
    print("dentro del contexto with")
