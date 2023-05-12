# Archivo: padre1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 09/05/2023
# Descripción: Un objeto mínimo que implementa un canal de mensajes sobre un par de descriptores de
# archivo (como un pipe)

"""
El script proporcionado define una clase Channel que se utiliza para enviar y recibir datos entre
dos procesos de Python. Esta clase se define utilizando dos flujos de archivos proporcionados en el
constructor: out_f y in_f, que representan los flujos de salida y entrada del proceso remoto.

La clase Channel proporciona dos métodos principales: send y recv. El método send toma un objeto
como argumento y lo serializa utilizando el módulo pickle, después envía los datos serializados al
proceso remoto a través del flujo de salida. El método recv espera a recibir un objeto del flujo de
entrada y lo deserializa utilizando el módulo pickle antes de devolverlo.

Además, el script principal crea un nuevo proceso utilizando subprocess.Popen() y crea una
instancia de la clase Channel utilizando los flujos de entrada y salida del proceso recién creado.
A continuación, se envían varios objetos utilizando el método send, y se registran las respuestas
recibidas utilizando el método recv.

El módulo logging se utiliza para registrar mensajes de depuración en la salida estándar.
En particular, se registran los mensajes de depuración que indican qué objetos se envían y reciben
a través del canal.

En resumen, este script proporciona una forma sencilla de comunicarse entre procesos utilizando
flujos de archivos y el módulo pickle.

En el contexto de programación, "flush" se refiere a la acción de limpiar o vaciar un búfer de
memoria y asegurarse de que todos los datos almacenados en él se han enviado o escrito en su
destino final. En el script proporcionado, la línea self.out_f.flush() se utiliza para asegurarse
de que todos los datos enviados a través del canal se han escrito en el flujo de salida (out_f)
antes de continuar. Sin esta llamada a flush(), es posible que algunos datos se queden en el búfer
sin ser enviados, lo que podría provocar comportamientos inesperados o errores en el programa.
"""

import pickle
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


class Channel(object):
    """
    Clase que representa un canal de comunicación entre dos procesos.
    """

    def __init__(self, out_f, in_f):
        """
        Constructor de la clase Channel.

        Parámetros:
        -----------
        out_f : file object
            Objeto que representa un archivo abierto en modo escritura, donde se escribirán los
            datos que se envíen por el canal.
        in_f : file object
            Objeto que representa un archivo abierto en modo lectura, de donde se leerán los datos
            que se reciban por el canal.
        """
        self.out_f = out_f
        self.in_f = in_f

    def send(self, item: object):
        """
        Método que envía un objeto por el canal.

        Parámetros:
        -----------
        item : object
            Objeto que se enviará por el canal.

        Raises:
        -------
        pickle.PicklingError:
            Si ocurre algún error durante la serialización del objeto.
        """
        pickle.dump(item, self.out_f)
        self.out_f.flush()

    def recv(self) -> object:
        """
        Método que recibe un objeto por el canal.

        Returns:
        --------
        object:
            Objeto recibido por el canal.

        Raises:
        -------
        EOFError:
            Si se alcanza el final del archivo de entrada antes de leer un objeto completo.
        pickle.UnpicklingError:
            Si ocurre algún error durante la deserialización del objeto.
        """
        return pickle.load(self.in_f)


if __name__ == '__main__':
    import subprocess
    p = subprocess.Popen(['python3', 'hijo1.py'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    ch = Channel(p.stdin, p.stdout)
    ch.send("Hello World")
    logging.debug(ch.recv())
    ch.send(42)
    logging.debug(ch.recv())
    ch.send([1, 2, 3, 4, 5])
    logging.debug(ch.recv())
    ch.send("fin de datos")
