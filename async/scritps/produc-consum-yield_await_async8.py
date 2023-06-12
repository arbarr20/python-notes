# Archivo: produc-consum-yield_await_async8.py
# Autor: Arbarr20 y ayuda online
# Fecha:09/06/2023
# Este es un enfoque alternativo de async con generadores para solucionar el problema del
# productor, consumidor (paso de datos de uno al otro)
# Archivo problema principal: problem_producer_consumer.py.

"""
await algo: Puedes hacer otra cosa, mientras hago algo. lo que ponga delante de await, si es una funcíon,
  esta debe ser una corrutina, debe tener el async def.
async def método o funcion(): la funcion es asincrona y puede contener un await, automaticamente
 esta funcion es una corrutina que se puede ejecutar como una tarea asincrónica utilizando el await. Esto
 permite que el programa ejecute otras tareas mientras espera la finalización de una tarea asincrónica, en lugar de bloquearse y esperar directamente la respuesta.


Await en este caso es un poco confuso, puesto que en las lineas
* `await q.put(n): no hay cambio de contexto, a no ser que sea por salir un momento del for
  donde esta contenido. pero no veo la aplicación del "Puedes hacer otra cosa" mientras pone un item
  en la cola de producción.
* item = await q.get()`: mientas hay items producidos disponibles no se logra evidenciar 
  "puedes hacer otra cosa". creo que es para salir del while.
   
pero en las lineas await sched.sleep(4) --> lleva a await switch(): en esta si se evidencia cambio

* await sched.sleep(4): Puedes hacer otra cosa, mientras le digo al sched que  voy a demorarme 4 seg
  en realizar una tarea (es una simulación de una tarea costosa, como guardar en disco, o consultar una
 web), esta linea lleva a await switch()

* await switch():aquí es donde veo el verdadero cambio de "contexto", ya que lleva a un yield, y el 
  manejo que se le da el código antes y después de esta linea es lo que permite la concurrencia.

Problema: una que ya habíamos visto anteriormente, el productor debe enviar una señal de apagado cuando
deje de producir elementos. esto es basicamente cerrar la COLA, esta señal debe ser recibida por el 
consumidor, para dejar de consumir.lo que pasa con esta señal es que si hay elementos en la cola que aun 
no se han consumido,se perderán, para esto es necesario envolver una excepción en un objeto y darle
 manejo, esto lo veremos en el proximo script.

"""

import time
from collections import deque
import heapq


import logging

# mostrar mas información de depuración
# logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')

# mostrar solo información de interés, salida de consola
logging.basicConfig(level=logging.INFO, format='[%(threadName)s:%(process)d] %(message)s')


class Awaitable:
    def __await__(self):
        yield


def switch() -> Awaitable:
    """
    Función que devuelve un objeto Awaitable.

    Returns:
        Awaitable: Objeto Awaitable.
    """
    return Awaitable()


class Scheduler:
    """
    Clase Scheduler que administra la ejecución de tareas asincrónicas.

    Attributes:
        ready (deque): Cola de tareas listas para ser ejecutadas.
        sleeping (list): Lista de tareas en espera.
        current: Tarea actualmente en ejecución.
        sequence (int): Número de secuencia para administrar el orden de las tareas en espera.
    """

    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self.current = None    # Currently executing generator
        self.sequence = 0

    async def sleep(self, delay: float) -> None:
        """
        Método para suspender la ejecución de la tarea actual durante un tiempo dado.

        Args:
            delay (float): Tiempo de suspensión en segundos.

        Raises:
            None
        """
        deadline = time.time() + delay
        self.sequence += 1
        heapq.heappush(self.sleeping, (deadline, self.sequence, self.current))
        self.current = None  # "Disappear"
        await switch()       # Switch tasks

    def new_task(self, coro) -> None:
        """
        Método para agregar una nueva tarea a la lista de tareas listas para ser ejecutadas.

        Args:
            coro: Tarea a agregar.

        Returns:
            None
        """
        self.ready.append(coro)

    def run(self) -> None:
        """
        Método principal que ejecuta las tareas encoladas hasta que no haya más tareas encoladas ni tareas en espera.

        Returns:
            None
        """
        while self.ready or self.sleeping:
            logging.debug(f"antes-ready {self.ready}")
            logging.debug(f"antes-sleeping {self.sleeping}")
            if not self.ready:
                deadline, _, coro = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(coro)

            self.current = self.ready.popleft()
            logging.debug(f"despues-ready {self.ready}")
            logging.debug(f"despues-sleeping {self.sleeping}")
            logging.debug(f"Actual: {self.current}")
            # Drive as a generator
            try:
                self.current.send(None)   # Send to a coroutine
                if self.current:
                    self.ready.append(self.current)
            except StopIteration:
                pass


sched = Scheduler()


class AsyncQueue:
    """
    Clase AsyncQueue que implementa una cola asincrónica.

    Attributes:
        items (deque): Cola de elementos.
        waiting (deque): Cola de tareas en espera.

    Methods:
        put(item) -> None: Agrega un elemento a la cola asincrónica.
        get() -> Any: Obtiene un elemento de la cola asincrónica.
    """

    def __init__(self):
        self.items = deque()
        self.waiting = deque()

    async def put(self, item) -> None:
        """
        Método para agregar un elemento a la cola asincrónica.

        Args:
            item: Elemento a agregar a la cola.

        Returns:
            None

        Raises:
            None
        """
        self.items.append(item)
        logging.debug(f"put-items: {self.items}")
        if self.waiting:
            logging.debug(f"put-wating: {self.waiting}")
            sched.ready.append(self.waiting.popleft())
            logging.debug(f"ready-put: {sched.ready}")

    async def get(self):
        """
        Método para obtener un elemento de la cola asincrónica.

        Returns:
            Elemento obtenido de la cola.

        Raises:
            None
        """
        logging.debug(f"get-items: {self.items}")
        if not self.items:
            self.waiting.append(sched.current)   # Put myself to sleep
            logging.debug(f"get-wait-poner: {self.waiting}")
            sched.current = None        # "Disappear"
            await switch()              # Switch to another task
        return self.items.popleft()


async def producer(q, count: int) -> None:
    """
    Tarea asincrónica que produce elementos y los agrega a la cola.

    Args:
        q: Objeto AsyncQueue al que se agregarán los elementos.
        count (int): Número total de elementos a producir.

    Returns:
        None

    Raises:
        None
    """
    for n in range(count):
        logging.info(f"Producing, {n}")
        await q.put(n)
        await sched.sleep(2)

    logging.info("Productor Terminó")
    await q.put(None)   # "Sentinel" to shut down


async def consumer(q) -> None:
    """
    Tarea asincrónica que consume elementos de la cola.

    Args:
        q: Objeto AsyncQueue del que se consumirán los elementos.

    Returns:
        None

    Raises:
        None
    """
    while True:
        item = await q.get()
        if item is None:
            break
        logging.info(f"consuming, {item}")
    logging.info("Consumidor Terminó")


q = AsyncQueue()
sched.new_task(producer(q, 10))
sched.new_task(consumer(q))
sched.run()
