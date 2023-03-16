# uno de los cambia es el _ guion bajo en el nombre de la clase
# esto hace que la clase sea interna del modulo
# indica a otros desarrolladores que no se debe usar  _ProductivitySystem directamente
class _ProductivitySystem:
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

# otro de los cambios, es la instantiation dentro del modulo de _ProductivitySystem
# con una variable a nivel de modulo, por esto el guion bajo en _productivity_system
# y la ejecución de sus métodos, con una cierto sobre escritura,
# funcionan como interfaz pública del módulo. Esto es lo que deberían usar otros módulos.
_productivity_system = _ProductivitySystem()

def get_role(role_id):
    return _productivity_system.get_role(role_id)

def track(employees, hours):
    _productivity_system.track(employees, hours)