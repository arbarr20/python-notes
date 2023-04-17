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
    # aunque estamos diciendo que un hilo espere hasta que el otro termine,
    # observe la ejecución del script y vera que hay la secuencia tiene errores.
    logging.info(f"Valor final del contador:, {counter}")
