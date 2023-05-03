# Archivo: test_proces_cpub.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/05/2023
# Descripción: Test de rendimiento con procesos en tarea CPU BOUND


"""
La función "freeze_support" se utiliza para que el programa principal solo se ejecute si no está en
un proceso secundario. Esto ayuda a prevenir errores y problemas relacionados con la ejecución del
código de manera inapropiada en procesos secundarios.
"""
import time
import multiprocessing
import logging
from multiprocessing import freeze_support

logging.basicConfig(format='[%(processName)s] %(message)s', level=logging.DEBUG)


def count(n):
    while n > 0:
        n -= 1


start = time.time()
count(10000000)
count(10000000)
end = time.time()
logging.info(f"Secuencial demora: {end-start}")

if __name__ == '__main__':
    # comente el proceso 2 pra que pueda ver la diferencia en el
    # tiempo de ejecución
    freeze_support()
    start = time.time()
    p1 = multiprocessing.Process(target=count, args=(10000000,))
    p2 = multiprocessing.Process(target=count, args=(10000000,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    logging.info(f"Multiprocesos demora: {end-start}")
