# echogood.py
#
# Otro intento en un servidor de eco. Este funciona porque
# de las operaciones de E / S en espera que suspenden las tareas cuando hay
# no hay datos disponibles. Comparar con echobad.py



from socket import *
from pyos7coment import *

def handle_client(client,addr):
    print ("Connection from", addr)
    while True:
        yield ReadWait(client)
        data =client.recv(65536) 
        print(f"Cliente send: {data.decode()}",end='')
        if not data:
            break
        yield WriteWait(client)
        client.send(b"Server response: "+data)
    client.close()
    print ("Client closed")

def server(port):
    print ("Server starting")
    sock = socket(AF_INET,SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(("",port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client,addr = sock.accept()
        yield NewTask(handle_client(client,addr))    

def alive():
        while True:
            print ("I'm alive!")
            yield

sched = Scheduler()
#.new(alive())
sched.new(server(45000))
sched.mainloop()
