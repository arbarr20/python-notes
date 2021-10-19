# follow.py
#
# Un generador que monitorea un archivo de registro como Unix 'tail -f'.
#
# Nota: Para que este ejemplo funcione, debe solicitar
# un archivo de registro del servidor activo. Ejecute el programa "logsim.py"
# en segundo plano para simular dicho archivo. Este programa
# escribirá las entradas en un archivo "access-log".
import time
def follow(thefile):        
    thefile.seek(0, 2)     
    while True:                          
        line = thefile.readline()           
        if not line:            
            time.sleep(0.1) 
            continue            
        yield line


# Ejemplo de Uso
if __name__ == '__main__':
    logfile = open("access-log")
    for line in follow(logfile):        
        print ("\n",line)