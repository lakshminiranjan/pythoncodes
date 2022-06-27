#copyfile()   = copies contents of a file
#copy()  = copyfile()+permission mode +  destination can be a directory
#copy2() = copy() +copies metadata (file's creation and modification times)


#all the three copyfile(),copy(),copy2() does the same thing
import shutil

shutil.copyfile("./files_in_python/test.txt", "./files_in_python/copy.txt")#source,destination
