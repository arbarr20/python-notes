# Archivo: async_producer_consumer.py
# Autor: Arbarr20 y ayuda online
# Fecha:05/06/2023
# Descripción: productor consumidor solo con un Hilo.


"""
Cambios importantes de la implementación con hilos:

colas de ejecución: scheduler ejecución de las funciones que producen y consumen
colas de producción: los datos que comporten Asyncdeque
* Se crea una cola asíncrona:
* productor: no deben haber ciclos ni for, ni while
* problema: como enviar señal de apagado al consumidor, cuando el productor termine.
  esto de hace para reemplazar el q.put(None) por algo como q.close().
  * que pasa con la cola cerrada y el get
  * como comunicar un error


"""
import time
from collections import deque
import heapq

import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


class Scheduler:
    def __init__(self):
        # en la cola ready se guardan todas las TAREAS O FUNCIONES (PRODUCTORES O CONSUMIDORES)
        #  que están disponibles para  ejecutarse
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions
        self.sequence = 0

    def call_soon(self, func):
        self.ready.append(func)
        logging.info(f"lo que hay en ready: {self.ready}")

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay     # Expiration time
        # Priority queue
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                # Find the nearest deadline
                deadline, _, func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)

            while self.ready:
                logging.info(f"ready-antes: {self.ready}")
                func = self.ready.popleft()
                logging.info(f"ready-desoues: {self.ready}")
                func()


sched = Scheduler()     # Behind scenes scheduler object

# -----


class AsyncQueue:
    # En la cola items se guardan los ELEMENTOS que se producen y que posteriormente
    # se consumirán, no se guardan FUNCIONES se guarda la DATA
    # en la cola waiting se guardan FUNCIONES que deben esperar data que no esta disponible.
    # luego, cuando el productor pone un dato en item, verifica si hay  (FUNCIONES) en la cola
    # waiting y lo envía a la cola ready para ser ejecutada.
    def __init__(self):
        self.items = deque()
        self.waiting = deque()    # All getters waiting for data
    # pone item producidos por el productor en  la cola async
    # revisa si hay elementos (consumidores que intentaron ejecutarse pero no había nada producido
    # en su  momento)  en la cola de espera
    # pone en la cola ready a consumidores que estuvieron esperando en la cola waiting

    def put(self, item):
        self.items.append(item)
        logging.info(f"waiting-put {self.waiting}")
        if self.waiting:
            func = self.waiting.popleft()
            # ¿Lo llamamos de inmediato? No. Programarlo para que se llame más tarde.
            sched.call_soon(func)
    # si hay items (elementos producidos) los consume, sacar de la cola items y consumirlos
    # si no hay items producidos, se pone a el consumidor en la cola de espera,
    # esto le da al productor un "tiempo"" para que  produzca items.

    def get(self, callback):
        # Esperar hasta que haya un elemento disponible. Luego, devolverlo.
        logging.info(f"waiting antes: {self.waiting}")
        if self.items:
            # _consume(3)
            callback(self.items.popleft())
        else:
            self.waiting.append(lambda: self.get(callback))
        logging.info(f"waiting despuess: {self.waiting}")


def producer(q, count):
    def _run(n):
        if n < count:
            logging.info(f'Producing {n}')
            q.put(n)
            sched.call_later(1, lambda: _run(n+1))
        else:
            logging.info('Producer done')
            q.put(None)
    _run(0)


def consumer(q):
    def _consume(item):
        if item is None:
            logging.info('Consumer done')

        else:
            logging.info(f'Consuming {item}')
            sched.call_soon(lambda: consumer(q))
    q.get(callback=_consume)


q = AsyncQueue()
sched.call_soon(lambda: producer(q, 10))
sched.call_soon(lambda: consumer(q,))
sched.run()
