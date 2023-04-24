# Archivo:sinc_hilo_semaforo.py
# Autor: Arbarr20 y ayuda online
# Fecha: 24/04/2023
# Descripción: uso de semáforos para la sincronización de hilos

import time
import threading
import logging


logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)

"""
Los hilos se suichean solos, lo que hacemos es orientarlos, controlarlos en zonas críticas, como a
la hora de acceder a memoria compartida
"""

done = threading.Semaphore(0)
item = None
# contador = 0 el hilo se bloquea
# contador > 0 se adquiere el semáforo y decrementa contador


def producer():
    global item

    logging.info("Soy el productor y produzco datos.")
    logging.info("El productor va a dormir.")
    # cuando este hilo se pausa por alguna razón, ya sea por que esta haciendo una tarea de I/O
    # o esta esperando como en este caso, sucede un suicheo automático de hilo
    time.sleep(5)
    item = "Hola"
    logging.info("El productor está vivo. Señalando al consumidor.")
    done.release()


def consumer():
    logging.info("Soy un consumidor y estoy esperando datos.")
    logging.info("El consumidor está esperando.")
    # es importante tener en cuanta el contador del semaforo, en este caso, como
    # el contador vale 0 el acquire ESPERA y hasta que el otro hilo lo libere
    done.acquire()
    logging.info(f"Consumidor obtiene {item}")


# al parecer el primer hilo que se ejecute, es el primer que adquiere el semáforo implícitamente
# en este caso es t1 producer
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
