#!/usr/bin/env python3

"""Here am demostrating why storing data in data structure
like list is key as opposed to individual variable
consider: list named temp
"""
temp = [27,29,30,30,28,29,30] # recorded weekly temperature

# use min() function to find minimum temp within the week
minTemp = min(temp)

# print the output using 3 methods
# method 1: using f-string
print(f'The first day of the week recorded the minimun temperature of {minTemp}')

# method 2: using .format method
print('The first day of the week recorded the minimun temperature of {}'.format(minTemp))

# method 3:
print('The first day of the week recorded the minimun temperature of', minTemp) 

"""Let's check what happens when we use the individual variable to store the values.
we shall be forced to use the conditional statement if-elif-else
"""
tempDay1 = 27
tempDay2 = 29
tempDay3 = 30
tempDay4 = 30
tempDay5 = 28
tempDay6 = 29
tempDay7 = 30

minTemp = tempDay1

if tempDay2 < minTemp:
    minTemp = tempDay2

elif tempDay3 < minTemp:
    minTemp = tempDay3

elif tempDay4 < minTemp:
    minTemp = tempDay4

elif tempDay5 < minTemp:
    minTemp = tempDay5

elif tempDay6 < minTemp:
    minTemp = tempDay6

elif tempDay7 < minTemp:
    minTemp = tempDay7

print('The first day of the week recorded the minimun temperature of', minTemp)

"""Now imagine with no data structure like a List and we are to calculate a 
whole year temperarute? Quite chaotic indeed.
"""
