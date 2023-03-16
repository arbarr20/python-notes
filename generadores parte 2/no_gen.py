from mesure_time_peso import peso,mide_tiempo

# no_gen.py
# mesure_time_peso es simplemente para medir tiempo de ejecucion y peso de algunas variables
# El mundo sin generadores
@mide_tiempo
def pares(lis):
    par = []
    for numero in lis:
        if numero % 2 == 0:
            par.append(numero)
            print(f"pares: {peso(numero)} - Retorno: {peso(par)}")    
    return par

# Ejemplo de uso
if __name__ == '__main__':
    lista = [0,1,2,3,4,5,6,7,8,9,10]
    print(f"""lista= {lista} y ocupa {peso(lista)}""")
    print (pares(lista))
    # otra forma de implementar pares
    par= [numero for numero in lista if numero % 2 == 0 ]
    print(par)