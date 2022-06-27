#str.format() = optional method that gives users more control when displaying outputs 

# animal = "cow"
# item = "moon"

# print("The ",animal," jumped over the ",item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item))#positional argument-we can reuse the same index
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))#keyword arguments-we can reuse the same index

# text = "The {} jumped over the {}"
# print(text.format(animal,item))





# name = "Nizy"

# print("Hello, My name is {}".format(name))
# print("Hello, My name is {:10}.NIce to meet you".format(name))
# print("Hello, My name is {:<10}.NIce to meet you".format(name))#left align-default
# print("Hello, My name is {:>10}.NIce to meet you".format(name))#right align
# print("Hello, My name is {:^10}.NIce to meet you".format(name))#center align



pi = 3.14153
number = 1000

print("The number pi is {:.2f}".format(pi))#displays only the first two digits after the decimal point
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))#displays the binary num of the "number" variable
print("The number is {:o}".format(number))#displays the octal num of the "number" variable
print("The number is {:X}".format(number))#displays the hexadecimal num of the "number" variable
print("The number is {:E}".format(number))#displays the scientific notation of the "number" variable