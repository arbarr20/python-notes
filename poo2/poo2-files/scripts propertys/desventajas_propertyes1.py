# Archivo: desventajas_propertyes1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/02/2023
# Descripción: desventajas de las propertyes


class Movie:
    def __init__(
        self, title: str, rating: int, runtime: int, budget: float, gross: float
    ) -> None:
        """
        Constructor de la clase Movie.

        Parámetros:
        - title: Título de la película (str).
        - rating: Calificación de la película (int).
        - runtime: Duración de la película en minutos (int).
        - budget: Presupuesto de la película (float).
        - gross: Ingresos de la película (float).
        """
        self._rating = None
        self._runtime = None
        self._budget = None
        self._gross = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        self.budget = budget

    @property
    def budget(self) -> float:
        """
        Getter para el presupuesto de la película.

        Retorna:
        - El presupuesto de la película (float).
        """
        return self._budget

    @budget.setter
    def budget(self, value: float) -> None:
        """
        Setter para el presupuesto de la película.

        Parámetros:
        - value: Nuevo valor del presupuesto de la película (float).

        Lanza:
        - ValueError: Si el valor del presupuesto es negativo.
        """
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    @property
    def rating(self) -> int:
        """
        Getter para la calificación de la película.

        Retorna:
        - La calificación de la película (int).
        """
        return self._rating

    @rating.setter
    def rating(self, value: int) -> None:
        """
        Setter para la calificación de la película.

        Parámetros:
        - value: Nueva calificación de la película (int).

        Lanza:
        - ValueError: Si el valor de la calificación es negativo.
        """
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._rating = value

    @property
    def runtime(self) -> int:
        """
        Getter para la duración de la película.

        Retorna:
        - La duración de la película en minutos (int).
        """
        return self._runtime

    @runtime.setter
    def runtime(self, value: int) -> None:
        """
        Setter para la duración de la película.

        Parámetros:
        - value: Nueva duración de la película en minutos (int).

        Lanza:
        - ValueError: Si el valor de la duración es negativo.
        """
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._runtime = value

    @property
    def gross(self) -> float:
        """
        Getter para los ingresos de la película.

        Retorna:
        - Los ingresos de la película (float).
        """
        return self._gross

    @gross.setter
    def gross(self, value: float) -> None:
        """
        Setter para los ingresos de la película.

        Parámetros:
        - value: Nuevos ingresos de la película (float).

        Lanza:
        - ValueError: Si el valor de los ingresos es negativo.
        """
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._gross = value

    def profit(self):
        return self.gross - self.budget
    
m = Movie('Casablanca', 97, 102, 964000, 1300000)
print (m.budget)  # calls Movie.budget.__get__(m, Movie)
m.rating = 100  # calls Movie.budget.__set__(m, 100)
try:
    m.rating = -1   # calls Movie.budget.__set__(m, -100)
except ValueError:
    print ("Woops, negative value")
