#!/ussr/bin/env python3

"""
List: How to use individual value from a list.
Usage: Use of concatination to create a message based on 
values from the list
"""

Language = ['Python', 'Php', 'Java', 'JavaScript', 'Ruby']

message = "My favourite first language was " + Language[0].upper() + "."

print(message)
