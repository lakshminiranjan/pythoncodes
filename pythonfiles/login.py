#!/bin/python3
#for singup a new account
#printing a design or pattern
i = 0
while(i < 3):
	i+=1
	print(i * '*')

print("Create your account")
#printing samepattern in reverse
j = 4
while(j > 0):
	j-=1
	print(j * '*')

user = input('Enter username :')
paswd = input('Enter password :')

print('Your account has been created successfully')
print('Login Now')
#Logging in into the new account
user1 = input('Enter username :')
paswd1 = input('Enter password :')
#Verifying the login
if(user == user1 and paswd == paswd1):
	print("-" * 20)
	print("Welcome",user)
	print("-" * 20)
else:
	print('Creditionals are not correct')

