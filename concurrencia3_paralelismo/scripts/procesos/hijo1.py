# Archivo: hijo1.py
# Autor: Arbarr20 y ayuda online
# Fecha: 12/05/2023
# Descripción: 


import sys
import padre1
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


ch = padre1.Channel(sys.stdout.buffer, sys.stdin.buffer)
while True:
    try:
        item = ch.recv()
        # esta validación fue dispensable para decirle al proceso hijo
        # cuando se termina la transmisión de datos
        if item == "fin de datos":
            break
        logging.debug(f"P-Hijo recibe:{item} tipo:{type(item)}")
        ch.send(("P-Hijo Envia:", "Hola Padre"))
    except EOFError:
        break
