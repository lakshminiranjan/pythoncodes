#method chaining = calling multiple methods sequentially each call perform an action on the same object and returns self
#like printing them in a sinle print statement

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brake")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()
# car.turn_on().drive()#doing the same methods simultaneously in the same thing
# car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()