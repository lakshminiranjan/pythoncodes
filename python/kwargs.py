#**kwargs = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amount of keyword arguments
#only "**" is imp kwags can be written as a any dictionary
def hello(**kwargs):
    # print("Hello ",kwargs["first"]," ",kwargs["last"])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(key, end=" ")


hello(title = "Mr." ,first = "Nizy", middle = "Lakshmi", last = "Niranjan")