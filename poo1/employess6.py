from representations6 import AsDictionaryMixin

# observe como camban las importaciones usando el patron singleton
#from productivity6 import*
from productivity6 import get_role

#from hr6 import PayrollSystem
from hr6 import get_policy

#from contacts6 import AddressBook
from contacts6 import get_employee_address

# hay cambios en la estructura de la definición del diccionario y el guion bajo en el nombre dela clase
class _EmployeeDatabase:
    def __init__(self):
        #antes
        ''' 
        {
            'id': 1,
            'name': 'Mary Poppins',
            'role': 'manager'
        },
        '''
        # con el patron singleton
        self._employees = {  
            
            
            1:{
                
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2:{
                
                'name': 'John Smith',
                'role': 'secretary'
            },
            3:{
                
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4:{
                
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5:{
                
                'name': 'Robin Williams',
                'role': 'secretary'
            },
        }
        # esto se elimina con la nueva implementación
    ''' self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook() '''

    # se elimina
    ''' @property
    def employees(self): 
        return [self._create_employee(**data) for data in self._employees '''

    # nueva implementación
    # se llama desde el punto de entrada como employees = employee_database.employees
    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    # nueva implementación
    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info
    # se omite esta implementación
    ''' def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy) '''
        
class Employee(AsDictionaryMixin):
    # se elimina esta implementación
    ''' def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll '''

    # nueva implementación   
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    # nueva implementación
    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy

# esta linea se agregó con el patron singleton
employee_database = _EmployeeDatabase()