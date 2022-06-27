#Prevents a user from creating an object of that class
#compels the user to override any abstract methods in a child class
#if a abstract class is present in the parent it must and should be present in the children
#abstract class = a class which contains one or more abstarct methods,--they can not have objects created 
#abstract method = a class that has declaration but no definition,only declare but no definition no implementation(definition)

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Bicycle(Vehicle):
    def go(self):
        print("you drive a bicycle")

    def stop(self):
        print("this bicycle is stopped")
class Car(Vehicle):
    def go(slef):
        print("You drive a car")

    def stop(self):
        print("this car is stopped")

# vehicle = Vehicle()
bicycle = Bicycle()
car = Car()

car.go()
# vehicle.go()
bicycle.go()