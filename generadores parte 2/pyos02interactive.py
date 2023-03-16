# ------------------------------------------------------------
# pyos1.py  Sistema Operativo con python
# 
# Paso2: El programador - Planificador scheduler
# ------------------------------------------------------------


# ------------------------------------------------------------
#                       === Tareas ===
# ------------------------------------------------------------
class Task(object):
    print("Task class: soy la clase Task")
    taskid = 0
    print(f"Task class: var clase taskid inicia en {taskid}")
    def __init__(self,target):
        print("init de task")
        Task.taskid += 1
        print(f"init task: var clase taskid se incremento:")
        self.tid     = Task.taskid   # Task ID
        print(f"init task: tarea numero: {self.tid} creada")
        self.target  = target        # Target corrutina
        print(f"init task: El target de esta tarea es: {self.target}")
        self.sendval = None          # Valor a enviar
        print(f"init task: El sendval es:{self.sendval}")

    # Ejecute una tarea hasta que llegue el proximo yield - TRAP
    def run(self):
        print(f"run:  self: {self}, target: {self.target} espero el yield del target y regreso al main lopop")
        return self.target.send(self.sendval)

# ------------------------------------------------------------
#                      === Scheduler Programador  ===
# ------------------------------------------------------------
from queue import Queue
import time
class Scheduler(object):
    print("Soy la clase manejador")
    def __init__(self):
        print("init schedule")
        self.ready   = Queue()  
        print(f"init scheduler: se creo el queue: {self.ready}") 
        self.taskmap = {}    
        print(f"init scheduler: se creo el diccionario de tareas: {self.taskmap}")     

    def new(self,target):
        print(f"soy el metodo new, sigue newtask = Task(target) target:{target}")
        newtask = Task(target)
        print(f"new: se creo una new task: {newtask}")
        self.taskmap[newtask.tid] = newtask    
        print(f"new: Se agrego al dic la tarea: {newtask} conel id: {newtask.tid} ") 
        print("new: se llama al metodo planificador self.schedule(newtask)")   
        self.schedule(newtask)
        print(f"new: se retorna de la llamda al metodo planificdor y retornamos elid de la tarea: {newtask.tid} ")
        return newtask.tid

    def schedule(self,task):
        print(f"schedule: soy el metodo planificador, recibo self:{self} y task:{task}")
        print(f"schedule:  agregare a la cola la task")
        self.ready.put(task)
        print(f"schedule: tarea {task} agregda a la cola")

    def mainloop(self):
        print(f"soy el mainloop: recibo parametro self:{self}")
        while self.taskmap:
            print("mainloop: dento del while mainloop")            
            task = self.ready.get()
            print(f"mainloop: saque una tarea: {task} de la cola sigue result = task.run() ")
            result = task.run()
            print(f"mainloop: ejecute la tarea {task}")
            print(f"mainloop: poniendo de nuevo la tarea {task} en la cola enviandola an met shedu")
            self.schedule(task)
            time.sleep(2)
            print("mainloop: termino ciclo del mainloop")

# ------------------------------------------------------------
#                      === Ejemplo de uso ===
# ------------------------------------------------------------
if __name__ == '__main__':
    
    # Dos tareas
    def foo():
        print(foo)
        while True:
            print ("soy la tarea foo sigue yield")
            yield

    def bar():
        while True:
            print ("Soy la tarea bar sigue yield")
            yield    
        
    # Ejecutando
    print("ppal: voy a crear el objeto manejador=sched")
    sched = Scheduler()
    print(f"ppal: Se creo el manejador sched : {sched},sigue sched.new(foo()) ")
    sched.new(foo())
    print("ppal: se llamo sched.new(foo()), sigue sched.new(bar())")
    sched.new(bar())
    print("ppal: se llamo sched.new(bar())")
    print("ppal: se va a llamar el mainloop")
    sched.mainloop()
    print("ppal: fin de todo")
