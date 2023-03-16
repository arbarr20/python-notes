# Archivo: class_decorates_func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/01/2023
# Descripción: Clases que decoran funciones


# Se define la clase "logit"
class logit(object):
    # Se define un atributo de clase llamado "_logfile" con el valor "out.log"
    _logfile = 'out.log'

    # Se define el método "__init__" de la clase, que toma como argumento una
    # función, en este caso es la función que se decora
    def __init__(self, func):
        self.func = func

    # Se define el método "__call__" de la clase, que se ejecutará cuando
    # se llame a una instancia de la clase, la función que se decore actuará
    # como una instancia de esta clase, lo qu e significa que al ejecutar
    # myfunc1() se llamará a __call__
    def __call__(self, *args):
        # Se construye un string con el nombre de la función almacenada en
        # "func" y se imprime
        log_string = self.func.__name__ + " fue llamada"
        print(log_string)
        # # Se abre el archivo de log y se escribe el string
        with open(self._logfile, 'a') as opened_file:
            # Escribimos el contenido
            opened_file.write(log_string + '\n')
        # Enviamos una notificación (ver método)
        # Se llama al método "notify" de la clase
        # es un método que aun no esta implementado, pero podría enviar un
        # correo electrónico o hacer cualquier otra cosa
        self.notify()

        # Devuelve la función base
        return self.func(*args)

    # Se define el método "notify", que no hace nada
    def notify(self):
        # Aun no esta implementada
        pass


# Se cambia el valor del atributo de clase "_logfile" a "out2.log"
logit._logfile = 'out2.log'


# Se aplica el decorador "logit" a la función "myfunc1"
# se ejecuta logit solo se inicializan sus funciones no hace nada
# myfunc1 = logit(myfunc1)
@logit
# aquí se llama __init__ de logit (__init__(self, myfunc1))
def myfunc1():
    pass


# Se llama a la función "myfunc1", lo que ejecutará el decorador "logit"
# y la función original
# en cierta forma esta función es una instancia de logit, aquí se llama a call
# Output: myfunc1 fue llamada
myfunc1()
# Output: myfunc1 fue llamada
print(type(myfunc1))
# Se imprime el tipo de "myfunc1", que en este caso es
# <class '__main__.logit'> ya que myfunc1 es una instancia de logit
