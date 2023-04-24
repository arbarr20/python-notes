# Archivo: sinc_hilo_RLock.py
# Autor: Arbarr20 y ayuda online
# Fecha: 24/04/2023
# Descripción: Uso de Rlock, llamadas anidadas por por un Hilo al Lock, para que 
# otro holo lo pueda usar, el hilo anterior debe liberar Todas las adquisiciones
# del Lock

import time
import threading
import logging


logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


class Foo(object):
    lock = threading.RLock()

    def __init__(self):
        self.x = 0

    def add(self, n):
        with Foo.lock:
            logging.info(f"adquiere lok add {self.x}")
            self.x += n
            logging.info(f"libera lok add {self.x}")

    def incr(self):
        with Foo.lock:
            logging.info(f"adquiere lok incr {self.x}")
            self.add(1)
            time.sleep(1)
            logging.info(f"libera lok incr {self.x}")

    def decr(self):
        with Foo.lock:
            logging.info(f"adquiere lok decr {self.x}")
            self.add(-1)
            time.sleep(1)
            logging.info(f"libera lok decr {self.x}")


def adder(f, count):
    while count > 0:
        f.incr()
        count -= 1


def subber(f, count):
    while count > 0:
        f.decr()
        count -= 1


# Inicio de ejecución del script
COUNT = 5
f = Foo()
t1 = threading.Thread(target=adder, args=(f, COUNT))
t2 = threading.Thread(target=subber, args=(f, COUNT))
t1.start()
t2.start()
t1.join()
t2.join()
logging.info(f.x)
