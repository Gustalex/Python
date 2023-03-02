# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
#name =  "Guga Santos"

#first_name = name[0:4] #o primeiro index é inclusivo e p segundo é exclusivo
#last_name = name[4:11]
#funky_name = name[0:11:3]
#full_name = first_name + last_name
#reversed_name = name [::-1]
#print(full_name)

#slice() function

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)
print(website1[slice])
print(website2[slice])