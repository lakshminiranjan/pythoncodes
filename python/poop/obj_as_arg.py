class Car:
    color = None
#arguments names should be lower case at beginning

class Motorcycle:
    color = None


def change_color(car,color):#(self=car,arg)--car acts as a self
    car.color = color



car_1 = Car()
car_2 = Car()
car_3 = Car()


bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "green")
change_color(bike_1, "indigo")
change_color(bike_2, "white")
change_color(bike_3, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
print(bike_2.color)
print(bike_3.color)


