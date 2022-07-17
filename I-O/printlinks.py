# printlinks.py
#
# Un programa de Python 2 que imprime enlaces en una página web.
# Bueno no tanto esta en python3
# Intente ejecutar 2to3 en este programa y convertirlo a Python 3.

import urllib.request
import requests
import sys
#from HTMLParser import HTMLParser
from html.parser import HTMLParser

class LinkPrinter(HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == 'href': print (value)
                
url = 'http://www.python.org'
r = requests.get(url)
data = r.text


LinkPrinter().feed(data)






