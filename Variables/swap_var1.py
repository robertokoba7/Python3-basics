#!/usr/bin/env python3

"""Use of temporary variable to swap the 
variables x and y
"""

x,y = 20,30
tmp = None # assign None to tmp to avoid NameError.
tmp = x # THe value of var x is assigned to tmp leaving x empty.
x = y # The value of y now is assigned to the var x whch is empty
y = tmp # Var y now being empty is assigned the value stored temporarily in tmp

print(f'The value to x is: {x}')
print(f'The value to y is: {y}')

"""Point to note here.
    1.  the syntax 'x = 20, y = 30' is not allowed in Python for 
    simultaneous assignment to multiple variables. The correct 
    syntax for multiple assignments in Python is to use separate 
    statements or lines:
        x, y = 20, 30

    2. If you try to use the syntax 'x = 20, y = 30', Python will 
    interpret it differently. It will create a tuple with the 
    values '20' and 'y = 30', and then attempt to assign that tuple to 
    the variable 'x'. This is likely not what you intend, and it 
    will result in an error-SyntaxError. Therefore, it's essential to use 
    the correct syntax for multiple assignments.

    3. Note here we have used f-string in our print statement.
"""
