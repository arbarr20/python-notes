# Archivo: sinc_hilo_lock2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 17/03/2023
# Descripción: Sincronización de hilos con lock y with.

import threading
import time
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)
counter_lock: threading.Lock = threading.Lock()
counter = 0


def increment():
    global counter
    for i in range(10):
        """ counter_lock.acquire()
        counter += 1
        time.sleep(1)
        logging.info(counter)
        counter_lock.release() """
        with counter_lock:
            counter += 1
            time.sleep(1)
            logging.info(counter)


if __name__ == "__main__":
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # aunque estamos diciendo que no se muestre el valor del hilo principal, hata que los 2 hilos
    # t1 y t2 (join) terminene.
    # observe la ejecución del script y vera que la secuencia tiene errores.
    logging.info(f"Valor final del contador:, {counter}")
