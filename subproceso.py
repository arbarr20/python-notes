import sys,pickle,io,time

hijo = "hola desde subproceso hijo"
print(hijo)

""" with open(sys.stdin.fileno(), 'rb') as f:
    datos_ds = pickle.load(f)
    #f.flush()
    print(f"desde hijo: {datos_ds}") """



""" entada_file_object= sys.stdin.buffer
try:
    while True:
        datos_ds = pickle.load(entada_file_object)              
        print(f"desde hijo: {datos_ds}")     
        
except Exception as e:

        print(f"Ocurrio un error: {e}")    """  
entada_file_object= sys.stdin.buffer
while True:
    try:
        if entada_file_object.read:
            datos_ds = pickle.load(entada_file_object)              
            print(f"desde hijo: {datos_ds}")
        else:
            break
    except Exception as e:
        
        print(f"Ocurrio un error: {e}")
        break
        







