#multi-level-inheritance - a child class inhertis another derivrd class
#eg-its like brother having the same properties as I have
class Oragnism:
    alive = True

class Animal(Oragnism):
    def eat():
        print("This animal is eating")
class Dog(Animal):
    def smell():
        print("This dog can smell good")

dog = Dog()
print(dog.alive)
dog.eat()
dog.smell()