# ------------------------------------------------------------
# pyos1.py  Sistema Operativo con python
# 
# Paso1: Tasks
# ------------------------------------------------------------

# Este objeto encapsula una tarea en ejecución.

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
#                       == Ejemplo ==
# ------------------------------------------------------------
if __name__ == '__main__':
    
    # Una simple funcion Generador /Corrutina
    def foo():
        print ("Part 1")
        yield # estos yield serian el aquivalente a una trap
        print ("Part 2")
        yield

    t1 = Task(foo()) # envolver en una tarea
    print ("Running foo()")
    t1.run()
    print ("Resuming foo()")
    t1.run()


