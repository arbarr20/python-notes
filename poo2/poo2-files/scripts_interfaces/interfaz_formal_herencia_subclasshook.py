# Archivo: interfaz_formal_herencia_subclasshook.py
# Autor: Arbarr20 y ayuda online
# Fecha: 07/03/2023
# Descripción: Interfaces formales en python, se muestra la forma correcta de diseñar he
# implementar una interface en python

'''
El script define una interfaz abstracta Database que tiene dos métodos abstractos: connect y
execute. Tres clases, CommandLineDatabase, DesktopDatabase y WebDatabase, implementan esta interfaz.
Cada una de estas clases proporciona una implementación concreta de los métodos connect y execute
para una base de datos específica. Además, hay una función execute_database_query que toma un
objeto Database y una consulta, y llama a los métodos connect y execute de ese objeto para ejecutar
la consulta en la base de datos. Finalmente, se crean tres instancias de las clases
CommandLineDatabase, DesktopDatabase y Además, se definen tres clases que implementan la interfaz
Database: CommandLineDatabase, DesktopDatabase y WebDatabase. Cada una de estas clases implementa
los métodos abstractos connect y execute de la interfaz.

Finalmente, se define una función execute_database_query que toma un objeto Database y una consulta
query, y llama a los métodos connect y execute en el objeto Database.

En el ejemplo de uso al final del script, se crean objetos de cada una de las tres clases y se
llama a la función execute_database_query con cada objeto y una consulta de ejemplo.

La documentación de Sphinx se encarga de describir en detalle la interfaz Database y cada uno de
sus métodos, así como las clases que la implementan y cómo utilizarlas. También se incluyen
ejemplos de uso en la documentación.

'''

import abc


class Database(abc.ABC):
    """
    Interface para un objeto de base de datos que puede ser utilizado por diferentes tipos de
    clientes.

    Esta clase define dos métodos abstractos: connect y execute. Los clientes deben implementar
    estos métodos.
    """

    @abc.abstractmethod
    def connect(self) -> None:
        """
        Método abstracto para conectar con la base de datos.

        Los clientes deben implementar este método.
        """
        pass

    @abc.abstractmethod
    def execute(self, query: str) -> None:
        """
        Método abstracto para ejecutar una consulta en la base de datos.

        :param query: La consulta a ejecutar.
        :type query: str
        """
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Implementa el método abstracto __subclasshook__ del módulo abc.

        Verifica si la subclase proporcionada cumple con los requisitos para ser considerada una
        subclase de la clase base Database.

        Parámetros:
        -----------
        cls: tipo
            El objeto de clase que se está comprobando, en este caso Database.
        subclass: tipo
            La subclase que se está comprobando para determinar si es una subclase de Database.

        Retorna:
        --------
        True si subclass es una subclase de Database, False en caso contrario.

        """
        if cls is Database:
            if (hasattr(subclass, 'connect') and callable(subclass.connect) and
                    hasattr(subclass, 'execute') and callable(subclass.execute)):
                return True
        return NotImplemented


class CommandLineDatabase(Database):
    """
    Implementación de la interfaz Database para una base de datos de línea de comandos.
    """

    def connect(self) -> None:
        print("Connecting to command line database")

    def execute(self, query: str) -> None:
        print(f"Executing query '{query}' on command line database")


class DesktopDatabase(Database):
    """
    Implementación de la interfaz Database para una base de datos de escritorio.
    """

    def connect(self) -> None:
        print("Connecting to desktop database")

    def execute(self, query: str) -> None:
        print(f"Executing query '{query}' on desktop database")

# Aquí hacemosl uso de subclasshook, ya que no usamos herencia


class WebDatabase():
    """
    Implementación de la interfaz Database para una base de datos web.
    """

    def connect(self) -> None:
        print("Connecting to web database")

    def execute(self, query: str) -> None:
        print(f"Executing query '{query}' on web database")


def execute_database_query(database: Database, query: str) -> None:
    """
    Función que conecta a una base de datos y ejecuta una consulta.

    :param database: Objeto de la base de datos a utilizar.
    :type database: Database
    :param query: La consulta a ejecutar.
    :type query: str
    """
    database.connect()
    database.execute(query)


cli_database = CommandLineDatabase()
desktop_database = DesktopDatabase()
web_database = WebDatabase()

execute_database_query(cli_database, "SELECT * FROM users")
execute_database_query(desktop_database, "SELECT * FROM users")
execute_database_query(web_database, "SELECT * FROM users")
