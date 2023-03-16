def buenos_dias():
    return f"Buenos días"

def buenas_noches ():
    return f"buenas noches"

def  normal (func):
    print (buenos_dias())
    return func 

def distinto (func):
    print (buenas_noches())
    print (func())

# Aquí es necesario el doble ()
print (normal(buenas_noches)())

# Aquí No es necesario el doble ()
distinto(buenos_dias)