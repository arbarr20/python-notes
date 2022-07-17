#iterenc.py
#
# Iterar sobre las líneas de un archivo usando tres codificaciones diferentes

from timethis import timethis
import codecs

with timethis("Iterate over lines (UTF-8)"):
    for line in open("Mastering-Python-3-I0/files/access-log",encoding='utf-8'):
        pass

with timethis("Iterate over lines (ASCII)"):
    for line in open("Mastering-Python-3-I0/files/access-log",encoding='ascii'):
        pass

with timethis("Iterate over lines (Latin-1)"):
    for line in open("Mastering-Python-3-I0/files/access-log",encoding='latin-1'):
        pass
