#!/bin/python3
#Inheritance amazing concept.
#Make sure we have both in the same directory.
from child import Child

class Parent(Child):
	pass#avoids the errors or we can say exceptions.

c = Child()
print(c.name)
print(c.age)
print(c.gender)
