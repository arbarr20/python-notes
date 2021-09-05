# copipe.py
#
# Un ejemplo simple que muestra cómo conectar una tubería con
# corrutinas. Para ejecutar esto, necesitará un archivo de registro.
# Ejecute el programa logsim.py en segundo plano para obtener datos
# fuente.

from coroutine import coroutine

# Una fuente de datos. Esta no es una corrutina, pero envía
# datos en uno (TARGET)

import time

# No corrutina (consumidor) Empuja los datos
def follow(thefile, target):
    thefile.seek(0, 2)      
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)    
            continue
        target.send(line)

# Corrutina pipeline de Filtrado
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)           
        if pattern in line:
            target.send(line)    

# Corrutina pipeline vertedero
@coroutine
def printer():
    while True:
        line = (yield)
        print (line,)


# Ejemplo de USO
if __name__ == '__main__':
    f = open("access-log")
    follow(f,grep('python',printer()))
