class Car():
    def __init__(self,marca:str,modelo:str) :
        self.marca = marca
        self.modelo = modelo
        # no se instancian engine ni wheel dentro del __init__
        self.engine = None
        self.wheel = None

    def show_car(self):
        print(f"\nbrand: {self.marca}\nmodel: {self.modelo}")
        if self.engine == None:
            print("buy a engine")
        else:
            print(self.engine)
        if self.wheel == None:
            print("buy a wheel")
        else:           
            print(self.wheel)

    def add_wheel(self, wheel):
        if isinstance (wheel,Wheel):
            self.wheel = wheel
        else:
            print("buy a whell")

    def add_engine(self, engine):
        if isinstance (engine,Engine):
            self.engine = engine
        else:
            print("buy a engine")

class EngineInstpection(object):
    def __init__(self,horas_instpeccion:float):
        self.horas_instpeccion = horas_instpeccion
        self.engine = None

    def show_inspection(self):        
        if self.engine == None:
            print(f"no engine for {self.horas_instpeccion} inspection")
        else:
            print(f"inspection hours: {self.horas_instpeccion} for engine: {self.engine}")
            

    def add_engine(self, engine):
        if isinstance (engine,Engine):
            self.engine = engine
        else:
            print("buy a engine")

class Engine (object):
    def __init__(self,horse_power:float):
        self.horse_power = horse_power
    def __str__(self):
        return f"horse_power: {self.horse_power}"

class Wheel(object):
    def __init__(self,tipo:str):
        self.tipo = tipo
    def __str__(self):
        return f"wheel tipe: {self.tipo}"

if __name__ == "__main__":
    engine = Engine(2500)
    wheel = Wheel("grande")
    engine_inspection = EngineInstpection(20000)
    car = Car("chevi","2021")
    car.show_car()
    engine_inspection.show_inspection()

    ## add engine and wheel to car
    car.add_engine(engine)
    car.add_wheel(wheel)
    car.show_car()

    ## ad engine to inspection
    engine_inspection.add_engine(engine)
    engine_inspection.show_inspection()

    # removing the cart does not remove the motor and wheels
    del(car)
    try:
        print('\n',engine)
        print(wheel)
        car.show_car()
    except Exception as e:
        print(f"the vehicle was removed {e}")
