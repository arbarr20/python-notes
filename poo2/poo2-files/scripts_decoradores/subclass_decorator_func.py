# Archivo: subclass_decorator_func.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/01/2023
# Descripción: Clases que Heredan de una Clase Decoradora

# Se define la clase "logit"
class logit(object):
    # Se define un atributo de clase "_logfile" con el valor "out.log"
    _logfile = 'out.log'

    # Se define el método "__init__" de la clase, que toma argumentos variables
    def __init__(self, *args, **kwargs):
        '''
        se pueden capturar los args y kwargs que son los argumentos del
        decorador y hacer algo con ellos

        def __init__(self,función):
            self.función = función

        # pero (@email_logit(función = otra función))
        en la linea anterior se podría añadir la funcionalidad de otra función
        externa que sea pasada como argumento del decorador, y este argumento
        de llama desde este constructor como una clave de kwargs y hacer algo
        con el.

        self:objeto email_logit
            dic-self {'email': 'admin@myproject.com'}
            args: ()
            kwargs {}
        '''
        # Se imprime información sobre el constructor y los argumentos
        # recibidos
        print(f""" logit:
            self:{self}
            dic-self {self.__dict__}
            args: {args}
            kwargs: {kwargs}
            self.email:{self.email}""")

    # Se define el método "__call__" de la clase, que se ejecutará cuando se
    # llame a una instancia de la clase
    def __call__(self, *args, **kwargs):
        '''
        * self: objeto de tipo email_logit
        * self__dict__:atributos del objeto, en este caso
            {'email': 'admin@myproject.com'}
        * args[0]:esta la función decorada myfunc1
        * kwargs: esta vació
        '''
        print(f""" __call__:
            self:{self}
            dic-self {self.__dict__}
            args: {args}
            kwargs: {kwargs}
            """)
        # Se obtiene el nombre de la función a la que se le ha aplicado
        # el decorador
        log_string = args[0].__name__ + " fue llamada"
        # Se imprime el nombre de la función
        print(log_string)
        # Se abre el archivo de log y se escribe el nombre de la función
        with open(self._logfile, 'a') as opened_file:
            # Escribimos el contenido
            opened_file.write(log_string + '\n')
        # Se llama al método "notify" de la clase
        self.notify()
        # Se llama al método "notifyy" de la clase
        self.notifyy()
        # Se obtiene la función original
        myfun = args[0]
        # Se devuelve la función original
        return myfun

    # Se define el método "notify", que imprime un mensaje
    def notify(self):
        print("notificación de logit escribir en el log")


# Se define la clase "email_logit", que hereda de "logit"
class email_logit(logit):
    '''
    Implementación de logit con envío de email
    '''
    # Se define el método "__init__" de la clase, que toma un argumento
    # opcional "email" y argumentos variables
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        '''
        self: es un objeto email.logit que se creo al llamar @email.logit()
        *args: lo que se pase como paramentos en el decorador @email.logit(2)
        **kwargs: lo que se pase como claves en el decorador
            (función = una_función)
        * super().__init__(*args(2), **kwargs({función:una_función}))
        '''
        # Se almacena la dirección de correo electrónico en el atributo "email"
        # de la clase
        self.email = email
        print(f""" email_logit:
            self:{self}
            dic-self {self.__dict__}
            args: {args}
            kwargs: {kwargs}
            self.email:{self.email}""")
        # Se llama al método "__init__" de la clase "logit" mediante
        # "super(email_logit, self).__init__(*args, **kwargs)"
        super(email_logit, self).__init__(*args, **kwargs)

    # Se define el método "notifyy", que no hace nada
    def notifyy(self):
        # Enviamos email a self.email
        # Código para enviar email
        # ...
        print(f"el email se se envió a {self.email}")


'''
Para entender como se ejecuta el decorador
los paréntesis son muy importantes aquí
@email_logit(): se puede sustituir de varias formas:

1. myfunc1 = email_logit()(myfunc1)
2. instance = email_logit() -- se crea la instancia
    instance(myfunc1)() ó
        myfunc1 = instance(myfunc1) - se llama la instancia (call)

'''


# Se aplica el decorador "email_logit" a la función "myfunc1"
# el primer parámetro es el correo, si no pones nada, se pone
# el parámetro por defecto del constructor de email_logit
@email_logit('arbarr.com', 'otro_arg', edad=78)
def myfunc1():
    # Se imprime un mensaje
    print("mensaje dentro del email")
# Se llama a la función "myfunc1", lo que ejecutará el decorador "email_logit"
# y la función original


myfunc1()
