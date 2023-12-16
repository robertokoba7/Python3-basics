#!/usr/bin/env python3

my_food = ["githeri", "chapati", "rice", "pizza", "ugali"]
friends_food = my_food [:]

print("My fav food are: ", my_food)
print("\nMy friend's fav food are: ", friends_food)

"""To prove we have two different lists,
we add different foods to each list
"""
my_food.append("ice cream")
friends_food.append("coffee")

print("\nMy additonal favo food are: ", my_food)
print("\nMy friend's additional favo food are: ", friends_food)
