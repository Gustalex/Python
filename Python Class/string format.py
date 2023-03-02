# str. format() = optional metho that gives user more control when displaying  output 

animal = "cow"
item = "moon"

#print("The " + animal + " jumped over the "+ item )

#print("The {} jumped over the {}" .format(animal,item))

# the {} are a placeholder for a value or a variable 

#print("The {1} jumped over the {0}" .format(animal,item)) #positional argument 

#print("The {animal} jumped over the {moon}" .format(animal = "cow ",item = "moon")) # keyword argument 

#text = "The {} jumped over the {}"  ---> melhor forma de usar o str.format dentre os exemplos anteriores
#print(text.format(animal,item))


#name = "Guga"

#print("Heloo, my name is {}" .format(name))
#print("Heloo, my name is {:10}. Nice to meet you" .format(name))
#rint("Heloo, my name is {:<10}. Nice to meet you" .format(name))
#print("Heloo, my name is {:>10}. Nice to meet you" .format(name))
#print("Heloo, my name is {:^10}. Nice to meet you" .format(name))



number = 1000


#print("Th number pi is {:.2f}" .format(number))   # se fosse :.3f seriam os 3 primeiros decimais apos a virgula 
print("Th number is {:,}" .format(number)) # adciona a virgula 
print("Th number is {:b}" .format(number)) #transforma o numero em binario 
print("Th number is {:o}" .format(number)) #transforma o numero em octa 
print("Th number is {:x}" .format(number)) #transforma o numero em hexadecimal 
print("Th number is {:e}" .format(number)) #coloca o numero em notacao cientifica 


























