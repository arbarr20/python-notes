# Archivo: haciendo_async2.py
# Autor: Arbarr20 y ayuda online
# Fecha:29/05/2023
# Descripción: Segundo acercamiento a async, se trata de simular como se construyó la biblioteca
# ASYNC de python. En esta entrada se trata de aprovechar los tiempos muertos(sleep)

"""
* shed.call_later(8, lambda: _run(x + 1)): olle manejador, me demoro 8 unidades de tiempo, estaré
  listo  para que me llames después de ese tiempo
* shed.call_soon(lambda:countdouwn(5)): esto es aproximado a :
        def count_down_recursive(n):
            countdown(n-1)

        shed.call_soon(count_down_recursive(n))
    cuantas veces la ejecución pasa por esta linea?
    1: al guardar en la cola shed.call_soon(....)
    2: al regresar de guardar en la cola
    3: cuando es llamada para ejecutar lambda:countdouwn(5) o lambda: countdouwn(n-1)desde run(self)
    para pasar los argumento.  sería algo como llamar a count_down_recursive(5)
    4: al guardar de nuevo en la cola dentro de countdouwn(n)
    5: regresa del punto 4
    6: retorno de 3
    el ciclo se repite desde el punto 3 cuando es llamado de nuevo por run

* shed.run(): este es un bucle, que saca de la cola funciones de cuenta regresiva, siempre y cuando
  existan disponibles, y las ejecuta.

* countdouwn(n):es la función concurrente, decrementa una variable hasta cero, pero lo mas 
  importante lo hace de la siguiente manera shed.call_soon(lambda: countdouwn(n-1)), ademas guarda
  en la cola  su proxima llamada.

"""

import time
import logging
from collections import deque

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


class Scheduler():
    def __init__(self) -> None:
        self.ready = deque() # cola de elementos disponibles
        # array de elementos que están en espera(esperando a que terminen su 
        # tarea)
        self.sleeping = [] 

    def call_soon(self, func):
        self.ready.append(func)
        # logging.info(f"cola: {self.ready}")

    def call_later(self, delay, func):
        deadline = time.time() + delay  # tiempo de expiración
        self.sleeping.append((deadline, func)) # guarda la tarea en el arreglo de esperas
        self.sleeping.sort() # organiza por tiempo de espera menor las tareas pendientes (cierta prioridad)
        

    def run(self):
        while self.ready or self.sleeping:
            # si no hay elementos en la cola de elementos disponibles
            # verifica si algun elemento dentro del arreglo de tareas en espera ya terminó
            if not self.ready: 
                # encontrar el tiempo de expiración mas proximo
                logging.info(f" sleeping: {self.sleeping}")
                # saca una tarea de la cola de espera
                deadline, func = self.sleeping.pop(0)
                # calcula cuanto tiempo le falta a la tarea que sacaste
                delta = deadline - time.time()  
                # si dicha tarea no ha terminado siga esperando
                if delta > 0:
                    time.sleep(delta)
                # de lo contrario agrégala a la cola de elementos disponibles
                self.ready.append(func)  

            while self.ready:
                logging.info(f"entrada -disponible: {self.ready}")
                func = self.ready.popleft()
                logging.info(f"ejecutando: {func}")
                logging.info(f"lo que queda: {self.ready}")
                func()


shed = Scheduler()


def countdouwn(n):
    if n > 0:
        logging.info(f"Regresiva: {n}\n")
        # time.sleep(1)
        # se reemplaza el tiempo muerto time.sleep (simulación de tarea bloqueante)
        # por la siguiente linea. (haz otra cosa mientras termino
        # termino en 2 unidades de tiemp
        shed.call_later(4, lambda: countdouwn(n-1))


def countup(stop):
    def _run(x):
        if x < stop:
            logging.info(f"Up: {x}\n")
            # time.sleep(1)
            # se reemplaza el tiempo muerto time.sleep (simulación de tarea bloqueante)
            # por la siguiente linea. (haz otra cosa mientras termino
            # termino en 2 unidades de tiempo)
            shed.call_later(2, lambda: _run(x + 1))
    _run(0)


shed.call_soon(lambda: countdouwn(8))
shed.call_soon(lambda: countup(2))
shed.run()
