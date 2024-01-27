#!/usr/bin/env python3
"""looping through all key-value pairs"""
lang = {
        'jack' : 'python',
        'jill' : 'java',
        'mark' : 'ruby',
        'jay': 'javascript'
        }

for name in sorted(lang.keys()):
    print(name.title() + ", thank you for taking the polls!")
