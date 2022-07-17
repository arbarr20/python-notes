# iterlines.py
#
# Iterar sobre las líneas de un archivo usando open() nativo

from timethis import timethis

with timethis("Iterate over lines"):
    for line in open("Mastering-Python-3-I0/files/access-log"):
        pass
