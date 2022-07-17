# structwrite.py
#
# An example of writing a binary-packed data structure

from timethis import timethis
import struct
from random import random


# Crear un millón de puntos aleatorios (x,y) 
points = [(random(),random()) for n in range(1000000)]



# Escribir en un archivo usando write() y struct.pack()
# cada tupla se va empaquetando una por una
with timethis("Writing many small structs"):
    f = open("pts1.bin","wb")
    f.write(struct.pack("I",len(points)))
    for p in points:
        f.write(struct.pack("ff",*p))
    f.close()

# Empaqueta un bytearray y escríbelo todo de una vez
with timethis("Packing a bytearray and writing"):
    out = bytearray() # Creando una secuencia vacía
    out.extend(struct.pack("I",len(points)))#Creando una instancia de una longitud determinada, rellena con ceros

    for p in points:
        out.extend(struct.pack("ff",*p))# se cncatenan todos los vlores en un array (memoriview)      
    f = open("pts2.bin","wb")
    f.write(out) # despues de concatenadas con extend se escriben TODOS de golpe en elfihero
    f.close()



