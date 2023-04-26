# Archivo: sinc_hilo_event_barriee.py
# Autor: Arbarr20 y ayuda online
# Fecha: 26/04/2023
# Descripción: Sincronización de hilos con event

import time
import threading
import logging


logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


init = threading.Event()


def worker():
    logging.info("Pronto estaré trabajando")
    init.wait()        # Esperar hasta que esté inicializado.
    logging.info("Estoy trabajando")


def initialize():
    logging.info("Inicializando Datos")
    time.sleep(5)
    logging.info("Desbloqueando trabajadores")
    init.set()


# Lanzan varios hilos para ejecutar la función worker
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

# Ir a inicializar y eventualmente desbloquear a los trabajadores.
initialize()
