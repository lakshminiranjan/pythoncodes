import random

x = random.randint(1,9)
y = random.random()#gives a random b/w 0 and 1

print(y)


#generating  a random string or data type from a string

myList = ['rock','paper','scissors']
z = random.choice(myList)#print a random choice from the list


cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)#shuffles and gives the random order of the deck of the cards

print(cards)