# genfind.py
#
# Una función que genera ficheros que coinciden con un patrón de nombre de archivo dado

from pathlib import Path

def gen_find(filepat, top):
    # from: ir a este generador, ejecute lo que hay  en el y regrese
    yield from Path(top).rglob(filepat)

# Ejemplo de uso

if __name__ == '__main__':
    lognames = gen_find("access-log*","www")
    for name in lognames:
        print(name)