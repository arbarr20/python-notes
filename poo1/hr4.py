class PayrollSystem:
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        print("--------------------------------")
        for employee in employees:
            print(f"Pago para {employee.id} -- {employee.name}")
            print(f"El monto es de: {employee.calculate_payroll()}")

            if employee.address:
                print('- send to: ')
                print(employee.address)
            print('')

class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission