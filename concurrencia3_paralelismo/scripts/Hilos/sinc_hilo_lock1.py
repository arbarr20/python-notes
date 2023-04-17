# Archivo: sinc_hilo_lock1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 17/03/2023
# Descripción: Sincronización de hilos con lock.


import threading
import logging
import time


logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)

"""
x: Una variable global que representa el valor que será modificado por los hilos.
x_lock: Un objeto de la clase threading.Lock que se utiliza para evitar que los hilos modifiquen x
simultáneamente.
COUNT: Una constante que representa la cantidad de veces que cada hilo modifica x.
foo(): Función que incrementa el valor de x por COUNT veces utilizando el lock.
bar(): Función que decrementa el valor de x por COUNT veces utilizando el lock.
t1: Un objeto de la clase threading.Thread que representa el hilo que ejecuta foo().
t2: Un objeto de la clase threading.Thread que representa el hilo que ejecuta bar().
t1.start(): Inicia la ejecución del hilo t1.
t2.start(): Inicia la ejecución del hilo t2.
t1.join(): Espera a que el hilo t1 termine su ejecución antes de continuar con el código.
t2.join(): Espera a que el hilo t2 termine su ejecución antes de continuar con el código.
logging.info(x): Imprime el valor final de x después de que ambos hilos hayan modificado su valor.
"""
x: int = 0
x_lock: threading.Lock = threading.Lock()

COUNT: int = 10


def foo() -> None:
    """
    Esta función incrementa el valor de la variable global x por COUNT veces
    utilizando un lock para evitar problemas de concurrencia.
    """
    global x
    for i in range(COUNT):
        x_lock.acquire()
        x += 1
        logging.info(x)
        time.sleep(1)
        x_lock.release()
        # Puedes usar with después del for
        # un administrador de contexto también es buena idea
        """ with x_lock:
            x += 1 """


def bar() -> None:
    """
    Esta función decrementa el valor de la variable global x por COUNT veces
    utilizando un lock para evitar problemas de concurrencia.
    """
    global x
    for i in range(COUNT):
        x_lock.acquire()
        x -= 1
        logging.info(x)
        time.sleep(1)
        x_lock.release()
        # Puedes usar with después del for
        # un administrador de contexto también es buena idea
        """ with x_lock:
            x += 1 """


t1: threading.Thread = threading.Thread(target=foo)
t2: threading.Thread = threading.Thread(target=bar)
t1.start()
t2.start()
t1.join()
t2.join()
logging.info(x)
