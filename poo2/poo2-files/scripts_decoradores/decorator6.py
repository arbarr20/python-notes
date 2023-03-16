# Decoradores 6
#Cascading Decorators
# Arbarr20
from functools import wraps

def logit(logfile='./out.log'):

    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):            
            log_string = func.__name__ + " fue llamada"
            print(log_string)
            # Abre el fichero y añade su contenido
            with open(logfile, 'a') as opened_file:
                # Escribimos en el fichero el contenido
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit() # cuando llega a este punto se ejecuta logit -> logit() retorna logging_decorator
#myfunc1 = logit() -> myfunc1 = logging_decorator

def myfunc1(): # esto se traduce como myfunc1 = logging_decorator(func=(myfunc1))  y retorna wrapped_function
    pass

myfunc1()  # se traduce como wrapped_function(*args, **kwargs)
# Salida: myfunc1 fue llamada
# Se ha creado un fichero con el nombre por defecto (out.log)#

@logit(logfile='./func2.log') # ejecuta logit()
# esta definición ejecuta el retorno de logit() myfunc2()-> esos paréntesis ejecutan logging_decorator = logging_decorator()
# retorna wrapped_function
def myfunc2():
    pass

# aquí es donde realmente se ejecuta el decorador o se inyecta la nueva funcionalidad y se ejecuta el contenido real de la función
#myfunc2() -> myfunc2 = wrapped_function()
myfunc2() 
# Salida: myfunc2  fue llamada
# Se crea un fichero func2.log