# Abstract class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class (Implemented abstract methods from abstract class)
class Car(Vehicle):
    def start(self):
        print('Car engine started...')
    def stop(self):
        print('Car engine stopped...')

c = Car()
c.start()
c.stop()

# Abstract method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass    # abstract method, no implementation here


# Concrete method
from abc import ABC, abstractmethod
class Animal1(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        return "Moving"

class Dog(Animal1):
    def make_sound(self):
        return "Bark"

cc = Dog()
print(cc.make_sound())
print(cc.move())


# Abstract properties
from abc import ABC, abstractmethod
class Animal3(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Dog2(Animal3):
    @property
    def species(self):
        return "Canine"

doff = Dog2()
print(doff.species)





















