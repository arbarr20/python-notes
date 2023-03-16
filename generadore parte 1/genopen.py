
# genopen.py
#
# Toma una secuencia de nombres de archivos como entrada y produce una secuencia 
# file object que son  abiertos adecuadamente

import gzip, bz2

def gen_open(paths):
    for path in paths:
        if path.suffix == '.gz':
            yield gzip.open(path, 'rt')
        elif path.suffix == '.bz2':
            yield bz2.open(path, 'rt')
        else:
            yield open(path, 'rt')

# Ejemplo de uso

if __name__ == '__main__':
    from pathlib import Path
    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    for f in logfiles:
        print(f)