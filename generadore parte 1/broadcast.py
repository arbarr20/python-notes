# broadcast.py
#
# Transmita una fuente generadora a una colección de consumidores

def broadcast(source, consumers):
    for item in source:
        for c in consumers:
            c.send(item)


# Ejemplo
if __name__ == '__main__':

    class Consumer(object):
        def send(self,item):
            print(self, "got", item)

    c1 = Consumer()
    c2 = Consumer()
    c3 = Consumer()

    from follow import follow
    lines = follow(open("run/foo/access-log"))
    broadcast(lines,[c1,c2,c3])