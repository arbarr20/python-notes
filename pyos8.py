# ------------------------------------------------------------
# pyos8.py  -  Sistema operativo de python
#
# Paso 7: Soporte para trampolines de corrutinas (subrutinas)
# ------------------------------------------------------------

import types

# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   # ID de la tarea
        self.target  = target        # Target coroutina
        self.sendval = None          # Valor a enviar
        self.stack   = []            # Call stack

    # Ejecute una tarea hasta que llegue a la siguiente declaración de yield
    def run(self):
        while True:
            try:
                result = self.target.send(self.sendval)
                if isinstance(result,SystemCall): return result
                if isinstance(result,types.GeneratorType):
                    self.stack.append(self.target)
                    self.sendval = None
                    self.target  = result
                else:
                    if not self.stack: return
                    self.sendval = result
                    self.target  = self.stack.pop()
            except StopIteration:
                if not self.stack: raise
                self.sendval = None
                self.target = self.stack.pop()

# ------------------------------------------------------------
#                === Scheduler Manejador ===
# ------------------------------------------------------------
from queue import Queue
import select

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()   
        self.taskmap = {}        

        # Tareas esperando que otras tareas se eliminen# Tasks waiting for other tasks to exit
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

    # I/O en espera
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
#             === System Calls LLamadas al sistema ===
# ------------------------------------------------------------

class SystemCall(object):
    def handle(self):
        pass

# Retorna el ID de una tarea
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

# Crea una Nueva tarea
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

# Mata una tarea
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

# Espere a que termine Su tarea hija, mientras
# espere en un diccionario waitforexit
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
#     === Library Functions Funciones de 
#          Nueva implementación ===
# ------------------------------------------------------------

def Accept(sock):
    yield ReadWait(sock)
    yield sock.accept()

def Send(sock,buffer):
    while buffer:
        yield WriteWait(sock)
        len = sock.send(buffer)
        buffer = buffer[len:]

def Recv(sock,maxbytes):
    yield ReadWait(sock)
    yield sock.recv(maxbytes)

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------

# Mira y ejecuta el script echoserver.py para ver un ejemplo



