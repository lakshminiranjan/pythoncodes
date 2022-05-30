#!/bin/python3
#Functions in python
print('The example of a simple function :')

def who_am_i():#This is a function(A mini program)
	name = "Niranjan"
	age = 20
	print("My name is "+name +"\nI am "+ str(age) +" years old.")

who_am_i()
#print(age)->this doesnt work at all as it is defined on who_am_i() function.

#adding parameters
def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x+y)
add(2,7)#user input working we can say

def mul(x,y):
	return x*y#just returns doent print the output,we can store the var using this "return"
print(mul(2,7))		

def sqrt_of_a_num(x):
	print(x ** 0.5)
sqrt_of_a_num(2)#returns in float type
def new_line():
	print('\n')
new_line()#prints a new line
