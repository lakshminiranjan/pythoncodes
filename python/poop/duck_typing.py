#Duck_typing == is the concept where the class of an object is less important than the methods/attribtes
#                class type is not checked if min methods/attributes are present
#                "if it walks like a duck,and it quacks like a duck then it must be a duck"

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch_a_duck(self,bird):
        bird.walk()
        bird.talk()
        print("You caught the critter!")

duck = Duck()#in java psvm before we have to write this code and in the bigger Main class itself
chicken = Chicken()
person = Person()

person.catch_a_duck(chicken)#If we didnt write the walk function in the Chicken.It will not print.An error will be occured