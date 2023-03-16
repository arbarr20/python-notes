import hr4
import employees4
import productivity4
import contacts

manager = employees4.Manager(1, 'Mary Poppins', 3000)
manager.address = contacts.Address(
    '121 Admin Rd', 
    'Concord', 
    'NH', 
    '03301'
)
secretary = employees4.Secretary(2, 'John Smith', 1500)
secretary.address = contacts.Address(
    '67 Paperwork Ave.', 
    'Manchester', 
    'NH', 
    '03101'
)
sales_guy = employees4.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees4.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = employees4.TemporarySecretary(5, 'Robin Williams', 40, 9)
employees4 = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity4.ProductivitySystem()
productivity_system.track(employees4, 40)
payroll_system = hr4.PayrollSystem()
payroll_system.calculate_payroll(employees4)