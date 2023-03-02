# nested loop in general concept is having a loop inside another loop 
#       nested loops = The "inner loop" will finihsh all of it's interations before  
#                       finishing the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: ")) 
symbol = (input("Enter on symbol to use: "))

for i in range (rows):
    for j in range(columns):
        print(symbol, end="") # end="" is for not going to the next line 
    print()