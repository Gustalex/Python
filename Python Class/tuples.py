# tuple = collection which is ordered and unchangeable
#           used to group together related data 

student = ("Guga",19,"male")


print(student.count("Guga"))
print(student.index("male"))

for x in student:
    print(x)
if "Guga" in student:
    print("Guga is here!")