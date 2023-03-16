# genmessages.py
#
# Un generador que genera mensajes en un socket UDP

import socket
def receive_messages(addr,maxsize):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
        msg = s.recvfrom(maxsize)
        yield msg

# Ejemplo de uso
# Para enviar un mensaje a este generador, use el código "msgtest.py"

if __name__ == '__main__':
    for msg, addr in receive_messages(("",10000),1024):
        print(msg, "from", addr)