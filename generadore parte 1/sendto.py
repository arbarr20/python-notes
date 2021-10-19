# sendto.py
#
# Enviar lineas a una máquina remota

import socket
from genpickle import gen_pickle

def sendto(source,addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    for pitem in gen_pickle(source):
        s.sendall(pitem)
    s.close()

# Ejemplo de uso. Esto requiere que ejecute receivefrom.py
# en un proceso / ventana diferente

if __name__ == '__main__':
    from apachelog import apache_log
    from follow import follow

    lines = follow(open("run/foo/access-log"))
    log = apache_log(lines)
    sendto(log,("",15000))