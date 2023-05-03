# Archivo: test_hilos_cpub.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/05/2023
# Descripción: Test de rendimiento con Hilos en tarea CPU BOUND


import threading
import time
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


def count(n):
    while n > 0:
        n -= 1


start = time.time()
count(10000000)
count(10000000)
end = time.time()
logging.info(f"secuencial {end-start}")
start = time.time()

# comente el hilo 2 pra que pueda ver la diferencia en el
# tiempo de ejecución
t1 = threading.Thread(target=count, args=(10000000,))
t2 = threading.Thread(target=count, args=(10000000,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
logging.info(f"Hilos {end-start}")
