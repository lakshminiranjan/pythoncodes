#!/bin/python3
#Conditinal statements(Think logically and get the logic),Consider all chances.
def drink(money):
	if money >= 2:
		return "You are welcome to buy a drink."
	else :
		return "Please bring the sufficient money."
print(drink(3))
print(drink(1))
print('\n')

def drink_alochol(age,money):
	if (age >= 21) and (money >= 5):
		return "You are eligible to drink."
	elif (age >= 21) and (money < 5):
		return "Come back with sufficient money."
	elif (age < 21) and (money >= 5):
		return "Nice try,Kid!"
	else :
		return "Sorry you are not eligible to drink the alocohol."
print(drink_alochol(21,5))
print(drink_alochol(21,4))
print(drink_alochol(20,5))
print(drink_alochol(20,2))
