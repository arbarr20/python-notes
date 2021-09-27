from sys import implementation
from typing import Generator
from mesure_time_peso import peso,mide_tiempo
from collections.abc import Iterable
# first_gen.py
# Generador de numeros pares a partir de un generador de 10 numeros
# Nuestro primer generador
@mide_tiempo
def pares(lista):
    if isinstance(lista, Iterable) :
        for item in lista:
            if item % 2 == 0:
                yield item
                print(f"pares: {peso(item)}- Retorno: {peso(item)}")
    else:
        print("el Argumento de la funcion no es iterable")
    
if __name__ == '__main__': 
    gen = pares(range(10))   
    for par in gen:
        print(par,end=' ')
    