# textformat.py
#
# Diferentes ejemplos de formato de texto ilustrados por la salida de
# mesa en diferentes formatos.

# El archivo stocks.csv tiene algunos datos bursátiles en formato CSV
# "símbolo", precio, cambio, volumen. Léelo en una lista de tuplas

stockdata = []
for line in open("Mastering-Python-3-I0/files/stocks.csv"):
    
    fields = line.split(",")
   
    record = (fields[0].strip('"'),float(fields[1]),float(fields[2]),int(fields[3]))
    print(record)
    stockdata.append(record)

print(stockdata)

# Formato de cadena tradicional

print("Traditional string formatting:")
for s in stockdata:
    print("%10s %10.2f %10.2f %10d" % s)

# Algunos ejemplos de formato de estilo nuevo
print("\nFormateo de nuevo estilo:")
for s in stockdata:
    print("{0:10s} {1:10.2f} {2:10.2f} {3:10d}".format(*s))

print("\nFormato de nuevo estilo con campos omitidos")
for s in stockdata:
    print("{:10s} {:10.2f} {:10.2f} {:10d}".format(*s))

print("\nFormateo de nuevo estilo con alineación:")
for s in stockdata:
    print("{0:>10s} {1:10.2f} {2:10.2f} {3:10d}".format(*s))

print("\nFormateo de nuevo estilo con indexación")
for s in stockdata:
    print("{0[0]:>10s} {0[1]:10.2f} {0[2]:10.2f} {0[3]:10d}".format(s))

WIDTH = 18
print("\nFormato de nuevo estilo con ancho personalizable")
for s in stockdata:
    print("{0:{width}s} {1:{width}.2f} {2:{width}.2f} {3:{width}d}".format(*s,width=WIDTH))

