# dictionary = A chageable, unordered collection of unique key: value pairs
#               Fast because  they use hashing, allow us to acess a value quickly 

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "Brasil":"Brasilia",
            "Russia":"Moscou"}

capitals.update({"Germany":"Berlim"})
capitals.update({"USA":"Las vegas"})
capitals.pop("Russia")
capitals.clear()
#print(capitals["Brasil"])
#print(capitals.get("Alemanha"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key ,value)
