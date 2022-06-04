#!/bin/python3
num1 = int(input("Enter first number :"))#taking input for 1 st number
num2 = int(input("Enter second number :"))#taking input for 2 nd number
op = input("Enter a operator :")#taking operator input from user
if(op == '+'):
	print(num1 + num2)#adding
elif(op == '-'):
	print(num1 - num2)#subtracting
elif(op == '*'):
	print(num1 * num2)#multiplying
elif(op == '/'):
	print(num1 / num2)#division(float o/p)
elif(op == '//'):
	print(num1 // num2)#division(int o/p)
elif(op == '**'):
	print(num1 ** num2)#num1 power num2
else:
	print("Invalid operation") 
