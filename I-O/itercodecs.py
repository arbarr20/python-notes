# itercodecs.py
#
# Iterar sobre las líneas de un archivo usando codecs.open()()

from timethis import timethis
import codecs

with timethis("Iterate over lines (codecs,latin-1)"):
    for line in codecs.open("Mastering-Python-3-I0/files/access-log",encoding="latin-1"):
        pass

with timethis("Iterate over lines (native open)"):
    for line in open("Mastering-Python-3-I0/files/access-log"):
        pass
