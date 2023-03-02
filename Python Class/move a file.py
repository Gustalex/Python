import os 

source =  "C:\\Users\\alexa\\OneDrive\\Documentos\\license code win 11.txt"
destination = "C:\\Users\\alexa\\OneDrive\\Área de Trabalho\\license code win 11.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination) 
        print(source+" was moved")   
    
except FileNotFoundError:
    print(source+" was not found")
    