def hola (nombre ="arbarr",):
    print ("dentro de hola")

    def saluda ():
        print ("dentro de saluda")
        return f"return dentro de saluda"

    def pico ():
        print("dentro de pico")
        # Aquí También se retorna la EJECUCIÓN de la función saluda
        return saluda()

    # Tenga en cuenta que se retorna LA  EJECUCIÓN de una función    
    return pico ()

print(hola())