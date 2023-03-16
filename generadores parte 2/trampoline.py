# trampoline.py
#
# Un ejemplo simple de un trampolin entre corrutinas


# Funcion-subrrutina-corrutina
def add(x,y):
    yield x+y

# una corrutina - funcion- que llama una subrrutina-funcion-generador etc
def main():
    r = yield add(2,2)
    print (r)
    yield

def run():
    m      = main()       
    #Un ejemplo de un trampolin
    sub    = m.send(None)             
    result = sub.send(None)
    m.send(result)

run()

