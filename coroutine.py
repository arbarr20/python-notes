# coroutine.py
#
# Una función de decorador que se encarga de iniciar una corrutina
# automáticamente en llamada

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

# Ejemplo de uso
if __name__ == '__main__':
    @coroutine
    def grep(pattern):# esta es una funcion = corrutina
        print ("Buscando el patron %s" % pattern)
        while True:
            line = (yield)
            if pattern in line:                
                print (line,)
    g = grep("python")
    # Observe cómo no necesita la llamada next () aqui
    g.send("Esta linea no tiene el patron")
    g.send("Estamos en la seccion de Corrutinas")  
    g.close()  
    g.send("python Generadors y corrutinas Encontrando!")
    
   
    
