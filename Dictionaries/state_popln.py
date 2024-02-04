#!/usr/bin/python3

"""
This challenge asks you to build a dictionary and use keys into that dictionary to extract
information. The information is given as a table of state names (keys) and the population
of each state (values). The program should allow the user to enter the name of a state.
If the state is found in the dictionary, then the program should report the population of
that state. If the state is not found, then the program should output a message like “Sorry,
but we do not have information for that state.” The program should run in a loop, allow
the user to enter any number of states, and then exit when the user presses Return (Mac)
or Enter (Windows). As of 2018, the data for the 12 states with the highest populations is
shown in Table 11-1.
"""
popultnDict = {'California': 39776830, 'Texas': 28704330, 'Florida': 21312211, 'New York': 19862512,\
        'Pennsylvania': 12823989, 'Illinois': 12768320, 'Ohio': 11694664, 'Georgia': 10545138,\
        'North Carolina': 10390149, 'Michigan': 9991177, 'New Jersey': 9032872, 'Virginia': 8525660}

user_input = input("Key in the state's name: ")

state = popultnDict.keys()
if user_input not in state:
    print('Sorry,but we do not have information for that state.')

else:
    print(popultnDict[user_input])


