# ------------------------------------------------------------
# pyos1.py  Sistema Operativo con python
# 
# Paso2: El programador - Planificador scheduler
# ------------------------------------------------------------


# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   # Task ID
        self.target  = target        # Target corrutina
        self.sendval = None          # Valor a enviar

    # Ejecute una tarea hasta que llegue el proximo yield - TRAP
    def run(self):
        return self.target.send(self.sendval)

# ------------------------------------------------------------
#                      === Scheduler Programador  ===
# ------------------------------------------------------------
from queue import Queue
import time
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

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            result = task.run()
            self.schedule(task)
            time.sleep(2)

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    
    # Dos tareas
    def foo():
        print(foo)
        while True:
            print ("I'm foo")
            yield

    def bar():
        while True:
            print ("I'm bar")
            yield    
        
    # Ejecutando
    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
