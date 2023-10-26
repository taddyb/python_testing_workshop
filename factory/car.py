from abc import ABC, abstractmethod

class BaseCar(ABC):
    def __init__(self, engine, wheels, name):
        self.name = name
        self.engine = engine
        self.wheels = wheels

    @abstractmethod
    def add_fuel(self):
        pass

    def print(self):
        return self.name

class Subaru(BaseCar):
    def __init__(self, engine, wheels, name):
        super(Subaru, self).__init__(engine, wheels, name)

    def check_fuel(self):
        if self.engine.fuel < 0:
            return "No fuel"
        else:
            return "Fuel"

    def add_fuel(self):
        self.engine.fuel = 10

class Ferari(BaseCar):
    def __init__(self, engine, wheels, name):
        super(Ferari, self).__init__(engine, wheels, name)

    def add_fuel(self):
        self.engine.fuel = 1

class Engine:
    def __init__(self):
        self.fuel = 0

    def status(self):
        pass

    def check_oil(self):
        pass

class Wheels:
    def __init__(self):
        self.size = 16

class Access:
    def __init__(self, name):
        self.name = name

