# ------------------------------------------------------------
# pyos7.py  -  El sistema operativo de python
#
# Step 6 : Se agregó soporte de E / S en espera
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   #  ID de las tareas
        self.target  = target        # Target corrutina
        self.sendval = None          # Valor a enviar

    # Run a task until it hits the next yield statement
    def run(self):
        return self.target.send(self.sendval)

# ------------------------------------------------------------
#                      === Manejador ===
# ------------------------------------------------------------
from queue import Queue
import select

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()   
        self.taskmap = {}        

        # Tareas esperando que otras tareas se eliminen
        self.exit_waiting = {}

        # E/S En espera
        self.read_waiting = {}
        self.write_waiting = {}
        
    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print (f"Tarea {task.tid} Terminada ")
        del self.taskmap[task.tid]
        # Notificar otras tareas en espera de salir
        for task in self.exit_waiting.pop(task.tid,[]):
            self.schedule(task)

    def waitforexit(self,task,waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid,[]).append(task)
            return True
        else:
            return False

    # I/O waiting
    def waitforread(self,task,fd):
        self.read_waiting[fd] = task

    def waitforwrite(self,task,fd):
        self.write_waiting[fd] = task

    def iopoll(self,timeout):
        if self.read_waiting or self.write_waiting:
            r,w,e = select.select(self.read_waiting,self.write_waiting,[],timeout)
            for fd in r: self.schedule(self.read_waiting.pop(fd))
            for fd in w: self.schedule(self.write_waiting.pop(fd))

    def iotask(self):
        while True:
            if self.ready.empty():
                self.iopoll(None)
            else:
                self.iopoll(0)
            yield

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):
        self.new(self.iotask())
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
#                   === System Calls ===
# ------------------------------------------------------------

class SystemCall(object):
    def handle(self):
        pass

# Return a task's ID number
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

# Create a new task
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

# Kill a task
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

# Wait for a task to exit
class WaitTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        self.task.sendval = result
        # Si está esperando una tarea inexistente,
        # regresa inmediatamente sin esperar
        if not result:
            self.sched.schedule(self.task)

# En espera de lectura
class ReadWait(SystemCall):
    def __init__(self,f):
        self.f = f
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforread(self.task,fd)

# En espera de escritura
class WriteWait(SystemCall):
    def __init__(self,f):
        self.f = f
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforwrite(self.task,fd)

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------

# Ejecute el script echogood.py para ver este trabajo


