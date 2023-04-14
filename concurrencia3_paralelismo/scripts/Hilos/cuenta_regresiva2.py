# Archivo: cuenta_regresiva2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 14/04/2023
# Descripción: Definir un Hilo en una función. se muestra como asignar un hilo
# para le ejecución de una función

import threading
import logging
import time

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


def cuenta_regresiva(cuenta: int) -> None:
    while cuenta > 0:
        logging.info(f"Cuenta Regresiva, {cuenta}")
        cuenta -= 1
        time.sleep(1)
    return


# ejemplo de ejecución
t1 = threading.Thread(target=cuenta_regresiva, args=(5,))
t1.start()
# si deseas modificar la secuencia por defecto de los hilos, puedes usar .join()
# por ejemplo, si deseas que el hilo t1 ejecute todo su código y luego t2 ejecute el suyo,
# puedes descomentar la siguiente linea
# t1.join()
t2 = threading.Thread(target=cuenta_regresiva, args=(10,))
t2.start()
