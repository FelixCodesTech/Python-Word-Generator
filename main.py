from random import *
from playsound import playsound

lenght = 5
quantity = 5
words = []

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowals = ['a', 'e', 'i', 'o', 'u']
vowalsConsonantsRatio = 1   # how many vowals per consonant

for round in range(quantity):
    word = ""
    for i in range(lenght):
        if randint(0, vowalsConsonantsRatio) == 0:
            word += choice(consonants)
        else:
            word += choice(vowals)

        #print(word)

    words.append(word)

print(f"These are the suggested words:\n")
for word in words:
    print(f"•{word}")

playsound("ding.mp3")