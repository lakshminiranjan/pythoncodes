#delete a file
import os
import shutil

path = "./files_in_python/new_folder"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)#it is dangerous as it deletes all the files of the folders
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to delete the file")
except OSError:
    print("We can't use the above function to delete the non-empty folders")
else:
    print(path," was successfully deleted")