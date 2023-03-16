# Archivo: ventajas_descriptors_on_propertys1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/02/2023
# Descripción: ventajas de los descriptores sobre las property


class NonNegative(object):
    """Un descriptor que prohíbe los valores negativos."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # llegamos aquí cuando alguien llama a x.d, y d es una instancia no negativa
        # instance = x
        # owner = type(x)
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # llegamos aquí cuando alguien llama x.d = val, y d es una instancia No Negativa
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Valor negativo no permitido: %s" % value)
        instance.__dict__[self.name] = value


class Movie(list):

    # siempre ponga descriptores a nivel de clase
    rating = NonNegative()
    runtime = NonNegative()
    budget = NonNegative()
    gross = NonNegative()

    def __init__(self, title, rating=0, runtime=0, budget=0, gross=0):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


m = Movie("Casablanca", 97, 102, 964000, 1300000)
print(m.budget)  # llama Movie.budget.__get__(m, Movie)
m.rating = 100  # llama Movie.budget.__set__(m, 100)
try:
    m.rating = -1  # llama Movie.budget.__set__(m, -100)
except ValueError:
    print("Woops, valor negativo")
