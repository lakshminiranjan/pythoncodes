# class Car:#should initiate with capital
#     pass -----class can function as a blueprint to create objects. 
from car import Car

# car_1 = Car("Chevy", "Corvette", 2022, "blue")#Craeting a obj in java --- Class obj =new Class(int n1,int n2);obj.meth(String a,String b)
# car_2 = Car("Ford","Mustang",2021,"red")
# print("\n",car_1.make,"\n",car_1.model,"\n",car_1.year,"\n",car_1.color,"\n")
# print("\n",car_2.make,"\n",car_2.model,"\n",car_2.year,"\n",car_2.color,"\n")

# car_1.drive()
# car_1.stop()
# car_1.wheels = 2 

# car_2.drive()
# car_2.stop()
# print(car_1.wheels)
print(Car.wheels)#as the wheels are constnat for every car we can use classname.var
