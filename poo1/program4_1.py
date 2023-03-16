from hr4_1 import PayrollSystem
from productivity4_1 import ProductivitySystem
from employees4_1 import EmployeeDatabase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track(employees,40)
payroll_system.calculate_payroll(employees)