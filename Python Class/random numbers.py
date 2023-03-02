import random


x = random.randint(1,6)
y = random.random() #give us a arandom number between 0 and 1

mylist = ["pedra", "papel","tesoura"]

z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)


print(cards)