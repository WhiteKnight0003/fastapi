# composition - has a relationship : ex : verhicle (car, truck, ..) has a engine (getOn() , getOff()) ,  car.getengine().getOn()
# inheritance - is a relationship : ex : dog is a animal

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print("Engine started...")

    def stop(self):
        print("Engine stopped...")

class Verhicle:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

engine = Engine(1000)
verhicle = Verhicle("Car", engine)
verhicle.engine.start()
# Output: Engine started...



