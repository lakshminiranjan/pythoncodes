#!/bin/python3
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

#We are going to del the class
try:
	p1 = Person('Bujji',2)
	del p1
	print(p1)
except NameError:#It should print a name error but I have cathced the name error at here.
	print("Alraedy deleted no tension")
