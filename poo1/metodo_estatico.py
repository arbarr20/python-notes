class Student(object):
    
    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

print(Student.is_full_name('Arbarr sanchez') )  # True
print(Student.is_full_name('Arbarr'))#false

class Persona ():
    
    """ esta es la clase persona"""
    def __init__(self, edad:int):
        self.edad = edad

    @staticmethod
    def mitad_edad (edad:float):        
        return edad/2
    
per1 = Persona(6)
print (per1.mitad_edad(per1.edad))
#3