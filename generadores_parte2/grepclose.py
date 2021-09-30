# grepclose.py
#
# Una corrutina que captura la operación close ()

from coroutine import coroutine
""" @coroutine
def grep(pattern):
    print ("Buacando el patron %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print (line,) """


@coroutine
def grep(pattern):
    print("Buacando el patron %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line,)    
    except GeneratorExit:
        print(f"except GeneratorExit")    
        


# Ejemplo de Uso
if __name__ == '__main__':    
    g = grep("python")
    g.send("Esta linea no tiene el patron")
    g.send("Estamos en la seccion de Corrutinas")
    g.send("python Generadors y corrutinas Encontrando!")
    g.close()