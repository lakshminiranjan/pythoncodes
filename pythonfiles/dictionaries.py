#!/bin/python3
#Dictionaries in python-key/value pairs-{},We can have multiple values for a single key. 
marks = {"Telugu" : 90,"Hindi" : 92,"English" : 95,"Maths" :100}#Subject-key,marks-value.
print(marks)
VIT = {"B.Tech" :["CSE","ECE","Mech"],"M.Tech" :["Civil","EEE","Bioinf"]}
print(VIT)
VIT["Ph.D"] = ["Nano Technology"]#adds new key :value pair at the end of the dict.
print(VIT)
VIT.update({"School" : ["10th","11th","12th"]})
print(VIT)#works as same as the above functon.

#We can even update only the value of the key
marks["Telugu"] = 95
print(marks)

print(marks.get("Telugu"))#prints the value of the key constraint given in the brackets.
