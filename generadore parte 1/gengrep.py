# gengrep.py
#
# Grep (filtrar) una secuencia de líneas que coinciden con un patrón re

import re
def gen_grep(pat, lines):
    patc = re.compile(pat)
    return (line for line in lines if patc.search(line))

# Ejemplo de uso

if __name__ == '__main__':
    from pathlib import Path
    from genopen import  gen_open
    from gencat  import  gen_cat

    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    """
    patron:r'ply-.*\.gz' traduce:
    cualquier linea que contenga  (ply- cuantas veces cualquiercosa,pero
    que termine con .gz)   """
    
    plylines = gen_grep(r'ply-.*\.gz',loglines)
    for line in plylines:
        print(line, end='')