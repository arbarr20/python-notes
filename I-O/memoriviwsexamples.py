
# memoryview accede al buffer de una variable, No a la memoria donde esta 
# la variable, asi es como lo veo yo
s1 = b'hello word'
s1view = memoryview(s1)
print(f"s1view: {s1view}") #s1view: <memory at 0x10da2b400>
for ch in s1view:
    
    print(chr(ch),end="")
print()

#-------------------------------------------------------------------
# memoryviews soporta slicing y  el indexado
#-------------------------------------------------------------------
print("*"*15+" memoryviewsslicing- indexado"+"*"*15)
#indexado
s1 = b'hello world'
s1view = memoryview(s1)
#observe que en el indexado muestra los valores que corresponden al caracter
# sin tener que iterar
print(f"s1view[0]: {s1view[0]}")
print(f"s1view[-3]: {s1view[-3]}")

# slicing
#toca convertirlos a bytes u otra cosa lista, tuple, para ver algo legible
print(f"s1view[6:12]: {s1view[6:12]}")
print(f"s1view[6:12]: {bytes(s1view[6:12])}")

#-------------------------------------------------------------------
# memoryview en array
#-------------------------------------------------------------------
print("*"*15+"memoryview en array"+"*"*15)
import array
from typing import cast

nums = array.array('i',range(1,11))
numsview= memoryview(nums)

#indexing
print(f"numsview[-1]: {numsview[-1]}")
# slicing
print(f"numsview[3:6]: {numsview[3:6].tolist()}")

#-------------------------------------------------------------------
# memoryview modificando objetos
#-------------------------------------------------------------------
print("*"*15+"memoryview modifiying obj"+"*"*15)
s1 = b'hello world'
s2 = bytearray(b'hello world')
s1view=memoryview(s1)
s2view = memoryview(s2)
print(f" bytes is readonly:{s1view.readonly}")
print(f" bytearray is readonly:{s2view.readonly}")

# modifiying bytearray 
s2 = bytearray(b'hello world!')
s2view = memoryview(s2)
print(f"before: {s2}")
s2view[6:12]= b'python'  # s2view es como un puntero a s2
print(f"after: {s2}")

#-------------------------------------------------------------------
# memoryview functions
#-------------------------------------------------------------------
print("*"*15+"memoryview functions"+"*"*15)

# tolist() retorna  los datos del buffer como una lista de elementos

num = array.array('i',range(1,11))
n_view = memoryview(num)
print(n_view.tolist())


#toreadonly()
s1 = bytearray(b'hello world!')
s1view=memoryview(s1)
print(f"s1view: {s1view.readonly}")

s1ROview= s1view.toreadonly()
print(f"s1ROview: {s1ROview.readonly}")

#tobytes(order=None) Retorna los datos de buffer como un string de bytes
# esto es lo mismo que llamar bytes(mview)
num = array.array('i',range(1,11))
n_view = memoryview(num)
print(f"tobytes: {n_view.tobytes()}")
print(f"bytes: {bytes(n_view)}")

#hex([sep[,bytes_per_sep]]) retorna un objeto string que contiene 2 digitos hexadecimal por cada byte en el buffer
#sep: separar entre bytes
#bytes_per_sep: numero de bytes por separador

s1 = b'hello world'
s1view = memoryview(s1)
print(f"hex(): {s1view.hex()}")
print(f"hex(':'):{s1view.hex(':')}")
print(f"hex(':',2):{s1view.hex(':',2)}")

#release():Libera el búfer subyacente expuesto por el objeto memoryview. Muchos objetos 
# realizan acciones especiales cuando se mantiene una vista sobre ellos (por ejemplo, 
# a bytearray prohibiría temporalmente el cambio de tamaño); por lo tanto, llamar a release () 
# es útil para eliminar estas restricciones (y liberar cualquier recurso pendiente) lo antes posible.
#Después de que se haya llamado a este método, cualquier operación adicional en la vista
# genera un ValueError(excepto él release()mismo, que se puede llamar varias veces)

s1 = b'hello world'
s1view = memoryview(s1)
print(f" antes de release: {s1view.tobytes()}")
s1view.release() # vacia el buffer del memoryview, pero no afecta a s1 que es el objeto original
print(f"s1: {s1}")
try:
    print(f"s1view[6:12]: {s1view[6:12]}") # acceder al memory view despues de relesase levanta unerror
except:
    print("no se puede hacer esta operacion despues de release")

# El protocolo de gestión de contexto se puede utilizar para un efecto similar, utilizando la declaración with:

s1 = b'hello world'
with memoryview(s1) as s1view:
    print(bytes(s1view[6:12]))

#cast: para modificar un objeto cast(format[, shape])
#format: 'B' (signed char), 'b'(unsigned char) or 'c' char
#sheape: byte_lenght // new_itemsize el resultado del memory view es de una dimencion

s1 = b'hello world' # no se p uede modificar
s1view = memoryview(s1)
try:
    s1view[0]= b'H'
except:
    print("s1view[0]= b'H' no se purde realizar")

#modificando con cast un bit
s1 = bytearray(b'hello world!')
s1view = memoryview(s1)
s1viewcast = s1view.cast('c')
print(f"before:{s1}")
s1viewcast[0]=b'H'
print(f"after:{s1}")

#cating 1d ints to 2d and 3d ints
#shape[3,4] de los datos pasados conviertoa a una matriz 3*4
#shape[2,2,3] de los datos pasados convierta a 2 matrises de 2*3
#shape[2,3,2] de los datos pasados convierta a 2 matrises de 3*2
import struct

buffer= struct.pack('12i',*range(1,13))
print(f"buffer: {buffer}")
n1D= memoryview(buffer)
print(f"n1D={n1D.tolist()}")
n2D =n1D.cast('i',shape=[3,4])
print(f"n2Dshape[3,4]= {n2D.tolist()}")

n3D = n1D.cast('i', shape=[2,2,3])
print(f"n3Dshape[2,2,3]= {n3D.tolist()}")

n3D = n1D.cast('i', shape=[2,3,2])
print(f"n3Dshape[2,3,2]= {n3D.tolist()}")

#-------------------------------------------------------------------
# memoryview Atributes
#-------------------------------------------------------------------
print("*"*15+"memoryview Atributes"+"*"*15)

#obj: retorna el objeto al que esta haciendo referencia el memoryview
# supuntero, al objeto qu eesta apuntando
s1 = bytearray(b'hello world!')
s1view = memoryview(s1)
print(s1view.obj)
print(s1view.obj is s1)

#nbytes (cuenta los bytes reales) no cuantos elementos hay tener cuidado
#nbytes == product(shape) * itemsize == len(m.tobytes()).
#Esta es la cantidad de espacio en bytes que usaría la matriz en 
# una representación contigua. No es necesariamente igual a len (m):

import struct
buffer = struct.pack('5i',*range(1,6))
b1view = memoryview(buffer)
print('\nlen: ',len(b1view))
print(f"nbytes: {b1view.nbytes}")

# caso 2 cuando len(obj) !=nbytes
import array
array1 = array.array('i',range(1,6))
b2view = memoryview(array1)
print('len: ',len(b2view))
print(f"nbytes: {b2view.nbytes}")

#readonly
#Un bool que indica si la memoria es de solo lectura.
s1 = b'hello world'
s2 = bytearray(b'hello world')

s1view = memoryview(s1)
s2view = memoryview(s2)

print(f"\nBytes view is readonly?: {s1view.readonly}")
print(f"ByteArray view is readonly?: {s2view.readonly}")

#format
#Una cadena que contiene el formato (en estilo struct de módulo) 
# para cada elemento de la vista. Se puede crear una vista de memoria
#  a partir de exportadores con cadenas de formato arbitrario, pero algunos
#  métodos (por ejemplo tolist()) están restringidos a formatos nativos de un solo elemento.
#Modificado en la versión 3.3: el formato 'B'ahora se maneja de acuerdo con la
# sintaxis del módulo de estructura. Esto significa eso .memoryview(b'abc')[0] == b'abc'[0] == 97

import struct
s1=struct.pack('13si',b'hello world',127)
s1view= memoryview(s1)
print(f"\nformats1view: {s1view.format}")

#itemsize
#El tamaño en bytes de cada elemento de la vista de memoria:
import array
array2= array.array('l',range(1,6))
print(array2)
a2view = memoryview(array2)
print(a2view.itemsize)

#ndim
#Un número entero que indica cuántas dimensiones de una matriz multidimensional representa la memoria.
# no entiendo muy bien a que se refiere, es como la cantidad de listta anidadas [una diemencion],[[ dos diemnciones]]
#[[[tres dimenciones]]]
import struct

buffer= struct.pack('12i',*range(1,13))
print(f"\nbuffer: {buffer}")
n1D= memoryview(buffer)
print(f"n1D={n1D.tolist()}")
print(f"n1d.ndin= {n1D.ndim}")
n2D =n1D.cast('i',shape=[3,4])
print(f"n2Dshape[3,4]= {n2D.tolist()}")

print(f"n2d.ndin= {n2D.ndim}")
n3D = n1D.cast('i', shape=[2,2,3])
print(f"n3Dshape[2,2,3]= {n3D.tolist()}")
print(f"n3d.ndin= {n3D.ndim}")

n3D = n1D.cast('i', shape=[2,3,2])
print(f"n3Dshape[2,3,2]= {n3D.tolist()}")
print(f"n3d.ndin= {n3D.ndim}")



#shape
#Una tupla de números enteros cuya longitud ndim da la forma de la memoria como una matriz N-dimensional.
#esto arroja una tupla asi n3D=(2,3,2) significa (2 matrices, de 3 filas cada una,de 2columnas cada una)
#Modificado en la versión 3.3: una tupla vacía en lugar de None cuando ndim = 0.
print(f"\nn1D={n1D.tolist()}")
print(f"n1d.shape= {n1D.shape}")
print(f"n2Dshape[3,4]= {n2D.tolist()}")
print(f"n2d.shape= {n2D.shape}")
print(f"n3Dshape[2,3,2]= {n3D.tolist()}")
print(f"n3d.shape= {n3D.shape}")



#strides (pasos,zancadas):Los strides (pasos) son la cantidad de bytes que se deben saltar en la memoria para pasar
# de un elemento al siguiente elemento a lo largo de cada dirección / dimensión de la matriz.
# ejemplo de matriz de 2 dimenciones = [[]] anque en matematicas es 3 dimenciones
#       [[1, 2, 3], itemsiza=4- strides(12,4)
#       [4, 5, 6],
#       [7, 8, 9]]
# para ir de de a 1 hay que recorrer 4 bytes,
#para ir de 1 a 4 hay que recorrer toda laprimer fila y luegollegar a 4, para esto se recorrieron 8bytes
# entonces para recorrer desde 1 a 7 hay que recorrer  12 bytes
# strides (numero de bytes a recorrer desde 1 a 7, numero de bytes a recorrer desde 1 a 2 )
#strides(maximo nuemro de bytes a recorrer, minimo numero de bytes a recorrer)
# buenoexpicacion aqui:https://stackoverflow.com/questions/53097952/how-to-understand-numpy-strides-for-layman


# otra definicion: Una tupla de números enteros cuya longitud ndim indica el tamaño en bytes para acceder 
# a cada elemento de cada dimensión de la matriz.
#n3d.stride= (24, 8, 4)
# itemsiza=4
#       [[[1, 2],       [[7, 8],  
#        [3, 4],         [9, 10],
#        [5, 6]],        [11, 12]]]
#   stride= (#bytes de 1 a 11, #bytes de 1 a 5, #bytes de 1 a 2)   
# #n3d.stride= (24, 8, 4) =  (totalque pesa cada matriz, peso de cada fila de cada matriz, lo que pesa cada elemento de cada matriz)

# strides fue Modificado en la versión 3.3: una tupla vacía en lugar de Nonecuando ndim = 0.     

print(f"\nn1D={n1D.tolist()}")
print(f"itemsize: {n1D.itemsize}")
print(f"n1d.stride= {n1D.strides}")
print(f"n2Dshape[3,4]= {n2D.tolist()}")
print(f"itemsize: {n2D.itemsize}")
print(f"n2d.stride= {n2D.strides}")
print(f"n3Dshape[2,3,2]= {n3D.tolist()}")
print(f"itemsize: {n3D.itemsize}")
print(f"n3d.stride= {n3D.strides}")

#contiguous: Un bool que indica si la memoria es contigua .


import struct
buffer = struct.pack('12i',*range(1,13))
n1D= memoryview(buffer)
n2D = n1D.cast('i', shape=[3,4])
print(f"\ncast('i', shape[3,4]:  ")
print(n2D.tolist())
print(f"ndim: {n2D.ndim}")
print(f"lenght: {len(n2D)}")
print(f"shape: {n2D.shape}")
print(f"strides: {n2D.strides}")
print(f"contiguous: {n2D.contiguous}")

# accesado a elementos de una matriz
#n3D[(0,1,1)]
#n3D[entregueme el valor (de la matriz 0, la fila 1, columna1)]
import struct
buffer = struct.pack('12i',*range(1,13))
n1D= memoryview(buffer)
n3D = n1D.cast('i', shape=[2,2,3])
print(f"\nn3D.tolist: {n3D.tolist()}")
print(f"n3D[(0,1,1)]: {n3D[(0,1,1)]}")
print(f"n3D[(1,0,1)]: {n3D[(1,0,1)]}")

#c_contiguous
#Un bool que indica si la memoria es C- contigua .
#f_contiguous
#Un bool que indica si la memoria es contigua a Fortran .

import struct

buffer= struct.pack('12i',*range(1,13))
n1D= memoryview(buffer)
print(f"\nc_contiguous: {n1D.c_contiguous}")
print(f"c_contiguous: {n1D.f_contiguous}")


#-------------------------------------------------------------------
# ejemplo de optimizacion con memoryview
#-------------------------------------------------------------------
print("*"*15+"optimizacion con memoryview"+"*"*15)

from timethis import timethis

with timethis ("sin buffer"):
    for n in (100000,200000,300000,400000):
        data = b'x'*n
        b=data
        while b:
            b = b[1:]
        print(f"bytes {n}")

with timethis ("memori view"):
    for n in (100000,200000,300000,400000):
        data = b'x'*n
        b=memoryview(data)
        while b:
            b = b[1:]
        print(f"memori view {n}")