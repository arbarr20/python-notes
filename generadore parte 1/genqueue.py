# genqueue.py
#
# Genera una secuencia de elementos que se colocan en una cola.

def genfrom_queue(thequeue):
    while True:
        item = thequeue.get()
        if item is StopIteration: 
            break
        yield item

def sendto_queue(items, thequeue):
    for item in items:
        thequeue.put(item)
    thequeue.put(StopIteration)

# Ejemplo de uso
if __name__ == '__main__':
    import queue, threading
    def consumer(q):
        for item in genfrom_queue(q):
            print("Consumido", item)
        print("hecho")

    in_q = queue.Queue()
    con_thr = threading.Thread(target=consumer,args=(in_q,))
    con_thr.start()

    # Ahora, canalice (pipe) un montón de datos a la cola
    sendto_queue(range(100), in_q)