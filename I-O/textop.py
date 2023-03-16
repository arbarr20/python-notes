# textop.py
#
# Un programa que lee una gran colección de texto en la memoria.
# y realiza varias operaciones en él. Esto debería funcionar en ambos
# Python 2 y Python 3. Úselo para comparar el rendimiento.

NSAMPLES = 10
from timethis import timethis
import sys

# Leer un archivo de registro de Apache en la memoria y replicarlo para hacer una muestra grande.
# El resultado debe ser una cadena con alrededor de 6 millones de caracteres.
logdata = open("Mastering-Python-3-I0/files/access-log","rt").read()*10


# Test 1: Uso de Memoria
print("Tamaño : %d bytes" % sys.getsizeof(logdata))

# Prueba 2: Encontrar todas las líneas usando find () y separar
with timethis("encontrar líneas"):
    index = 0
    while index < len(logdata):
        nextindex = logdata.find("\n",index)
        line = logdata[index:nextindex]        
        index = nextindex+1

# Prueba 3: dividir en líneas
with timethis("dividir en líneas"):
    lines = logdata.splitlines()
    #print(lines)

# Prueba 4: División en espacios en blanco
with timethis("división de espacios en blanco"):
    fields = logdata.split()

# Prueba 5: Coincidencia de patrones de expresiones regulares.  
import re
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
with timethis("Coincidencia de patrones"):
    unique_ips = set()
    for m in ip_pattern.finditer(logdata):
        unique_ips.add(m.group())

# Prueba 6: Iterar por caracteres
with timethis("Iterar por caracteres"):
    for c in logdata:
        pass
        