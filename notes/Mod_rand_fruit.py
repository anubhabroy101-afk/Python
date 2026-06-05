#Create a list of fruits and print a random fruit

import random

n = int(input("Enter the number of fruits: "))
fruits = []

for i in range(n):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

print("Fruits: ", fruits)
random_fruit = random.choice(fruits)
print("Random fruit: ", random_fruit)