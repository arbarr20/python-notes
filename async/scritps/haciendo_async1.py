
# Archivo: haciendo_async1.py
# Autor: Arbarr20 y ayuda online
# Fecha:29/05/2023
# Descripción: Primer acercamiento a async, se trata de simular como se construyó la biblioteca
# ASYNC de python. la clave a qui son los callback, las colas y el cheduler.

"""
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
        self.ready = deque()

    def call_soon(self, func):
        self.ready.append(func)  # 2-30-45-60-75
        logging.info(f"cola: {self.ready}")  # 3-16-31-46-61-76

    def run(self):
        while self.ready:  # 6-20-35-50-65-80-89
            logging.info(f"a-cola: {self.ready}")  # 7-21-36-51-66-81
            func = self.ready.popleft()  # 8-22-37-52-67-82
            logging.info(f"d- cola: {self.ready}")  # 9-23-38-53-68-83
            func()  # 10ejecutacount-19terminocount*repite-24ejectacount-34terminocount*repite-39ejecutacount-49terminocount*repite-54-64-69-79fin-fun-retorconta*repitewhile-84-ejecutarcount-88


shed = Scheduler()


def countdouwn(n):
    if n > 0:  # 12-26-41-56-71-86
        logging.info(f"Regresiva: {n}")  # 13-27-42-57-72
        time.sleep(1)  # 14-28-43-58-73
        # 15guardarcola-17returguardacola-25agsself-29guardacola-32regresacola-33returcountself-40argsself-44guardacola-47regresocola-48returcountself-55argsself-59-62-63-70args-self-74cola-77retorno-cola
        shed.call_soon(lambda: countdouwn(n-1))
        # 78retorno-run-85-args-87


shed.call_soon(lambda: countdouwn(5))  # 1guarda-cola-4regre-cola-11argscount-18raturnocount
shed.run()  # 5-90fin
