# netsend.py
#
# Consumir lineas y enviarlos a una máquina remota

import socket, pickle

class NetConsumer(object):
    def __init__(self,addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(addr)
    def send(self,item):
        pitem = pickle.dumps(item)
        self.s.sendall(pitem)
    def close(self):
        self.s.close()

# Ejemplo de uso. Esto requiere que primero ejecute receivefrom.py.

if __name__ == '__main__':
    from broadcast import broadcast
    from follow import follow
    from apachelog import apache_log

    # Una clase que envía solicitudes 404 a otro host
    class Stat404(NetConsumer):
        def send(self,item):
            if item['status'] == 404:
                NetConsumer.send(self,item)
    
    stat404 = Stat404(("",15000))
    
    lines = follow(open("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[stat404])