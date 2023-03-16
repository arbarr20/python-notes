# Archivo: ventajas_descriptors_on_propertys2.py
# Autor: Arbarr20 y ayuda online
# Fecha: 21/02/2023
# Descripción: ventajas de los descriptores sobre las property


class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)  # 0
print(my_values.value2)  # 4
