# ------------------------------------------------------------
# pyos7.py  -  El sistema operativo de python
#
# Step 6 : Se agregó soporte de E / S en espera
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
import time
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

    # E/S en espera
    
    def waitforread(self,task,fd):
        # espere hasta que este listo para leer
        self.read_waiting[fd] = task
        print(f"agregando a dic en espera de ser leido:{self.read_waiting}")

    def waitforwrite(self,task,fd):
        # espere hasta que este listo para escribir
        self.write_waiting[fd] = task
        print(f"agregando a dic en espera de ser escrito:{self.write_waiting}")

    def iopoll(self,timeout):
        """
        Sondeo de E/S. Utilice select() para
        determinar qué descriptores de archivo se pueden utilizar.
        Desbloquea cualquier tarea asociada
        - Cuando se alcanza el tiempo de espera sin que un descriptor
        de archivo esté listo, se devuelven tres listas vacías. 
        
        """
        if self.read_waiting or self.write_waiting:
            #- espere hasta que al menos uno de los sockets este listo para
            #procesar
            r,w,e = select.select(self.read_waiting,self.write_waiting,[],timeout)
            
            print(f"lista de lectura:{r}")
            print(f"lista de escrituta: {w}")
            print(f"lista de error: {e}")
        
            for fd in r:
                print(f"poner en la cola fd:{fd} de readlistwait:{r}")
                self.schedule(self.read_waiting.pop(fd))
            
            for fd in w:
                print(f"poner en la cola fd:{fd} de writelistwait:{w}")
                self.schedule(self.write_waiting.pop(fd))
            

    def iotask(self):
        while True:
            if self.ready.empty():
                #self.iopoll(timeout) tiempo de espera en seg
                #Cuando se omite el argumento de tiempo de espera,
                #la función se bloquea hasta que al menos un descriptor 
                #de archivo esté listo
                self.iopoll(None)
            else:
                #Un valor de tiempo de espera de cero especifica
                # una encuesta (poll) y nunca se bloquea
                self.iopoll(0)
            yield

    def schedule(self,task):
        print(f"se agregara tarea: {task}")
        self.ready.put(task)
        print(f"total en cola schedule: {self.ready.queue}")
        
        

    def mainloop(self):
        self.new(self.iotask()) # esta linea es nueva se ejecuta una vez
        #cuando recien ingresa al mainloop
        while self.taskmap:
            task = self.ready.get()
            print(f"total en lacola: {self.ready.queue}")
            print(f"la tarea a ejecutar es: {task}")
            

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

# Retorna el numero de id de una tarea
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

# Crear una Nueva tarea
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

# Matar una tarea
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
        print(f"WaitTask self.tid:{self.tid}")
    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        print(f"WaitTask handle result:{result}")
        self.task.sendval = result
        # Si está esperando una tarea inexistente,
        # regresa inmediatamente sin esperar
        if not result:
            self.sched.schedule(self.task)

# En espera de lectura
class ReadWait(SystemCall):
    def __init__(self,f):
        #f es el socket
        self.f = f
        print(f"ReadWait init self.f:{self.f}")
    def handle(self):
        #fd file descriptor
        #fileno() retorna  un descriptor de archivo es un entero
        fd = self.f.fileno()
        print(f"ReadWait handle self.f.fileno():{fd}")
        print("y sigue guardarlo en lista para ser leido")
        self.sched.waitforread(self.task,fd)

# En espera de escritura
class WriteWait(SystemCall):
    def __init__(self,f):
        self.f = f
        print(f"WriteWait init self.f:{self.f}")
    def handle(self):
        fd = self.f.fileno()
        print(f"WriteWait  handle self.f.fileno():{fd}")
        self.sched.waitforwrite(self.task,fd)

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------

# Ejecute el script echogood.py para ver este trabajo


