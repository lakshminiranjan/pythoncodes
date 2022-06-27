#moving a file
import os

source = "./files_in_python/copy.txt"
destination = "./files_in_python/folder/copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file existing with the same name")
    else:
        os.replace(source, destination)
        print(source,"was moved")
except FileNotFoundError:
    print(source,"was not found")    