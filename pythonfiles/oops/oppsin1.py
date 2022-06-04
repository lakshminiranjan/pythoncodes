#!/bin/python3
'''
Oops says that everything in the world is a Objects and claases.
Class-Class is a thing which defines the object.,Constructor of object,under class we have various objects
Python is a Object-oriented programming language
'''
class Your_info:
	def __init__(self,name,age):#(__init__(self,...,....) is common for everything to intialise.(self-this in java.)
		self.name = name
		self.age = age
		
		
#We are writing here the print statement of the java
name = input("Enter your name :")
age = int(input("Enter your age :"))
p1 = Your_info(name,age)#constructor in java-Classname()-and start letter should be true.
print(p1.name)
print(p1.age)
