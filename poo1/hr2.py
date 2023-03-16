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