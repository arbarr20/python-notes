# Archivo: sinc_hilo_event2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 26/04/2023
# Descripción: Sincronización de hilos con event.


"""
La línea de código while True: if input() == "s": event.set() es un ciclo que espera a que el
usuario ingrese una letra "s" por la entrada estándar (es decir, por teclado) y luego establece el
evento event utilizando el método set() de threading.Event().

Cuando se establece el evento, la función do_something() que se está ejecutando en el hilo
secundario, puede continuar su ejecución. En particular, si el evento está activado, la función
imprimirá el valor actual de la variable count y luego incrementará count en 1. Este proceso se
repetirá hasta que count llegue a 10, momento en el que el evento se desactivará (event.clear() y
se reiniciará la cuenta en 0.

Para Parar la ejecución del programa oprima ctrl +C
"""
import logging
import threading
import time

logging.basicConfig(format='[%(threadName)s] %(message)s', level=logging.DEBUG)


def do_something(event: threading.Event) -> None:
    """
    Esta función espera hasta que el evento se active y luego imprime el valor de count.
    Después incrementa el valor de count en 1 y espera un segundo antes de volver a verificar
    si el evento se ha activado. Si count llega a 10, el evento se desactiva y count se establece
    en 0. Si el evento no se activa, la función continúa esperando indefinidamente.

    Args:
        event (threading.Event): un objeto threading.Event que se utiliza para sincronizar
                                 la ejecución entre los hilos.

    Returns:
        None

    Raises:
        No raise explícito.
    """
    count = 0
    while True:
        if count == 10:
            event.clear()
            logging.info("stop oprima s para iniciar seguido de enter")
            count = 0
        event.wait()
        logging.info(f"Count: {count}")
        count += 1
        time.sleep(1)


event = threading.Event()
t = threading.Thread(target=do_something, args=(event,))
t.start()

while True:
    logging.info("oprima s para iniciar seguido de enter")
    if input() == "s":
        logging.info("Iniciando contador..")
        event.set()
