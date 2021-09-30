# sockwrap.py
#
# Envoltorio de corrutina alrededor de un objeto de socket

from pyos8 import *

class Socket(object):
    def __init__(self,sock):
        self.sock = sock
    def accept(self):
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        yield Socket(client), addr
    def send(self,buffer):
        while buffer:
            yield WriteWait(self.sock)
            len = self.sock.send(buffer)
            buffer = buffer[len:]
    def recv(self, maxbytes):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxbytes)
    def close(self):
        yield self.sock.close()
