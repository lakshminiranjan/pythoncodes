#multiple_inheritance = where a child class is derived from more than one parent class
#i can get cahracteristics from my mother and from my father
#multiple inheritance in java is not possible but in here it is possible
class Prey:
    def flee(self):
        print("This animal flees away")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk  = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()