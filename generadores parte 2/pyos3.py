# ------------------------------------------------------------
# pyos3.py  -  Systema operativo con python
#
# Paso 3: Se ha añadido el manejo de la terminación de tareas
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   # Task ID
        self.target  = target        # Target coroutine
        self.sendval = None          # Value to send

# Ejecute una tarea hasta que llegue a la siguiente declaración de yield
    def run(self):
        return self.target.send(self.sendval)

# ------------------------------------------------------------
#                      === Planificador ===
# ------------------------------------------------------------
from queue import Queue

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()   
        self.taskmap = {}        

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid
    

    def schedule(self,task):
        self.ready.put(task)

    def exit(self,task):
        print ("Task %d terminated" % task.tid)
        del self.taskmap[task.tid]

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

# ------------------------------------------------------------
#                      === Ejemplo de Uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    def foo():
        for i in range(5):
            print ("I'm foo")
            yield

    def bar():
        for i in range(2):
            print ("I'm bar")
            yield

    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
