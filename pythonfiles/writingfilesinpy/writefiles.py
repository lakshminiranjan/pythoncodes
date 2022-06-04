#!/bin/python3
'''
Writing Files.
Note:After executing the python script only the "countries.txt" will be updated with new text
In Linux:
cat "filename.txt"-Will gives the info of the file

'''
con_file = open("countries.txt",'w')#'w' indicates writing a file.
con_file.write("Everything is erased.")#The countries that are already present in the file will be erased and this text will be shown
con_file.close()
#Creating a new file in the directory. 
new_file = open("newfile.txt",'w')
new_file.write("Created a new file")
new_file.close()
