from cgitb import text



text  = "Have a nice day"


with open("C:\\Users\\alexa\OneDrive\\Área de Trabalho\\test.txt","a") as file:
    file.write(text)


#  "w" ----> write a file 
#  "a"  ----> append a file ----> escreve mais texto sem excluir os escritos anteriormente 
#  "r" -----> read a file 

