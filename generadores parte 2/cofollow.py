# cofollow.py
#
# Un ejemplo simple que muestra cómo conectar una tubería con
# corrutinas. Para ejecutar esto, necesitará un archivo de registro.
# Ejecute el programa logsim.py en segundo plano para obtener datos
# fuente.

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

# Un Vertedero. Una corrutina que recibe datos


@coroutine
def printer():
    while True:
        line = (yield)
        print("\n", line,)


# Ejemplo de Uso
if __name__ == '__main__':
    f = open("access-log")
    follow(f, printer())



