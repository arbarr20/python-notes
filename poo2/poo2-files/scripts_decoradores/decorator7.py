# Decoradores 7
#class decorator
# Arbarr20

from functools import wraps # no es necesario para estos casos

def class_decorator_parameter(gasto = 100):
    def class_decorator (Cls):# Recibe como parámetro una clase        
        #@wraps(Cls) #AttributeError: 'mappingproxy' object has no attribute 'update'
        class Envolvente (Cls):
            """Esto equivale a tener class Envolvente(Salary)"""            
            def sueldo_real (self):
                """this is current salary Decorated"""
                return f"{self.nombre}'s current salary is : {(self.pago - gasto)}"
            def __str__(self):
                return f"Object type:{self.__class__.__name__}"        
        return Envolvente #Retorna la clase        
    return class_decorator


@class_decorator_parameter(50)
class Salary():
    def __init__ (self,nombre:str,pago:int(0)) ->object:
        self.pago = pago
        self.nombre = nombre
    def get_salary(self):
        return f"{self.nombre} has a salary of: {self.pago}"
    
# Todos los objetos que se crean de Salary, en realidad 
# son de tipo Envolvente
salary1 = Salary("Arbarr",200)
print(salary1.sueldo_real())
print (salary1)
print(salary1.sueldo_real.__doc__)
print(f"the class of salary is: {salary1.__class__.__name__}")