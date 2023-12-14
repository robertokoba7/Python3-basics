#!/usr/bin/env python3

"""make a list of the first 10 square 
using range() function
"""
# define an empty list
squares = []

#iterate over each values from 1 to 10
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
