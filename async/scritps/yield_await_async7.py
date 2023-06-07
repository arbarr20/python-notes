# Archivo: yield_await_async7.py
# Autor: Arbarr20 y ayuda online
# Fecha:06/06/2023
# Descripción: Se solucionan los problemas de:
# * aun tenemos bloqueos no es concurrente.
# Este es un enfoque alternativo de async con generadores para solucionar el problema del
# decremento, incremento no bloqueante
# # Archivo: problem_producer_consumer.py


""""
Código que hace que la declaración "await" funcione. Proporcionamos
una única función "switch" que es utilizada por el planificador para
cambiar entre tareas.

Problemas Anteriores:
* aun tenemos bloqueos no es concurrente.

Partes de la solución:
1. se hará una abstracción de los yield en las funciones countdown y countup en la clase Awaitable.
2. abordamos el problema del bloqueo tieme.sleep() simula tarea bloqueante.

Teoría:

Cuando se encuentra una expresión await, Python verifica si el objeto que sigue a await es un
awaitable. Un awaitable es un objeto que implementa el método __await__(). En este caso, la clase 
Awaitable define ese método.

Cuando se ejecuta una expresión await, el intérprete de Python verifica si el objeto al que se le 
aplica el await es awaitable. Si es así, invoca el método __await__() en ese objeto. En el caso de 
la clase Awaitable, el método __await__() simplemente devuelve un generador que se pausa 

inmediatamente utilizando la instrucción yield. Esto permite que la ejecución se suspenda en ese 
punto y se ceda el control a otra tarea.

El uso de await junto con la clase Awaitable y su método __await__() permite pausar y reanudar la 
ejecución de una función asincrónica de manera controlada. Cuando se alcanza una expresión await, 
la función se pausa y devuelve el control al planificador o al bucle principal hasta que se cumpla 
alguna condición, como la finalización de una operación de E/S o un tiempo de espera.

* Inicializar Generador:
    Es importante tener en cuenta que la primera llamada a send() siempre debe ser send(None) o next(), 
    ya que no hay un valor previo que se pueda enviar al generador. A partir de la segunda llamada, 
    podemos enviar cualquier valor que sea compatible con la asignación en el generador.

* self.current = None
    si se quita la línea self.current = None, se puede producir un comportamiento inesperado donde una 
    tarea anterior se ejecuta continuamente sin permitir que otras tareas
    (las que están en cola de espera self.sleeping) tengan la oportunidad de 
    ejecutarse, esto ocaciona que la cola sleeping se llene con generadores que ya han terminado, y en
    el momento que se ejecuten salte una excepción, ya que se debe reiniciar el generador y esto no 
    esta contemplado. Es importante restablecer self.current a None después de que una tarea se haya 
    completado para garantizar que el planificador avance correctamente y permita la ejecución de otras 
    tareas en la cola self.ready.   

* if self.current: si el generador aun tiene trabajo pendiente. Aun no encuentro la funcionalidad 
    de  linea de codigo, ya que si la quito, no pasa nada. ademas con la linea anterior
    (self.current = None) nunca este condicional es verdadero.
    Solo es verdadero cuando se quita la linea (self.current = None) y genera una exepción.
    Pero hay otra salvedad, si se quitan las 2 lineasself.current = None y if self.current 
    el codigo corre sin errores.
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


def switch():
    return Awaitable()


class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self.current = None    # Generador que se estará ejecutando
        self.sequence = 0
    # toda función que desea usar await debe iniciar con async

    async def sleep(self, delay):
        logging.debug(f"current: {self.current}")
        deadline = time.time() + delay
        self.sequence += 1
        heapq.heappush(self.sleeping, (deadline, self.sequence, self.current))
        self.current = None  # Desaparecer por un tiempo y dormir
        # espera y ve hacer otra cosa, aquí es clave:
        # de donde viene: (que hizo antes de llegar aquí=heapq.heappush)
        # para donde va: (repetir el ciclo while self.ready or self.sleeping)
        await switch()       # Switch tasks es como un yield solito

    def new_task(self, coro):
        self.ready.append(coro)
        logging.debug(f"task: {self.ready}")

    def run(self):
        # el or self.sleeping es importante quí
        while self.ready or self.sleeping:
            logging.debug(f"run-antes-ready: {self.ready} ")
            logging.debug(f"run-antes-sleeping: {self.sleeping} ")
            if not self.ready:
                deadline, _, coro = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(coro)

            self.current = self.ready.popleft()
            logging.debug(f"run-despu-ready: {self.ready} ")
            logging.debug(f"run-despu-sleeping: {self.sleeping} ")
            # Drive as a generator
            try:
                logging.debug(f"run-ejecucion: {self.current}")
                self.current.send(None)   # next(self.current) en el script anterior
                logging.debug(f"run-current: {self.current}")
                if self.current:
                    self.ready.append(self.current)
            except StopIteration:
                pass


sched = Scheduler()    # Background scheduler object

# ---- Example code


async def countdown(n):
    while n > 0:
        logging.info(f'Down: {n}')
        # me voy a demorar un tiempo (4 seg) en hacer mi trabajo, por esto,
        # hey, manejador llamame de nuevo  en 4 seg aprox
        await sched.sleep(2)
        n -= 1


async def countup(stop):
    x = 0
    while x < stop:
        logging.info(f'Up: {x}')
        await sched.sleep(1)
        x += 1

sched.new_task(countdown(10))
sched.new_task(countup(5))
sched.run()
