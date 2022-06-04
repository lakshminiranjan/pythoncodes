#!/bin/python3
'''
Reading files
If anything we update in the file-This will be even updated in when we run the python script.

Actually in linux 
countries_file = open("countries.txt","r")-This command will work fine and o/p will be true for the command-"print(countries_file.readable())"
but it is better to give the entire file location because some windows machines will not work at all with the above simple command so;
countries_file = open("/home/kali/Documents/pythonfiles/countries.txt","r")-This command will be perfect for everything.
readline()-This function will print the first element normally,if we use it again it will print the secong element this time.
readlines()-Helps to print everything in the form of list
readlines()[n]-prints the n-1 element from the list.
'''
countries_file = open("countries.txt",'r')#Just reading a file
print(countries_file.readable())#prints "True" if we are able to read the file.
for i in countries_file.readlines():#prints the first element of the text file.
	print(i)
countries_file.close()#Everytime we open something we have to close it. 
