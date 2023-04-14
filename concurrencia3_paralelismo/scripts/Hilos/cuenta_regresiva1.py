# Archivo: cuenta_regresiva1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 14/04/2023
# Descripción: Definir un Hilo en una clase. se muestra como ejecutar un Hilo en una clase

import threading
import logging
import time

'''
esta línea de código establece la configuración básica de registro para que cada mensaje de
registro incluya el nombre del hilo y el mensaje, y que se registren todos los mensajes con un
nivel de registro de DEBUG o superior.
'''
logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


class CountdownThread(threading.Thread):
    """
    Un hilo que cuenta hacia atrás desde un número entero hasta cero.

    Args:
        count (int): El número entero para contar hacia atrás desde.

    Attributes:
        count (int): El número entero para contar hacia atrás desde.

    Methods:
        run(self) -> None:
            El método principal del hilo. Cuenta hacia atrás desde el valor `count`
            hasta cero, imprimiendo un mensaje de registro en cada iteración.
            El método se ejecuta hasta que el contador llega a cero.
    """

    def __init__(self, count: int) -> None:
        """
        Inicializa una nueva instancia de CountdownThread.

        Args:
            count (int): El número entero para contar hacia atrás desde.
        """
        threading.Thread.__init__(self)
        self.count = count

    def run(self) -> None:
        """
        El método principal del hilo. Cuenta hacia atrás desde el valor `count`
        hasta cero, imprimiendo un mensaje de registro en cada iteración.
        El método se ejecuta hasta que el contador llega a cero.

        Returns:
            None
        """
        while self.count > 0:
            logging.info(f"Cuenta Regresiva, {self.count}")
            self.count -= 1
            time.sleep(1)
        return


if __name__ == '__main__':
    logging.info("Inicia la ejecución del programa")
    t1 = CountdownThread(5)
    t1.start()
    t2 = CountdownThread(10)
    t2.start()
    
