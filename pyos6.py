# ------------------------------------------------------------
# pyos6.py  -  El sistema operativo de python
#
# Soporte agregado para tareas en espera
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   # Task ID
        self.target  = target        # Target corutinas
        self.sendval = None          # Valor a enviar

    # Ejecute una tarea hasta que llegue a la siguiente declaración de yield
    def run(self):
        print(f"run self.target: {self.target} self.sendval: {self.sendval}")
        return self.target.send(self.sendval)

# ------------------------------------------------------------
#              === Scheduler o Manejador ===
# ------------------------------------------------------------
from queue import Queue

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()   
        self.taskmap = {}        

        # Diccionario de tareas Padre en espera
        # Tareas padre esperando que sus hijos termine su ejecucion para ser
        # puestas en la cola de ejecucion y posterior ser eliminadas
        self.exit_waiting = {}

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print ("Tarea %d terminada" % task.tid)
        del self.taskmap[task.tid]
        # Cuando una tarea Hija termina de ejecutarse, se elimina, apenas se elimina
        # se ejecuta este trozo de codigo.
        # saca una de las tareas padre qu estan en el diccionario de espera exit_waiting
        # y la pone en la cola de ejecucion para posterior ser eliminada        
        espera_to_ejecut=self.exit_waiting.pop(task.tid,[])        
        for task in espera_to_ejecut:            
            self.schedule(task) #se pone la tarea padre en la cola de ejecucion

    def waitforexit(self,task,waittid):
        """
        hace que una tarea padre espere,
        pone la tarea en un diccionario de espera exit_waiting
        """        
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid,[]).append(task)            
            return True
        else:
            return False

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
    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        self.task.sendval = result
        # Si está esperando una tarea inexistente,
        # regresa inmediatamente sin esperar
        if not result:
            print(f"tarea inexistente")
            self.sched.schedule(self.task)

# ------------------------------------------------------------
#                      === Ejemplo de Uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    def foo():
        for i in range(2):
            print ("Funcion foo")
            yield
    def bar():
        for i in range(2):
            print ("funcion Bar")
            yield
    #Tarea padre
    def main():
        # foo es una tarea hija de main
        child = yield NewTask(foo())
        print ("Esperando que el hijo termine")
        yield WaitTask(child)# se envia al diccionario de espera hasta que su hijo termi
        print ("Hijo termino con Exito")

    # Tarea padre   
    def main2():
        # bar es la tarea hija de main2
        child = yield NewTask(bar())
        print ("Esperando que el hijo termine")
        yield WaitTask(child) # se envia al diccionario de espera
        print ("Hijo termino con Exito")

    sched = Scheduler()
    sched.new(main2())
    sched.new(main())
    sched.mainloop()
