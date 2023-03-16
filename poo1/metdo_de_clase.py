
class Pizza (object):
    def __init__ (self, ingredientes,nombre:str):
        self.ingredientes = ingredientes
        self.name = nombre

    def __repr__ (self): 
        for i,f in  self.ingredientes.items():            
            print (f"{i}:{f}")    
        return f"Estos fueron los ingredientes de tu {self.__class__.__name__} {self.name}"
        

    @classmethod
    def pizza_hawallana (cls,name:str) -> dict:
        ingre_hawallana = {
            "piña":"mucha",
            "queso":"muchisisisimo",
        }       
        return cls(ingre_hawallana,name)

    @classmethod
    def pizaa_carnes(cls,name:str)-> dict:
        ingre_carnes = {
            "tomate":"mucho",
            "chorizo": 2
        }
        return cls(ingre_carnes,name)   
        
        
pizza_hawallana = Pizza.pizza_hawallana("hawallana")
print(pizza_hawallana)
pizza_carnes = Pizza.pizaa_carnes("carnes")
print(pizza_carnes)

