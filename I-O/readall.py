# readall.py
#
# Leer un archivo de texto de una sola vez

from timethis import timethis

with timethis("Read a text file"):
    data = open("Mastering-Python-3-I0/files/access-log").read()

with timethis("Read a binary file"):
    data = open("Mastering-Python-3-I0/files/access-log","rb").read()

