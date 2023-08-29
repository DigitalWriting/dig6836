# make a new list called fruits
# remember lists are "zero-indexed"
fruits = ["apple","banana","orange"]
print (fruits[0]) # print out fruit in position 0 in fruits list (apple)
print (fruits[1]) # print out fruit in position 1 in fruits list (banana)
print (fruits[2]) # print out fruit in position 2 in fruits list (orange)

print ("-----------")

# you can also use a For loop to dynamically loop through and print out each item
for fruit in fruits:
    print(fruit)
    
print ("-----------")

# you can also use a For loop and range to dynamically loop through and print out each item in reverse order
num_of_fruits = len(fruits) # get the number of fruits in the list
for i in range(num_of_fruits):
    index = num_of_fruits - 1 - i # remember that i will increase by one each time through the loop
    print(fruits[index]) # print the current fruit at the index value of i

print ("-----------")

# if you want to randomly shuffle a list, that's easy too
from random import shuffle
shuffle(fruits)
for fruit in fruits:
    print(fruit)
