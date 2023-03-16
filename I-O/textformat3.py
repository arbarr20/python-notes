# textformat3.py
#
# Diferentes ejemplos de formato de texto.

# El archivo stocks.csv tiene algunos datos bursátiles en formato CSV
# "símbolo", precio, cambio, volumen. Léelo en una lista de diccionarios

from collections import namedtuple
StockData = namedtuple("StockData",["name","price","change","volume"])

stockdata = []
for line in open("Mastering-Python-3-I0/files/stocks.csv"):
    fields = line.split(",")
    record = StockData(fields[0].strip('"'),float(fields[1]),float(fields[2]),int(fields[3]))
    stockdata.append(record)



print("Formato de un string tradicional:")
for s in stockdata:
    print("%10s %10.2f %10.2f %10d" % (s.name,s.price,s.change,s.volume))


print("\nEl nuevo estilo:")
for s in stockdata:
    print("{s.name:>10s} {s.price:10.2f} {s.change:10.2f} {s.volume:10d}".format(s=s))

