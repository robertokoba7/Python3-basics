#!/usr/bin/env python3

"""What is the effect of ommitting the [:] i.e the slice when copying a list"""

my_food = ["pizza", "cannolli", "broccoli", "coffee cake", "ice cream"]
friend_food =  my_food # By just ommiting the slice part([:]) in this line gave a different output

my_food.append("cake")
friend_food.append("KFC chicken")

print("My favo food is: ", my_food)
print("\nMy friend's favo food is: ", friend_food)

"""              Try It Yourself

4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

- Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.

- Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.

- Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
"""
print(f'\nThe first three items in the list are: ' + str(my_food[:3]))
print(f'\nThree items from the middle of the list are: ' + str(my_food[2:]))
print(f'\nThe last three items in the list are: ' + str(my_food[-3:]))

