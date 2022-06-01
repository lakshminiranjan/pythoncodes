#!/bin/python3
#List-have brackets []->"MUTABLE"
#everything starts with 0 in list
movies = ["Jalsa","F2","Gabbarsingh","Bahubali","RRR"]

print(movies[0])#prints jalsa movie  or prints the first item
print(movies[1])#This will return second item.
print(movies[1 : 3])#prints from F2 and gabbarsingh(like it prints item 1,2 but  it doesnt print item 3)
print(movies[0 : 5])#prints all items of the list
print(movies[0:])#prints everything after item 0 including 0.
print(movies[:4])#prints elements present before in the list excluding item 4.
print(movies[-1])#prints the last element likewise -2->prints thesecond last element.

print(len(movies))#prints the total no.of elements present in the list.
movies.append('F3')#appends at the end of the list.
print(movies)#The film or element willl be added at the end of the list.
movies.pop()#removes the very last element in the list.
print(movies)
movies.pop(0)#removes the very first element
print(movies)
movies.pop(3)#removes the fourth element of the list.
print(movies)
