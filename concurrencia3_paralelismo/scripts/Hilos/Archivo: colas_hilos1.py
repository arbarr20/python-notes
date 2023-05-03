# Archivo: colas_hilos1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/05/2023
# Descripción: Un ejemplo de uso de colas para establecer problemas de productor/consumidor..

import threading
import time
import queue
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)

# Una cola de elementos que están siendo producidos.
items: queue.Queue = queue.Queue()


# Hilo productor
def producer() -> None:
    logging.info("Soy el productor")
    for i in range(5):
        items.put(i)
        logging.info(f"Se produjo {items.queue}")
        time.sleep(1)


# Hilo consumidor
def consumer() -> None:
    logging.info("Soy un consumidor")
    while True:
        x = items.get()
        logging.info(f"Se obtuvo {x}")
        time.sleep(5)


# Lanzar un montón de consumidores
cons = cons = [threading.Thread(target=consumer)for i in range(10)]
for c in cons:
    c.daemon = True
    c.start()

# Ejecutar el productor
producer()
