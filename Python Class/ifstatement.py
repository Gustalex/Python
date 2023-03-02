# if statement = a block of code that will execute if the condition is true 

age = float(input("How old are you?:"))

if age == 100:
    print("You are a century old!")
elif age >=18:
    print("You are an adult!")

elif age < 0:
    print("You haven't born yet")
else:
    print("You are an child!")
    