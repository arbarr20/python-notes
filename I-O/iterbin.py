# iterbin.py
#
# Iterar sobre las líneas de un archivo usando el modo binario

from timethis import timethis

with timethis("Iterate over lines (binary mode)"):
    for line in open("Mastering-Python-3-I0/files/access-log","rb"):
        pass

with timethis("Iterate over lines (unbuffered binary mode)"):
    for line in open("Mastering-Python-3-I0/files/access-log","rb",buffering=0):
        pass
