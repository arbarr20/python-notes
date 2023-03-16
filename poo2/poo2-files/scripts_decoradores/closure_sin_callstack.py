def hola (nombre ="arbarr"):
    print ("dentro de hola")

    def saluda ():
        print ("dentro de saluda")
        return f"return dentro de saluda"

    def pico ():
        print("dentro de pico")
        #tenga en cuenta que no se retorna saluda() 
        # los paréntesis significan mucho
        return saluda

    #tenga en cuenta que no se retorna saluda() 
    # los paréntesis significan mucho
    return pico 
    
hi = hola()
print (f"hi=return de hola (f(pico)) {hi}")
hii = hi()
print (f"hii = return de pico (f(saluda)) {hii}")
hiii = hii()
print (f"hiii=  return de saluda (string) {hiii}")