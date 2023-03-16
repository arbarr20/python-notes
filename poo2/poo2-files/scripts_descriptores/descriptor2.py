# Descriptor 2
# Atributos de solo lectura
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
        # Aquí se genera una excepción cuando se intenta cambiar el atributo edad_self_descriptor
        raise AttributeError

    def __delete__(self, instancia_prop):
        """
        si queremos que un atributo de sólo lectura aún pueda ser modificado mediante un borrado previo a su resignación se implementa el __delete__
        """
        print (f"Eliminando a {self}")

class ClassPropietario():
    """
    Al momento de instanciar la ClaseDescriptor,
    ClassDescriptor se puede llamar DESCRIPTOR
    """

    atr_propietario_instan_descriptor = ClassDescriptor()

instancia_Propietario = ClassPropietario()
instancia_Propietario.atr_propietario_instan_descriptor =34
print (instancia_Propietario.atr_propietario_instan_descriptor)