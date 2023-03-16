
import hr
import disgruntled 

def parte1():
    print("############# parte 1 ###########")
    salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee
    ])

# 2 errors distintos
# cuando en hr Employee no es abstracto y cuando si lo es
def error():
    print("################## error #################")
    try:
        empleado = hr.Employee(1,'invalid')
        payroll_system = hr.PayrollSystem()
        payroll_system.calculate_payroll([empleado])
    except Exception as e:
        print("ocurrió un error",e)

def wit_disgruntled():
    print("############# wit_disgruntled ###########")
    salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')
    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee,
        disgruntled_employee
    ])

parte1()
error()
wit_disgruntled()
