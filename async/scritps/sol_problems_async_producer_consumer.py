# Archivo: sol_problems_async_producer_consumer.py
# Autor: Arbarr20 y ayuda online
# Fecha:05/06/2023
# Descripción: Se solucionan los problemas de:
# * señal de apagado
# * como comunicar el Error


"""
Como es esto de la señal de apagado: básicamente es que el productor cierra la cola de ELEMENTOS 
producidos, esto lógicamente es para no producir mas datos, lo que pasa con esto es que en el
momento de cerrar la cola se genera una excepción, y los datos que aun están en la cola y faltan 
por consumirse se perderán.

Solución de comunicación del error para la señal de apagado:
 * se captura la excepción que se produce el cerrar la cola en un objeto, esto para que no
  se genere la excepción que cierra la cola y hace que se pierdan los datos.
  para esta solución es clave:
   * el callback que se para como parámetro en el método `get()`
   * la clase Result de la cual se crea un objeto que captura la excepción de cierre de la cola
     y la data que se produce para ser mostrada o consumida, es decir result se puso en medio entre
     el consumidor y el productor, esta clase captura los valores y las excepciones.
     esta clase captura los valores y las excepciones. esta clase Result
     es lo que mas adelante llamaremos Futuros.

Problemas: se esta formando un espagueti de callbacks
  * tenga en cuanta que aun no se pueden usar loops (while, for) en las funciones
    consumidores y productoras

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


class Result:
    def __init__(self, value=None, exc=None) -> None:
        self.value = value
        self.exc = exc

    def result(self):

        if self.exc:
            logging.info(f"result excepcion: {self.exc}")
            raise self.exc
        else:
            logging.info(f"result value: {self.value}")
            return self.value


class AsyncQueue:
    # En la cola items se guardan los ELEMENTOS que se producen y que posteriormente
    # se consumirán, no se guardan FUNCIONES se guarda la DATA
    # en la cola waiting se guardan FUNCIONES que deben esperar data que no esta disponible.
    # luego, cuando el productor pone un dato en item, verifica si hay  (FUNCIONES) en la cola
    # waiting y lo envía a la cola ready para ser ejecutada.
    def __init__(self):
        self.items = deque()
        self.waiting = deque()    # All getters waiting for data
        self._closed = False      # Can queue be used anymore?

    def close(self):
        self._closed = True
        # esta linea es vitar para que se muestre el consumer done
        # cuando el productor cierra la cola se debe verificar que las funciones en waiting se 
        # ejecuten (poner el la cola ready)
        # el and not self.items: me parece una doble verificación, ya que en
        # get se verifica con if self.items
        if self.waiting and not self.items:
            for func in self.waiting:
                sched.call_soon(func)

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
            # callback(self.items.popleft()) # << error close queue vieja implementación
            # capture el valor (Data) en un Objeto result para que sea consumido
            callback(Result(value=self.items.popleft()))  # <<< nueva implementación
        # si no hay data producida, es por 2 razones:
        # el productor ya termino y cerro la cola
        # o aun esta ocupado y no ha producido mas
        else:
            # si el productor cerro la cola
            if self._closed:
                # self.waiting.append(lambda: self.get(callback)) # << vieja implementación
                # captura la excepción en un objeto de Result
                callback(Result(exc=QueueClosed()))  # <<< nueva implementación
            # si el productor esta ocupado produciendo mas Data
            # ponga el consumidor en la cola waiting
            else:
                self.waiting.append(lambda: self.get(callback))
                logging.info(f"waiting despuess: {self.waiting}")


class QueueClosed(Exception):
    pass


def producer(q, count):
    def _run(n):
        if n < count:
            logging.info(f'Producing {n}')
            q.put(n)
            sched.call_later(1, lambda: _run(n+1))
        else:
            logging.info('Producer done')
            # q.put(None) # <<<< vieja implementación
            q.close()  # <<<< nueva implementación para cerrar la cola
    _run(0)


def consumer(q):
    def _consume(result):
        try:
            item = result.result()
            logging.info(f'Consuming {item}')
            sched.call_soon(lambda: consumer(q))
        except QueueClosed:
            logging.info("Consumer done")
    q.get(callback=_consume)


"""     def _consume():
        if item is None:
            logging.info('Consumer done')

        else:
            logging.info(f'Consuming {item}')
            sched.call_soon(lambda: consumer(q))
    q.get(callback=_consume) """


q = AsyncQueue()
sched.call_soon(lambda: producer(q, 4))
sched.call_soon(lambda: consumer(q,))
sched.run()
