# Archivo: colas_join_done.py
# Autor: Arbarr20 y ayuda online
# Fecha: 03/05/2023
# Descripción: Un ejemplo de uso de colas para establecer problemas de productor/consumidor.
# esta vez usando los señalizadores task_done() y q.join()

import threading
import queue
import logging

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)

# en Function Annotations asi de pone que la cola q contiene una lista
# de elementos enteros
q: queue.Queue[int] = queue.Queue()


def worker() -> None:
    while True:
        logging.info(f"cola: {q.queue}")
        item: int = q.get()
        logging.info(f'Trabajando en {item}')
        logging.info('tarea completada')
        q.task_done()


# Enciende el hilo del trabajador
cons = [threading.Thread(target=worker)for i in range(3)]
for c in cons:
    c.daemon = True
    c.start()

# Enviar treinta solicitudes de tarea al trabajador
for item in range(5):
    q.put(item)
    logging.info(f"Poniendo el item {item}")

# Bloquear hasta que se completen todas las tareas.
logging.info("esperando hasta que todas las tareas terminen")
q.join()
print('Todo el trabajo ha sido completado')
