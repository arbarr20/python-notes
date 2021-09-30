# echoserver.py
#
# A concurrent echo server using coroutines

from pyos8 import *
from socket import *

def handle_client(client,addr):
    print ("Conectado desde", addr)
    while True:
        data = yield Recv(client,65536)
        if not data:
            break
        yield Send(client,data)
    print ("Cliente Cerrado")
    client.close()


def server(port):
    print("Server Iniciando..")
    sock = socket(AF_INET,SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(("",port))
    sock.listen(5)
    while True:
        client,addr = yield Accept(sock)
        yield NewTask(handle_client(client,addr))

sched = Scheduler()
sched.new(server(45000))
sched.mainloop()
