# Archivo: multiprocessing-1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 12/05/2023
# Descripción: Cuenta regresiva con Multiprocesos


import time
import multiprocessing
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


class CountdownProcess(multiprocessing.Process):
    def __init__(self, count):
        # Es obligatorio iniciar la clase padre para que funcione bien
        multiprocessing. Process.__init__(self)
        self.count = count
    # este método esta sobre escrito, y se llama el momento de
    # ejecutar start()

    def run(self):
        while self.count > 0:
            logging.info(f"Cuenta Regresiva: {self.count}")
            self.count -= 1
            time.sleep(1)
        return


if __name__ == '__main__':
    p1 = CountdownProcess(10)  # Crea el objeto Proceso
    p1.start()                 # Lanzar el proceso

    p2 = CountdownProcess(5)   # Crea el objeto Procesos
    p2.start()                  # Lanzar el proceso
