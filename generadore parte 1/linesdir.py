# linesdir.py
#
# Genera una secuencia de líneas a partir de archivos en un directorio

from pathlib import Path
from gencat import *
from genopen import *

def lines_from_dir(filepat, dirname):
    names = Path(dirname).rglob(filepat)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines

# ejemplo de uso

if __name__ == '__main__':
    loglines = lines_from_dir("access-log*","www")
    for line in loglines:
        print(line, end='')