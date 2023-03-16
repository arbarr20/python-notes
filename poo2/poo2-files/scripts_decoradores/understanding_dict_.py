class Perro():
    """Clase perro"""
    def __init__(self,name,color) -> None:
        self.name = name
        self.color = color

    def bark (self):
        if self.color == 'black':
            return True
        else:
            return False
        
tobi = Perro('tobi','black')
print(tobi.__dict__)
#{'name': 'tobi', 'color': 'black'}
print(Perro.__dict__)
"""
{'__module__': '__main__', '__doc__': 'Clase perro', '__finit__': <function Perro.__init__ at 0x1099d0ca0>,
 'bark': <function Perro.bark at 0x1099d0d30>, '__dict__': <attribute '__dict__' of 'Perro' objects>,
  '__weakref__': <attribute '__weakref__' of 'Perro' objects>}
"""
