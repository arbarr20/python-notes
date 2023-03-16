class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }
    def get_role(self,role_id):
        role_type = self._roles.get(role_id)        
        if not role_type:
            raise ValueError ('role_id')
        return role_type()

    def track (self,employees,hours):
        print('Rastreando la Productividad')
        print('===================================')
        for employee in employees:            
            employee.work(hours)
        print('')


    
class ManagerRole:
    def perform_duties(self,hours):        
        return f'Grita y grita durante {hours} horas'

class SecretaryRole:
    def perform_duties(self,hours):
        return f'realiza trámites durante {hours} horas.'

class SalesRole:
    def perform_duties(self,hours):
        return f'gasta {hours} horas en el teléfono.'

class FactoryRole:
    def perform_duties(self,hours):
        return f'fabrica aparatos durante {hours} horas.'