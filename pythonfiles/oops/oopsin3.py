#!/bin/python3

class Laptop:
	def __init__(self,name,price):
		self.name = name
		self.price = price
		
a = Laptop("Dell",10000)
print(a.name)
print(a.price)
