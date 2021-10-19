# consumer.py
#
# consumer decorator and co-routine example

def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        c.send(None) # es una obligacion inicializar el generador
        return c
    return start

# Ejemplo
if __name__ == '__main__':

    @consumer # para inicializar el generador
    def recv_count():
        try:
            while True:
                n = yield
                print("T-minus", n)
        except GeneratorExit:
            print("Kaboom!")

    r = recv_count()
    for i in range(5,0,-1):
        r.send(i)

    r.close()