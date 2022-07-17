# textformat2.py
#
# Diferentes ejemplos de formato de texto.

# El archivo stocks.csv tiene algunos datos bursátiles en formato CSV
# "símbolo", precio, cambio, volumen. Léelo en una lista de diccionarios

stockdata = []
for line in open("Mastering-Python-3-I0/files/stocks.csv"):
    fields = line.split(",")
    record = {
        'name': fields[0].strip('"'),# elimine las " al inicio y al fin del dato de este indice
        'price': float(fields[1]),
        'change' : float(fields[2]),
        'volume' : int(fields[3])}
    stockdata.append(record)



print("Formato tradicional:")
for s in stockdata:
    print("%(name)10s %(price)10.2f %(change)10.2f %(volume)10d" % s)


print("\nEstilo de nuevo formato:")
for s in stockdata:
    print("{name:>10s} {price:10.2f} {change:10.2f} {volume:10d}".format(**s))

print("\nFormateo de nuevo estilo con búsquedas en el diccionario:")
for s in stockdata:
    print("{s[name]:>10s} {s[price]:10.2f} {s[change]:10.2f} {s[volume]:10d}".format(s=s))

