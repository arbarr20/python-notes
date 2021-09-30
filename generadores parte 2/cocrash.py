# cocrash.py
#
# Un ejemplo de cómo conectar corrutinas de una manera que podría causar un potencial
# choque. Básicamente, hay dos hilos que alimentan datos al
# corrutina printer () .    

from cobroadcast import *
from cothread import threaded

p = printer()
target = broadcast([threaded(grep('foo',p)),threaded(grep('bar',p))])
print(target)

# Ajuste el recuento si esto no causa un bloqueo
for i in range(2):
    target.send("foo is nice\n")
    target.send("bar is bad\n")

del target
del p

