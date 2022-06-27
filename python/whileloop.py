#while-executes the block of code,as long as the its condition remains true
#used when we don't have a exact count of the inputs

name = None

# while len(name) == 0:
#     name =input("Enter your name:")

while not name:
    name = input("Enter your name: ")

print("Hello"+name)
