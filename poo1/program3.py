
import employees3
from productivity3 import ProductivitySystem
from hr3 import PayrollSystem

manager = employees3.Manager(1, 'Mary Poppins', 3000)
secretary = employees3.Secretary(2, 'John Smith', 1500)
sales_guy = employees3.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees3.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees3.TemporarySecretary(5, 'Robin Williams', 40, 9)
company_employees = [
manager,
secretary,
sales_guy,
factory_worker,
temporary_secretary,]

payroll_system =PayrollSystem()
payroll_system.calculate_payroll(company_employees)
productivity_system =ProductivitySystem()
productivity_system.track(company_employees,40)





