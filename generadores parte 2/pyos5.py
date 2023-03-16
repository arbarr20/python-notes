# ------------------------------------------------------------
# pyos5.py  -  El sistema operativo de python
#
# Paso 5: llamadas al sistema agregadas para una administración
#  de tareas simple
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tasks ===
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
#                   === Maneajdor - Scheduler ===
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

    def exit(self,task):
        print ("Task %d terminated" % task.tid)
        del self.taskmap[task.tid]

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result,SystemCall):
                    result.task  = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

# ------------------------------------------------------------
#                   === Llamadas al sistema ===
# ------------------------------------------------------------

class SystemCall(object):
    def handle(self):
        pass

# Retorna los Id's de las tareas
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

# Crea una nueva tarea
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

# Elimina una tarea
class KillTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        task = self.sched.taskmap.get(self.tid,None)
        if task:
            task.target.close() 
            self.task.sendval = True
        else:
            self.task.sendval = False
        self.sched.schedule(self.task)

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    def foo():
        mytid = yield GetTid()
        while True:
            print ("I'm foo", mytid)
            yield

    def main():
        child = yield NewTask(foo())    # Lanza una nueva tarea
        for i in range(2):
            yield
        yield KillTask(child)           # mata una tarea
        print ("main done")

    sched = Scheduler()
    sched.new(main())
    sched.mainloop()
