# copyfile() = copies contents of a file 
# copy() = copyfile() + permission mode + destinatuion can be a directory 
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("C:\\Users\\alexa\OneDrive\\Área de Trabalho\\test.txt","C:\\Users\\alexa\OneDrive\\Área de Trabalho\\copy.txt") #src,dst