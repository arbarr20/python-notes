# echoserver2.py
#
# Un servidor de eco concurrente que usa corrutinas

from pyos8 import *
from socket import *
from sockwrap import Socket

def handle_client(client,addr):
    print ("Conectado desde", addr)
    while True:
        data = yield client.recv(65536)#recv es metodo de nuestra clase Socket
        if not data:
            break
        yield client.send(data)# send es metodo de nuesta clase Socket
    print ("Cliente Cerrado")
    yield client.close() # close es metodo de nuestra clase Socket

def server(port):
    print ("Servidor Iniciando")
    rawsock = socket(AF_INET,SOCK_STREAM)
    rawsock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    rawsock.bind(("",port))
    rawsock.listen(1024)

    sock = Socket(rawsock) # se crea el objeto de nuestra clase Socket
    while True:
        client,addr = yield sock.accept()# se llaman los metodo de nuestra clase socket
        yield NewTask(handle_client(client,addr))

sched = Scheduler()
sched.new(server(45000))
sched.mainloop()
