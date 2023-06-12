# Archivo: corrutinas_callbacks10.py
# Autor: Arbarr20 y ayuda online
# Fecha:12 /06/2023
# Este es un enfoque alternativo de async con generadores para solucionar el problema del
# productor, consumidor (paso de datos de uno al otro)
# Archivo problema principal: problem_producer_consumer.py.
# solucionamos el problema del script produc-consum-yield_await_async8
# Un ejemplo de cómo implementar concurrencia basada en corutinas sobre un planificador basado en  devoluciones de llamada.

import time
from collections import deque
import heapq

import logging

# mostrar mas información de depuración
# logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')

# mostrar solo información de interés, salida de consola
logging.basicConfig(level=logging.INFO, format='[%(threadName)s:%(process)d] %(message)s')


# Callback based scheduler (from earlier)
class Scheduler:
    def __init__(self):
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions
        self.sequence = 0
        self.current = None 

    # es llamado por tareas basado en callbacks, donde func = callback
    # llamada por funciones normalitas sin async def
    # pone en la cola de ejecución el callback-tarea a ejecutar
    def call_soon(self, func):
        self.ready.append(func)
    """
    call_later, es una forma de decir, me demoro un tiempo en hacer algo,
    regreso en un tiempo (apenas termine) --> ponme en la colo de prioridades.
    mientras, haz algo. este mientras.... es casi mágico y depende de quien llamo a func,
    esto es clave, por que a ese lugar es donde regresa, y esta parte es el método run()
    """
    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay     # Expiration time
        # Priority queue
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))
    """
    Para mi, este es el método mas importante, su lógica es el que permite la verdadera concurrencia de tareas.
    1. mientras hay corrutinas listas para ejecutarse en la cora ready o corrutinas esperando a ejecutarse en la cola 
    sleeping verifica:
      * si no hay corrutinas en la cola ready: esto es porque hay corrutinas que se están demorando en hacer su trabajo
        esta corrutinas son las que en otras partes del código dicen (me demoro en hacer esto, llámame después de x tiempo)
        si entra en este condicional, se debe esperar (bloqueante) el tiempo (que aun falta por que la corrutina termine 
        su trabajo) delta, una vez este tiempo llegue a cero, esta corrutina o  callback para  a la cola ready.

     * si por el contrario hay corrutinas o callbacks en la cola ready, saca la que este en la posición 0 
       (self.ready.()) y ejecútala (func())
    """
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
                func = self.ready.popleft()
                func()

    # Corrutinas basadas en Funciones.
    # es usada por corrutinas (funciones inician con async def)
    def new_task(self, coro):
        self.ready.append(Task(coro))   # Wrapped coroutine

    # observe que el sleep solo es llamado por otra corrutina (asycn def)
    async def sleep(self, delay):
        # la corrutina que llamo este método es enviado a la call_later, en la cual es puesto
        # en una cola de prioridad
        self.call_later(delay, self.current)
        # linea clave para desvincular la corrutina, como ya se guardo en una cola de prioridad
        # por medio de call_later, para que seguirla ejecutando. por esto se pone self.current=none
        self.current = None 
        # aquí es donde veo el verdadero cambio de "contexto", ya que lleva a un yield, y el 
        # manejo que se le da el código antes y después de esta linea es lo que permite la concurrencia.
        await switch()   # Switch to a new task


# Clase que envuelve una corutina, haciéndola parecer como una devolución de llamada.
class Task:
    def __init__(self, coro):
        self.coro = coro        # "Corrutina envuelta"

    # Haz que parezca una devolución de llamada
    # __call__ llamar la instancia como si fuera una función.
    def __call__(self):
        try:
            # Ejecutando la corutina como antes
            sched.current = self  # type: ignore
            self.coro.send(None)
            if sched.current:
                sched.ready.append(self)
        except StopIteration:
            pass


class Awaitable:
    def __await__(self):
        yield


def switch():
    return Awaitable()


sched = Scheduler()    # Background scheduler object

# ----------------


class AsyncQueue:
    def __init__(self):
        # Aquí se pone la data que se produce y que se consume
        self.items = deque() 
        # corrutinas consumidoras que no encontraron datos para consumir
        self.waiting = deque()

    # corrutina para poner data en la cola items
    # 1. pone el item producido en la cola item
    # 2. verifica si hay corrutinas consumidoras en la cola de espera y si las hay
    #  saca una de ellas y la pone en la cola ready del manejador.
    # esto tiene mucha lógica que suceda, ya que si hay un data producido y hay consumidor en 
    #  espera para consumirlo, por que no habilitarlo (ready) para que lo consuma.
    async def put(self, item):
        self.items.append(item)
        if self.waiting:
            sched.ready.append(self.waiting.popleft())

    """
    Corrutina para obtener un dato dela cola de items producidos, es logíco que esca corrutina
    solo sea  llamada por el consumidor
    1. verifica si no hay datos en la cola de items, si no los hay: 
      * pone en la cola de espera la corrutina o callback que ha llamado a put()
      * el sched.current = None es para reiniciar la variable current
      * await switch es para ceder el control a otra corrutina o callback
    2. Si hay mensajes en la cola items, saca el que este en la posición 0 y lo retorna    
    """

    async def get(self):
        if not self.items:
            self.waiting.append(sched.current)   # Put myself to sleep
            sched.current = None        # "Disappear"
            await switch()              # Switch to another task
        return self.items.popleft()


# Tareas basadas en corrutinas
async def producer(q, count):
    for n in range(count):
        logging.info(f"Produciendo: {n}")
        await q.put(n)
        await sched.sleep(1)

    logging.info("Productor Terminó")

    await q.put(None)   # "Sentinel" to shut down


async def consumer(q):
    while True:
        item = await q.get()
        if item is None:
            break
        logging.info(f"consuming, {item}")
    logging.info("Consumidor Terminó")

q = AsyncQueue()
sched.new_task(producer(q, 10))
sched.new_task(consumer(q))


# Tareas basadas en callbacks
def countdown(n):
    if n > 0:
        logging.info(f"Down {n}")
        # time.sleep(4)    # Llamada bloqueante (nada mas puede ejecutarse)
        # lo que significa la siguiente linea es, oye me demoraré 4 segundos,
        # en hacer la cuenta regresiva, mientras, haz otra cosa.
        # esa (haz otra cosa) se hace en el método call_later
        sched.call_later(4, lambda: countdown(n-1)) # esta no es una llamda bloqueante


def countup(stop):
    def _run(x):
        if x < stop:
            logging.info(f"Up {x}")
            # time.sleep(1)
            sched.call_later(1, lambda: _run(x+1))
    _run(0)

# call_soon es para tareas basadas en callbacks
sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(20))
sched.run()
