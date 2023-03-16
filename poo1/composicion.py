class Person():
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age
        # los órganos son instanciado dentro del constructor,
        # es por esto que si se elimina el objeto contenedor, el objeto contenido también desaparece
        self.brain =Brain("brilliant")
        self.heart = Heart("big")
        self.legs = Legs("two legs")
    def __str__(self) -> str:
        return f"name:{self.name}\nage:{self.age}\n{self.brain}\n{self.heart}\n{self.legs}"

class Brain():
    def __init__(self,brain:str):
        self.brain = brain
    def __str__(self) -> str:
        return f"brain:{self.brain}"
class Heart():
    def __init__(self,heart:str):
        self.heart = heart
    def __str__(self) -> str:
        return f"heart:{self.heart}"
class Legs():
    def __init__(self,legs:str):
        self.legs =legs

    def __str__(self) -> str:
        return f"legs:{self.legs}"

if __name__ == "__main__":
    juan = Person("juan",50)
    print(type(juan.brain))
    print(type(juan.heart))
    print(type(juan.legs))
    print(juan)

    # if we remove juan, brain,heart,legs are also removed
    del(juan)
    try:
        print(juan.brain)
    except Exception as e:
        print(f" Juan murió, sus órganos no existen ")
    
