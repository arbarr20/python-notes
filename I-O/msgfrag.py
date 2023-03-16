# msgfrag.py
#
# Tres técnicas diferentes para formar un mensaje grande a partir de fragmentos de bytes.

from timethis import timethis

FRAGMENT_SIZE = 256
NUMBER_FRAGS  = 10000

# Un generador que crea fragmentos de bytes para nosotros
def make_fragments(size,count):
    frag = b"x"*size
    while count > 0:
        yield frag        
        count -= 1

#Prueba la concatenación de bytes
with timethis("Concatenacion de bytes +="):
    msg = b""
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msg += chunk
    

# .join()
with timethis("Uniendo lista de fragmentos"):
    msgparts = []
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msgparts.append(chunk)
    msg = b"".join(msgparts)

# bytearray.extend
with timethis("Extendiendo bytearray"):
    msg = bytearray()
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msg.extend(chunk)



