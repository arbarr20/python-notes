# Archivo: sinc_hilo_condition1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 02/05/2023
# Descripción: Sincronización de Hilos con ,Es posible utilizar `threading.Condition`
# sin utilizar la sentencia `with` en Python.


import threading
import time
import logging
import random

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


# Variables compartidas
number = None
condition = threading.Condition()

# Hilo de producción


def producer():
    global number
    for _ in range(10):
        # Simular tiempo de producción
        time.sleep(1)
        # Generar un número aleatorio
        number = random.randint(1, 100)
        logging.info(f"Generated number: {number}")
        # Adquirir el candado
        condition.acquire()
        # Notificar al hilo de consumo
        condition.notify()
        # Liberar el candado
        condition.release()


# Hilo de consumo
def consumer():
    global number
    for _ in range(10):
        # Adquirir el candado
        condition.acquire()
        # Esperar a que haya un número disponible
        while number is None:
            condition.wait()
        # Consumir el número
        logging.info(f"Consumed number: {number}")
        number = None
        # Liberar el candado
        condition.release()


# Iniciar los hilos
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
