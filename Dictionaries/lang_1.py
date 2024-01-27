#!/usr/bin/python3

"""looping through all values in a dict"""
lang = {
        'joe': 'python',
        'jill': 'java',
        'bob' : 'ruby',
        'jack': 'javascript',
        'mike': 'python',
        'paul': 'java'

        }
print("The following languages have been listed: ")
for language in set(lang.values()):
    print(language.title())
