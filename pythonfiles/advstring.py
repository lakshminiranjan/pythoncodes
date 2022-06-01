#!/bin/python3
#Advanced Strings.
#In pyhton strings,lists and everything start with 0.
my_name = "Nizy"
print(my_name[0])#prints first letter of my_name.
print(my_name[-1])#prints the last letter of my_name


fact = "Nizy is a great hacker."
print(fact[:4])#prints the Nizy
print(fact.split())#prints a list which contains all the words of fact.

fact_split = fact.split()
fact_join = ' '.join(fact_split)#converts the list form into a normal sentence form.
print(fact_join)

quote = "HE said ,'give me all your money'"#max use double quotes.
sudheer = "He said,\"Sudheer is a good BGMI player\""#(\)gives us the way to print the statement without any errors.
print(quote+"\n"+sudheer)


too_much_space ="                                  Hello                     "
print(too_much_space.strip())#prints the word or sentence of the string without any spaces.

print("N" in "Nizy")#python checks whether N is there in the word or not and this is case sensitive.

letter = "N"
word = "Nizy"
print(letter.lower() in word.lower())#This lower() will convert all the capital letters so the o/p will be true.
#format use, in place of {}->movie name is going to be printed.
movie = "Gabbarsingh"
print("My fav movie is {}.".format(movie))#prints the same thing like we did in the cacatenation of strings.
