#resolv_dudas_objs.py
#
# Una pequeña demostración para resolver dudas sobre como
#se asignan objetos de una clase a otros de otra clase!!!!


# ------------------------------------------------------------
#                === Ejecute paso a paso ===
# ------------------------------------------------------------

class Myclase():
    def __init__(self) -> None:        
        self.nombre = "arbarr"
        self.edad = 20

class OtraClase():
    def __init__ (self):
        self.var1= "var OtraClase"

miclase = Myclase()     
otraclase = OtraClase()
print (f"atributos de miclase:{miclase.__dict__}")
print (f"atributos de otraclase:{otraclase.__dict__}")
# nada distinto gasta aqui
#-----------------------------------------------

# se crea un atributo dinamico 
otraclase.atributo_dinamico = miclase
#obsevemos el dicionario del obj otraclase
# puede darse cuenta que atributo_dinamico pertenece a Otraclase, pero
# es de tipo Myclase
print (f"\natributos de otraclase:{otraclase.__dict__}")
# tambien podemos sobreescribir atributos ya existentes
# var1 inicialmente es de tipo str
print(f"tipo de atributo var1 de la clase Otraclase: {type (otraclase.var1)}")
#ahora sobreescribamoslo
otraclase.var1 =miclase
# miremos es listado de atributos de otraclase obj
#obseve que var1 aes de tipostr aobj tipo Myclase
print (f"atributos de otraclase:{otraclase.__dict__}")

#------------------------------------------------------------
# si lo anterior es correcto entonces podemos accedes desde var1 a
#nombre y edad de la clas Myclase
print (f"\natributos otraclase.var1:{otraclase.var1.__dict__}")
#modifiquemos el atributo nombre desde var
otraclase.var1.nombre = "otro nombre"
# verifiquemos este cambio pero desde obj miclase
#si se puede.
print (f"atributos de miclase:{miclase.__dict__}")
# cambiemos el mismo atributo nombre como normalmente se haría
miclase.nombre = "arbarr de nuevo"
#verifiquemos este cambio o desde obj miclase
print (f"atributos de miclase:{miclase.__dict__}")
#Nota: ahora podemos cambiar los atributos desde 2 partes distintas
# objeto directo de la propia clase miclase y un atributo var 
# que pertenece a Otraclase pero es de tipo Myclase




