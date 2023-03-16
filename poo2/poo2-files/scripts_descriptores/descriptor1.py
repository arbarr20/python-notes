# Descriptor 1
# Estructura General de un descriptor
# Arbarr20

class ClassDescriptor():
    """
    Esta clase Implementa el Protocolo descriptor
    """

    def __init__(self):
        self.edad_self_descriptor=""  
    def __get__ (self,instancia_prop,classpropietario):        
        print (f"Estas accediendo al atributo edad_self_descriptor = {self.edad_self_descriptor}")
        return self.edad_self_descriptor

    def __set__ (self,instancia_prop,edad_argumento):       
        print (f'Asignándole valor a edad_self_descriptor = {edad_argumento}')
        self.edad_self_descriptor = edad_argumento

    def __delete__(self, instancia_prop):
        print (f"Eliminando a {self.edad_self_descriptor}")

class ClassPropietario():
    """
    Al momento de instanciar la ClaseDescriptor,
    ClassDescriptor se puede llamar DESCRIPTOR
    """

    atr_propietario_instan_descriptor = ClassDescriptor()

instancia_Propietario = ClassPropietario()
instancia_Propietario.atr_propietario_instan_descriptor =34
print (instancia_Propietario.atr_propietario_instan_descriptor)