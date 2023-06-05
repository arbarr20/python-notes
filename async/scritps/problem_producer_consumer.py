#
# Archivo: problem_producer_consumer.py
# Autor: Arbarr20 y ayuda online
# Fecha:05/06/2023
# Descripción: productor consumidor con hilos, tiene un problema, el cambio de contexto
# lo hace lento

"""
Problema Principal: hacer que el siguiente codigo no se bloquee, que no tenga tiempos
  muertos.
def countdown(n):
    while n > 0:
        print("decrementando:",n)
        time.sleep(1)
        n -= 1
def countup(stop):
    x = 0
    while x < stop:
        print(f"Up {x}")
        time.sleep(1)
        x += 1
countdown()
countup()
"""

import queue
import threading
import time

import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


def producer(q, count):
    for n in range(count):
        logging.info(f'Producing {n}')
        q.put(n)
        time.sleep(1)

    logging.info('Producer done')
    q.put(None)   # "Sentinel" to shut down


def consumer(q):
    while True:
        item = q.get()  # problema: se bloquea, esta esperando a que haya  elementos disponibles
        if item is None:
            break
        logging.info(f'Consuming, {item}')
    logging.info('Consumer done')


q = queue.Queue()   # Thread-safe queue
threading.Thread(target=producer, args=(q, 10)).start()
threading.Thread(target=consumer, args=(q,)).start()
