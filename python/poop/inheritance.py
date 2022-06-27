#inheritance--child recieve the characteristics from parents 
#all parent class methods will be in sub class and sub class can or may have new methods
#saves the time
class Animal:#parent class
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):#sub-class  in java class Dog extends Animal
    def smell(self):
        print("this dog smells so good")
class Fish(Animal):
    def swim(self):
        print("This fish can swim")
class Bird(Animal):
    def fly(self):
        print("This bird can fly")

dog = Dog()
fish = Fish()
bird = Bird()

print(dog.alive)
fish.eat()
bird.sleep()
bird.fly()
