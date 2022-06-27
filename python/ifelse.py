#if statement -- a block of code that excecutes if its condition is true
#executes linearly checking each and every block of the code
age = eval(input("What is your age?: "))

if(age == 100):
    print("Congrats you hit a centuary")

elif(age >=18):
    print("Hey,you became an adult")

elif(age <=18 and age >0):
    print("Hi kid")

elif(age < 0):
    print("You haven't born yet")

else:
    print("you are not a human")