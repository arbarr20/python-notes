# Archivo: multiprocessing-pipes.py
# Autor: Arbarr20 y ayuda online
# Fecha: 13/05/2023
# Descripción: Comunicando procesos con pipes

"""
Este script es un ejemplo de cómo utilizar el módulo multiprocessing de Python para implementar un 
programa con múltiples procesos que se comunican a través de pipes. El programa consiste en un 
productor que envía datos a un consumidor a través de un pipe.

El productor y el consumidor se ejecutan en procesos separados, lo que permite que la comunicación 
 ellos se realice de forma asíncrona. El productor envía una secuencia de datos a través del pipe y 
 el consumidor los recibe y los procesa.

La función consumer() recibe los datos del productor a través de un extremo del pipe y los procesa. 
La función producer() envía los datos al consumidor a través del otro extremo del pipe. El programa 
utiliza la función multiprocessing.Pipe() para crear el pipe y pasar los extremos correspondientes 
a las funciones consumer() y producer().
"""
import logging
import time
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


def consumer(p1, p2) -> None:
    """
    Recibe los datos de Producer.

    Args:
        p1: Extremo del Productor.
        p2: Extremo del Consumidor.
        
    Raises:
        EOFError: Cuando se termina la lectura del Pipe.
    """

    logging.info(f'Close-Prod in CONsu:{p1.close()}')

    while True:
        try:
            item = p2.recv()
            time.sleep(1)
        except EOFError:
            break
        logging.info(f"H-recibe del padre-Producer: {item}")


def producer(sequence: range, output_p) -> None:
    """
    Envia los datos al consumidor.

    Args:
        sequence: Una secuencia de datos a enviar.
        output_p: El extremo de entrada del objeto Pipe.
    """
    for item in sequence:
        logging.info(f'Padre enviando {item}')
        output_p.send(item)
        time.sleep(1)


if __name__ == '__main__':
    p1, p2 = multiprocessing.Pipe()

    cons = multiprocessing.Process(
        target=consumer,
        args=(p1, p2))
    cons.start()

    logging.info(f'Close-CON:{p2.close()}')

    sequence = range(5)
    producer(sequence, p1)

    logging.info(f'Close-Prod:{p1.close()}')
