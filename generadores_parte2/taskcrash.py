# taskcrash.py
#
# Un ejemplo que muestra cómo el planificador inicial no maneja
# finalización de la tarea correctamente.

from pyos2 import Scheduler

def foo():
    for i in range(5):
        print ("I'm foo")
        yield
def bar():
    while True:
        print ("I'm bar")
        yield

sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
