# ------------------------------------------------------------
# pyos4.py  -  El sistema operativo Python
#
# Paso 4: Introducir la idea de un "Llamadas al Sistema"
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tareas===
# ------------------------------------------------------------
class Task(object):
    print(f"Task class")
    taskid = 0
    print(f"Task class: {taskid}")
    def __init__(self,target):
        print(f"Taskclass-init")
        Task.taskid += 1
        print(f"Taskclass-init: Task.taskid: {Task.taskid}")
        self.tid     = Task.taskid   # Task ID
        print(f"Taskclass-init: elf.tid: {self.tid}")
        self.target  = target        # Target cororutina
        print(f"Taskclass-init: self.target: {self.target }")
        self.sendval = None          # Valor a Enviar
        print(f"Taskclass-init: self.sendval: {self.sendval }")

    # Ejecute una tarea hasta que llegue a la siguiente declaración de yield
    def run(self):
        print(f"Task class-run(self):self {self} - sigue return self.target.send(self.sendval)")
        #El funcionamiento de esto es un poco sutil- delicado
        return self.target.send(self.sendval) # retorne  result = task.run()
        

# ------------------------------------------------------------
#                      === Manejador ===
# ------------------------------------------------------------
from queue import Queue

class Scheduler(object):
    print(f"Scheduler class")
    def __init__(self):
        print(f"Scheduler class-init")
        self.ready   = Queue()   
        print(f"Scheduler class-init: self.ready: {self.ready}")
        self.taskmap = {}   
        print(f"Scheduler class-init: self.taskmap: {self.taskmap}")     

    def new(self,target):
        print(f"Scheduler class-new(self,target):self: {self}-target: {target}")
        newtask = Task(target)
        print(f"Scheduler class-new(self,target):newtask = Task(target) {newtask} se creo tarea desde Sheduler")
        self.taskmap[newtask.tid] = newtask
        print(f"Scheduler class-new(self,target):self.taskmap[newtask.tid] = newtask {self.taskmap[newtask.tid]}")
        print(f"Scheduler class-new(self,target):sigue self.schedule(newtask)")        
        self.schedule(newtask)
        print(f"Scheduler class-new(self,target):retornó de self.schedule(newtask) se puso la task en la cola")
        print(f"Scheduler class-new(self,target):cola: {self.ready.queue}- sigue:return newtask.tid-va al main")
        return newtask.tid

    def exit(self,task):
        print(f"Scheduler class-exit(self,task):self: {self}-task: {task}")
        print ("Scheduler class-exit(self,task) -Task %d terminated" % task.tid)
        print(f"Scheduler class-exit(self,task):se eliminara la tarea {self.taskmap[task.tid]}")
        del self.taskmap[task.tid]
        print(f"Scheduler class-exit(self,task):self: tara eliminada self.taskmap: {self.taskmap}")

    def schedule(self,task):
        print(f"Scheduler class-schedule(self,task):self: {self}-task: {task} Poner en la cola")
        self.ready.put(task)
        print(f"Scheduler class-schedule(self,task):cola-ready: {self.ready.queue}")

    def mainloop(self):
        print(f"Scheduler class-mainloop(self):self: {self}")
        while self.taskmap:
            print(f"Scheduler class-mainloop(self)-while: sigue task = self.ready.get()- sacar de la cola")
            task = self.ready.get()
            print(f"Scheduler class-mainloop(self)-while: task = {task} la cola quedo: {self.ready.queue}")
            try:
                print(f"Scheduler class-mainloop(self)-while-try- sigue result = task.run()")
                """
                Mira el resultado que arroja la tarea. Si es una SystemCall, haz algo
                configurar y ejecutar la llamada al sistema en nombre de la tarea.
                """
                result = task.run()
                print(f"Scheduler class-mainloop(self)-while-try-result: {result}")
                if isinstance(result,SystemCall):
                    print(f"Scheduler class-mainloop(self)-while-try-if:")
                    """
                    result.task  = task
                    result.sched = self
                    Estos atributos contienen información sobre el 
                    entorno (tarea actual y planificador)
                    """
                    result.task  = task
                    print(f"Scheduler class-mainloop(self)-while-try-if:result.task=task: {result.task}")
                    result.sched = self
                    print(f"Scheduler class-mainloop(self)-while-try-if:result.sched=self:{result.sched}- sigue result.handle()")
                    result.handle()
                    print(f"Scheduler class-mainloop(self)-while-try-if:sigue continue")
                    continue
            except StopIteration:
                print(f"Scheduler class-mainloop(self)-while-except-sigue self.exit(task) eliminar taskt: {task}")
                self.exit(task)
                print(f"Scheduler class-mainloop(self)-while-except: retorno de exit se elimino tarea self.taskmap: {self.taskmap}")
                print(f"Scheduler class-mainloop(self)-while-except: sigue continue")
                continue
            print(f"Scheduler class-mainloop(self)-while: sigue self.schedule(task) oner de nuevo tarea en cola")
            print(f"Scheduler class-mainloop(self)-while: task: {task}- cola ready: {self.ready.queue}")
            self.schedule(task)
            print(f"Scheduler class-mainloop(self)-while:se puso la tarea en la cola")
            print(f"Scheduler class-mainloop(self)-while:task: {task}- cola: {self.ready.queue}")
            print(f"Scheduler class-mainloop(self)-while:Fin while")

# ------------------------------------------------------------
#         === System Calls - Llamadas al Sistema ===
# ------------------------------------------------------------

class SystemCall(object):
    print(f"SystemCall class No init interface")
    """
    Clase base de llamada al sistema.Todas las operaciones del sistema
    será implementado por heredando de esta clase. es ina cierta "interface"
    """
    def handle(self):
        print(f"SystemCall class-handle(self):self: {self} no impelnetada")
        pass

# Retorna los ID's de las Tareas
class GetTid(SystemCall):
    print(f"GetTid(SystemCall) class No init")
    def handle(self):
        print(f"GetTid(SystemCall) class-handle(self):self: {self}")
        self.task.sendval = self.task.tid # envia a metodo run 
        #return self.target.send(self.sendval)
        print(f"GetTid(SystemCall) class-handle(self):self: self.task.sendval = self.task.tid :{self.task.sendval}")
        print(f"GetTid(SystemCall) class-handle(self):sigue self.sched.schedule(self.task)")
        print(f"GetTid(SystemCall) class-handle(self):poner en la cola a self.task: {self.task}")
        self.sched.schedule(self.task)
        print(f"GetTid(SystemCall) class-handle(self):se puso en la cola a a self.task: {self.task}")

# ------------------------------------------------------------
#                    === Ejemplo de Uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    print(f"PPAL")
    def foo():
        print(f"PPAL-foo():{foo} - sigue- mytid = yield GetTid()")
        # la siguiete linea, convierte a result en un obj tipo GetTid()
        mytid = yield GetTid() #ejemplos de uso de las llamadas al sistema
        print(f"PPAL-foo():despues de mytid = yield GetTid(): {mytid}")
        for i in range(2):
            print(f"PPAL-foo()-for:")
            print ("I'm foo", mytid)
            print(f"PPAL-foo()-for:sigue yield")
            yield

    def bar():
        print(f"PPAL-bar():{bar} - sigue- mytid = yield GetTid()")
        mytid = yield GetTid() #ejemplos de uso de las llamadas al sistema
        print(f"PPAL-bar():despues de mytid = yield GetTid(): {mytid}")
        for i in range(5):
            print(f"PPAL-bar()-for:")
            print ("I'm bar", mytid)
            print(f"PPAL-bar()-for:sigue yield")
            yield # retorne a run()
    print(f"PPAL sigue: sched = Scheduler()")
    sched = Scheduler()
    print(f"PPAL se creo sched: {sched}-sigue sched.new(foo())- crar un obj Task desde Sheduler")
    sched.new(foo())
    print(f"PPAL se creo la tarea foo-sigue sched.new(bar())")
    sched.new(bar())
    print(f"PPAL se creo la tarea bar-sched.mainloop()")
    sched.mainloop()
