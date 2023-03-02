
try:
    with open ("C:\\Users\\alexa\OneDrive\\Área de Trabalho\\license code win 11.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")