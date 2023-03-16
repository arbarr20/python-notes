# find404.py
#
# Encuentra un conjunto de todas las URL con un error 404

from timethis import timethis

with timethis("Find 404 urls - text"):
    error_404_urls = set()
    for line in open("Mastering-Python-3-I0/files/access-log"):
        fields = line.split()
        if fields[-2] == '404':
            error_404_urls.add(fields[-4])

    for name in error_404_urls:
        print(name)

with timethis("Find 404 urls - binary"):
    error_404_urls = set()
    for line in open("Mastering-Python-3-I0/files/access-log","rb"):
        fields = line.split()
        if fields[-2] == b'404':
            error_404_urls.add(fields[-4])
    #Conversión Unicode en la siguiente linea
    error_404_urls = { n.decode('latin-1')  for n in error_404_urls }

    for name in error_404_urls:
        print(name)
