# scope =  The region that a variable is recognized
#          A variable is only avaliable from inside in the region it is created 
#          A  global ond locally scope versions of a variable can be created

name = "Guga"  # Global scope (avaliable inside and outside functions)

def display_name():
    name = "Silva"  # local scope (avaliable only inside this function)
    print(name)
    
display_name()
print(name)