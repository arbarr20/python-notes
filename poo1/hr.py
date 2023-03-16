
from abc import ABC, abstractmethod

class PayrollSystem:
    # aquí usamos polimorfismo, recibimos varios tipos de employees
    # los objetos que quieran utilizar esta PayrollSystem deben haber
    #implementado por o menos implícitamente la interfaz, ya que si Heredaron de Employee
    # obligatoriamente deben implementar sus métodos e inicializar sus atributos
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


# implementation abstract Employee (solo es para estudio: esta mal esta clase abstracta)
# casi podría ser uan interfaz (las interfaces no deberían tener __init__) ya
# que no se pueden instanciar directamente de ellas
# mas bien llamemosla por Clase base Abstracta
''' class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass '''

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#implementa Herencia explícitamente, implícitamente implementa interfaz
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

#implementa Herencia explícitamente, implícitamente implementa interfaz
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

#implementa Herencia explícitamente, implícitamente implementa interfaz
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
