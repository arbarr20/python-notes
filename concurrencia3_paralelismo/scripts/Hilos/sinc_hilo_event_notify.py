# Archivo: sinc_hilo_event_notify.py
# Autor: Arbarr20 y ayuda online
# Fecha: 26/04/2023
# Descripción: Un ejemplo de cómo usar un semáforo y un evento para que un hilo
# señale la finalización de alguna tarea (combinación evento y semáforo)

"""
El productor (producer()) crea un item y espera a que el trabajador (worker()) lo procese.
Para coordinar su trabajo, se utilizan un semáforo y un evento.

El semáforo (available) se utiliza para indicar cuándo hay un elemento disponible para ser
procesado. El valor del semáforo comienza en cero, lo que indica que no hay elementos disponibles.
Cuando el productor produce un elemento, aumenta el valor del semáforo con el método release().
El trabajador espera a que el semáforo tenga un valor mayor que cero antes de procesar un elemento,
lo que se hace mediante el método acquire().

El evento (completed) se utiliza para indicar cuándo el trabajador ha procesado un elemento.
El productor espera a que el evento se active con el método wait() antes de producir otro elemento.
El trabajador activa el evento con el método set() después de procesar un elemento.

En resumen, el productor crea un elemento, lo pone a disposición del trabajador y espera a que se
procese. El trabajador espera a que haya elementos disponibles, procesa un elemento, indica que ha
terminado y espera a que haya otro elemento disponible. El proceso se repite hasta que el productor
ha creado y procesado todos los elementos.
"""
import threading
import time
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)

# Una variable que contiene datos
item = None

# Un semáforo para indicar que un elemento está disponible.
available = threading.Semaphore(0)

# An event to indicate that processing is complete
completed = threading.Event()

# A worker thread


def worker():
    while True:
        logging.info(f"Adquirimos el semaforo contador: {available._value} y lo decrementmos")
        available.acquire()
        logging.info(f"worker: Procesando el item: {item}")
        time.sleep(1)
        logging.info("worker: Item procesado")
        logging.info("Estableciendo evento - productor puede continuar")
        completed.set()
        # cuando esta función se ejecuta por segunda vez,  regresa el inicio del ciclo,
        # al ver que  el valor del contador del semáforo esta en 0 este hilo se bloquea


# A producer thread
def producer():
    global item
    for x in range(3):
        logging.info("clear,puede producir item, pero espera hasta que se procese, para producir otro")
        completed.clear()       # Clear the event
        item = x                # Set the item
        logging.info("producer: Produciendo un ITEM")
        logging.info("habilitamos al trabajador para que procese el item - release cont+")
        available.release()     # Signal on the semaphore
        logging.info(f"contador semaforo: {available._value}")
        logging.info("Esperemos hasta que el trabajador procese el item")
        completed.wait()
        logging.info("producer: El item fue procesado")


t1 = threading.Thread(target=producer)
t1.start()
t2 = threading.Thread(target=worker)
t2.daemon = True
t2.start()
