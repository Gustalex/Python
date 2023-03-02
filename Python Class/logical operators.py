# logical operators (and, or, not) = used to check if two or more contidional statements are true

temp =  float(input("What's the temperature outside?: "))

if temp >=0 and temp <= 30:
    print("The temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")
    
# o operador not, transforma tudo o que for true em false ou tudo o que for false em true, ou seja, os resultados dos prints se invertem
#if not(temp>= 0 and temp <=30):
#    print("The temperature is good today!")
#    print("Go outside!")
#elif not(temp < 0 or temp >30):
#    print("The temperature is bad today!")
#    print("Stay inside!")