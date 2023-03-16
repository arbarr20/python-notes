import hr2
import employees2
import productivity

def system_pyroll():
    print("############# system_pyroll ###########")
    salary_employee = employees2.SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = employees2.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = employees2.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    payroll_system = hr2.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee
    ])

def system_productivity():
    print("############# system_productivity ###########")
    manager = employees2.Manager(1, 'Mary Poppins', 3000)
    secretary = employees2.Secretary(2, 'John Smith', 1500)
    sales_guy = employees2.SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = employees2.FactoryWorker(2, 'Jane Doe', 40, 15)
    employees = [
        manager,
        secretary,
        sales_guy,
        factory_worker,
    ]
    productivity_system = productivity.ProductivitySystem()
    productivity_system.track(employees, 40)
    payroll_system = hr2.PayrollSystem()
    payroll_system.calculate_payroll(employees)

def sec_temporary():
    print("############# sec_temporary ###########")
    manager = employees2.Manager(1, 'Mary Poppins', 3000)
    secretary = employees2.Secretary(2, 'John Smith', 1500)
    sales_guy = employees2.SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = employees2.FactoryWorker(2, 'Jane Doe', 40, 15)
    temporary_secretary = employees2.TemporarySecretary(5, 'Robin Williams', 40, 9)
    company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,]

    productivity_system = productivity.ProductivitySystem()
    productivity_system.track(company_employees, 40)
    payroll_system = hr2.PayrollSystem()
    payroll_system.calculate_payroll(company_employees)

system_pyroll()
system_productivity()
sec_temporary()