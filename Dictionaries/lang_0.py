#!/usr/bin/python3

"""looping through all values in a dict"""
lang = {
        'joe': 'python',
        'jill': 'java',
        'bob' : 'ruby',
        'jack': 'javascript'
        }
print("The following languages have been listed: ")
for language in lang.values():
    print(language.title())
