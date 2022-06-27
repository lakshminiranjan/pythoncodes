
#actually textbpresent in the file already gets erased and this text is overwritten IN THAT 
#write a file
# text = "Niranjan is great\nNizy is very silent\nNandu is a bad-boy\nNizy is so good that if mistake is done by nandu he excuses him"
text = "uh-oh! The text is over written"
with open("./files_in_python/test.txt",'w') as file:
    file.write(text)

#reading a file which is existing in the system
with open("./files_in_python/test.txt",'r') as file:
    print(file.read())

#appending text to existing file
appending_text = "\nN\nI\nR\nA\nN\nJ\nA\nN"
with open("./files_in_python/test.txt",'a') as file:
    file.write(appending_text)

#reading a file which is existing in the system after appending a text
with open("./files_in_python/test.txt",'r') as file:
    print(file.read())


'''
simple way to write and read files
text = "Niranjan"

with open('test.txt','w') as file:   ------ for appending a txt to file replace w with a
    file.write(text)

with open('test.txt','r') as file:
    print(file.read())


'''