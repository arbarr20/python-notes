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
        print(f"Taskclass-init: self.tid: {self.tid}")
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
        print(f"Scheduler class-new(self,target):cola: {self.ready.queue}- sigue:return newtask.tid-va al main o al Newtask class")
        return newtask.tid

    def exit(self,task):
        print(f"Scheduler class-exit(self,task):self: {self}-task: {task}")
        print ("Scheduler class-exit(self,task) -Task %d terminated" % task.tid)
        print(f"Scheduler class-exit(self,task):se eliminara la tarea {self.taskmap[task.tid]}")
        del self.taskmap[task.tid]
        print(f"Scheduler class-exit(self,task):self: tarea eliminada self.taskmap: {self.taskmap}")

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
            print(f"Scheduler class-mainloop(self)-while: sigue self.schedule(task) poner de nuevo tarea en cola")
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



# Crea una nueva tarea
class NewTask(SystemCall):
    print(f"NewTask(SystemCall)")
    def __init__(self,target):
        print(f"NewTask(SystemCall)-init")
        self.target = target
        print(f"NewTask(SystemCall)-init: self.target : {self.target}")
    def handle(self):
        print(f"NewTask(SystemCall)-handle(self):self: {self}")
        tid = self.sched.new(self.target)
        print(f"NewTask(SystemCall)-handle(self):tid = self.sched.new(self.target):{tid}")
        self.task.sendval = tid
        print(f"NewTask(SystemCall)-handle(self):self.task.sendval = tid:{self.task.sendval}")
        print(f"NewTask(SystemCall)-handle(self):sigue self.sched.schedule(self.task)")
        self.sched.schedule(self.task)
        print(f"NewTask(SystemCall)-handle(self):despues de self.sched.schedule(self.task)")


# Elimina una tarea
class KillTask(SystemCall):
    print(f"KillTask(SystemCall)")
    def __init__(self,tid):
        print(f"KillTask(SystemCall)-init")
        self.tid = tid
        print(f"KillTask(SystemCall)-init:self.tid: {self.tid}")
    def handle(self):
        print(f"KillTask(SystemCall)-handle(self):self: {self}")
        task = self.sched.taskmap.get(self.tid,None)
        print(f"KillTask(SystemCall)-handle(self):task = self.sched.taskmap.get(self.tid,None): {task}")
        print(f"KillTask(SystemCall)-handle(self):sigue if task")
        if task:
            print(f"KillTask(SystemCall)-handle(self)-if:sigue task.target.close() task={task} target={task.target} ")
            task.target.close() 
            print(f"KillTask(SystemCall)-handle(self)-if: despues de task.target.close() ")
            print(f"KillTask(SystemCall)-handle(self)-if:sigue self.task.sendval = True: {self.task.sendval}")
            self.task.sendval = True
            print(f"KillTask(SystemCall)-handle(self)-if:despues de self.task.sendval = True")
            print(f"KillTask(SystemCall)-handle(self)-if:sigue else")
        else:
            print(f"KillTask(SystemCall)-handle(self)-else:sigue self.task.sendval = False")
            self.task.sendval = False
            print(f"KillTask(SystemCall)-handle(self)-else:despues de self.task.sendval = False: {self.task.sendval}")
        print(f"KillTask(SystemCall)-handle(self)-fin del if else")
        print(f"KillTask(SystemCall)-handle(self):sigue self.sched.schedule(self.task)")
        print(f"KillTask(SystemCall)-handle(self):self.task):{self.task}")
        self.sched.schedule(self.task)
        print(f"fin del KillTask(SystemCall)-handle(self)")
    print(f"fin del KillTask(SystemCall)")


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

    def main():
        print(f"PPAL-main():{main} - sigue- child = yield NewTask(foo())")
        child = yield NewTask(foo())    # Lanza una nueva tarea
        print(f"PPAL-main():child = yield NewTask(foo()): {child}")
        for i in range(1):
            print(f"PPAL-main()-for:sigue yield")
            yield
        print(f"PPAL-main()-for:sigue yield KillTask(child) child: {child}")
        yield KillTask(child)           # mata una tarea
        print ("main done -- despues de yield KillTask(child) child {child} ")


    def bar():
        print(f"PPAL-bar():{bar} - sigue- mytid = yield GetTid()")
        mytid = yield GetTid() #ejemplos de uso de las llamadas al sistema
        print(f"PPAL-bar():despues de mytid = yield GetTid(): {mytid}")
        for i in range(2):
            print(f"PPAL-bar()-for:")
            print ("\nI'm bar", mytid)
            print(f"PPAL-bar()-for:sigue yield")
            yield # retorne a run()

    print(f"PPAL sigue: sched = Scheduler()")
    sched = Scheduler()
    #print(f"PPAL se creo sched: {sched}-sigue sched.new(foo())- crar un obj Task desde Sheduler")
    print(f"PPAL se creo sched: {sched}-sigue sched.new(main())- crar un obj Task especial main desde Sheduler")
    sched.new(main())
    print(f"PPAL se creo la tarea especial main foo-sigue sched.mainloop()")    
    sched.mainloop()

