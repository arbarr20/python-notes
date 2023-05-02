# Archivo: sinc_hilo_condition2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 02/05/2023
# Descripción: Un ejemplo de uso de una variable de condición para establecer un problema de
# consumidor, se usa el with.


import threading
import time
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


# Una lista de elementos que se están produciendo. Nota: en realidad
# es más eficiente usar un objeto collections.deque() para esto.

items = []

# Una variable de condición para elementos
items_cv = threading.Condition()

# Un hilo productor


def producer():
    logging.info("Soy el productor")

    for i in range(3):
        # el with tiene implícito el acquire() y el release()
        with items_cv:
            # en esta linea hay un hilo.acquire implícito espera si es 0, de lo contrario decrementa
            # contador y continua
            # Siempre se debe adquirir el lock primero.
            logging.info("Agregando elementos a la lista adquiere lock dec conta continua")
            items.append(i)
            logging.info("notificando al  consumidor")   # Agregar un item a las lista
            items_cv.notify()   # Enviar una señal de notificación
            logging.info("fin del with se libera el lock inc conta ")
        time.sleep(1)

# A consumer thread


def consumer():
    logging.info("Soy el consumidor")
    while True:
        # el with tiene implícito el acquire() y el release()
        with items_cv:
            logging.info("consumidor en acción  adquiere lock dec conta continua")
            while not items:
                # Revisa si hay algún elemento.
                logging.info("no hay items.. a esperar una notify")
                items_cv.wait()
            logging.info("sacando un elemento de la lista")  # Si no vamos a dormir
            x = items.pop(0)     # Eliminar un elemento de la lista.
            logging.info("fin del with se libera el lock inc conta ")

        logging.info(f"Recibiendo, {x}")
        # en esta linea implícitamente  hay un hilo.release inc contador
        time.sleep(1)


# Lanza varios consumidores.
cons = [threading.Thread(target=consumer)
        for i in range(3)]

for c in cons:
    c.daemon = True
    c.start()

# Correr el productor
producer()
