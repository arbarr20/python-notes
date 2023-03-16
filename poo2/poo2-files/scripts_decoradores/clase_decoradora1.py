# Archivo: clase_decoradora1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/01/2023
# Descripción: Clases que decoran Funciones, no se usa __call__ en este ejemplo
# un ejemplo de como flask implementa el decorador route.

from functools import wraps

"""
La clase Flask se encarga de manejar las rutas de una aplicación web, tiene un método llamado route
que es un decorador para funciones, que al ser llamado con una función como argumento, devuelve una
función decorada que guarda la función original en un diccionario de rutas con la ruta especificada
como clave. El script crea una instancia de Flask llamada app, y define dos funciones index y about
decoradas con app.route("/") y app.route("/about"), respectivamente, estas funciones manejan las
rutas raíz y /about de la aplicación. Luego, llama a las dos funciones decoradas y las imprime.

"""


class Flask:
    """
    Clase Flask que se encarga de manejar las rutas de una aplicación web.
    """

    def __init__(self):
        self.routes = {}

    def route(self, route):
        """
        Decorador para funciones que especifica la ruta a la que esta asociada una función.
        Al ser llamada con una función como argumento, devuelve una función decorada que
        guarda la función original en un diccionario de rutas con la ruta especificada como clave.
        """

        def decorator(f):
            """
            Función decoradora que se encarga de llamar a la función original y retornar su valor.
            """

            @wraps(f)
            def wrapped(*args, **kwargs):
                """
                Función que se encarga de llamar a la función original y retornar su valor.
                """
                return f(*args, **kwargs)

            # Se guarda la función en el diccionario routes con la ruta como clave
            self.routes[route] = f
            return wrapped

        return decorator

# Se crea un objeto de la clase flask, por esto es que no se usa la función __call__
# dentro de la clase Flask
# observe que el decorador se realiza con el objeto, No con la clase.


app = Flask()


@app.route("/")
def index():
    """
    Función que maneja la ruta raíz de la aplicación.
    """
    return "Hello, World!"


@app.route("/about")
def about():
    """
    Función que maneja la ruta '/about' de la aplicación.
    """
    return "About me"


print(index())
print(about())
