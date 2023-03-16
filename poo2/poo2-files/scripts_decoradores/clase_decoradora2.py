# Archivo: clase_decoradora2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 29/01/2023
# Descripción: Clases que decoran Funciones, no se usa __call__ en este ejemplo
# un ejemplo de como flask implementa el decorador route y una reglas

class Flask:
    """
    Clase Flask que se encarga de manejar las reglas de una aplicación web.
    """

    def __init__(self):
        self.rules = []

    def route(self, route, methods=["GET"]):
        """
        Decorador para funciones que especifica la ruta y los métodos HTTP permitidos
        para una función. Al ser llamada con una función como argumento, devuelve una
        función decorada que crea una instancia de la clase Rule y la guarda en una lista
        de reglas.
        """

        def decorator(f):
            rule = Rule(route, f, methods)
            self.rules.append(rule)
            return f

        return decorator


class Rule:
    """
    Clase Rule que representa una regla de una aplicación web.
    """

    def __init__(self, route, f, methods):
        """
        Inicializador de la clase Rule.
        Recibe como argumentos:
            route (str): la ruta a la que se aplica la regla.
            f (function): la función de controlador asociada a la regla.
            methods (list): los métodos HTTP permitidos para la regla.
        """
        self.route = route
        self.f = f
        self.methods = methods

    def match(self, request):
        """
        Método que determina si la regla se aplica a una solicitud dada.
        Recibe como argumento:
            request (objeto): la solicitud a comparar con la ruta y los métodos HTTP permitidos.
        """
        pass

    def handle(self, request):
        """
        Método que ejecuta la función de controlador asociada a la regla si se determina
        que la regla se aplica a una solicitud dada.
        Recibe como argumento:
            request (objeto): la solicitud a comparar con la ruta y los métodos HTTP permitidos.
        """
        pass


app = Flask()


@app.route("/")
def index():
    """
    Función que maneja la ruta raíz de la aplicación.
    """
    return "Hello, World!"


@app.route("/about", methods=["GET", "POST"])
def about():
    """
    Función que maneja la ruta '/about' de la aplicación con los métodos GET y POST permitidos.
    """
    return "About me"


print(index())
print(about())
