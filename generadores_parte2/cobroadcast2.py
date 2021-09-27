# cobroadcast2.py
#
# Un ejemplo de transmisión de un flujo de datos a múltiples objetivos de rutina.
# Este ejemplo muestra "fan-in" --- una situación en la que múltiples corrutinas
# enviar al mismo objetivo.

from coroutine import coroutine


# Una fuente de datos. Esta no es una corrutina, pero envía
# datos en uno (target)

import time


def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

# Un Filtro.


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)           # Recibe la linea
        if pattern in line:
            target.send(line)    # La envia a la proxina estación

# A sink. Corrutina Final que recibe Tosa la data de todos los Targerts,
# se odria saturar


@coroutine
def printer():
    while True:
        line = (yield)
        print(line,)


# Transmita una transmisión a múltiples objetivos
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


# Example use
if __name__ == '__main__':
    f = open("access-log")
    p = printer()
    follow(f,
           broadcast([grep('python', p),
                      grep('ply', p),
                      grep('swig', p)])
           )



