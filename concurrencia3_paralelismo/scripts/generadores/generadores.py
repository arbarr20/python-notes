
# Archivo: generadores.py
# Autor: Arbarr20 y ayuda online
# Fecha:23/05/2023
# Descripción: Planificador de tareas, que itera sobre generadores.

from collections import deque
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


def tarea_cuenta_regresiva(n: int):
    """
    Realiza una cuenta regresiva a partir de un número dado.

    :param n: El número inicial para la cuenta regresiva.
    :type n: int
    """
    while n > 0:
        logging.info(f"se ejecuta tarea = {n}")
        yield
        n -= 1


tareas = deque([
    tarea_cuenta_regresiva(5),
    tarea_cuenta_regresiva(3),
    tarea_cuenta_regresiva(2)
])


def manejador(tareas: deque) -> None:
    """
    Maneja la ejecución de las tareas en una cola.

    :param tareas: La cola de tareas a manejar.
    :type tareas: deque
    """
    while tareas:
        tarea = tareas.popleft()
        logging.info(f"se saca tarea: {hex(id(tarea))} para ejecutarla")
        try:
            next(tarea)
            tareas.append(tarea)
            logging.info(f"se pasa tarea: {hex(id(tarea))} al final de la cola\n")
            # se genera na excepción cuando un generador termine, pero no se para la
            # ejecución, es decir se omite el error
        except StopIteration:
            pass


# Ejecución
manejador(tareas)
