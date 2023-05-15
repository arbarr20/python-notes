
# Archivo: multiprocessing-queues.py
# Autor: Arbarr20 y ayuda online
# Fecha: 15/05/2023
# Descripción: Comunicando procesos con Colas

"""
La línea entrada_cola.task_done() indica que se ha completado el procesamiento de un elemento de la 
cola entrada_cola.

Cada vez que se obtiene un elemento de la cola mediante el método get(), se debe llamar a 
task_done() después de que se ha procesado el elemento. De lo contrario, los elementos no 
procesados ​​seguirán contando en la cola y el programa no podrá saber cuándo ha terminado de 
procesar todos los elementos.

Cuando se llama al método join() en la cola, se bloquea el programa hasta que se hayan llamado a 
task_done() para todos los elementos obtenidos de la cola.
"""

import logging
import time
from multiprocessing import Process, JoinableQueue


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


def consumidor(entrada_cola: JoinableQueue) -> None:
    """
    Consumidor de la cola.

    Recibe los items de la cola, los procesa y marca su finalización.

    Args:
        entrada_cola: Cola de entrada de datos.

    Returns:
        None

    Raises:
        None
    """
    while True:
        item = entrada_cola.get()
        logging.info(f"consumiendo {item}")
        time.sleep(5)
        entrada_cola.task_done()


def productor(datos: range, salida_cola: JoinableQueue) -> None:
    """
    Productor de la cola.

    Envía los items de los datos a la cola.

    Args:
        datos: Secuencia de datos a producir.
        salida_cola: Cola de salida de datos.

    Returns:
        None

    Raises:
        None
    """
    for item in datos:
        logging.info(f"Produciendo {item}")
        time.sleep(1)
        salida_cola.put(item)


if __name__ == '__main__':
    q = JoinableQueue()

    cons_p = Process(target=consumidor, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    datos = range(5)
    productor(datos, q)

    q.join()
