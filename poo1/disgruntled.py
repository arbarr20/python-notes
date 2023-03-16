# In disgruntled.py
#auque es una clase en otro modulo, implementa interfaz,
# pero no HEREDA de una clase base
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000