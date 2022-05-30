#!bin/python3

#Variables and methods
quote = "Failure is stepping stone to success."
print(quote.upper())#prints the quote words in uppercase
print(quote.lower())#prints the quote words in lowercase
print(quote.title())#prints everystarting letter in quote in uppercase

print(len(quote))#prints the length of the variablr quote


name="Niranjan"#string
age=20#int(no decimal points)
cgpa=6.3#float(decimal points are allowed)

print(int(age))
print(int(20.9))#output will be 20 only.
#print(int(cgpa))converts the float into the integer

#print("My name is "+ name + "\n I am "+ age + "\n years old")->cant concatenate str with int.
print("My name is "+name +"\nI am "+ str(age) +" years old.")#prints without any error

age +=1
print(age)#increments the age

birthday = 1
age += birthday
print(age)#increments for every birthday
