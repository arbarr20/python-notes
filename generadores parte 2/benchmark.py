# benchmark.py
#
# Un micro benchmark que compara el rendimiento del envío de mensajes a
# una corrutina frente a enviar mensajes a un objeto

# Una clase - bjeto

class GrepHandler(object):
    def __init__(self,pattern, target):
        self.pattern = pattern
        self.target = target
    def send(self,line):
        if self.pattern in line:
            self.target.send(line)

# Una corrutina
from coroutine import coroutine

@coroutine
def grep(pattern,target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

#  Vertedero-Null Recibe la data
@coroutine
def null(): 
    while True: item = (yield)

# Compare
line = 'python is nice'
p1   = grep('python',null())          # Coroutina
p2   = GrepHandler('python',null())   # Object

from timeit import timeit

print ("coroutine:", timeit("p1.send(line)",
                        "from __main__ import line, p1"))

print ("object:", timeit("p2.send(line)",
                        "from __main__ import line, p2"))

