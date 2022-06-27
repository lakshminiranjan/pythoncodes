#method_overridiing:a method which is already present in the parent class is also present in child class it is method overriding
#imp     ------ parameters should also match
class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):#sub-class uses its own method than inherited from the parent class
    def eat(self):
        print("This rabbit is eating  a carrot")

rabbit = Rabbit()
rabbit.eat()