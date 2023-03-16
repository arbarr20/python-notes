class Ubicacion():
    def __init__(self,coordenadas:list=["sin", "coordenadas"]):
        self.__coordenadas = coordenadas

    def get_coordenadas(self):
        return self.__coordenadas
    
    def __str__(self):
        return f" {__class__.__name__}({self.get_coordenadas()})"

    def __repr__(self):
        # de esta forma se crea un nuevo objeto al llamar a repr
        #obj=Ubicacion(["5.948020833382328", "-75.92583004242971"])
        return f" {__class__.__name__}({self.get_coordenadas()})"

ubicacion= Ubicacion(["5.948020833382328", "-75.92583004242971"])
# imprime el contenido definido en  __str__
print(ubicacion)
# llamada normal a un metodo de una clase
print(ubicacion.get_coordenadas()[0])
# obj es un otro objeto tipo Ubicacion
# que se crea con la llamada a __repr__
obj= eval(repr(ubicacion))
print(obj.get_coordenadas()[0])
# la forna mas clara de netender repr es con el siguiente if 
# donde se confirma que obj en realidad es un objeto y podemos acceder
# a sus métodos
if ubicacion.get_coordenadas()[0] == obj.get_coordenadas()[0]:
    print("son iguales")
    